"""Bounded literal discovery only. A positive word is physical; no-hit is UNKNOWN."""
from pathlib import Path
import json,sys
G=json.load(open('chronology_dcuv/literal_residual_geometry.json'))['geometry'];J=json.load(open('chronology_dcuv/vcc_d_vc_joint_patch/model.json'));pts=J['points'];B={tuple(q):bool(J['start'][2]>>i&1)for i,q in enumerate(pts)};ids=(0,1,4,5,6,7,8,9);mp={a:i for i,a in enumerate(ids)};D=((0,1),(1,0),(0,-1),(-1,0));C={tuple(map(int,s.split()[:8]))for s in Path('chronology_dcuv/critical_ucc_count5/closure.tsv').read_text().splitlines()};P={tuple(map(int,s.split()[:7]))for s in Path('chronology_dcuv/protected_patch2.tsv').read_text().splitlines()};watch=(2,0);goal=(0,1,1);limit=int(sys.argv[1])if len(sys.argv)>1 else 16;cap=1000000;nodes=0;found=None

def rot(q,h):x,y=q;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def walk(w,p,h):
 undo=[]
 for c in w:
  if p in B and B[p]!=(c=='L'):
   unwalk(undo);return None
  undo.append((p,B.get(p)));B[p]=c!='L';h=(h+(1 if c=='R'else-1))%4;p=(p[0]+D[h][0],p[1]+D[h][1])
 return p,h,undo
def unwalk(u):
 for p,b in reversed(u):
  if b is None:B.pop(p,None)
  else:B[p]=b
def possible(p,h,r):
 if r>=2:return True
 z=rot((-1,-1),h);tar=rot((-1,-1),goal[2]);diff=(2*(goal[0]-p[0])+tar[0]-z[0],2*(goal[1]-p[1])+tar[1]-z[1]);dx,dy=rot(diff,-h)
 if dx%2 or dy%2:return False
 x,y=dx//2,dy//2
 if r==0:return x>=0 and y>=x and(x+y)%2==0 and(x!=0 or y%4==0)
 x-=1;y-=1;return y>=0 and x<=y and(x+y)%2==0 and(y!=0 or x%4==0)
def dfs(p,h,c,path):
 global nodes,found
 nodes+=1
 if nodes>=cap:return False
 if c==3 and(*p,h)==goal:
  rr=walk(G[5]['word']+G[5]['marker'],p,h)
  if rr:found=path+[5];unwalk(rr[2]);return True
 if len(path)>=limit or not possible(p,h,3-c):return False
 for a in ids:
  cc=G[a]['name'].count('C')
  if c+cc>3:continue
  qq=rot((watch[0]-p[0],watch[1]-p[1]),-h)
  if any(tuple(q[:2])==qq for q in G[a]['requirements']):continue
  t=(0,a,*p,h,*watch);dp=rot((goal[0]-p[0],goal[1]-p[1]),-h);dh=(goal[2]-h)%4;v=(a,5,*dp,dh,*qq)
  if t in P or v in P or(mp[0],mp[a],*p,h,*watch,c)in C or(mp[a],mp[5],*dp,dh,*qq,3-c)in C:continue
  rr=walk(G[a]['word'],p,h)
  if rr:
   if dfs(rr[0],rr[1],c+cc,path+[a]):unwalk(rr[2]);return True
   unwalk(rr[2])
 return False

dfs((1,1),0,0,[]);R={'status':'LITERAL_WORD_FOUND'if found else'UNKNOWN_BOUNDED_DISCOVERY','max_intermediate_packets':limit,'node_cap':cap,'nodes':nodes,'intermediates_and_goal':found,'whole_prefix_and_goal':[6,5,0]+found if found else None,'C_gap_from_D':3,'scope':'Literal physical finite control if positive; no negative theorem from bounds.'};Path('chronology_dcuv/vcc_d_vc_joint_patch/literal_probe.json').write_text(json.dumps(R,indent=2)+'\n');print(R)
