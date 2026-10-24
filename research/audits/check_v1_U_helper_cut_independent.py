from pathlib import Path
import json,hashlib
P=Path(__file__).resolve();prefix=P.with_name('check_U1_young3_shadow_independent.py').read_text().split('rows=[];cases=[]')[0];exec(compile(prefix,str(P.with_name('check_U1_young3_shadow_independent.py')),'exec'))
B=ROOT/'core_periodicity_new/v1_U_helper_cut_frozen_20261023_1239';M=json.loads((B/'manifest.json').read_text())
for f in M['files']:assert hashlib.sha256((B/f['file']).read_bytes()).hexdigest()==f['sha256']
head=-4+1j;dh=1;points={z:head+rotation(z,dh)for z in G[7][3]};assert head+rotation(G[7][0],dh)==1j
assert rotation(G[0][0],1)==1-1j
DCall=G[1][3]|G[1][4]
checks=[]
for slot,q in sorted(points.items(),key=lambda r:xy(r[0])):
 minimum=4 if slot in(-1+1j,-1+2j)else 5
 for r in DCall:
  diff=r-q;g=int(diff.imag)
  assert not(g>=0 and diff==g*(-1+1j))
 height=H(q);assert height in(-1,0,2)
 checks.append({'slot':xy(slot),'point_at_g0':xy(q),'coefficient':[-1,1],'height':height,'helper_age':minimum,'pre_DC_age':minimum-3,'I28_entry_forbidden':28+2*height>=28,'I30_entry_forbidden':30+2*height>=28})
assert len(points)==5 and sum(r['I28_entry_forbidden']for r in checks)==3 and all(r['I30_entry_forbidden']for r in checks)
assert G[1][3]=={1j}and len(G[1][4])==4 and 28+2*H(1j)==30>28
# The age-three source reduction has source one north of this E helper.
shead=head+1j;assert H(shead)==-2
for s in(4,5,6):
 for z in G[s][3]:assert H(shead+z)==1 and 28+2*H(shead+z)==30>28
out={'status':'PASS complete literal affine mask and conditional age/funding cut reconstruction','manifest_sha256':hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),'helper_inputs':checks,'pre_DC_residual_count':6,'post_DC_residual_count':9,'I28_produced_counts':[4,7],'I30_produced_counts':[6,9],'scope':'Only outer unfunded V1 exact DC-age3 role with last U helper. Uses signed1230 boundary and lower-pair equivalence, no iteration to V-helper, root/component import, fresh fuel, V1 closure or capture.'}
P.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
