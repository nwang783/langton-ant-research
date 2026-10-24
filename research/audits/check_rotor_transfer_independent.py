from pathlib import Path
from collections import Counter,defaultdict
from itertools import product
from fractions import Fraction
import json,hashlib
S=Path(__file__).resolve();R=S.parents[1];D=R/'global_attraction_bridge_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'ROTOR_EXCURSION_TRANSFER_MANIFEST.json';assert sha(MF)=='1e47a635b51cf90a9458105c1c685b5d81713a2971ec87a9f6489da70d7874b6';mf=json.loads(MF.read_text())
for f,h in mf['files'].items():assert sha(D/f)==h
J=json.loads((D/'ROTOR_EXCURSION_TRANSFER_CHECKED.json').read_text())
for f,h in J['dependencies'].items():assert sha(D/f)==h
lib=S.with_name('check_phase13_double_scatter_independent.py');ns={'__file__':str(lib)};exec(lib.read_text().split('# Canonical source')[0],ns);future,phases=[ns[k]for k in('future','phases')]
V=(1j,1,-1j,-1);xy=lambda p:[int(p.real),int(p.imag)];p=0j;h=1;B={};events=[];snap={};snapref={z['cut']:z for z in J['complete_snapshots']}
for t in range(10082):
 if t in snapref:
  z=snapref[t];assert z['pose']==[xy(p),h]and z['black']==[dict(cell=xy(q),lifetime=B[q])for q in sorted(B,key=lambda q:(q.real,q.imag))];snap[t]=(dict(B),p,h)
 if t==10081:break
 prior=B.get(p);c='L'if p in B else'R';r=1 if c=='R'else-1;ho=(h+r)%4;new=p+V[ho];eps=1 if int(p.real+p.imag)%2 else-1;mu=eps*r;iv=V[h];mv=complex(mu*iv.imag,mu*iv.real)
 assert mv==V[ho]and h%2==1-int(p.real+p.imag)%2
 e=dict(tick=t,cell=xy(p),incoming=h,turn=c,outgoing=ho,next=xy(new),old_lifetime=prior,mirror_sign=mu);events.append(e)
 if c=='L':del B[p]
 else:B[p]=t
 p,h=new,ho
assert ''.join(z['turn']for z in events)==J['full_word']and events[:53]==J['first_53_events']and len(events)==J['fine_reads']==10081
bb,pp,hh=snap[9977];w,d,dead,tests=future(bb,pp,hh);assert w==J['tail_word']==''.join(z['turn']for z in events[9977:])and w in phases and d==-2+2j and len(bb)==715
assert xy(d)==J['tail_drift']
def interval(s,t):
 es=events[s:t];ct=Counter(tuple(z['cell'])for z in es)
 return dict(start=s,end=t,reads=t-s,word=''.join(z['turn']for z in es),read_counts=[dict(cell=list(q),count=n)for q,n in sorted(ct.items())],read_set=list(map(list,sorted(ct))),max_reads=max(ct.values()))
returns=[z['tick']for z in events[:53]if z['cell']==[0,0]];assert returns==J['return_cuts']==[0,4,8,16,52]
for s,t,au in[(0,8,J['return_packets'][0]),(8,52,J['return_packets'][1]),(0,5,J['literal_printed_threshold_packets'][0]),(5,17,J['literal_printed_threshold_packets'][1])]:assert interval(s,t)==au
missing=sorted(set(tuple(z['cell'])for z in events[:8])-set(tuple(z['cell'])for z in events[8:52]));assert list(map(list,missing))==J['lost_previous_packet_cells']==[[0,-1],[1,0],[1,1]]
seen={};repeat=None
for z in events[8:]:
 e=(tuple(z['cell']),tuple(z['next']))
 if e in seen:repeat=(seen[e],z['tick'],e);break
 seen[e]=z['tick']
assert repeat==(9,13,((0,1),(-1,1)))and next(z['tick']for z in events[9:]if z['cell']==[0,0])==16
assert sorted(map(xy,snap[8][0]))==[[-1,-1],[-1,0],[0,-1],[0,1],[1,0],[1,1]]and snap[8][1:]==(0j,3)
# Universal local algebra, independent of any global routing/seed.
nalg=0
for ax,r0,n in product((0,1),(-1,1),range(1,9)):
 for ins in product((-1,1),repeat=n):
  outs=[]
  for j,sgn in enumerate(ins):
   hin=ax if sgn==1 else(ax+2)%4;ho=(hin+r0*(-1)**j)%4;val=1 if V[ho]==V[(ax+1)%4]else-1;assert V[ho]==val*V[(ax+1)%4]and val==r0*(-1)**j*sgn;outs.append(val)
  assert sum(outs)==r0*sum((-1)**j*v for j,v in enumerate(ins));Jp=sum(ins[j]!=ins[j+1]for j in range(0,n-1,2));assert abs(sum(outs))<=2*Jp+n%2
  assert all((outs[j]==outs[j+1])==(ins[j]!=ins[j+1])for j in range(n-1));nalg+=1
assert nalg==J['local_algebra_cases']==2040
local=[]
for seq in((0,2),(2,0)):
 outs=[(h+(1 if j%2==0 else-1))%4 for j,h in enumerate(seq)];local.append(dict(incoming=list(seq),outgoing=outs,final_rotator=1))
assert local==J['nonabelian_port_orders']and local[0]['outgoing']==[1,1]and local[1]['outgoing']==[3,3]
# Exact finite-interval odometer identity, including the signed defect term.
flowtests=[]
for s,t in[(0,52),(8,52),(9977,10081)]:
 ct=Counter(complex(*z['cell'])for z in events[s:t]);imb=Counter()
 for z in events[s:t]:
  q=complex(*z['cell']);f=1j if int(q.real+q.imag)%2==0 else 1;imb[q]+=1 if complex(*z['next'])-q==f else-1
 for fn in[lambda q:int(q.real),lambda q:int(q.imag),lambda q:int(q.real*q.imag),lambda q:int(q.real*q.real+3*q.imag*q.imag)]:
  rhs=Fraction(0)
  for q,u in ct.items():
   f=1j if int(q.real+q.imag)%2==0 else 1;rhs+=u*(Fraction(fn(q+f)+fn(q-f),2)-fn(q))+Fraction(imb[q]*(fn(q+f)-fn(q-f)),2)
  end=complex(*events[t-1]['next']);beg=complex(*events[s]['cell']);assert rhs==fn(end)-fn(beg);flowtests.append((s,t,str(rhs)))
a,b=events[9980],events[9984];assert a['cell']==b['cell']==[8,16]and(a['incoming'],b['incoming'],a['turn'],b['turn'],a['outgoing'],b['outgoing'])==(3,1,'L','R',2,2);assert all(z['cell']!=[8,16]for z in events[9981:9984])
# All108-window starts are covered by one residue calculation plus the certified infinite translation.
window=[]
for r in range(104):
 start=9980+r;k=0 if r==0 else 1;u=9980+104*k;v=u+4;assert start<=u<v<start+108;window.append((r,u-start,v-start))
literature=[
 dict(source='https://arxiv.org/pdf/1408.5533',review='Primary PDF inspected independently, pages1/4/5. Simple rotor uses a prescribed cyclic order of outgoing edges. Lemmas2.1/2.4 require that rule and Eulerian balance. The printed visit-count threshold and prose return-cut convention differ by their starting-visit convention; both ant packets are retained, so no conclusion rests on resolving that indexing. General periodic Eulerian range lower bound is external, not an ant transfer or a new proof.'),
 dict(source='https://archive.intlpress.com/site/pub/files/_fulltext/journals/joc/2012/0003/0002/JOC-2012-0003-0002-a003.pdf',review='Primary PDF inspected independently, Theorem1, Corollary6, Proposition7, Lemma8. Its global setting is locally finite connected simple UNDIRECTED graphs with fixed rotor mechanism. Theorem1/Corollary6 concern start/finite-rotor perturbations and use abelian routing; Lemma8 first-repeat conclusion uses cyclic exits. They are cited only as distinct-rule comparison, not imported to the ant directed sector.'),
 dict(source='https://www-fourier.univ-grenoble-alpes.fr/~rechtmaa/Documents/det-walk.pdf',review='Primary Theorem1 inspected. For horizontal origin heading, gauge sign is(-1)^(|x|+|y|+1); uniform flipping rotators become checkerboard flipping mirrors. Finite perturbations are relative to the transformed checkerboard, not uniform mirrors. All10081 actual gauge steps independently verified.'),
 dict(source='https://arxiv.org/abs/1404.3629',review='Primary abstract inspected: honeycomb flipping scatterers and a specified initial class, not square finite-seed universality.'),
 dict(source='https://arxiv.org/abs/1507.07133',review='Primary abstract inspected: honeycomb independent random scatterers, periodicity for probabilities strictly between0and1; not this square finite perturbation problem.'),
 dict(source='https://arxiv.org/pdf/2608.23545',review='Primary abstract/model independently inspected. Four-neighbor clockwise rotor mechanism with independent uniform initial arrows; recurrence/range2/3 claim is external and distinct, with no proof audit or applicability to ant.')]
report=dict(status='PASS exact direct simple-rotor transfer obstruction, including no108-read rotor-simple window in certified blank tail',manifest=sha(MF),dependencies=J['dependencies'],complete_read_count=len(events),full_field_cuts=[(t,len(bb),xy(q),hh)for t,(bb,q,hh)in sorted(snap.items())],full_tail=dict(word=w,drift=xy(d),parity_tests=tests,canonical=True),return_cuts=returns,lost_previous_packet_cells=missing,first_repeat=repeat,algebra_cases=nalg,nonabelian_orders=local,odometer_control_equalities=flowtests,all104_window_residues=window,primary_source_scope_checks=literature,analytic_review=[
'The fixed checkerboard sector is genuinely a connected periodic Eulerian directed unit graph: even sites emit vertically and receive horizontally, odd sites vice versa. That graph premise for the directed Eulerian range paper is satisfied. The failure is the simple cyclic-exit mechanism, not degree or graph connectivity.',
'For contiguous same-cell visits, turn signs alternate but incoming signs need not. z_j=r0(-1)^j a_j proves repeated successive exits exactly when incoming signs reverse, with signed imbalance bounded by2J+odd remainder. This algebra and the two-input nonabelian port test are local, not a constructed exterior route or an impossibility of every possible encoding.',
'Whole blank field atcut8 is retained. The first repeated directed edge of the reset segment occurs9/13 at(0,1), before origin return16, falsifying the proposed ant analogue. Return packets0..8/8..52 lose three prior cells and exceed degree2; literal printed thresholds0..5/5..17 also lose cells. External theorem indexing is not silently adjusted.',
'Fresh10081-read simulation, full birth IDs, every stored field, proper canonical phase membership and exact infinite future ray parity reconstruct. Stable pair9980/9984 has opposite arrivals and equalS exits with no intermediate same-cell read. Every104translate repeats it forever on the complete physical future.',
'For any integer starta>=9980, first pair-start>=a lies at mosta+103 and pair-end at mosta+107, both inside[a,a+108). Thus no108-read window on this successful tail follows the simple physical degree2 rotor rule. In particular longF*(H) windows forH>=2 cannot be made rotor-simple by waiting, and raw defects cannot have an original-seed-only finite budget even for seed0.',
'The odometer/test-function identity retains the signed ordered-arrival term, with no bound|d|<=1 asserted for the ant. Mirror conjugacy preserves the correct checkerboard background but does not remove arrival dependence. No record-window occurrence, universal capture, finite-perturbation invariance or classification is obtained.'
])
S.with_suffix('.json').write_text(json.dumps(report,indent=2)+'\n');print(report['status']);print(sha(S.with_suffix('.json')));print(tests,nalg,missing)
