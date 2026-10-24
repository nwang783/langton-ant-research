"""Exact uncapped WHITE outer L/K at the signed five-mode Q square.
Finite domains follow exact two-port counts, not a multiplicity cutoff.
"""
from pathlib import Path
from itertools import combinations,product
from collections import Counter,defaultdict,deque
import json
b=Path(__file__).parent;S={'__file__':str(b/'check_terminal_LL_upper_side_collision.py')};exec((b/'check_terminal_LL_upper_side_collision.py').read_text().split('# Shift the physical Q')[0],S)
analyze,out=S['analyze'],S['out']
def sparse(axis,n,k):
 for pos in combinations(range(n),k):
  p=set(pos);yield ''.join(axis[0] if r in p else axis[1] for r in range(n))
Ls=[h for n in range(2,9) for h in sparse('WE',n,2) if sum(out(h,r)=='S' for r in range(n))==2]
assert len(Ls)==18
Ks={}
for m in sorted({h.count('E') for h in Ls}):
 Ks[m]=[h for n in range(2,2*(2+m)+2) for h in sparse('NS',n,2) if sum(out(h,r)=='E' for r in range(n))==m]
tops=[('SNN','SSNN','EE'),('SNN','SSNN','EEW'),('SNNS','SNN','WWE'),('SNNS','SNNS','WWEE'),('SNNS','SSNN','EEWW')]
def calendar(hs,cert):
 ev={(p,r) for p,h in hs.items() for r in range(len(h))}
 su={(tuple(a[0]),a[1]):(tuple(e[0]),e[1]) for a,e in cert['successor_edges']}
 pred={e:a for a,e in su.items()};cs=[];ci={}
 for e in sorted(ev):
  if e in pred:continue
  comp=[];cur=e;i=len(cs)
  while cur not in ci:
   comp.append(cur);ci[cur]=i
   if cur not in su:break
   cur=su[cur]
  cs.append(comp)
 assert set(ci)==ev
 adj=defaultdict(set);degree=[0]*len(cs)
 for p,h in hs.items():
  for r in range(len(h)-1):
   a,e=ci[p,r],ci[p,r+1]
   if a!=e and e not in adj[a]:adj[a].add(e);degree[e]+=1
 ready=deque(i for i,d in enumerate(degree) if d==0);order=[]
 while ready:
  i=ready.popleft();order.append(i)
  for e in adj[i]:
   degree[e]-=1
   if degree[e]==0:ready.append(e)
 assert len(order)==len(cs)
 phase=lambda p:2*(p[0]%2) if sum(p)%2==0 else 3-2*(p[0]%2)
 times={};end=-128
 for i in order:
  start=end+128;start+=(phase(cs[i][0][0])-start)%4
  for k,e in enumerate(cs[i]):times[e]=start+k
  end=start+len(cs[i])-1
 assert len(set(times.values()))==len(ev)
 assert all(times[e]==times[a]+1 for a,e in su.items())
 assert all(times[p,r]-times[p,r-1]>=4 for p,h in hs.items() for r in range(1,len(h)))
 assert all(times[e]%4==phase(e[0]) for e in ev)
 return dict(components=cs,order=order,times=[[e,t] for e,t in sorted(times.items())])
ct=Counter();pr=Counter();ans=[]
for (r,a,z),ll in product(tops,Ls):
 for k in Ks[ll.count('E')]:
  hs={(-2,-1):'EEWW',(-1,-1):'SNNS',(0,-1):'WWEE',(1,-1):r,(0,0):a,(1,0):z,(-1,0):ll,(-2,0):k}
  res,cert=analyze(hs);ct[res]+=1;pr[(r,a,z),res]+=1
  if res=='open':
   values={tuple(p):h for p,h in cert['face_values']}
   assert values[(-2,0)]==-(len(ll)-2) and len(ll) in [7,8] and len(k)>=6
   ans.append(dict(R=r,U=a,W=z,L=ll,K=k,histories={str(p):h for p,h in sorted(hs.items())},certificate=cert,finite_event_calendar=calendar(hs,cert)))
assert ct=={'rank':7998,'clock':108,'higher_C':86,'open':18}
assert len({(r['L'],r['K']) for r in ans})==9
print('L',len(Ls),'K',{m:len(z) for m,z in Ks.items()},'counts',dict(ct),'open',len(ans));print('18 necessary shields, nine outer pairs, L7/8 and K6..8, low L=M-5/M-6; all finite calendars distinct')
Path(__file__).with_suffix('.json').write_text(json.dumps(dict(scope=__doc__,L_domain=Ls,K_domains=Ks,counts=dict(ct),profile_counts={str(k):v for k,v in pr.items()},open=ans),indent=2)+'\n')
