"""Exact candidate source-endpoint local limit of the constant-184 family.

The board is defined explicitly by integer orbit rays, not by finite-window
sampling. Its identification with the family limit is a separate geometric
claim. This discovery run follows the actual board and tests every encountered
standard tail with a complete ray-threshold verifier. No finite-seed claim.
"""
from pathlib import Path
from collections import defaultdict,Counter
import json,sys,time,hashlib,math
from check1564_noncrossing_producer import setup,H,W,V
from check_prepared1564_router_geometry import trace,infer
P=Path(__file__).resolve().parent

def key(q):return(q[0]-q[1],q[0]%14)
def z(q):return(q[0]-(q[0]%14))//14
class RayBoard:
 def __init__(self):self.full=set();self.rays=defaultdict(set);self.F=set()
 def toggle(self,q):self.F.symmetric_difference_update({q})
 def ray(self,q):
  k=key(q);s=z(q);self.rays[k].symmetric_difference_update({s})
 def color(self,q):return (key(q)in self.full)^(sum(z(q)<=s for s in self.rays.get(key(q),()))%2)^(q in self.F)
 def manifest(self):return {'full':sorted(self.full),'upper_rays':[[list(k),sorted(v)]for k,v in sorted(self.rays.items())if v],'finite_xor':sorted(self.F)}

def build():
 b=RayBoard();start,seed,ss,caps=setup(100,0)
 b.F=set(infer(H*30,start,3)['input'])
 # First writer starts at the retained original source and continues SW.
 for _,q,h,c in list(trace(H,start,3))[:-1]:
  for r in range(7):b.ray((q[0]-2*r,q[1]-2*r))
 # The remaining six writers become complete bi-infinite profiles.
 flights=[s for s in ss if s['kind']=='H']
 for f in flights[1:]:
  p,h=f['start'];C=Counter((q[0]-q[1],q[0]%2)for _,q,hh,c in list(trace(H,p,h))[:-1])
  for(t,a),n in C.items():
   if n%2:
    for r in range(a,14,2):b.full.symmetric_difference_update({(t,r)})
 # Completed W copies are indexed k<=2 in the fixed normalized gauge.
 for _,q,h,c in list(trace(W,(-6,-6),0))[:-1]:b.ray((q[0]+28,q[1]+28))
 # The current partial copy is k=3, stopped immediately before slot854.
 for _,q,h,c in list(trace(W[:854],(36,36),0))[:-1]:b.toggle(q)
 _,p,h,c=list(trace(W[:854],(36,36),0))[-1];assert(p,h)==((31,71),2)
 return b,p,h

def mult(q,d):
 if d[0]:
  if q[0]%d[0]:return None
  n=q[0]//d[0];return n if q[1]==n*d[1]else None
 if q[0]or q[1]%d[1]:return None
 return q[1]//d[1]

def first_bad(b,p,h,w):
 rows=list(trace(w,p,h));d=rows[-1][1][0]-p[0],rows[-1][1][1]-p[1]
 assert rows[-1][2]==h and d!=(0,0)
 slots=[q for _,q,hh,c in rows[:-1]];answer=None;P0=len(w)
 keys=b.full|set(b.rays)
 for i,q in enumerate(slots):
  thresholds=[]
  for j,qq in enumerate(slots):
   k=mult((qq[0]-q[0],qq[1]-q[1]),d)
   if k is not None and(k>0 or(k==0 and j<i)):thresholds.append(k)
  tests={0}
  if d[0]==d[1]:
   period=14//math.gcd(abs(d[0]),14);tests.update(range(period))
   for k in thresholds:tests.update(range(k,k+period))
   for r in range(period):
    qq=(q[0]+r*d[0],q[1]+r*d[1]);slope=period*d[0]//14
    for cut in b.rays.get(key(qq),()):
     j=(cut-z(qq))//slope
     for jj in (j-1,j,j+1):
      if jj>=0:tests.add(r+period*jj)
  else:
   tests.update(thresholds)
   dt=d[0]-d[1];qt=q[0]-q[1]
   for t,a in keys:
    if(t-qt)%dt:continue
    k=(t-qt)//dt
    if k>=0:tests.update((k,k+1))
  for qq in b.F:
   k=mult((qq[0]-q[0],qq[1]-q[1]),d)
   if k is not None and k>=0:
    tests.update((k,k+1))
    if d[0]==d[1]:tests.add(k+period)
  for k in sorted(tests):
   qq=q[0]+k*d[0],q[1]+k*d[1]
   actual=b.color(qq)^(sum(s<=k for s in thresholds)%2)
   if actual!=(w[i]=='L'):
    at=P0*k+i
    if answer is None or at<answer:answer=at
    break
 return answer,d

def main():
 b,p,h=build();initial=b.manifest();assert not b.color(p)
 # Compare the fixed normalized limit against existing finite endpoint field.
 A=json.loads((P/'prepared1564_first_finite_endpoint.json').read_text());B={tuple(q)for q in A['field_before_contact']}
 # Only a local control, never used as the limit proof.
 agreement=all(b.color((x,y))==((x,y)in B)for x in range(11,52)for y in range(51,92))
 print('local41square',agreement,flush=True)
 rot={H[i:]+H[:i]for i in range(104)};recent='';word=[];events=[];start=time.time();limit=1000000
 def step():
  nonlocal p,h,recent
  c='L'if b.color(p)else'R';b.toggle(p);h=(h+(1 if c=='R'else-1))%4;v=V[h];p=(p[0]+v[0],p[1]+v[1]);word.append(c);recent=(recent+c)[-208:];return c
 status='DISCOVERY_LIMIT'
 while len(word)<limit:
  if len(recent)==208 and recent[:104]==recent[104:]and recent[104:]in rot:
   w=recent[104:];bad,d=first_bad(b,p,h,w);e={'offset':len(word),'pose':[p,h],'word':w,'drift':d,'first_bad':bad};events.append(e);print('candidate',e,flush=True)
   if bad is None:status='EXACT_PREPARED_STANDARD_TAIL';break
   if len(word)+bad>=limit:status='EXACT_FLIGHT_BEYOND_DISCOVERY_LIMIT';break
   for j in range(bad):assert step()==w[j%104]
   e['contact']={'offset':len(word),'pose':[p,h],'wanted':w[bad%104],'actual':'L'if b.color(p)else'R'};step();recent='';continue
  step()
  if len(word)%100000==0:print('steps',len(word),'pose',p,h,'F',len(b.F),flush=True)
 out={'scope':__doc__,'status':status,'initial_board':initial,'initial_pose':[[31,71],2],'local_sample_agreement':agreement,'word':''.join(word),'events':events,'last_pose':[p,h],'final_finite_xor':sorted(b.F),'seconds':time.time()-start}
 (P/'prepared1564_source_endpoint_limit.json').write_text(json.dumps(out,indent=2)+'\n');print(status,len(word),'seconds',time.time()-start,flush=True)
if __name__=='__main__':main()
