"""Canonical turn-level inequalities in all complete WHITE cap-four histories.
Uses the already frozen 78-sheet local reconstruction, no front search.
"""
from pathlib import Path
import json
r=Path(__file__).parent
base=json.loads((r/'canonical_sheet_two_level_contact_barriers.json').read_text())['checks']
rows=[];counts={'L':0,'R_non_singleton':0,'R_singleton':0}
for q in base:
 h=q['headings'];j=q['j'];C=q['C'];L=q['L']
 for p in q['pairs']:
  if p['turn']=='L':
   assert max(C.values())>=j+1
   typ='L'
  elif len(h)==1:
   assert set(C.values())=={j,j-1} and set(L.values())=={j-1}
   typ='R_singleton'
  else:
   assert min(L.values())<=j-2
   typ='R_non_singleton'
  counts[typ]+=1
  rows.append(dict(headings=h,j=j,C=C,L=L,canonical_pair=p,type=typ))
# Independently check the exact reflex inequalities against bounded-disk
# constraints at every possible E/W physical corner.
H='NESW';cw=[];ccw=[]
for q in base:
 h=q['headings'];j=q['j'];C=q['C'];L=q['L']
 for p in q['pairs']:
  x=h[p['in_rank']]
  if p['turn']=='L' and max(C.values())<=j and L['SE' if x=='E' else 'NW']>=j-1:cw.append((h,j,p))
  if len(h)%2==0 and p['turn']=='R' and min(L.values())>=j-1 and C['NE' if x=='E' else 'SW']<=j:ccw.append((h,j,p))
assert not cw and not ccw
out=dict(scope=__doc__,counts=counts,turns=rows,CW_reflex_survivors=cw,zero_output_CCW_reflex_survivors=ccw)
p=Path(__file__).with_suffix('.json');p.write_text(json.dumps(out,indent=2)+'\n')
print('PASS',counts,'no allowed reflex corner')
