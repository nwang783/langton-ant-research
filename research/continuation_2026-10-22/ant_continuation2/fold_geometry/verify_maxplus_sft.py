"""Exact finite-field verifier for a directional max-plus ant potential.

The candidate has 512 pattern entries (zero is ignored) and either four head
weights or four head weights for each actual history port.
For an integer K, subtract K from all y coordinates.  The sublevel E <= 0 is
then a finite-height column SFT above an unconstrained lower half-plane.
Trimming its de Bruijn graph to paths from 00 back to 00 makes the exterior
quantification exactly that of finite black fields, rather than local boxes.

This verifier is independent of the parent's local-domination CSP.  It either
checks every relevant macro/head-height case or returns a literal finite-field
counterexample.  No sampled contexts are used.
"""
from pathlib import Path
from collections import defaultdict, deque
import argparse
import hashlib
import json

ROOT = Path(__file__).resolve().parents[2]
DATA = json.loads((ROOT/'ant_continuation/factor_language/five_macro_footprints.json').read_text())
DIRS = ((0,1),(1,0),(0,-1),(-1,0))


def rot(p,h):
    x,y=p
    return ((x,y),(y,-x),(-x,-y),(-y,x))[h]


def head_index(h,port=None):
    return 512+h if port is None else 512+4*port+h


def value(black,pose,w,port=None):
    centers={(x-dx,y-dy) for x,y in black for dx in (-1,0,1) for dy in (-1,0,1)}
    out=pose[1]+w[head_index(pose[2],port)]
    for x,y in centers:
        mask=sum(1<<((dy+1)*3+dx+1) for dy in (-1,0,1) for dx in (-1,0,1)
                 if (x+dx,y+dy) in black)
        assert mask
        out=max(out,y+w[mask])
    return out


def context_data(path,use_ports=False):
    """Load the earlier after-marker context export as physical templates.

    The fixed colors are optionally enlarged to all recorded history colors;
    the latter option is implemented by a separate full-context exporter.
    Macro first-read colors are always retained so every counterexample can be
    checked by literal execution of the entire word.
    """
    raw=json.loads(Path(path).read_text())
    M='LLLLRLRRRRLR'
    out={}
    for c in raw['contexts']:
        name=c['macro'];before=DATA[name]['word'];assert before.startswith(M)
        word=before[len(M):]+M
        x=y=h=0;first={};last={};odd=set()
        for letter in word:
            p=x,y;assert last.get(p)!=letter
            first.setdefault(p,letter);last[p]=letter;odd.symmetric_difference_update({p})
            h=(h+(1 if letter=='R' else -1))%4
            dx,dy=DIRS[h];x+=dx;y+=dy
        black=set(map(tuple,c['initial_black']))|{p for p,v in first.items() if v=='L'}
        white=set(map(tuple,c['initial_white']))|{p for p,v in first.items() if v=='R'}
        assert not black&white and odd==set(map(tuple,c['toggled']))
        assert [x,y,h]==c['end_pose']
        out['context_'+str(c['id'])]={'word':word,'first_L':sorted(black),'first_R':sorted(white),
            'odd_visits':sorted(odd),'end_pose':[x,y,h],'macro_type':name}
    if use_ports:
        expanded={}
        for i,e in enumerate(raw['edges']):
            d=out['context_'+str(e['context'])].copy()
            d['source']=e['source'];d['target']=e['target']
            expanded['edge_'+str(i)]=d
        return expanded
    return out


class BoundarySFT:
    def __init__(self,w,data=None):
        self.w=w
        self.data=DATA if data is None else data
        # A topmost black cell at Y contributes through a center at Y+1,
        # with a nonzero bottom-row mask, so Y <= -1-min(w[1:8]).
        # Centers at y <= -max(w) impose no restrictions.
        self.lo=-max(w[1:512])
        self.hi=-1-min(w[1:8])
        self.height=max(0,self.hi-self.lo+1)
        if self.height>30:
            raise ValueError('Strip height exceeds the targeted search cap')
        self.alphabet=range(1<<self.height)
        self.adj=defaultdict(list)
        self.rev=defaultdict(list)
        self.allowed=set()
        # Grow the three-column window one horizontal row at a time.  Each
        # completed 3x3 patch is checked immediately.  This enumerates the same
        # finite truth table as all 2^(3*height) triples, but prunes forbidden
        # partial windows before materializing the exponential alphabet cube.
        partial=[(0,0,0,0,0)]
        for j in range(self.height+2):
            nxt=[]
            for a,b,c,r0,r1 in partial:
                for r2 in (range(8) if j<self.height else (0,)):
                    mask=r0|(r1<<3)|(r2<<6)
                    if j>=2 and mask and self.lo+j-1+self.w[mask]>0:
                        continue
                    aa=a|((r2&1)<<j) if j<self.height else a
                    bb=b|(((r2>>1)&1)<<j) if j<self.height else b
                    cc=c|(((r2>>2)&1)<<j) if j<self.height else c
                    nxt.append((aa,bb,cc,r1,r2))
            partial=nxt
            if len(partial)>1000000:
                raise ValueError('More than one million partial strip triples')
        for a,b,c,_,_ in partial:
            self.allowed.add((a,b,c))
            self.adj[(a,b)].append((b,c))
            self.rev[(b,c)].append((a,b))
        self.left_parent=self.bfs(self.adj)
        self.right_next=self.bfs(self.rev)
        self.states=set(self.left_parent)&set(self.right_next)
        self.edges={u:[v for v in self.adj[u] if v in self.states] for u in self.states}

    @staticmethod
    def bfs(graph):
        parent={(0,0):None}
        queue=deque([(0,0)])
        while queue:
            u=queue.popleft()
            for v in graph[u]:
                if v not in parent:
                    parent[v]=u
                    queue.append(v)
        return parent

    def triple_legal(self,cols):
        for cy in range(self.lo+1,self.hi+2):
            mask=0
            for dx,col in enumerate(cols):
                for dy,y in enumerate(range(cy-1,cy+2)):
                    if self.lo<=y<=self.hi and col>>(y-self.lo)&1:
                        mask |= 1<<(dy*3+dx)
            if mask and cy+self.w[mask]>0:
                return False
        return True

    def finite_columns(self,start,cols):
        prefix=[]
        u=start
        while self.left_parent[u] is not None:
            prefix.append(u[1])
            u=self.left_parent[u]
        prefix.reverse()
        out=[0,0]+prefix+cols
        u=(out[-2],out[-1])
        while self.right_next[u] is not None:
            u=self.right_next[u]
            out.append(u[1])
        assert out[:2]==[0,0] and out[-2:]==[0,0]
        return out,len(prefix)

    def case_signature(self,name,h,y0):
        """Exact sublevel-set equivalence, ignoring unrestricted lower rows.

        Horizontal translation does not change the potential.  Two templates
        with equal signatures therefore have exactly the same finite-strip
        realizations and violation flag, even if their lower history differs.
        """
        d=self.data[name]
        fixed={}
        for cells,bit in ((d['first_L'],1),(d['first_R'],0)):
            for p in cells:
                x,y=rot(p,h);y+=y0
                if bit and y>self.hi:
                    return ('infeasible',)
                if self.lo<=y<=self.hi:
                    mask,ones=fixed.get(x,(0,0));b=1<<(y-self.lo)
                    fixed[x]=(mask|b,ones|(b if bit else 0))
        flips=defaultdict(int);outside=False
        for p in d['odd_visits']:
            x,y=rot(p,h);y+=y0
            if y>self.hi:outside=True
            if self.lo<=y<=self.hi:flips[x]|=1<<(y-self.lo)
        ey=rot(d['end_pose'][:2],h)[1]
        eh=(h+d['end_pose'][2])%4
        headbad=y0+ey+self.w[head_index(eh,d.get('target'))]>0
        shift=min(set(fixed)|set(flips),default=0)
        return (tuple(sorted((x-shift,m,b) for x,(m,b) in fixed.items())),
                tuple(sorted((x-shift,b) for x,b in flips.items())),outside,headbad)

    def case_shift(self,name,h,y0):
        d=self.data[name]
        points=[rot(p,h) for key in ('first_L','first_R','odd_visits') for p in d[key]]
        return min((x for x,y in points if self.lo<=y+y0<=self.hi),default=0)

    def literal_witness(self,name,h,y0,black):
        d=self.data[name]
        firstL={(a,b+y0) for a,b in (rot(p,h) for p in d['first_L'])}
        firstR={(a,b+y0) for a,b in (rot(p,h) for p in d['first_R'])}
        toggled={(a,b+y0) for a,b in (rot(p,h) for p in d['odd_visits'])}
        ex,ey=rot(d['end_pose'][:2],h)
        end=(ex,ey+y0,(h+d['end_pose'][2])%4)
        assert firstL<=black and not firstR&black
        pre=value(black,(0,y0,h),self.w,d.get('source'))
        post=value(black^toggled,end,self.w,d.get('target'))
        assert pre<=0<post,(pre,post,name,h,y0)
        actual=set(black);x=0;y=y0;hh=h
        for i,c in enumerate(d['word']):
            assert ((x,y) in actual)==(c=='L'),(i,c,(x,y))
            actual.symmetric_difference_update({(x,y)})
            hh=(hh+(1 if c=='R' else -1))%4
            dx,dy=DIRS[hh];x+=dx;y+=dy
        assert (x,y,hh)==end and actual==black^toggled
        return {'status':'counterexample','macro':name,'heading':h,'start_y':y0,
                'initial_black':sorted(black),'pre_value':pre,'post_value':post,
                'post_head':end,'top_strip_rows':[self.lo,self.hi]}

    def transfer_witness(self,name,h,y0,old):
        dx=self.case_shift(name,h,y0)-self.case_shift(old['macro'],old['heading'],old['start_y'])
        black={(x+dx,y) for x,y in old['initial_black'] if y>=self.lo}
        for p in self.data[name]['first_L']:
            x,y=rot(p,h);y+=y0
            if y<self.lo:black.add((x,y))
        return self.literal_witness(name,h,y0,black)

    def check(self,name,h,y0):
        d=self.data[name]
        firstL={(a,b+y0) for a,b in (rot(p,h) for p in d['first_L'])}
        firstR={(a,b+y0) for a,b in (rot(p,h) for p in d['first_R'])}
        toggled={(a,b+y0) for a,b in (rot(p,h) for p in d['odd_visits'])}
        ex,ey=rot(d['end_pose'][:2],h)
        end=(ex,ey+y0,(h+d['end_pose'][2])%4)
        if y0+self.w[head_index(h,d.get('source'))]>0:
            raise AssertionError('Inadmissible initial head height')
        if any(y>self.hi for x,y in firstL):
            return {'status':'infeasible precondition'}
        required={}
        flips=defaultdict(int)
        for cells,bit in ((firstL,1),(firstR,0)):
            for x,y in cells:
                if self.lo<=y<=self.hi:
                    fixed,ones=required.get(x,(0,0))
                    p=1<<(y-self.lo)
                    required[x]=(fixed|p,ones|(p if bit else 0))
        for x,y in toggled:
            if self.lo<=y<=self.hi:
                flips[x] |= 1<<(y-self.lo)
        outside_bad=any(y>self.hi for x,y in toggled)
        head_bad=end[1]+self.w[head_index(end[2],d.get('target'))]>0
        xs=set(required)|set(flips)
        a=min(xs,default=0)-2
        b=max(xs,default=0)+2
        # (last two pre-columns, seen a postcondition failure) ->
        # (initial state, complete chosen finite window columns).
        current={(u,bool(outside_bad or head_bad)):(u,[]) for u in self.states}
        for x in range(a,b+1):
            nxt={}
            fixed,ones=required.get(x,(0,0))
            for (u,bad),(start,cols) in current.items():
                for v in self.edges[u]:
                    c=v[1]
                    if c&fixed != ones:
                        continue
                    post=(u[0]^flips[x-2],u[1]^flips[x-1],c^flips[x])
                    nb=bad or post not in self.allowed
                    key=(v,nb)
                    if key not in nxt:
                        nxt[key]=(start,cols+[c])
            current=nxt
            if not current:
                return {'status':'infeasible precondition'}
        for (u,bad),(start,cols) in current.items():
            if not bad:
                continue
            allcols,prefixlen=self.finite_columns(start,cols)
            x0=a-prefixlen-2
            black={(x,y) for x,y in firstL if y<self.lo}
            for i,c in enumerate(allcols):
                black.update((x0+i,self.lo+j) for j in range(self.height) if c>>j&1)
            return self.literal_witness(name,h,y0,black)
        return {'status':'verified'}


def run(w,stop_first=True,data=None,expand_counterexamples=False):
    data=DATA if data is None else data
    s=BoundarySFT(w,data)
    summary={'strip_rows':[s.lo,s.hi],'strip_alphabet':len(s.alphabet),
             'raw_triples':len(s.allowed),'trimmed_states':len(s.states),
             'trimmed_edges':sum(map(len,s.edges.values())),'checked':0,
             'feasible_cases':0,'unique_strip_cases':0,'counterexamples':[]}
    seen={}
    for name,d in data.items():
        for h in range(4):
            ty=max(rot(p,h)[1] for p in d['odd_visits'])
            ey=rot(d['end_pose'][:2],h)[1]
            eh=(h+d['end_pose'][2])%4
            low=min(s.lo-ty,1-ey-w[head_index(eh,d.get('target'))])
            high=-w[head_index(h,d.get('source'))]
            for y0 in range(low,high+1):
                signature=s.case_signature(name,h,y0)
                if signature in seen:
                    summary['checked']+=1
                    old=seen[signature]
                    summary['feasible_cases']+=old['status']!='infeasible precondition'
                    if expand_counterexamples and old['status']=='counterexample':
                        summary['counterexamples'].append(s.transfer_witness(name,h,y0,old))
                    continue
                result=s.check(name,h,y0)
                seen[signature]=result
                summary['unique_strip_cases']+=1
                summary['checked']+=1
                if result['status']!='infeasible precondition':
                    summary['feasible_cases']+=1
                if result['status']=='counterexample':
                    summary['counterexamples'].append(result)
                    if stop_first:
                        summary['status']='refuted by an exact finite field'
                        return summary
    summary['status']=('refuted by exact finite fields' if summary['counterexamples'] else
                       'verified for every finite field and every feasible five-macro transition')
    return summary


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--weights',default=str(ROOT/'ant_continuation2/maxplus/sample_potential.json'))
    p.add_argument('--output',default=str(Path(__file__).with_name('maxplus_sft_verification.json')))
    p.add_argument('--all',action='store_true')
    p.add_argument('--contexts')
    p.add_argument('--port-head',action='store_true')
    args=p.parse_args()
    raw=Path(args.weights).read_bytes()
    w=json.loads(raw)['weights']
    assert len(w)>=516 and (len(w)-512)%4==0 and all(isinstance(x,int) for x in w)
    data=None if args.contexts is None else context_data(args.contexts,args.port_head)
    report=run(w,not args.all,data)
    report['candidate_sha256']=hashlib.sha256(raw).hexdigest()
    report['weights']=w
    Path(args.output).write_text(json.dumps(report,indent=2)+'\n')
    concise={k:v for k,v in report.items() if k not in ('weights','counterexamples')}
    concise['counterexample_count']=len(report['counterexamples'])
    concise['first_counterexample']=report['counterexamples'][:1]
    print(json.dumps(concise,indent=2))


if __name__=='__main__':main()
