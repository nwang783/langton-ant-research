"""Independent no-solver enumeration after the separately verified LK dual caps.
Wake input is derived from literal104; no author history or edge generator used.
"""
from pathlib import Path
from itertools import product
from collections import defaultdict,Counter
import json,hashlib
R=Path(__file__).resolve().parents[1];D=R/'causal_reduction/unit_scale'
H=json.loads((R/'recovered_bundle/ant_global/root/standard.json').read_text())['word']
v=(1j,1,-1j,-1);p=0j;h=1;reads=defaultdict(list)
for t,c in enumerate(H):
 x,y=int(p.real),int(p.imag);reads[x-y,x%2].append((t-104*(x//2),c));h=(h+(1 if c=='R'else-1))%4;p+=v[h]
assert(p,h)==(2+2j,1)
wake=set()
for q,ts in reads.items():
 ts.sort();assert ts[0][1]=='R'and all(a[1]!=b[1]for a,b in zip(ts,ts[1:]));
 if len(ts)%2:wake.add(q)
ps=[complex(x,x+y-2)for y in range(4)for x in range(2)];idx={z:i for i,z in enumerate(ps)}
bound=json.loads((R/'audits/check_oblique_cylinder_flow_independent.json').read_text())['results'][0]
assert bound['certificate_sha256']==hashlib.sha256((D/'wake_return_flow_bounds_h4_off-2.json').read_bytes()).hexdigest()
caps=bound['site_visit_bounds'];assert caps==[0,1,2,3,3,2,1,0]and bound['total_period_bound']==12
bits=[int((int(z.real-z.imag),int(z.real)%2)in wake)for z in ps]
options=[]
for z,cap in zip(ps,caps):
 hh=[j for j in range(4)if(int(z.real+z.imag)+j)%2==1]
 options.append([s for n in range(cap+1)for s in product(hh,repeat=n)])
count=Counter();balanced=[]
for hs in product(*options):
 count['all_assignments']+=1;N=sum(map(len,hs))
 if not N:count['empty']+=1;continue
 incoming=defaultdict(list);outgoing=defaultdict(list)
 for i,s in enumerate(hs):
  for rank,hh in enumerate(s):
   incoming[i,hh].append((i,rank));turn=1 if(rank+bits[i])%2==0 else-1;outgoing[i,(hh+turn)%4].append((i,rank))
 successors={};ok=True
 # Process every incoming stream from its physical predecessor, including
 # outside-strip predecessors (which necessarily carry no events).
 for i,z in enumerate(ps):
  for hh in range(4):
   pred=z-v[hh];shift=int(pred.real)//2;rep=pred-2*shift*(1+1j);j=idx.get(rep)
   a=outgoing.get((j,hh),[]);b=incoming.get((i,hh),[])
   if len(a)!=len(b):ok=False;break
   for src,dst in zip(a,b):successors[src]=(dst,shift)
  if not ok:break
 if not ok or len(successors)!=N:continue
 # Edges leading out of the strip cannot appear in the permutation.
 if len({w for w,k in successors.values()})!=N:continue
 count['nonempty_balanced']+=1;unseen=set(successors);cycles=[]
 while unseen:
  first=min(unseen);u=first;cycle=[];winding=0
  while u in unseen:
   unseen.remove(u);nxt,k=successors[u];cycle.append((u,k));winding+=k;u=nxt
  assert u==first;cycles.append(dict(events=cycle,length=len(cycle),winding=winding))
 assert any(c['winding']==0 for c in cycles)
 balanced.append(dict(histories=hs,cycles=cycles))
assert count==dict(all_assignments=99225,empty=1,nonempty_balanced=2)
J=json.loads((D/'wake_return_fourrow_finite.json').read_text());assert bits==J['input']
assert sorted(tuple(tuple(h)for h,_ in e['histories'])for e in J['examples']['cycles'])==sorted(b['histories']for b in balanced)
for b in balanced:
 e=next(e for e in J['examples']['cycles']if tuple(tuple(h)for h,_ in e['histories'])==b['histories'])
 assert sorted((len(c),sum(k for u,k in c))for c in e['cycles'])==sorted((c['length'],c['winding'])for c in b['cycles'])
out=dict(status='PASS all cap-derived local histories; every nonempty ordinal-balanced assignment contains a zero-winding successor cycle',counts=dict(count),input=bits,caps=caps,balanced=balanced,author_result_sha256=hashlib.sha256((D/'wake_return_fourrow_finite.json').read_bytes()).hexdigest(),scope='Specified central four-row prepared104 cylinder, full drift(-2,-2), sector1, arbitrary outputs. No supplied cap or period bound beyond signed LK, no variable-width or nonperiodic-return exclusion.')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
