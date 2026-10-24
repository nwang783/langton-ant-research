"""Independent full-prefix cell-graph check of the incremental departure monitor.

No author geometry, graph update, generator or control is imported.  Random
histories satisfy the physical incoming/outgoing axis and expose both ports,
but are NOT claimed port-balanced ant fronts.  The reference rebuilds every
processed physical dependency graph from its original full history.
"""
from pathlib import Path
from random import Random
from collections import defaultdict
import importlib.util, json, hashlib

ROOT=Path(__file__).resolve().parents[1]
P=ROOT/'periodic_classification_new/first_departure_backbone_frontier.py'
spec=importlib.util.spec_from_file_location('candidate',P)
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
D=(1j,1,-1j,-1);rng=Random(731993)

class Physical:
    def __init__(self,a,b):self.a=a;self.b=b
    def point(self,x,y):return complex(x,y+self.b*x//self.a)
    def reduce(self,z):
        shift=int(z.real)//self.a;x=int(z.real)-shift*self.a
        return (x,int(z.imag)-shift*self.b-self.b*x//self.a),shift
    def splice_arcs(self,p):
        out=[]
        for row in (0,1):
            for x in range(self.a):
                q=self.point(x,p+row)
                for h,d in enumerate(D):
                    if h%2!=(int(q.real+q.imag)%2):continue
                    (xx,yy),k=self.reduce(q+d);rr=yy-p
                    if 0<=rr<=1 and not(row==rr==0):out.append((row,x,rr,xx,h,k))
        return out

def reference(history,g,top,cap,row0=0):
    nodes={(x,y)for y in range(top+1)for x in range(g.a)if history[y][x]['h']}
    parent={};neighbors=defaultdict(set)
    for v in nodes:
        x,y=v;d=(history[y][x]['h'][0]+1)%4
        (xx,yy),k=g.reduce(g.point(x,row0+y)+D[d]);u=(xx,yy-row0)
        if u not in nodes:continue
        hh=history[u[1]][u[0]]['h']
        rank=next(j for j,t in enumerate(hh)if t==d)
        parent[v]=(u,k,0 if rank==0 else 4*rank-2)
        neighbors[u].add(v);neighbors[v].add(u)
    unseen=set(nodes);answer=[];bound=0;counterflow=2*max(abs(g.a),abs(g.b))
    while unseen:
        start=min(unseen);stack=[start];component=set()
        while stack:
            v=stack.pop()
            if v in component:continue
            component.add(v);stack.extend(neighbors[v]-component)
        unseen-=component
        roots=component-parent.keys();front=sorted(v for v in component if v[1]==top)
        if roots:
            assert len(roots)==1
            root=next(iter(roots))
            if root not in front:return None,0,0
            entries=[]
            for v in front:
                pos=v;wind=cost=length=0;seen=set()
                while pos!=root:
                    assert pos not in seen;seen.add(pos)
                    pos,k,c=parent[pos];wind+=k;cost+=c;length+=1
                entries.append((v[0],(-wind)%3,min(cap,cost),min(cap,length)))
            answer.append((root[0],tuple(entries)))
        else:
            pos=start;order=[];seen={}
            while pos not in seen:
                seen[pos]=len(order);order.append(pos);pos=parent[pos][0]
            cycle=order[seen[pos]:]
            if sum(parent[v][1]for v in cycle)!=-1:return None,0,0
            bound=max(bound,min(cap,sum(parent[v][2]for v in cycle)))
            counterflow+=len(cycle)+2*max(abs(g.a),abs(g.b))
            if front:answer.append((-1,tuple((x,0,0,0)for x,y in front)))
    return tuple(sorted(answer,key=lambda z:z[1][0][0])),bound,min(cap,counterflow)

counts=defaultdict(int);by_drift={}
for a,b in ((2,0),(4,0),(6,0),(3,1),(3,-1),(4,2),(4,-2),(2,2),(2,-2)):
    local=defaultdict(int);g=Physical(a,b)
    for trial in range(500):
        height=rng.randrange(3,11);cap=rng.choice((1,3,7,16,31,64,120,512));history=[]
        for y in range(height):
            row=[]
            for x in range(a):
                q=g.point(x,y);axis=1-int(q.real+q.imag)%2
                allowed=[h for h in (axis,axis+2)if 0<=g.reduce(q+D[(h+1)%4])[0][1]<height]
                assert allowed
                hs=[rng.choice(allowed)]
                hs.extend(rng.choice((axis,axis+2))for _ in range(rng.randrange(1,8)))
                while len(set(hs))<2:
                    hs.append(rng.choice((axis,axis+2)))
                row.append({'h':tuple(hs)})
            history.append(row)
        state=();old=[{'h':()}for _ in range(a)];bound=0;flow=min(cap,2*max(abs(a),abs(b)))
        for y,new in enumerate(history):
            actual,debt,increment,reason=module.transition(state,old,new,(y-1)%2,g,cap)
            expected,eb,ef=reference(history,g,y,cap)
            assert (reason is None)==(expected is not None),(a,b,trial,y,reason,expected)
            local['prefixes']+=1
            if reason:
                local['rejected']+=1;break
            bound=max(bound,debt);flow=min(cap,flow+increment);assert (bound,flow)==(eb,ef),(a,b,trial,y,bound,eb,flow,ef)
            norm=tuple((rt,tuple((c,0,0,0)if rt<0 else(c,w,z,l)for c,w,z,l in es))for rt,es in actual)
            assert norm==expected,(a,b,trial,y,norm,expected)
            local['accepted']+=1;local['cyclic_frontiers']+=any(rt<0 for rt,es in actual)
            state=actual;old=new
    by_drift[str((a,b))]=dict(local)
    for k,v in local.items():counts[k]+=v
positives=[]
word=(ROOT/'word_stabilization/standard_word.txt').read_text().strip()
for copies in (1,2,3):
    for sign in (1,-1):
        a=2*copies;b=sign*a;period=104*copies;g=Physical(a,b)
        q=-1+0j if sign==1 else 0j;h=1j if sign==1 else 1;events=defaultdict(list)
        for t,turn in enumerate(word*copies):
            (x,y),k=g.reduce(q);events[x,y].append((t-k*period,D.index(h),turn))
            h*=(-1j if turn=='R'else 1j);q+=h
        lo=min(y for x,y in events)-1;hi=max(y for x,y in events)+1;history=[]
        for y in range(lo,hi+1):
            row=[]
            for x in range(a):
                ev=sorted(events[x,y]);assert all(turn==('R'if j%2==0 else'L')for j,(t,hh,turn)in enumerate(ev))
                row.append({'h':tuple(hh for t,hh,turn in ev)})
            history.append(row)
        for cap in (16,64,120,512):
            state=();bound=0;flow=min(cap,2*max(abs(a),abs(b)));old=[{'h':()}for _ in range(a)];cyclic=0
            for y,new in enumerate(history):
                actual,debt,increment,reason=module.transition(state,old,new,(lo+y-1)%2,g,cap)
                expected,eb,ef=reference(history,g,y,cap,lo)
                assert reason is None and expected is not None
                bound=max(bound,debt);flow=min(cap,flow+increment);assert (bound,flow)==(eb,ef) and max(bound,flow)<=period
                norm=tuple((rt,tuple((c,0,0,0)if rt<0 else(c,w,z,l)for c,w,z,l in es))for rt,es in actual)
                assert norm==expected
                cyclic+=any(rt<0 for rt,es in actual);state=actual;old=new
            assert state==() and bound>0 and cyclic>0
            positives.append(dict(period=period,drift=[a,b],cap=cap,period_debt=bound,counterflow_bound=flow,cyclic_frontiers=cyclic))
result={'status':'PASS independent physical-coordinate full-prefix graph reconstruction',
        'graphs':4500,'counts':dict(counts),'by_drift':by_drift,
        'nonvacuous_actual_standard_controls':positives,
        'module_sha256':hashlib.sha256(P.read_bytes()).hexdigest(),
        'scope':'Graph-monitor implementation control; random histories are not asserted ant fronts. Analytic simulation and any complete exclusion graph remain separate obligations.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
