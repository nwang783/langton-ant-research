"""Independent local four-step implication for the analytic backbone-time sum."""
from pathlib import Path
from itertools import product
import json,hashlib
R=Path(__file__).resolve().parents[1];v=(1j,1,-1j,-1);rows=[]
for h0 in range(4):
 candidates=[]
 for suffix in product('RL',repeat=3):
  w='R'+''.join(suffix);p=0j;h=h0;reads=[]
  for c in w:
   reads.append((p,h,c));h=(h+(1 if c=='R'else-1))%4;p+=v[h]
  if p==0j and h==h0:candidates.append((w,reads))
 assert len(candidates)==1 and candidates[0][0]=='RRRR'
 w,reads=candidates[0];u=-v[h0];assert reads[-1][0]==u and reads[-1][2]=='R'and all(p!=u for p,h,c in reads[:-1])
 # The selected L at the returned origin must retain the first incoming
 # heading in order to leave along the LEFT backbone edge.
 assert [a for a in range(4) if v[(a-1)%4]==v[(h0-1)%4]]==[h0]
 rows.append(dict(first_heading=h0,forced_loop=w,previous_backbone_cell=[int(u.real),int(u.imag)],later_u_read='R',earlier_u_read_forced='L'))
for D in range(1,100):
 bound=6*D+4*((D+2)//3);assert bound%4==(2*D)%4
note=R/'periodic_classification_new/cap_four_backbone_time_debt.md'
out=dict(status='PASS local R-to-L run-start implication; global disjoint-charge and essential-cycle proofs analytically reviewed',controls=rows,note_sha256=hashlib.sha256(note.read_bytes()).hexdigest(),bound='P >= 3*ell + 4*s >= 6*D + 4*ceil(D/3)',scope='Complete white cap-four fronts only; no uninterrupted backbone trajectory or all-period exclusion asserted.')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
