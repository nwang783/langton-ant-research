from pathlib import Path
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'foreign_B_core_guard_2026-10-23'
ns={'__file__':str(R/'audits/check_foreign_kinked_barrier_turn_independent.py')};exec(Path(ns['__file__']).read_text().split('geometries=[]')[0],ns)
W,M,walk,center,xy,meet=(ns[k]for k in('W','M','walk','center','xy','meet'))
K={q for q,b in walk(M)['req'].items()if b};assert K=={-1-1j,-1,-1j,0,1};L={0,1j,1,1+1j};E={2,2+1j};p=3;h=1;BK={p+q*(-1j)**h for q in K};assert BK=={2,2+1j,3-1j,3,3+1j}
assert E<=BK and not L&BK;fresh={3-1j+q for q in L};assert fresh&BK=={3-1j,3}
G=json.loads((R/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json').read_text())['geometry']
for i in(7,8,9):
 raw=walk(G[i]['word']);out={q for q,b in raw['req'].items()if b}^raw['odd'];endcore={raw['p']+q*(-1j)**raw['h']for q in K};outputs=out-endcore
 assert L<=outputs
 for q in L:
  reads=[(i,c)for i,(qq,hh,c)in enumerate(raw['reads'])if qq==q];assert reads[-1][1]=='R'and reads[-1][0]<28
rows=[]
for a in'DCVU':
 t=walk(W[a]);hh=(h-t['h'])%4;pp=p-t['p']*(-1j)**hh;full=walk(W[a]+M);core={pp+q*(-1j)**hh for q in K};whites={pp+q*(-1j)**hh for q,b in full['req'].items()if not b}
 if a in'DV':assert L&core
 if a=='C':
  assert(pp,hh)==(3+1j,2)
  assert [(pp+q*(-1j)**hh,c)for q,_,c in full['reads'][7:9]]==[(1,'R'),(1+1j,'R')]
  assert{1,1+1j}<=whites
 if a=='U':
  assert(pp,hh)==(-1,1);hit=meet(xy(center(0,0)),xy(center(4j,0)),xy(center(pp,hh)),xy(center(p,h)));assert hit[:2]==(ns['F'](1,4),ns['F'](1,4))and hit[2]==(-1,1)
 rows.append({'atom':a,'pose':[*xy(pp),hh],'old_star_core_hits':sorted(map(xy,L&core)),'old_star_white_hits':sorted(map(xy,L&whites))})
manifest=D/'manifest.json';sha=hashlib.sha256(manifest.read_bytes()).hexdigest();assert sha=='7fa7d39d61d964f0d4ccaa02566c61ca04f4e452f5f6d3a2c30cbada8cac33c7'
for name,expected in json.loads(manifest.read_text())['files'].items():assert hashlib.sha256((D/name).read_bytes()).hexdigest()==expected
out={'status':'PASS all-age genuine-ancestry exclusion of first foreign B(3,0,E)','manifest_sha256':sha,'predecessors':rows,'analytic':['If the original east identities remain current they collide with the actual foreign-entry core. If not, their actual first breaker is the genuine right U-family at(3,-1,N), whose newly born permanent star also collides with that core. These are exhaustive and use no permanence after foreign entry.','The independent immediate-atom argument covers D,C,V,U including an internal C. D/V hit the original permanent star in entry core; C requires two old tags before-white at RAW7/8; U strictly crosses the creating U chord at both parameters1/4. No adjacency exception survives.'],'scope':'One normalized first-foreign pose excluded at all clocks. No arbitrary foreign budget, proxy Jordan assumption, preparation or global capture.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
