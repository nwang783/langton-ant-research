"""Finite exact formula for the complete infinite incoming/outgoing S arms.
Each fixed physical cell class modulo d=(-1,+1) is s=x+y. Events are ordered
by increasing x, then within-lap time. Classes outside the finite cap/end
span are the automatic pair RL. This is a local corner necessity, not a
whole finite-seed racetrack certificate.
"""
from collections import defaultdict
from search_spiral_caps import *

def check(K):
 ev,end=walk(K);a,b,h=end
 assert h==1
 span=[0,a+b-1]+[x+y for (x,y),h,c in ev];lo=min(span);hi=max(span)
 groups=defaultdict(list)
 for i,((x,y),h,c) in enumerate(ev):groups[x+y].append((x,i,c,(x,y)))
 for s in range(lo,hi+1):
  if s<=0:
   y=s-1;t=4*(y//2)+(1 if y%2==0 else 2)
   groups[s].append((1,t,'L',(1,y)))
   if s<0:
    y=s;t=4*(y//2)+(0 if y%2==0 else 3)
    groups[s].append((0,t,'R',(0,y)))
  if s>=a+b-1:
   x=s-b+1;k=x-a;t=len(K)+4*(k//2)+(1 if k%2==0 else 2)
   groups[s].append((x,t,'L',(x,b-1)))
   if s>=a+b:
    x=s-b;k=x-a;t=len(K)+4*(k//2)+(0 if k%2==0 else 3)
    groups[s].append((x,t,'R',(x,b)))
 bad=[];odd=[]
 for cl,g in sorted(groups.items()):
  g.sort();ww=''.join(c for x,t,c,p in g)
  if any(c!='RL'[j%2] for j,c in enumerate(ww)):bad.append([cl,ww])
  if len(g)%2:odd.append(cl)
 return dict(valid=not bad,bad=bad,odd_classes=odd,span=[lo,hi],end=end)

if __name__=='__main__':
 from corner_chronology import corner_check
 start=time.time();cnt=0
 for K,end in words(17,heading=1):
  r=check(K);r2=corner_check(K)
  assert r['valid']==r2['valid'];assert sorted(r['bad'])==sorted([list(x) for x in r2['bad']])
  cnt+=1
 print('ALL_LOCAL_CHECKS_AGREE',cnt,time.time()-start,flush=True)
 w=json.loads((Path('/workspace/shared/langton/recovered_bundle/ant_global/root/standard.json')).read_text())['word']
 caps=list(words(7,heading=1));tested=0;ok=[]
 for shift in range(len(w)):
  ww=w[shift:]+w[:shift]
  for K,end in caps:
   for cap in (ww+K,K+ww):
    tested+=1;r=check(cap)
    if r['valid']:ok.append(dict(cap=cap,phase=shift,short_cap=K,check=r));print('VALID',json.dumps(ok[-1]),flush=True)
 print('HIGHWAY_CAPS',tested,len(ok),time.time()-start,flush=True)
 (HERE/'highway_decorated_corner_caps.json').write_text(json.dumps(dict(short_max=7,tested=tested,valid=ok,seconds=time.time()-start),indent=2))
