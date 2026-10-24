#!/usr/bin/env python3
"""Necessary local test only for k33,diag(3,11) fresh-record saturation.
An accepted extension is not a full inflation model or a finite seed witness.
"""
import itertools,json,time
from pathlib import Path
D=((0,1),(1,0),(0,-1),(-1,0))
FG='RRRRLRRRRLLLLRLR'
def realize(ds,h):
 x=y=0;board={};last={};word=''
 for d in ds:
  bit=0 if (d-h)%4==1 else 1
  if (d-h)%4 not in (1,3):return None
  old=board.get((x,y))
  if old is None and y>=9:old=0
  if old is not None and old!=bit:return None
  board[x,y]=1-bit;word+='RL'[bit];x+=D[d][0];y+=D[d][1];h=d
 return board,(x,y,h),word
def search(board,pose,cap=33):
 x0,y0,h0=pose;nodes=0;target=(8,10,8,7);counts=[0]*4
 def dfs(x,y,h,word):
  nonlocal nodes
  nodes+=1
  if len(word)==cap:return word if (x,y)==(x0+3,y0) else None
  old=board.get((x,y));options=(old,) if old is not None else ((0,) if y>=9 else (0,1))
  for bit in options:
   d=(h+(1 if bit==0 else -1))%4
   if counts[d]>=target[d]:continue
   counts[d]+=1;board[x,y]=1-bit
   result=dfs(x+D[d][0],y+D[d][1],d,word+'RL'[bit])
   counts[d]-=1
   if old is None:board.pop((x,y),None)
   else:board[x,y]=old
   if result is not None:return result
  return None
 return dfs(x0,y0,h0,''),nodes
def main():
 started=time.monotonic();legal=0;records=[];total=0
 # Prefix has nine N moves, eight horizontal moves, net horizontal +2.
 for ws in itertools.combinations(range(8),3):
  prefix=[0]
  for j in range(8):prefix.extend([3 if j in ws else 1,0])
  ds=list(prefix);h=0
  for c in FG:h=(h+(1 if c=='R' else -1))%4;ds.append(h)
  for h0 in [1,3]:
   r=realize(ds,h0)
   if r is None:continue
   legal+=1;board,pose,word=r
   assert len(word)==33 and pose==(0,11,0)
   extension,nodes=search(board,pose);total+=nodes
   rec=dict(prefix_west_slots=ws,heading=h0,predecessor=word,extension=extension,nodes=nodes)
   records.append(rec)
   if extension is not None:
    out=dict(status='LOCAL SURVIVOR, NOT A MODEL',legal_predecessors_tested=legal,nodes=total,witness=rec,seconds=time.monotonic()-started)
    break
  else:continue
  break
 else:out=dict(status='ALL LOCAL PREDECESSOR-RECORD PAIRS EXCLUDED',legal_predecessors=legal,nodes=total,records=records,seconds=time.monotonic()-started)
 Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
if __name__=='__main__':main()
