"""Exact cube/identity compression of an already frozen global-Q graph.
CLI UNCOMPRESSED_Q_MODEL.json PREFIX. Exhaustively verifies each finite Q relation.
"""
from pathlib import Path
import sys,json,hashlib,collections
src,out=map(Path,sys.argv[1:3]);J=json.loads(src.read_text());assert J['format']=='guarded_reset_global_record_residual_height_bound_v1';B=json.loads(Path(J['base_model_file']).read_text());qb=J['height_bits'];qm=(1<<qb)-1;F=J['initial_height_bound'];cap=J['height_upper_bound'];cache={};C=[]
def cover(values):
 values=set(values);ans=[]
 def go(start,size):
  present=values.intersection(range(start,start+size))
  if not present:return
  if len(present)==size:ans.append([qm^(size-1),start]);return
  go(start,size//2);go(start+size//2,size//2)
 go(0,1<<qb);return ans
for relation in J['geometric_height_relations']:
 key=tuple(map(tuple,relation))
 if key not in cache:
  groups=collections.defaultdict(set)
  for q,q2 in relation:groups[None if q==q2 else q2-F].add(q-F)
  ops=[]
  for dest,vals in groups.items():
   for k,v in cover(vals):ops.append([k,v,0 if dest is None else qm,0 if dest is None else dest])
  actual={(q-F,q2-F)for q,q2 in relation};represented=set()
  for q in range(1<<qb):
   for k,v,c,r in ops:
    if(q&k)==v:represented.add((q,(q&~c)|r))
  assert represented==actual
  cache[key]=ops
 C.append(cache[key])
TT=[];emap=[]
for ti,t in enumerate(B['transitions']):
 ei=B['edge_map'][ti][0]
 for oi,(qk,qv,qc,qr)in enumerate(C[ei]):
  fr,to,k,v,f,c,r,g,a=t;TT.append([fr,to,(k<<qb)|qk,(v<<qb)|qv,f<<qb,(c<<qb)|qc,(r<<qb)|qr,g,a]);emap.append([ti,ei,oi])
N={'format':'guarded_reset_global_record_residual_height_compressed_v1','n':J['n'],'out':J['out'],'start':J['start'],'reentry':[],'transitions':TT,'uncompressed_model_file':str(src.resolve()),'uncompressed_model_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'height_bits':qb,'height_cube_operations':C,'edge_map':emap,'scope':'Exact finite before/after-Q relation, with identity updates kept symbolic and nonidentity target values grouped into disjoint before-Q cubes. Every Q truth table, including unused binary codes, is exhaustively compared to the frozen uncompressed relation.'}
out.with_suffix('.json').write_text(json.dumps(N,separators=(',',':')))
with out.with_suffix('.dat').open('w')as f:
 f.write(f"{N['n']} {N['out']+1} {len(TT)} 0\n");f.write(' '.join(map(str,N['start']))+'\n')
 for t in TT:f.write(' '.join(map(str,t))+'\n')
 f.write('\n')
print(json.dumps({'bits':N['n'],'old_edges':len(J['transitions']),'new_edges':len(TT),'unique_relation_tables':len(cache)}))
