"""Actual full-field continuation of the smallest supplied 394-cell producer.
Every detected standard flight receives an exact infinite/future-contact guard.
"""
from pathlib import Path
import json,sys,time,hashlib
P=Path(__file__).resolve().parent;sys.path.insert(0,str(P.parents[1]/'computability'))
from periodic_tail_checker import State,first_mismatch
from check4352_noncrossing_producer import H,V
J=json.loads((P/'prepared4352_first_finite_endpoint.json').read_text());B={tuple(z)for z in J['field_before_contact']};p=tuple(J['pose'][0]);h=J['pose'][1];t=J['time'];start=t;recent='';rot={H[i:]+H[:i]for i in range(104)};word=[];events=[];last={};st=time.time()
def step():
 global p,h,t,recent
 c='L'if p in B else'R';last[p]=[t,h,c];B.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;v=V[h];p=p[0]+v[0],p[1]+v[1];t+=1;word.append(c);recent=(recent+c)[-208:];return c
while True:
 if len(recent)==208 and recent[:104]==recent[104:]and recent[104:]in rot:
  w=recent[104:];n=first_mismatch(State(frozenset(B),p,h),w)
  event={'time':t,'offset':t-start,'pose':[p,h],'word':w,'mass':len(B),'next_mismatch':n};events.append(event)
  print('flight',len(events),{k:v for k,v in event.items()if k!='word'},flush=True)
  if n is None:
   out={'scope':__doc__,'status':'EXACT_STANDARD104_CAPTURE','start_time':start,'capture_time':t,'capture_pose':[p,h],'capture_word':w,'capture_mass':len(B),'events':events,'continuation_word':''.join(word),'final_field_sha256':hashlib.sha256(json.dumps(sorted(B),separators=(',',':')).encode()).hexdigest(),'seconds':time.time()-st}
   (P/'prepared4352_first_endpoint_capture.json').write_text(json.dumps(out,indent=2)+'\n');break
  for i in range(n):assert step()==w[i%104]
  event['contact']={'time':t,'pose':[p,h],'wanted':w[n%104],'actual':'L'if p in B else'R','previous_since_endpoint':last.get(p)}
  assert event['contact']['actual']!=event['contact']['wanted'];step();recent='';continue
 step()
 if(t-start)%100000==0:print('steps',t-start,'mass',len(B),'pose',p,h,flush=True)
print('finished',t,'seconds',time.time()-st,flush=True)
