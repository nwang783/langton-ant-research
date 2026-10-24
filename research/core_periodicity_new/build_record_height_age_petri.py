"""Current high-residual height/C-age multiset, with nested threshold resources.
CLI FULL_HEIGHT_PETRI.json PREFIX [COMMA_HEIGHTS]. No guessed token-count bound.
"""
from pathlib import Path
import sys,json,hashlib
src,out=map(Path,sys.argv[1:3]);J=json.loads(src.read_text());S=json.loads(Path(J['source_file']).read_text());G=json.loads(Path('chronology_dcuv/literal_residual_geometry.json').read_text())['geometry'];R=Path('chronology_dcuv/counted_input_age_rules_complete.json');ages={(a,x,y):r for a,x,y,r in json.loads(R.read_text())};F=J['initial_bound'];phase=S['phase'];heights=list(map(int,sys.argv[3].split(',')))if len(sys.argv)>3 else J['places'];idx={h:i for i,h in enumerate(heights)};m=len(heights)
def rot(p,h):x,y=p;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
def ht(p):return sum(rot(p,phase))
def op(pi,a):
 h,q=J['poses'][pi];I=[0]*(5*m);O=[0]*m;c=G[a]['name'].count('C')
 if q is not None:
  for p in G[a]['inputs']:
   z=q+ht(rot(p,h))
   if z in idx:
    k=idx[z];r=ages[a,*p]
    for j in range(r+1):I[5*k+j]+=1
  for p in G[a]['outputs']:
   z=q+ht(rot(p,h))
   if z in idx:O[idx[z]]+=1
 return c,I,O
ops={};goals=[]
for p,r in J['goal_requirements']:
 pi=J['positions'][p][0];c,I,O=ops.setdefault((pi,S['target']),op(pi,S['target']));goals.append([p,I])
# The exact low-bin cutoff is below every crossing. Thus a source low-bin edge
# has no tracked input/output; its hidden source-height choices need no split.
for p,q,a,i,o in J['transitions']:
 pi=J['positions'][p][0];c,I,O=ops.setdefault((pi,a),op(pi,a))
 assert [I[5*k]for k in range(m)]==[i[J['places'].index(h)]for h in heights]
 assert O==[o[J['places'].index(h)]for h in heights]
N={'format':'record_height_age_petri_v1','source_file':str(src.resolve()),'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'rules_file':str(R.resolve()),'rules_sha256':hashlib.sha256(R.read_bytes()).hexdigest(),'height_places':heights,'age_cap':4,'initial_controls':J['initial_controls'],'goal_requirements':goals,'positions':J['positions'],'poses':J['poses'],'operations':[[pi,a,c,I,O]for(pi,a),(c,I,O)in ops.items()],'transitions':[[p,q,a]for p,q,a,_,_ in J['transitions']],'scope':'Current residual counts at selected exact heights above F, split by saturated C-age0..4. Coordinates are tail counts of age>=j. Unselected heights are unlimited. Inputs require signed minimum ages, outputs have producer C count, surviving identities age on every packet. No spatial or producer-role matching is imposed; overapproximation only.'}
out.with_suffix('.json').write_text(json.dumps(N,separators=(',',':')))
with out.with_suffix('.dat').open('w')as f:
 f.write(f'{m} {len(J["positions"])} {len(J["transitions"])} {len(J["initial_controls"])} {len(goals)}\n');f.write(' '.join(map(str,J['initial_controls']))+'\n')
 for p,r in goals:f.write(' '.join(map(str,[p]+r))+'\n')
 for p,q,a,_,_ in J['transitions']:
  c,I,O=ops[J['positions'][p][0],a];f.write(' '.join(map(str,[p,q,a,c]+I+O))+'\n')
print({'heights':heights,'tail_coordinates':m*5,'controls':len(J['positions']),'edges':len(J['transitions'])})
