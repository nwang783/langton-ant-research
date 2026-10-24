"""Monotone initial-activation parameter refinement for an implicit-core residual model.
CLI MODEL.json PREFIX I. Literal transitions are unchanged; only initial white mask grows.
"""
from pathlib import Path
import sys,json,hashlib
source,out=map(Path,sys.argv[1:3]);I=int(sys.argv[3]);J=json.loads(source.read_text());assert J['format']=='guarded_reset_global_record_residual_v1';assert I>=J['initial_token_weight'];W=json.loads(Path(J['potential_file']).read_text());d=W['values']['ax'],W['values']['ay'];h=J['target_global_phase'];S=J['record_threshold']
def rot(q,h):x,y=q;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
high=[q for q in J['points']if I+2*sum(a*b for a,b in zip(d,rot(q,h)))>=S];mask=sum(1<<i for i,q in enumerate(J['points'])if q in high);assert mask&J['start'][1]==J['start'][1];new={**J,'initial_token_weight':I,'minimum_required_initial_weight':J.get('minimum_required_initial_weight',J['initial_token_weight']),'start':[J['start'][0],mask,0],'high_initial_white_cells':high,'lower_weight_model_file':str(source.resolve()),'lower_weight_model_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'activation_parameter_scope':'Any I>=minimum demand is valid; higher I shrinks the unfunded-record event class. Different case certificates combine at their maximum I.'};out.with_suffix('.json').write_text(json.dumps(new,separators=(',',':')))
with out.with_suffix('.dat').open('w')as f:
 f.write(f"{new['n']} {new['out']+1} {len(new['transitions'])} {len(new['reentry'])}\n");f.write(' '.join(map(str,new['start']))+'\n')
 for r in new['transitions']:f.write(' '.join(map(str,r))+'\n')
 f.write(' '.join(map(str,new['reentry']))+'\n')
print(json.dumps({'I':I,'free_initial_bits':new['n']-mask.bit_count(),'variables':new['n']}))
