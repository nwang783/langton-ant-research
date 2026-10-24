#!/usr/bin/env python3
"""Independent literal invariant verifier, row-major colors and vector headings."""
import hashlib,json,time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
p=ROOT/'frontier_exploration/barrier_h9_w11.hex'
data=p.read_bytes()
assert hashlib.sha256(data).hexdigest()=='04ec386f8d519687306a073b3ead9cb859109f133c62ae2ff34f132a3c4058c4'
H,W=9,11
raw=[int(s,16) for s in data.splitlines()]
assert len(raw)==len(set(raw))==275057 and 0 in raw
assert all(0<=m<1<<(H*W) for m in raw)
def transpose(m):
 r=0
 while m:
  b=m&-m;i=b.bit_length()-1;x,y=divmod(i,H)
  r|=1<<(y*W+x);m-=b
 return r
S={transpose(m) for m in raw}
assert len(S)==len(raw)
counts={'left':0,'vertical':0}; longest=0;t=time.monotonic()
for original in S:
 for row in (1,3,5,7):
  colors=original;x,y=0,row;dx,dy=1,0;steps=0
  while 0<=x<W and 0<=y<H:
   bit=1<<(y*W+x)
   if colors&bit:dx,dy=-dy,dx
   else:dx,dy=dy,-dx
   colors^=bit;x+=dx;y+=dy;steps+=1
   # A failed bound rejects, never silently accepts or truncates.
   assert steps<=171
  longest=max(longest,steps)
  if not 0<=y<H:counts['vertical']+=1
  else:
   assert x==-1 and dx==-1 and dy==0,(original,row,x,y)
   assert colors in S
   counts['left']+=1
assert counts=={'left':686294,'vertical':413934} and longest==171
result=dict(status='PASS',certificate_sha256=hashlib.sha256(data).hexdigest(),states=len(S),checked_entries=4*len(S),counts=counts,max_steps=longest,elapsed_seconds=time.monotonic()-t)
(ROOT/'audits/strip_barrier_independent.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
