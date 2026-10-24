"""Challenge fixed-cap rigidity by allowing periodic changing corner states.
All caps share the same geometric endpoint, so their side rails line up.
A valid local corner is not a complete racetrack or finite-seed countermodel.
"""
from exact_corner_chronology import *

def check_sequence(caps):
 q=len(caps);data=[walk(K) for K in caps];ends=[e for ev,e in data]
 assert len(set(ends))==1 and ends[0][2]==1
 a,b,h=ends[0];span=[0,a+b-1]+[x+y for ev,en in data for (x,y),h,c in ev];lo=min(span);hi=max(span)
 groups=defaultdict(list)
 for k,(K,(ev,en)) in enumerate(zip(caps,data)):
  def add(x,y,t,c):groups[(x+y,(x-k)%q)].append((x-k,k,t,c))
  for i,((x,y),h,c) in enumerate(ev):add(x,y,i,c)
  for s in range(lo,hi+1):
   if s<=0:
    y=s-1;add(1,y,4*(y//2)+(1 if y%2==0 else 2),'L')
    if s<0:
     y=s;add(0,y,4*(y//2)+(0 if y%2==0 else 3),'R')
   if s>=a+b-1:
    x=s-b+1;j=x-a;add(x,b-1,len(K)+4*(j//2)+(1 if j%2==0 else 2),'L')
    if s>=a+b:
     x=s-b;j=x-a;add(x,b,len(K)+4*(j//2)+(0 if j%2==0 else 3),'R')
 bad=[];odd=[]
 for cl,g in sorted(groups.items()):
  g.sort();ww=''.join(c for x,k,t,c in g)
  if any(c!='RL'[j%2] for j,c in enumerate(ww)):bad.append([cl,ww])
  if len(g)%2:odd.append(cl)
 return dict(valid=not bad,bad=bad,odd_classes=odd)

if __name__=='__main__':
 maxlen=int(sys.argv[1]) if len(sys.argv)>1 else 13
 start=time.time();byend=defaultdict(list);total=0
 for K,end in words(maxlen,heading=1):
  total+=1
  if feasible(S*(2*maxlen)+K+S*(2*maxlen)):
   assert check_sequence([K])['valid']==check(K)['valid']
   byend[end].append(K)
 tested=0;ok=[]
 for end,ks in byend.items():
  for i,K in enumerate(ks):
   for J in ks[i:]:
    tested+=1;r=check_sequence([K,J])
    if r['valid']:
     rec=dict(caps=[K,J],end=end,check=r);ok.append(rec);print('VALID',json.dumps(rec),flush=True)
 print('DONE',total,sum(map(len,byend.values())),tested,len(ok),time.time()-start,flush=True)
 (HERE/f'period2_corner_states_{maxlen}.json').write_text(json.dumps(dict(capmax=maxlen,total_caps=total,locally_feasible=sum(map(len,byend.values())),geometric_ports=len(byend),tested_pairs=tested,valid=ok,seconds=time.time()-start),indent=2))
