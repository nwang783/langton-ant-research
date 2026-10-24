"""Necessary zero/one-C producer displacement for a surviving young token.
CLI AGE_CONTROL_EXPANSION.json PREFIX. No guard is inferred for abstract far poses.
"""
from pathlib import Path
import sys,json,hashlib
from resource_profile import load_profile
src,out=map(Path,sys.argv[1:3]);J=json.loads(src.read_text());assert J['format']=='trailing_finite_control_expansion_v1'and J['field_cardinality']==5;A=json.loads(Path(J['base_model_file']).read_text());assert A['format']=='signed_upper_input_c_age_guarded_reset_v1';P,D,M=load_profile(Path(A['resource_profile_file']));G=D['geometry']['geometry'];keep=P['keep'];q=tuple(A['watched_cell']);bit=1<<list(map(tuple,J['points'])).index(q);forbidden={};witnesses={}
def rot(z,h):x,y=z;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
def cone(z,c):
 x,y=z
 if c==0:return x>=0 and y>=x and(x+y)%2==0 and(x!=0 or y%4==0)
 assert c==1;X,Y=x-1,y-1;return Y>=0 and X<=Y and(X+Y)%2==0 and(Y!=0 or X%4==0)
for p,pose in enumerate(A['poses']):
 if pose is None:continue
 x,y,h=pose
 for age in [0,1]:
  hs=(h+age)%4;poss=[]
  for a in keep:
   g=G[a];cs=g['name'].count('C');ex,ey,eh=g['endpoint'];assert eh%4==(-cs)%4
   if cs>age:continue
   for oi,o in enumerate(g['outputs']):
    z=rot(o,hs);sx,sy=q[0]-z[0],q[1]-z[1]
    if(sx+sy+hs)%2:continue
    z=rot((ex,ey),hs);ep=sx+z[0],sy+z[1];hh=(hs+eh)%4;d=rot((x-ep[0],y-ep[1]),-hh)
    if cone(d,age-cs):poss.append([a,oi,sx,sy,hs,age-cs,*d])
  pid=p*5+age
  if not poss:forbidden[pid]=[p,age,*pose]
  else:witnesses[pid]=poss[0]
T=[];mapping=[];dropped=0
for ei,e in enumerate(J['transitions']):
 e=e[:]
 if e[0]in forbidden:
  if e[3]&bit:dropped+=1;continue
  e[2]|=bit # Require white; only a surviving BLACK young identity is forbidden.
 T.append(e);mapping.append(ei)
N={**J,'format':'single_token_age_kinematic_restriction_v1','kinematic_base_file':str(src.resolve()),'kinematic_base_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'transitions':T,'kinematic_watched_cell':q,'young_black_forbidden_controls':forbidden,'young_allowed_producer_controls':witnesses,'edge_map_to_control':mapping,'scope':'At near poses, black token ages0/1 require at least one geometrically possible literal source/output slot with matching source heading and necessary zero/one remaining-C cone. Far poses and all ages>=2 remain unfiltered.'};out.with_suffix('.json').write_text(json.dumps(N,separators=(',',':')))
with out.with_suffix('.dat').open('w')as f:
 f.write(f"{N['n']} {N['out']+1} {len(T)} 0\n");f.write(' '.join(map(str,N['start']))+'\n')
 for t in T:f.write(' '.join(map(str,t))+'\n')
 f.write('\n')
print(json.dumps({'young_black_forbidden_controls':len(forbidden),'dropped_edges':dropped,'retained_edges':len(T)}))
