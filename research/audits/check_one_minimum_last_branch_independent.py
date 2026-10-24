from pathlib import Path
from collections import Counter
from itertools import product
import json,hashlib
S=Path(__file__);bp=S.with_name('check_one_minimum_three_branches_independent.py');ns={'__file__':str(bp)};exec(bp.read_text().split('stats=Counter();winds=Counter()')[0],ns)
R,P,sha,domains,upper,check,targets,byid,prior,V,dr,xy,qt=[ns[k]for k in('R','P','sha','domains','upper','check','targets','byid','prior','V','dr','xy','quotient')]
bind={}
for line in(P/'ONE_MINIMUM_LAST_BRANCH_SHA256SUMS').read_text().splitlines():
 h,f=line.split();assert sha(P/f)==h;bind[f]=h
assert bind['ONE_MINIMUM_LAST_BRANCH_EXCLUSION.md']=='1e3faf573b9d45724535c8d10606d5d4302596ad82e36c1d0c49fa684653147f'
ref=json.loads((P/'one_minimum_last_branch_certificate.json').read_text());key=(3,(3,1));initial=byid[key];assert list(map(list,initial))==ref['initial_complete_histories']and ref['excluded_coarse_id']==[3,[3,1]]
# New independent arbitrary COMPLETE named-cell graph. Omitted cells are unknown, whereas explicitly empty cells remain indexed.
CURRENT_POINTS=None
def graph(H):
 pts=CURRENT_POINTS if CURRENT_POINTS is not None else[complex(r,t-r)for t in range(-1,len(H)//2-1)for r in(0,1)];assert len(pts)==len(H)and len(set(pts))==len(pts);index={p:i for i,p in enumerate(pts)};ev={(i,j)for i,h in enumerate(H)for j in range(len(h))};su={};pr={};oo={};oi={}
 for i,hs in enumerate(H):
  for h in range(4):
   src=[j for j,x in enumerate(hs)if(x+(1 if j%2==0 else-1))%4==h];q,k=qt(pts[i]+V[h])
   if q in index:
    ii=index[q];dst=[j for j,x in enumerate(H[ii])if x==h];assert len(src)==len(dst)
    for u,v in zip(src,dst):su[i,u]=((ii,v),k);assert(ii,v)not in pr;pr[ii,v]=((i,u),k)
   else:
    for a,j in enumerate(src):oo[i,j]=(q,k,h,a)
 for i,j in ev:
  if(i,j)not in pr:
   h=H[i][j];q,k=qt(pts[i]-V[h]);assert q not in index;oi[i,j]=(q,k,h)
 assert set(su)|set(oo)==ev and set(pr)|set(oi)==ev
 return pts,su,pr,oo,oi
ns['graph']=graph;winds=Counter();ns['winds']=winds;stats=Counter();visits=0;largest=0;rounds=[];front=[initial]
for rd in ref['full_rows']:
 assert rd['parent_count']==len(front)==len(rd['parents'])and [list(map(list,H))for H in front]==[z['complete_histories']for z in rd['parents']];nxt=[];ss=Counter()
 for H,pa in zip(front,rd['parents']):
  counts,rels=upper(H);assert counts==pa['port_counts']and rels==pa['actual_first_return_paths'];dd=[];t=len(H)//2-1
  for lane,(I,J)in enumerate(counts):
   good,bound,v=domains(I,J,t,rels[lane]);sup=list(map(tuple,pa['complete_helper_domains'][lane]));assert len(sup)==len(set(sup))and set(sup)==good and bound==pa['derived_read_bounds'][lane];dd.append(sup);visits+=v
  pairs={tuple(z['helper_indices']):z for z in pa['all_pairs']};assert len(pairs)==len(pa['all_pairs'])==len(dd[0])*len(dd[1])
  for i,j in product(range(len(dd[0])),range(len(dd[1]))):
   HH=H+[dd[0][i],dd[1][j]];row=pairs[i,j];check(HH,row);ss[row['outcome']]+=1
   if row['outcome']=='open':nxt.append(HH)
 assert dict(ss)==rd['outcomes'];stats.update(ss);front=nxt;rounds.append(dict(ss));print('FULL',dict(ss),flush=True)
assert dict(stats)==ref['two_full_row_outcomes']and len(front)==1312==ref['terminal_parent_count']==len(ref['terminal_one_cell_covers'])
ts=Counter()
for ind,(H,pa)in enumerate(zip(front,ref['terminal_one_cell_covers'])):
 assert pa['parent_index']==ind and pa['complete_lower_histories']==list(map(list,H));counts,rels=upper(H);assert counts==pa['both_mandatory_port_counts'];lane=pa['selected_lane'];assert lane in(0,1)and rels[lane]==pa['selected_actual_first_return_paths'];t=len(H)//2-1;I,J=counts[lane];good,bound,v=domains(I,J,t,rels[lane]);visits+=v;largest=max(largest,bound);assert bound==pa['selected_derived_bound'];sup=list(map(tuple,pa['selected_complete_helper_domain']));assert len(sup)==len(set(sup))and set(sup)==good
 pts=[complex(r,s-r)for s in range(-1,t)for r in(0,1)]+[complex(lane,t-lane)];assert list(map(lambda p:list(xy(p)),pts))==pa['all_complete_points_with_selected_cell'];assert complex(1-lane,t-(1-lane))not in pts
 CURRENT_POINTS=pts
 rejects={z['helper_index']:z for z in pa['all_word_rejections']};assert len(rejects)==len(pa['all_word_rejections'])==len(sup)and set(rejects)==set(range(len(sup)))
 for i,w in enumerate(sup):check(H+[w],rejects[i]);ts[rejects[i]['outcome']]+=1
 ts['empty_domain_parents'if not sup else'nonempty_domain_parents']+=1;CURRENT_POINTS=None
 if ind%250==0:print('TERMINAL',ind,flush=True)
assert dict(ts)==ref['terminal_outcomes']and largest==42==ref['maximum_selected_derived_bound']and sum(len(x['all_word_rejections'])for x in ref['terminal_one_cell_covers'])==13968
assert {str(k):v for k,v in winds.items()}==ref['closed_windings']=={'-1':187,'1':116,'0':2}
# Positive complete-subset controls use only the supplied genuine full standard histories, not assumed field completions.
std=json.loads((P/'check_single_used_first_circle.json').read_text())['all_standard_stable_histories'];ps=[complex(*q['point'])for q in std];hs=[tuple('NESW'.index(c)for c in q['headings'])for q in std];controls=ref['partial_graph_controls']['proper_standard_subsets'];assert len(controls)==322
for ids in controls:
 CURRENT_POINTS=[ps[i]for i in ids];HH=[hs[i]for i in ids];pts,su,pr,oo,oi,ch,seen=ns['net'](HH);assert len(seen)==sum(map(len,HH))
 for seq in ch:
  old={}
  for (i,j),k in seq:
   p=pts[i]+k*dr
   if p in old:assert j==old[p]+1
   old[p]=j
CURRENT_POINTS=ps;pts,su,pr,oo,oi=graph(hs);assert not oo and not oi and len(su)==104;u=min(su);start=u;k=0;seen=set()
while u not in seen:seen.add(u);u,dk=su[u];k+=dk
assert u==start and len(seen)==104 and k==1;CURRENT_POINTS=None
three=json.loads((P/'one_minimum_three_branches_certificate.json').read_text());rem97={(a,tuple(b))for a,b in three['exact_remaining97_ids']};remaining=rem97-{key};assert len(remaining)==96 and [[a,list(b)]for a,b in sorted(remaining)]==ref['exact_remaining96_coarse_ids'];assert all(a in(5,8,9)for a,b in remaining)
out={'status':'PASS final one-minimum diagonal g8 branch excluded; all such fronts have single-used negative F4 circle,96 necessary interfaces OPEN','bindings':bind,'two_rows':rounds,'terminal_counts':dict(ts),'closed_windings':dict(winds),'largest_selected_derived_bound':largest,'independent_binary_prefix_nodes':visits,'standard_proper_subset_controls':322,'remaining_ids':[[a,list(b)]for a,b in sorted(remaining)],'analytic_review':[
'Fresh independent rank-position binary-prefix generator from the separately signed three-branch audit reconstructs every complete domain in both whole rows and all1312 selected terminal cells. Derived bound42 concerns only the selected cell. Every empty domain is exhaustively empty, not omitted because of a timeout or untested sibling.',
'The final graph is independently rebuilt on an arbitrary supplied set of COMPLETE physical quotient classes. Explicit empty lower cells remain indexed; the unselected upper sibling is ABSENT from that set, hence UNKNOWN. All edges to any unknown class remain open, including zero-source cases; no WHITE/empty/cap condition is assigned outside the known set.',
'Every whole-row pair and every open next parent is propagated exactly. Every terminal word is rejected by its own physical same-cell first-return chain, proper/nonpositive closed event component, or full g8 residue subset contradiction. No Cartesian enumeration of both upper siblings or large discovery scan is used.',
'All116 positive-winding closed components have additional named events outside, which an actual single event orbit cannot leave unvisited. Negative/zero winding contradict positive summed duration independently. The complete104-event standard+1 cycle with no outside events is explicitly retained as valid;322 proper named subsets remain open.',
'Combining exact three other excluded one-minimum IDs with this final ID forces two singleton minimum classes at full diagonal drift2,-2 and g8. Signed mixed-corner theorem with winding erratum then gives an actual single-used F4 departure circle of winding-1; signed cyclic-E exclusion forces at least one quadruple. The22 one-quadruple and74 two-quadruple necessary interfaces remain OPEN. No standard footprint, g>=12, other-drift classification or global capture follows.'
]};S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S),sha(S.with_suffix('.json')))
