"""Complete direct fine-step trees, with no macro palette or source imports."""
from pathlib import Path
import json,hashlib
P=Path(__file__).resolve().parents[1]
results=[]
for k in[5,9]:
 positions=[0j];turns=[];board={};nodes=0;macro_nodes=0;max_macro=0;endfail=0;deepest=0;digest=hashlib.sha256()
 def visit(heading):
  global nodes,macro_nodes,max_macro,endfail,deepest
  t=len(turns);nodes+=1;deepest=max(deepest,t)
  if t and t%k==0 and positions[-1]!=positions[t//k]:
   endfail+=1;digest.update((''.join(turns)+'\n').encode());return
  if t%k==0:macro_nodes+=1;max_macro=max(max_macro,t//k)
  # This safety assertion is not used to reject a branch or certify exhaustion.
  # If it fires, the entire audit fails instead of claiming a theorem.
  assert t<1000
  p=positions[-1];old=board.get(p)
  choices=[old]if old is not None else[False,True]
  for black in choices:
   d=heading*(1j if black else -1j);board[p]=not black;turns.append('L'if black else'R');positions.append(p+d);visit(d);positions.pop();turns.pop()
  if old is None:del board[p]
  else:board[p]=old
 visit(1j)
 saved=json.loads((P/f'causal_reduction/unit_scale/position_only_unit_k{k}.json').read_text());assert(macro_nodes,max_macro)==(saved['nodes'],saved['max_macros'])
 results.append({'radix':k,'status':'EXHAUSTED','fine_tree_nodes':nodes,'accepted_macro_nodes':macro_nodes,'max_macros':max_macro,'endpoint_mismatch_leaves':endfail,'largest_examined_time':deepest,'terminal_word_digest':digest.hexdigest()})
out={'status':'PASS occurrence-dependent pure p(kn)=p(n) exclusion on arbitrary initial colorings','results':results,'scope':'k5 and k9 only, no heading constraint, no eventual offsets or general unit-scale exclusion.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
