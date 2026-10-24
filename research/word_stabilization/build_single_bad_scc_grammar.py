import json,collections,sys
from pathlib import Path
sys.setrecursionlimit(100000)
M=json.load(open('spaced_two_marker_macros.json'))['macros'];Q=json.load(open('spaced_two_marker_port_quotient.json'));good={i for i,z in enumerate(M)if not z['K_end_indices']};E=[(u,a,v)for u,a,v in Q['quotient_edges']if a in good|{57}];A=collections.defaultdict(list);R=collections.defaultdict(list)
for u,a,v in E:A[u].append((a,v));R[v].append(u)
seen=set();order=[]
def dfs(u):
 if u in seen:return
 seen.add(u)
 for a,v in A[u]:dfs(v)
 order.append(u)
for u in range(Q['classes']):dfs(u)
comp={};groups=[]
def rev(u,i):
 if u in comp:return
 comp[u]=i;groups[i].append(u)
 for v in R[u]:rev(v,i)
for u in reversed(order):
 if u not in comp:groups.append([]);rev(u,len(groups)-1)
i=next(comp[u]for u,a,v in E if a==57 and comp[u]==comp[v]);vertices=set(groups[i]);EE=[(u,a,v)for u,a,v in E if u in vertices and v in vertices];AA=collections.defaultdict(list)
for u,a,v in EE:AA[u].append((a,v))
pairs=set();triples=set()
for u,a,v in EE:
 for b,w in AA[v]:
  pairs.add((a,b))
  for c,z in AA[w]:triples.add((a,b,c))
out={'vertices':sorted(vertices),'edges':EE,'alphabet':sorted({a for u,a,v in EE}),'pairs':sorted(pairs),'triples':sorted(triples)};Path('single_bad57_scc_grammar.json').write_text(json.dumps(out,indent=2));print('vertices',len(vertices),'edges',len(EE),'pairs',len(pairs),'triples',len(triples),'alphabet',out['alphabet'])
