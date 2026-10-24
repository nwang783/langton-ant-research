"""Project the bounded-core return automaton to turn words, never to profiles."""
from collections import Counter
from pathlib import Path
import json,time
P=Path(__file__).parent;T=json.loads((P/'component_kernel_M7_compact.json').read_text())['transitions'];C=json.loads((P/'cap7_core_certificate.json').read_text());n=C['states'];S=set(C['unique_nonempty_scc']);g0=min(S);cy=C['internal_edge_indices'];inside={T[z]['source']:z for z in cy};adj=[[]for _ in range(n)]
for z,t in enumerate(T):adj[t['source']].append(z)
D=[None]*n;D[0]={'':1};total=1;maxwords=1
for g in reversed(C['condensation_topological_order']):
 if g!=g0:
  out=Counter()
  for z in adj[g]:
   t=T[z]
   for w,a in D[t['target']].items():out[t['turn']+w]+=a
  D[g]=dict(out);total+=len(out);maxwords=max(maxwords,len(out))
 else:
  for root in S:
   out=Counter();u=root;prefix=''
   for k in range(12):
    for z in adj[u]:
     t=T[z];v=t['target']
     if v not in S:
      for w,a in D[v].items():out[prefix+t['turn']+w]+=a
    z=inside[u];prefix+=T[z]['turn'];u=T[z]['target']
   D[root]=dict(out);total+=len(out);maxwords=max(maxwords,len(out))
root=Counter()
for z in adj[0]:
 t=T[z]
 for w,a in D[t['target']].items():root[t['turn']+w]+=a
assert sum(root.values())==C['conditional_empty_return_path_count']
out={'status':'AUTHOR_BOUNDED_CORE_WORD_QUOTIENT_PENDING_AUDIT','first_return_profile_count':sum(root.values()),'distinct_turn_words':len(root),'word_counts':dict(sorted(root.items(),key=lambda x:(len(x[0]),x[0]))),'total_nonterminal_word_entries':total,'maximum_words_at_one_nonterminal':maxwords,'maximum_word_length':max(map(len,root)),'scope':'Exact projection of bounded-core local automaton. Many profiles/words may be physically impossible; no cap7 exit theorem.'}
(P/'cap7_turn_word_quotient.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items()if k!='word_counts'})
