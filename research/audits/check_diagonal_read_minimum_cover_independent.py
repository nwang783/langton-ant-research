from pathlib import Path
from itertools import combinations,product
from collections import Counter
import json,hashlib
S=Path(__file__).resolve();R=S.parents[1];P=R/'autonomous_controllers_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
binds={'DIAGONAL_READ_MINIMUM_COMPLETE_INTERFACE.md':'77fde6d49196db1c3074c9db7adfa1abda3a80500213f0c0d712bdeb0505b274','certify_diagonal_read_minimum.py':'3a370e8eccb2493caa1cdf42bf210decd20ae7e78d2788a6e48ac43c85cbb1a6','certify_diagonal_read_minimum.json':'a4de122acffd766aee76c6676bb247f02c8754fc9ecfd5949cd20c5478929c7f'}
for f,h in binds.items():assert sha(P/f)==h
ref=json.loads((P/'certify_diagonal_read_minimum.json').read_text());x={'__file__':str(S.parent/'check_g8_two_row_covers_independent.py')};src=(S.parent/'check_g8_two_row_covers_independent.py').read_text();exec(src[:src.index('# Independent binary-position domain')],x);graph=x['graph'];rot=x['rot'];V=x['V'];quotient=x['quotient'];xy=x['xy'];dr=2-2j;fmt=lambda w:''.join('NESW'[v]for v in w)
def directed_words(I,J,axis):
 result=[]
 bound=2*(I+J)+(1 if axis==1 else 0)
 for n in range(bound+1):
  for chosen in combinations(range(n),I):
   es=set(chosen);w=tuple(axis if j in es else(axis+2)%4 for j in range(n))
   if sum(rot(h,j)==(2 if axis==1 else 3)for j,h in enumerate(w))==J:result.append(w)
 return result
# Actual maximum and minimum sector modes, independently using directions, not a black-board extreme.
minimum={}
for parity in(0,1):
 modes=[]
 for h in((0,2)if parity==0 else(1,3)):
  if V[h].real+V[h].imag!=-1:continue
  for s in(1,-1):
   o=(h+s)%4
   if V[o].real+V[o].imag==1:modes.append(('NESW'[h],'R'if s==1 else'L','NESW'[o]))
 minimum[parity]=modes
assert minimum=={0:[('S','L','E')],1:[('W','R','N')]}
assert set(directed_words(1,0,0))=={(0,),(0,2)}and set(directed_words(0,1,0))=={(2,),(2,2)}
Q={(2,2,0),(2,2,0,2),(0,2,2),(0,2,2,2)};assert set(directed_words(1,1,0))==Q
expected={((3,),(),a,b)for a,b in product(directed_words(1,0,0),directed_words(0,1,0))}|{((3,),(3,),a,b)for a,b in product(Q,repeat=2)}
assert len(expected)==20 and len(ref['cases'])==20 and {tuple(map(tuple,z['lower_headings']))for z in ref['cases']}==expected

def chains(H):
 pts,su,pr,oo,oi=graph(H);seqs=[];used=set()
 for root in sorted(oi):
  u=root;k=0;seq=[]
  while True:
   assert u not in used;used.add(u);seq.append((u,k))
   if u not in su:break
   u,dk=su[u];k+=dk
  seqs.append(seq)
 return pts,su,pr,oo,oi,seqs,used

def check_witness(H,kind,w):
 pts,su,pr,oo,oi,seqs,used=chains(H);N=sum(map(len,H))
 if kind=='closed_component':
  cy=[(tuple(u),k)for u,k in w['cycle']];assert len(cy)==len({u for u,k in cy})
  for(u,k),(v,l)in zip(cy,cy[1:]):assert su[u]==(v,l-k)
  u,k=cy[-1];v,l=cy[0];assert su[u]==(v,l+w['winding']-k)
  assert w['other_local_events']==N-len(cy)>0 and w['open_chains']==len(seqs)
  assert len(cy)==4 and w['winding']==1 and N-len(cy)==16 and len(seqs)==4
  return
 assert kind=='positive_rank_clock_cycle'and len(used)==N
 stored=[[(tuple(u),k)for u,k in seq]for seq in w['chains']];assert stored==seqs
 where={u:(i,a,k)for i,seq in enumerate(seqs)for a,(u,k)in enumerate(seq)}
 allowed=set()
 for i,hs in enumerate(H):
  for j in range(len(hs)-1):
   u,a,ka=where[i,j];v,b,kb=where[i,j+1];allowed.add((u,v,4+a-b,kb-ka,i,j))
 cycle=list(map(tuple,w['inequality_cycle']));assert cycle and all(e in allowed for e in cycle)
 # Stored in backwards traversal order; verify every directed endpoint and total.
 assert all(cycle[(i+1)%len(cycle)][1]==e[0]for i,e in enumerate(cycle))
 C=sum(e[2]for e in cycle);K=sum(e[3]for e in cycle)
 assert(C,K,N,C+K*N)==(w['constant'],w['period_coefficient'],w['local_event_count'],w['positive_at_minimum_period'])
 assert K>=0 and C+K*N>0

def returns(H):
 pts,su,pr,oo,oi,seqs,used=chains(H);assert len(used)==sum(map(len,H));relations=[[],[]];routes=[]
 for seq in seqs:
  root,k=seq[0];assert k==0;sr,sk,hi=oi[root];start=sr+sk*dr
  end,kk=seq[-1];tr,tk,ho,eo=oo[end];target=tr+(kk+tk)*dr
  assert start.real+start.imag==target.real+target.imag==1
  assert hi==2 and ho==1
  if start==target:
   ord0=[j for j,h in enumerate(H[root[0]])if h==hi].index(root[1]);lane=int(sr.real);length=len(seq)+1
   assert all(pts[u[0]]+k*dr!=start for u,k in seq)
   relations[lane].append((ord0,eo,length));routes.append({'lane':lane,'outgoing_ordinal':ord0,'incoming_ordinal':eo,'length':length,'physical_start':list(xy(start)),'lower_chain':[[list(u),k]for u,k in seq]})
 return relations,routes

lower_stats=Counter();outcomes=Counter();opened=[];domains=0;cover=[]
for case in ref['cases']:
 H=list(map(tuple,case['lower_headings']));kind=case['lower_status'];lower_stats[kind]+=1
 if kind!='open':
  check_witness(H,kind,case['rejection']);assert H[2][0]==H[3][0]==0;continue
 rel,paths=returns(H);assert paths==case['first_returns']and [[list(t)for t in r]for r in rel]==case['rank_relations']
 counts=[(sum(rot(h,j)==1 for j,h in enumerate(H[3])),H[2].count(2)),(sum(rot(h,j)==1 for j,h in enumerate(H[2])),H[3].count(2))];assert list(map(list,counts))==case['top_counts']
 choices=[]
 for lane,(I,J)in enumerate(counts):
  words=directed_words(I,J,1);assert len(words)==case['raw_single_cell_counts'][lane]
  valid=set()
  for w in words:
   E=[j for j,h in enumerate(w)if h==1];Ss=[j for j,h in enumerate(w)if rot(h,j)==2]
   if all(E[b]==Ss[a]+1 for a,b,L in rel[lane]):valid.add(w)
  stored=list(map(tuple,case['filtered_A_words'][lane]));assert len(stored)==len(set(stored))and set(stored)==valid;choices.append(stored)
 universe=set(product(range(len(choices[0])),range(len(choices[1]))));domains+=len(universe)
 rejects={tuple(z['A_indices']):z for z in case['rejections']};survivors={tuple(z['A_indices']):z for z in case['survivors']}
 assert len(rejects)==len(case['rejections'])and len(survivors)==len(case['survivors'])and not(rejects.keys()&survivors.keys())and rejects.keys()|survivors.keys()==universe
 stats=Counter()
 for key,z in rejects.items():
  HH=H+[choices[0][key[0]],choices[1][key[1]]];check_witness(HH,z['reason'],z['witness']);stats[z['reason']]+=1
 for key,z in survivors.items():
  HH=H+[choices[0][key[0]],choices[1][key[1]]];pts,su,pr,oo,oi,seqs,used=chains(HH)
  assert len(used)==sum(map(len,HH))==z['event_count']and [[list(u),k]for u,k in []]==[]
  assert [[ [list(u),k]for u,k in seq]for seq in seqs]==z['chains']and list(map(list,HH[4:]))==z['A_headings']
  # Open is only a retained necessary case. It need not admit all global clocks or a full front.
  stats['open']+=1;opened.append({'lower':[fmt(w)for w in H],'A':[fmt(w)for w in HH[4:]],'events':sum(map(len,HH))})
 assert dict(stats)==case['pair_outcomes'];outcomes.update(stats);cover.append({'case':case['case'],'lower':[fmt(w)for w in H],'filtered_domains':list(map(len,choices)),'outcomes':dict(stats)})
assert lower_stats=={'open':16,'positive_rank_clock_cycle':4}and domains==444 and outcomes=={'open':227,'positive_rank_clock_cycle':214,'closed_component':3}
classes=Counter(tuple(z['lower'][2:])for z in opened if z['lower'][1]);assert classes[('SSN','SSN')]==9 and classes[('SSNS','SSNS')]==144 and classes[('SSN','SSNS')]==classes[('SSNS','SSN')]==28
assert not any('NSS'in z['lower']for z in opened)
assert len([z for z in opened if not z['lower'][1]])==6
assert sum(v for k,v in classes.items()if'NSSS'in k)==12
assert len(opened)-9==218
out={'status':'PASS exact complete all-cap diagonal-two read-minimum20/444 necessary cover; 218 open ordered interfaces atg8, no exclusion','bindings':binds,'minimum_actual_read_modes':minimum,'lower_outcomes':dict(lower_stats),'paired_domain':domains,'paired_outcomes':dict(outcomes),'all16_open_lower_case_domains':cover,'open_boundary_classes':{str(k):v for k,v in classes.items()},'remaining_g8_count':218,'analytic_review':[
'For full d=(2,-2), the actual finite-period read footprint has a finite normal minimum. At an even minimum every visit would beS-toE/L, impossible from WHITE; odd minimum every visitW-toN/R, hence singleton by alternation. Genuine translations fix sector and level, and translation(1,-1) exchanges lanes. There are exactly two full-drift classes per level. One or two nonempty W singleton classes exhaust the minimum, without primitive-drift replacement or arbitrary occupancy upstairs.',
'Exact lower incoming-N/outgoing-W counts imply ceil(n/2)<=I+J and hence derive all4 one-singleton or16 two-singleton complete B profiles. Empty upper classes are included whenever counts permit; no minimum future width or visit cap is imposed.',
'All20 lower configurations and all444 next-row pairs were independently rebuilt from complete position-subset histories and literal lower-chain first-return rank relations. The whole stored paired domain is partitioned duplicate-free into explicit rejections and open cases. These relations only apply at the SAME physical top cell, with full voltage accumulation and no intervening return.',
'Every one of4 lower and214 paired rank-clock contradictions is checked by independently reconstructed chains, exact representative offsets, actual consecutive-rank inequality>=4, complete edge membership and directed-cycle sum. Each has K>=0 and C+K*N>0, so contradicts any full P>=N. Bellman-Ford discovery and its selected testP are not proof premises; no extra chain-separation constraint is used.',
'All3 closed-component witnesses have4 events, winding+1,16 OTHER named events and4 open chains. Their internal successor/predecessor ports are fully fixed and cannot splice to the rest of the unique actual event orbit. Winding+1 by itself is not rejected.',
'The227 surviving interfaces are necessary OPEN cases only:6 one-singleton,12 mixed N-first/S-first,9 two-triple S-first,56 one-quadruple S-first and144 two-quadruple S-first. Only the9 two-triple cases use the separately signed cyclic-E g8 exclusion, leaving218 atg8. Higher region, period and visit counts outside the derived patch remain unbounded. Other drifts and all remaining cases remain open; no physical completion, growth>=12, controller classification or attraction follows.'
]};S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
