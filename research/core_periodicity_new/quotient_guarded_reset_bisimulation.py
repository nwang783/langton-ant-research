"""Exact reachability bisimulation quotient after all semantic layers are frozen.
CLI MODEL.json PREFIX. Packet labels are deliberately not observable; witnesses
must be lifted through original edges. Any no-hit invariant lifts root-by-class.
"""
from pathlib import Path
import sys,json,subprocess,hashlib
src,out=map(Path,sys.argv[1:3]);B=json.loads(src.read_text());assert not B['reentry'];bin=Path(__file__).with_suffix('');subprocess.run([str(bin),str(src.with_suffix('.dat')),str(out.with_suffix('.dat')),str(out.with_suffix('.map'))],check=True)
a=list(map(int,out.with_suffix('.map').read_text().split()));np,nc,rounds=a[:3];part=a[3:];assert len(part)==np==B['out']+1
x=iter(map(int,out.with_suffix('.dat').read_text().split()));n,cp,nt,nr=[next(x)for _ in range(4)];start=[next(x)for _ in range(3)];T=[[next(x)for _ in range(9)]for _ in range(nt)];assert nr==0 and not list(x) and cp==nc+1 and n==B['n'];assert start==[part[B['start'][0]],*B['start'][1:]]
def sig(t):
 fr,to,k,v,f,c,r,g,a=t
 return(k,v,0 if g else f,0 if g else c,0 if g else r,g,-1 if g else part[to])
old=[set()for _ in range(np)];new=[set()for _ in range(nc+1)]
for t in B['transitions']:old[t[0]].add(sig(t))
for fr,to,k,v,f,c,r,g,a in T:new[fr].add((k,v,f,c,r,g,-1 if g else to))
assert not new[-1]
for s in range(np):assert old[s]==new[part[s]],s
N={'format':'exact_guarded_reset_bisimulation_quotient_v1','n':n,'out':nc,'start':start,'reentry':[],'transitions':T,'base_model_file':str(src.resolve()),'base_model_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'original_to_class':part,'refinement_rounds':rounds,'scope':'Exact strong control bisimulation for guarded-reset reachability. Complete outgoing operation/class sets agree for EVERY old position. Packet labels and irrelevant goal updates are omitted observations; physical witnesses require lifting, while no-hit BDD roots lift by original_to_class.'};out.with_suffix('.json').write_text(json.dumps(N,separators=(',',':')));print('PASS every original outgoing operation/class set exactly matches its quotient class')
