"""Packet-DFA low zone as a finite unit push/pop/zero graph, C-age weighted.
CLI DELAYED_GEOMETRY.json PREFIX. This does not build a record exclusion.
"""
from pathlib import Path
import sys,json,hashlib
src,out=map(Path,sys.argv[1:3]);J=json.loads(src.read_text());D=json.loads(Path(J['dfa_file']).read_text());nd=len(D['transitions']);keep=D['keep'];ops={(v[0],v[1]):v for v in J['actions']};nodes=[{'heading':h,'dfa':d}for h in range(4)for d in range(nd)];edges=[];packets=[]
for h in range(4):
 for d,row in enumerate(D['transitions']):
  for k,a in enumerate(keep):
   dd=row[k]
   if dd<0:continue
   v=ops[h,a];c,dq,dh=v[2:5];start=h*nd+d;end=((h+dh)%4)*nd+dd;sgn=0 if dq==0 else(-1 if dq>0 else 1);n=max(1,abs(dq));p=start;ids=[]
   for i in range(n):
    if i==n-1:q=end
    else:q=len(nodes);nodes.append({'packet_source':[h,d,a],'private_step':i+1})
    ids.append(len(edges));edges.append([p,q,sgn,c if i==0 else 0]);p=q
   packets.append({'source':[h,d],'packet':a,'target':[(h+dh)%4,dd],'head_delta':dq,'C_count':c,'unit_edges':ids})
N={'format':'low_height_unit_graph_v1','source_file':str(src.resolve()),'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'dfa_file':J['dfa_file'],'dfa_sha256':J['dfa_sha256'],'original_controls':4*nd,'nodes':nodes,'edges':edges,'packet_expansions':packets,'scope':'Exact unit-chain low-head-height counter graph for the given packet DFA; no high-token resource effects. Push raises depth, pop lowers depth. Weights count C macros, saturated4 only in summary.'};out.with_suffix('.json').write_text(json.dumps(N,separators=(',',':')))
with out.with_suffix('.dat').open('w')as f:
 f.write(f'{len(nodes)} {len(edges)}\n')
 for v in edges:f.write(' '.join(map(str,v))+'\n')
print({'nodes':len(nodes),'original_controls':4*nd,'edges':len(edges)})
