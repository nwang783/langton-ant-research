from pathlib import Path
from functools import lru_cache
import sys,json,hashlib
ROOT=Path(__file__).resolve().parents[1];H=ROOT/'computability/flat_exact_validator';sys.path.insert(0,str(H))
import finite_order_adapter as A
D=(1j,1,-1j,-1)
controls=[('half',((-1,0),(0,-1)),2,['RRRRLRLLL','LRRRLRLLL']*4),('quarter',((0,-1),(1,0)),4,['RRRRLRR','LRRRLRR']*4),('oblique_reflection',((1,2),(0,-1)),2,['R','L','RRRRLLRLL','LRRRLLRLL','R','L','RRRRLLRLL','LRRRLLRLL'])]
records=[];total=0
for name,M,period,words in controls:
 P=A.standard_physical();images=[A.word_states(w,s//2)for s,w in enumerate(words)]
 model,report=A.prepare(P,images,M,period,max_powered_reads=100000)
 def apply(z):return complex(M[0][0]*int(z.real)+M[0][1]*int(z.imag),M[1][0]*int(z.real)+M[1][1]*int(z.imag))
 @lru_cache(None)
 def expand(s,r):return (s,)if r==0 else tuple(t for u in images[s]for t in expand(u,r-1))
 checks=0
 for s in range(8):
  assert tuple(model.images[s])==expand(s,report['common_power'])
  for r in range(period+1):
   z=0j;h=D[P[s][0]];read=[]
   for t in expand(s,r):
    ih,turn=P[t];assert h==D[ih];read.append((z,turn==-1));h*=(-1j if turn==1 else 1j);z+=h;checks+=1
   want=D[(P[s][0]+P[s][1])%4]
   for _ in range(r):want=apply(want)
   assert z==want and h==D[(P[s][0]+P[s][1])%4]
 result=A.solve_finite_order(P,images,M,period,max_powered_reads=100000)
 if not result['possible']:
  bits={};odd=set();h=D[P[0][0]];z=0j;conflict=None
  for j,t in enumerate(expand(0,report['common_power'])):
   need=(P[t][1]==-1)^(z in odd)
   if z in bits and bits[z][0]!=need:conflict=(z,bits[z][1],j);break
   bits[z]=(need,j);odd.symmetric_difference_update({z});h*=(-1j if P[t][1]==1 else 1j);z+=h
  assert conflict is not None
  C=result['conflict'];assert complex(*C['cell'])==conflict[0]and C['conflicting_read']==conflict[2]
 else:assert not result['given_seed_validation']['accepted_growing_model']
 total+=checks;records.append(dict(name=name,literal_moves=checks,result=result))
# Decorated actual first-letter two-cycle, not a spatial-axis inference.
P=A.standard_physical()*2;images=[]
for s in range(16):
 w=A.word_states(controls[0][3][s%8],(s%8)//2);w[0]=(s+8)%16;images.append(w)
model,report=A.prepare(P,images,controls[0][1],2);assert report['first_letter_root_cycle']==2 and report['common_power']==2 and model.images[0][0]==0
bad=0
for arguments in [dict(order=True),dict(order=3),dict(order=0)]:
 try:A.prepare(A.standard_physical(),[[s]for s in range(8)],((1,0),(0,1)),**arguments)
 except ValueError:bad+=1
 else:
  assert arguments['order']==3  # Nonminimal orders are intentionally legal.
assert bad==2
res=dict(status='PASS independent recursive expansion, exact complex pose and conflict witnesses',literal_moves=total,controls=records,decorated_first_letter_cycle=report,invalid_controls=bad,subject_sha256=hashlib.sha256((H/'finite_order_adapter.py').read_bytes()).hexdigest(),scope='Selected cofinal root power-limit only, exact physical boundary headings and finite-order supplied matrix. Does not require all intermediate root phases to share one seed.')
Path(__file__).with_suffix('.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps(res,indent=2))
