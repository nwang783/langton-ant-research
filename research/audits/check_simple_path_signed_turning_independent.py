from pathlib import Path
import json,hashlib,math
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'simple_path_turning_2026-10-23'
def trace(ds):
 ps=[0j]
 for d in ds:ps.append(ps[-1]+d)
 return ps

def turn(ds):
 s=0
 for a,b in zip(ds,ds[1:]):
  z=b/a;assert z!=-1;s+=1 if z==1j else -1 if z==-1j else 0
 return s

def polar(ps):
 q=(ps[0]+ps[1])/2;r=(ps[-2]+ps[-1])/2;vs=[p-q for p in ps[1:-1]]+[r-q];total=0
 for a,b in zip(vs,vs[1:]):total+=math.atan2((b/a).imag,(b/a).real)
 return total
controls=[]
for q in(1,2,3,4,7,10,20,40,80):
 ds=[]
 for j in range(q):ds.extend([1j**j]*((j//2)+1))
 ps=trace(ds);n=len(ds);assert len(set(ps))==len(ps);assert n==(q+1)**2//4 and turn(ds)==q-1
 if n>=2:
  A=polar(ps);Ar=polar(ps[::-1]);assert abs(A-Ar-turn(ds)*math.pi/2)<1e-8;assert abs(turn(ds))<8*math.sqrt(n-1)+2;assert abs(A)<2*math.pi*math.sqrt(n-1)+math.pi/2
 controls.append({'runs':q,'edges':n,'signed_left_turn':turn(ds)})
for n in(2,3,10,100,1000):
 ds=[1 if i%2==0 else 1j for i in range(n)];ps=trace(ds);assert len(set(ps))==n+1 and abs(turn(ds))<=1;assert abs(polar(ps)-polar(ps[::-1])-turn(ds)*math.pi/2)<1e-8
crossings=[]
for m in(1,2,5,20):
 ds=[]
 for i in range(m):
  ds += [1,-1j,-1,1j]
  if i<m-1:ds += [1j,1,1,1]
 ps=trace(ds);edges=[frozenset((a,b))for a,b in zip(ps,ps[1:])];assert len(set(edges))==len(edges)and len(ds)==8*m-4 and -turn(ds)==4*m-1;crossings.append((m,len(ds),-turn(ds)))
# Exact integer lower bound underlying every endpoint ray charge.
from itertools import permutations,combinations
for k in range(1,7):
 for hs in combinations(range(1,k+4),k):
  assert 2*sum(hs)-max(hs)>=k*k
note=D/'PROOF.md';sha=hashlib.sha256(note.read_bytes()).hexdigest();assert sha=='8647be7a9158e11985f60a7643c64411d0cd396e73449ed02032c084f7e7303f'
out={'status':'PASS universal square-root signed-turn bound for vertex-simple square-lattice paths','proof_sha256':sha,'spiral_controls':controls,'crossing_edge_simple_countercontrols':crossings,'analytic':['For n>=2, deleting half of each endpoint edge leaves length n-1 and every original internal turn. Quarter-circle smoothing inside disjoint radius<1/4 vertex neighborhoods preserves embeddedness, is regular C1, keeps the same signed tangent lift and shortens length. Unit square-lattice vertex simplicity excludes all nonincident edge intersections.','On the closed secant triangle s<=t, the normalized nonzero secant extends continuously to the tangent on the diagonal. Regular C1 gives continuity uniformly there. Contractibility supplies a single real lift, hence tangent increment is EXACTLY A-A_reverse, not merely modulo2pi.','An endpoint is an original edge midpoint. After lattice rotation its perpendicular ray has x=1/2 and misses all vertex rounding neighborhoods and all vertical edges. Its intersections with the smoothed arc remain distinct horizontal-edge midpoints at nonzero integer heights, including any terminal midpoint intersection.','For nonnegative endpoint increment A, first hits of pi/2+2pi*j have distinct positive heights h_i. Between successive first hits, continuity forces a downward-ray hit at an integer height<=-1. Therefore length>=2sum(h_i)-h_k+2(k-1)>=k^2+2(k-1). The unordered-height inequality uses coefficient2 on all but the possibly largest final height and is valid without monotonic radial ordering. Reflection handles negative A.','Thus |A|<2pi sqrt(length)+pi/2, and likewise at the reversed endpoint. Their exact difference yields |R-L|<8sqrt(n-1)+2. n0/1 have zero internal turn. Square spirals give matching Theta(sqrt(n)) order; constant8 is not optimality claim.','The optional edge-simple noncrossing-contact extension requires every interior degree-four visit to use disjoint adjacent-edge pairings. Local disjoint smoothing preserves the itinerary and all signed turns; endpoint truncation removes endpoint-only contacts. Transverse or repeated-edge walks are not included.'],'scope':'Pure embedded square-lattice geometry, no ant capture or global recurrence application assumed. Fixed construction controls corroborate, not establish the universal proof.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
