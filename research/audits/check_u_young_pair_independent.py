"""Literal reconstruction of young U pair producers and full positive identities."""
from pathlib import Path
import json,hashlib
from check_dcuv_patch_model_independent import ROOT,raws,mark,walk,rotation,xy
B=ROOT/'core_periodicity_new/u_young_pair_frozen_20261023_1025';j=json.loads((B/'02_u_young_lower_pair.json').read_text());m=json.loads((B/'manifest.json').read_text())
for f in m['files']:assert hashlib.sha256((B/f['file']).read_bytes()).hexdigest()==f['sha256']
for f in m['dependencies']:assert hashlib.sha256((ROOT/'core_periodicity_new'/f['file']).read_bytes()).hexdigest()==f['sha256']
ids=(0,1,4,5,6,7,8,9);cc={a:c for a,c in zip(ids,(0,1,0,1,2,0,1,2))};mapping={a:i for i,a in enumerate(ids)};K={z for z,b in walk(mark)[2].items()if b};G={}
for a in ids:
 end,h,_,flip=walk(raws[a]);req=walk(raws[a]+mark)[2];black={z for z,b in req.items()if b};postcore={end+rotation(z,h)for z in K};O=(black^flip)-postcore
 G[a]=(black-K,sorted(O,key=xy),req,end,h)
q=-1+2j;a=-1+1j;upper={-1+4j,2j,3j}
def at(z,protected):
 result=[]
 for b in ids:
  I,O,req,end,hh=G[b]
  for oi,o in enumerate(O):
   p=z-rotation(o,3)
   if(sum(xy(p))+3)%2:continue
   if any(rotation(x-p,-3)in req for x in protected):continue
   output={p+rotation(x,3)for x in O}
   result.append(dict(packet=b,head=[*xy(p),3],output_slot=oi,other_lower_is_output=a in output,exit=[*xy(p+rotation(end,3)),(3+hh)%4]))
 return result
Q=at(q,upper);Qzero=[r for r in Q if cc[r['packet']]==0];A=at(a,upper|{q});same=[r for r in Q if r['other_lower_is_output']]
assert Qzero==j['q_zero_C_producers']and A==j['a_producers_avoiding_q_and_uppers']and same==j['same_birth_candidates']
assert all(r['head']==[-1,0,3]for r in Qzero)and max(r['exit'][0]for r in Qzero)==-2
assert len(A)==11 and min(r['head'][0]for r in A)==0
for b in ids:
 if cc[b]==0:assert rotation(G[b][3],3).real<=0 and G[b][4]==0
closure=ROOT/'core_periodicity_new/chronology_dcuv/critical_ucc_count5/frozen_20261023_0813/01_closure.tsv';C={tuple(map(int,l.split()[:8]))for l in closure.read_text().splitlines()}
for r in j['signed_count3_queries']:
 source=r['source'];consumer=r['consumer'];out=tuple(r['source_output']);key=(mapping[source],mapping[consumer],0,-1,1,*out,3)
 assert list(key)==r['tuple']and(key in C)==r['excluded']==(source in(7,8,9))
controls=[]
for record in j['controls']:
 seed={complex(*z)for z in record['initial_black_cells']};assert len(seed)==11 and seed==K|{3j,1+2j,-1+2j,4,2-1j,3-1j}
 board=set(seed);res={z:('entry',None)for z in seed-K};p=0j;h=0;clock=0;t=0;boundaries=[];births={}
 for index,b in enumerate(record['word']):
  I,O,req,end,dh=G[b];inputs={p+rotation(z,h)for z in I};core={p+rotation(z,h)for z in K}
  assert set(res)==board-core and core<=board and all((p+rotation(z,h)in board)==color for z,color in req.items())
  if index==3:
   assert(p,h)==(-1j,1)
   lower=[p+rotation(z,h)for z in(q,a)];up={p+rotation(z,h)for z in upper}
   assert set(lower)=={1,2}and up=={4,2-1j,3-1j}
   assert all(res[z][0]==0 and clock-res[z][1]==3 for z in lower)
   assert all(res[z][0]=='entry'for z in up)
  for z in inputs:assert z in res;del res[z]
  outputs={p+rotation(z,h)for z in O}
  for z in outputs:assert z not in res;res[z]=(index,clock)
  for ch in raws[b]:
   actual='L'if p in board else'R';assert actual==ch
   board.symmetric_difference_update({p});h=(h+(-1 if actual=='L'else 1))%4;p+=(1j,1,-1j,-1)[h];t+=1
  clock+=cc[b];boundaries.append([t,*xy(p),h,len(board)])
  assert set(res)==board-{p+rotation(z,h)for z in K}
 assert boundaries==record['raw_boundaries']and t==record['raw_length']
 for ch in mark:
  assert('L'if p in board else'R')==ch;board.symmetric_difference_update({p});h=(h+(-1 if ch=='L'else 1))%4;p+=(1j,1,-1j,-1)[h]
 controls.append({'word':record['word'],'raw_length':t,'raw_plus_marker':t+len(mark),'lower_exact_age':3,'upper_entry_identity_count':3})
out={'status':'PASS independent producer geometry, signed queries and actual identity-aware positive controls','q_zero_C_producers':Qzero,'later_a_producers':len(A),'same_birth_candidates':[r['packet']for r in same],'surviving_sources':[4,5,6],'counted_queries':len(j['signed_count3_queries']),'physical_controls':controls,'manifest_sha256':hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),'scope':'Necessary same-V-family source classification at lower-q C-age3. Age3 is actually attained; no raised individual minimum or U budget.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
