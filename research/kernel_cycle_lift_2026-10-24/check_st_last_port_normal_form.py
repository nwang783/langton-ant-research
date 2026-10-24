"""Symbolic RL-tail/first-star geometry plus four finite prefunded fixtures.
The fixture suffix choice specifies a necessary future tail-component type;
it is NOT claimed to execute that successor without all its other input cells.
"""
from pathlib import Path
from itertools import product
import sys,json
ROOT=Path('/workspace/shared/langton');OUT=Path(__file__).parent
sys.path.insert(0,str(ROOT/'reframe_finite_seed_2026-10-24'))
from active_flight import DIR,rot,cursor,ends,vertices,comp,step
S='RRRRLRLRL';T='RRRRLLLLRLRL';WORDS={'S':S,'T':T};a=(-1,-1);c=(-1,0);e=(2,1)
F={'S':{a,(-1,1),(-2,2)},'T':{a,c,e}}
expectedC={'S':[{a},{(-1,1),(-2,2)}],'T':[{a,c},{e}]}
def components(B):
 seen=set();C=[]
 for q in sorted(B):
  if q not in seen:
   z=comp(B,1,ends(q,1)[0]);seen|=z;C.append(z)
 return C
for x in 'ST':
 assert set().union(*expectedC[x])==F[x]
 assert sorted(map(sorted,components(F[x])))==sorted(map(sorted,expectedC[x]))
 r=cursor((0,0),0);U=set()
 for dx,dy in product((-2,2),repeat=2):U|=comp(F[x],1,(r[0]+dx,r[1]+dy))
 assert U==F[x]and len(U)==3

fixtures=[]
for x,y in product('ST',repeat=2):
 B=set(F[x]);connector=(-3,1)if x=='S'else(1,2)
 if y=='T':B.add(connector)
 desired=set(B);seed=(B-{a})|{(0,-1)};B=set(seed);birth={q:None for q in B};p=a;h=0;W='RL'+WORDS[x];trace=[];imports=[]
 lastR=2+(7 if x=='S' else 10)
 for t in range(len(W)+1):
  C=comp(B,1,cursor(p,h));zz=rot((-1,-1),h);z=(2*p[0]+zz[0],2*p[1]+zz[1]);Z=comp(B,0,z)
  trace.append(dict(cut=t,pose=[p,h],w_cursor=cursor(p,h),z_cursor=z,full_black=sorted(B),active_w=sorted(C),active_z=sorted(Z)))
  assert len(C)<=7
  if t==2:assert(p,h)==((0,0),0)and B==desired and not C and birth[a]==0
  if t==len(W):break
  q=p;ch=W[t];assert ch==('L'if q in B else'R')
  if ch=='R':
   r=cursor(p,h);u,v=ends(q,1);o=v if u==r else u;D=comp(B,1,o)if o not in vertices(C,1)|{r}else set()
   imports.append(dict(update=t,component=sorted(D)))
   birth[q]=t
  else:birth.pop(q)
  p,h=step(B,p,h)
 assert not comp(B,1,cursor(p,h))
 qtail=next(q for q,b in birth.items()if b==lastR)
 tail=comp(B,1,ends(qtail,1)[0]);normal={rot((q[0]-p[0],q[1]-p[1]),(-h)%4)for q in tail}
 assert normal==({a}if y=='S'else{a,c})
 D=next(v['component']for v in imports if v['update']==lastR)
 assert D==([]if y=='S'else[connector])
 fixtures.append(dict(current=x,successor_tail_type=y,initial_pose=[a,0],initial_black=sorted(seed),initial_mass=len(seed),word=W,incoming_hook_birth=0,current_macro_start=2,last_R_update=lastR,last_R_import=D,exit_pose=[p,h],tail_component=sorted(tail),normalized_tail_component=sorted(normal),trace=trace))
# The two non-tail inputs of the next word were not read by the previous word.
old_inputs=[]
for x,y in product('ST',repeat=2):
 p=(0,0);h=0;reads=[]
 for ch in WORDS[x]:
  reads.append(p);h=(h+(1 if ch=='R'else-1))%4;p=(p[0]+DIR[h][0],p[1]+DIR[h][1])
 local={(-1,1),(-2,2)}if y=='S'else{c,e}
 world={(p[0]+v[0],p[1]+v[1])for q in local for v in[rot(q,h)]}
 assert world.isdisjoint(reads)
 old_inputs.append(dict(previous=x,current=y,previous_exit=[p,h],non_tail_input_cells=sorted(world),not_read_by_previous=True))
out=dict(status='AUTHOR exact RL-tail and S/T first-port normal forms with finite prefunded controls',canonical_hook=a,mandatory_initial_fields={x:sorted(v)for x,v in F.items()},complete_components={x:[sorted(v)for v in z]for x,z in expectedC.items()},old_import_budget=3,fixtures=fixtures,old_input_placement=old_inputs,scope='Universal normal forms follow analytically from mandatory3-edge saturation and exact reverse-two-toggle geometry. Fixtures execute only a real RL prefix plus one current block, not an uncharged full successor or an infinite circuit.')
(OUT/'st_last_port_normal_form_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':out['status'],'fixtures':[{k:a[k]for k in['current','successor_tail_type','initial_mass','last_R_import','exit_pose','normalized_tail_component']}for a in fixtures],'old_inputs':old_inputs},indent=2))
