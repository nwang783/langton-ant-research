"""Strengthening: opposed interior center coincidences force a V corridor."""
import itertools,json
from pathlib import Path
from verify_uv_interior_crossing import window,SOURCE
import hashlib
words=list(map(''.join,itertools.product('UV',repeat=5)));rows=[];unexcluded=[]
for x in words:
 af,al,ns,ne=window(x,0)
 for y in words:
  bf,bl,ss,se=window(y,2)
  qlist=[q for q in al.keys()&bf.keys()if al[q][3]==bf[q][3] and ns[1]<q[1]<ne[1]-1 and se[1]+1<q[1]<ss[1] and q[1]<ne[1]-5]
  compliant=x[2]=='V' and y[1:3]=='VV'
  if not compliant:
   assert qlist,(x,y)
   q=min(qlist,key=lambda q:(q[1],q[0]));rows.append(dict(north=x,south=y,cell=q,letter=al[q][3],north_last=al[q],south_first=bf[q],north_window_start=ns,north_window_end=ne,south_window_start=ss,south_window_end=se))
  if not qlist:unexcluded.append([x,y])
assert len(rows)==896 and len(unexcluded)==56
out={'status':'PASS','source_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),'necessary_rule':'earlier outgoing V; later incoming and outgoing V','excluded_cases':rows,'unexcluded_windows_not_asserted_feasible':unexcluded}
Path(__file__).with_name('uv_shared_center_certificate.json').write_text(json.dumps(out,indent=2))
print('PASS: all 896 rule-violating five-window pairs have shielded flip conflicts')
