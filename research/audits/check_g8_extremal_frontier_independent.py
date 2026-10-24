from pathlib import Path
from itertools import product
from collections import defaultdict
import hashlib,json
S=Path(__file__).resolve();R=S.parents[1];D=R/'autonomous_controllers_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();note=D/'G8_EXTREMAL_CYCLE_FRONTIER.md';assert sha(note)=='0e3f0ea39edd5c600e7f9950f630b33bef5514d6ad21654110f5f9b1622072ab';ref=json.loads((D/'check_g8_extremal_boundary_interface.json').read_text());assert sha(D/'check_g8_extremal_boundary_interface.json')=='e95c347b40823c706aa40a656fa5d6f822b4f520ac00f196281013301a996156'
V=(1j,1,-1j,-1);dr=2-2j;P=124;xy=lambda q:(int(q.real),int(q.imag))
def key(q):
 x,y=xy(q);rx=x%2;k=(x-rx)//2;return complex(rx,y+2*k),k
DATA=[(0-1j,[3],[0]),(1-2j,[3],[94]),(0j,[2,2,0],[-31,-3,1]),(1-1j,[2,2,0],[-1,91,95]),(1j,[1,1,3,3,3],[-32,-28,-16,-4,28]),(1+0j,[1,1,3,3],[-2,2,14,90])]
H={q:[{'rank':i,'h':h,'out':(h+(1 if i%2==0 else-1))%4,'turn':'R'if i%2==0 else'L','clock':t}for i,(h,t)in enumerate(zip(hs,ts))]for q,hs,ts in DATA}
assert len({e['clock']%P for es in H.values()for e in es})==17
for q,es in H.items():
 assert all((e['clock']-(2*int(q.real)-int(q.real+q.imag)%2+1))%4==0 for e in es)
 assert all(b['clock']-a['clock']>=4 for a,b in zip(es,es[1:]))
 rr=next(z for z in ref['complete_histories_on_six_named_classes']if z['cell']==list(xy(q)));assert rr['events']==es
edges=[];oi=[];oo=[];E={};FG={}
for q,es in H.items():
 for h in range(4):
  src=[e for e in es if e['out']==h]
  if not src:continue
  v,k=key(q+V[h])
  if v not in H:
   oo.extend((xy(q),e['rank'],xy(v),k,e['clock'])for e in src);continue
  dst=[e for e in H[v]if e['h']==h];assert len(src)==len(dst)
  for a,b in zip(src,dst):
   assert a['clock']+1==b['clock']+k*P;edges.append((xy(q),a['rank'],xy(v),b['rank'],k))
   if a['rank']==0:
    FG[q]=(v,k)
    if b['rank']==len(H[v])-1:E[q]=(v,k)
 for e in es:
  v,k=key(q-V[e['h']])
  if v not in H:oi.append((xy(q),e['rank'],xy(v),k,e['clock']))
assert len(edges)==12 and len(oi)==len(oo)==5
assert set(edges)=={(tuple(z['source']),z['source_rank'],tuple(z['target']),z['target_rank'],z['voltage'])for z in ref['internal_matched_edges']}
assert set(oi)=={(tuple(z['cell']),z['rank'],tuple(z['source_class']),z['voltage'],z['clock'])for z in ref['open_incoming_ports']}
assert set(oo)=={(tuple(z['cell']),z['rank'],tuple(z['target_class']),z['voltage'],z['clock'])for z in ref['open_outgoing_ports']}
q=-1j;cycle=[];w=0
while q not in cycle:cycle.append(q);q,k=E[q];w+=k
assert q==cycle[0]and len(cycle)==4 and set(cycle)==set(E)and w==-1
for p in H:
 q=p
 for _ in range(6):
  if q in E:break
  q,k=FG[q]
 else:raise AssertionError('first departure does not feed the boundary')
ages=[H[q][-1]['clock']-H[q][0]['clock']for q in(0j,1-1j)];assert ages==[32,96]and sum(ages)==P+4
assert any(z[0]==(1,0)and z[1]==3 for z in oi)
# Materialize prescribed phase positions and check each stored GEOMETRIC gap.
ph=sorted((e['clock']%P,q-(e['clock']//P)*dr,e)for q,es in H.items()for e in es);bridges=[]
for i,(t,q,e)in enumerate(ph):
 tn,qn,en=ph[(i+1)%len(ph)]
 if i==len(ph)-1:tn+=P;qn+=dr
 gap=tn-t;pp=q+V[e['out']];hh=e['out'];path=[]
 if gap>1:
  rr=next(z for z in ref['geometric_bridges']if z['start_phase']==t and z['next_phase']==tn);word=rr['unknown_turns'];assert len(word)==gap-1
  for ch in word:
   assert key(pp)[0]not in H and 2<=pp.real+pp.imag<=11;path.append(xy(pp));hh=(hh+(1 if ch=='R'else-1))%4;pp+=V[hh]
  bridges.append(dict(start=t,end=tn,unknown_updates=len(word),minimum_level=min(x+y for x,y in path),maximum_level=max(x+y for x,y in path)))
 assert(pp,hh)==(qn,en['h'])
assert len(bridges)==5
O={complex(*z)for z in ref['odd_class_screen_only']['O']};assert len(O)==8 and max(q.real+q.imag for q in O)-min(q.real+q.imag for q in O)==12
for ax in(0,1):
 for r in(0,1):assert sum((-1)**int(q.real+q.imag)for q in O if xy(q)[ax]%2==r)%4==2
Q={q for q in O if int(q.real+q.imag)%2==0};C=O-Q;J=sum(q.real+q.imag<c.real+c.imag for q in Q for c in C);assert len(Q)==2 and J==8
# Exact local count algebra, not a guessed visit cap. Row1 incoming E=2,
# outgoing S=2: 2*R_E=4-floor(m/2), with full nonnegative event counts.
row1=[]
for m in range(1,30):
 r=(m+1)//2
 for X in range(3):
  cnt=[X,2-X,r-X,m-2-r+X]
  if min(cnt)>=0 and X+cnt[3]==2:row1.append((m,cnt))
assert sorted({m for m,cnt in row1})==[4,5,8,9]
# Next even row has incoming N=a<=7 and outgoing W=c<=7,
# r=c-a+2R_N<=c+a<=14, so m=2r<=28.
assert max(2*(c-a+2*X)for a in range(8)for c in range(8)for X in range(a+1))==28
out={'status':'PASS normalized cyclic-E growth-eight necessary geometry and open17-event interface only','author_note':sha(note),'internal_edges':edges,'open_incoming_ports':oi,'open_outgoing_ports':oo,'E_cycle':[xy(q)for q in cycle],'winding':w,'triple_ages':ages,'geometric_bridges_NOT_color_certified':bridges,'row1_count_options':row1,'analytic_review':[
'Signed residue charge restricts cyclicE at g8 to full signed diagonal2,2 and ell4. Proper quarter rotations reach full(2,-2), without reflection. Four alternating-axis steps of displacement(-2,2) must alternate N/W. SingletonR corners are incomingW at level-1 and tripleL corners have fullSSN at level0, after translating one triple to0. Their two full-drift xparity classes exhaust each boundary level.',
'Signed one-sided E boundary puts all other used cell classes on the RIGHT of this staircase, hence at levels>=1. At the highest used level, arrival and departure must be from/to the lower half-plane. With fixed cell incoming axis, a firstR is possible only for horizontal incomingE; a subsequent alternatingL would require vertical incomingN, impossible. Thus that highest cell is a singletonR on an odd level in the normalized sector. At least one residual odd class is therefore odd checker; residualcheckerpurity forces ALLfour residual odd classes on positive odd levels, two per lane.',
'The17-event patch is independently reconstructed from explicit six histories and clocks. Physical directed-port ordinal matching checks all12 internal edges including exact full-drift voltages;17 phases are distinct, samecellgaps>=4, five ports each direction remain OPEN. E has the required fourcell winding-1 circle, both other firstR nodes feed it, and tripleages32+96=P+4. The even A finalL predecessor is genuinely open, so no fictitious first/last overlap charge is asserted.',
'Five supplied gap words were checked only as geometric unitstep paths with exact endpoint headings, all unspecified intermediate cells in levels2..11 and outside the six named classes. They are NOT checked or asserted color-compatible with one another. No fullperiod event orbit, finite initial board, or genuine autonomous controller is certified.',
'The proposed eight-odd screen has width12 and both signed residues2mod4, V2/J8. Its three still-unspecified odd classes are not emitted field. Nextrow visitlengths4/5/8/9 follow exactly from two lowerincoming/two loweroutgoing counts; the next evenrow bound28 follows from <=7 each lowerport, not a chosen cap. Exploratory solver statuses are not premises.',
'The historical width10g8 missingexhaustion status is unchanged. AcyclicE remains the larger open branch. This is a necessarygeometry and nonempty OPEN localconstraint interface, not g8 attainment/exclusion, arbitrarycontrollerclassification or capture.'
]}
S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],len(edges),len(oi),len(bridges))
