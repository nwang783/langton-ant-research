"""Normalize never-consumed high-valued initial residual cells to white.
CLI GLOBAL_RECORD_MODEL.json PREFIX. Requires the entire-prefix record protocol,
not an anchored producer suffix. Initial-core installation edges are unchanged.
The literal input/output ledger justifies existential trajectory recoloring.
"""
from pathlib import Path
import sys,json,hashlib
src,out=map(Path,sys.argv[1:3]);J=json.loads(src.read_text());assert J['format']=='guarded_reset_global_record_prefix_v1';P=json.loads(Path(J['potential_file']).read_text());v=P['values'];phase=J['target_global_phase'];I=J['initial_token_weight'];S=J['record_threshold'];start=J['start'][:];changed=[]
def rot(q,h):x,y=q;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
for c in J['origin_cells']:
 x,y=rot(c['cell'],phase)
 if I+2*(v['ax']*x+v['ay']*y)>=S:
  mask=((1<<c['bits'])-1)<<c['offset'];start[1]|=mask;start[2]&=~mask;changed.append(c['cell'])
new={**J,'start':start,'format':'guarded_reset_global_record_prefix_high_white_v1','normalization_base_file':str(src.resolve()),'normalization_base_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'high_initial_white_cells':changed,'initial_recoloring_scope':'Existential preservation for unfunded full prefixes: these initial residual black identities cannot be consumed, hence all complete contexts avoid them. Initial-core installation edges still overwrite their core cells black.'}
out.with_suffix('.json').write_text(json.dumps(new,separators=(',',':')))
with out.with_suffix('.dat').open('w')as f:
 f.write(f"{J['n']} {J['out']+1} {len(J['transitions'])} {len(J['reentry'])}\n");f.write(' '.join(map(str,start))+'\n')
 for r in J['transitions']:f.write(' '.join(map(str,r))+'\n')
 f.write(' '.join(map(str,J['reentry']))+'\n')
print(json.dumps({'variables':J['n'],'high_initial_cells_fixed_white':len(changed),'start':start,'source_hash':new['normalization_base_sha256']}))
