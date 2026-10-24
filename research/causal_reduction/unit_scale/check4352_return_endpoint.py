"""Actual first departure from the15324 return wave on the supplied M1 board.
Retain all original394 cells and every write of both nonstandard phases.
"""
from pathlib import Path
import json,hashlib
from check4352_noncrossing_producer import V
P=Path(__file__).resolve().parent;J=json.loads((P/'prepared4352_two_phase_manifest.json').read_text());m=1
v=lambda a:a[0]*m+a[1]
B={(v(x),v(y))for x,y in J['seed_families']};initial=set(B);p=(v(J['initial_pose']['x_N_constant']),v(J['initial_pose']['y_N_constant']));h=3;t=0;last={}
for s in J['stages']:
 for r in range(v(s['count_N_constant'])):
  for c in s['word']:
   assert(p in B)==(c=='L');last[p]=[t,h,c,s['kind'],r];B.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p=(p[0]+V[h][0],p[1]+V[h][1]);t+=1
assert(p,h)==((117,111),0);entry=t;w=J['stages'][-1]['word'];i=0
while('L'if p in B else'R')==w[i%len(w)]:
 c=w[i%len(w)];last[p]=[t,h,c,'extra-return',i//len(w)];B.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p=(p[0]+V[h][0],p[1]+V[h][1]);t+=1;i+=1
out={'scope':__doc__,'M':m,'original_mass':394,'checkpoint_time':entry,'offset_after_M_return_periods':i,'extra_complete_periods':i//len(w),'return_phase':i%len(w),'time':t,'pose':[p,h],'wanted':w[i%len(w)],'actual':'L'if p in B else'R','prior_read':last.get(p),'initial_black':p in initial,'field_mass':len(B),'field_before_contact':sorted(B),'field_sha256':hashlib.sha256(json.dumps(sorted(B),separators=(',',':')).encode()).hexdigest()}
(P/'prepared4352_return_endpoint.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items()if k!='field_before_contact'},indent=2))
