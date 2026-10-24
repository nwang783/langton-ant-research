"""Exact outgoing-phase parity check for later favorable corner collisions."""
import json,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
sys.path.insert(0,'/workspace/shared/langton/continuation_2026-10-22/ant_continuation')
from ant_exact import W,plan,multiple
FRESH=[13,14,15,27,28,29,32,38,45,46,47,55,56,57,60,61,62,70,71,72,75,89]
FAVORABLE=[14,28,32,38,46,56,60,62,70,72]

def main():
 source=json.loads((HERE/'ordinary_interfaces.json').read_text());rows=[]
 for row in source['rows']:
  p,h=row['capture_pose_constant'];p=tuple(p);phase=row['tail_phase'];d=tuple(row['outgoing_drift'])
  assert (sum(p)+h)%2==0 # Invariant sigma=+1; adding m(2,-2) does not change it.
  tw=W[phase:]+W[:phase];skip=(104-phase)%104;_,_,p0,h0=plan(tw[:skip],p,h)
  assert (sum(p0)+h0)%2==0
  qs,hs,end,eh=plan(W,p0,h0);assert (end[0]-p0[0],end[1]-p0[1])==d and eh==h0
  expected_heading={(-2,2):0,(2,2):1,(2,-2):2,(-2,-2):3}[d];assert h0==expected_heading
  fresh=[]
  for i,q in enumerate(qs):
   prior=False
   for j,v in enumerate(qs):
    k=multiple((v[0]-q[0],v[1]-q[1]),d)
    if k is not None and (k>0 or k==0 and j<i):prior=True
   if not prior:fresh.append(i)
  assert fresh==FRESH
  # The opposite-sign axial neighbor a has both coordinates odd; the positive
  # opposite corner d has even x and odd y. These follow from q=(odd,even)
  # and opposite b signs at each remote degree-two row/column vertex.
  target_parity={(-2,2):(1,1),(2,2):(0,1),(-2,-2):(1,0),(2,-2):(0,0)}[d]
  target_sum=sum(target_parity)%2
  allowed=[i for i in fresh if sum(qs[i])%2==target_sum]
  assert allowed==FAVORABLE
  rows.append(dict(core_phase=row['phase'],outgoing_drift=d,outgoing_W0_pose=[p0,h0],remote_corner_parity=target_parity,possible_fresh_phases=allowed))
 assert len(rows)==21
 out=dict(status='all outgoing phases preserve the favorable ten corner sector',invariant='(x+y+h) mod2=0 from initial head(0,0),N',reason='every turn and move flips h parity and x+y parity; complete periods have even displacement',rows=rows)
 (HERE/'corner_sectors.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
