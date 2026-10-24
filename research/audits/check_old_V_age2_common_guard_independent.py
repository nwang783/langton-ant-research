from pathlib import Path
from fractions import Fraction as F
import json,hashlib
P=Path(__file__);R=P.parent.parent;D=R/'old_V_age2_common_port_guard_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();mf=D/'manifest.json';assert sha(mf)=='94150227df6389a917b04f25d8fa9eda591ead92f61bacc6d813eb54c36766df';m=json.loads(mf.read_text())
for f,h in m['files'].items():assert sha(D/f)==h
ref=json.loads((D/'common_port_guard.json').read_text())
for f,h in ref['dependencies'].items():assert sha(R/f)==h
bp=P.with_name('check_old_V_second_age1_independent.py');ns={'__file__':str(bp)};exec(bp.read_text().split('# Universal')[0],ns);W,M,K,tr,rot,xy,center,cross=[ns[k]for k in('W','M','K','tr','rot','xy','center','cross')];raw=lambda s:''.join(W[a]for a in s)
for src in('V','VC','VCC'):
 t=tr(raw(src));assert t['last'][2+0j]==('R',8)and 2+0j not in{t['p']+q*rot(t['h'])for q in K}
res=json.loads(P.with_name('check_old_DCV_age2_beta_independent.json').read_text());assert res['manifest_sha256']=='807e78d3c21b66fc8aa573bf1bd47c069f0d6354739ab67c65d2c612835836f3'
targets=[]
for z in ref['two_targets']:
 A=z['foreign'];ap=complex(*z['FOREIGN_pose'][:2]);h=z['FOREIGN_pose'][2];local=(2-ap)/rot(h);assert xy(local)==z['common_FOREIGN_local']and local not in K;t=tr(W[A]);first=next((i,c)for i,(q,hh,c)in enumerate(t['reads'])if q==local);assert first==({'B':72,'F':52}[A],'R')and t['req'][local]is False
 end=tr(raw(A+'C'),ap,h);assert[*xy(end['p']),end['h']]==z['SECOND_pose'];v=tr(W['V'],end['p'],end['h']);old=tr(W['V']);a,b=center(0j,0),center(old['p'],old['h']);c,d=center(end['p'],end['h']),center(v['p'],v['h']);u,w=b-a,d-c;den=cross(u,w);s,tt=F(cross(c-a,w),den),F(cross(c-a,u),den);assert str(s)==z['contact_source_s']and str(tt)==z['contact_second_t'];targets.append((A,tuple(z['FOREIGN_pose']),tuple(z['SECOND_pose'])))
assert set(targets)=={(r[1],tuple(r[4]),tuple(r[5]))for r in res['residues']}
out={'status':'PASS two genuine V common-R8 guards; with signed beta interface closes all old D/C/V true age2 FIRST SECOND-RAW contacts','manifest_sha256':sha(mf),'dependencies':ref['dependencies'],'beta_independent_report_sha256':sha(P.with_name('check_old_DCV_age2_beta_independent.json')),'targets':targets,'analytic_review':['All three genuine V/VC/VCC source roles retain the SAME common(2,0) R8 outside final core. Signed1344 measures atomic ENTRY age, so true foreign age2 is less than3 regardless own completed C tails.','Recomputed exact foreign pulls, first own RAW R72/read73 forB and R52/read53 forF, both outside entryK, no preceding read. Contradictions are preforeign CURRENT BLACK versus actual first WHITE requirement, no maturity beyondFOREIGN.','Actual C and returnedV poses/contact parameters rebuilt; targets exactly equal the two signed807 necessary V2 residues. Hence composition closes D2,C2,V2 chronological first second-RAW source slices. The standalone guard does not need firstcontact. No arbitrary-tail simplicity or global language claim.']};P.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(P),sha(P.with_suffix('.json')))
