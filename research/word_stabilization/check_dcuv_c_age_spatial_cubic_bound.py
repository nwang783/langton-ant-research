"""Author arithmetic/geometry control. This is not independent signoff."""
import json,hashlib
from pathlib import Path
from fractions import Fraction
ROOT=Path(__file__).resolve().parents[1]
gp=ROOT/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json'
ap=ROOT/'core_periodicity_new/chronology_dcuv/counted_input_age_rules_complete.json'
G=json.loads(gp.read_text())['geometry'];A={(a,x,y):r for a,x,y,r in json.loads(ap.read_text())}
chosen={0:(0,1),1:(0,1),4:(1,2),5:(1,2),6:(0,3),7:(0,3),8:(0,3),9:(0,3)}
rows=[]
for a,p in chosen.items():
 g=G[a];dist=max(max(abs(x-p[0]),abs(y-p[1]))for x,y in g['outputs']);age=A[a,*p];c=g['name'].count('C');ni=len(g['inputs']);ln=len(g['word'])
 assert list(p)in g['inputs']and age>=dist and age<=4 and ln<=10*ni+15*c
 for h in range(4):
  def rot(p):
   x,y=p
   return [(x,y),(y,-x),(-x,-y),(-y,x)][h]
  u,v=rot(p)
  assert max(max(abs(x-u),abs(y-v))for x,y in map(rot,g['outputs']))==dist
 rows.append(dict(packet=a,name=g['name'],chosen_input=p,minimum_age=age,max_Linf_output_distance=dist,inputs=ni,outputs=len(g['outputs']),C_count=c,raw_length=ln))
for k in range(10001):
 # The direct sum is updated to avoid quadratic checker work.
 if k==0:s=0
 s+=(2*k+9)**2
 closed=Fraction(k+1,3)*(4*k*k+56*k+243)
 assert closed==s
out=dict(status='AUTHOR_ARITHMETIC_PASS_NOT_INDEPENDENT',scope='Complete recurrent-eight factors only; auxiliary genealogy plus distinct physical cells; no exclusion.',inputs={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()for p in [gp,ap]},rows=rows,checked_polynomial_k=10001,radius='k+4',residual_mass_bound='(m-5)*(2*k+9)^2',raw_duration_bound='(10/3)*(m-5)*(k+1)*(4*k^2+56*k+243)+15*k')
(ROOT/'word_stabilization/dcuv_c_age_spatial_cubic_bound.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
