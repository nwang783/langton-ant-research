"""Exact first-R incidence of the two fixed late-supplier local controls.
Outside first headings/caps/colors remain arbitrary within the same actual
incoming-axis sector. Not a complete-front or prepared-factor existence test.
"""
from pathlib import Path
import json
H='NESW';V={'N':(0,1),'E':(1,0),'S':(0,-1),'W':(-1,0)}
j=json.loads(Path(__file__).with_name('check_fixed_LL_L3_supplier_controls.json').read_text());rows=[]
for row in j['rows']:
 import ast
 hs={ast.literal_eval(p):h for p,h in row['histories'].items()}
 def dest(p):
  h=hs[p][0];d=H[(H.index(h)+1)%4];return p[0]+V[d][0],p[1]+V[d][1]
 def incoming_possible(p):
  axis='NS'if sum(p)%2==0 else'EW'
  out=[]
  for h in axis:
   q=p[0]-V[h][0],p[1]-V[h][1]
   assert q in hs
   if dest(q)==p:out.append(q)
  return out
 U=(1,2);Y=(1,1)
 assert incoming_possible(U)==[] and incoming_possible(Y)==[U]and dest(U)==Y
 rows.append(dict(kind=row['kind'],U_indegree=0,Y_unique_predecessor=U,known_first_departures={str(p):dest(p)for p in[(0,2),(2,2),(1,2),(1,0)]},cannot_put_U_or_Y_on_any_b_cycle=True))
Path(__file__).with_suffix('.json').write_text(json.dumps(dict(scope=__doc__,rows=rows,full_quotient_reason='Any incoming quotient edge lifts to one of these actual physical neighbor edges; no rotation or new first heading is introduced.'),indent=2)+'\n');print('PASS both fixed controls: U has zero b-indegree and solely feeds Y')
