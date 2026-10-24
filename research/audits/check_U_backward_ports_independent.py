from pathlib import Path
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'old_U_Q_B_backward_ports_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(D/'manifest.json')=='4a85c7789f5c69b7f5486d431db47ac4fce052856303c217f2301def56a19c3e'
for f,h in json.loads((D/'manifest.json').read_text())['files'].items():assert sha(D/f)==h
J=json.loads((D/'backward_ports.json').read_text())
for f,h in J['dependencies'].items():assert sha(R/f)==h
ns={'__file__':str(S.with_name('check_old_V_second_age1_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Universal')[0],ns)
W,M,K,tr,G,rot,center,xy,meet=[ns[k]for k in('W','M','K','tr','G','rot','center','xy','meet')];raw=lambda seq:''.join(W[a]for a in seq)
pairs={};star={0,1j,1,1+1j}
for full in('D','DC','V','VC','VCC','U','UC','UCC'):
 for A in'FQB':pairs[full,A]=tr(raw(full+A)+M)['bad']is None
assert{p for p,b in pairs.items()if b}=={('V','F'),('V','Q'),('U','F'),('U','Q'),('U','B')}
assert pairs=={(r['actual_full_predecessor'],r['foreign']):r['feasible']for r in J['all24_actual_full_eight_foreign_literal_pairs']}
rows=[]
for A,ap in(('Q',-1-3j),('B',-4j)):
 for full in('D','DC','V','VC','VCC','U','UC','UCC'):
  if not pairs[full,A]:continue
  e=tr(raw(full),h=2);p=ap-e['p'];assert e['h']==2
  hits=star&{p+k*rot(2)for k in K};assert hits
  ref=next(r for r in J['all3_allowed_genuine_predecessor_core_chord_guards']if r['foreign']==A and r['actual_last_complete_eight_packet']==full)
  assert xy(p)+[2]==ref['predecessor_entry_pose']and set(map(tuple,map(xy,hits)))==set(map(tuple,ref['SAME_original_U_star_inside_core']))
  if p==-1+1j:
   assert full=='U'and A=='Q';a,b=center(p,2),center(ap,2);assert(a,b)==(-1+3j,-1-5j)
   hit=meet(-1-1j,-1+7j,a,b);assert hit[0]=='OVERLAP'and hit[1:]==(0,1/2)
  rows.append((A,full,xy(p),sorted(map(xy,hits))))
out=dict(status='PASS all-age PREfirstforeign old-U Q/B backward core guards only',manifest=sha(D/'manifest.json'),actual_pairs=24,three_core_guards=rows,scope=['Actual complete G8-to-FIRSTforeign pair coverage leaves only plain V/U; no arbitrary standalone-C predecessor is admitted.','Signed1918 SAME original U-star remains external CURRENT throughout the preforeign uninterrupted factor at every age; each candidate preceding entry core contradicts this. No source bud age invoked after foreign.','The extra Q/U strict-interior overlap is independently checked but unnecessary to the core cut. No later-tail persistence or third simplicity.'])
S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
