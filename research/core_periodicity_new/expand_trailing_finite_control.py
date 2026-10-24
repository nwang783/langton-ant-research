"""Exact search-only expansion of a trailing finite-domain bitfield into poses.
CLI MODEL.json PREFIX FIELD_BITS CARDINALITY. Starts and every retained transition
must preserve the finite domain. A later certificate can be lifted to the source.
"""
from pathlib import Path
import sys,json,hashlib
src,out=map(Path,sys.argv[1:3]);fb,card=map(int,sys.argv[3:5]);J=json.loads(src.read_text());assert not J['reentry'];n=J['n']-fb;assert n>=0 and 0<card<=1<<fb;cm=(1<<n)-1;fm=(1<<fb)-1;sp,sk,sv=J['start'];assert sk>>n==fm and(sv>>n)<card;T=[];emap=[]
for ei,e in enumerate(J['transitions']):
 p,to,k,v,f,c,r,g,a=e
 for field in range(card):
  if(field&(k>>n))!=(v>>n):continue
  new=((field^(f>>n))&~(c>>n))|((r>>n)&(c>>n));assert 0<=new<card,(ei,field,new)
  T.append([p*card+field,to*card+new,*[x&cm for x in (k,v,f,c,r)],g,a]);emap.append([ei,field,new])
OUT=(J['out']+1)*card;poses=[J['poses'][p]if p<len(J['poses'])else None for p in range(J['out']+1)for field in range(card)];N={'format':'trailing_finite_control_expansion_v1','n':n,'out':OUT,'poses':poses,'points':J.get('points',[])[:n],'start':[sp*card+(sv>>n),sk&cm,sv&cm],'reentry':[],'transitions':T,'base_model_file':str(src.resolve()),'base_model_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'field_bits':fb,'field_cardinality':card,'edge_map':emap,'scope':'Exact state bijection on the inductive finite field domain; remaining bit assignments unchanged. Search optimization, not a stronger ant abstraction.'};out.with_suffix('.json').write_text(json.dumps(N,separators=(',',':')))
with out.with_suffix('.dat').open('w')as f:
 f.write(f"{n} {OUT+1} {len(T)} 0\n");f.write(' '.join(map(str,N['start']))+'\n')
 for t in T:f.write(' '.join(map(str,t))+'\n')
 f.write('\n')
print(json.dumps({'bits':n,'positions':OUT+1,'edges':len(T),'domain':card}))
