"""Exact all-age first-retirement/white-blocker theorem; no word search.

Independently regenerates literal raw+marker contexts and output graphs,
exhausts all input-slot placements, and directly replays the signed finite
19-cell control. No historical-component or global U-budget assertion.
"""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import hashlib, json

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
GP=ROOT/'chronology_dcuv/literal_residual_geometry.json'
J=json.loads(GP.read_text()); G=J['geometry']; IDS=(0,1,4,5,6,7,8,9)
K=set(map(tuple,J['core'])); VEC=((0,1),(1,0),(0,-1),(-1,0))
MARK=G[0]['marker']; CWORD=G[1]['word'][len(G[0]['word']):]

def rot(q,h):
 x,y=q
 return ((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def add(a,b): return a[0]+b[0],a[1]+b[1]
def sub(a,b): return a[0]-b[0],a[1]-b[1]
def det(a,b): return a[0]*b[1]-a[1]*b[0]
def place(q,p,h): return add(p,rot(q,h))
def edge(q):
 x,y=q; d=(1,1)if (x+y)%2==0 else(1,-1)
 return ((2*x-d[0],2*y-d[1]),(2*x+d[0],2*y+d[1]))
def leaf_core(cells):
 cells=set(cells)
 while cells:
  degrees=Counter(v for q in cells for v in edge(q))
  leaves={q for q in cells if any(degrees[v]==1 for v in edge(q))}
  if not leaves:break
  cells-=leaves
 return cells

def reconstruct(word):
 p=(0,0);h=0;par=set();req={}
 for ch in word:
  b=(ch=='L')^(p in par)
  assert p not in req or req[p]==b
  req[p]=b;par.symmetric_difference_update({p})
  h=(h+(-1 if ch=='L'else 1))%4;p=add(p,VEC[h])
 return req,par,p,h

# Do not trust the supplied literal masks without raw reconstruction.
for a in IDS:
 g=G[a]
 req,_,_,_=reconstruct(g['word']+MARK)
 assert req=={(x,y):bool(b)for x,y,b,*_ in g['requirements']}
 assert {q for q,b in req.items()if b}==K|set(map(tuple,g['inputs']))
 _,par,p,h=reconstruct(g['word'])
 assert [*p,h]==g['endpoint']
 board=(K|set(map(tuple,g['inputs'])))^par
 exitcore={place(q,p,h)for q in K}
 assert exitcore<=board
 assert board-exitcore==set(map(tuple,g['outputs']))

Z=leaf_core(map(tuple,G[7]['outputs']))
assert Z=={(1,0),(1,1),(2,0),(2,1)}
assert all(leaf_core(map(tuple,G[a]['outputs']))==Z for a in(7,8,9))
w=(0,1)
assert all(w in set(map(tuple,G[a]['outputs']))for a in(7,8,9))
# Source internal C tails do not touch any of these exact base outputs.
for a in (7,8,9):
 p=(0,0);h=0
 for tick,ch in enumerate(G[a]['word']):
  if tick>=len(G[7]['word']):assert p not in Z|{w}
  h=(h+(-1 if ch=='L'else 1))%4;p=add(p,VEC[h])

# Exact segment intersection, with parameters on the earlier source and
# later consumer chord. Fractions avoid numerical endpoint ambiguities.
def intersection(a,b,c,d):
 u,v,z=sub(b,a),sub(d,c),sub(c,a);den=det(u,v)
 if den:
  s,t=F(det(z,v),den),F(det(z,u),den)
  return dict(kind='point',source=s,consumer=t)if 0<=s<=1 and 0<=t<=1 else None
 if det(z,u):return None
 k=0 if u[0]else 1
 lo,hi=sorted((F(c[k]-a[k],u[k]),F(d[k]-a[k],u[k])))
 lo=max(F(0),lo);hi=min(F(1),hi)
 return dict(kind='collinear',source_interval=(lo,hi))if lo<=hi else None

def atom_chord(p,h,a):
 s=add((2*p[0],2*p[1]),rot((-1,-1),h))
 step=rot((2,2)if a in(0,1,'C')else(2,6)if a in(4,5,6)else(0,8),h)
 return s,add(s,step)
SOURCE=atom_chord((0,0),0,7)

def hit_source_interior(hit):
 if hit is None:return False
 if hit['kind']=='point':return 0<hit['source']<1
 lo,hi=hit['source_interval']
 return hi>0 and lo<1

# Place every true input of every full packet on every cycle cell.
first_rows=[];gates={}
for a in IDS:
 for q in sorted(Z):
  for slot in G[a]['inputs']:
   for h in range(4):
    p=sub(q,rot(slot,h))
    I={place(z,p,h)for z in G[a]['inputs']}
    core={place(z,p,h)for z in K}
    white={place(z[:2],p,h)for z in G[a]['requirements']if not z[2]}
    reason='sector'if(sum(p)+h)%2 else'core'if Z&core else'white'if Z&white else'candidate'
    row=dict(packet=a,name=G[a]['name'],pose=(*p,h),source_cycle_cell=q,input_slot=slot,reason=reason,cycle_inputs=sorted(Z&I))
    first_rows.append(row)
    if reason=='candidate':gates[a,*p,h]=row
assert len(first_rows)==368
expected={(0,-1,1),(0,2,2),(3,-1,0),(3,2,3)}
assert set(gates)=={(a,*p)for a in(7,8,9)for p in expected}
for (a,x,y,h),row in gates.items():
 assert set(map(tuple,row['cycle_inputs']))=={place((-1,1),(x,y),h),place((-1,2),(x,y),h)}
 row['source_chord_intersection']=intersection(*SOURCE,*atom_chord((x,y),h,a))
 row['blocker_before_white']=w in {place(z[:2],(x,y),h)for z in G[a]['requirements']if not z[2]}

# Any strict earlier retirement of w must preserve every exact cycle ID.
# A context contact with a protected cycle edge means a core conflict,
# wrong before-white requirement, or actual input retirement.
blocker_rows=[];blocker_survivors=[]
for a in IDS:
 for slot in G[a]['inputs']:
  for h in range(4):
   p=sub(w,rot(slot,h))
   context={place(z[:2],p,h)for z in G[a]['requirements']}
   why='sector'if(sum(p)+h)%2 else'protected_cycle_context'if Z&context else'source_chord'
   hit=intersection(*SOURCE,*atom_chord(p,h,a))if why=='source_chord'else None
   row=dict(packet=a,name=G[a]['name'],pose=(*p,h),input_slot=slot,reason=why,cycle_context_hits=sorted(Z&context),source_chord_intersection=hit)
   blocker_rows.append(row)
   if why=='source_chord':
    assert hit_source_interior(hit)
    blocker_survivors.append(row)
assert len(blocker_rows)==92
assert {(r['packet'],*r['pose'])for r in blocker_survivors}=={(a,0,2,2)for a in(0,1)}|{(a,0,4,2)for a in(4,5)}|{(a,-1,3,2)for a in(7,8,9)}|{(a,-1,5,2)for a in(7,8)}
assert len(blocker_survivors)==9

for (a,x,y,h),row in gates.items():
 if (x,y,h)in((0,-1,1),(3,2,3)):
  hit=row['source_chord_intersection'];assert hit is not None
  # (0,-1,E) repeats the source entry. The other contact is interior.
  row['final_disposition']='SIMPLE_PATH_SOURCE_CONTACT'
 elif (x,y,h)==(0,2,2):
  assert row['blocker_before_white'];row['final_disposition']='PERSISTENT_W_WHITE_CONFLICT'
 else:
  assert(x,y,h)==(3,-1,0)
  row['final_disposition']='UNEXCLUDED_AND_PHYSICALLY_REALIZED'
  new={place(q,(x,y),h)for q in Z}
  assert new=={add(q,(3,-1))for q in Z}
  assert not new&Z

# Optional useful upper-support refinement: after the creating packet and
# before the breaker, no one producer can supply b,c together, nor c,d.
# The latter's context survivors start at the future U exit center.
upper_pair_rows=[]
for gp in((3,-1,0),(0,2,2)):
 p=gp[:2];h=gp[2]
 targets={k:place(z,p,h)for k,z in [('b',(-1,4)),('c',(0,2)),('d',(0,3))]}
 for pair in(('b','c'),('c','d')):
  T={targets[k]for k in pair};poses=set()
  for a in IDS:
   for out in G[a]['outputs']:
    for sh in range(4):
     sp=sub(targets[pair[0]],rot(out,sh))
     O={place(z,sp,sh)for z in G[a]['outputs']}
     if not(sum(sp)+sh)%2 and T<=O:poses.add((a,*sp,sh))
  for a,x,y,sh in sorted(poses):
   ctx={place(z[:2],(x,y),sh)for z in G[a]['requirements']}
   conflict=sorted(ctx&Z)
   hit=intersection(*atom_chord(p,h,7),*atom_chord((x,y),sh,a))
   row=dict(goal_pose=gp,pair=pair,producer_packet=a,producer_pose=(x,y,sh),cycle_context_hits=conflict,goal_chord_intersection=hit)
   if not conflict:
    assert pair==('c','d')
    assert hit is not None
    # The producer starts at the FUTURE goal exit: never an adjacent
    # incoming-producer / outgoing-goal shared-entry exception.
    assert atom_chord((x,y),sh,a)[0]==atom_chord(p,h,7)[1]
   upper_pair_rows.append(row)

# Direct actual finite witness of the surviving right renewal. The seed is
# reconstructed by first-read parity, not imported from a search output.
word=[9,4,1,0,5,0,7]
raw=''.join(G[a]['word']for a in word)
req,_,_,_=reconstruct(raw+MARK)
seed={q for q,b in req.items()if b};assert len(seed)==19
B=set(seed);p=(0,0);h=0;boards={0:set(B)};poses={0:(p,h)};t=0
for ch in raw+MARK:
 assert('L'if p in B else'R')==ch
 black=p in B;B.symmetric_difference_update({p});h=(h+(-1 if black else 1))%4;p=add(p,VEC[h]);t+=1
 boards[t]=set(B);poses[t]=(p,h)
T={q:('entry',j)for j,q in enumerate(sorted(seed-K))};p=(0,0);h=0;t=0;history=[];source_cycle_ids=None
for j,a in enumerate(word):
 core={place(q,p,h)for q in K};assert boards[t]==core|set(T)and not core&set(T)
 I=[place(q,p,h)for q in G[a]['inputs']]
 if j>0:assert all(T.get(q)==source_cycle_ids[q]for q in Z)
 inputs=[(q,T.pop(q))for q in I]
 for oi,q in enumerate(G[a]['outputs']):
  q=place(q,p,h);assert q not in T;T[q]=(j,oi)
 if j==0:source_cycle_ids={q:T[q]for q in Z};assert T[w][0]==0
 history.append(dict(index=j,packet=a,name=G[a]['name'],pose=(*p,h),inputs=inputs,cycle_intact_before=j>0))
 dx,dy,dh=G[a]['endpoint'];p=place((dx,dy),p,h);h=(h+dh)%4;t+=len(G[a]['word']);assert poses[t]==(p,h)
assert history[-1]['pose']==(3,-1,0)
assert [q for q,tag in history[-1]['inputs'][:2]]==[(2,0),(2,1)]
assert all(tag[0]==0 for q,tag in history[-1]['inputs'][:2])
assert all(tag[0]=='entry'for q,tag in history[-1]['inputs'][2:])
assert T[w][0]==0
arcs=[];t=0
for a in word:
 base=0 if a in(0,1)else 4 if a in(4,5,6)else 7
 for at in[base]+['C']*G[a]['name'].count('C'):
  p,h=poses[t];chord=atom_chord(p,h,at);length=len(CWORD)if at=='C'else len(G[at]['word']);ep,eh=poses[t+length]
  assert chord[1]==add((2*ep[0],2*ep[1]),rot((-1,-1),eh))
  arcs.append(chord);t+=length
for i,earlier in enumerate(arcs):
 for j in range(i+1,len(arcs)):
  hit=intersection(*earlier,*arcs[j])
  if j==i+1:
   assert arcs[j][0]==earlier[1]
   assert hit==dict(kind='point',source=F(1),consumer=F(0)) or hit==dict(kind='collinear',source_interval=(F(1),F(1)))
  else:assert hit is None
assert len(arcs)==11

out=dict(status='AUTHOR_EXACT_DIRECTED_U_CYCLE_RENEWAL',scope='Actual complete recurrent-eight simple atomic-center factor, source U/UC/UCC and its four exact output-cycle identities. First retirement only; not incidence connectivity or finite U budget.',conclusion='Only U/UC/UCC at (3,-1,N) relative to the creating U pose can first retire its intact output cycle. It consumes exactly its lower pair. The two east-column identities (2,0),(2,1) can only retire together at that gate, never separately or as upper inputs. Every inheritance chain has fixed heading and cycle centers advance by the same rotated vector (3,-1).',cycle_cells=sorted(Z),persistent_white_blocker=w,first_retirement_alignment_count=len(first_rows),first_retirement_counts=dict(Counter(r['reason']for r in first_rows)),first_retirement_candidates=list(gates.values()),blocker_alignment_count=len(blocker_rows),blocker_counts=dict(Counter(r['reason']for r in blocker_rows)),all_blocker_rows=blocker_rows,blocker_context_survivors=blocker_survivors,upper_pair_rows=upper_pair_rows,physical_control=dict(word=word,names=[G[a]['name']for a in word],seed=sorted(seed),raw_length=len(raw),history=history,all_atomic_chords_twice=arcs,simple_pairs_checked=len(arcs)*(len(arcs)-1)//2),limits=['A directed unbounded cycle-renewal chain is not excluded.','The intact-cycle count is nondecreasing, not finite fuel.','A cycle is a physical unit face, not a historical incidence cycle or component.','Upper inputs from distinct producers can already share a historical component.'],dependencies={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()for p in(GP,Path(__file__).resolve())})
def encode(x):
 if isinstance(x,F):return int(x)if x.denominator==1 else str(x)
 if isinstance(x,(tuple,list)):return[encode(v)for v in x]
 if isinstance(x,dict):return{k:encode(v)for k,v in x.items()}
 return x
(HERE/'directed_cycle_renewal.json').write_text(json.dumps(encode(out),indent=2)+'\n')
print(json.dumps(dict(status=out['status'],first_alignments=len(first_rows),first_candidates=len(gates),blocker_counts=out['blocker_counts'],only_surviving_pose=(3,-1,0),control_raw=len(raw)),indent=2))
