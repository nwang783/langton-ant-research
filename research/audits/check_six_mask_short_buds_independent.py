from pathlib import Path
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'core_periodicity_new/six_mask_short_return_buds_frozen_20261023_2046'
ns={'__file__':str(R/'audits/check_U_foreign_prefix_buds_independent.py')};exec(Path(ns['__file__']).read_text().split('COUNT=')[0],ns);inv,xy=ns['inv'],ns['xy'];rows=[]
for a,p,h,k in[('DC',-5+1j,0,4),('VC',-4+7j,1,5)]:
 ep=p+inv[a]['p']*(-1j)**h;eh=(h+inv[a]['h'])%4;n=k-a.count('C');goal=-ep*(1j)**eh;gh=(-eh)%4;bud=ep+(1-1j)*(-1j)**eh;slot=(bud-p)*(1j)**h
 assert slot in inv[a]['outputs']and n in(3,4)and gh==(-n)%4 and goal.real<=0
 assert bud not in inv['UCC']['inputs'] and inv['UCC']['full']['req'][bud]is False
 first=next((i,c)for i,(q,hh,c)in enumerate(inv['UCC']['full']['reads'])if q==bud)
 rows.append((a,xy(p),h,k,xy(ep),eh,n,xy(goal),gh,xy(bud),xy(slot),first))
assert rows[0][-1]==(65,'R') and rows[1][-1]==(34,'R')
m=D/'manifest.json';sha=hashlib.sha256(m.read_bytes()).hexdigest();assert sha=='a5e3d631a2a923b2a4616e070eea39bca0ae5e8ad8feeea2dd0a6ebdc5ea9d9d'
for r in json.loads(m.read_text())['files']:assert hashlib.sha256((D/r['file']).read_bytes()).hexdigest()==r['sha256']
out={'status':'PASS two exact short six-mask return representatives, not longer overflow ages','manifest_sha256':sha,'cases':rows,'analytic':'At the actual producer full exit A there is a genuine preceding atom inside the factor, even if that full producer is factor-first. Its true exitbud at A+(1,-1) is current. The creator UCC entry is an actual atomic cut at relative3C E with X=-3 or4C N with X0. Signed1505 therefore preserves that exact bud until the creator. Full UCC requires it WHITE at phases65/34, not as an input. Full-source ages4/5 map to post-exit gaps3/4. No following fictional packet or untouched-root argument is used.','scope':'Only DC(-5,1,N) age4 and VC(-4,7,E) age5 before UCC0,N. Congruent ages8+/9+ remain open. This does not sign the still-pending2044 necessary-filter table, event funding or capture.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
