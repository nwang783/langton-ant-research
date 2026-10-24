"""Full actual finite-board checks of the finitely exceptional N=1,2,3,
plus the first uniformly certified member N=4. No finite exploration is used
as the uniform-parameter premise. Every reported terminal tail is all-future.
"""
from pathlib import Path
import json,hashlib,sys,time
from check1564_noncrossing_producer import setup,H,W,V
P=Path(__file__).resolve().parent;sys.path.insert(0,str(P.parents[1]/'computability'))
from periodic_tail_checker import State,first_mismatch
rot={H[i:]+H[:i]for i in range(104)}
def run(N):
 R=100+28*N;start,B,ss,caps=setup(R,N);p=start;h=3;t=0;initial=set(B);st=time.time()
 for s in ss:
  w=H*s['count']if s['kind']=='H'else W*s['count']if s['kind']=='wave'else s['word']
  assert[p,h]==s['start']
  for c in w:
   assert(p in B)==(c=='L');B.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;v=V[h];p=(p[0]+v[0],p[1]+v[1]);t+=1
 checkpoint=t;word=[];recent='';events=[];firstwave=None
 def step():
  nonlocal p,h,t,recent,firstwave
  c='L'if p in B else'R'
  if firstwave is None and c!=W[len(word)%1564]:firstwave={'offset':len(word),'time':t,'pose':[p,h],'wanted':W[len(word)%1564],'actual':c}
  B.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;v=V[h];p=(p[0]+v[0],p[1]+v[1]);t+=1;word.append(c);recent=(recent+c)[-208:];return c
 while True:
  if len(recent)==208 and recent[:104]==recent[104:]and recent[104:]in rot:
   w=recent[104:];bad=first_mismatch(State(frozenset(B),p,h),w);e={'time':t,'offset':len(word),'pose':[p,h],'mass':len(B),'word':w,'next_mismatch':bad};events.append(e);print('N',N,'flight',{k:v for k,v in e.items()if k!='word'},flush=True)
   if bad is None:break
   for i in range(bad):assert step()==w[i%104]
   e['contact']={'time':t,'pose':[p,h],'wanted':w[bad%104],'actual':'L'if p in B else'R'};step();recent='';continue
  step()
  if len(word)%1000000==0:print('N',N,'continuation',len(word),'pose',p,h,flush=True)
 out={'N':N,'R':R,'status':'EXACT FINITE-BOARD STANDARD104 CAPTURE','initial_mass':len(initial),'checkpoint_time':checkpoint,'first_wave_departure':firstwave,'continuation_word':''.join(word),'events':events,'capture_time':t,'capture_pose':[p,h],'capture_mass':len(B),'capture_word':w,'final_field_sha256':hashlib.sha256(json.dumps(sorted(B),separators=(',',':')).encode()).hexdigest(),'seconds':time.time()-st}
 (P/f'prepared1564_endpoint_N{N}.json').write_text(json.dumps(out,indent=2)+'\n');return{k:v for k,v in out.items()if k not in('continuation_word','events','capture_word')}
if __name__=='__main__':
 ans=[]
 for n in [1,2,3,4]:ans.append(run(n));print(json.dumps(ans[-1]),flush=True)
 (P/'prepared1564_exceptional_endpoint_members.json').write_text(json.dumps({'scope':__doc__,'results':ans},indent=2)+'\n')
