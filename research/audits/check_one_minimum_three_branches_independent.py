from pathlib import Path
from itertools import product
from collections import Counter
import json,hashlib
S=Path(__file__);R=S.parent.parent;P=R/'autonomous_controllers_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
bind={}
for line in(P/'ONE_MINIMUM_THREE_BRANCH_SHA256SUMS').read_text().splitlines():
 h,f=line.split();assert sha(P/f)==h;bind[f]=h
assert bind['ONE_MINIMUM_THREE_BRANCH_EXCLUSION.md']=='68ad7151b52df8f217429168063ef49198b8ce48998a90ea619b8d56f80300da'
bp=S.with_name('check_g8_two_row_covers_independent.py');ns={'__file__':str(bp)};exec(bp.read_text().split('# Independent binary-position domain')[0],ns)
graph,V,dr,xy,quotient=[ns[k]for k in('graph','V','dr','xy','quotient')]
ref=json.loads((P/'one_minimum_three_branches_certificate.json').read_text());source=json.loads((P/'certify_diagonal_read_minimum.json').read_text());old=json.loads((P/'diagonal_selected_pair_exclusions_certificate.json').read_text())
prior={(a,tuple(b))for a,b in old['remaining100_ids']};ids={(a,tuple(b))for a,b in ref['three_excluded_ids']};assert ids=={(1,(0,0)),(1,(1,0)),(3,(3,0))}and ids<=prior
byid={(c['case'],tuple(s['A_indices'])):list(map(tuple,c['lower_headings']+s['A_headings']))for c in source['cases']for s in c.get('survivors',[])}
targets=[]
for a in range(9):
 for b in range(9-a):
  for c in range(9-a-b):
   d=8-a-b-c
   if all(v%4==2 for v in(a-b,d-c,a-c,d-b)):targets.append((a,b,c,d))
assert len(targets)==10 and list(map(list,targets))==ref['all_ten_full_g8_parity_vectors']
def net(H):
 pts,su,pr,oo,oi=graph(H);chains=[];seen=set()
 for root in sorted(oi):
  seq=[];u=root;k=0
  while True:
   assert u not in seen;seen.add(u);seq.append((u,k))
   if u not in su:break
   u,dk=su[u];k+=dk
  chains.append(seq)
 return pts,su,pr,oo,oi,chains,seen

def upper(H):
 pts,su,pr,oo,oi,chains,seen=net(H);assert len(seen)==sum(map(len,H))
 t=len(H)//2-1;plus,dep=(1,2)if t%2 else(0,3);counts=[[0,0],[0,0]];rels=[[],[]]
 for q,k,h,j in oo.values():
  assert int(q.real+q.imag)==t and h==plus;counts[int(q.real)][0]+=1
 for q,k,h in oi.values():
  assert int(q.real+q.imag)==t and h==dep;counts[int(q.real)][1]+=1
 for seq in chains:
  (u,k),(v,l)=seq[0],seq[-1];p=pts[u[0]]-V[H[u[0]][u[1]]];h=(H[v[0]][v[1]]+(1 if v[1]%2==0 else-1))%4;q=pts[v[0]]+l*dr+V[h]
  if p!=q:continue
  lane=int(quotient(p)[0].real);a=[j for j,x in enumerate(H[u[0]])if x==H[u[0]][u[1]]].index(u[1]);b=[j for j,x in enumerate(H[v[0]])if(x+(1 if j%2==0 else-1))%4==h].index(v[1])
  rels[lane].append(dict(outgoing_ordinal=a,incoming_ordinal=b,duration=len(seq)+1,physical_source=list(xy(p)),lower_chain=[[list(e),k]for e,k in seq]))
 return counts,rels

def domains(I,J,t,rel):
 plus,minus,dep=(1,3,2)if t%2 else(0,2,3);bound=2*(I+J)+(t%2);constraints=[(z['outgoing_ordinal'],z['incoming_ordinal'])for z in rel];answer=[];stack=[((),(),())];visits=0
 # Independent rank-position prefix check, not the author's pending/last-departure automaton.
 while stack:
  word,ip,op=stack.pop();n=len(word);visits+=1
  valid=True
  for a,b in constraints:
   if b<len(ip):
    if a>=len(op)or ip[b]!=op[a]+1:valid=False;break
   elif a<len(op)and op[a]+1<n:valid=False;break
  if not valid:continue
  if len(ip)==I and len(op)==J and all(a<len(op)and b<len(ip)for a,b in constraints):answer.append(word)
  if n==bound:continue
  for h in(minus,plus):
   ni=ip+(n,)if h==plus else ip;no=op+(n,)if(h+(1 if n%2==0 else-1))%4==dep else op
   if len(ni)<=I and len(no)<=J:stack.append((word+(h,),ni,no))
 assert len(answer)==len(set(answer));return set(answer),bound,visits

def check(H,row):
 kind=row['outcome'];pts,su,pr,oo,oi,chains,seen=net(H);N=sum(map(len,H))
 if kind=='open':assert len(seen)==N;return
 w=row['witness']
 if kind=='residue_budget':
  bins=[0]*4
  for p,h in zip(pts,H):
   if len(h)%2:bins[2*(int(p.real)%2)+int(p.imag)%2]+=1
  assert bins==w['named_odd_parity_inventory']and len(w['violated_bins'])==10
  for z,k in zip(targets,w['violated_bins']):assert bins[k]>z[k]
 elif kind in('skipped_rank','closed_component'):
  seq=[(tuple(u),k)for u,k in w['segment'if kind=='skipped_rank'else'cycle']]
  for (u,k),(v,l)in zip(seq,seq[1:]):assert su[u]==(v,l-k)
  if kind=='skipped_rank':
   (u,k),(v,l)=seq[0],seq[-1];p=pts[u[0]]+k*dr;assert p==pts[v[0]]+l*dr and all(pts[e[0]]+z*dr!=p for e,z in seq[1:-1]);assert v[1]!=u[1]+1 and w['rank_before']==u[1]and w['rank_after']==v[1]and w['point']==list(xy(p))
  else:
   assert len({u for u,k in seq})==len(seq);u,k=seq[-1];v,l=seq[0];wind=w['winding'];assert su[u]==(v,l+wind-k);assert w['other_local_events']==N-len(seq)and w['open_chains']==len(chains);assert wind<=0 or N>len(seq);winds[wind]+=1
 elif kind=='positive_rank_clock_cycle':
  assert len(seen)==N and w['chains']==[[[list(e),k]for e,k in q]for q in chains];where={e:(ci,i,k)for ci,q in enumerate(chains)for i,(e,k)in enumerate(q)};valid=set()
  for i,h in enumerate(H):
   for j in range(len(h)-1):
    a,u,ka=where[i,j];b,v,kb=where[i,j+1];valid.add((a,b,4+u-v,kb-ka,i,j))
  cy=list(map(tuple,w['inequality_cycle']));assert cy and all(e in valid for e in cy)and all(cy[i][0]==cy[(i+1)%len(cy)][1]for i in range(len(cy)))
  C=sum(e[2]for e in cy);K=sum(e[3]for e in cy);assert C==w['constant']and K==w['period_coefficient']and N==w['local_event_count']and K>=0 and C+K*N==w['positive_at_minimum_period']>0
 else:assert False,kind
stats=Counter();winds=Counter();visits=0;largest=0;roundstats=[]
for branch in ref['branches']:
 key=(branch['coarse_id'][0],tuple(branch['coarse_id'][1]));H=byid[key];assert list(map(list,H))==branch['initial_histories'];front=[H]
 for rd in branch['rounds']:
  assert len(front)==rd['parent_count']==len(rd['parents']);assert [list(map(list,H))for H in front]==[p['complete_histories']for p in rd['parents']];nxt=[];ss=Counter()
  for H,pa in zip(front,rd['parents']):
   counts,rels=upper(H);assert counts==pa['port_counts']and rels==pa['actual_first_return_paths'];t=len(H)//2-1;assert pa['next_normal_level']==t;dd=[]
   for lane,(I,J)in enumerate(counts):
    good,bound,v=domains(I,J,t,rels[lane]);sup=list(map(tuple,pa['complete_helper_domains'][lane]));assert len(sup)==len(set(sup))and set(sup)==good;assert bound==pa['derived_read_bounds'][lane];dd.append(sup);visits+=v;largest=max(largest,bound)
   pairs={tuple(r['helper_indices']):r for r in pa['all_pairs']};assert len(pairs)==len(pa['all_pairs'])==len(dd[0])*len(dd[1])
   for i,j in product(range(len(dd[0])),range(len(dd[1]))):
    HH=H+[dd[0][i],dd[1][j]];r=pairs[i,j];check(HH,r);ss[r['outcome']]+=1
    if r['outcome']=='open':nxt.append(HH)
  assert dict(ss)==rd['outcomes'];stats.update(ss);front=nxt;roundstats.append(dict(id=key,parents=rd['parent_count'],counts=dict(ss)));print(key,dict(ss),flush=True)
 assert not front and branch['final_open_count']==0
assert dict(stats)==ref['total_pair_outcomes']and {str(k):v for k,v in winds.items()}==ref['closed_cycle_windings'];assert largest==32
remaining=prior-ids;assert len(remaining)==97 and [[a,list(b)]for a,b in sorted(remaining)]==ref['exact_remaining97_ids']
out={'status':'PASS exact three one-minimum g8 branches excluded;97 necessary interfaces remain OPEN','bindings':bind,'outcomes':dict(stats),'closed_windings':dict(winds),'independent_prefix_nodes':visits,'largest_derived_bound':largest,'rounds':roundstats,'remaining_ids':[[a,list(b)]for a,b in sorted(remaining)],'analytic_review':[
'All next-row mandatory port counts were reconstructed directly from the complete exposed physical directed graph, with quotient voltage and all zero-use ports. Both empty classes and either complete-word parity are retained. Vertical bound n<=2(I+J), horizontal n<=2(I+J)+1 follow exact turn counts, not a front-wide cap.',
'Independent helper generation used complete binary prefixes and explicit stored incoming/outgoing RANK POSITIONS. A prefix is rejected only if a known physical return relation cannot still satisfy incoming_rank=outgoing_rank+1 or fixed counts are exceeded. Every completed prefix satisfying all constraints is retained AND can be extended. This differs from the author pending/last-departure automaton and reconstructs every supplied domain through bound32.',
'Every lower first-return chain is reconstructed from actual full drift and SAME physical source/target; no quotient-only return equation is imposed. All Cartesian choices and every intermediate open parent are retained exactly through all three levels.',
'Every rejection is independently checked: literal successor chains with skipped consecutive physical ranks; complete odd-bin lower bounds against ALL ten full g8 residue vectors; explicit cycle edges from rank gaps>=4, with nonnegative period coefficient and positivity already at P>=named_event_count; or closed event components. The three positive-winding closed cycles are rejected for PROPERNESS with additional named events, not for winding+1 alone.',
'The exact three source IDs are members of the signed100 remainder. The remaining one-minimum ID(3,[3,1]) and96 two-minimum interfaces remain OPEN necessary cases, not models or completed controllers. No growth-eight exclusion, higher-row support bound, solver result, or general classification follows.'
]};S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S),sha(S.with_suffix('.json')))
