"""Lift exact-control quotient witness and replay full high residue-age ledger.
CLI ORIGINAL_MODEL.json QUOTIENT.json WITNESS.txt OUTPUT.json.
Reports deficits in unretained places, not a physical ant witness claim.
"""
from pathlib import Path
import sys,json,collections,re,gzip
src,qp,wp,out=map(Path,sys.argv[1:5]);J=json.loads(src.read_text());Q=json.loads(qp.read_text())
# Only the finite-control metadata is needed from the underlying height model.
# Its full transition vectors can be hundreds of MB and are deliberately not
# loaded again. The residue model already carries the exact positions/poses.
with Path(J['source_file']).open()as f:header=f.read(16384)
base_source=json.loads(re.search(r'"source_file"\s*:\s*("(?:[^"\\]|\\.)*")',header).group(1))
F=int(re.search(r'"initial_bound"\s*:\s*(-?\d+)',header).group(1))
B=dict(positions=J['base_positions'],poses=J['poses'])
S=json.loads(Path(base_source).read_text());G=json.loads(Path(J['geometry_file']).read_text())['geometry'];ages={(a,x,y):r for a,x,y,r in json.loads(Path(J['rules_file']).read_text())};mod=J['modulus'];phase=J['phase'];target=S['target']
def rot(p,h):x,y=p;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
def coords(p):x,y=rot(p,phase);return x+y,x-y
lines=wp.read_text().splitlines();assert lines[0].startswith('status AGE_PETRI_WITNESS')
needed={int(v.split()[1])for v in lines if v.startswith('EDGE ')};qe={}
qdat=qp.with_suffix('.dat')
with(qdat.open()if qdat.exists()else gzip.open(str(qdat)+'.gz','rt'))as f:
 m,np,ne,ni,ng=map(int,f.readline().split());f.readline()
 for _ in range(ng):f.readline()
 for i in range(ne):
  raw=f.readline()
  if i in needed:qe[i]=tuple(map(int,raw.split()))
assert len(qe)==len(needed)
initial=J['initial_controls'];goals=J['goal_requirements'];edges=J['transitions'];cl=Q['class_map'];adj=collections.defaultdict(list)
for ei,(p,q,a)in enumerate(edges):adj[p].append(ei)
ops={(pi,tr,a):(c,*I,*O)for pi,tr,a,c,I,O in J['operations']}
qc=int(next(v for v in lines if v.startswith('start ')).split()[1]);p=next(p for p in initial if cl[p]==qc)
path=[]
for raw in lines:
 if not raw.startswith('EDGE '):continue
 ei,qf,qt,a=map(int,raw.split()[1:5]);e=qe[ei];assert(e[0],e[1])==(qf,qt)and cl[p]==qf
 old,tr=J['positions'][p];pi,d=B['positions'][old]
 candidates=[(ix,edges[ix])for ix in adj[p]if cl[edges[ix][1]]==qt and ops[pi,tr,edges[ix][2]]==e[3:]];assert candidates
 ix,v=candidates[0];path.append(dict(edge=ix,packet=v[2],source=p,destination=v[1],quotient_edge=ei));p=v[1]
assert any(g[0]==p for g in goals)
path.append(dict(edge=None,packet=target,source=p,destination=None,quotient_edge=None))
M={};deficit=None;states=[]
for step,row in enumerate(path):
 p=row['source'];old,tr=J['positions'][p];pi,d=B['positions'][old];h,q=B['poses'][pi];a=row['packet'];c=G[a]['name'].count('C');req=[];put=[]
 if q is not None:
  for v in G[a]['inputs']:
   dq,dt=coords(rot(v,h));z=q+dq
   if z>F:req.append(((z,(tr+dt)%mod),ages[a,*v]))
  for v in G[a]['outputs']:
   dq,dt=coords(rot(v,h));z=q+dq
   if z>F:put.append((z,(tr+dt)%mod))
 state=dict(**row,pose=[h,q,tr],requirements=req,outputs=put)
 for z,r in sorted(req,key=lambda v:-v[1]):
  bucket=M.setdefault(z,[]);available=[(x,k)for k,x in enumerate(bucket)if x>=r]
  if not available:
   deficit=dict(packet_index=step,packet=a,place=z,needed_age=r,available_ages=sorted(bucket));break
  _,k=min(available);bucket.pop(k)
 states.append(state)
 if deficit:break
 for z in M:M[z]=[min(4,x+c)for x in M[z]]
 for z in put:M.setdefault(z,[]).append(c)
word=[v['packet']for v in path]
def legal(seq):
 x=y=h=0;last={};t=0
 for a in seq+[-1]:
  for c in ('LLLLRLRRRRL'if a<0 else G[a]['word']):
   if(x,y)in last and last[x,y][0]==c:return False,dict(cell=[x,y],previous_read=last[x,y][1],conflicting_read=t,turn=c)
   last[x,y]=c,t;h=(h+(1 if c=='R'else-1))%4;dx,dy=[(0,1),(1,0),(0,-1),(-1,0)][h];x+=dx;y+=dy;t+=1
 return True,None
illegal=[]
for n in range(1,len(word)+1):
 for s in range(len(word)-n+1):
  ok,bad=legal(word[s:s+n])
  if not ok:illegal.append(dict(start=s,word=word[s:s+n],conflict=bad))
 if illegal:break
N=dict(status='FULL_RESIDUE_AGE_DEFICIT'if deficit else'FULL_RESIDUE_AGE_WITNESS',deficit=deficit,word=word,path=path,replayed_states=states,minimal_illegal_factors=illegal,source_file=str(src),quotient_file=str(qp),scope='A quotient witness is lifted to the original finite control graph using identical complete update labels. Full high-height/residue age resources are replayed with youngest-compatible consumption. This is not a physical ant path; literal-factor conflicts are reported separately.')
out.write_text(json.dumps(N,indent=2)+'\n');print(json.dumps({k:N[k]for k in ['status','deficit','word','minimal_illegal_factors']}))
