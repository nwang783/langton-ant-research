from pathlib import Path
from itertools import combinations,product
from collections import Counter
from functools import lru_cache
import json,hashlib
S=Path(__file__);R=S.parent.parent;P=R/'autonomous_controllers_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
bind={'DIAGONAL_TWO_SINGLETONS_FORCE_FIRST_CIRCLE.md':'3efd718ef7613128f71b76114837cf7e4641d78a4388809c180b450cc73395dd','DIAGONAL_MIXED_CORNER_WINDING_CORRECTION.md':'81383bd15b4bead3dc87df3d1616ad3fe4854db0a8271a358e5d23faab70d8b9','certify_diagonal_mixed_corner_exclusion.py':'5612960679cd6875765568a454fe8c0436323a2a7ae0944b7c376ba08dad5694','diagonal_mixed_corner_exclusion_certificate.json':'89d65aaf7f0d492c81094c064e9182d936e8c36466ad20e6d3eaf7183e01e89d'}
for n,h in bind.items():assert sha(P/n)==h
ns={'__file__':str(S.with_name('check_g8_two_row_covers_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Independent binary-position domain')[0],ns);graph,rot,dr,xy=[ns[k]for k in ('graph','rot','dr','xy')]
ref=json.loads((P/'diagonal_mixed_corner_exclusion_certificate.json').read_text());dom=json.loads((P/'certify_diagonal_read_minimum.json').read_text());prior=json.loads((P/'first_N_return_rules_certificate.json').read_text())
assert sha(S.with_name('check_first_N_rules_independent.json'))=='61f072f4f95ae663ff2654124039f4e47e274d58c62642c66d8b67acfbd8270c'
def relations(H):
 pts,su,pr,oo,oi=graph(H);rel=[[],[]];counts=[[0,0],[0,0]];seen=set()
 for root,(sr,k,h)in oi.items():assert h==3 and sum(xy(sr))==2;counts[int(sr.real)][1]+=1
 for node,(tr,k,h,o)in oo.items():assert h==0 and sum(xy(tr))==2;counts[int(tr.real)][0]+=1
 for root in sorted(oi):
  sr,k,h=oi[root];p=sr+k*dr;lane=int(sr.real);a=[j for j,v in enumerate(H[root[0]])if v==h].index(root[1]);u=root;k=0;path=[]
  while True:
   assert u not in seen;seen.add(u);z=pts[u[0]]+k*dr;assert z!=p and sum(xy(z))<=1
   path.append(dict(physical_cell=list(xy(z)),class_index=u[0],complete_rank=u[1],voltage=k,heading=H[u[0]][u[1]],turn='R'if u[1]%2==0 else'L'))
   if u not in su:break
   u,dk=su[u];k+=dk
  q,dk,h,b=oo[u]
  if q+(k+dk)*dr==p:rel[lane].append(dict(W_ordinal=a,N_ordinal=b,duration=len(path)+1,physical_base=list(xy(p)),internal_events=path))
 assert len(seen)==sum(map(len,H));return counts,rel
@lru_cache(None)
def candidates(I,J):
 out=set()
 # Independent generation by ALL incoming-N position subsets, not R/L population split.
 for n in range(I,2*(I+J)+1):
  for inds in combinations(range(n),I):
   z=set(inds);w=tuple(0 if j in z else 2 for j in range(n))
   if sum(rot(h,j)==3 for j,h in enumerate(w))==J:out.add(w)
 return out

def verify(H,row):
 pts,su,pr,oo,oi=graph(H);w=row['witness'];kind=row['reason'];seq=[(tuple(u),k)for u,k in w['segment'if kind=='skipped_rank'else'cycle']]
 for(u,k),(v,l)in zip(seq,seq[1:]):assert su[u]==(v,l-k)
 if kind=='skipped_rank':
  (u,k),(v,l)=seq[0],seq[-1];p=pts[u[0]]+k*dr;assert p==pts[v[0]]+l*dr and all(pts[a[0]]+b*dr!=p for a,b in seq[1:-1]);assert u[1]==w['rank_before']and v[1]==w['rank_after']and v[1]>=u[1]+2 and len(seq)==5;assert list(xy(p))==w['point']
 else:
  assert kind=='closed_component'and len(seq)==4 and len({u for u,k in seq})==4
  u,k=seq[-1];v,l=seq[0];assert su[u]==(v,l+w['winding']-k);assert w['winding']==-1
  assert sum(map(len,H))-4==w['other_local_events']>=44 and len(oi)==w['open_chains']>0
 return kind
allmixed={};allids=set()
for c in dom['cases']:
 for a in c.get('survivors',[]):
  key=(c['case'],tuple(a['A_indices']));allids.add(key);low=c['lower_headings']
  if low[0]and low[1]and any(w[0]==0 for w in low[2:]):allmixed[key]=list(map(tuple,low+a['A_headings']))
assert len(allmixed)==12
rows={(c['lower_case'],tuple(c['A_indices'])):c for c in ref['cases']};assert set(rows)==set(allmixed)
stats=Counter();checks=[]
for key,H in allmixed.items():
 c=rows[key];assert list(map(list,H))==c['complete_lower_histories'];counts,rels=relations(H);assert counts==c['next_Q_port_counts'];assert [2*sum(x)for x in counts]==c['derived_max_helper_lengths']
 for lane in (0,1):assert {json.dumps(x,sort_keys=True)for x in rels[lane]}=={json.dumps(x,sort_keys=True)for x in c['actual_first_return_paths'][lane]}
 domains=[]
 for lane,(I,J)in enumerate(counts):
  raw=candidates(I,J);assert len(raw)==c['raw_complete_helper_word_counts'][lane]
  good=set()
  for w in raw:
   nr=[j for j,h in enumerate(w)if h==0];wr=[j for j,h in enumerate(w)if rot(h,j)==3]
   if all(nr[z['N_ordinal']]==wr[z['W_ordinal']]+1 for z in rels[lane]):good.add(w)
  supplied=list(map(tuple,c['filtered_helper_words'][lane]));assert len(supplied)==len(set(supplied))and set(supplied)==good;domains.append(supplied)
 rejects={tuple(r['helper_indices']):r for r in c['rejections']};assert len(rejects)==len(c['rejections'])==len(domains[0])*len(domains[1])==c['paired_candidates'];local=Counter()
 for i,j in product(range(len(domains[0])),range(len(domains[1]))):local[verify(H+[domains[0][i],domains[1][j]],rejects[i,j])]+=1
 assert dict(local)==c['outcomes'];stats.update(local);checks.append(dict(id=key,counts=counts,raw=[len(candidates(*x))for x in counts],filtered=list(map(len,domains)),outcomes=dict(local)))
assert stats=={'skipped_rank':4668,'closed_component':24}and sum(stats.values())==4692
ids=set(allmixed);p155={(a,tuple(b))for a,b in prior['explicit_set_difference']['exact_final155_ids']};p157={(r['lower_case'],tuple(r['A_indices']))for r in prior['remaining_before_other_signed_reductions']}-{(3,(1,0)),(3,(1,1))}
serial=lambda x:[[a,list(b)]for a,b in sorted(x)]
assert ids<=p155 and ids<=p157 and serial(ids)==ref['explicit_removed_ids']==ref['previous155_intersection']
assert serial(p155-ids)==ref['remaining_g8_143_ids']and serial(p157-ids)==ref['remaining_all_growth_145_ids']and len(p155-ids)==143 and len(p157-ids)==145
out=dict(status='PASS all-growth twelve mixed-minimum interfaces excluded; both minimum singletons force single-used negative F4 circle; g8 remainder143 OPEN',bindings=bind,cases=checks,outcomes=dict(stats),removed_ids=serial(ids),remaining_g8_ids=serial(p155-ids),analytic_review=['Exact complete neighbor ports bound helper n<=2(I+J)<=24 by WHITE alternation, not an assumed global visit cap. Independent enumeration selects every incoming-N subset at every derived length.','Every submitted first-return path is independently rebuilt in full d=(2,-2), with equal physical endpoints and no intermediate occurrence; only then are complete helper words filtered. Both lane orders and odd/even lengths retained.','All4692 Cartesian pairs present exactly once. Every4668 witness has an uninterrupted four-step SAME physical return skipping at least one complete rank. All24 four-event cycles have winding MINUS ONE, so clocks already imply4=-P; mandatory prose correction bound.','All12 exact IDs occur in prior155 and all-growth157. Remainders143/145 are necessary open interfaces, not physical completions.','With two minimum W singleton classes and only SSN/SSNS next corners, their first-R edges alternate through the two singleton classes, form a four-edge winding-1 circle, and are single-used by exact port multiplicities; no claim one-singleton branch disappears.'])
S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],stats)
