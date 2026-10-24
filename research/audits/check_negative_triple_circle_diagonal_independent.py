from pathlib import Path
from itertools import product
import hashlib,json,math,random
S=Path(__file__).resolve();R=S.parents[1];D=R/'K1_pipeline_detours_2026-10-23';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();note=D/'homogeneous_negative_triple_circles_force_diagonal_drift.md';assert sha(note)=='2bcd69edc9e2c98270c468be3b66706e646e4edd842cab01c78aec5a2cf66182'
H='NESW';V=(1j,1,-1j,-1);rows=[]
def side(z,u,v):
 # LEFT is the CCW angular component from outgoing ray v to incoming ray -u.
 start=math.atan2(v.imag,v.real);angle=(math.atan2(z.imag,z.real)-start)%(2*math.pi);width=(math.atan2((-u).imag,(-u).real)-start)%(2*math.pi)
 assert angle>1e-8 and abs(angle-width)>1e-8
 return 'LEFT'if angle<width else'RIGHT'
for axis in ((0,2),(1,3)):
 for m in range(1,5):
  for hh in product(axis,repeat=m):
   oo=[(h+(1 if t%2==0 else-1))%4 for t,h in enumerate(hh)]
   inc=[h for h in axis if hh.count(h)==3];out=[h for h in range(4)if oo.count(h)==3]
   if len(inc)!=1 or len(out)!=1:continue
   hi,ho=inc[0],out[0];ir=[t for t,h in enumerate(hh)if h==hi];orr=[t for t,h in enumerate(oo)if h==ho]
   if(ir[1],orr[1])!=(2,1):continue
   assert m==4;u,v=V[hi],V[ho];turn='RIGHT'if(ho-hi)%4==1 else'LEFT';s='LEFT'if turn=='RIGHT'else'RIGHT';ports=[]
   for t in range(4):
    row=[]
    for incoming,ranks,dirs in ((True,ir,hh),(False,orr,oo)):
     travel=V[dirs[t]];q=-travel if incoming else travel
     if t in ranks:
      k=ranks.index(t)
      if k==1:row.append('MIDDLE');continue
      q+=(-1 if k==0 else 1)*1j*travel/8
     row.append(side(q,u,v))
    ports.append(row)
   assert ports==[['RIGHT','RIGHT'],[s,'MIDDLE'],['MIDDLE',s],['LEFT','LEFT']]
   rows.append(dict(headings=''.join(H[z]for z in hh),gamma_incoming=H[hi],gamma_outgoing=H[ho],incoming_ranks=ir,outgoing_ranks=orr,turn=turn,off_circle_side=s,actual_rank_in_out_sides=ports))
assert len(rows)==8
ref=json.loads((D/'negative_triple_circle_crossing_inventory.json').read_text());assert {r['headings']for r in rows}=={r['headings']for r in ref['all_rotated_rows']}
for q in rows:
 r=next(z for z in ref['all_rotated_rows']if z['headings']==q['headings']);assert all(q[k]==r[k]for k in ('gamma_incoming','gamma_outgoing','incoming_ranks','outgoing_ranks','turn','off_circle_side'))
# Arbitrary positive-gap algebra controls, NOT ant front realizations.
rng=random.Random(2701);clocktests=[]
for ell in (2,4,6,8,17):
 for rep in range(10):
  delta=[4+rng.randrange(30)for _ in range(ell)];P=sum(delta)-ell;tt=[0]
  for i in range(1,ell):tt.append(tt[-1]+1-delta[i])
  def tau(i):q,r=divmod(i,ell);return tt[r]-q*P
  def eta(i):return tau(i)+delta[i%ell]
  for i in range(ell):
   assert tau(i)<eta(i+1)<tau(i-1)<eta(i)
   assert eta(i+1)==tau(i)+1 and eta(i)==tau(i-1)+1
   ev=[(tau(j),'L1',j)for j in range(i-2*ell,i+2*ell+1)]+[(eta(j),'R2',j)for j in range(i-2*ell,i+2*ell+1)]
   assert not [z for z in ev if eta(i+1)<z[0]<tau(i-1)]
  clocktests.append(dict(length=ell,period=P,gaps=delta))
# Side period two has only constant or alternating solutions. Constants close
# an elementary square; alternating turns fix two compass directions.
geom=[]
for ell in range(2,18,2):
 for start in range(4):
  for firstturn in(-1,1):
   dirs=[start];p=0j
   for i in range(ell):
    p+=V[dirs[-1]];dirs.append((dirs[-1]+firstturn*(-1)**i)%4)
   assert abs(p.real)==abs(p.imag)==ell//2 and dirs[-1]==start
   geom.append((ell,start,firstturn,[int(p.real),int(p.imag)]))
outp={'status':'PASS homogeneous negative G3 circle forces alternating turns and full diagonal drift','author_note':sha(note),'local_profiles':rows,'abstract_clock_controls_not_fronts':clocktests,'alternating_geometry_controls':geom,'analytic_review':[
'Fresh enumeration of all WHITE histories of lengths1..4 in both compass axes gives exactly eight negative internal triple-use profiles, necessarily four-read. Sides were independently reconstructed from actual perturbed port coordinates, not copied labels: first triple tracks RIGHT, third LEFT, middle on gamma. R0 is RIGHT→RIGHT; L3 LEFT→LEFT; L1 comes from side s to middle and R2 leaves middle to the same s. The side s is opposite geometric turn.',
'Ordinal first/second/third matching across every actual physical triple edge gives globally consistent tracks. Small disjoint vertex disks and edge strips realize those perturbations. Unused physical edges have no crossing of gamma away from vertices and attach to their actual side. An excursion involving only R0/L3 contacts can therefore be homotoped into one component of the complement without crossing the middle cut, even if it uses boundary-tangent first/third tracks or unused chords between gamma vertices.',
'Negative middle routing is eta(i+1)=tau(i)+1 and Delta(i)=eta(i)-tau(i)>=4. Hence tau(i-1)-tau(i)=Delta(i)-1>=3. Summing one quotient circuit gives winding*kP=ell-sumDelta<0; embedded essential simplicity forces winding-1. A contractible cycle is already ruled out by the strictly negative clock sum. Full-winding-1 means this one lift contains all full-drift translates, with no extra gamma contacts omitted.',
'The bi-infinite time order is exactly L1(i),R2(i+1),L1(i-1),R2(i). No other gamma L1 or R2 lies between R2(i+1) and L1(i-1), since all R2 events are one update after their predecessor-index L1 and consecutive L1 gaps are>=3. Thus this real off-circle excursion forces s(i+1)=s(i-1). Other circles or off-gamma cells do not alter separation by this fixed gamma.',
'Period-two turn sequence is constant or alternating. A constant quarter-turn repeats the same four-edge physical square, impossible for this embedded essential lift. Therefore turns strictly alternate, ell is even, and exactly two perpendicular travel directions persist. Winding-1 full displacement is -d, yielding |dx|=|dy|=ell/2, with no primitive-drift replacement.',
'No K1, maximum level, root-free collar or zero-output premise is needed for the homogeneous-negative theorem. The root-free shallow valley corollary uses the separately signed axis rail, so simultaneous homogeneous-negative circles are impossible there. Mixed-sign circles remain open; the top-plateau alternative odd corner or lower neighbor is not an injection or global exclusion.'
]}
S.with_suffix('.json').write_text(json.dumps(outp,indent=2)+'\n');print(outp['status'],len(rows),len(clocktests))
