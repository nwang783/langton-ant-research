"""Author literal/projection arithmetic control, not independent signoff."""
import json,hashlib
from pathlib import Path
R=Path(__file__).resolve().parents[1];P=R/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json';G=json.loads(P.read_text())['geometry']
chosen={0:(0,1),1:(0,1),4:(1,2),5:(1,2),6:(0,3),7:(0,3),8:(0,3),9:(0,3)};rows=[]
for a,p in chosen.items():
 g=G[a];c=g['name'].count('C');s=sum(p);prog=sum(g['endpoint'][:2]);assert s in[1,3]and len(g['word'])<=28+15*c
 if c==0:assert g['endpoint'][2]==0 and prog in[2,4]
 rows.append(dict(packet=a,name=g['name'],chosen_progress=s,head_progress_change=prog,heading_change=g['endpoint'][2],C_count=c,raw_length=len(g['word'])))
for j in range(10001):
 lo,hi=-2*j-11,2*j+7
 for parity in[0,1]:
  first=lo+((parity-lo)%2);n=0 if first>hi else(hi-first)//2+1
  assert n<=2*j+10
 if j==0:total=0
 total+=2*j+10
 assert total==(j+1)*(j+10)
O=dict(status='AUTHOR_ARITHMETIC_PASS_NOT_INDEPENDENT',scope='Complete recurrent-eight context-complete factors only; fixed-heading epochs and original-entry root boxes; no confinement.',geometry_sha256=hashlib.sha256(P.read_bytes()).hexdigest(),rows=rows,checked_j=10001,raw_duration_bound='28*(m-5)*(k+1)*(k+10)+15*k')
(R/'word_stabilization/dcuv_c_age_projection_quadratic_bound.json').write_text(json.dumps(O,indent=2)+'\n');print(json.dumps(O,indent=2))
