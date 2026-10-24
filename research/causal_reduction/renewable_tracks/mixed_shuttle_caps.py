"""Exact separated-endcap conditions for W20-west/S-east row shuttles.
The prospective full front is W20^n K S^n J with drift (0,4).
K goes (0,0,E)->(0,4,E); J is pose-return from E. No cap exists here yet.
"""
from search_spiral_caps import *
from collections import defaultdict
W='LLRLRRRRLRRRRLLLLRLL';S='RLLR'
WE,we=walk(W,(0,0,1));SE,se=walk(S,(0,0,1))
assert we==(-2,0,1) and se==(2,0,1)

def histories(cap,side):
 ce,en=walk(cap,(0,0,1));assert en==((0,4,1) if side=='left' else (0,0,1))
 # Infinite arms from right for left cap, from left for right cap.
 # Left: incoming W epochs from x=2k,k>=1; outgoing S starts x=2k,y=4.
 # Right: incoming S starts x=-2k,k>=1; outgoing W starts x=-2k,y=0.
 I,O=(WE,SE) if side=='left' else (SE,WE)
 step=2 if side=='left' else -2;OY=4 if side=='left' else 0
 xs=[p[0] for p,h,c in ce]+[p[0]+step for p,h,c in I]+[p[0] for p,h,c in O]
 lo=min(xs)-4;hi=max(xs)+4;hist={}
 for x in range(lo,hi+1):
  groups=defaultdict(list)
  for i,((a,b),h,c) in enumerate(I):
   z=x-a
   if z%step==0 and z//step>=1:
    k=z//step;groups[b%4].append((-b,-len(I)*k+i,c,'I',i,k))
  for i,((a,b),h,c) in enumerate(ce):
   if a==x:groups[b%4].append((-b,i,c,'K',i,0))
  for i,((a,b),h,c) in enumerate(O):
   z=x-a
   if z%step==0 and z//step>=0:
    k=z//step;B=b+OY;groups[B%4].append((-B,len(cap)+len(O)*k+i,c,'O',i,k))
  for r,g in groups.items():g.sort();hist[x,r]=g
 return hist

def test(cap,side):
 hist=histories(cap,side);bad=[];odd=[]
 for cl,g in hist.items():
  cs=''.join(e[2] for e in g)
  if cs[0]!='R' or any(a==b for a,b in zip(cs,cs[1:])):bad.append((cl,cs))
  if len(cs)%2:odd.append(cl)
 return dict(word=cap,bad_count=len(bad),bad=bad,odd=odd,net_R=cap.count('R')-cap.count('L'))

if __name__=='__main__':
 hi=int(sys.argv[1]) if len(sys.argv)>1 else 16;t=time.time();out={}
 for side,disp in [('left',(0,4)),('right',(0,0))]:
  count=0;best=1000000;bestwords=[];success=[]
  # words() uses N; rotation to E maps (x,y)->(y,-x), so left needs(-4,0).
  for w,en in words(hi,heading=0,disp=((-4,0) if side=='left' else (0,0))):
   count+=1;r=test(w,side)
   if r['bad_count']<best:best=r['bad_count'];bestwords=[]
   if r['bad_count']==best and len(bestwords)<20:bestwords.append(r)
   if not r['bad_count']:success.append(r);print('CANDIDATE',side,json.dumps(r),flush=True)
  out[side]=dict(count=count,best=best,bestwords=bestwords,candidates=success)
  print('SIDE',side,count,best,len(success),time.time()-t,flush=True)
 (HERE/f'mixed_shuttle_caps_{hi}.json').write_text(json.dumps(dict(max_length=hi,results=out,seconds=time.time()-t),indent=2))
