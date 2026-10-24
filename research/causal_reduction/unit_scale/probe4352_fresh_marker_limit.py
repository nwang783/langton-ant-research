"""The SAME canonical marker on the explicit complete return-end ray limit.
This is a prepared-interface calculation, never a finite-seed inference.
"""
from pathlib import Path
import json,time,hashlib
from probe4352_return_end_limit import build,first_bad,H,V
P=Path(__file__).resolve().parent
Q=json.loads((P/'prepared4352_fresh_return_marker.json').read_text())
C=json.loads((P/'prepared4352_fresh_marker_M1_capture.json').read_text())
b=build();q=tuple(Q['marker']);assert not b.color(q);b.toggle(q)
initial=b.manifest();p=(117,111);h=0;word=[];recent='';events=[];started=time.time();comparison=None
def step():
 global p,h,recent,comparison
 c='L'if b.color(p)else'R'
 j=len(word)-Q['offset_after_checkpoint']
 if j>=0 and j<len(C['continuation_word'])and comparison is None and c!=C['continuation_word'][j]:
  comparison={'offset_from_checkpoint':len(word),'offset_from_marker':j,'pose':[p,h],'limit_turn':c,'M1_turn':C['continuation_word'][j]}
  print('first M1 divergence',comparison,flush=True)
 b.toggle(p);h=(h+(1 if c=='R'else-1))%4;p=p[0]+V[h][0],p[1]+V[h][1];word.append(c);recent=(recent+c)[-208:];return c
for c in Q['preceding_unmodified_return_prefix']:assert step()==c
assert(p,h)==(q,1);assert step()=='L'
rot={H[i:]+H[:i]for i in range(104)}
while True:
 if len(recent)==208 and recent[:104]==recent[104:]and recent[104:]in rot:
  w=recent[104:];bad,d=first_bad(b,p,h,w)
  e={'offset':len(word),'pose':[p,h],'word':w,'first_bad':bad,'drift':d};events.append(e);print('flight',e,flush=True)
  if bad is None:break
  for i in range(bad):assert step()==w[i%104]
  e['contact']={'offset':len(word),'pose':[p,h],'wanted':w[bad%104],'actual':'L'if b.color(p)else'R'}
  step();recent='';continue
 step()
 if len(word)%100000==0:print('steps',len(word),'pose',p,h,'F',len(b.F),flush=True)
out={'scope':__doc__,'status':'EXACT_PREPARED_STANDARD_TAIL','initial_board':initial,'initial_pose':[[117,111],0],'marker':q,'word':''.join(word),'events':events,'final_pose':[p,h],'final_finite_xor':sorted(b.F),'first_M1_divergence':comparison,'seconds':time.time()-started,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(P/'prepared4352_fresh_marker_limit.json').write_text(json.dumps(out,indent=2)+'\n')
print('finished',len(word),time.time()-started,flush=True)
