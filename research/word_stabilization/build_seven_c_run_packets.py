"""Exploratory exact C-run contraction of the seven-word marker graph.
Every infinite path has this packetization after an initial bounded C run,
because C^5 is physically impossible. Packet ends are followed by a non-C.
"""
from pathlib import Path
import json
from collections import defaultdict
p='shifted1_llrlrrrrlll_fold_coalesced';q=json.load(open(p+'_port_quotient.json'));W=q['macro_words'];A=defaultdict(list)
for u,a,v in q['quotient_edges']:A[u].append((a,v))
paths=[]
for u,a,v in q['quotient_edges']:
 if a==1:continue
 frontier={(v,(a,))}
 for k in range(4):
  nxt=set()
  for z,w in frontier:
   if any(b!=1 for b,y in A[z]):paths.append((u,w,z))
   for b,y in A[z]:
    if b==1:nxt.add((y,w+(1,)))
  frontier=nxt
words=sorted({w for u,w,v in paths},key=lambda w:(sum(len(W[a]['word']) for a in w),w));idx={w:i for i,w in enumerate(words)}
M=[{'word':''.join(W[a]['word']for a in w),'start_marker':W[w[0]]['start_marker'],'end_marker':'LLLLRLRRRRL','source_types':w}for w in words]
result={'source':p,'classes':q['classes'],'macro_words':M,'quotient_edges':sorted({(u,idx[w],v)for u,w,v in paths}),'scope':'Each packet owns a non-C macro and its maximal following C run, at most three C letters; next packet begins non-C.'}
Path('seven_c_run_packets_port_quotient.json').write_text(json.dumps(result,indent=2))
print(len(M),len(result['quotient_edges']),[(i,m['source_types'])for i,m in enumerate(M)])
