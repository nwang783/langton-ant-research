"""Add one latest-output C-clock for a fixed set of upper U goal cells.
CLI COMPLETE_PACKET_GRAPH.json PREFIX POINTS.json.
Suitable for residual/Q models with all actual packets
represented, including far steps, and no teleporting OUT/reentry transitions.
"""
from pathlib import Path
import json,sys,hashlib
from resource_profile import load_profile
src,out=map(Path,sys.argv[1:3]);watched=set(map(tuple,json.loads(Path(sys.argv[3]).read_text())));J=json.loads(src.read_text());assert not J['reentry'];n=J['n'];assert n+3<=50
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
assert watched <= set(map(tuple,J['points'])) and watched
P,D,M=load_profile(Path(root['resource_profile_file']));G=D['geometry']['geometry'];keep=P['keep'];assert keep==[0,1,4,5,6,7,8,9];upper={(-1,4),(0,2),(0,3)};counts={a:G[a]['name'].count('C')for a in keep};am=7<<n;T=[];meta=[]
def rot(z,h):x,y=z;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
for ei,e in enumerate(J['transitions']):
 fr,to,k,v,f,cl,r,goal,a=e;assert a in keep,'Every transition must execute its actual packet; no hidden OUT or initialization epsilon.';c=counts[a];pose=J['poses'][fr]if fr<len(J['poses'])else None;outputs=set();touch=set();isupper=False
 if pose is not None:
  x,y,h=pose
  def at(z):u,v=rot(z,h);return x+u,y+v
  outputs=set(map(at,G[a]['outputs']));touch={at(z[:2])for z in G[a]['requirements']};isupper=a in [7,8,9]and watched <= set(map(at,upper))
 # Guard/age cases are exact on ages0..4; omitted codes5..7 are unreachable.
 if isupper:cases=[(4,c if watched & outputs else 4)]
 elif watched & outputs:cases=[(None,c)]
 elif c==0:cases=[(None,None)]
 else:cases=[(age,min(4,age+c))for age in range(5)]
 for age,new in cases:
  kk=k|(am if age is not None else 0);vv=v|((age<<n)if age is not None else 0);cc=cl|(am if new is not None else 0);rr=r|((new<<n)if new is not None else 0)
  T.append([fr,to,kk,vv,f,cc,rr,goal,a]);meta.append([ei,age,new])
sid,sk,sv=J['start'];N={'format':'signed_upper_latest_output_c_clock_guarded_reset_v2','n':n+3,'out':J['out'],'poses':J['poses'],'points':J['points'],'start':[sid,sk|am,sv|(4<<n)],'reentry':[],'transitions':T,'base_model_file':str(src.resolve()),'base_model_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'resource_profile_file':root['resource_profile_file'],'resource_profile_sha256':root['resource_profile_sha256'],'watched_cells':sorted(watched),'age_offset':n,'age_bits':3,'age_values':[0,1,2,3,4],'packet_C_counts':counts,'edge_cases':meta,'scope':'Signed IE plus latest-output survival: at a consumer reading ALL watched cells as upper residual inputs, the most recent output at any watched cell must survive, since a removed cell needs a later output to be black again. Thus its C-clock is at least4. Clock increments on every packet and resets to source C count on ANY watched output, never on removal. No individual-input guard when some watched cell might be absent.'};out.with_suffix('.json').write_text(json.dumps(N,separators=(',',':')))
with out.with_suffix('.dat').open('w')as f:
 f.write(f"{N['n']} {N['out']+1} {len(T)} 0\n");f.write(' '.join(map(str,N['start']))+'\n')
 for t in T:f.write(' '.join(map(str,t))+'\n')
 f.write('\n')
print(json.dumps({'bits':N['n'],'old_bits':n,'watched_cells':sorted(watched),'edges':len(T),'old_edges':len(J['transitions'])}))
