"""Existential initial-board normalization, not direct embedding of every initial board.
High-value initial residual blacks are never read in an unfunded record prefix and may be whitened.
The original explicit initial-core reset edges remain unchanged and override this restriction.
CLI ORIGINAL_GLOBAL_RECORD.json PREFIX
"""
from pathlib import Path
import json,sys,hashlib
source,out=map(Path,sys.argv[1:3]);J=json.loads(source.read_text());W=json.loads(Path(J['potential_file']).read_text());v=W['values'];d=(v['ax'],v['ay']);h=J['target_global_phase'];I=J['initial_token_weight'];S=J['record_threshold'];start=list(J['start']);changed=[]
def rot(q,h):x,y=q;return [(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
for c in J['origin_cells']:
 q=rot(c['cell'],h);value=I+2*sum(a*b for a,b in zip(d,q))
 if value>=S:
  mask=((1<<c['bits'])-1)<<c['offset'];start[1]|=mask;start[2]&=~mask;changed.append({'cell':c['cell'],'activation_value':value,'mask':mask})
N={**J,'start':start,'format':'guarded_reset_global_record_whitened_initial_v1','unwhitened_model_file':str(source.resolve()),'unwhitened_model_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'whitened_initial_cells':changed,'normalization_scope':'Existential recoloring of unread high-value INITIAL RESIDUAL identities only; explicit initial-core reset edges override the white start cube. All transition and reentry data unchanged.'}
out.with_suffix('.json').write_text(json.dumps(N,separators=(',',':')))
with out.with_suffix('.dat').open('w')as f:
 f.write(f"{N['n']} {N['out']+1} {len(N['transitions'])} {len(N['reentry'])}\n");f.write(' '.join(map(str,start))+'\n')
 for r in N['transitions']:f.write(' '.join(map(str,r))+'\n')
 f.write(' '.join(map(str,N['reentry']))+'\n')
print(json.dumps({'variables':N['n'],'whitened':len(changed),'initial_free_bits':N['n']-start[1].bit_count()}))
