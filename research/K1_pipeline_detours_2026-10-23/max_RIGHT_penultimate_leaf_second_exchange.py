"""Port-ordinal obstruction to a penultimate graph leaf rooted at max RIGHT.
Complete white local words only; no front or period scan.
"""
from pathlib import Path
import json
root=Path(__file__).parent
base=json.loads((root/'triple_use_edge_graph_local_inventory.json').read_text())['rows'];H='NESW';roots=[];targets=[]
for r in base:
 h=r['headings']
 if len(h)>=3 and h[0]==h[2]:
  outs=[H[(H.index(x)+(1 if i%2==0 else-1))%4]for i,x in enumerate(h)]
  c_out=r['C']['NE']if outs[1]=='N'else r['C']['SW']
  ordinal=outs[:2].count(outs[1]);label=c_out-ordinal+1
  if label==-1:
   assert h[1]!=h[0]and ordinal==2 and outs.count(outs[1])in(3,4)
   roots.append(dict(headings=h,L1_output=outs[1],output_count=outs.count(outs[1]),ordinal=ordinal,label=label))
 if h.count('E')in(3,4):
  rank=[i for i,x in enumerate(h)if x=='E'][1]
  assert rank in(1,2)and len(h)>=3
  targets.append(dict(headings=h,port_count=h.count('E'),second_input_rank=rank))
assert len(roots)==6 and len(targets)==6
out=dict(scope=__doc__,root_count=len(roots),target_count=len(targets),roots=roots,targets=targets)
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
