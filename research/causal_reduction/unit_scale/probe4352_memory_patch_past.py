"""The deterministic inverse orbit of the unique15-cell launch-only patch.
No other patch, marker, cap radius, or word is synthesized.
"""
from pathlib import Path
import json,time,hashlib
from probe4352_repaired_launch_past import build
from probe4352_return_end_limit import first_bad,H,V,L
import inverse4352_tail_completion as T
P=Path(__file__).resolve().parent
J=json.loads((P/'prepared4352_launch_memory_patch.json').read_text());patch=set(map(tuple,J['patch']))
b=build();assert all(not T.future_read(q)for q in patch)
for q in patch:b.toggle(q)
initial=b.manifest();p=(-1,3);h=1;word=[];recent='';events=[];firstdiv=None;clock=time.time()
original=L['inverse_prefix'];I=''.join('L'if c=='R'else'R'for c in H[::-1]);rot={H[i:]+H[:i]:'H'for i in range(104)};rot.update({I[i:]+I[:i]:'inverse_H'for i in range(104)})
def step():
 global p,h,recent,firstdiv
 c='L'if b.color(p)else'R'
 if firstdiv is None and len(word)<len(original)and c!=original[len(word)]:
  firstdiv={'time':len(word),'pose':[p,h],'original':original[len(word)],'actual':c};print('divergence',firstdiv,flush=True)
 b.toggle(p);h=(h+(1 if c=='R'else-1))%4;p=p[0]+V[h][0],p[1]+V[h][1];word.append(c);recent=(recent+c)[-208:];return c
status='FINITE_DIAGNOSTIC_ONLY'
while len(word)<100000:
 candidate=None;kind=None
 if len(recent)>=8 and recent[-8:]in('LR'*4,'RL'*4):candidate=recent[-2:];kind='alternating_staircase'
 elif len(recent)==208 and recent[:104]==recent[104:]and recent[104:]in rot:candidate=recent[104:];kind=rot[candidate]
 if candidate is not None:
  w=candidate;bad,d=first_bad(b,p,h,w);e={'offset':len(word),'kind':kind,'pose':[p,h],'word':w,'first_bad':bad,'drift':d};events.append(e);print('flight',e,flush=True)
  if bad is None:status='EXACT_PREPARED_PERIODIC_PAST';break
  if len(word)+bad>=100000:status='EXACT_TEMPORARY_FLIGHT_BEYOND_DIAGNOSTIC';break
  for i in range(bad):assert step()==w[i%len(w)]
  e['contact']={'offset':len(word),'pose':[p,h],'wanted':w[bad%len(w)],'actual':'L'if b.color(p)else'R'};step();recent='';continue
 step()
 if len(word)%10000==0:print('steps',len(word),'pose',p,h,'F',len(b.F),flush=True)
out={'scope':__doc__,'status':status,'patch':sorted(patch),'patch_future_unread':True,'initial_board':initial,'initial_inverse_pose':[[-1,3],1],'word':''.join(word),'events':events,'first_divergence_from_original_inverse':firstdiv,'final_pose':[p,h],'final_finite_xor':sorted(b.F),'seconds':time.time()-clock,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(P/'prepared4352_memory_patch_past.json').write_text(json.dumps(out,indent=2)+'\n');print('finished',status,len(word),time.time()-clock,flush=True)
