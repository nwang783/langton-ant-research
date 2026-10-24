"""Add one latest-output C-clock for a fixed set of upper U goal cells.
CLI COMPLETE_PACKET_GRAPH.json PREFIX POINTS.json.
Only suitable for unpermuted one-bit residual models with all actual packets
represented, including far steps, and no teleporting OUT/reentry transitions.
"""
from pathlib import Path
import json,sys,hashlib
from resource_profile import load_profile
src,out=map(Path,sys.argv[1:3]);watched=set(map(tuple,json.loads(Path(sys.argv[3]).read_text())));J=json.loads(src.read_text());assert not J['reentry'];n=J['n'];assert n+3<=50
if 'points'not in J or 'poses'not in J:
 parent=json.loads(Path(J['base_model_file']).read_text());assert 'retained_old_positions'in J and 'points'in parent and 'poses'in parent
 J['points']=parent['points'];J['poses']=[parent['poses'][p]if p<len(parent['poses'])else None for p in J['retained_old_positions']]
assert n==len(J['points'])and watched <= set(map(tuple,J['points'])) and watched
# Follow exact graph wrappers until resource metadata is available.
root=J;chain=[]
while 'resource_profile_file'not in root or root['resource_profile_file']is None:
 key=next(k for k in ['base_model_file','unpruned_model_file','unpermuted_model_file']if k in root);p=Path(root[key]);chain.append(str(p));root=json.loads(p.read_text())
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
sid,sk,sv=J['start'];N={'format':'signed_upper_latest_output_c_clock_guarded_reset_v1','n':n+3,'out':J['out'],'poses':J['poses'],'points':J['points'],'start':[sid,sk|am,sv|(4<<n)],'reentry':[],'transitions':T,'base_model_file':str(src.resolve()),'base_model_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'resource_profile_file':root['resource_profile_file'],'resource_profile_sha256':root['resource_profile_sha256'],'watched_cells':sorted(watched),'age_offset':n,'age_bits':3,'age_values':[0,1,2,3,4],'packet_C_counts':counts,'edge_cases':meta,'scope':'Signed IE plus latest-output survival: at a consumer reading ALL watched cells as upper residual inputs, the most recent output at any watched cell must survive, since a removed cell needs a later output to be black again. Thus its C-clock is at least4. Clock increments on every packet and resets to source C count on ANY watched output, never on removal. No individual-input guard when some watched cell might be absent.'};out.with_suffix('.json').write_text(json.dumps(N,separators=(',',':')))
with out.with_suffix('.dat').open('w')as f:
 f.write(f"{N['n']} {N['out']+1} {len(T)} 0\n");f.write(' '.join(map(str,N['start']))+'\n')
 for t in T:f.write(' '.join(map(str,t))+'\n')
 f.write('\n')
print(json.dumps({'bits':N['n'],'old_bits':n,'watched_cells':sorted(watched),'edges':len(T),'old_edges':len(J['transitions'])}))
