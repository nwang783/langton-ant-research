from pathlib import Path
import json,hashlib
from check_dcuv_patch_model_independent import ROOT,raws,mark,walk,rotation,xy
B=ROOT/'core_periodicity_new/young_VC_left_isolation_frozen_20261023_1146';M=json.loads((B/'manifest.json').read_text())
for f in M['files']:assert hashlib.sha256((B/f['file']).read_bytes()).hexdigest()==f['sha256']
J=json.loads((B/'02_young_VC_control_left_isolation.json').read_text());suffix=''.join(raws[a]for a in J['suffix']);rows=[]
for author in J['rows']:
 a=author['predecessor'];e,dh,_,_=walk(raws[a]);h=(-dh)%4;p=-rotation(e,h);assert [*xy(p),h]==author['start_pose']
 seen={};found=None;word=raws[a]+suffix
 for t,c in enumerate(word):
  if p in seen and seen[p][1]==c:
   found={'cell':list(xy(p)),'previous_read':seen[p][0],'conflicting_read':t,'turn':c};break
  seen[p]=(t,c);h=(h+(1 if c=='R'else-1))%4;p+=(1j,1,-1j,-1)[h]
 assert found==author['conflict'];phase=found['conflicting_read']-len(raws[a]);assert phase==author['conflict_suffix_phase']and phase<=138
 rows.append({'predecessor':a,'conflict':found,'suffix_phase':phase})
assert [r['predecessor']for r in rows]==[0,1,4,5,6,7,8,9]
assert len(''.join(raws[a]for a in J['suffix'][:-1]))==127
# U/UC/UCC share the whole final U raw prefix, so each conflict remains.
assert raws[8].startswith(raws[7])and raws[9].startswith(raws[7])
out={'status':'PASS complete eight-predecessor any-board literal obstruction','manifest_sha256':hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),'rows':rows,'latest_final_U_phase':max(r['suffix_phase']for r in rows)-127,'scope':'Fixed funded16-cell suffix has no recurrent-eight left extension; must start such a factor. Not generic young-VC exclusion, new DFA/global record closure, or an obstruction to arbitrary earlier non-language ant history.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
