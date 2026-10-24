import json,sys
sys.path.insert(0,'/workspace/shared/langton/word_stabilization')
from verify_macro_word import D
DIR=((0,1),(1,0),(0,-1),(-1,0))
def rot(x,y,h):
 for _ in range(h):x,y=y,-x
 return x,y
def center(x,y,h):
 f=DIR[h];r=DIR[(h+1)%4];return 2*x+f[0]-r[0],2*y+f[1]-r[1]
S=json.load(open('/workspace/shared/langton/causal_reduction/five_macro_depth_samples.json'))
for sample in S:
 w=sample['word'];x=y=h=0;old=center(x,y,h);seen={old:0}
 for i,m in enumerate(w):
  dx,dy,dh=D[m]['end_pose'];dx,dy=rot(dx,dy,h);x+=dx;y+=dy;h=(h+dh)%4;c=center(x,y,h)
  if c!=old:
   if c in seen:print('RETURN',w[:i+1],seen[c],i+1,c);break
   seen[c]=i+1
  old=c
else:print('SAMPLED WORDS',len(S))
