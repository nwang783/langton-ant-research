"""Lift discovery path through exact live pruning and literal-DFA control product.
The colors and packet actions are unchanged. No epsilon quotient accepted.
CLI LIVE.json PATH.log OUTPUT.witness.
"""
import json,sys
from pathlib import Path
model,path,out=map(Path,sys.argv[1:4]);J=json.loads(model.read_text());assert J['format']=='guarded_reset_live_pruning_v1';D=json.loads(Path(J['base_model_file']).read_text());assert D['format']=='guarded_reset_literal_dfa_product_v1';B=json.loads(Path(D['base_model_file']).read_text());rows=[]
for line in path.read_text().splitlines():
 if line.startswith('WITNESS'):
  _,s,m,a=line.split();sid=J['retained_old_positions'][int(s)];bs=B['out']if sid==D['out']else D['position_map'][sid][0];rows.append(f'WITNESS {bs} {m} {a}')
out.write_text('\n'.join(rows)+'\n');print(json.dumps({'base':D['base_model_file'],'steps':len(rows),'output':str(out)}))
