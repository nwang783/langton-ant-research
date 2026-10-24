"""Conservative upward rounding of the global residual-height bound Q.
CLI EXACT_Q_MODEL.json PREFIX comma,separated,increasing,Q,values.
Chosen values include the initial F and universal output-height cap.
"""
from pathlib import Path
import json,sys,hashlib,collections,bisect
src,out=map(Path,sys.argv[1:3]);J=json.loads(src.read_text());assert J['format']=='guarded_reset_global_record_residual_height_bound_v1';B=json.loads(Path(J['base_model_file']).read_text());vals=list(map(int,sys.argv[3].split(',')));assert vals==sorted(set(vals));assert vals[0]==J['initial_height_bound']and vals[-1]==J['height_upper_bound'];qb=max(1,(len(vals)-1).bit_length());qm=(1<<qb)-1;ix={q:i for i,q in enumerate(vals)};tables=[];ops=[];cache={}
def cover(S):
 S=set(S);ans=[]
 def go(l,n):
  s=S.intersection(range(l,l+n))
  if not s:return
  if len(s)==n:ans.append([qm^(n-1),l]);return
  go(l,n//2);go(l+n//2,n//2)
 go(0,1<<qb);return ans
for R in J['geometric_height_relations']:
 key=tuple(map(tuple,R))
 if key not in cache:
  table=sorted({(ix[q],bisect.bisect_left(vals,q2))for q,q2 in R if q in ix});groups=collections.defaultdict(set)
  for q,q2 in table:groups[None if q==q2 else q2].add(q)
  O=[]
  for to,S in groups.items():
   for k,v in cover(S):O.append([k,v,0 if to is None else qm,0 if to is None else to])
  represented={(q,(q&~c)|r)for q in range(1<<qb)for k,v,c,r in O if(q&k)==v};assert represented==set(table)
  cache[key]=(table,O)
 table,O=cache[key];tables.append(table);ops.append(O)
TT=[];emap=[]
for ti,t in enumerate(B['transitions']):
 ei=B['edge_map'][ti][0]
 for oi,(qk,qv,qc,qr)in enumerate(ops[ei]):
  fr,to,k,v,f,c,r,g,a=t;TT.append([fr,to,(k<<qb)|qk,(v<<qb)|qv,f<<qb,(c<<qb)|qc,(r<<qb)|qr,g,a]);emap.append([ti,ei,oi])
N={'format':'guarded_reset_global_record_residual_height_coarse_v1','n':B['n']+qb,'out':B['out'],'start':[B['start'][0],(B['start'][1]<<qb)|qm,B['start'][2]<<qb],'reentry':[],'transitions':TT,'exact_height_model_file':str(src.resolve()),'exact_height_model_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'height_values':vals,'height_bits':qb,'color_bit_shift':qb,'geometric_height_relations':tables,'height_cube_operations':ops,'edge_map':emap,'scope':'Q remains an upper bound but rounds each max(Q,new output heights) upward to the next finite grid value. Input upper-bound guards and all underlying spatial/color/record/funding rules remain. Exact finite coarse relation tables are cubically compressed and exhaustively checked.'}
out.with_suffix('.json').write_text(json.dumps(N,separators=(',',':')))
with out.with_suffix('.dat').open('w')as f:
 f.write(f"{N['n']} {N['out']+1} {len(TT)} 0\n");f.write(' '.join(map(str,N['start']))+'\n')
 for t in TT:f.write(' '.join(map(str,t))+'\n')
 f.write('\n')
print(json.dumps({'bits':N['n'],'Q_bits':qb,'height_values':vals,'edges':len(TT)}))
