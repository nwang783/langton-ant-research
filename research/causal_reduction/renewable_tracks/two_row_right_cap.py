"""Explore the exact two-row input interface for right-cap height [-1,4].
Width bound is on finite input bits, not on cap words. UNKNOWN stays unknown.
"""
from height4_right_cap import *

def run_two(mask,M,budget=2000):
 x=y=0;h=1;changed=set();w=[];returns=[];D=((0,1),(1,0),(0,-1),(-1,0));minx=0;charge=0
 for t in range(budget):
  p=x,y;base=(y==0 and x<0)
  if 0<=x<M and y in (-1,0):base=bool(mask>>(2*x+(y==0))&1)
  black=base^(p in changed);c='L' if black else 'R';w.append(c);charge+=-1 if black else 1;changed.symmetric_difference_update({p});h=(h+(-1 if black else 1))%4;dx,dy=D[h];x+=dx;y+=dy;minx=min(minx,x)
  if (x,y,h)==(0,0,1) and charge>=8:returns.append(''.join(w))
  if y<-1 or y>4:return 'HEIGHT_EXIT',w,returns,(x,y,h)
  if y==0 and h==0 and x<=-2:
   if not any((b==0 and a<=x) or (b==-1 and a<=x-1) for a,b in changed):return 'S_ESCAPE',w,returns,(x,y,h)
  if y==0 and h==1 and x<=-2 and len(w)>=60 and ''.join(w[-60:])==W*3:
   def zone(a,b):return (b==0 and (a<=x-2 or a==x)) or (b==1 and a<=x) or (b in (2,3) and a<=x-1)
   guard={(x,1),(x-1,2)}
   if {p for p in changed if zone(*p)}==guard:return 'W20_ESCAPE',w,returns,(x,y,h)
 return 'UNKNOWN',w,returns,(x,y,h)

if __name__=='__main__':
 M=int(sys.argv[1]) if len(sys.argv)>1 else 6;t0=time.time();counts=Counter();words=set();valid=[];unknown=[];longest=0;maxreturns=0
 for mask in range(1<<(2*M)):
  status,letters,ret,en=run_two(mask,M);counts[status]+=1;longest=max(longest,len(letters));maxreturns=max(maxreturns,len(ret))
  if status=='UNKNOWN':unknown.append(mask)
  for w in ret:
   if w in words:continue
   words.add(w)
   if fast_test(w,'right'):
    cert=test(w,'right');assert not cert['bad_count'];v=dict(mask=mask,word=w,certificate=cert);valid.append(v);print('CANDIDATE',json.dumps(v),flush=True)
 out=dict(M=M,counts=dict(counts),distinct_returns=len(words),max_steps=longest,max_returns=maxreturns,candidates=valid,unknown_masks=unknown,seconds=time.time()-t0)
 (HERE/f'two_row_right_cap_{M}.json').write_text(json.dumps(out,indent=2));print(json.dumps({k:v for k,v in out.items() if k!='unknown_masks'}),flush=True)
 (HERE/f'two_row_right_cap_{M}_words.json').write_text(json.dumps(sorted(words,key=lambda w:(len(w),w)),indent=2))
