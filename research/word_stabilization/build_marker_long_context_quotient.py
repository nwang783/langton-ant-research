from pathlib import Path
from collections import defaultdict
import json,sys
base,out,k=sys.argv[1],sys.argv[2],int(sys.argv[3]);Q=json.load(open(base+'_port_quotient.json'));M=Q['macro_words'];A=defaultdict(list)
for u,a,v in Q['quotient_edges']:A[u].append((a,v))
paths=set()
def rec(v,w):
 if len(w)==k+1:paths.add(w);return
 for a,z in A[v]:rec(z,w+(a,))
for u in A:rec(u,())
D=(1j,1,-1j,-1)
def feasible(t):
 p=0j;h=0;last={}
 for c in ''.join(M[a]['word']for a in t)+M[t[-1]]['end_marker']:
  if last.get(p)==c:return False
  last[p]=c;h=(h+(1 if c=='R'else-1))%4;p+=D[h]
 return True
paths={w for w in paths if feasible(w)};contexts=sorted({w[:-1]for w in paths}|{w[1:]for w in paths});idx={w:i for i,w in enumerate(contexts)}
macros=[{'word':M[w[0]]['word'],'start_marker':M[w[0]]['start_marker'],'end_marker':''.join(M[a]['word']for a in w[1:])+M[w[-1]]['end_marker'],'context':w}for w in contexts]
edges=sorted({(idx[w[:-1]],idx[w[:-1]],idx[w[1:]])for w in paths})
Path(out+'_port_quotient.json').write_text(json.dumps({'macro_words':macros,'quotient_edges':edges,'classes':len(contexts),'context_length':k,'source':base,'scope':'actual overlapping successor contexts; only first raw block is owned'},indent=2));print('contexts',len(contexts),'edges',len(edges))
