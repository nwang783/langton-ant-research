"""Finite height-count Petri overapproximation for an unfunded record.
CLI DELAYED_GEOMETRY.json PREFIX. This ignores colors, transverse position and
age envelopes, but conserves the multiset of residual heights above F.
"""
from pathlib import Path
import sys,json,hashlib,collections
src,out=map(Path,sys.argv[1:3]);J=json.loads(src.read_text());G=json.loads(Path('chronology_dcuv/literal_residual_geometry.json').read_text())['geometry'];B=json.loads(Path(J['dfa_file']).read_text());keep=B['keep'];F=J['initial_bound'];phase=J['phase'];cap=J['height_cap'];old=J['old_core_limits'];target=J['target'];acts={(a[0],a[1]):a for a in J['actions']}
def rot(p,h):x,y=p;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
def ht(p):return sum(rot(p,phase))
offs={(a,h,k):[ht(rot(p,h))for p in G[a][k]]for a in keep for h in range(4)for k in ['inputs','outputs']}
natural_cut=F-max(max(v)for v in offs.values());cut=int(sys.argv[3])if len(sys.argv)>3 else natural_cut;assert cut<=natural_cut,(cut,natural_cut);places=list(range(F+1,cap+1));P=len(places)
poses=[]
for h in range(4):
 poses.append((h,None))
 poses += [(h,q) for q in range(cut+1,old[h]+1) if (q-h)%2==0]
pidx={p:i for i,p in enumerate(poses)};nd=len(B['transitions']);positions=[(p,d)for p in range(len(poses))for d in range(nd)];pid={p:i for i,p in enumerate(positions)}
def counts(a,h,q,k):
 v=[0]*P
 if q is None:return v
 for o in offs[a,h,k]:
  if q+o>F:
   assert q+o<=cap,(a,h,q,k,q+o,cap)
   v[q+o-F-1]+=1
 return v
edges=[]
for pi,(h,q) in enumerate(poses):
 for ai,a in enumerate(keep):
  aa=acts[h,a];dq,dh,lim=aa[3],aa[4],aa[6];hh=(h+dh)%4
  choices=[]
  if q is not None:
   if q>lim:continue
   q2=q+dq;assert q2<=old[hh];choices=[(q,q2 if q2>cut else None)]
  else:
   # Every source low-bin packet has all residual inputs/outputs <= F.
   choices=[(None,None)]
   for q2 in range(cut+1,min(old[hh],cut+dq)+1):
    qq=q2-dq
    if (qq-h)%2==0 and qq<=lim:choices.append((qq,q2))
  for qq,q2 in choices:
   pp=pidx[hh,q2];ii=counts(a,h,qq,'inputs');oo=counts(a,h,qq,'outputs')
   for d,row in enumerate(B['transitions']):
    dd=row[ai]
    if dd>=0:edges.append([pid[pi,d],pid[pp,dd],a,ii,oo])
initial=[pid[pi,B['initial_class']] for pi in range(len(poses))]
goals=[];ai=keep.index(target);pi=pidx[0,0];req=counts(target,0,0,'inputs')
for d,row in enumerate(B['transitions']):
 if row[ai]>=0:goals.append([pid[pi,d],req])
N={'format':'record_height_petri_v1','source_file':str(src.resolve()),'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'dfa_file':J['dfa_file'],'dfa_sha256':J['dfa_sha256'],'initial_bound':F,'height_cap':cap,'low_cutoff':cut,'places':places,'poses':poses,'positions':positions,'initial_controls':initial,'goal_requirements':goals,'transitions':edges,'scope':'Finite-control exact height multiset updates above F; lower resources are unlimited. Low-bin steps are existentially exact and have no high resources. No color/transverse/age consistency is asserted. Initial high multiset is empty. This is an overapproximation only.'};out.with_suffix('.json').write_text(json.dumps(N,separators=(',',':')))
with out.with_suffix('.dat').open('w')as f:
 f.write(f'{P} {len(positions)} {len(edges)} {len(initial)} {len(goals)}\n');f.write(' '.join(map(str,initial))+'\n')
 for p,r in goals:f.write(' '.join(map(str,[p]+r))+'\n')
 for p,q,a,i,o in edges:f.write(' '.join(map(str,[p,q,a]+i+o))+'\n')
print({'places':P,'positions':len(positions),'edges':len(edges),'goals':len(goals),'low_cutoff':cut})
