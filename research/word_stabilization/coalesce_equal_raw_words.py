from pathlib import Path
from collections import defaultdict
import json,sys,os
base,out=sys.argv[1:3];q=json.load(open(base+'_port_quotient.json'));old=q['macro_words'];W=sorted({z['word']for z in old},key=lambda s:(len(s),s));wi={w:i for i,w in enumerate(W)};groups=[[i for i,z in enumerate(old)if z['word']==w]for w in W]
M=[{'word':w,'start_marker':os.path.commonprefix([old[i]['start_marker']for i in g]),'end_marker':os.path.commonprefix([old[i]['end_marker']for i in g])}for w,g in zip(W,groups)]
A=defaultdict(list)
for u,a,v in q['quotient_edges']:A[u].append((wi[old[a]['word']],v))
vertices=sorted(A);vi={u:i for i,u in enumerate(vertices)};cl=[0]*len(vertices)
while True:
 sig=[tuple(sorted(set((a,cl[vi[v]])for a,v in A[u])))for u in vertices];si={s:i for i,s in enumerate(sorted(set(sig)))};nc=[si[s]for s in sig]
 if len(set(cl))==len(si):cl=nc;break
 cl=nc
edges=sorted({(cl[vi[u]],a,cl[vi[v]])for u in vertices for a,v in A[u]});r={'source':base,'source_type_groups':groups,'source_vertices':vertices,'source_vertex_classes':cl,'macro_words':M,'quotient_edges':edges,'classes':len(si),'scope':'same raw words coalesced; actual right marker replaced only by common guaranteed prefix'}
Path(out+'_port_quotient.json').write_text(json.dumps(r,indent=2));print('raw types',len(M),'classes',len(si),'edges',len(edges));print([(i,len(z['word']),z['word'],z['end_marker'])for i,z in enumerate(M)])
