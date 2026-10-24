"""Finite-horizon discovery on an INFINITE striped background; not a proof."""
import json,pathlib,collections
D=((0,1),(1,0),(0,-1),(-1,0));HERE=pathlib.Path(__file__).resolve().parent

def trial(start,steps=10000):
 flips=set();x,y,h=start;letters=[];poses=[start]
 for t in range(steps):
  p=x,y;black=((x%2==1)and(0<=y<=5))^(p in flips)
  if p in flips:flips.remove(p)
  else:flips.add(p)
  letters.append('L'if black else'R');h=(h+(-1 if black else 1))%4;dx,dy=D[h];x+=dx;y+=dy;poses.append((x,y,h))
 w=''.join(letters)
 for P in range(4,513,4):
  if w[-P:]!=w[-2*P:-P] or w[-P:]!=w[-3*P:-2*P]:continue
  a,b=poses[-P-1],poses[-1]
  if a[1:]!=b[1:]or a[0]==b[0]:continue
  word=w[-P:];canon=min(word[i:]+word[:i]for i in range(P))
  return dict(start=start,status='PERIOD_CANDIDATE_ONLY',period=P,drift=(b[0]-a[0],0),entry=a,word=word,canonical_word=canon,flips=len(flips),end=b)
 return dict(start=start,status='NO_AXIAL_TAIL_DETECTED',end=(x,y,h),flips=len(flips))
if __name__=='__main__':
 out=[trial((x,y,h))for x in range(2)for y in range(-2,8)for h in range(4)]
 (HERE/'striped_bulk_candidates.json').write_text(json.dumps(out,indent=2));print(collections.Counter(z['status']for z in out))
 groups=collections.defaultdict(list)
 for z in out:
  if z['status']=='PERIOD_CANDIDATE_ONLY':groups[(z['canonical_word'],tuple(z['drift']))].append(z['start'])
 for k,v in groups.items():print(k,len(v),v[:5])
