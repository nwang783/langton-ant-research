"""Independent finite-weight OUT-only initial-state normalization."""
from pathlib import Path
import json,sys,subprocess
from check_global_record_residual_independent import check as basecheck
from check_dcuv_producer_model_independent import geometry,rotation,xy,ROOT,digest,resolve_file
OUT=ROOT/'audits/global_record_initial_out_replays';OUT.mkdir(exist_ok=True)
def check(path):
 path=Path(path).resolve();J=json.loads(path.read_text());assert J['format']=='guarded_reset_global_record_initial_out_v1'
 bp=resolve_file(path,J['base_model_file']);assert digest(bp)==J['base_model_sha256'];basecheck(bp);B=json.loads(bp.read_text())
 for k in ['n','points','poses','out','initial_control_pose','reentry','keep','target','target_pose','target_global_phase','potential_file','potential_sha256','record_threshold','resource_profile_file','resource_profile_sha256']:assert J[k]==B[k],k
 v=json.loads(Path(B['potential_file']).read_text())['values'];phase=B['target_global_phase'];S=B['record_threshold'];init=B['initial_control_pose'];out=B['out'];n=B['n']
 twice=lambda z:2*int(rotation(z,phase).real*v['ax']+rotation(z,phase).imag*v['ay'])
 allq={complex(*p)for p in B['points']}
 for x,y,h in B['poses']:
  for a in B['keep']:
   assert geometry[a]['inputs']
   allq.update(complex(x,y)+rotation(q,h)for q in geometry[a]['inputs'])
 minimum=min(map(twice,allq));I=max(B['initial_token_weight'],S-minimum);assert J['initial_token_weight']==I
 N=J['initial_out_normalization'];assert N['old_weight']==B['initial_token_weight']and N['new_weight']==I and N['minimum_twice_linear_value']==minimum and N['all_near_input_and_patch_cells']==[list(xy(q))for q in sorted(allq,key=xy)]
 assert all(I+twice(q)>=S for q in allq)
 rows=[r for r in B['transitions']if r[0]!=init];start=[out,(1<<n)-1,0]
 assert J['transitions']==rows and J['start']==start and J['initial_transition_indices']==[]and J['packet_transition_indices']==list(range(len(rows)))and J['high_initial_white_cells']==B['points']
 lines=[f"{n} {out+1} {len(rows)} {len(B['reentry'])}",' '.join(map(str,start))]+[' '.join(map(str,r))for r in rows]+[' '.join(map(str,B['reentry']))]
 assert path.with_suffix('.dat').read_text()=='\n'.join(lines)+'\n'
 result=dict(status='PASS independent finite-I OUT-only normalization',target=J['target'],phase=phase,variables=n,initial_weight=I,minimum_twice_linear_value=minimum,checked_physical_cells=len(allq),packet_edges=len(rows),hashes={str(p.relative_to(ROOT)):digest(p)for p in[path,path.with_suffix('.dat'),bp]})
 if path.with_suffix('.bdd').exists():
  dest=OUT/(path.stem+'.invariant.json');subprocess.run([str(ROOT/'audits/check_guarded_reset_bdd64_invariant_independent'),str(path.with_suffix('.dat')),str(path.with_suffix('.bdd')),str(dest)],check=True);result['invariant']=json.loads(dest.read_text())
 (OUT/(path.stem+'.model_check.json')).write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True);return result
if __name__=='__main__':
 for p in sys.argv[1:]:check(p)
