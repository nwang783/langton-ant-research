from pathlib import Path
import hashlib,json
from check_dcuv_patch_model_independent import ROOT,raws,mark,walk,rotation,xy
SELF=Path(__file__).resolve();B=ROOT/'core_periodicity_new/U_q_source_history_frozen_20261023_2027';man=json.loads((B/'manifest.json').read_text())
for r in man['files']:assert hashlib.sha256((B/r['file']).read_bytes()).hexdigest()==r['sha256']
assert walk(raws[8])[:2]==(5j,3);assert walk(raws[9])[:2]==(-1+5j,2)
W={s:xy(rotation(walk(raws[s])[0],3))for s in(0,4,7)};C={s:xy(rotation(walk(raws[s])[0],3))for s in(1,5,8)};S={s:xy(rotation(walk(raws[s])[0],2))for s in(0,4,7)}
assert [W[s][0]for s in(0,4,7)]==[-1,-3,-4];assert[C[s][0]for s in(1,5,8)]==[-2,-4,-5];assert[S[s][0]for s in(0,4,7)]==[-1,-1,0];assert all(y<0 for x,y in S.values())
# Direct literal compatibility of the immediate sharp UCC,V and UCC,VC pairs.
for a in(4,5):walk(raws[9]+raws[a]+mark)
# Original U1 candidate UC at(1,7,S), tail output(2,5) feeds q(-1,2).
p=1+7j;assert p+rotation(2+5j,2)==-1+2j
sib=p+rotation(-1+2j,2);assert sib==2+5j
req=walk(raws[7]+mark)[2];assert sib in req and not req[sib]
out=dict(status='PASS UC q permanence and UCC immediate V/VC q retirement',manifest_sha256=hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),UC_exit=[0,5,3],UCC_exit=[-1,5,2],W_zero_displacements=W,W_one_C_displacements=C,S_zero_displacements=S,U1_sibling_white=xy(sib),analytic='Signed exact q-consumer law fixes V/VC(-1,5,S) at full-source age2. UC exits0,5W atclock1; remaining complete intermediates have W-zero, exactlyone DC/VC/UC, S-zero form. Their x displacement<=-2 cannot equal-1. UCC already exits at the target pose and clock; any nonempty S-zero run strictly lowers y, so the consumer must immediately follow. This uses full source-entry clocks, not internal installation clocks.',scope='UC q genuine identity permanent only within retained factor; UCC q possible only immediate V/VC, not all UCC-output permanence. No plain-U q permanence or funding-case closure.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
