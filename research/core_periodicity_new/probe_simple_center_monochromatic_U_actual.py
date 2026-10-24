"""ONE bounded positive-discovery probe for simple-center monochromatic U.
Actual full literal prefix states, exact current identities/historical components,
exact nonadjacent closed-center-contact pruning. No-hit is UNKNOWN, no escalation.
"""
from pathlib import Path
from collections import Counter
import json,sys,time,hashlib
import search_literal_all_input_reconvergence as L
W=Path(__file__).resolve().parent;G=L.G
MAXDEPTH=int(sys.argv[1])if len(sys.argv)>1 else 14
MAXNODES=int(sys.argv[2])if len(sys.argv)>2 else 200000
OUT=W/'chronology_dcuv/simple_monochromatic_U_actual_probe_20261023_1645.json'
def sub(a,b):return a[0]-b[0],a[1]-b[1]
def det(a,b):return a[0]*b[1]-a[1]*b[0]
def base(a):return 0 if a in[0,1]else 4 if a in[4,5,6]else 7
def touches(p,q,z,w):
 d=sub(q,p);e=sub(w,z);r=sub(z,p);dd=det(d,e)
 if dd:
  s=det(r,e);t=det(r,d)
  if dd<0:dd=-dd;s=-s;t=-t
  return 0<=s<=dd and 0<=t<=dd
 return det(r,d)==0 and all(max(min(p[k],q[k]),min(z[k],w[k]))<=min(max(p[k],q[k]),max(z[k],w[k]))for k in[0,1])
def add_arcs(old,s,a,newstate):
 p=s[0];h=s[1];clock=s[-2];arcs=old.copy()
 for at in[base(a)]+['C']*G[a]['name'].count('C'):
  c=L.add((2*p[0],2*p[1]),L.rot((-1,-1),h));step=(2,2)if at in[0,'C']else(2,6)if at==4 else(0,8);e=L.add(c,L.rot(step,h));n=len(arcs)
  if arcs:assert tuple(arcs[-1]['end'])==c
  for prior in arcs[:-1]:
   if touches(tuple(prior['start']),tuple(prior['end']),c,e):return None
  arcs.append(dict(atom=at,head=[*p,h],entry_C=clock,start=c,end=e))
  if at=='C':p=L.add(p,L.rot((0,1),h));h=(h-1)%4;clock+=1
  else:p=L.add(p,L.rot(G[at]['endpoint'][:2],h))
 assert(p,h,clock)==(newstate[0],newstate[1],newstate[-2])
 return arcs
def score(s):
 p,h=s[0],s[1];tok=s[3];P=s[4];hits=Counter();live=Counter(L.find(P,z[-1])for z in tok.values())
 for x in G[7]['inputs']:
  q=L.add(p,L.rot(x,h))
  if q in tok:hits[L.find(P,tok[q][-1])]+=1
 return(max(hits.values(),default=0),sum(hits.values()),max(live.values(),default=0),-len(s[-3]))
start=time.time();stats=dict(max_packet_depth=MAXDEPTH,node_budget=MAXNODES,nodes=0,attempts=0,actual_literal_extensions=0,simple_extensions=0,contact_prunes=0,depth_counts=[0]*(MAXDEPTH+1),max_component_U_input_hits=0,first_types=[7,8,9],scope='Single bounded positive-discovery test only. No-hit UNKNOWN; no no-reachability theorem, no U1 model and no cap escalation.')
stack=[]
for a in[7,8,9]:
 t=L.advance(L.INIT,a,1000);ar=add_arcs([],L.INIT,a,t)
 assert ar is not None;stack.append((t,ar))
hit=None;hit_arcs=None;budget=False
while stack:
 if stats['nodes']>=MAXNODES:budget=True;break
 s,arcs=stack.pop();stats['nodes']+=1;d=len(s[-1]);stats['depth_counts'][d]+=1;statsscore=score(s);stats['max_component_U_input_hits']=max(stats['max_component_U_input_hits'],statsscore[0])
 last=s[-1][-1]
 if last['packet']in[7,8,9]and len(last['input_components'])==1:
  assert d>1 and not last['new_initial_roots'];hit=s;hit_arcs=arcs;break
 if d==MAXDEPTH:continue
 kids=[]
 for a in L.IDS:
  stats['attempts']+=1;t=L.advance(s,a,1000)
  if t is None:continue
  stats['actual_literal_extensions']+=1;aa=add_arcs(arcs,s,a,t)
  if aa is None:stats['contact_prunes']+=1;continue
  stats['simple_extensions']+=1;kids.append((score(t),a,t,aa))
 kids.sort(key=lambda z:(z[0],z[1]))
 for _,a,t,aa in kids:stack.append((t,aa))
 if stats['nodes']%10000==0:print(dict(nodes=stats['nodes'],depth=d,attempts=stats['attempts'],simple=stats['simple_extensions'],contact_prunes=stats['contact_prunes'],seconds=round(time.time()-start,2)),flush=True)
stats['seconds']=time.time()-start;stats['budget_exhausted']=budget
if hit:
 head,h,col,tok,P,roots,C,hist=hit;O=dict(status='ACTUAL_SIMPLE_CENTER_MONOCHROMATIC_U_COUNTERCONTROL',word=[r['packet']for r in hist],names=[r['name']for r in hist],entry_actual_board=sorted(L.K|set(roots)),entry_mass=5+len(roots),C=C,final_pose=[*head,h],target_input_component_count=len(hist[-1]['input_components']),beta=sum(r['beta_increment']for r in hist),history=hist,all_atomic_chords=hit_arcs,stats=stats)
else:O=dict(status='UNKNOWN_NO_HIT_IN_THIS_SINGLE_BOUNDED_DISCOVERY_PROBE',stats=stats)
O['dependencies']={str(p.relative_to(W)):hashlib.sha256(p.read_bytes()).hexdigest()for p in[W/'chronology_dcuv/literal_residual_geometry.json',W/'search_literal_all_input_reconvergence.py',Path(__file__).resolve()]}
OUT.write_text(json.dumps(O,indent=2)+'\n');print(json.dumps({k:v for k,v in O.items()if k not in['history','all_atomic_chords']},indent=2),flush=True)
