from pathlib import Path
from collections import Counter
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'global_attraction_bridge_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();mf=D/'LEAF_PREDECESSOR_OBSTRUCTION_MANIFEST.json';assert sha(mf)=='38ad7337b9b99fdfacaaf3edc7dfa0352671125fb3773f63f19ed046c6d0127a';m=json.loads(mf.read_text())
for f,h in m['files'].items():assert sha(D/f)==h
for f,h in m['dependencies'].items():assert sha(D/f)==h
J=json.loads((D/'LEAF_PREDECESSOR_OBSTRUCTION_CHECKED.json').read_text());SRC=json.loads((D/'WHOLE_LAST_EXIT_RENEWAL_CHECKED.json').read_text());ns={'__file__':str(S.with_name('check_phase13_double_scatter_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Canonical source')[0],ns);sim,xy=ns['sim'],ns['xy'];summary=[]
for row in J['cases']:
 src=next(z for z in SRC['cases']if z['name']==row['case']);s,t=row['start'],row['end'];seed={complex(*p)for p in src['seed']};z=sim(seed,t+1,0j,1,expected=src['full_turn_word'][:t+1],cuts={s,t});SB,sp,sh=z['snap'][s];TB,tp,th=z['snap'][t];last={};vis={}
 for i in range(s,t):q=z['pts'][i];last[q]=i;vis.setdefault(q,[]).append([i,z['word'][i]])
 assert tp not in last and xy(tp)==row['interval_tree_root'];tree={q:z['pts'][i+1]for q,i in last.items()};ind=Counter(tree.values());leaves={q for q in last if ind[q]==0};C=set(SB)&set(last);O=set(TB)&set(last);marked=C|O;f={}
 for q,i in last.items():
  if i==s:continue
  u=z['pts'][i-1]
  if last[u]>i:f[q]=u;assert tree[u]!=q
 assert len(f)==len(set(f.values()))and all(q in f or last[q]==s for q in leaves);assert hashlib.sha256(json.dumps([[xy(p),xy(q)]for p,q in sorted(f.items(),key=lambda kv:(kv[0].real,kv[0].imag))]).encode()).hexdigest()==row['inversion_map_sha256']
 bad=[]
 for v in leaves-marked:
  q=v;chain=[]
  while q not in marked and q in f:chain.append(q);q=f[q]
  if q not in marked:bad.append((v,chain,q))
 assert(len(last),len(leaves),len(leaves-marked),len(bad),len(f))==(row['read_vertices'],row['leaf_count'],row['unmarked_leaves'],row['unmarked_leaf_starts_ending_unmarked'],row['inversion_map_size'])
 for ex in row['selected_examples']:
  v=complex(*ex['start']);q=v;chain=[]
  while q not in marked and q in f:chain.append(q);q=f[q]
  assert q not in marked and v in leaves and xy(q)==ex['terminal'];nodes=[]
  for a in chain+[q]:
   i=last[a];u=z['pts'][i-1]if i>s else None;assert a not in SB and a not in TB and vis[a][0][1]=='R'and vis[a][-1][1]=='L';nodes.append(dict(cell=xy(a),is_tree_leaf=a in leaves,tree_indegree=ind[a],actual_reads=vis[a],last_predecessor=xy(u)if u is not None else None,predecessor_last_read=last[u]if u is not None else None,last_tree_edge=xy(tree[a])))
  assert nodes==ex['nodes'];assert ex['terminal_last_arrival_is_tree_edge']==(u is not None and tree[u]==q and last[u]==last[q]-1)
 assert hashlib.sha256(json.dumps([[xy(q),i]for q,i in sorted(SB.items(),key=lambda kv:(kv[0].real,kv[0].imag))]).encode()).hexdigest()==row['full_input_hash'];assert hashlib.sha256(json.dumps([[xy(q),i]for q,i in sorted(TB.items(),key=lambda kv:(kv[0].real,kv[0].imag))]).encode()).hexdigest()==row['full_output_hash'];summary.append(dict(name=row['case'],start=s,end=t,leaves=len(leaves),unmarked=len(leaves-marked),unmarked_ending_starts=len(bad),injective_map=len(f),selected_examples=row['selected_examples']))
O=dict(status='PASS fresh-root last-predecessor partial injection and literal failures of direct terminal resource charging; numerical leaf budget remains open',manifest=sha(mf),script=sha(S),cases=summary,analytic_review=[
'With a fresh unread endpoint every lastarrivalpredecessor of a readvertex is itself read and has a selected last-exit edge. If its lasttime is later, that selectededge differs from the edge into the vertex. Fixedsector gives exactlytwo outgoingneighbors, so the partialmap is injective on its ENTIREdomain, not just leaves. Lasttimes increase and chains terminate. An arbitraryold root lacks the selectededge and is an actual exception, excluded here.',
'Every treeleaf belongs to the domain except a possible initialcutlastread. Images neednotbenonleaves; two unmarkedleaves can lie on one chain even though chainsdo notmerge. The explicit MTchain57427->71738->71753 ends at an unmarked indegree2vertex. Empty/MTotherchains stop at unmarked indegree1vertices. Thus directterminalassignment is neither a guaranteedresourcehit nor injective on leaves.',
'Both intervaltrees and fullbefore/afterfields freshly replayed from ORIGINALempty/MT100seeds, with all displayed visits/owners and hashes. Counts1 and275 are starting leaves ending unmarked, not distinct terminals or independent debts. The intervalresettrees are not confused with wholehistoricaltrees.',
'No counterexample to leaf<=C+O+1, gross outputpayment or a more globalsubtreepotential is claimed. This only rejects the specified direct-chain proof mechanism; universal attraction remainsopen.'])
S.with_suffix('.json').write_text(json.dumps(O,indent=2)+'\n');print(O['status']);print([(r['name'],r['leaves'],r['unmarked'],r['unmarked_ending_starts'])for r in summary]);print(sha(S.with_suffix('.json')))
