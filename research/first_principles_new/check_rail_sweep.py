"""Literal local certificate for a sector-sensitive rail transfer.
No blank-board or random seed search is used.
"""
import json
from pathlib import Path
P=Path(__file__).resolve().parent
DXY=((0,1),(1,0),(0,-1),(-1,0))
A='RRLRRRRL'; D='RLLLLRLL'

def spec(word,pose):
 x,y,h=pose; first={}; parity={}; reads=[]
 for a in word:
  p=(x,y);b=int(a=='L');need=b^parity.get(p,0)
  if p in first: assert first[p]==need,(word,pose,p)
  else:first[p]=need
  parity[p]=1^parity.get(p,0);reads.append((x,y,h,a))
  h=(h+(1 if a=='R' else -1))%4;dx,dy=DXY[h];x+=dx;y+=dy
 return first,{p for p,v in parity.items() if v},(x,y,h),reads

def replay(word,black,pose):
 black=set(black);x,y,h=pose
 for a in word:
  p=x,y; assert (p in black)==(a=='L'),(p,h,a)
  if p in black:black.remove(p)
  else:black.add(p)
  h=(h+(1 if a=='R' else -1))%4;dx,dy=DXY[h];x+=dx;y+=dy
 return black,(x,y,h)

f,mask,end,reads=spec(A,(0,0,0))
assert end==(2,0,0)
assert {p for p,b in f.items() if b}=={(1,-1)}
assert mask=={(0,0),(1,0),(1,-2),(2,-2)}
assert D==''.join('L' if a=='R' else 'R' for a in A[::-1])
checks=[]
for n in [1,2,3,4,8,16,32,100]:
 seed={(2*k+1,-1) for k in range(n)}
 dense=seed|{(x,0) for x in range(2*n)}|{(x,-2) for x in range(1,2*n+1)}
 out,pose=replay(A*n,seed,(0,0,0));assert out==dense and pose==(2*n,0,0)
 out2,pose2=replay(D*n,dense,(2*n,-1,2));assert out2==seed and pose2==(0,-1,2)
 assert (sum(pose[:2])+pose[2])%2==0
 assert (2*n-1+2)%2==1
 checks.append(n)
# Full infinite bulk first-read constraints for D (one westward period).
fD,mD,endD,readsD=spec(D,(0,0,2))
# An aligned reverse at (even,-1,S) has opposite sector. Every sector0
# horizontal shift of that alignment is odd, and hence mismatches a middle
# first read of D. Vertical shifts +/-1 require a black exterior rail.
def dense(p):
 x,y=p;return int(y in (0,-2) or y==-1 and x%2==1)
rejections=[]
for pose in [(1,-1,2),(-1,-1,2),(0,0,2),(0,-2,2)]:
 ff,_,_,_=spec(D,pose)
 bad=sorted((p,v,dense(p)) for p,v in ff.items() if v!=dense(p))
 assert bad and (sum(pose[:2])+pose[2])%2==0
 rejections.append({'pose':pose,'conflicts':bad})
out={'status':'PASS','east_word':A,'west_reverse_word':D,
 'east_local_reads':reads,'east_toggle':sorted(mask),'finite_induction_controls':checks,
 'reverse_local_reads':readsD,'sector_compatible_nearest_shift_conflicts':rejections,
 'scope':'The finite controls check the stated symbolic induction. Nearest shifts only; no arbitrary-front exclusion.'}
(P/'rail_sweep.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
