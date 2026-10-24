from pathlib import Path
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'seven_word_spatial_return_2026-10-23';m=D/'returned_C_UC_F_core_guard_manifest.json';h=hashlib.sha256(m.read_bytes()).hexdigest();assert h=='773464470ea83b565a51e150dccc0af9ff0e680ca1b144ff37b866a11fd0f6de'
j=json.loads(m.read_text())
for f,v in j['files'].items():assert hashlib.sha256((D/f).read_bytes()).hexdigest()==v
for f,v in j['dependencies'].items():assert hashlib.sha256((R/f).read_bytes()).hexdigest()==v
ns={'__file__':str(SELF.parent/'check_foreign_kinked_barrier_turn_independent.py')};exec(Path(ns['__file__']).read_text().split('geometries=[]')[0],ns);W,M,walk,xy=[ns[x]for x in('W','M','walk','xy')]
u=walk(W['U']);assert(u['p'],u['h'])==(4j,0);creator=-4j;star={creator+x for x in(0j,1j,1+0j,1+1j)};K={-1-1j,-1,-1j,0j,1+0j};rows=[]
for f,p in [('F',2-5j),('Q',4-5j),('B',5-4j)]:
 tr=walk(W[f]+W['C']+M);assert tr['feasible'];ctx={p+q*(-1j):v for q,v in tr['req'].items()};core={p+q*(-1j)for q in K};hits=star&set(ctx);corehits=star&core
 if f=='F':
  assert 1-4j in corehits and p+(-1-1j)*(-1j)==1-4j
  rr=[(i,ch)for i,(q,hh,ch)in enumerate(tr['reads'])if p+q*(-1j)==1-4j];assert rr[0]==(2,'L')
 else:assert not hits and not corehits
 rows.append({'foreign':f,'star_context_hits':sorted(map(xy,hits)),'star_entry_core_hits':sorted(map(xy,corehits))})
out={'status':'PASS exact UC-containing-source exclusion for F/C3 only','manifest_sha256':h,'creator_relative_to_old_C':[0,-4,0],'old_star':sorted(map(xy,star)),'three_foreign_contexts':rows,'analytic':'Actual U base ends at(0,4,N), so normalizing its own C1 to0 places its genuine creator at(0,-4,N). Its original star site(1,-4) remains a current residual identity throughout the actual old-eight factor. F entry K at(2,-5,E) contains that exact site as local(-1,-1), contradicting residual/core disjointness at the PREforeign full cut. F context tick2/read3 confirms the core role, not a postforeign age claim. Q/B combined actual contexts miss all four star sites and remain open.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
