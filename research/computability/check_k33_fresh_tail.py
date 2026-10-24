#!/usr/bin/env python3
"""Complete 425-node local certificate for the k33 rectangular record tail.
All untouched cells below row0 are allowed arbitrary initial colors.
"""
from pathlib import Path
from collections import Counter
import hashlib,json
D=((0,1),(1,0),(0,-1),(-1,0));F='RRRRLR';G='RRRLLLLRLR'
def imprint(w):
 x=y=h=0;board={}
 for c in w:
  bit=int(c=='L');old=board.get((x,y))
  if old is None and y>=0:old=0
  if old is not None and bit!=old:return None
  board[x,y]=1-bit;h=(h+(1 if bit==0 else -1))%4
  x+=D[h][0];y+=D[h][1]
 return board,(x,y,h)
def certify():
 assert imprint(G+F) is None
 initial,pose=imprint(F+G);assert pose==(-2,2,0)
 target=(8,10,8,7);board=dict(initial);counts=[0]*4;nodes=[];accepted=[]
 def visit(x,y,h,word):
  old=board.get((x,y))
  options=[old] if old is not None else ([0] if y>=0 else [0,1])
  node=dict(word=word,pose=[x,y,h],counts=list(counts),options=options,pruned=[])
  nodes.append(node)
  if len(word)==33:accepted.append(node);return
  for bit in options:
   d=(h+(1 if bit==0 else -1))%4
   if counts[d]==target[d]:node['pruned'].append(d);continue
   counts[d]+=1;board[x,y]=1-bit
   visit(x+D[d][0],y+D[d][1],d,word+'RL'[bit])
   counts[d]-=1
   if old is None:board.pop((x,y),None)
   else:board[x,y]=old
 visit(*pose,'')
 assert not accepted and len(nodes)==425
 return dict(status='EXACT LOCAL EXCLUSION',tail=F+G,initial_pose=list(pose),fixed_output_board=[[x,y,c] for (x,y),c in sorted(initial.items())],untouched_white_y_at_least=0,target_counts_NE_SW=list(target),nodes=len(nodes),max_legal_extension=max(len(n['word']) for n in nodes),pruned_direction_counts=dict(Counter(d for n in nodes for d in n['pruned'])),tree=nodes)
if __name__=='__main__':
 out=certify();path=Path(__file__).with_suffix('.json');path.write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({k:v for k,v in out.items() if k!='tree'}));print('sha256',hashlib.sha256(path.read_bytes()).hexdigest())
