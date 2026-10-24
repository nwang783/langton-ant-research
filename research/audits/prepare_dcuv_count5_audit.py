from pathlib import Path
import json,hashlib
R=Path('/workspace/shared/langton'); A=R/'audits'; F=R/'core_periodicity_new/chronology_dcuv/critical_ucc_count5/frozen_20261023_0813'
manifest=json.loads((F/'manifest.json').read_text())
for f in manifest['files']:
 p=F/f['frozen']; assert len(p.read_bytes())==f['bytes']; assert hashlib.sha256(p.read_bytes()).hexdigest()==f['sha256']
old=json.loads((A/'dcuv_counted_replay/frozen_manifest.json').read_text())
for p,h in old.items(): assert hashlib.sha256((R/p).read_bytes()).hexdigest()==h,p
lit0=(A/'dcuv_counted_replay/literal.input').read_text().split(); lit1=(F/'05_literal8.input').read_text().split(); assert lit1[:len(lit0)]==lit0
base0={tuple(map(int,l.split())) for l in (A/'dcuv_counted_replay/protected.tsv').read_text().splitlines()}
base1={tuple(map(int,l.split()[:7])) for l in (F/'07_protected8.tsv').read_text().splitlines()}; assert base0==base1
assert not (F/'06_ordinary8.tsv').read_bytes()
s=(A/'check_dcuv_counted_protected_independent.cpp').read_text()
replacements=[('r.k>4','r.k>5'),('min(k,4)','min(k,5)'),('return k==4||','return k==5||'),('if(k==4)return true','if(k==5)return true'),('u<=4','u<=5'),('k<=4','k<=5'),('l<=4','l<=5'),('graph[20]','graph[24]'),('for(int k=0;k<4;k++)for(int c=0;c<4;c++)graph','for(int k=0;k<5;k++)for(int c=0;c<4;c++)graph'),('for(int i=0;i<20;i++)for(int v=0;v<20;v++)','for(int i=0;i<24;i++)for(int v=0;v<24;v++)')]
for x,y in replacements:
 assert x in s,x;s=s.replace(x,y)
s=s.replace('// Independent literal least-gap checker for capped-C protected clauses.','// Independent cap-five variant of signed IE checker. Exact counts 0..4, overflow >=5.\n// No generator imports; all literal guards and smaller-actual-gap checks retained.')
(A/'check_dcuv_count5_protected_independent.cpp').write_text(s)
O=A/'dcuv_count5_replay';O.mkdir(exist_ok=True)
meta={'frozen_manifest_sha256':hashlib.sha256((F/'manifest.json').read_bytes()).hexdigest(),'all_frozen_hashes_verified':True,'signed_IE_hashes_verified':True,'literal_words_and_right_markers_equal':True,'signed_protected_base_equal':len(base0),'ordinary_base':0,'changes':replacements,'checker_sha256':hashlib.sha256(s.encode()).hexdigest()}
(O/'inputs.json').write_text(json.dumps(meta,indent=2)+'\n')
print(json.dumps(meta,indent=2))
