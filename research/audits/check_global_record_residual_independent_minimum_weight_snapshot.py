"""Independent implicit-core, whitened residual membership record model.
Literal geometry and exact ordered ledger; no author generator imports.
"""
from pathlib import Path
import json,sys,subprocess
from check_dcuv_producer_model_independent import geometry,core,rotation,xy,walk,raws,mark,ROOT,digest,resolve_file
from check_dcuv_patch_model_independent import validate_profile
OUT=ROOT/'audits/global_record_residual_replays';OUT.mkdir(exist_ok=True)
def check(path):
 path=Path(path).resolve();J=json.loads(path.read_text());assert J['format']=='guarded_reset_global_record_residual_v1'
 keep=validate_profile(J);assert J['keep']==list(keep)
 pp=resolve_file(path,J['potential_file']);assert digest(pp)==J['potential_sha256'];P=json.loads(pp.read_text());assert P['profile_sha256']==J['resource_profile_sha256'];v=P['values']
 phase=J['target_global_phase'];target=J['target'];assert phase in range(4)and target in keep and J['target_pose']==[0,0,0]
 L=lambda z:int(z.real*v['ax']+z.imag*v['ay']);A=lambda h:L(rotation(-1+1j,h))+v[f'c{h%4}']
 g=[(*walk(raw)[:2],walk(raw+mark)[2],walk(raw)[3])for raw in raws]
 def T(a,h):
  h%=4;end,dh,_,_=g[a]
  return max([2*L(rotation(end,h))+A(h+dh)]+[2*L(rotation(q,h))+v[f'w_{a}_{i}_{h}']for i,q in enumerate(geometry[a]['outputs'])])
 S=T(target,phase);I=max(T(a,h)-2*L(rotation(q,h))for a in keep for h in range(4)for q in geometry[a]['inputs'])
 assert S>A(phase)and J['record_threshold']==S and J['initial_token_weight']==I
 assert J['core_offsets']==[A(h)for h in range(4)]and J['created_peaks']==[[a,h,T(a,h)]for a in keep for h in range(4)]
 points=[complex(*q)for q in J['points']];assert len(points)==len(set(points))and points==sorted(points,key=xy);ix={q:i for i,q in enumerate(points)};n=len(points)
 assert J['n']==n and n<63
 high={q for q in points if I+2*L(rotation(q,phase))>=S};assert geometry[target]['inputs']<=high
 assert J['high_initial_white_cells']==[list(xy(q))for q in sorted(high,key=xy)]
 poses=set()
 for q in points:
  for a in keep:
   for h in range(4):
    for z in g[a][2]:
     p=q-rotation(z,h)
     if(sum(xy(p))-h)%2==0:poses.add((*xy(p),h))
 poses=sorted(poses);where={q:i for i,q in enumerate(poses)};init=len(poses);out=init+1
 assert J['poses']==[list(p)for p in poses]and J['initial_control_pose']==init and J['out']==out
 mask=lambda s:sum(1<<ix[q]for q in s if q in ix)
 start=[init,mask(high),0];assert J['start']==start
 expected=[];initial=[];packet=[];reentry=set()
 for sid,pose in enumerate(poses):
  p=complex(*pose[:2]);h=pose[2];oldcore={p+rotation(z,h)for z in core}
  if 2*L(rotation(p,phase))+A(h+phase)<S:
   initial.append(len(expected));expected.append([init,sid,0,0,0,mask(oldcore),0,0,-1])
  for a in keep:
   end,dh,req,odd=g[a];ep=p+rotation(end,h);eh=(h+dh)%4;to=where.get((*xy(ep),eh),out)
   predh=(h-dh)%4;predp=p-rotation(end,predh)
   if (*xy(predp),predh)not in where:reentry.add(sid)
   goal=int(a==target and p==0 and h==0)
   if not goal and 2*L(rotation(p,phase))+max(A(h+phase),T(a,h+phase))>=S:continue
   newcore={ep+rotation(z,eh)for z in core};inputs={p+rotation(z,h)for z in geometry[a]['inputs']};outputs={p+rotation(z,h)for z in geometry[a]['outputs']}
   assert not inputs&oldcore and not outputs&newcore
   # Derive residual guard from full entry read requirements, not a cached graph.
   guard=mask(oldcore);value=0
   for q in points:
    z=rotation(q-p,-h)
    if z in req:
     if q in oldcore:assert req[z]
     else:
      guard|=1<<ix[q]
      if req[z]:value|=1<<ix[q]
   # Literal output equality verifies removal/install even at recycled U inputs.
   entry={p+rotation(z,h)for z,b in req.items()if b}
   rawflip={p+rotation(z,h)for z in odd}
   assert entry==oldcore|inputs and(entry^rawflip)==newcore|outputs
   packet.append(len(expected));expected.append([sid,to,guard,value,0,mask(inputs|outputs|newcore),mask(outputs),goal,a])
 initial.append(len(expected));expected.append([init,out,0,0,0,0,0,0,-1])
 assert J['transitions']==expected and J['initial_transition_indices']==initial and J['packet_transition_indices']==packet and J['reentry']==sorted(reentry)
 lines=[f'{n} {out+1} {len(expected)} {len(reentry)}',' '.join(map(str,start))]+[' '.join(map(str,r))for r in expected]+[' '.join(map(str,sorted(reentry)))]
 assert path.with_suffix('.dat').read_text()=='\n'.join(lines)+'\n'
 result=dict(status='PASS independent whitened implicit-core residual abstraction',target=target,phase=phase,threshold=S,initial_weight=I,variables=n,initial_free_bits=n-len(high),near_poses=len(poses),initial_near_branches=len(initial)-1,packet_transitions=len(packet),reentry_poses=len(reentry),scope='Fixed target/phase unfunded record only; whole family not asserted.',hashes={str(p.relative_to(ROOT)):digest(p)for p in[path,path.with_suffix('.dat'),pp]})
 if path.with_suffix('.bdd').exists():
  dest=OUT/(path.stem+'.invariant.json');subprocess.run([str(ROOT/'audits/check_guarded_reset_bdd64_invariant_independent'),str(path.with_suffix('.dat')),str(path.with_suffix('.bdd')),str(dest)],check=True);result['invariant']=json.loads(dest.read_text());result['hashes'][str(path.with_suffix('.bdd').relative_to(ROOT))]=digest(path.with_suffix('.bdd'))
 (OUT/(path.stem+'.model_check.json')).write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True);return result
if __name__=='__main__':
 for p in sys.argv[1:]:check(p)
