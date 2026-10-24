"""Exact candidate generation for right caps confined to read rows0..4.
Initial field: black negative half-row y=0 plus arbitrary finite positive bits.
Complete cap verification is still required. Finite simulation caps are UNKNOWN.
"""
from sample_shuttle_caps import fast_test
from mixed_shuttle_caps import *
from collections import Counter

def run(mask,M,budget=10000):
 x=y=0;h=1;changed=set();w=[];D=((0,1),(1,0),(0,-1),(-1,0))
 for t in range(budget):
  p=x,y;base=(y==0 and (x<0 or 0<=x<M and mask>>x&1));black=base^(p in changed)
  c='L' if black else 'R';w.append(c);changed.symmetric_difference_update({p});h=(h+(-1 if black else 1))%4;dx,dy=D[h];x+=dx;y+=dy
  if (x,y,h)==(0,0,1):return 'RETURN',''.join(w),(x,y,h)
  if y<0 or y>4:return 'HEIGHT_EXIT',''.join(w),(x,y,h)
 return 'UNKNOWN',''.join(w),(x,y,h)

if __name__=='__main__':
 M=int(sys.argv[1]) if len(sys.argv)>1 else 16;t0=time.time();counts=Counter();words=set();valid=[];unknown=[];longest=0
 # A0 must be black, or first R exits the allowed strip.
 for mask in range(1,1<<M,2):
  status,w,en=run(mask,M);counts[status]+=1;longest=max(longest,len(w))
  if status=='UNKNOWN':unknown.append(mask)
  if status=='RETURN' and w not in words:
   words.add(w)
   if fast_test(w,'right'):
    cert=test(w,'right');assert not cert['bad_count'];v=dict(mask=mask,word=w,certificate=cert);valid.append(v);print('CANDIDATE',json.dumps(v),flush=True)
 out=dict(M=M,counts=dict(counts),distinct_returns=len(words),max_steps=longest,candidates=valid,unknown_masks=unknown,seconds=time.time()-t0)
 (HERE/f'height4_right_cap_{M}.json').write_text(json.dumps(out,indent=2));print(json.dumps(out),flush=True)
 (HERE/f'height4_right_cap_{M}_words.json').write_text(json.dumps(sorted(words,key=lambda w:(len(w),w)),indent=2))
