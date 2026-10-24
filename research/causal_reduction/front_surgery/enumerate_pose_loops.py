"""Enumerate exact finite-seed-feasible pose-return words, without lift grammar."""
import json,sys
from collections import Counter
from loop_decoration_solver import DIR,HERE

def loops(N):
 out=[];last={}
 def rec(x,y,h,w):
  n=len(w)
  if n and (x,y,h)==(0,0,0):out.append(w)
  if n==N:return
  if abs(x)+abs(y)>N-n:return
  q=(x,y);old=last.get(q);letters=('R','L') if old is None else ('L' if old=='R' else 'R',)
  for c in letters:
   last[q]=c;hh=(h+(1 if c=='R' else -1))%4;dx,dy=DIR[hh];rec(x+dx,y+dy,hh,w+c)
  if old is None:del last[q]
  else:last[q]=old
 rec(0,0,0,'');return out
if __name__=='__main__':
 N=int(sys.argv[1]) if len(sys.argv)>1 else 16;w=loops(N);print(len(w),dict(sorted(Counter(map(len,w)).items())))
 (HERE/f'pose_loops_{N}.json').write_text(json.dumps(w,indent=2))
