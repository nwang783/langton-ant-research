"""Independent full-prefix record abstraction from literal words, no author imports.
Checks exact disjoint guard partitions, initial-board branches, OUT completeness,
and a separately implemented reset-BDD inductive invariant.
"""
from pathlib import Path
from collections import defaultdict
from math import prod
import json,sys,subprocess
from check_dcuv_producer_model_independent import geometry,core,rotation,xy,walk,raws,mark,ROOT,digest,resolve_file
from check_dcuv_patch_model_independent import validate_profile
OUT=ROOT/'audits/global_record_whitened_replays';OUT.mkdir(exist_ok=True)
def check(path):
 path=Path(path).resolve();J=json.loads(path.read_text());assert J['format']=='guarded_reset_global_record_whitened_initial_v1';bp=resolve_file(path,J['unwhitened_model_file']);assert digest(bp)==J['unwhitened_model_sha256']
 keep=validate_profile(J);assert J['keep']==list(keep)
 pp=resolve_file(path,J['potential_file']);assert digest(pp)==J['potential_sha256'];P=json.loads(pp.read_text());assert P['profile_sha256']==J['resource_profile_sha256'];v=P['values']
 phase=J['target_global_phase'];target=J['target'];assert phase in range(4)and target in keep and J['target_pose']==[0,0,0]
 L=lambda z:int(z.real*v['ax']+z.imag*v['ay'])
 A=lambda h:L(rotation(-1+1j,h))+v[f'c{h%4}']
 g=[(*walk(raw)[:2],walk(raw+mark)[2],walk(raw)[3])for raw in raws]
 def T(a,h):
  h%=4;end,dh,_,_=g[a]
  return max([2*L(rotation(end,h))+A(h+dh)]+[2*L(rotation(q,h))+v[f'w_{a}_{i}_{h}']for i,q in enumerate(geometry[a]['outputs'])])
 S=T(target,phase);I=max(T(a,h)-2*L(rotation(q,h))for a in keep for h in range(4)for q in geometry[a]['inputs'])
 assert S>A(phase) and J['record_threshold']==S and J['initial_token_weight']==I
 assert J['core_offsets']==[A(h)for h in range(4)]and J['created_peaks']==[[a,h,T(a,h)]for a in keep for h in range(4)]
 assert J['origin_encoding']=={'white':0,'black_unknown_or_core':1,'black_initial':2,'black_produced':3}
 points=[complex(*q)for q in J['points']];assert len(points)==len(set(points))and points==sorted(points,key=xy)
 assert geometry[target]['inputs']<=set(points)
 cells=J['origin_cells'];assert len(cells)==len(points);n=0;watch=set()
 for q,c in zip(points,cells):
  assert c['cell']==list(xy(q))and c['offset']==n and c['bits']in(1,2)and c['watched']==(c['bits']==2)
  if c['watched']:watch.add(q)
  n+=c['bits']
 assert geometry[target]['inputs']<=watch and n==J['n']and n<63
 poses=set()
 for q in points:
  for a in keep:
   for h in range(4):
    for z in g[a][2]:
     p=q-rotation(z,h)
     if(sum(xy(p))-h)%2==0:poses.add((*xy(p),h))
 poses=sorted(poses);where={q:i for i,q in enumerate(poses)};init=len(poses);out=init+1
 assert J['poses']==[list(p)for p in poses]and J['initial_control_pose']==init and J['out']==out
 start=[init,sum(1<<c['offset']for c in cells if c['watched']),0];white=[]
 for q,c in zip(points,cells):
  rank=I+2*L(rotation(q,phase))
  if rank>=S:
   mask=((1<<c['bits'])-1)<<c['offset'];start[1]|=mask
   white.append(dict(cell=list(xy(q)),activation_value=rank,mask=mask))
 assert J['whitened_initial_cells']==white and J['start']==start
 base=json.loads(bp.read_text());assert base['format']=='guarded_reset_global_record_prefix_v1'
 for k in ['transitions','poses','reentry','points','origin_cells','initial_transition_indices','packet_transition_indices']:assert J[k]==base[k],k
 grouped=defaultdict(list);initial=[];packet=[]
 for ti,row in enumerate(J['transitions']):
  sid,to,k,val,f,rm,rv,goal,a=row
  assert not((k|val|f|rm|rv)>>n)and not(val&~k)and not(rv&~rm)
  assert 0<=sid<out and 0<=to<=out and to!=init
  if a==-1:assert sid==init;initial.append(ti)
  else:assert sid<init and a in keep;packet.append(ti)
  grouped[sid,to,goal,a].append((k,val,f,rm,rv))
 assert J['initial_transition_indices']==initial and J['packet_transition_indices']==packet
 expectedkeys=set();reentry=set();initial_count=0;packet_groups=0;cube_count=0
 # Resetting core values does not restrict the arbitrary initial residual choices.
 for sid,pose in enumerate(poses):
  p=complex(*pose[:2]);h=pose[2]
  if 2*L(rotation(p,phase))+A(h+phase)<S:
   key=(init,sid,0,-1);expectedkeys.add(key);rm=rv=0
   initialcore={p+rotation(z,h)for z in core}
   for q,c in zip(points,cells):
    if q in initialcore:rm|=((1<<c['bits'])-1)<<c['offset'];rv|=1<<c['offset']
   assert grouped[key]==[(0,0,0,rm,rv)];initial_count+=1
  for a in keep:
   end,dh,req,odd=g[a];dest=(*xy(p+rotation(end,h)),(h+dh)%4);to=where.get(dest,out)
   oldh=(h-dh)%4;oldp=p-rotation(end,oldh)
   if (*xy(oldp),oldh)not in where:reentry.add(sid)
   goal=int(a==target and p==0 and h==0)
   peak=2*L(rotation(p,phase))+max(A(h+phase),T(a,h+phase))
   if not goal and peak>=S:continue
   key=sid,to,goal,a;expectedkeys.add(key);packet_groups+=1;choices=[];f=rm=rv=0
   for q,c in zip(points,cells):
    local=rotation(q-p,-h);off=c['offset'];width=c['bits']
    if local not in req:
     assert local not in odd;choices.append(set(range(1<<width)));continue
    black=int(req[local])
    if width==1:
     choices.append({black})
     if local in odd:f|=1<<off
    else:
     if not black:allowed={0}
     elif goal and local in geometry[a]['inputs']:allowed={3}
     elif local in geometry[a]['inputs']and 2*L(rotation(q,phase))+I>=S:allowed={1,3}
     else:allowed={1,2,3}
     choices.append(allowed);rm|=3<<off
     rv|=(3 if local in geometry[a]['outputs']else black^(local in odd))<<off
   cubes=grouped[key];volume=0
   for m,val,flip,reset,value in cubes:
    assert(flip,reset,value)==(f,rm,rv)
    for c,allowed in zip(cells,choices):
     mask=(1<<c['bits'])-1;lm=m>>c['offset']&mask;lv=val>>c['offset']&mask
     vals={z for z in range(1<<c['bits'])if z&lm==lv};assert vals<=allowed
    volume+=1<<(n-m.bit_count());cube_count+=1
   for i,(m,val,*_)in enumerate(cubes):
    for m2,v2,*_ in cubes[:i]:assert (val^v2)&m&m2
   assert volume==prod(map(len,choices))
 key=init,out,0,-1;expectedkeys.add(key);assert grouped[key]==[(0,0,0,0,0)]
 assert set(grouped)==expectedkeys and J['reentry']==sorted(reentry)
 lines=[f"{n} {out+1} {len(J['transitions'])} {len(reentry)}",' '.join(map(str,start))]+[' '.join(map(str,t))for t in J['transitions']]+[' '.join(map(str,sorted(reentry)))]
 assert path.with_suffix('.dat').read_text()=='\n'.join(lines)+'\n'
 result=dict(status='PASS independent normalized entire-prefix strict-record abstraction',target=target,phase=phase,threshold=S,initial_weight=I,variables=n,patch_cells=len(points),watched_cells=len(watch),near_poses=len(poses),initial_near_branches=initial_count,packet_groups=packet_groups,guard_cubes=cube_count,reentry_poses=len(reentry),scope='Fixed target/phase strict UNFUNDED record only; no complete event-family or global confinement claim.',hashes={str(p.relative_to(ROOT)):digest(p)for p in[path,path.with_suffix('.dat'),pp]})
 if path.with_suffix('.bdd').exists():
  dest=OUT/(path.stem+'.invariant.json');subprocess.run([str(ROOT/'audits/check_guarded_reset_bdd64_invariant_independent'),str(path.with_suffix('.dat')),str(path.with_suffix('.bdd')),str(dest)],check=True);result['invariant']=json.loads(dest.read_text());result['hashes'][str(path.with_suffix('.bdd').relative_to(ROOT))]=digest(path.with_suffix('.bdd'))
 (OUT/(path.stem+'.model_check.json')).write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True);return result
if __name__=='__main__':
 for p in sys.argv[1:]:check(p)
