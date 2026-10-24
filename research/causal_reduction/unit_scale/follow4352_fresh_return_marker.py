"""One supplied canonical fresh-R marker, on the complete original M1 board.
The all-M unread proof is separate. No other cap or marker is explored.
"""
from pathlib import Path
import json,hashlib,sys,time
P=Path(__file__).resolve().parent
sys.path.insert(0,str(P.parents[1]/'computability'))
from periodic_tail_checker import State,first_mismatch
from check4352_noncrossing_producer import H,V
J=json.loads((P/'prepared4352_two_phase_manifest.json').read_text())
Q=json.loads((P/'prepared4352_fresh_return_marker.json').read_text())
m=int(sys.argv[1])if len(sys.argv)>1 else 1
val=lambda a:a[0]*m+a[1]
q=tuple(Q['marker']);B={(val(x),val(y))for x,y in J['seed_families']}
assert len(B)==394 and q not in B
B.add(q);initial=set(B)
p=(val(J['initial_pose']['x_N_constant']),val(J['initial_pose']['y_N_constant']));h=3;t=0
history='LRLRRRRLLL';factors={(H*2)[i:i+10]for i in range(104)};bad=history not in factors;K=0
last={};first={};stages=[];recent='';word=[];events=[];clock=time.time()
def digest(B):return hashlib.sha256(json.dumps(sorted(B),separators=(',',':')).encode()).hexdigest()
def step(save=False):
 global p,h,t,history,bad,K,recent
 c='L'if p in B else'R';first.setdefault(p,c);last[p]=[t,h,c]
 history=(history+c)[-10:];nb=history not in factors;K+=bad and nb;bad=nb
 B.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p=p[0]+V[h][0],p[1]+V[h][1];t+=1
 if save:word.append(c);recent=(recent+c)[-208:]
 return c
for s in J['stages']:
 assert(p,h,t)==((val(s['start_x_N_constant']),val(s['start_y_N_constant'])),s['heading'],val(s['start_time_N_constant']))
 for _ in range(val(s['count_N_constant'])):
  for c in s['word']:
   assert p!=q and step()==c
 stages.append({'kind':s['kind'],'time':t,'pose':[p,h],'mass':len(B),'K':K})
for c in Q['preceding_unmodified_return_prefix']:
 assert p!=q and step()==c
assert(p,h,t)==(q,1,455250+129780*m)and p not in last and p in B
start=t;marker={'M':m,'scope':__doc__,'original_seed':sorted(initial),'original_mass':len(initial),'marker':q,'time':t,'pose':[p,h],'K':K,'mass':len(B),'field_before_marker':sorted(B),'field_sha256':digest(B),'stages':stages,'proof_sha256':hashlib.sha256((P/'prepared4352_fresh_return_marker.json').read_bytes()).hexdigest()}
(P/f'prepared4352_fresh_marker_M{m}_entry.json').write_text(json.dumps(marker,indent=2)+'\n')
print('fresh marker',t,p,h,'mass',len(B),'K',K,flush=True)
assert step(True)=='L'
rot={H[i:]+H[:i]for i in range(104)}
while True:
 if len(recent)==208 and recent[:104]==recent[104:]and recent[104:]in rot:
  w=recent[104:];n=first_mismatch(State(frozenset(B),p,h),w)
  event={'time':t,'offset':t-start,'pose':[p,h],'word':w,'mass':len(B),'K':K,'next_mismatch':n};events.append(event)
  print('flight',len(events),{k:v for k,v in event.items()if k!='word'},flush=True)
  if n is None:
   out={'scope':__doc__,'M':m,'status':'EXACT_STANDARD104_CAPTURE','original_mass':len(initial),'marker':q,'start_time':start,'capture_time':t,'capture_pose':[p,h],'capture_word':w,'capture_mass':len(B),'total_K':K,'events':events,'continuation_word':''.join(word),'final_field':sorted(B),'final_field_sha256':digest(B),'first_L_equals_seed':{a for a,c in first.items()if c=='L'}==initial,'seconds':time.time()-clock}
   (P/f'prepared4352_fresh_marker_M{m}_capture.json').write_text(json.dumps(out,indent=2)+'\n');break
  for i in range(n):assert step(True)==w[i%104]
  event['contact']={'time':t,'pose':[p,h],'wanted':w[n%104],'actual':'L'if p in B else'R','previous':last.get(p)}
  assert event['contact']['actual']!=event['contact']['wanted'];step(True);recent='';continue
 step(True)
 if(t-start)%100000==0:print('steps',t-start,'mass',len(B),'pose',p,h,'K',K,flush=True)
print('finished',t,'seconds',time.time()-clock,flush=True)
