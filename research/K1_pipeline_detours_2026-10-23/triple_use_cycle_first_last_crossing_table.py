"""Literal first/last cycle-edge eligibility for all8 flow3 internal WHITE cells.
Uses physical ports and rank order, not an assumed chronological circuit.
"""
from pathlib import Path
import json
root=Path(__file__).parent
base=json.loads((root/'triple_use_edge_graph_local_inventory.json').read_text())['rows']
rows=[];H='NESW'
for r in base:
 if r['type']!='internal':continue
 h=r['headings'];fl=r['port_flows'];hi='E'if fl['W']==3 else'W';ho='N'if fl['N']==3 else'S'
 turn='RIGHT'if(H.index(ho)-H.index(hi))%4==1 else'LEFT'
 ti=[i for i,c in enumerate(h)if c==hi]
 tout=[i for i,c in enumerate(h)if H[(H.index(c)+(1 if i%2==0 else-1))%4]==ho]
 si=[i for i in range(4)if i not in ti];so=[i for i in range(4)if i not in tout]
 assert len(ti)==len(tout)==3 and len(si)==len(so)==1
 first=[i for i in si if i in tout and not any(j<i for j in tout)]
 last=[i for i in so if i in ti and not any(j>i for j in ti)]
 assert not first or(first==[0]and turn=='LEFT'and h[0]!=h[1]==h[2]==h[3])
 assert not last or(last==[3]and turn=='RIGHT'and h[0]==h[2]==h[3]!=h[1])
 rows.append(dict(headings=h,triple_input=hi,triple_output=ho,turn=turn,triple_input_ranks=ti,triple_output_ranks=tout,single_input_rank=si[0],single_output_rank=so[0],single_port_side='RIGHT'if turn=='LEFT'else'LEFT',eligible_first_edge_departure=first,eligible_last_edge_arrival=last))
assert len(rows)==8 and sum(bool(r['eligible_first_edge_departure'])for r in rows)==2 and sum(bool(r['eligible_last_edge_arrival'])for r in rows)==2
out=dict(scope=__doc__,count=len(rows),rows=rows)
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
