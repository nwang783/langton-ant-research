"""Complete cap-four WHITE local histories at one prescribed S-directed port.
No front, period, width, drift, multiplicity, or seed scan.
"""
from itertools import product
from pathlib import Path
import json
H='NESW'
def output(hs,r):
 return H[(H.index(hs[r])+(1 if r%2==0 else -1))%4]
def repair(r,n):
 return 3-r if n>=3 and r in (1,2) else r
source=[];target=[]
for n in range(1,5):
 for hs in product('EW',repeat=n):
  p=[r for r in range(n)if output(hs,r)=='S']
  if n>=3 and set((1,2))<=set(p):
   source.append(dict(headings=''.join(hs),port_ranks=p,rank12_ordinals=[p.index(1),p.index(2)]))
 for hs in product('NS',repeat=n):
  p=[r for r in range(n)if hs[r]=='S']
  if len(p)>=2:
   row=dict(headings=''.join(hs),port_ranks=p,repaired_outputs=[output(hs,repair(r,n))for r in p])
   row['rank12_ordinals']=[p.index(1),p.index(2)]if n>=3 and set((1,2))<=set(p)else None
   row['both_unit_C_L_turns']=len(p)==2 and row['repaired_outputs']==['W','E']
   target.append(row)
matched=[];possible=[]
for s in source:
 for t in target:
  if len(s['port_ranks'])!=len(t['port_ranks']):continue
  row=dict(source=s['headings'],target=t['headings'],flow=len(s['port_ranks']),source_ranks=s['port_ranks'],target_ranks=t['port_ranks'],target_of_source_rank12=[t['port_ranks'][i]for i in s['rank12_ordinals']])
  possible.append(row)
  if s['rank12_ordinals']==t['rank12_ordinals']:matched.append(row)
assert len(source)==6 and len(matched)==10
assert {r['flow']:sum(q['flow']==r['flow']for q in matched)for r in matched}=={2:4,3:5,4:1}
flat=[r for r in target if r['both_unit_C_L_turns']]
assert {r['headings']for r in flat}=={'SS','NSS','SSN','NNSS','NSSN','SNNS','SSNN'}
out=dict(scope=__doc__,source_profiles=source,target_profiles=target,matched=matched,counts={str(f):sum(r['flow']==f for r in matched)for f in (2,3,4)},unit_loop_target_profiles=flat,warning='Targets SS/SSN/SSNN/NNSS/SNNS have the two necessary elementary-loop turns without matching rank12 at this edge. Some hand the lower L loop to another C loop; others have no exchange at this edge. Rows are necessary port histories, not an attained complete front.')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(dict(matched_counts=out['counts'],unit_loop_targets=[r['headings']for r in flat],possible_ports=len(possible)),indent=2))
