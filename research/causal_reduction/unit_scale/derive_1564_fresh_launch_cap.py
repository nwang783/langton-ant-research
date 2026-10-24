"""Prune the positive launch to four mature bands, one causal SW writer,
and a finite additions-only cap outside its entire strict past READ set.
"""
from pathlib import Path
from collections import defaultdict
import json
import inverse_wave_tail_completion as T
P=Path(__file__).resolve().parent
J=json.loads((P/'LLR_inverse_completion_certificate.json').read_text());p,h=J['inverse_tail_pose'];p=tuple(p)
I=J['inverse_tail_word'];rows,_,_=T.trace(I,p,h);groups=defaultdict(list)
for i,(x,y),hh,ch in rows:groups[x-y,x%2].append((i-104*(x//2),x//2,ch))
groups={j:sorted(g)for j,g in groups.items()}
def required(z):
 x,y=z
 for time,k,c in groups.get((x-y,x%2),()):
  if k<=x//2:return c=='L'
 return None
def otherbulk(z):
 return T.bulk(z) and (z[0]-z[1],z[0]%2)not in groups
F={tuple(z)for z in J['forward_entry_cap_vs_full_bulk']}
def oldentry(z):return T.bulk(z)^(z in F)
fr,ep,eh=T.trace(J['forward_prelude_word'],tuple(J['forward_entry_pose'][0]),J['forward_entry_pose'][1]);finitefuture={q for _,q,_,_ in fr}
# All future wave cells outside the incoming strict-past rays are finite within
# the last writer strip; enumerate exactly up to each ray's first I-read index.
for (t,a14),start in T.FUTURE.items():
 a2=a14%2
 if(t,a2)not in groups:continue
 threshold=min(z[1]for z in groups[t,a2]);x=a14+14*start
 while x//2<threshold:
  finitefuture.add((x,x-t));x+=14
K=set();checked=[]
for z in finitefuture|F:
 # F can include irrelevant cells; demand equality only where subsequently read.
 if z not in finitefuture and not T.future_read(z):continue
 c=required(z);baseline=otherbulk(z)^(bool(c)if c is not None else False)
 if oldentry(z)!=baseline:
  assert c is None,(z,'past overlap');assert not baseline,(z,'not addition');assert oldentry(z)
  K.add(z)
 assert(required(z)is None or z not in K)
# Independent finite check of full equality on complete future ray fringes and
# one mature point on each ray; beyond these all functions have the same profile.
checks=0
for (t,a),start in T.FUTURE.items():
 crit={start}
 for _,k,_ in groups.get((t,a%2),()):
  n=(2*k-a)//14
  crit.update(n+d for d in(-1,0,1)if n+d>=start)
 for z in F|K:
  if z[0]-z[1]==t and z[0]%14==a:
   n=z[0]//14;crit.update(n+d for d in(-1,0,1)if n+d>=start)
 for n in crit:
  z=a+14*n,a+14*n-t;c=required(z)
  fresh=otherbulk(z)^(bool(c)if c is not None else False)^(z in K)
  assert fresh==oldentry(z),(z,fresh,oldentry(z));checks+=1
for _,z,_,_ in fr:
 c=required(z);assert oldentry(z)==(otherbulk(z)^(bool(c)if c is not None else False)^(z in K))
result={'scope':__doc__,'forward_entry_pose':J['forward_entry_pose'],'incoming_original_H_phase':55,
 'incoming_inverse_tail_pose':J['inverse_tail_pose'],'incoming_inverse_tail_word':I,
 'other_full_black_profiles':sorted(j for j in T.B if j not in groups),
 'fresh_cap':sorted(K),'fresh_cap_mass':len(K),'forward_prelude':J['forward_prelude_word'],
 'wave_pose':T.N['pose'],'future_ray_equality_tests':checks,'incoming_strict_past_read_orbits':len(groups),
 'cap_disjoint_entire_incoming_past':all(required(z)is None for z in K)}
(P/'prepared1564_fresh_launch_cap.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
