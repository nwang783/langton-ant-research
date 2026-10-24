from pathlib import Path
from itertools import product,permutations
import hashlib,json,math
S=Path(__file__).resolve();R=S.parents[1];D=R/'K1_pipeline_detours_2026-10-23';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();note=D/'triple_circle_passage_permutation_and_side_currents.md';assert sha(note)=='6e776346bf19ae5b7d13f367e31d3e0773bb01d8eb6e70bde842a0c8d9191f53'
H='NESW';V=(1j,1,-1j,-1);local=[]
def side(z,u,v):
 start=math.atan2(v.imag,v.real);a=(math.atan2(z.imag,z.real)-start)%(2*math.pi);width=(math.atan2((-u).imag,(-u).real)-start)%(2*math.pi);assert a>1e-8 and abs(a-width)>1e-8;return 'LEFT'if a<width else'RIGHT'
for axis in((0,2),(1,3)):
 for hh in product(axis,repeat=4):
  oo=[(h+(1 if i%2==0 else-1))%4 for i,h in enumerate(hh)];ip=[h for h in axis if hh.count(h)==3];op=[h for h in range(4)if oo.count(h)==3]
  if len(ip)!=1 or len(op)!=1:continue
  hi,ho=ip[0],op[0];ir=[i for i,h in enumerate(hh)if h==hi];orr=[i for i,h in enumerate(oo)if h==ho];positive=(ir[1],orr[1])==(1,2);assert positive or(ir[1],orr[1])==(2,1);u,v=V[hi],V[ho];turn='RIGHT'if(ho-hi)%4==1 else'LEFT';ss='LEFT'if turn=='RIGHT'else'RIGHT';ports=[]
  for i in range(4):
   rr=[]
   for inc,ranks,dirs in((True,ir,hh),(False,orr,oo)):
    travel=V[dirs[i]];p=-travel if inc else travel
    if i in ranks:
     k=ranks.index(i)
     if k==1:rr.append('MIDDLE');continue
     p+=(-1 if k==0 else 1)*1j*travel/8
    rr.append(side(p,u,v))
   ports.append(rr)
  assert ports==([['RIGHT','RIGHT'],['MIDDLE',ss],[ss,'MIDDLE'],['LEFT','LEFT']]if positive else[['RIGHT','RIGHT'],[ss,'MIDDLE'],['MIDDLE',ss],['LEFT','LEFT']])
  local.append(dict(headings=''.join(H[z]for z in hh),sign='positive'if positive else'negative',turn=turn,sides=ports))
assert len(local)==16
# Solve corner stream heights directly from physical port flows, independently
# of the author's R/L count height formula. Normalize max C to zero.
quad={'NE':1+1j,'NW':-1+1j,'SW':-1-1j,'SE':1-1j};pairs={'W':('SW','NW'),'E':('NE','SE'),'N':('NE','NW'),'S':('SW','SE')};streams=[];ref=json.loads((D/'triple_circle_side_stream_inventory.json').read_text())
for row in local:
 h=row['headings']
 if set(h)-set('EW'):continue
 oo=[H[(H.index(ch)+(1 if i%2==0 else-1))%4]for i,ch in enumerate(h)];flow={'W':h.count('E'),'E':h.count('W'),'N':oo.count('N'),'S':oo.count('S')};hin='E'if flow['W']==3 else'W';hout='N'if flow['N']==3 else'S';u,v=V[H.index(hin)],V[H.index(hout)]
 hs={'SW':0,'NW':-flow['W'],'SE':-flow['S'],'NE':flow['E']-flow['S']};top=max(hs['NE'],hs['SW']);hs={q:z-top for q,z in hs.items()};sides={q:side(z,u,v)for q,z in quad.items()};left={q:(hs[q]+2 if sides[q]=='LEFT'else 0)for q in hs};right={q:(hs[q]+1 if sides[q]=='RIGHT'else 0)for q in hs};lf={p:left[c]-left[l]for p,(c,l)in pairs.items()};rf={p:right[c]-right[l]for p,(c,l)in pairs.items()};mf={p:int(flow[p]==3)for p in flow}
 assert all(lf[p]>=0 and rf[p]>=0 and lf[p]+rf[p]+mf[p]==flow[p]for p in flow)
 assert lf['W']+lf['E']==lf['N']+lf['S']and rf['W']+rf['E']==rf['N']+rf['S']
 rr=next(z for z in ref['rows']if z['headings']==h);assert hs==rr['heights']and left==rr['h_LEFT']and right==rr['h_RIGHT']and lf==rr['LEFT_flows']and rf==rr['RIGHT_flows']
 streams.append(dict(headings=h,heights=hs,LEFT=lf,RIGHT=rf,MIDDLE=mf))
assert len(streams)==8
def cycles(p):
 seen=set();out=[]
 for i in range(len(p)):
  if i in seen:continue
  cyc=[];j=i
  while j not in seen:seen.add(j);cyc.append(j);j=p[j]
  assert j==i;out.append(cyc)
 return out
pc=[]
for ell in range(2,8):
 count=0
 for F in permutations(range(ell)):
  Hnext=[F[(i+1)%ell]for i in range(ell)]
  if len(cycles(Hnext))!=1:continue
  CF=len(cycles(F));assert(ell-CF)%2==0
  # Actual abstract orbit: D_i -> A_(i+1), A_i -> D_F(i).
  sig=[0]*(2*ell)
  for i in range(ell):sig[2*i]=2*((i+1)%ell)+1;sig[2*i+1]=2*F[i]
  assert len(cycles(sig))==1
  repair=sig[:]
  for i in range(ell):repair[2*i],repair[2*i+1]=repair[2*i+1],repair[2*i]
  assert len(cycles(repair))==1+CF and ell-len(cycles(repair))+1==ell-CF
  # Give H its actual phase order, so one wrap is a full actual time period.
  order=cycles(Hnext)[0];time={v:i for i,v in enumerate(order)}
  for w in(-1,1):
   Hl=[Hnext[i]+w*ell*(time[Hnext[i]]<=time[i])for i in range(ell)]
   Fl=[Hl[(i-1)%ell]-(ell if i==0 else 0)for i in range(ell)]
   assert sum(Hl[i]-i for i in range(ell))==w*ell
   assert sum(Fl[i]-i for i in range(ell))==(w-1)*ell
  count+=1
 pc.append(dict(length=ell,one_actual_cycle_abstract_models=count))
for ell in(2,4,6,8,20):assert len(cycles([(i-2)%ell for i in range(ell)]))==2
for cl in range(-3,4):
 cr=cl+1
 for c in range(-5,6):
  pos=(c-2-cl,cr-c+1);neg=(cr-c+2,c-1-cl);assert sum(pos)==0 and sum(neg)==2
  assert(pos==(0,0))==(c==cr+1);assert(neg==(1,1))==(c==cr+1)
out={'status':'PASS all-sign G3 passage permutation, partial excess and physical side-current split','author_note':sha(note),'geometric_side_profiles':local,'eight_normalized_stream_profiles':streams,'abstract_permutation_controls_NOT_fronts':pc,'analytic_review':[
'Each middle D departure is immediately followed by the next-index A arrival. Every off-middle interval starts at exactly one A and ends at exactly one D. Thus F and actual next-D map H are equivariant bijections, H(i)=F(i+1); side preservation follows from the freshly reconstructed R0/L3 same-side perturbation at all16 compass profiles. Full embedded winding +/-1 makes all translates belong to one physical lift.',
'All D event classes occur once per actual P interval. H is one quotient ell-cycle and H^ell(i)=i+w*ell, not merely some unspecified multiple. Summing lifted displacements and subtracting the index shift gives sum(F(i)-i)=(w-1)ell. Quotient H and cyclic index shift have equal permutation sign, so F is even. No bound Delta<P is assumed.',
'Repair only the disjoint gamma L1/R2 switches. It redirects D-to-middle and A-to-excursion transitions into exactly one middle gamma circle plus one cycle for each quotient F cycle. A hypothetical additional repaired cycle avoiding all switches would already be a proper cycle of the original single actual event permutation. Hence partial beta=ell-C(F), nonnegative even. Each additional disjoint transposition changes cycle count by +/-1 and edge count by+1, so beta increases by0 or2. This is one reservation, not additive over overlapping circles.',
'Fresh heights solved from actual port counts yield hLEFT=h-(c-2) on LEFT, zero RIGHT, and hRIGHT=h-(c-1) on RIGHT, zero LEFT. Every gamma edge carries one nonnegative use in each side stream and the middle; all other physical multiplicity belongs wholly to its side. The corner balances hold in all eight normalized profiles. These are the actual first/third ordinal streams and their partial-repair F cycles, not just equal total homologies.',
'Using c_right-c_left=1 and the actual orientation of the two unbounded cylinder ends gives w+ side homologies(c-2-c_left,c_right-c+1), w- gives(c_right-c+2,c-1-c_left). Their sum is1-w. F cycle index voltage q*ell gives physical homology w*q; it need not be primitive or embedded.',
'Homogeneous positive forces A_i<D_i<A_(i+1), w+ and F=id. All side cycles close at the same physical vertex and have zero homology, forcing c=c_right+1. Homogeneous negative uses signed diagonal rigidity and F(i)=i-2, ell even; its two side cycles each have index winding-1 and physical winding+1. Thus beta_full>=ell-2 and the same critical c follows. Mixed signs remain unclassified. No beta upper bound, initial fuel, actual ant splice or global capture follows.'
]}
S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],pc)
