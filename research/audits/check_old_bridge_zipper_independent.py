from pathlib import Path
import json, hashlib
from collections import Counter
SELF=Path(__file__).resolve();ROOT=SELF.parents[1]
exec((SELF.parent/'check_cycle_birth_finite_fuel_independent.py').read_text().split('cells=')[0])
stats=Counter()
def zvertex(p,h):return 2*p+(-1-1j)*(-1j)**h
def nonbridge(B,q,k):return connected(B-{q},k,*ends(q,k))
def control(B0,p0,h0,steps):
 B=set(B0);p=p0;h=h0;m=len(B);k=int(wvertex(p,h).real+wvertex(p,h).imag)%4
 initial=set(B);initial_active=component(B,k,wvertex(p,h))[1];initial_bridges={q for q in initial_active if not nonbridge(B,q,k)}
 wseen={wvertex(p,h)};new=set();Ls=0;Rs=0;D=0;E=0;r=0;C=component(B,k,wvertex(p,h))[1];blockmass=m;blockbirth=False;epochmass=m;epochcount=0;counts=[];masses=[m]
 for t in range(steps):
  if p not in B:
   if isbirth(B,p,k):blockbirth=True
   q=p;oldw=wvertex(p,h);p,h,ch=step(B,p,h);new.add(q);r+=1;Rs+=1
   assert wvertex(p,h)==oldw and r<=4
  else:
   q=p;oldw=wvertex(p,h);nbw=nonbridge(B,q,k);nbz=nonbridge(B,q,2-k);erases=nbw or nbz
   if r>=3:
    assert nbz;stats['three_or_four_R_unit_cycle_erasures']+=1
   exceptional=r>=3 or nbw
   if D==0 and not erases:
    assert q in initial_bridges and q not in new and r<=2
   if erases:D+=1
   p,h,ch=step(B,p,h);Ls+=1;new.discard(q)
   assert {oldw,wvertex(p,h)}==set(ends(q,k)) and len(B)-blockmass==r-1
   if not exceptional:
    actual=component(B,k,wvertex(p,h))[1];expected=component(C-{q},k,wvertex(p,h))[1]
    assert q in C and actual==expected and len(actual)<len(C)
    epochcount+=1;assert epochcount<=epochmass
    stats['exact_ordinary_inheritances']+=1
    if blockbirth:stats['ordinary_blocks_with_w_cycle_birth']+=1
   else:
    assert erases;E+=1;counts.append(epochcount);assert len(B)<=2*epochmass+3
    epochmass=len(B);masses.append(epochmass);epochcount=0;stats['exceptional_blocks']+=1
   if D==0:
    assert wvertex(p,h) not in wseen;wseen.add(wvertex(p,h))
   C=component(B,k,wvertex(p,h))[1];blockmass=len(B);r=0;blockbirth=False
  assert E<=D
  assert all(M<=2**j*(m+3)-3 for j,M in enumerate(masses))
  assert t+1<=3*(sum(counts)+epochcount)+5*E+4
  assert t+1<=3*(m+3)*(2**(E+1)-1)-4*E-5<=6*(m+3)*2**D
  if D==0:
   assert Ls<=m and Rs<=2*Ls+4 and t+1<=3*m+4 and len(B)<=2*m+4
   assert new<=B
   assert abs((p-p0).real)+abs((p-p0).imag)<=2*m+2
   assert len(wseen)==Ls+1
   stats['zipper_prefixes']+=1
  stats['all_prefixes']+=1
 stats['runs']+=1
 # When observed, the first erasure deadline is separately checked from a new replay.
 B=set(B0);p=p0;h=h0
 for t in range(3*m+5):
  if p in B and any(nonbridge(B,p,kk)for kk in(0,2)):
   stats['first_erasure_deadlines']+=1;return t+1
  p,h,ch=step(B,p,h)
 raise AssertionError('missed exact first-erasure deadline')
cells=[complex(x,y)for x,y in[(0,0),(1,0),(0,1),(1,1),(-1,0),(0,-1)]]
for mask in range(64):
 for h in range(4):control({q for i,q in enumerate(cells)if mask>>i&1},0j,h,96)
control(set(),0j,0,1200)
control({complex(x,y)for x in range(-2,3)for y in range(-2,3)}|{100+100j,101+100j,100+101j,101+101j},0j,0,256)
rods=[]
for r in(1,2,3,7,16,31,64):
 wait=control({complex(x,0)for x in range(2*r)},0j,1,4*r+9);assert wait==4*r+5;rods.append({'r':r,'first_erasure':wait})
note=ROOT/'global_cycle_birth_2026-10-23/old_bridge_zipper_and_cycle_erasure.md';sha=hashlib.sha256(note.read_bytes()).hexdigest();assert sha=='bfd61ce9b6fd0a78a5fb14a495f11cc0b488b1c643e34682219ea2b45c670f30'
report={'status':'PASS arbitrary-word old-bridge zipper and global cycle-erasure bound','note_sha256':sha,'counts':dict(stats),'rods':rods,'analytic':['At a block entry the stationary w cursor scans distinct ports for at most four R turns. For r<=3 the subsequent black departing edge is old. If it is still a bridge after the insertions, no new edge can reach its old far component, since all new edges originate at w and such a connection would bypass it. The post-L active edge set therefore equals the far component of the exact block-entry active component minus that edge, even when the R prefix created cycles on the departed side.','For r=3, three freshly inserted edges and the old departing fourth edge form a z unit cycle before L. For r=4 the departing edge is the first new edge of the freshly completed z unit cycle. Both L updates are genuine cycle erasures.','On an erasure-free interval every full block thus has r<=2 and a w-bridge L. Inductively the retained active component is an initial-component piece cut only along initial bridges. Original nonbridge cycles remain whole under these cuts, so each L consumes a distinct initial bridge. The w vertices form a simple path; every added edge remains behind and every R-created lifetime stays black through the interval.','With n<=m L steps, R<=2n+4, giving T<=3m+4 and mass<=2m+4. Each w crossing has L1 length2 and physical head is L1 distance1 from its w cursor at both endpoints, giving head displacement<=2m+2, including the terminal run. Consequently a cycle-erasing L occurs by update3m+5, also for m0.','For an arbitrary interval mark full blocks exceptional if r>=3 or L is a w nonbridge. Each such block ends in an erasure, so E<=D, where D counts physical L updates once even if both graphs lose a cycle. Ordinary blocks may erase a z cycle without being marked, which only reduces E. Exact ordinary inheritance gives n_j<=M_j; mass gain per ordinary block<=1 and exceptional<=3 give M_(j+1)<=2M_j+3 and M_j<=(m+3)2^j-3.','Summing E+1 epochs yields T<=3 sum n_j+5E+4<=3(m+3)(2^(E+1)-1)-4E-5<=6(m+3)2^D. Starting mid-run causes no issue: the departing edge is old at the interval block start whenever r<=3. No original black mass or current cycle-rank bound on total erasures is inferred.'],'scope':'All actual finite-support intervals, whole current graphs with all passive components retained. Recurrence and logarithmic lower bound for cycle erasures, not a defect bound, standard104 capture, positive density, finite-state quotient or monotone rank.'}
SELF.with_suffix('.json').write_text(json.dumps(report,indent=2)+'\n');print(report['status']);print(dict(stats))
