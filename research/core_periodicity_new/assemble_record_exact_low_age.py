"""Assemble exact-low finite summaries with the current high height/age resource.
CLI DELAYED_GEOMETRY.json LOW.ports PREFIX CUTOFF WIDTH.
Writes compact shared-operator format, not millions of repeated zero vectors.
"""
from pathlib import Path
import json,sys,hashlib
src,ports,out=map(Path,sys.argv[1:4]);L,W=map(int,sys.argv[4:6]);S=json.loads(src.read_text());D=json.loads(Path(S['dfa_file']).read_text());G=json.loads(Path('chronology_dcuv/literal_residual_geometry.json').read_text())['geometry'];age={(a,x,y):r for a,x,y,r in json.loads(Path('chronology_dcuv/counted_input_age_rules_complete.json').read_text())};nd=len(D['transitions']);keep=D['keep'];phase=S['phase'];F=S['initial_bound'];H=S['height_cap'];heights=list(range(F+1,H+1));m=len(heights);acts={(v[0],v[1]):v for v in S['actions']};assert L<=min(v[6]for v in S['actions']);assert W>=max(abs(v[3])for v in S['actions'])
def rot(p,h):x,y=p;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
def ht(p):return sum(rot(p,phase))
for h in range(4):
 for a in keep:
  assert all(L+ht(rot(v,h))<=F for k in ['inputs','outputs']for v in G[a][k])
positions=[];ix={}
for h in range(4):
 for q in range(L+1,S['old_core_limits'][h]+1):
  if(q-h)%2:continue
  for d in range(nd):ix[h,q,d]=len(positions);positions.append([h,q,d,'high'])
nhigh=len(positions)
f=ports.open();np,ne,ni=map(int,next(f).split());initialports=list(map(int,next(f).split()));assert len(initialports)==ni
portrows=[];pix={}
for p in range(np):
 h,d,dep=map(int,next(f).split());assert 0<=dep<W and(L-dep-h)%2==0;pix[h,d,dep]=p;portrows.append([h,d,dep]);positions.append([h,L-dep,d,'low',p])
ops=[];opix={}
def intern(c,I,O):
 key=(c,tuple(I),tuple(O))
 if key not in opix:opix[key]=len(ops);ops.append([c,I,O])
 return opix[key]
zero=[intern(c,[0]*(5*m),[0]*m)for c in range(5)]
def op(h,q,a):
 I=[0]*(5*m);O=[0]*m;c=G[a]['name'].count('C')
 for v in G[a]['inputs']:
  z=q+ht(rot(v,h))
  if z>F:
   assert z<=H,(h,q,a,z,H);k=z-F-1
   for j in range(age[a,*v]+1):I[5*k+j]+=1
 for v in G[a]['outputs']:
  z=q+ht(rot(v,h))
  if z>F:assert z<=H,(h,q,a,z,H);O[z-F-1]+=1
 return intern(c,I,O)
edges=[]
for p,(h,q,d,_)in enumerate(positions[:nhigh]):
 for k,a in enumerate(keep):
  dd=D['transitions'][d][k]
  if dd<0:continue
  v=acts[h,a];c,dq,dh=v[2:5]
  if q>v[6]:continue
  h2=(h+dh)%4;q2=q+dq
  if q2>L:to=ix[h2,q2,dd]
  else:to=nhigh+pix[h2,dd,L-q2]
  edges.append([p,to,a,op(h,q,a)])
# Only crossing packets need remain explicit in the low zone; internal low
# packets are covered exactly by the attained summary relation.
for pp,(h,d,dep)in enumerate(portrows):
 q=L-dep
 for k,a in enumerate(keep):
  dd=D['transitions'][d][k]
  if dd<0:continue
  v=acts[h,a];c,dq,dh=v[2:5];q2=q+dq
  if q2>L:edges.append([nhigh+pp,ix[(h+dh)%4,q2,dd],a,zero[c]])
for _ in range(ne):
 p,q,c=map(int,next(f).split());edges.append([nhigh+p,nhigh+q,-1,zero[c]])
f.close()
initial=[p for p,v in enumerate(positions[:nhigh])if v[2]==D['initial_class']]+[nhigh+p for p in initialports]
goals=[];a=S['target'];ai=keep.index(a)
for d,row in enumerate(D['transitions']):
 if row[ai]>=0:
  c,I,O=ops[op(0,0,a)];goals.append([ix[0,0,d],I])
N={'format':'record_exact_low_height_age_ops_v1','source_file':str(src.resolve()),'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'ports_file':str(ports.resolve()),'ports_sha256':hashlib.sha256(ports.read_bytes()).hexdigest(),'cutoff':L,'boundary_width':W,'height_places':heights,'age_cap':4,'positions':positions,'high_controls':nhigh,'low_port_rows':portrows,'operations':ops,'initial_controls':initial,'goal_requirements':goals,'transitions':edges,'scope':'Current high height/C-age multiset relaxation with exact low-height excursion summaries. Operator4 may represent an attained low path with>=4 C; this is exactly its saturated-age effect. No transverse, literal white consistency or physical ant sufficiency is asserted. Model integration not independently signed.'}
out.with_suffix('.json').write_text(json.dumps(N,separators=(',',':')))
with out.with_suffix('.dat').open('w')as f:
 f.write(f'OPS {m} {len(positions)} {len(edges)} {len(initial)} {len(goals)} {len(ops)}\n');f.write(' '.join(map(str,initial))+'\n')
 for p,r in goals:f.write(' '.join(map(str,[p]+r))+'\n')
 for c,I,O in ops:f.write(' '.join(map(str,[c]+I+O))+'\n')
 for e in edges:f.write(' '.join(map(str,e))+'\n')
out.with_suffix('.weights').write_text(' '.join(str(2**(h-F))for h in heights for j in range(5))+'\n')
print({'heights':m,'controls':len(positions),'high_controls':nhigh,'low_ports':np,'edges':len(edges),'operators':len(ops),'goals':len(goals),'initial_controls':len(initial)})
