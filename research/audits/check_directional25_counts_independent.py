from pathlib import Path
import json,hashlib
P=Path(__file__).resolve().parents[1];W=P/'word_stabilization'
file=W/'dcv_protected_kinematic_count_signedbase.tsv'
count={tuple(map(int,line.split()[:8]))for line in file.read_text().splitlines()}
prior=json.loads((P/'audits/counted_target_queries_independent.json').read_text())
assert hashlib.sha256(file.read_bytes()).hexdigest()==prior['sha256']['word_stabilization/dcv_protected_kinematic_count_signedbase.tsv']
rows=[tuple(map(int,line.split()))for line in(W/'dcv_directional25_targets.tsv').read_text().splitlines()];c=[0,1,2,3,0,1,2];results=[]
for row in rows:
 methods=[]
 for k in range(4):
  trivial=k<c[row[0]]or(row[4]+k)%4!=0
  assert trivial or(*row,k)in count
  methods.append('source count/heading'if trivial else'signed counted clause')
 assert(*row,4)not in count
 lower=next(k for k in range(4,8)if(row[4]+k)%4==0)
 results.append({'tuple':row,'low_count_exclusions':methods,'minimum_C_count':lower,'overflow_excluded':False})
out={'status':'PASS all25 require at least4 C macros; no overflow exclusion','cases':results,'counted_relation_sha256':hashlib.sha256(file.read_bytes()).hexdigest()}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
