"""Historical height presence relaxation: deletes and multiplicity are forgotten."""
from pathlib import Path
import sys,json,hashlib
src,out=map(Path,sys.argv[1:3]);J=json.loads(src.read_text());n=len(J['places']);np=len(J['positions']);dummy=np;T=[]
def bits(a):return sum(1<<i for i,x in enumerate(a)if x)
for p,q,a,i,o in J['transitions']:
 k=bits(i);r=bits(o);T.append([p,q,k,k,0,r,r,0,a])
for p,r in J['goal_requirements']:
 k=bits(r);T.append([p,p,k,k,0,0,0,1,-1])
for p in J['initial_controls']:T.append([dummy,p,0,0,0,0,0,0,99])
N={'format':'record_height_historical_presence_v1','n':n,'out':dummy+1,'start':[dummy,(1<<n)-1,0],'reentry':[],'transitions':T,'base_model_file':str(src.resolve()),'base_model_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'height_places':J['places'],'scope':'Historical availability of a height forgets removals and multiplicities, hence overapproximates exact high-height residual counts.'};out.with_suffix('.json').write_text(json.dumps(N,separators=(',',':')))
with out.with_suffix('.dat').open('w')as f:
 f.write(f'{n} {dummy+2} {len(T)} 0\n');f.write(' '.join(map(str,N['start']))+'\n')
 for t in T:f.write(' '.join(map(str,t))+'\n')
 f.write('\n')
print({'bits':n,'positions':dummy+2,'edges':len(T)})
