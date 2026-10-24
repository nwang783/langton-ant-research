"""Skip boundaries owning a noncore-marker exit to M/N.
Such skipped blocks cannot be consecutive, so every packet has1 or2 raw blocks.
This is an outgoing-edge cross-section, not a claim of forced exit choice.
"""
from pathlib import Path
from collections import defaultdict
import sys,json
base,out=sys.argv[1:3];q=json.load(open(base+'_port_quotient.json'));M=q['macro_words'];core={'LLLLRLRRRRLR','RRRLLRLLRRRR'};E=[tuple(z)for z in q['quotient_edges']];A=defaultdict(list)
for i,(u,a,v)in enumerate(E):A[u].append(i)
skip=set(map(int,sys.argv[3].split(',')))if len(sys.argv)>3 else{a for a,z in enumerate(M)if z['start_marker']not in core and z['end_marker']in core};ports=[i for i,(u,a,v)in enumerate(E)if a not in skip];pi={u:i for i,u in enumerate(ports)};R=[];types=set()
for i in ports:
 u,a,v=E[i]
 for j in A[v]:
  w,b,z=E[j]
  if b not in skip:
   t=(M[a]['start_marker'],M[b]['start_marker'],M[a]['word']);types.add(t);R.append((i,t,j))
  else:
   for k in A[z]:
    _,c,y=E[k];assert c not in skip
    t=(M[a]['start_marker'],M[c]['start_marker'],M[a]['word']+M[b]['word']);types.add(t);R.append((i,t,k))
T=sorted(types,key=lambda t:(len(t[2]),t));ti={t:i for i,t in enumerate(T)};adj=[[]for _ in ports]
for u,t,v in R:adj[pi[u]].append((ti[t],pi[v]))
cl=[0]*len(ports)
while True:
 sig=[tuple(sorted(set((a,cl[v])for a,v in z)))for z in adj];si={s:i for i,s in enumerate(sorted(set(sig)))};nc=[si[s]for s in sig]
 if len(set(cl))==len(si):cl=nc;break
 cl=nc
edges=sorted({(cl[pi[u]],ti[t],cl[pi[v]])for u,t,v in R});res={'source':base,'skipped_original_types':sorted(skip),'source_edge_ports':ports,'source_port_classes':cl,'macro_words':[{'start_marker':a,'end_marker':b,'word':w}for a,b,w in T],'quotient_edges':edges,'classes':len(si),'scope':'one-or-two-block packets defined by an outgoing-edge cross-section'}
Path(out+'_port_quotient.json').write_text(json.dumps(res,indent=2));print('skipped',sorted(skip),'packets',len(T),'classes',len(si),'edges',len(edges))
