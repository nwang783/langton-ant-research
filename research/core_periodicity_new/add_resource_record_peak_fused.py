"""Historical strict-record conditioning, no unproved relation or induction clauses.
CLI BASE.json PREFIX POTENTIAL.json SOURCE_GLOBAL_PHASE
Only goal-input identities need origins. Codes0 white,1 black unknown,3 black produced since source.
Source and every explicit strict intermediate peak are below the fixed outer goal peak.
OUT may omit all geometric restrictions, conservatively.
"""
from pathlib import Path
import json,sys,hashlib
from resource_profile import load_profile
base,out,potential=map(Path,sys.argv[1:4]);phase=int(sys.argv[4]);assert phase in range(4)
J=json.loads(base.read_text());P,D,M=load_profile(J['resource_profile_file']);W=json.loads(potential.read_text());assert W['profile_sha256']==M['resource_profile_sha256'];v=W['values'];G=D['geometry']['geometry'];direction=(v['ax'],v['ay'])
def rot(q,h):x,y=q;return [(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
def L(q):return sum(a*b for a,b in zip(direction,q))
def A(h):return L(rot((-1,1),h))+v[f'c{h%4}']
def T(a,h):
 h%=4;g=G[a];e=g['endpoint'];return max([2*L(rot(e[:2],h))+A(h+e[2])]+[2*L(rot(q,h))+v[f'w_{a}_{i}_{h}']for i,q in enumerate(g['outputs'])])
def peak(a,x,y,h):return 2*L(rot((x,y),phase))+max(A(h+phase),T(a,h+phase))
tx,ty,th=J['target_pose'];b=J['target'];a0=J['source'];threshold=2*L(rot((tx,ty),phase))+T(b,th+phase)
assert T(b,th+phase)>A(th+phase),'target cannot create a strict record'
assert peak(a0,0,0,0)<threshold,'source already meets or exceeds proposed record'
watch={tuple(tx+z[0]if i==0 else ty+z[1]for i in range(2)) for q in G[b]['inputs']for z in [rot(q,th)]}
assert watch<=set(map(tuple,J['points'])),'retain all goal residual inputs'
assert tuple(J['protected_q'])in watch and J['protected_q']in G[a0]['outputs']
cells=[];n=0
for i,q in enumerate(J['points']):
 bits=2 if tuple(q)in watch else 1;cells.append({'cell':q,'old_color_bit':i,'offset':n,'bits':bits,'watched':bits==2});n+=bits
assert n<=50,'engine variable cap'
sp,sk,sv=J['start'];nk=nv=0
for c in cells:
 i=c['old_color_bit'];off=c['offset'];bits=c['bits'];q=c['cell']
 if bits==1:
  if sk>>i&1:nk|=1<<off;nv|=((sv>>i)&1)<<off
 elif q in G[a0]['outputs']:
  assert sk>>i&1 and sv>>i&1;nk|=3<<off;nv|=3<<off
 else:
  nk|=2<<off
  if sk>>i&1:nk|=1<<off;nv|=((sv>>i)&1)<<off
transitions=[];filtered=[]
for bi,(sid,to,k,val,f,goal,a)in enumerate(J['transitions']):
 x,y,h=J['poses'][sid]
 if not goal and peak(a,x,y,h)>=threshold:filtered.append(bi);continue
 branches=[(0,0)];flip=clear=reset=0
 for c in cells:
  i=c['old_color_bit'];off=c['offset'];bits=c['bits'];touched=(k>>i)&1
  if bits==1:
   if touched:branches=[(kk|(1<<off),vv|(((val>>i)&1)<<off))for kk,vv in branches]
   if f>>i&1:flip|=1<<off
   continue
  if not touched:assert not(f>>i&1);continue
  initial=(val>>i)&1
  if initial:branches=[(kk|(1<<off),vv|(1<<off))for kk,vv in branches]
  else:branches=[(kk|(3<<off),vv)for kk,vv in branches]
  z=rot((c['cell'][0]-x,c['cell'][1]-y),-h)
  final=3 if list(z)in G[a]['outputs']else initial^((f>>i)&1)
  clear|=3<<off;reset|=final<<off
 if goal:
  highbits=sum(1<<(c['offset']+1)for c in cells if c['watched'])
  branches=[(kk|highbits,vv|highbits)for kk,vv in branches if not((vv^highbits)&kk&highbits)]
 for kk,vv in branches:transitions.append([sid,to,kk,vv,flip,clear,reset,goal,a])
new={**J,'n':n,'start':[sp,nk,nv],'transitions':transitions,'format':'guarded_reset_fused_record_peak_v1','base_model_file':str(base.resolve()),'base_model_sha256':hashlib.sha256(base.read_bytes()).hexdigest(),'potential_file':str(potential.resolve()),'potential_sha256':hashlib.sha256(potential.read_bytes()).hexdigest(),'source_global_phase':phase,'record_threshold':threshold,'source_peak':peak(a0,0,0,0),'core_offsets':[A(h)for h in range(4)],'created_peaks':[[a,h,T(a,h)]for a in J['keep']for h in range(4)],'origin_cells':cells,'goal_input_cells':sorted(watch),'origin_encoding':{'white':0,'black_unknown':1,'black_known_produced':3},'geometrically_filtered_base_transition_indices':filtered,'record_scope':'Strict historical record: every source/intermediate recorded core/output value below threshold. All goal residual inputs have producers at or after outer source; protected q retains outer-source identity. OUT unrestricted. No unproved family or clause used.'}
out.with_suffix('.json').write_text(json.dumps(new,separators=(',',':')))
with out.with_suffix('.dat').open('w')as f:
 f.write(f"{n} {J['out']+1} {len(transitions)} {len(J['reentry'])}\n");f.write(' '.join(map(str,new['start']))+'\n')
 for r in transitions:f.write(' '.join(map(str,r))+'\n')
 f.write(' '.join(map(str,J['reentry']))+'\n')
print(json.dumps({'variables':n,'positions':J['out']+1,'transitions':len(transitions),'watched_cells':len(watch),'source_peak':new['source_peak'],'threshold':threshold,'filtered_transitions':len(filtered)}))
