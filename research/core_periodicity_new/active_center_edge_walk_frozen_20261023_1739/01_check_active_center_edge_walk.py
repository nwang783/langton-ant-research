"""Eight local fine-step checks and exact literal atomic edge walks."""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib
R=Path(__file__).resolve().parent;GP=R/'chronology_dcuv/literal_residual_geometry.json';G=json.load(open(GP))['geometry']
K={(-1,-1),(-1,0),(0,-1),(0,0),(1,0)};c=(F(-1,2),F(-1,2));STEPS=((0,1),(1,0),(0,-1),(-1,0))
def rot(p,h):
 x,y=p;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(p,q):return p[0]+q[0],p[1]+q[1]
def sub(p,q):return p[0]-q[0],p[1]-q[1]
def edge(q,sigma):
 v=(F(1,2),F(1,2))if(sum(q)-sigma)%2==0 else(F(1,2),F(-1,2))
 return frozenset((add(q,v),sub(q,v)))
local=[]
for h in range(4):
 p=(0,0);sigma=h%2;z=rot(c,h);d=rot((1,1),h)
 assert edge(p,sigma)==frozenset((z,add(z,d)))
 star={edge(rot(q,h),sigma)for q in K-{(1,0)}}
 assert star=={frozenset((z,add(z,rot((1,1),k))))for k in range(4)}
 bud=edge(rot((1,0),h),sigma)
 assert bud==frozenset((add(z,d),add(add(z,d),rot((1,1),h+1))))
 for turn in 'LR':
  H=(h+(-1 if turn=='L'else 1))%4;P=STEPS[H];Z=add(P,rot(c,H));D=rot((1,1),H)
  assert Z==(z if turn=='L'else add(z,d))
  assert D==rot(d,3 if turn=='L'else 1)
  assert(sum(P)+H)%2==sigma
  local.append(dict(heading=h,turn=turn,center_displacement=sub(Z,z),pointer_displacement=D))
D=G[0]['word'];C=G[1]['word'][len(D):];words={'D':D,'V':G[4]['word'],'U':G[7]['word'],'C':C};traces={}
for name,word in words.items():
 p=(0,0);h=0;z=c;occupied=set();required={};r_vertices=[z];allreads=[]
 for tick,turn in enumerate(word):
  e=edge(p,0);assert z in e
  if p not in required:required[p]=turn=='L'
  H=(h+(-1 if turn=='L'else 1))%4;P=add(p,STEPS[H]);Z=add(P,rot(c,H))
  assert Z==(z if turn=='L'else next(v for v in e if v!=z))
  if turn=='R':r_vertices.append(Z)
  allreads.append(dict(tick=tick,turn=turn,head=p,entry_heading=h,edge=sorted(e),center_before=z,center_after=Z))
  p,h,z=P,H,Z
 traces[name]=dict(raw_length=len(word),R_traversals=word.count('R'),L_deletions=word.count('L'),exit_pose=(*p,h),R_walk_relative_to_entry=[sub(v,c)for v in r_vertices],all_reads=allreads)
assert traces['D']['R_walk_relative_to_entry']==[(0,0),(1,1),(2,2),(3,1),(2,0),(1,1)]
assert (0,1)not in [tuple(r['head'])for r in traces['D']['all_reads']]
O=dict(status='AUTHOR_EXACT_ACTIVE_VERTEX_EDGE_TOGGLE_FORMULATION',scope='Physical fine-step coordinate equivalence and explicit marked-core ports only. No residual incidence embedding or fine-walk simplicity.',local_eight_cases=local,atomic_traces=traces,dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in(GP,Path(__file__).resolve())})
def encode(x):
 if isinstance(x,F):return int(x)if x.denominator==1 else str(x)
 if isinstance(x,(tuple,list)):return[encode(z)for z in x]
 if isinstance(x,dict):return{k:encode(z)for k,z in x.items()}
 return x
(R/'chronology_dcuv/active_center_edge_walk.json').write_text(json.dumps(encode(O),indent=2)+'\n')
print(json.dumps({a:{k:v for k,v in r.items()if k not in('all_reads','R_walk_relative_to_entry')}for a,r in traces.items()}))
