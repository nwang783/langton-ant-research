"""Exact low-height unit graph with packet transverse displacement modulo4.

Every nonzero-height unit edge receives odd transverse residue. Thus every
balanced unit path has even residue, including paths at private chain nodes.
CLI DELAYED_GEOMETRY.json PREFIX.
"""
from pathlib import Path
import sys,json,hashlib
src,out=map(Path,sys.argv[1:3]);J=json.loads(src.read_text());D=json.loads(Path(J['dfa_file']).read_text());G=json.loads(Path(D['geometry_file']).read_text())['geometry'];nd=len(D['transitions']);keep=D['keep'];phase=J['phase'];ops={(v[0],v[1]):v for v in J['actions']}
def rot(p,h):x,y=p;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
def transverse(p):x,y=rot(p,phase);return x-y
nodes=[dict(heading=h,dfa=d)for h in range(4)for d in range(nd)];edges=[];packets=[]
for h in range(4):
 for d,row in enumerate(D['transitions']):
  for k,a in enumerate(keep):
   dd=row[k]
   if dd<0:continue
   v=ops[h,a];c,dq,dh=v[2:5];dt=transverse(rot(G[a]['endpoint'][:2],h));assert(dq-dt)%2==0
   start=h*nd+d;end=((h+dh)%4)*nd+dd;sgn=0 if dq==0 else(-1 if dq>0 else 1);n=max(1,abs(dq));p=start;ids=[]
   for i in range(n):
    q=end if i==n-1 else len(nodes)
    if i<n-1:nodes.append(dict(packet_source=[h,d,a],private_step=i+1))
    tr=(dt-(n-1))%4 if i==n-1 else 1
    assert(tr-sgn)%2==0
    ids.append(len(edges));edges.append([p,q,sgn,c if i==0 else 0,tr]);p=q
   assert sum(edges[e][4]for e in ids)%4==dt%4
   packets.append(dict(source=[h,d],packet=a,target=[(h+dh)%4,dd],head_delta=dq,transverse_delta=dt,C_count=c,unit_edges=ids))
N=dict(format='low_height_residue_unit_graph_v1',source_file=str(src.resolve()),source_sha256=hashlib.sha256(src.read_bytes()).hexdigest(),dfa_file=J['dfa_file'],dfa_sha256=J['dfa_sha256'],geometry_file=D['geometry_file'],geometry_sha256=D['geometry_sha256'],original_controls=4*nd,transverse_modulus=4,nodes=nodes,edges=edges,packet_expansions=packets,scope='Private monotone unit expansion of the exact packet-DFA low counter. Whole-packet transverse displacement is exact modulo4. Unit transverse parity equals unit counter parity, hence every balanced path has residue0 or2. Intermediate transverse assignments are bookkeeping only; original-to-original paths are complete packet paths.')
out.with_suffix('.json').write_text(json.dumps(N,separators=(',',':')))
with out.with_suffix('.dat').open('w')as f:
 f.write(f'{len(nodes)} {len(edges)}\n')
 for e in edges:f.write(' '.join(map(str,e))+'\n')
print(dict(nodes=len(nodes),original_controls=4*nd,edges=len(edges),residue_modulus=4,balanced_profiles=2))
