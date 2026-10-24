from pathlib import Path
import json,hashlib
from collections import Counter
P=Path(__file__);R=P.parent.parent;S=R/'second_ordinary_after_first_foreign_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();mf=S/'remaining_92_angles_manifest.json';assert sha(mf)=='ef36a0afc4a7cdbcf3dff24c2d89a4e864287ad5ce46c9269d1a1b191d426956';m=json.loads(mf.read_text())
for f,h in m['files'].items():assert sha(S/f)==h
for f,h in m['dependencies'].items():assert sha(R/f)==h
angles=json.loads((S/'small_second_ordinary_geometry.json').read_text())['conditional217_old_source_angle_interfaces'];ref=json.loads((S/'remaining_92_angles.json').read_text());key=lambda x:json.dumps(x,sort_keys=True);assert len(angles)==len(set(map(key,angles)))==217
parts=[[],[],[],[]]
for a in angles:
 s=a['old_source'];n=a['actual_old_source_to_FOREIGN_C_age'];parts[0 if s=='U'else 1 if n==0 else 2 if n==1 else 3].append(a)
assert list(map(len,parts))==[60,17,48,92]and all(a['old_source']in'DV'for a in parts[1])and all(a['old_source']in'DCV'for a in parts[2])
assert list(map(key,parts[3]))==list(map(key,ref['exact_remaining92_angular_interfaces']))
assert Counter(a['old_source']for a in parts[3])=={'D':28,'C':28,'V':36}
for a in parts[3]:
 n=a['actual_old_source_to_FOREIGN_C_age'];assert 2<=n<=4
 if a['old_source']in'DC':assert n<=3
 if n==4:assert a['old_source']=='V'and a['first_ordinary']!='C'and a['second_ordinary']in'DC'
assert len(ref['all217_original_angles_with_disjoint_source_status'])==217 and [r['angle']for r in ref['all217_original_angles_with_disjoint_source_status']]==angles
out={'status':'PASS dependency-only217=60+17+48+92 angular partition','manifest_sha256':sha(mf),'dependencies':m['dependencies'],'counts':list(map(len,parts)),'remaining_by_source':dict(Counter(a['old_source']for a in parts[3])),'analytic_review':['The original signed217 angle rows are distinct and unchanged. Source-U closure covers all60; exact n=0 oldDV slice covers17; separate genuine D/C/V atomic-age1 proofs cover48 with their own source/full-tail clocks. C2 full age differs from selected atomic age and remains qualified by its signed proof.','Old-D/V positive finite words can contain later U, but their natural reverse closures exclude U BEFORE selected source only. The source here lies in the original genuine U-start old factor, so those scoped exclusions apply. OldV mandatory b6642b71 is bound.','The remaining92 are angular possibilities, not92 physical configurations or realizable histories. Epoch lengths remain unbounded. No generic second simplicity, later ordinary atom, foreign iteration, or new geometric theorem is inferred.']};P.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(sha(P),sha(P.with_suffix('.json')))
