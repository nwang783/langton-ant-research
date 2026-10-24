from pathlib import Path
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'word_stabilization/U_foreign_prefix_renewal_return_frozen_20261023_2204'
ns={'__file__':str(R/'audits/check_foreign_kinked_barrier_turn_independent.py')};exec(Path(ns['__file__']).read_text().split('geometries=[]')[0],ns)
W,M,walk,center,xy=(ns[k]for k in('W','M','walk','center','xy'))
foreign=3+3j;C=walk(W['C']);h=(0-C['h'])%4;p=foreign-C['p']*(-1j)**h;assert(p,h)==(2+3j,1)
east=2+1j;local=(east-p)/((-1j)**h);assert local==2
assert next((i,ch)for i,(q,hh,ch)in enumerate(C['reads'])if q==local)==(8,'R')and C['req'][local]is False
U=walk(W['U']);breaker=3-1j;assert breaker+U['p']==foreign and U['h']==0 and center(foreign,0)==5+5j
assert W['F'].startswith(M)
for source in('U','UC','UCC'):
 tr=walk(''.join(W[c]for c in source));assert tr['feasible'];assert tr['reads'][:28]==U['reads']
manifest=D/'manifest.json';sha=hashlib.sha256(manifest.read_bytes()).hexdigest();assert sha=='a852bd155d9757002dc31476682376c7ead567fbaa0bd1aaf1f1d52324fe2b1f'
data=json.loads(manifest.read_text())
for name,value in data['files'].items():assert hashlib.sha256((D/name).read_bytes()).hexdigest()==value
for name,value in data['dependencies'].items():assert hashlib.sha256((R/name).read_bytes()).hexdigest()==value
out={'status':'PASS actual east-pair renewal forces earlier identical U-base exit before F(3,3,N) age8','manifest_sha256':sha,'preceding_C_pose':[*xy(p),h],'old_east_before_white':[2,1,8],'breaker_full_entry':[3,-1,0,4],'earlier_and_final_base_exit':[3,3,0],'doubled_center':[5,5],'analytic':['Original east identity before-white at the final C forces its actual earlier directed right U-family retirement. The signed exact-four theorem fixes that full breaker entry at source clock4.','All three breaker types share the literal U-base exit(3,3,N) at clock4, before their tails. Final preceding C exits there again at8, a genuinely nonadjacent earlier vertex return inside the complete-eight interval.','The final cut has actual M11 supplied by foreign F. No following complete-eight packet or invented terminal marker is required. The four extra Cs ensure the earlier plain-U base exit also has an actual successor.'],'remaining_U_source_prefix_ports':[['F',[2,4,0],8,1],['Q',[2,4,0],8,1]],'scope':'One U-source F-prefix interface excluded; no Q/B-tail, other source, attainment or universal capture conclusion.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
