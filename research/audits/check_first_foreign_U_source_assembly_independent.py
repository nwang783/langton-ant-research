from pathlib import Path
from collections import Counter
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'seven_word_spatial_return_2026-10-23'
P=json.loads((D/'foreign_first_contact_interface.json').read_text());T=json.loads((D/'foreign_tail_first_contact.json').read_text());author=json.loads((D/'first_foreign_U_source_exclusion.json').read_text())
rows=[]
for name,rs in P['U_source_star_filters'].items():
 for r in rs:
  for n,b in zip(r['permitted_C_ages'],r['preceding_C_bits']):rows.append(('prefix',name,tuple(r['foreign_pose']),n,b,r['reason']))
for name,rs in T['U_source_filters'].items():
 for r in rs:
  for n,b in zip(r['permitted_C_ages'],r['preceding_C_bits']):rows.append(('tail',name,tuple(r['foreign_pose']),n,b,r['context_reason']))
assert len(rows)==144 and len(set(rows))==144
expected={('prefix','F',(-2,3,3),1):'early star',('prefix','F',(1,3,0),4):'cut impossible',('prefix','Q',(1,3,0),4):'cut impossible',('prefix','B',(1,3,0),4):'cut impossible',('prefix','F',(2,4,0),4):'forced preceding C',('prefix','Q',(2,4,0),4):'forced preceding C',('prefix','F',(3,3,0),4):'actual renewal and common bud',('tail','Q',(-4,3,3),1):'early star',('tail','B',(2,6,0),0):'early star',('tail','B',(-5,2,3),1):'early star',('tail','B',(-3,6,3),1):'original q survives to2',('tail','B',(3,0,1),3):'all-age B core guardian'}
counts=Counter();remaining=[]
for piece,name,p,n,b,ctx in rows:
 if ctx!='unexcluded_necessary_interface':counts['actual complete-context conflict']+=1
 elif b:counts['actual preceding-C pair conflict']+=1
 else:
  key=(piece,name,p,n);assert key in expected;remaining.append((key,expected[key]));counts['signed preforeign history cut']+=1
assert counts=={'actual complete-context conflict':120,'actual preceding-C pair conflict':12,'signed preforeign history cut':12}and{r[0]for r in remaining}==set(expected)
manifest=D/'first_foreign_U_source_exclusion_manifest.json';sha=hashlib.sha256(manifest.read_bytes()).hexdigest();assert sha=='18c60b120c83069c2f39901c0c5289ad89d0600d919e0d3e223a26d88df7ca4d'
for name,value in json.loads(manifest.read_text())['files'].items():assert hashlib.sha256((D/name).read_bytes()).hexdigest()==value
for name,value in author['dependencies'].items():assert hashlib.sha256((R/name).read_bytes()).hexdigest()==value
out={'status':'PASS all144 labelled U-source first-foreign contact cases closed by signed exact dependencies','manifest_sha256':sha,'counts':dict(counts),'twelve_history_cuts':remaining,'analytic':['The old U-entry complete-eight path is simple. A chronological first appended-proxy contact permits the signed local Jordan catalogue for its outgoing earlier source atom, including endpoint assignment and the exact Q/U collinear onset.','Every earlier U atom is the base of a genuine U-family full producer. Its original tags and full-source clock are retained; optional C tails are not reset. The target is the first foreign after an actual complete-eight packet boundary.','The literal24 pair theorem sets the actual preceding-C bit to0, without discarding the C-to-F wrap in other languages. Actual context removes120 labels, this pair obstruction12, and the explicitly age-matched signed history cuts12.','All renewal and permanence assertions apply before foreign entry only. Marker-owned foreign inputs are never mislabelled RAW retirements.','The conclusion concerns the FIRST new contact only: if an earlier D/C/V contact occurs, this theorem says nothing about a subsequent contact with an old U chord.'],'scope':'Only outgoing U-source first contact excluded. D/C/V-source interfaces, global proxy simplicity, seven-word coverage and universal capture remain open.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(counts)
