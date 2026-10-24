#!/usr/bin/env python3
"""Complete local continuation trees for the two k21 fresh-row tails."""
from pathlib import Path
from collections import Counter
import hashlib,json
D=((0,1),(1,0),(0,-1),(-1,0));F='RRRRLR';G='RRRLLLLRLR'
def imprint(w):
 x=y=h=0;board={}
 for c in w:
  bit=int(c=='L');old=board.get((x,y))
  if old is None and y>=0:old=0
  assert old is None or bit==old
  board[x,y]=1-bit;h=(h+(1 if bit==0 else -1))%4;x+=D[h][0];y+=D[h][1]
 return board,(x,y,h)
def tree(tail):
 initial,pose=imprint(tail);assert pose==(-1,1,0)
 target=(5,7,5,4);board=dict(initial);counts=[0]*4;nodes=[];accepted=[]
 def visit(x,y,h,word):
  old=board.get((x,y));options=[old] if old is not None else ([0] if y>=0 else [0,1])
  node=dict(word=word,pose=[x,y,h],counts=list(counts),options=options,pruned=[]);nodes.append(node)
  if len(word)==21:accepted.append(node);return
  for bit in options:
   d=(h+(1 if bit==0 else -1))%4
   if counts[d]==target[d]:node['pruned'].append(d);continue
   counts[d]+=1;board[x,y]=1-bit
   visit(x+D[d][0],y+D[d][1],d,word+'RL'[bit]);counts[d]-=1
   if old is None:board.pop((x,y),None)
   else:board[x,y]=old
 visit(*pose,'');assert not accepted
 return dict(tail=tail,initial_pose=pose,fixed_output_board=[[x,y,c] for (x,y),c in sorted(initial.items())],target_counts_NESW=target,nodes=len(nodes),max_legal_extension=max(len(n['word']) for n in nodes),tree=nodes)
def main():
 # Any nonempty same-height suffix after F with only one S remaining must
 # have4 moves. All four are forced; they actually use two S.
 board,(x,y,h)=imprint(F);word='';directions=[]
 for _ in range(4):
  bit=board.get((x,y),0 if y>=0 else None);assert bit is not None
  word+='RL'[bit];board[x,y]=1-bit;h=(h+(1 if bit==0 else -1))%4
  directions.append(h);x+=D[h][0];y+=D[h][1]
 assert word=='RRRL' and directions==[1,2,3,2]
 tails=[tree(F),tree(G)];assert [r['nodes'] for r in tails]==[166,149]
 out=dict(status='EXACT LOCAL EXCLUSION',post_F_forced_word=word,post_F_directions=directions,untouched_white_y_at_least=0,tails=tails)
 path=Path(__file__).with_suffix('.json');path.write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({**out,'tails':[{k:v for k,v in r.items() if k!='tree'} for r in tails]}));print('sha256',hashlib.sha256(path.read_bytes()).hexdigest())
if __name__=='__main__':main()
