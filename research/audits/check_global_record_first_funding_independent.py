"""Independent first-packet initial-funding contraction of residual record model."""
from pathlib import Path
import json,sys,subprocess
from check_global_record_residual_independent import check as basecheck
from check_dcuv_producer_model_independent import geometry,rotation,ROOT,digest,resolve_file
OUT=ROOT/'audits/global_record_first_funding_replays';OUT.mkdir(exist_ok=True)
def check(path):
 path=Path(path).resolve();J=json.loads(path.read_text());assert J['format']=='guarded_reset_global_record_first_funding_v1'
 bp=resolve_file(path,J['base_model_file']);assert digest(bp)==J['base_model_sha256'];basecheck(bp);B=json.loads(bp.read_text())
 for k in ['n','points','poses','start','out','initial_control_pose','reentry','keep','target','target_pose','potential_file','potential_sha256','record_threshold','initial_token_weight','high_initial_white_cells','resource_profile_file','resource_profile_sha256']:assert J[k]==B[k],k
 W=json.loads(Path(B['potential_file']).read_text())['values'];phase=B['target_global_phase'];I=B['initial_token_weight'];S=B['record_threshold'];init=B['initial_control_pose'];out=B['out'];n=B['n']
 L=lambda q:int(q.real*W['ax']+q.imag*W['ay'])
 rows=[r for r in B['transitions']if r[0]!=init];packet=list(range(len(rows)));initial=[];records=[];rejections=[]
 for ii in B['initial_transition_indices']:
  first=B['transitions'][ii];fr,sid,k0,v0,f0,c0,r0,g0,a0=first
  assert(fr,k0,v0,f0,r0,g0,a0)==(init,0,0,0,0,0,-1)
  if sid==out:
   initial.append(len(rows));records.append(dict(edge=len(rows),initial_out=True,source_initial_edge=ii));rows.append(first);continue
  x,y,h=B['poses'][sid];p=complex(x,y)
  for ti,t in enumerate(B['transitions']):
   if t[0]!=sid:continue
   _,to,k,v,f,c,r,goal,a=t
   high=[]
   for q in sorted(geometry[a]['inputs'],key=lambda q:(q.real,q.imag)):
    q=p+rotation(q,h);av=I+2*L(rotation(q,phase))
    if av>=S:high.append([int(q.real),int(q.imag),av])
   if high or goal:rejections.append(dict(initial_edge=ii,packet_edge=ti,high_initial_inputs=high,goal=bool(goal)));continue
   if v&c0:rejections.append(dict(initial_edge=ii,packet_edge=ti,guard_core_conflict=True));continue
   # Derive composition independently by truth table for every one-bit coordinate.
   cm=cv=flip=clear=reset=0
   for bit in range(n):
    flag=1<<bit;allowed=[];values=[]
    for xb in (0,1):
     middle=0 if c0&flag else xb
     if(k&flag)and middle!=bool(v&flag):continue
     allowed.append(xb)
     final=(middle ^ bool(f&flag))if not(c&flag)else int(bool(r&flag));values.append(final)
    assert allowed
    if len(allowed)==1:cm|=flag;cv|=allowed[0]<<bit
    # Compare the full composed update, including guard-excluded values, to a canonical reset/XOR map.
    full=[]
    for xb in(0,1):
     middle=0 if c0&flag else xb;full.append((middle ^ bool(f&flag))if not(c&flag)else int(bool(r&flag)))
    if full[0]==full[1]:clear|=flag;reset|=full[0]<<bit
    elif full==[1,0]:flip|=flag
    else:assert full==[0,1]
   initial.append(len(rows));records.append(dict(edge=len(rows),source_initial_edge=ii,source_packet_edge=ti,first_pose=B['poses'][sid],first_packet=a,initial_core_clear=c0));rows.append([init,to,cm,cv,flip,clear,reset,0,a])
 assert J['transitions']==rows and J['initial_transition_indices']==initial and J['packet_transition_indices']==packet
 assert J['first_packet_compositions']==records and J['first_packet_rejections']==rejections
 lines=[f"{n} {out+1} {len(rows)} {len(B['reentry'])}",' '.join(map(str,B['start']))]+[' '.join(map(str,r))for r in rows]+[' '.join(map(str,B['reentry']))]
 assert path.with_suffix('.dat').read_text()=='\n'.join(lines)+'\n'
 result=dict(status='PASS independent first-packet funding and bitwise composition',target=J['target'],phase=phase,variables=n,initial_compositions=len(records),initial_rejections=len(rejections),hashes={str(p.relative_to(ROOT)):digest(p)for p in[path,path.with_suffix('.dat'),bp]})
 if path.with_suffix('.bdd').exists():
  dest=OUT/(path.stem+'.invariant.json');subprocess.run([str(ROOT/'audits/check_guarded_reset_bdd64_invariant_independent'),str(path.with_suffix('.dat')),str(path.with_suffix('.bdd')),str(dest)],check=True);result['invariant']=json.loads(dest.read_text())
 (OUT/(path.stem+'.model_check.json')).write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True);return result
if __name__=='__main__':
 for p in sys.argv[1:]:check(p)
