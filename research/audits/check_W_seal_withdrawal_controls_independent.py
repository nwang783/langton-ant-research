from pathlib import Path
import json,hashlib
SELF=Path(__file__).resolve();ROOT=SELF.parents[1];ns={'__file__':str(SELF)};exec((SELF.parent/'check_foreign_kinked_barrier_turn_independent.py').read_text().split('geometries=[]')[0],ns);walk,W,M,xy=[ns[x]for x in('walk','W','M','xy')]
D=ROOT/'seven_word_spatial_return_2026-10-23';ref=json.loads((D/'ordered_W_seal_withdrawal_controls.json').read_text());results=[]
for row,seq,tag,expected in zip(ref['controls'],['UVVCCVV','UVCCVV'],[5j,-1+2j],[[(39,'R'),(131,'L')],[(13,'L'),(21,'R'),(113,'L')]]):
 word=''.join(W[x]for x in seq);tr=walk(word+M);assert tr['feasible'];seed={q for q,b in tr['req'].items()if b};assert sorted(map(xy,seed))==list(map(tuple,row['complete_finite_seed']))
 B=set(seed);p=0j;h=0;owned=[]
 for t,c in enumerate(word+M):
  assert(p in B)==(c=='L')
  if p==tag:owned.append((t,c))
  if t==len(word):assert tag in B
  B.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p+=1j*(-1j)**h
 assert owned==expected and owned[-1][0]==len(word)+1
 assert [*xy(p),h]==row['after_actual_M11']['pose']and len(B)==row['after_actual_M11']['mass']
 results.append({'raw_labels':seq,'mass':len(seed),'tag':xy(tag),'read_history':owned,'raw_length':len(word),'retirement_owner':'following-word RAW phase2, not final plain V RAW'})
mp=D/'ordered_W_seal_withdrawal_controls_manifest.json';mh=hashlib.sha256(mp.read_bytes()).hexdigest();assert mh=='e1ec487ac011d317dd3bb6d2beef5ae53740c213bbcedaca2ab254b8bc61f570'
for f,h in json.loads(mp.read_text())['files'].items():assert hashlib.sha256((D/f).read_bytes()).hexdigest()==h
out={'status':'PASS exact two genuine U-entry controls and withdrawal; 6ea48d5 remains NOT PASSED','manifest_sha256':mh,'controls':results,'analytic':'Both complete minimal finite boards execute their actual full words and marker. The old plain V A and plain U recycled q really survive to the final V residual input at source age2, then retire at the following-word phase2. The missing arbitrary S run invalidates the proposed ownership exclusion. These controls do not attain the narrower foreign endpoint, and do not refute all possible replacement seals. Earlier matching and bottleneck remain unchanged.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
