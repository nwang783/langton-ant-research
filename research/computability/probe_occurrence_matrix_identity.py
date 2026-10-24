#!/usr/bin/env python3
"""Occurrence-dependent literal ant CSP for a PURE matrix identity.
No constant image controller and no heading-preservation assumption.
SAT means only a finite prefix; a cap or greedy dead end is never global UNSAT.
"""
from pathlib import Path
import argparse,itertools,json,time
D=((0,1),(1,0),(0,-1),(-1,0))
def trace(word,h):
 x=y=0;board={};positions=[(0,0)];seed=[]
 for c in word:
  bit=int(c=='L');old=board.get((x,y))
  if old is not None and old!=bit:return None
  if old is None and bit:seed.append((x,y))
  board[x,y]=1-bit;h=(h+(1 if bit==0 else -1))%4;x+=D[h][0];y+=D[h][1];positions.append((x,y))
 return board,positions,h,seed
def solve(k,A,sign,h0,root,length,cap):
 initial=trace(root,h0);assert initial
 board,positions,h,seed=initial;nodes=0;capped=False
 def target(p):return sign*(A[0][0]*p[0]+A[0][1]*p[1]),sign*(A[1][0]*p[0]+A[1][1]*p[1])
 assert positions[k]==target(positions[1])
 def dfs(x,y,h,word):
  nonlocal nodes,capped
  nodes+=1
  if nodes>cap:capped=True;return None
  t=len(word)
  if t==length:return word
  block=t//k;end=(block+1)*k;tx,ty=target(positions[block+1])
  old=board.get((x,y));options=[old] if old is not None else [0,1]
  for bit in options:
   hh=(h+(1 if bit==0 else -1))%4;xx=x+D[hh][0];yy=y+D[hh][1];remaining=end-t-1
   horizontal=(remaining+(hh%2==0))//2;vertical=remaining-horizontal
   delta_x,delta_y=tx-xx,ty-yy
   if abs(delta_x)>horizontal or abs(delta_y)>vertical or (horizontal-delta_x)%2 or (vertical-delta_y)%2:continue
   board[x,y]=1-bit;positions.append((xx,yy));ans=dfs(xx,yy,hh,word+'RL'[bit]);positions.pop()
   if old is None:board.pop((x,y),None)
   else:board[x,y]=old
   if ans is not None:return ans
   if capped:return None
  return None
 start=time.monotonic();ans=dfs(*positions[-1],h,root)
 out=dict(sign=sign,heading=h0,root=root,status='SAT PREFIX' if ans else 'UNKNOWN CAP' if capped else 'ENTIRE ROOT UNSAT TO HORIZON',nodes=nodes,seconds=time.monotonic()-start)
 if ans:
  _,ps,_,seed=trace(ans,h0)
  assert all(ps[k*n]==target(ps[n]) for n in range(length//k+1))
  out.update(word=ans,seed=seed,seed_size=len(seed))
 return out
def main(k,A,length,cap):
 path=Path(__file__).with_name(f'occurrence_matrix_k{k}_{A[0][0]}_{A[0][1]}_{A[1][0]}_{A[1][1]}_n{length}.json');records=[]
 for sign in [1,-1]:
  for h0 in [0,1]:
   for letters in itertools.product('RL',repeat=k):
    root=''.join(letters);r=trace(root,h0)
    if r is None:continue
    ps=r[1];x,y=ps[1];target=(sign*(A[0][0]*x+A[0][1]*y),sign*(A[1][0]*x+A[1][1]*y))
    if ps[k]!=target:continue
    ans=solve(k,A,sign,h0,root,length,cap);records.append(ans)
    path.write_text(json.dumps(dict(k=k,A=A,horizon=length,nodecap_per_root=cap,records=records),indent=2)+'\n')
    print(json.dumps({k:v for k,v in ans.items() if k not in ['word','seed']}),flush=True)
 print('TOTAL',len(records),'SAT',sum(r['status']=='SAT PREFIX' for r in records),'UNKNOWN',sum(r['status']=='UNKNOWN CAP' for r in records))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--length',type=int,default=81);p.add_argument('--cap',type=int,default=1000000);z=p.parse_args();main(9,((3,2),(2,5)),z.length,z.cap)
