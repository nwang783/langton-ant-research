"""Discover and exactly certify translating fronts on A's infinite periodic wake.
These are not finite-support initial configurations and not counterexamples.
"""
from collections import Counter
import json
D=[(0,1),(1,0),(0,-1),(-1,0)]
def bg(p):
 x,y=p
 return y in (0,-2) or (y==-1 and x%2==1)
def solve(start,T=12000):
 x,y,h=start;flips=set();words=[];poses=[]
 for t in range(T):
  poses.append((x,y,h));p=(x,y);a=-1 if bg(p) ^ (p in flips) else 1
  words.append('R' if a==1 else 'L')
  if p in flips:flips.remove(p)
  else:flips.add(p)
  h=(h+a)%4;dx,dy=D[h];x+=dx;y+=dy
 poses.append((x,y,h));word=''.join(words)
 for q in range(1,513):
  if word[-4*q:] != word[-q:]*4:continue
  p0=poses[T-q];p1=poses[T];v=(p1[0]-p0[0],p1[1]-p0[1])
  if p1[2]!=p0[2] or not v[0] or v[1]!=0:continue
  if v[0]>0:continue
  w=word[-q:];reads=[(p[0],p[1]) for p in poses[T-q:T]]
  entry=flips.copy()
  for p in reads:
   if p in entry:entry.remove(p)
   else:entry.add(p)
  # Translate the output delta back to entry coordinates.
  back={(a-v[0],b-v[1]) for a,b in flips}
  mismatch=entry^back
  bound={}
  k=-v[0]
  for a,b in reads:bound[b,a%k]=max(bound.get((b,a%k),-10**20),a)
  bad=[p for p in mismatch if (p[1],p[0]%k) in bound and p[0]<=bound[p[1],p[0]%k]]
  if bad:continue
  # Exact first period was replayed, background is v-invariant, and every
  # future-read cell matches the shifted entry. Induction certifies infinity.
  toggles=Counter((a%k,b) for a,b in reads)
  ys=range(min([-2]+[p[1] for p in reads])-1,max([0]+[p[1] for p in reads])+2)
  output={str(b):[int(bg((r,b)))^(toggles[r,b]%2) for r in range(k)] for b in ys}
  return {'start':start,'entry_time':T-q,'entry_pose':p0,'period':q,'drift':v,'word':w,'exact_future_union_check':True,'bulk_output_rows':output,'entry_flip_count':len(entry)}
 return None
out=[]
for y in range(-6,5):
 for x in [0,1]:
  for h in range(4):
   if h%2!=(x+y)%2:continue
   z=solve((x,y,h))
   if z:out.append(z);print(json.dumps(z),flush=True)
report={'scope':'infinite A-wake input only','starts':44,'certified_west_fronts':out}
open('/workspace/shared/langton/core_periodicity_new/a_wake_fronts.json','w').write(json.dumps(report,indent=2))
