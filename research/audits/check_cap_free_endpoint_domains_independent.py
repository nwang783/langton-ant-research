from pathlib import Path
from itertools import product
from collections import Counter
import json,hashlib
S=Path(__file__);D=S.parents[1]/'first_departure_multiplicity_2026-10-24'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
files={'cap_free_one_use_RIGHT_endpoint_word_domains.md':'61ab7596','check_cap_free_one_use_endpoint_domains.py':'e40f4880','check_cap_free_one_use_endpoint_domains.json':'d0311e4e'}
for f,h in files.items():assert sha(D/f).startswith(h)
J=json.loads((D/'check_cap_free_one_use_endpoint_domains.json').read_text());H='NESW'
def out(w,r):return H[(H.index(w[r])+(1 if r%2==0 else-1))%4]
def source(f):return['E']if f==1 else['E'+'W'*(2*f-3),'E'+'W'*(2*f-2)]
def sink(f):return['E']if f==1 else['EE'+'WE'*(f-2),'EE'+'WE'*(f-2)+'W']
for row in J['formula_controls']:
 w=row['word'];fi=w.count('E');fo=sum(out(w,r)=='S'for r in range(len(w)));bal=w[::2].count('E')-w[::2].count('W')
 assert [fi,fo]==row['flows']and bal==row['R_balance']and len(w)==row['length'];assert w in(source(row['f'])if row['type']=='source'else sink(row['f']))
 # Derive stream sign directly: C_R0-C_opp=Sout-Win=R_E-R_W.
 assert fo-w.count('W')==bal
 assert bal==(3-row['f']if len(w)%2==0 else 2-row['f'])
 for rot in range(4):
  rw=''.join(H[(H.index(c)+rot)%4]for c in w);assert all(out(rw,r)==H[(H.index(out(w,r))+rot)%4]for r in range(len(w)))
counts=Counter();left=set()
# Bounded differential check of closed forms, not the all-length proof.
for n in range(1,13):
 for z in product('EW',repeat=n):
  w=''.join(z);fi=w.count('E');so=sum(out(w,r)=='S'for r in range(n));no=sum(out(w,r)=='N'for r in range(n))
  if w[0]=='E'and fi==1:assert w in source(so);counts['source']+=1
  if w[0]=='E'and so==1:assert w in sink(fi);counts['sink']+=1
  if w[0]=='W'and fi==1 and no==1:left.add(w)
assert left=={'WWE','WWEW'}
review=[
'WHITE complete chronology startsR and alternates, with fixed incoming E/W axis. At a RIGHT corner R0 arrivesE. Ein1 therefore fixes every later letterW, with south departures exactlyR0 plus allL, so f=1+floor(n/2) gives the two formulas for every integerf>=2 and singletonf1.',
'Sout1 fixes R0 as the only south departure. Therefore every later even R arrivesW and every odd L arrivesE. Ein count is1+floor(n/2); solving exactly gives EE(WE)^(f-2) and its optional finalW, again singletonf1. This is all-length position algebra, not a cutoff inference.',
'At the clockwise directed stream, C_R0 is southwest and C_opposite northeast in the normalized E/S corner. Thus C_R0-C_opposite=Sout-Win=(R_E+L_W)-(R_W+L_W)=R_E-R_W. Both formulas give3-f for even length and2-f for odd length. ONLY an independent R0-incident-max premise makes this nonnegative, forcing evenf<=3 or oddf<=2 and hence at most4 reads. No all-cap firstR maximum or cycle-level constancy is imported.',
'At LEFT incomingE/outN, R0 arrivesW. Nout1 prohibits every laterR_W and everyL_E. Ein1 must consequently be the soleR2E, so noR4 exists, giving exactlyWWE/WWEW. RIGHT1to1 remains singleton. Both constant-one internal alphabets are cap-free, while arbitrary endpointflow can still have arbitrarily long history without the independent height premise.',
'The conditions concern actual COMPLETE physical port totals and WHITE-first history. Prepared BLACK-first inputs, unknown exterior suppliers, physical event gluing and full-quotient closure are not solved. Nothing proves a general visit cap, odd-payment rule, unread exterior or global attraction.'
]
outobj=dict(status='PASS cap-free exact one-use endpoint and internal word-domain algebra',files={f:sha(D/f)for f in files},script=sha(S),finite_formula_controls=len(J['formula_controls']),bounded_differential_max_length=12,bounded_counts=counts,LEFT_exact=sorted(left),analytic_review=review)
S.with_suffix('.json').write_text(json.dumps(outobj,indent=2)+'\n');print(sha(S.with_suffix('.json')))
