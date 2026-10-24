"""Exact local complete-history test for a W20 expanding NE corner.
Incoming drift N (entry heading S), outgoing drift W (entry heading E),
corner translation (3,3) per lap. Full finite-seed racetrack NOT certified.
"""
from search_spiral_caps import *
from collections import defaultdict,Counter
W='LLRLRRRRLRRRRLLLLRLL'
IN,ie=walk(W,(0,0,2));OUT,oe=walk(W,(0,0,1))
assert ie==(0,2,2) and oe==(-2,0,1)

def histories(K):
 cap,end=walk(K,(0,0,2));a,b,h=end
 assert h==1
 crit=[x-y for (x,y),h,c in cap]+[x-y+2 for (x,y),h,c in IN]+[a-b+x-y for (x,y),h,c in OUT]
 lo=min(crit)-6;hi=max(crit)+6;hist={}
 for s in range(lo,hi+1):
  groups=defaultdict(list)
  for i,((x,y),h,c) in enumerate(IN):
   z=s-(x-y)
   if z%2==0 and z>=2:
    k=z//2;groups[x%3].append((-x,-20*k+i,c,'I',i,k))
  for i,((x,y),h,c) in enumerate(cap):
   if x-y==s:groups[x%3].append((-x,i,c,'K',i,0))
  for i,((x,y),h,c) in enumerate(OUT):
   z=(a-b+x-y)-s
   if z%2==0 and z>=0:
    k=z//2;X=a+x-2*k;groups[X%3].append((-X,len(K)+20*k+i,c,'O',i,k))
  for r,g in groups.items():g.sort();hist[s,r]=g
 return hist,end

def test(K):
 hist,end=histories(K);bad=[];odd=[]
 for cl,g in hist.items():
  cs=''.join(e[2] for e in g)
  if cs[0]!='R' or any(a==b for a,b in zip(cs,cs[1:])):bad.append((cl,cs))
  if len(cs)%2:odd.append(cl)
 return dict(word=K,end=end,bad_count=len(bad),first_bad=bad[:3],odd=odd,net_R=K.count('R')-K.count('L'))

if __name__=='__main__':
 hi=int(sys.argv[1]) if len(sys.argv)>1 else 17
 t=time.time();count=0;out=[];best=1000000;bestwords=[]
 for K,en in words(hi,heading=3):
  count+=1;r=test(K)
  if r['bad_count']<best:best=r['bad_count'];bestwords=[]
  if r['bad_count']==best and len(bestwords)<20:bestwords.append(r)
  if r['bad_count']==0:out.append(r);print('CANDIDATE',json.dumps(r),flush=True)
 print('DONE',count,len(out),'best',best,time.time()-t,flush=True)
 (HERE/f'w20_corner_caps_{hi}.json').write_text(json.dumps(dict(capmax=hi,count=count,candidates=out,best=best,bestwords=bestwords,seconds=time.time()-t),indent=2))
