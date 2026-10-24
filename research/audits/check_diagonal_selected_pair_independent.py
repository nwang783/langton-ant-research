from pathlib import Path
from itertools import product
from collections import Counter
import json,hashlib
S=Path(__file__);ns={'__file__':str(S.with_name('check_diagonal_mixed_corner_independent.py'))};exec(Path(ns['__file__']).read_text().split('allmixed={}')[0],ns)
R,P,sha,graph,relations,candidates,dr,xy=[ns[k]for k in('R','P','sha','graph','relations','candidates','dr','xy')]
bind={'DIAGONAL_SELECTED_PAIR_G8_EXCLUSIONS.md':'e2e81e31f57b715452227e34f221a54937465fa4cf931440dca002c75d6413a7','certify_diagonal_selected_pair_exclusions.py':'596947bb1d80a111d14b21f909458f088ec7d780597d092b07542272b75df3be','diagonal_selected_pair_exclusions_certificate.json':'85fab3456d7f7285e67171f88852fa3e5b5e7281fa2feaa91f63988b3a5e3cad'}
for n,h in bind.items():assert sha(P/n)==h
assert sha(S.with_name('check_diagonal_mixed_corner_independent.json'))=='7573760d0256aa1f0b443f55f8226e36d71e9cf328002d46f045fd9ffcde830e'
ref=json.loads((P/'diagonal_selected_pair_exclusions_certificate.json').read_text());dom=ns['dom'];mixed=json.loads((P/'diagonal_mixed_corner_exclusion_certificate.json').read_text());prior143={(a,tuple(b))for a,b in mixed['remaining_g8_143_ids']};select={(a,tuple(b))for a,b in ref['selected43_ids']};assert len(select)==43 and select<=prior143
# Independently enumerate all nonnegative four-bin compositions of total8, then BOTH coordinate residue laws.
targets=[]
for a in range(9):
 for b in range(9-a):
  for c in range(9-a-b):
   d=8-a-b-c
   if (a-b)%4==(d-c)%4==(a-c)%4==(d-b)%4==2:targets.append((a,b,c,d))
assert len(targets)==10 and list(map(list,targets))==ref['all_ten_signed_residue_compatible_g8_vectors']
byid={(c['case'],tuple(s['A_indices'])):list(map(tuple,c['lower_headings']+s['A_headings']))for c in dom['cases']for s in c.get('survivors',[])}
rows={(c['lower_case'],tuple(c['A_indices'])):c for c in ref['cases']};assert len(rows)==len(ref['cases'])==43 and set(rows)==select
stats=Counter();dur=Counter();checks=[]
for key,c in rows.items():
 H=byid[key];assert list(map(list,H))==c['complete_lower_histories'];counts,rels=relations(H);assert counts==c['next_Q_counts']and max(max(z)for z in counts)<=6 and[2*sum(z)for z in counts]==c['derived_max_lengths'];domains=[]
 for lane,(I,J)in enumerate(counts):
  assert {json.dumps(z,sort_keys=True)for z in rels[lane]}=={json.dumps(z,sort_keys=True)for z in c['actual_first_return_paths'][lane]}
  raw=candidates(I,J);assert len(raw)==c['raw_helper_word_counts'][lane];good=set()
  for w in raw:
   nr=[j for j,h in enumerate(w)if h==0];wr=[j for j,h in enumerate(w)if(h+(1 if j%2==0 else-1))%4==3]
   if all(nr[z['N_ordinal']]==wr[z['W_ordinal']]+1 for z in rels[lane]):good.add(w)
  supplied=list(map(tuple,c['filtered_helper_words'][lane]));assert len(supplied)==len(set(supplied))and set(supplied)==good;domains.append(supplied)
 rej={tuple(r['helper_indices']):r for r in c['rejections']};assert len(rej)==len(c['rejections'])==len(domains[0])*len(domains[1])==c['paired_candidates'];local=Counter()
 for i,j in product(range(len(domains[0])),range(len(domains[1]))):
  HH=H+[domains[0][i],domains[1][j]];row=rej[i,j];kind=row['reason'];w=row['witness'];pts,su,pr,oo,oi=graph(HH)
  if kind=='full_g8_signed_residue_budget':
   bins=[0]*4
   for q,hs in zip(pts,HH):
    if len(hs)%2:bins[2*(int(q.real)%2)+int(q.imag)%2]+=1
   assert bins==w['named_odd_counts_00_01_10_11']and len(w['incompatible_each_target_at_bin'])==10
   for target,k in zip(targets,w['incompatible_each_target_at_bin']):assert 0<=k<4 and bins[k]>target[k]
   assert not any(all(a<=b for a,b in zip(bins,z))for z in targets)
  else:
   seq=[(tuple(u),k)for u,k in w['segment'if kind=='skipped_rank'else'cycle']]
   for(u,k),(v,l)in zip(seq,seq[1:]):assert su[u]==(v,l-k)
   if kind=='skipped_rank':
    (u,k),(v,l)=seq[0],seq[-1];p=pts[u[0]]+k*dr;assert p==pts[v[0]]+l*dr and all(pts[a[0]]+b*dr!=p for a,b in seq[1:-1]);assert v[1]!=u[1]+1 and w['rank_before']==u[1]and w['rank_after']==v[1]and list(xy(p))==w['point'];assert len(seq)-1 in(4,8);dur[len(seq)-1]+=1
   else:
    assert kind=='closed_component'and len({u for u,k in seq})==len(seq);u,k=seq[-1];v,l=seq[0];assert w['winding']==-1 and su[u]==(v,l-1-k);assert w['other_local_events']==sum(map(len,HH))-len(seq)>0 and w['open_chains']==len(oi)>0
  local[kind]+=1
 assert dict(local)==c['outcomes'];stats.update(local);checks.append(dict(id=key,ports=counts,domain_sizes=list(map(len,domains)),outcomes=dict(local)))
assert stats==ref['outcomes']=={'skipped_rank':2846,'full_g8_signed_residue_budget':28,'closed_component':22}and sum(stats.values())==2896 and dur=={4:1544,8:1302}
serial=lambda z:[[a,list(b)]for a,b in sorted(z)];final=prior143-select;assert len(final)==100 and serial(final)==ref['remaining100_ids']and serial(select)==ref['previous143_intersection']and not ref['overlap_with_mixed12']
cat=Counter()
for key in final:
 H=byid[key];cat['one_singleton'if not H[1]else'one_quadruple'if sum(len(w)==4 for w in H[2:4])==1 else'two_quadruple']+=1
assert cat=={'one_singleton':4,'one_quadruple':22,'two_quadruple':74}
source=R/'sources/kehao95-core/wake_synthesis/proof/periodic-growth-closure.md'
out=dict(status='PASS specified43 growth8 complete helper covers; necessary diagonal remainder100 OPEN',bindings=bind,mixed_audit=sha(S.with_name('check_diagonal_mixed_corner_independent.json')),signed_residue_source=sha(source),all_ten_full_odd_vectors=targets,cases=checks,outcomes=dict(stats),skipped_first_return_lengths=dict(dur),remaining_ids=serial(final),remaining_types=dict(cat),analytic_review=['All43 chosen IDs are exact members of prior143 and disjoint from mixed12. Derived local lengths come only from total physical N/W ports; every complete WHITE helper string is regenerated by incoming-N position subsets. Higher support and period remain unbounded.','Every actual lower first-return path is reconstructed in full drift. Every2896 Cartesian choice appears once. Literal 4/8-step SAME-physical-cell paths have no intermediate target visit and fail consecutive ranks. This is not an eight-step-versus-minimum-time argument.','Twenty-two internal directed cycles have negative winding, impossible by summed positive-duration clocks. Properness and exterior open chains also checked.','Residue test concerns the FULL eight odd classes: both x and y parity-bin balances equal2mod4. All ten possible full vectors retained. Named COMPLETE histories contribute a coordinatewise lower bound only; no subset balanced-wake assertion or maximum-field assumption.','The exact100 remaining IDs are4 one-singleton/22 one-quadruple/74 two-quadruple necessary interfaces, not100 completed fronts, no g8 exclusion or universal capture.'])
S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],stats,cat)
