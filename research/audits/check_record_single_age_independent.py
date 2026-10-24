"""Independent complete valid-age truth tables on every supplied actual-packet edge."""
from pathlib import Path
from collections import defaultdict
import json,sys
from check_dcuv_producer_model_independent import ROOT,digest,resolve_file,geometry,rotation,xy,raws
from check_record_far_height_independent import datacheck,invariant,OUT
COUNTS={0:0,1:1,4:0,5:1,6:2,7:0,8:1,9:2}
def check(path):
 path=Path(path).resolve();J=json.loads(path.read_text());assert J['format']=='signed_upper_input_c_age_guarded_reset_v1'
 bp=resolve_file(path,J['base_model_file']);assert digest(bp)==J['base_model_sha256'];B=json.loads(bp.read_text())
 if B['format']=='guarded_reset_live_pruning_v1':
  from check_guarded_reset_live_independent import check as basecheck
 elif B['format']=='guarded_reset_global_record_far_height_first_funding_v1':
  from check_record_far_first_independent import check as basecheck
 else:raise AssertionError('Unreviewed age base '+B['format'])
 basecheck(bp);assert not B['reentry']
 if 'poses'in B:
  poses=B['poses'];points=B['points']
 else:
  P=json.loads(resolve_file(bp,B['base_model_file']).read_text());poses=[P['poses'][i]if i<len(P['poses'])else None for i in B['retained_old_positions']];points=P['points']
 n=B['n'];low=(1<<n)-1;q=complex(*J['watched_cell']);assert n==len(points) and [int(q.real),int(q.imag)]in points
 assert J['poses']==poses and J['points']==points and J['age_offset']==n and J['age_bits']==3 and J['age_values']==[0,1,2,3,4]
 assert J['packet_C_counts']=={str(a):c for a,c in COUNTS.items()}
 assert J['n']==n+3 and J['out']==B['out'] and J['reentry']==[]
 assert J['start']==[B['start'][0],B['start'][1]|(7<<n),B['start'][2]|(4<<n)]
 assert len(J['edge_cases'])==len(J['transitions']);groups=defaultdict(list)
 for row,meta in zip(J['transitions'],J['edge_cases']):
  ei,declared_old,declared_new=meta;assert 0<=ei<len(B['transitions']);old=B['transitions'][ei]
  assert row[:2]==old[:2] and row[7:]==old[7:]
  for k in range(2,7):assert row[k]&low==old[k]
  assert row[4]>>n==0 and not any(x>>(n+3)for x in row[2:7])
  assert row[3]&~row[2]==row[6]&~row[5]==0
  groups[ei].append(row)
 tests=0;rejected=0
 for ei,e in enumerate(B['transitions']):
  a=e[8];assert a in COUNTS
  pose=poses[e[0]]if e[0]<len(poses)else None;hits=set();outs=set();upper=False
  if pose is not None:
   p=complex(*pose[:2]);h=pose[2]
   hits={p+rotation(z,h)for z in geometry[a]['context']}
   outs={p+rotation(z,h)for z in geometry[a]['outputs']}
   upper=a in (7,8,9) and q in {p+rotation(complex(x,y),h)for x,y in [(-1,4),(0,2),(0,3)]}
  for age in range(5):
   expected=None if upper and age<4 else(COUNTS[a]if q in outs else 4 if q in hits else min(4,age+COUNTS[a]))
   results=set()
   for t in groups[ei]:
    if (age & (t[2]>>n)) != (t[3]>>n):continue
    val=(age^(t[4]>>n));val=(val&~(t[5]>>n))|(t[6]>>n);results.add(val)
   assert results==(set()if expected is None else{expected}),(ei,age,expected,results)
   tests+=1;rejected+=expected is None
 datacheck(path,J)
 result={'status':'PASS independent all-edge single-token C-age truth tables and complete base reconstruction','variables':J['n'],'base_edges':len(B['transitions']),'age_truth_tests':tests,'forbidden_young_cases':rejected,'watched_cell':J['watched_cell'],'hashes':{str(p.relative_to(ROOT)):digest(p)for p in(path,path.with_suffix('.dat'),bp)},'scope':'Signed input-age refinement only; initial/forgotten age4, every real far packet included. No case exclusion without checked invariant.'}
 invariant(path,result);dest=OUT/(path.stem+'.age_model_check.json');dest.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True);return result
if __name__=='__main__':
 for p in sys.argv[1:]:check(p)
