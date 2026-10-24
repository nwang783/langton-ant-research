"""Add one saturated C-age using signed recurrent-eight upper-U protection.
CLI COMPLETE_PACKET_GRAPH.json PREFIX X Y RULES.json.
RULES gives explicit [packet, input_x, input_y, minimum_C_age] necessities.
Suitable for residual/Q models with all actual packets
represented, including far steps, and no teleporting OUT/reentry transitions.
"""
from pathlib import Path
import json,sys,hashlib
from resource_profile import load_profile
src,out=map(Path,sys.argv[1:3]);q=tuple(map(int,sys.argv[3:5]));J=json.loads(src.read_text());assert not J['reentry'];n=J['n'];assert n+3<=50
# Metadata-only hydration. No color-bit indexing is used by this clock.
# Q puts its finite field below colors; exact pruning changes pose ids.
def hydrate(K, path, seen=()):
 assert str(path) not in seen, 'Cyclic wrapper metadata'
 if 'points' in K and 'poses' in K and K.get('resource_profile_file'):
  return K
 key=next(k for k in ['uncompressed_model_file','base_model_file','unpruned_model_file'] if k in K)
 pp=Path(K[key]);H=hydrate(json.loads(pp.read_text()),pp,seen+(str(path),))
 if 'retained_old_positions' in K:
  poses=[H['poses'][i] if i<len(H['poses']) else None for i in K['retained_old_positions']]
 else:
  assert K['out']==H['out'], 'Unrecognized pose-changing wrapper'
  poses=H['poses']
 K=dict(K);K.update(points=H['points'],poses=poses,resource_profile_file=H['resource_profile_file'],resource_profile_sha256=H['resource_profile_sha256'])
 return K
J=hydrate(J,src);root=J
assert q in set(map(tuple,J['points']))
P,D,M=load_profile(Path(root['resource_profile_file']));G=D['geometry']['geometry'];keep=P['keep'];assert keep==[0,1,4,5,6,7,8,9];upper={(-1,4),(0,2),(0,3)};counts={a:G[a]['name'].count('C')for a in keep};am=7<<n;T=[];meta=[]
rules_path=Path(sys.argv[5]);rules=json.loads(rules_path.read_text());assert all(a in keep and [x,y] in G[a]["inputs"] and 1<=m<=4 for a,x,y,m in rules)
def rot(z,h):x,y=z;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
for ei,e in enumerate(J['transitions']):
 fr,to,k,v,f,cl,r,goal,a=e;assert a in keep,'Every transition must execute its actual packet; no hidden OUT or initialization epsilon.';c=counts[a];pose=J['poses'][fr]if fr<len(J['poses'])else None;outputs=set();touch=set();threshold=0
 if pose is not None:
  x,y,h=pose
  def at(z):u,v=rot(z,h);return x+u,y+v
  outputs=set(map(at,G[a]['outputs']));touch={at(z[:2])for z in G[a]['requirements']};threshold=max([m for aa,xx,yy,m in rules if aa==a and at((xx,yy))==q]+[0])
 # Guard/age cases are exact on ages0..4; omitted codes5..7 are unreachable.
 if threshold:cases=[(age,c if q in outputs else 4) for age in range(threshold,5)]
 elif q in outputs:cases=[(None,c)]
 elif q in touch:cases=[(None,4)]
 elif c==0:cases=[(None,None)]
 else:cases=[(age,min(4,age+c))for age in range(5)]
 for age,new in cases:
  kk=k|(am if age is not None else 0);vv=v|((age<<n)if age is not None else 0);cc=cl|(am if new is not None else 0);rr=r|((new<<n)if new is not None else 0)
  T.append([fr,to,kk,vv,f,cc,rr,goal,a]);meta.append([ei,age,new])
sid,sk,sv=J['start'];N={'format':'resource_input_c_age_guarded_reset_v2','n':n+3,'out':J['out'],'poses':J['poses'],'points':J['points'],'start':[sid,sk|am,sv|(4<<n)],'reentry':[],'transitions':T,'base_model_file':str(src.resolve()),'base_model_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'resource_profile_file':root['resource_profile_file'],'resource_profile_sha256':root['resource_profile_sha256'],'watched_cell':q,'rules_file':str(rules_path.resolve()),'rules_sha256':hashlib.sha256(rules_path.read_bytes()).hexdigest(),'input_minimum_ages':rules,'age_offset':n,'age_bits':3,'age_values':[0,1,2,3,4],'packet_C_counts':counts,'edge_cases':meta,'scope':'The explicit rules are required proved premises: a produced residual token at each listed input has its listed minimum C count from producer start to consumer start. Age4 includes mature and unknown/initial; surviving labels increment by every actual packet C count; outputs reset to producer packet C count, including recycled cells. No new hypothesis.'};out.with_suffix('.json').write_text(json.dumps(N,separators=(',',':')))
with out.with_suffix('.dat').open('w')as f:
 f.write(f"{N['n']} {N['out']+1} {len(T)} 0\n");f.write(' '.join(map(str,N['start']))+'\n')
 for t in T:f.write(' '.join(map(str,t))+'\n')
 f.write('\n')
print(json.dumps({'bits':N['n'],'old_bits':n,'watched_cell':q,'rules_file':str(rules_path.resolve()),'rules_sha256':hashlib.sha256(rules_path.read_bytes()).hexdigest(),'input_minimum_ages':rules,'edges':len(T),'old_edges':len(J['transitions'])}))
