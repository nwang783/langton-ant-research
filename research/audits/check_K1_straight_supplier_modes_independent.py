"""Complete local port inventories and rotated strict-right helper rows.
Necessary histories only; no exterior physical realization is asserted.
"""
from itertools import product
from pathlib import Path
import hashlib,json
SELF=Path(__file__).resolve();R=SELF.parents[1];P=R/'K1_pipeline_detours_2026-10-23/K1_strict_straight_predecessor_supplier_table.md'
# N,E,S,W=0,1,2,3; outputs are actual clockwise R/counterclockwise L turns.
def outs(h):return tuple((x+(1 if i%2==0 else-1))%4 for i,x in enumerate(h))
# Reconstruct the previous RIGHT's second helper Y, rotated CCW into r.
rightY={2:(0,2,0),4:(0,0,0,2),5:(0,2,0,0)}
rrows={k:tuple((x-1)%4 for x in v)for k,v in rightY.items()}
assert rrows=={2:(3,1,3),4:(3,3,3,1),5:(3,1,3,3)}
# CCW(x,y)+(2,-1) maps former exit B=(1,1) to A=(1,0), Y=(0,1) to r=(1,-1).
rotate=lambda p:(2-p[1],p[0]-1)
assert rotate((1,1))==(1,0)and rotate((0,1))==(1,-1)
# All complete cap4 white q histories with unique S arrival, vertical inputs,
# the prescribed E-output count, and opposite/same R headings.
def qrows(same,Ecount):
 found=[]
 for n in range(1,5):
  for h in product((0,2),repeat=n):
   if h.count(2)!=1 or outs(h).count(1)!=Ecount:continue
   rs=h[::2]
   if len(rs)!=2:continue
   if same and rs!=(0,0):continue
   if not same and set(rs)!={0,2}:continue
   found.append(h)
 return found
flat=qrows(False,1);high=qrows(True,3)
assert set(flat)=={(2,0,0),(2,0,0,0),(0,0,2),(0,0,2,0)}
assert set(high)=={(0,2,0),(0,2,0,0),(0,0,0,2)}
# Both current-L1 candidates (with or without final L3) are rejected by the
# same late second-E output versus earlier A.R0 inequality.
# r's N departures feed A ranks0,1,3. q's E departures feed r's E-input ranks.
rs=dict(LEFT=(1,1,3,1),STRAIGHT=(3,3,3,1),RIGHT2=rrows[2],RIGHT4=rrows[4],RIGHT5=rrows[5]);table=[]
for k,r in rs.items():
 nouts=[i for i,x in enumerate(outs(r))if x==0];ein=[i for i,x in enumerate(r)if x==1]
 assert len(nouts)==3
 if k=='LEFT':assert nouts==[1,2,3]and ein==[0,1,3];selected=(0,0,0,2);rank=3
 elif k in('STRAIGHT','RIGHT4'):assert nouts==[0,2,3]and ein==[3];selected=[x for x in flat if x[0]==2];rank=0
 else:assert nouts==[0,1,2]and ein==[1];selected=[x for x in flat if x[2]==2];rank=2
 table.append(dict(previous=k,r=r,north_output_ranks=nouts,east_input_ranks=ein,q=selected,current_S_rank=rank))
out=dict(status='PASS independent rotated local inventories and exact supplier ordinal table',note_sha256=hashlib.sha256(P.read_bytes()).hexdigest(),flat_q_universe=flat,height_two_q_universe=high,rows=table,clock_identities=['current alpha=T2(A)+2','R0-current: T2(q)=T3(A)-2','R2-current: T0(q)=T1(A)-2; T2(q)-T0(q)=T2(A)-T1(A)+4','L3-current: T2(q)=T0(A)-2; cleanup times alpha-1 through alpha+3'],scope='Complete-white cap4, leftmost branch-free K1 strict-straight local context. Table is necessary, not a realized exterior itinerary or a fuel bound.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
