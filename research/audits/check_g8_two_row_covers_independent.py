from pathlib import Path
from itertools import combinations,product
from collections import Counter
import json,hashlib
S=Path(__file__).resolve();R=S.parents[1];P=R/'autonomous_controllers_2026-10-24'
sha=lambda f:hashlib.sha256(f.read_bytes()).hexdigest()
BIND={
'G8_TWO_OUTER_ROWS_EXACT_REDUCTION.md':'d4f164cfbf1f16105abe171954249fa695e157ef3f5dff634379ae51a83d9c1b',
'enumerate_g8_cycle_two_outer_rows.py':'c23d88a3244eed736d1419c1da98d4e69f4cc7e9303042eed4f6c4d1daa82d78',
'g8_two_outer_rows_rejection_certificate.json':'34f51adc3c4e9d4482e61261510ce5c6b1371a4f59b53f1119bc071aeb8fa4be',
'G8_CYCLIC_E_EXCLUSION.md':'8981c7ff365b0c686a4cad9a17124cf4c1fd559e166c2d4918da7a34312f3023',
'G8_CYCLIC_E_EXTREME_READ_SUPPORT_ADDENDUM.md':'b24cf42aec746317d3e0ef4f6d9ccd6eb557410f89c3393736db0a009654050b',
'enumerate_g8_cycle_next_c_row.py':'fb755415ea0cbe3b59373f32d849d287e0469b202a960d601420bbda92f44bec',
'g8_next_c_row_rejection_certificate.json':'8ffb2043e8326be420a1be00a10d3553f4e36f22d2c04d0bfaf402b93e9a022a'}
for f,h in BIND.items():assert sha(P/f)==h,(f,sha(P/f))
V=(1j,1,-1j,-1);dr=2-2j;A=((1,1,3,3),(1,1,3,3,3),(3,1,3,3,1));Q=(2,2,2,0,0,2,0,2)
rot=lambda h,j:(h+(1 if j%2==0 else -1))%4
xy=lambda z:(int(z.real),int(z.imag))
def quotient(z):
 k=int(z.real)//2;return z-k*dr,k

def graph(H):
 pts=[complex(r,t-r)for t in range(-1,len(H)//2-1)for r in(0,1)];index={q:i for i,q in enumerate(pts)}
 ev={(i,j)for i,w in enumerate(H)for j in range(len(w))};succ={};pred={};openout={};openin={}
 # Match whole physical directed-port lists, preserving ordinal and full drift.
 for i,w in enumerate(H):
  for h in range(4):
   src=[j for j,v in enumerate(w)if rot(v,j)==h];q,k=quotient(pts[i]+V[h])
   if q not in index:
    for ordinal,j in enumerate(src):openout[i,j]=(q,k,h,ordinal)
   else:
    ii=index[q];dst=[j for j,v in enumerate(H[ii])if v==h]
    assert len(src)==len(dst),(i,h,w,H[ii],src,dst)
    for j,jj in zip(src,dst):
     succ[i,j]=((ii,jj),k);assert(ii,jj)not in pred;pred[ii,jj]=((i,j),k)
 for i,j in ev:
  if(i,j)not in pred:
   h=H[i][j];q,k=quotient(pts[i]-V[h]);assert q not in index
   openin[i,j]=(q,k,h)
 assert set(succ)|set(openout)==ev and set(pred)|set(openin)==ev
 return pts,succ,pred,openout,openin

def verify_witness(H,row):
 pts,succ,pred,oo,oi=graph(H);w=row['witness'];kind=row['reason']
 field='cycle'if kind=='closed_event_component'else'segment';seq=[(tuple(a),k)for a,k in w[field]]
 assert seq
 for (u,k),(v,l)in zip(seq,seq[1:]):assert succ[u]==(v,l-k)
 if kind=='closed_event_component':
  assert len({a for a,k in seq})==len(seq)
  u,k=seq[-1];v,l=seq[0];assert succ[u]==(v,l+w['winding']-k)
 else:
  assert kind=='skipped_physical_rank';(u,k),(v,l)=seq[0],seq[-1]
  p=pts[u[0]]+k*dr;assert p==pts[v[0]]+l*dr and u[1]+1!=v[1]
  assert all(pts[a[0]]+b*dr!=p for a,b in seq[1:-1])
  assert xy(p)==tuple(w['same_physical_cell']) and u[1]==w['earlier_rank'] and v[1]==w['later_rank']
 return len(seq)

def independent_obstruction(H):
 pts,succ,pred,oo,oi=graph(H);seen=set();chains=[]
 for root in sorted(oi):
  seq=[];u=root;k=0;visits={}
  while True:
   assert u not in seen;seen.add(u);p=pts[u[0]]+k*dr
   if p in visits and u[1]!=visits[p]+1:return 'skipped_physical_rank'
   visits[p]=u[1];seq.append((u,k))
   if u not in succ:break
   u,dk=succ[u];k+=dk
  chains.append(seq)
 if len(seen)<sum(map(len,H)):return'closed_event_component'
 return'open'

# Independent binary-position domain, then a deterministic index list for binding.
qsets={};qlists={}
for I,J in product((2,3),repeat=2):
 allset=set()
 for n in range(2,13,2):
  for inds in combinations(range(n),I):
   ns=set(inds);w=tuple(0 if j in ns else 2 for j in range(n))
   if sum(rot(h,j)==3 for j,h in enumerate(w))==J:allset.add(w)
 ordered=[]
 for n in range(2,13,2):
  for x in range(I+1):
   if I+n//2-2*x!=J:continue
   for r,l in product(combinations(range(0,n,2),x),combinations(range(1,n,2),I-x)):
    ns=set(r+l);ordered.append(tuple(0 if j in ns else 2 for j in range(n)))
 assert len(ordered)==len(set(ordered)) and set(ordered)==allset
 qsets[I,J]=allset;qlists[I,J]=ordered
assert {k:len(v)for k,v in qsets.items()}=={(2,2):10,(2,3):19,(3,2):19,(3,3):46}
cert=json.loads((P/'g8_two_outer_rows_rejection_certificate.json').read_text())['rejections'];bycase={tuple(x['case']):x for x in cert};assert len(bycase)==len(cert)==10006
stats=Counter();remaining=[];domains=set();maxw=0
for a,b in product(range(3),repeat=2):
 qa=qlists[len(A[a])-2,len(A[b])-2];qb=qlists[len(A[b])-2,len(A[a])-2]
 for i,j in product(range(len(qa)),range(len(qb))):
  key=(a,b,i,j);domains.add(key);H=[(3,),(3,),(2,2,0),(2,2,0),A[a],A[b],qa[i],qb[j]]
  # Independent scan uses a different priority: every submitted witness is separately checked.
  verdict=independent_obstruction(H)
  if key in bycase:
   z=bycase[key];maxw=max(maxw,verify_witness(H,z));stats[z['reason']]+=1;assert verdict!='open'
  else:assert verdict=='open';remaining.append((key,H))
assert set(bycase)<domains and len(domains)==10008 and len(remaining)==2
assert {(k[0],k[1],H[6],H[7])for k,H in remaining}=={(1,1,Q,Q),(2,2,Q,Q)}
assert stats=={'closed_event_component':1494,'skipped_physical_rank':8512}
report1=json.loads((P/'enumerate_g8_cycle_two_outer_rows.json').read_text())
assert {tuple(z['case'])for z in report1['representative_survivors']}=={k for k,H in remaining}
for z in report1['representative_survivors']:
 H=list(map(tuple,z['headings']));pts,succ,pred,oo,oi=graph(H);assert len(oo)==len(oi)==10 and sum(map(len,H))==34
 clocks={tuple(map(int,k.split(':'))):v for k,v in z['representative_clocks'].items()};period=z['period_for_relaxed_clocks'];assert period==140
 for i,w in enumerate(H):assert all(clocks[i,j+1]-clocks[i,j]>=4 for j in range(len(w)-1))
 for u,(v,k)in succ.items():assert clocks[u]+1==clocks[v]+k*period
 assert 34-len({t%period for t in clocks.values()})==1

# Exact physical lower-patch routes from each C row3 departure to the next open arrival.
returns=[]
for mode in(1,2):
 H=[(3,),(3,),(2,2,0),(2,2,0),A[mode],A[mode],Q,Q];pts,succ,pred,oo,oi=graph(H)
 for lane in(0,1):
  start=complex(lane,3-lane);qi=6+lane;s_ranks=[j for j,h in enumerate(Q)if h==2]
  for s_ord in range(5):
   u=(qi,s_ranks[s_ord]);k=0;length=1;path=[xy(start),xy(pts[qi])];assert oi[u][0]==start
   seen=set()
   while u in succ:
    assert(u,k)not in seen;seen.add((u,k));u,dk=succ[u];k+=dk;length+=1;path.append(xy(pts[u[0]]+k*dr))
   q,dk,h,eo=oo[u];target=q+(k+dk)*dr;length+=1;path.append(xy(target))
   assert all(sum(p)<=2 for p in path[1:-1])
   row=dict(mode=mode,lane=lane,S_ordinal=s_ord,E_ordinal=eo,length=length,start=xy(start),target=xy(target),path=path)
   if s_ord in(0,2):
    assert h==1 and target==start and eo==s_ord+1
    assert length==({0:4,2:12}if mode==1 else{0:12,2:4})[s_ord]
   returns.append(row)

# Independently choose arbitrary five E positions up to DERIVED21, then impose two returns.
allc=set();filtered=set()
for n in range(5,22):
 for inds in combinations(range(n),5):
  ee=set(inds);w=tuple(1 if j in ee else 3 for j in range(n));ss=[j for j,h in enumerate(w)if rot(h,j)==2]
  if len(ss)!=5:continue
  assert n//2+2*sum(j%2==0 for j in inds)==10
  allc.add(w)
  if inds[1]==ss[0]+1 and inds[3]==ss[2]+1:filtered.add(w)
assert len(allc)==2498 and len(filtered)==25
report2=json.loads((P/'enumerate_g8_cycle_next_c_row.json').read_text());cs=list(map(tuple,report2['C_words']));assert len(cs)==len(set(cs))==25 and set(cs)==filtered
assert Counter(map(len,cs))=={8:3,9:4,12:9,13:9}
cert2=json.loads((P/'g8_next_c_row_rejection_certificate.json').read_text());b2={tuple(z['case']):z for z in cert2};assert len(b2)==len(cert2)==1250
stats2=Counter();domain2=set()
for mode in(1,2):
 for a,b in product(range(25),repeat=2):
  key=(mode,a,b);domain2.add(key);H=[(3,),(3,),(2,2,0),(2,2,0),A[mode],A[mode],Q,Q,cs[a],cs[b]];z=b2[key];kind=z['reason'];stats2[kind]+=1
  if kind=='skipped_physical_rank':maxw=max(maxw,verify_witness(H,z))
  else:
   assert kind=='odd_budget_exhausted_before_upper_exit';pts,succ,pred,oo,oi=graph(H)
   assert sum(len(w)%2 for w in H)==8 and all(len(H[i])%2 for i in(8,9))
   for i in(8,9):
    upper=[(j,q,k,h)for(ii,j),(q,k,h,o)in oo.items()if ii==i]
    assert len(upper)==len(H[i])-5 and all(h==0 and q.real+q.imag==4 for j,q,k,h in upper)
   assert z['witness']=={'row3_odd_classes':2,'odd_classes_already_fixed_below':6,'each_upper_outgoing_count':[len(cs[a])-5,len(cs[b])-5]}
assert set(b2)==domain2 and stats2=={'skipped_physical_rank':912,'odd_budget_exhausted_before_upper_exit':338}
# Literal sector/turn extreme check, not a black-field maximum.
extremes={}
for parity in(0,1):
 inc=(0,2)if parity==0 else(1,3);opts=[]
 for h in inc:
  if (V[h].real+V[h].imag)!=1:continue
  for turn in(1,-1):
   out=(h+turn)%4
   if V[out].real+V[out].imag==-1:opts.append(('NESW'[h],'R'if turn==1 else'L','NESW'[out]))
 extremes[parity]=opts
assert extremes=={0:[('N','L','W')],1:[('E','R','S')]}
res={'status':'PASS both derived local covers and cyclic-E exclusion at g8; acyclic E remains open','bindings':BIND,'independent_domain1':10008,'q_domain_sizes':{str(k):len(v)for k,v in qsets.items()},'stage1_rejections':dict(stats),'stage1_surviving_cases':[k for k,H in remaining],'stage1_surviving_Q':'SSSNNSNS','stage1_relaxed_clocks':'34 events,10 ports each direction, P140 one phase collision; NOT a physical completion','exact_lower_return_routes':returns,'single_C_count_domain':len(allc),'single_C_filtered_domain':len(filtered),'single_C_length_distribution':dict(Counter(map(len,cs))),'independent_domain2':1250,'stage2_rejections':dict(stats2),'longest_checked_witness_event_count':maxw,'literal_read_extreme_modes':extremes,'analytic_review':[
'Complete WHITE physical histories begin R and alternate. Exact sector plus directed-port totals derive all finite word bounds. No imposed global visit, period, width, or outside-field bound enters either cover. Higher ports remain open.',
'Every witness edge was reconstructed from the actual outgoing heading, spatial neighbor, full drift d=(2,-2), and full port occurrence ordinal. Each supplied rejection is independently checked as a closed successor component with all its predecessors fixed, or a contiguous lifted physical segment skipping a complete same-cell read rank. In a complete full event permutation no external event can splice into either witness.',
'A closed internal event component cannot be the whole period: at least two odd classes are still required outside the first patch. Nonzero voltage does not relax closure of the finite event permutation. A skipped rank is tested at the SAME physical cell after accumulated full-drift shifts, not just a quotient representative.',
'The two surviving lower assignments independently give literal return paths from row3 S ports0/2 to E ports1/3, durations4/12 interchanged between YY and ZZ. Every intermediate read has level<=2, so these are actual first returns to each same physical row3 cell. Rank adjacency follows regardless of its initial departure turn.',
'After the lower forcing six odd classes are fixed. In all338 odd/odd final cases eight odd classes are already named, and row3 has four or eight outgoing N uses, forcing READS at level4. The complete bi-infinite read footprint of a finite event period has finite maximum x+y, because full drift preserves x+y. Every read there arrives from below and leaves below. Sector makes an even maximum all L, impossible for a WHITE first read, and an odd maximum all R, hence singleton by alternation. Thus a ninth odd class occurs at odd level>=5. This uses READ support, not potential, black field, wake, chosen patch, or cropped-time endpoints.',
'With previously signed extremal residue and boundary geometry, every possible cyclic E at growth8 is normalized by genuine quarter rotations to this branch. Both complete local covers eliminate it at all periods and widths. Therefore growth8 E is acyclic (paths and isolated vertices). This does NOT exclude acyclic growth8 fronts, imply growth>=12, classify autonomous controllers, or prove finite-seed attraction.'
]}
S.with_suffix('.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps({k:v for k,v in res.items()if k not in('bindings','exact_lower_return_routes','analytic_review')},indent=2))
