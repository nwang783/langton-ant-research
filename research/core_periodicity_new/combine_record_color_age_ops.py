"""Synchronized finite color-patch and current high height/C-age product.
CLI FAR_HEIGHT_COLOR.json DELAYED_GEOMETRY.json PREFIX.
No unsafe truncation of unbounded token counts.
"""
from pathlib import Path
import json,sys,hashlib
src,geo,out=map(Path,sys.argv[1:4]);J=json.loads(src.read_text());S=json.loads(geo.read_text());B=json.loads(Path(J['base_model_file']).read_text());G=json.loads(Path('chronology_dcuv/literal_residual_geometry.json').read_text())['geometry'];rules={(a,x,y):r for a,x,y,r in json.loads(Path('chronology_dcuv/counted_input_age_rules_complete.json').read_text())};F=S['initial_bound'];H=S['height_cap'];phase=S['phase'];heights=list(range(F+1,H+1));m=len(heights);nnear=len(B['poses']);far=J['far_controls'];cut=J['lower_cutoff'];assert phase==B['target_global_phase'];assert F==(B['record_threshold']-B['initial_token_weight']-1)//2

def rot(p,h):x,y=p;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
def ht(p):return sum(rot(p,phase))
assert all(cut+ht(rot(v,h))<=F for h in range(4)for a in J['keep']for k in ['inputs','outputs']for v in G[a][k])
def pose(p):
 gp=J['position_map'][p][0]
 if gp<nnear:
  x,y,h=B['poses'][gp];return h,ht((x,y))
 if gp<nnear+len(far):return tuple(far[gp-nnear])
 return None
ops=[];opix={}
def intern(c,I,O):
 key=c,tuple(I),tuple(O)
 if key not in opix:opix[key]=len(ops);ops.append([c,I,O])
 return opix[key]
def op(p,a):
 I=[0]*(5*m);O=[0]*m
 if a==99:return intern(0,I,O)
 h,q=pose(p);c=G[a]['name'].count('C')
 if q is not None:
  for v in G[a]['inputs']:
   z=q+ht(rot(v,h))
   if z>F:
    assert z<=H,(p,a,z,H);k=z-F-1
    for j in range(rules[a,*v]+1):I[k*5+j]+=1
  for v in G[a]['outputs']:
   z=q+ht(rot(v,h))
   if z>F:assert z<=H,(p,a,z,H);O[z-F-1]+=1
 return intern(c,I,O)
edges=[];goals=set()
for fr,to,k,v,flip,clear,reset,goal,a in J['transitions']:
 edges.append([fr,to,a,op(fr,a),k,v,flip,clear,reset])
 if goal:goals.add(to)
N={'format':'record_color_age_ops_v1','color_model_file':str(src.resolve()),'color_model_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'geometry_model_file':str(geo.resolve()),'geometry_model_sha256':hashlib.sha256(geo.read_bytes()).hexdigest(),'color_bits':J['n'],'points':J['points'],'height_places':heights,'operations':ops,'positions':[pose(p)for p in range(len(J['position_map']))]+[None],'start':J['start'],'goal_controls':sorted(goals),'transitions':edges,'scope':'Synchronized product of a finite residual-color guarded-reset model and current global high-height saturated-C-age token counts. Colors are not ordered; resource counts are ordered by tails. Unknown low head bin has no high effects at this checked cutoff. No no-hit theorem without separate model and invariant checking.'}
out.with_suffix('.json').write_text(json.dumps(N,separators=(',',':')))
with out.with_suffix('.dat').open('w')as f:
 f.write(f'COLOROPS {m} {J["out"]+1} {len(edges)} {len(ops)} 1 {len(goals)} {J["n"]}\n');f.write(' '.join(map(str,J['start']))+'\n');f.write(' '.join(map(str,sorted(goals)))+'\n')
 for c,I,O in ops:f.write(' '.join(map(str,[c]+I+O))+'\n')
 for e in edges:f.write(' '.join(map(str,e))+'\n')
out.with_suffix('.weights').write_text(' '.join(str(2**(h-F))for h in heights for j in range(5))+'\n');print({'resource_coordinates':5*m,'color_bits':J['n'],'controls':J['out']+1,'edges':len(edges),'operators':len(ops),'goal_controls':len(goals)})
