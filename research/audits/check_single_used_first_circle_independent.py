from pathlib import Path
from itertools import combinations,product
import json,hashlib
S=Path(__file__).resolve();R=S.parents[1];P=R/'autonomous_controllers_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
binds={'SINGLE_USED_FIRST_CIRCLE_MIDDLE_READ_INTERFACE.md':'29cce94ff89eddaebdf8aede750cf56256febdb9ac17ec7850c72359ff335d7e','check_single_used_first_circle.py':'eb7ec7fc73b845f45f829dc2551816813e45b843474fd343ea5324f5a8eb2fbb','check_single_used_first_circle.json':'58a5240c545b65732e07eb5038ebb93a37bb3138a739d2038444883eb8aff1c1'}
for f,h in binds.items():assert sha(P/f)==h
ref=json.loads((P/'check_single_used_first_circle.json').read_text())
# Reuse only our independently signed graph construction, not the author's generator.
x={'__file__':str(S.parent/'check_g8_two_row_covers_independent.py')};src=(S.parent/'check_g8_two_row_covers_independent.py').read_text();exec(src[:src.index('# Independent binary-position domain')],x);graph=x['graph'];obstruction=x['independent_obstruction'];rot=x['rot'];V=x['V'];quotient=x['quotient'];xy=x['xy'];dr=2-2j
words=lambda n,axis:(tuple(axis[1]if j in chosen else axis[0]for j in range(n))for k in range(n+1)for chosen in combinations(range(n),k))
def adjacent(I,J):
 out=[]
 for n in range(1,2*(I+J)+2):
  for E in combinations(range(n),I):
   e=set(E);w=tuple(1 if j in e else 3 for j in range(n));ss=[j for j,h in enumerate(w)if rot(h,j)==2]
   if len(ss)==J and E[1]==ss[0]+1:out.append(w)
 return out
A=adjacent(2,3);B=adjacent(3,2);fmt=lambda w:''.join('NESW'[h]for h in w)
assert {fmt(w)for w in A}=={'EEWWWW','WEWWEW','EEWWWWW','WEWWEWW'}
assert {fmt(w)for w in B}=={'EEE','EEWEWW','EEWWWE','WEWWEE','EEWEWWW','EEWWWEW','WEWWEEW'}
assert set(A)==set(map(tuple,ref['A0_words']))and set(B)==set(map(tuple,ref['A1_words']))
for a,b in product(A,B):assert obstruction([(3,),(3,),(2,2,0,2),(2,2,0),a,b])=='open'
# Actual four-step return with target B0.R2, not fictitious terminal L3.
base=[(3,),(3,),(2,2,0,2),(2,2,0),A[0],(1,1,1)];pts,succ,pred,oo,oi=graph(base);returns=[]
for lane in(0,1):
 i=4+lane;start=pts[i];sr=next(j for j,h in enumerate(base[i])if rot(h,j)==2);u=(i,sr);k=0;chain=[(u,k)];seen=[]
 while True:
  u,dk=succ[u];k+=dk;chain.append((u,k));position=pts[u[0]]+k*dr
  if position==start:break
  seen.append(position)
 assert len(chain)-1==4 and chain[-1][0]==(i,sr+1)and base[i][sr+1]==1
 assert all(z!=start for z in seen)
 returns.append({'lane':lane,'lifted_event_chain':chain,'physical_positions':[xy(pts[u[0]]+k*dr)for u,k in chain]})
# All complete histories at rowQ, using direct position subsets rather than count recurrence.
def qwords(I,J):
 out=[]
 for n in range(1,2*(I+J)+1):
  for N in combinations(range(n),I):
   ns=set(N);w=tuple(0 if j in ns else 2 for j in range(n))
   if sum(rot(h,j)==3 for j,h in enumerate(w))==J:out.append(w)
 return out
Q0=qwords(3,0);Q1all=qwords(1,4);assert len(Q0)==2 and len(Q1all)==15
# Follow every open chain of the lower six classes, including accumulated full drift.
relations=[]
for root,(sr,sk,hi)in oi.items():
 start=sr+sk*dr;u=root;k=0;chain=[(u,k)];positions=[start,pts[u[0]]]
 while u in succ:
  u,dk=succ[u];k+=dk;chain.append((u,k));positions.append(pts[u[0]]+k*dr)
 tr,tk,ho,ordinal=oo[u];end=tr+(k+tk)*dr;positions.append(end)
 if start==end:
  assert start.real+start.imag==2
  inord=[j for j,h in enumerate(base[root[0]])if h==hi].index(root[1])
  assert hi==3 and ho==0
  assert all(z!=start for z in positions[1:-1])
  relations.append((int(sr.real),inord,ordinal,len(chain)+1,chain))
assert [(a,b,c,d)for a,b,c,d,_ in relations]==[(1,1,0,8)],relations
Q1=[w for w in Q1all if [j for j,h in enumerate(w)if h==0][0]==[j for j,h in enumerate(w)if rot(h,j)==3][1]+1]
assert {fmt(w)for w in Q0}=={'NSNSNS','NSNSN'} and{fmt(w)for w in Q1}=={'SSSNSS','SSSNS'}
quads=[]
for q,r in product(Q0,Q1):
 H=base+[q,r];assert obstruction(H)=='open';bins=[0]*4
 for i,w in enumerate(H):
  a=i%2;b=i//2-1-a
  if len(w)%2:bins[2*a+(b%2)]+=1
 full=[]
 for z in product(range(9),repeat=4):
  if sum(z)==8 and all((z[a]-z[b])%4==2 for a,b in[(0,1),(3,2),(0,2),(3,1)]) and all(a<=b for a,b in zip(bins,z)):full.append(z)
 quads.append({'Q_headings':[fmt(q),fmt(r)],'parity_bin_inventory_00_01_10_11':bins,'possible_full_g8_bin_inventories':list(map(list,full))})
assert sorted(quads,key=lambda z:z['Q_headings'])==sorted(ref['four_next_row_modes'],key=lambda z:z['Q_headings'])
assert sum(not z['possible_full_g8_bin_inventories']for z in quads)==1
# Independently reconstruct all actual standard events, full drift and chronological ranks.
stdfile=R/'recovered_bundle/ant_global/root/standard.json';assert sha(stdfile)==ref['standard_source_sha256'];word=json.loads(stdfile.read_text())['word'];p=0j;h=0;hist={}
for t,c in enumerate(word):
 q=-p+2j;r,k=quotient(q);hi=(h+2)%4;ho=rot(hi,0 if c=='R'else 1)
 hist.setdefault(r,[]).append({'rank_time':t-k*104,'phase':t,'hi':hi,'ho':ho,'turn':c})
 h=(h+(1 if c=='R'else-1))%4;p+=V[h]
assert p==-2+2j and h==0 and len(hist)==22
for v in hist.values():v.sort(key=lambda e:e['rank_time']);assert all(e['turn']==('R'if j%2==0 else'L')for j,e in enumerate(v))
assert sum(len(v)%2 for v in hist.values())==12
for row in ref['all_standard_stable_histories']:
 q=complex(*row['point']);assert hist[q]==row['events']and fmt(tuple(e['hi']for e in hist[q]))==row['headings']
assert fmt(tuple(e['hi']for e in hist[1j]))=='EEWWWW'and fmt(tuple(e['hi']for e in hist[1]))=='EEE'
F={};EE={}
for q,vs in hist.items():
 r,k=quotient(q+V[vs[0]['ho']]);F[q]=(r,k)
 # First-R arrival must be one actual target read; preserve its exact rank.
 targets=[j for j,e in enumerate(hist[r])if e['rank_time']+104*k==vs[0]['rank_time']+1];assert len(targets)==1
 if targets[0]==len(hist[r])-1:EE[q]=(r,k)
cycles=[];done=set()
for start in F:
 if start in done:continue
 order=[];ix={};q=start
 while q not in done and q not in ix:ix[q]=len(order);order.append(q);q=F[q][0]
 if q in ix:
  cyc=order[ix[q]:];uses=[sum(e['ho']==hist[v][0]['ho']for e in hist[v])for v in cyc]
  if all(n==1 for n in uses):cycles.append(cyc)
 done.update(order)
assert len(cycles)==1;cyc=cycles[0];assert sorted(fmt(tuple(e['hi']for e in hist[q]))for q in cyc)==['SSN','SSNS','W','W']
assert sum(F[q][1]for q in cyc)==-1 and len(set(cyc)-set(EE))==1
miss=next(q for q in cyc if q not in EE);target,k=F[miss];assert fmt(tuple(e['hi']for e in hist[target]))=='SSNS' and hist[miss][0]['rank_time']+1==hist[target][2]['rank_time']+104*k
out={'status':'PASS conditional all-cap single-used F boundary; genuine full standard positive and four open next-row interfaces','bindings':binds,'adjacent_mode_lists':[[fmt(w)for w in A],[fmt(w)for w in B]],'open_adjacent_pairs':28,'actual_lower_four_step_returns':returns,'next_Q_first_return_relations':relations,'next_Q_modes':quads,'standard_full_classes':22,'standard_growth':12,'standard_single_used_first_cycle':[xy(q)for q in cyc],'standard_missing_E_edge':{'source':xy(miss),'target':xy(target),'target_rank':2,'target_last_rank':3},'analytic_review':[
'For a WHITE cell first outgoing R(A) used once forces every later even rank to arrive -A and every odd rank A. The single-used cycle incoming port then forces singleton at a right corner, or exactly A,A,-A / A,A,-A,A at a left corner. Every other used port is to the right. The signed embedded essential F circle plus connected full used support places all other support on that side, giving at most one such circle. This is a conditional all-cap lemma; no arbitrary F circle is assumed single-used.',
'Its single-use edges land at the final R of triples/singletons or the middle R2 of quadruples. Thus precisely the no-quadruple case is a cyclic E, excluded at g8 by the separately signed complete covers. The quadruple R2-to-L3 lifetime is retained, not assigned to the first edge or omitted.',
'For the stated d=(2,-2) four-edge one-quadruple branch, exact lower ordinal routes are four-step first physical returns even when one B.R2 is not terminal. Counts derive the length bounds; every 4x7 adjacent mode is an open necessary interface, not a full front.',
'The standard positive control reconstructs all22 classes, all104 events and full-drift shifts from the complete literal word. Its growth is12. Its missed E edge is checked at actual target rank2 beforeL3. No cropped standard patch is called a g8 completion.',
'The standard adjacent pair forces one eight-step physical first-return relation at Q1. Direct complete binary position subsets give two Q0 and two Q1 words. Full signed residue inventories reject only the odd/odd case at g8; all three others remain open. No general acyclic-E, growth8, autonomous-controller or finite-seed capture conclusion.'
]};S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
