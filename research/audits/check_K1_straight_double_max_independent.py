from itertools import product
from collections import defaultdict,deque
from pathlib import Path
import json,hashlib
SELF=Path(__file__).resolve();ROOT=SELF.parents[1];D=ROOT/'K1_pipeline_detours_2026-10-23'
# Reconstruct every 1..4 read alternating R/L white history from its two
# possible incoming directions, filtering only the relevant R-face choice.
def choices(axis,mode):
 ans=[]
 for n in range(1,5):
  for h in product((axis,(axis+2)%4),repeat=n):
   r=h[::2]
   if mode=='equal':
    if len(r)!=2 or r[0]==r[1]:continue
   elif any(v!=axis for v in r):continue
   ans.append(h)
 return ans
def out(h):return tuple((x+(1 if k%2==0 else-1))%4 for k,x in enumerate(h))
ports=[('A',3,'w'),('w',0,'y'),('y',1,'B'),('B',2,'A'),('e',1,'z'),('w',2,'e'),('z',0,'A')]
def solve(hs):
 nodes=[(v,k)for v,h in hs.items()for k in range(len(h))];adj=defaultdict(list)
 for a,di,b in ports:
  src=[(a,k)for k,x in enumerate(out(hs[a]))if x==di];dst=[(b,k)for k,x in enumerate(hs[b])if x==di]
  if len(src)!=len(dst):return None
  for u,v in zip(src,dst):adj[u].append((v,1));adj[v].append((u,-1))
 comp={};delta={}
 for start in nodes:
  if start in comp:continue
  ci=len(set(comp.values()));comp[start]=ci;delta[start]=0;todo=[start]
  while todo:
   u=todo.pop()
   for v,d in adj[u]:
    if v in comp:
     if comp[v]!=ci or delta[v]!=delta[u]+d:return None
    else:comp[v]=ci;delta[v]=delta[u]+d;todo.append(v)
 edges=[]
 def lower(u,v,gap):
  a,b=comp[u],comp[v];g=gap+delta[u]-delta[v]
  if a==b:return g<=0
  edges.append((a,b,g));return True
 for v,h in hs.items():
  for k in range(len(h)-1):
   if not lower((v,k),(v,k+1),4):return None
 if not lower(('A',2),('B',1),1):return None
 nc=len(set(comp.values()));dist=[0]*nc
 for _ in range(nc):
  changed=False
  for a,b,g in edges:
   if dist[b]<dist[a]+g:dist[b]=dist[a]+g;changed=True
  if not changed:break
 else:return None
 return comp,delta
rows=[];attempts=0
for mw,my in product(('strict','equal'),repeat=2):
 for a,b,w,y,e in product([(0,0,2),(0,0,2,2)],[(1,1,3),(1,1,3,1),(1,1,3,3)],choices(3,mw),choices(0,my),choices(0,mw)):
  if mw=='strict' and len(w[::2])!=len(e[::2]):continue
  attempts+=1;hs=dict(A=a,B=b,w=w,y=y,e=e,z=(3,3,1,1));s=solve(hs)
  if s is None:continue
  cp,de=s;anchor=('A',1)
  forced={('w',0):-3,('e',1):-2,('z',3):-1,('A',1):0,('w',1):1,('e',2):2}
  for v,t in forced.items():assert cp[v]==cp[anchor] and de[v]-de[anchor]==t
  assert mw==my=='equal'
  rows.append({v:''.join('NESW'[h]for h in hist)for v,hist in hs.items()})
expected={('NNS','EWW','SSN','EEW'),('NNS','EWW','SSNS','EEWE'),('NNS','EWWE','SSNN','EEW'),('NNSS','EWW','SSN','EEWW'),('NNSS','EWWE','SSNN','EEWW')}
assert len(rows)==10 and{tuple(r[v]for v in('A','w','y','B'))for r in rows}==expected
assert all({r['e']for r in rows if tuple(r[v]for v in('A','w','y','B'))==s}=={'NSS','NSSN'}for s in expected)
p=D/'K1_straight_branch_double_max_successor.md';assert hashlib.sha256(p.read_bytes()).hexdigest()=='fdb4444ddd0593fdb361cc0e734fb408038339a1b40ddb9e986ff6362e60d8eb'
outdata=dict(status='PASS independent complete corner inventories, equality components and clock feasibility',note_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),candidate_rows=attempts,necessary_rows=rows,forced_clocks={'wR0':-3,'eL1':-2,'zL3':-1,'AL1':0,'wL1':1,'eR2':2},analytic_birth='w.R0 chooses H; therefore B(H)<=T0(w)-1=B(G)-4.',scope='Branchful complete-WHITE cap4 K1 straight equal-M branch and its signed forced RIGHT successor. Both LEFT neighbors M, actual old-stock LLLL; no realization, regress or initial-fuel charge.')
SELF.with_suffix('.json').write_text(json.dumps(outdata,indent=2)+'\n');print(outdata['status']);print('candidates',attempts,'survivors',len(rows))
