"""Exact local domination oracle for a max-plus height potential.

The state space for each query is finite. It includes every assignment to a
local square, not only random fields. A complete pass gives a sufficient
all-field certificate; a found assignment is a valid local constraint but
need not be a globally violating complete field.
"""
from pathlib import Path
from collections import deque
import json
import sys
import numpy as np
from probe import MACROS, PATTERNS, NVAR, rot

OFFSETS = [(dx,dy) for dy in range(-1,2) for dx in range(-1,2)]
ALL = (1 << PATTERNS)-1
ONES = [sum(1<<p for p in range(PATTERNS) if (p>>j)&1) for j in range(9)]

def filter_fixed(domain, cells, fixed):
    for j,p in enumerate(cells):
        if p in fixed:
            domain &= ONES[j] if fixed[p] else ALL ^ ONES[j]
    return domain

def solve_windows(windows, fixed):
    """Binary CSP by exact domain propagation and branching; no cutoff."""
    active = [(cells,filter_fixed(dom,cells,fixed)) for cells,dom in windows if dom != ALL]
    if any(not dom for _,dom in active):return None,1
    points = sorted({p for cells,dom in active for p in cells})
    ids = {p:i for i,p in enumerate(points)}
    cells = [[ids[p] for p in cc] for cc,d in active]
    domains = [d for cc,d in active]
    links=[[] for _ in points]
    for k,cc in enumerate(cells):
        for j,i in enumerate(cc):links[i].append((k,j))
    assign = [-1]*len(points)
    for p,b in fixed.items():
        if p in ids:assign[ids[p]]=int(b)
    nodes=0
    def dfs(domains,assign,queue):
        nonlocal nodes
        nodes+=1
        while queue:
            k=queue.pop()
            d=domains[k]
            for j,i in enumerate(cells[k]):
                if assign[i]>=0:d &= ONES[j] if assign[i] else ALL^ONES[j]
            if not d:return None
            domains[k]=d
            for j,i in enumerate(cells[k]):
                if assign[i]>=0:continue
                yes=d & ONES[j]
                if not yes:b=0
                elif yes==d:b=1
                else:continue
                assign[i]=b
                queue.extend(kk for kk,jj in links[i] if kk!=k)
        undecided=[(d.bit_count(),k) for k,d in enumerate(domains) if any(assign[i]<0 for i in cells[k])]
        if not undecided:return assign
        _,k=min(undecided)
        candidates=[i for i in cells[k] if assign[i]<0]
        i=max(candidates,key=lambda i:len(links[i]))
        for b in (0,1):
            aa=assign.copy();aa[i]=b
            result=dfs(domains.copy(),aa,[kk for kk,jj in links[i]])
            if result is not None:return result
        return None
    result=dfs(domains,assign,list(range(len(active))))
    if result is None:return None,nodes
    out=dict(fixed)
    out.update({p:result[i] for p,i in ids.items()})
    return out,nodes

def field_rep_at(assignment, origins):
    high={}
    for x,y in origins:
        p=sum(1<<j for j,(dx,dy) in enumerate(OFFSETS) if assignment.get((x+dx,y+dy),0))
        if p:high[p]=max(high.get(p,-10**9),y)
    return high

class Oracle:
    def __init__(self,radius=2,global_origins=False):
        self.radius=radius;self.contexts=[]
        for name,d in MACROS.items():
            for h in range(4):
                fixed={rot(p,h):1 for p in d['first_L']}
                fixed.update({rot(p,h):0 for p in d['first_R']})
                toggled={rot(p,h) for p in d['odd_visits']}
                affected=sorted({(x-dx,y-dy) for x,y in toggled for dx,dy in OFFSETS})
                full=[]
                for x,y in {(x-dx,y-dy) for x,y in fixed for dx,dy in OFFSETS}:
                    if all((x+dx,y+dy) in fixed for dx,dy in OFFSETS):full.append((x,y))
                known=field_rep_at(fixed,full)
                known[PATTERNS+h]=0
                global_set={(x+dx,y+dy) for x,y in fixed for dx in range(-radius,radius+1) for dy in range(-radius,radius+1)} if global_origins else set()
                queries=[]
                for a in affected:
                    origins=sorted(global_set | {(a[0]+dx,a[1]+dy) for dx in range(-radius,radius+1) for dy in range(-radius,radius+1)})
                    cc=[(a[0]+dx,a[1]+dy) for dx,dy in OFFSETS]
                    tm=sum(1<<j for j,p in enumerate(cc) if p in toggled)
                    central=filter_fixed(ALL,cc,fixed)
                    queries.append({'center':a,'origins':origins,'central_cells':cc,'toggle_mask':tm,'central_domain':central})
                end=rot(d['end_pose'][:2],h);eh=(h+d['end_pose'][2])%4
                origins=sorted(global_set | {(end[0]+dx,end[1]+dy) for dx in range(-radius-1,radius+2) for dy in range(-radius-1,radius+2)})
                queries.append({'center':end,'origins':origins,'head':PATTERNS+eh})
                self.contexts.append({'name':name,'heading':h,'fixed':fixed,'known':known,'queries':queries})

    def check(self,w,one_per_context=True):
        caps={cap:1|sum(1<<p for p in range(1,PATTERNS) if w[p]<=cap) for cap in range(int(w.min())-30,1)}
        cuts=[];stats={'contexts':len(self.contexts),'queries':0,'csp_calls':0,'nodes':0,'cuts':0}
        for ctx in self.contexts:
            fixed=ctx['fixed'];known=ctx['known']
            known_top=max(w[k]+v for k,v in known.items())
            broke=False
            for q in ctx['queries']:
                stats['queries']+=1
                a=q['center']
                if 'head' in q:
                    cases=[(int(w[q['head']]),None)]
                else:
                    buckets={}
                    for p in range(PATTERNS):
                        if not (q['central_domain']>>p)&1:continue
                        post=p^q['toggle_mask']
                        if not post:continue
                        v=int(w[post]);buckets[v]=buckets.get(v,0)|(1<<p)
                    cases=sorted(buckets.items(),reverse=True)
                for val,central_domain in cases:
                    height=a[1]+val
                    if known_top>=height:continue
                    windows=[]
                    for x,y in q['origins']:
                        cap=height-1-y
                        domain=ALL if cap>=0 else caps.get(cap,1)
                        cc=[(x+dx,y+dy) for dx,dy in OFFSETS]
                        if (x,y)==a and central_domain is not None:domain &= central_domain
                        windows.append((cc,domain))
                    stats['csp_calls']+=1
                    solution,nodes=solve_windows(windows,fixed);stats['nodes']+=nodes
                    if solution is None:continue
                    pre=field_rep_at(solution,q['origins'])
                    for k,y in known.items():pre[k]=max(pre.get(k,-10**9),y)
                    if 'head' in q:post={q['head']:a[1]}
                    else:
                        p=sum(1<<j for j,cell in enumerate(q['central_cells']) if solution.get(cell,0))
                        post={p^q['toggle_mask']:a[1]}
                    assert max(w[k]+y for k,y in pre.items()) < max(w[k]+y for k,y in post.items())
                    cuts.append({'macro':ctx['name'],'heading':ctx['heading'],'pre':pre,'post':post,
                                 'center':a,'assignment':[(x,y,b) for (x,y),b in sorted(solution.items())]})
                    stats['cuts']+=1
                    if one_per_context:broke=True;break
                if broke:break
        return cuts,stats

def relax_with_start(contexts,w,maxpasses=1000):
    arrays=[(np.array(list(c['pre'])),np.array(list(c['pre'].values())),np.array(list(c['post'])),np.array(list(c['post'].values()))) for c in contexts]
    for it in range(maxpasses):
        old=w.copy()
        for pi,py,qi,qy in arrays:
            top=np.max(w[pi]+py)
            w[qi]=np.minimum(w[qi],top-qy)
        if np.array_equal(w,old):return True,it+1
    return False,maxpasses

def main():
    here=Path(__file__).resolve().parent
    data=json.loads((here/'sample_potential.json').read_text())
    w=np.array(data['weights'],dtype=np.int64)
    radius=int(sys.argv[1]) if len(sys.argv)>1 else 2
    global_origins='--global' in sys.argv
    oracle=Oracle(radius,global_origins)
    cuts=[];log=[]
    maxrounds=int(sys.argv[2]) if len(sys.argv)>2 else 200
    success=False
    for it in range(maxrounds):
        new,stats=oracle.check(w)
        if it<10 or it%10==9 or not new:print({'round':it,'minimum':int(w.min()),'head':w[PATTERNS:].tolist(),**stats},flush=True)
        log.append({'round':it,'minimum':int(w.min()),'head':w[PATTERNS:].tolist(),**stats})
        if not new:success=True;break
        cuts.extend(new)
        stable,passes=relax_with_start(cuts,w)
        if not stable:
            print('Sampled constraints did not stabilize',flush=True);break
    out={'certificate_found':success,'radius':radius,'global_origins':global_origins,'weights':w.tolist(),'log':log,'cuts':cuts}
    (here/('global_oracle_result.json' if global_origins else 'exact_oracle_result.json')).write_text(json.dumps(out,indent=2)+'\n')
    print({'certificate_found':success,'cuts':len(cuts),'minimum':int(w.min()),'head':w[PATTERNS:].tolist()},flush=True)

if __name__=='__main__':main()
