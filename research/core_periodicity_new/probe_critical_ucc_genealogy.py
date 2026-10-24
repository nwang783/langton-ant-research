"""Discovery only: exact raw finite-word controls for tight UCC ancestry.
No negative result from a depth bound is a mathematical exclusion.
"""
import json,sys
from pathlib import Path
G=json.load(open('chronology_dcuv/literal_residual_geometry.json'))['geometry'];T=(0,1,4,5,6,7,8,9);D=((0,1),(1,0),(0,-1),(-1,0));limit=int(sys.argv[1])if len(sys.argv)>1 else 12
# Coordinate paths are literal, with first-read seed choices shared globally.
def walk(a,p,h,colors,watch=None):
 change=[]
 for c in a:
  if watch==p:
   for q,old in reversed(change):
    if old is None:colors.pop(q,None)
    else:colors[q]=old
   return None
  before=c=='L'
  if p in colors and colors[p]!=before:
   for q,old in reversed(change):
    if old is None:colors.pop(q,None)
    else:colors[q]=old
   return None
  change.append((p,colors.get(p)));colors[p]=not before;h=(h+(1 if c=='R'else-1))%4;p=(p[0]+D[h][0],p[1]+D[h][1])
 return p,h,change
def undo(ch,colors):
 for q,old in reversed(ch):
  if old is None:colors.pop(q,None)
  else:colors[q]=old
answers=[]
for slot in [(-1,7),(0,7)]:
 colors={};p,h,ch=walk(G[9]['word'],(0,0),0,colors);target=(slot[0],slot[1]-3);nodes=0;found=None
 def dfs(p,h,k,path):
  global nodes,found
  nodes+=1
  if k==2 and p==target and h==0:
   trial=walk(G[9]['word']+G[9]['marker'],p,h,colors)
   if trial:
    found=[9]+path+[9];undo(trial[2],colors);return True
  if len(path)>=limit:return False
  for a in T:
   c=G[a]['name'].count('C')
   if k+c>2:continue
   r=walk(G[a]['word'],p,h,colors,slot)
   if r:
    pp,hh,cc=r
    if dfs(pp,hh,k+c,path+[a]):undo(cc,colors);return True
    undo(cc,colors)
  return False
 dfs(p,h,0,[]);answers.append({'watched_output':slot,'target_pose':[*target,0],'max_intermediate_packets':limit,'nodes':nodes,'word':found})
 print(answers[-1],flush=True)
Path('chronology_dcuv/critical_ucc_genealogy_probe.json').write_text(json.dumps({'status':'finite discovery controls only','answers':answers},indent=2)+'\n')
