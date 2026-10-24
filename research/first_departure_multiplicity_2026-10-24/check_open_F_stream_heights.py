"""Independent dual-face potential reconstruction from the frozen OPEN F interface.
Read only its complete named histories and full drift; no solve/search/replay.
"""
from pathlib import Path
from collections import defaultdict,deque
import json,hashlib
src=Path('/workspace/shared/langton/autonomous_controllers_2026-10-24/cap4_multiply_used_F_open_interface.json');z=json.loads(src.read_text());pts=[tuple(p)for p in z['named_classes']];hist=dict(zip(pts,z['complete_named_heading_words']));d=tuple(z['full_drift']);assert d==(2,-2)
H='NESW';V={'N':(0,1),'E':(1,0),'S':(0,-1),'W':(-1,0)}
def q(p):
 r=p[0]%2;k=(p[0]-r)//2;return(r,p[1]+2*k)
def add(p,v):return(p[0]+v[0],p[1]+v[1])
def facepair(p,h):
 x,y=p
 return {'E':((x,y-1),(x,y)),'W':((x-1,y),(x-1,y-1)),'N':((x,y),(x-1,y)),'S':((x-1,y-1),(x,y-1))}[h]
E={}
for p,h in hist.items():
 outs=[H[(H.index(a)+(1 if r%2==0 else-1))%4]for r,a in enumerate(h)]
 incoming='NS'if sum(p)%2==0 else'EW';outgoing='EW'if sum(p)%2==0 else'NS'
 assert all(x in incoming for x in h)
 for dr in outgoing:
  k=(q(p),dr);f=outs.count(dr)
  assert k not in E or E[k]==f;E[k]=f
 for dr in incoming:
  v=V[dr];u=(p[0]-v[0],p[1]-v[1]);k=(q(u),dr);f=h.count(dr)
  assert k not in E or E[k]==f;E[k]=f
adj=defaultdict(list);eq=[]
for(p,dr),f in E.items():
 c,l=map(q,facepair(p,dr));assert sum(c)%2==1 and sum(l)%2==0
 adj[l].append((c,f));adj[c].append((l,-f));eq.append(dict(source=p,heading=dr,flow=f,C=c,L=l))
val={};comps=[];bad=[]
for root in sorted(adj,key=lambda p:(sum(p),p)):
 if root in val:continue
 val[root]=0;qq=deque([root]);co=[]
 while qq:
  u=qq.popleft();co.append(u)
  for v,w in adj[u]:
   if v in val:
    if val[v]!=val[u]+w:bad.append((u,v,w,val[u],val[v]))
   else:val[v]=val[u]+w;qq.append(v)
 comps.append(co)
assert not bad and len(comps)==1
# Lowest known-face levels are fixed zero by all inactive lower ports.
assert all(val[p]==0 for p in val if sum(p)<=-2)
cycle=z['first_R_cycles'][0];crows=[]
for p0 in cycle['cells']:
 p=tuple(p0);h=hist[p];first=h[0];dep=H[(H.index(first)+1)%4];c,l=map(q,facepair(p,dep));f=E[q(p),dep]
 # First-R selected maximizing C theorem checked directly, not merely assumed.
 Cinc=[]
 for dr in('E','W')if sum(p)%2==0 else('N','S'):
  cc,ll=map(q,facepair(p,dr));Cinc.append((cc,val[cc]))
 assert val[c]==max(x[1]for x in Cinc)
 crows.append(dict(cell=p,history=h,departure=dep,physical_uses=f,C=c,C_height=val[c],L=l,L_height=val[l],incident_C=Cinc))
assert len({r['C_height']for r in crows})==1
obj=dict(scope=__doc__,source_sha256=hashlib.sha256(src.read_bytes()).hexdigest(),status='PASS OPEN face-potential compatibility, including zero ports and actual full quotient',edge_count=len(E),face_count=len(val),connected_components=len(comps),known_face_heights=[dict(face=p,kind='C'if sum(p)%2 else'L',height=val[p])for p in sorted(val,key=lambda p:(sum(p),p))],cycle_rows=crows,limitations='Only incident-edge equations of the frozen named partial interface; upper field, one full actual event orbit, full WHITE board and global cap-four completion remain unsupplied.')
Path(__file__).with_suffix('.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps(obj,indent=2))
