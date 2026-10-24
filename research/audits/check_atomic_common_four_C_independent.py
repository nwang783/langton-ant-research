from pathlib import Path
import hashlib,json
P=Path(__file__).resolve();S=P.with_name('check_U1_young3_shadow_independent.py');exec(compile(S.read_text().split('rows=[];cases=[]')[0],str(S),'exec'))
B=ROOT/'core_periodicity_new/atomic_common_4C_frozen_20261023_1344';M=json.loads((B/'manifest.json').read_text())
for f in M['files']:assert hashlib.sha256((B/f['file']).read_bytes()).hexdigest()==f['sha256']
J=json.loads((B/'02_atomic_common_output_four_C.json').read_text())
# Fresh C output and marker are derived from the actual turn word, not its supplied table.
ce,ch,_,odd=walk(C);need=walk(C+mark)[2];newcore={ce+rotation(z,ch)for z in K};co=(K^odd)-newcore
assert {z for z,b in need.items()if b}==K and need[2]is False
assert(ce,ch)==(1j,3)and co=={1+2j,2+0j,2+1j}
roles=[]
for a in ids:
 assert raws[a]==raws[base[a]]+C*counts[a]
 assert 2 in G[a][4]and G[a][2][2]is False
 roles.append((a,'DVU'[(0,4,7).index(base[a])],(0,0,0),0,(2,0)))
 p,h=G[base[a]][:2]
 for j in range(counts[a]):
  o=p+rotation(2,h);assert o in G[a][4]
  roles.append((a,'C',(*xy(p),h),j,xy(o)))
  p+=rotation(ce,h);h=(h+ch)%4
 assert(p,h)==G[a][:2]
AR={(r['full_source'],r['atomic_source'],tuple(r['atomic_start']),r['atomic_birth_clock_shift'],tuple(r['full_source_output']))for r in J['all15_atomic_source_roles']}
assert set(roles)==AR and len(roles)==15 and sum(r[3]==1 for r in roles)==2
D=ROOT/'core_periodicity_new';C5={tuple(map(int,l.split()[:8]))for l in(D/'chronology_dcuv/critical_ucc_count5/frozen_20261023_0813/01_closure.tsv').read_text().splitlines()};mp={a:i for i,a in enumerate(ids)}
queries=[]
for a,o in((6,1+6j),(9,7j)):
 for n in range(4):
  h=(-n)%4
  for b in ids:
   for inp in G[b][3]:
    p=o-rotation(inp,h);key=(mp[a],mp[b],*xy(p),h,*xy(o),n)
    if(int(p.real+p.imag)+h)%2:why='SECTOR_IMPOSSIBLE'
    else:assert key in C5;why='SIGNED_COUNT5_EXCLUDED'
    queries.append((a,xy(o),n,n-1,b,xy(inp),(*xy(p),h),why,key))
AQ={(q['full_source'],tuple(q['output']),q['full_source_age'],q['atomic_source_age'],q['consumer'],tuple(q['input']),tuple(q['consumer_pose']),q['reason'],tuple(q['query']))for q in J['all184_second_C_clock_queries']}
assert set(queries)==AQ and len(queries)==184
age2=[];ends=[]
for a in ids:
 for inp in G[a][3]:
  assert oldages[a,inp]>=2
  if oldages[a,inp]==2:
   p=2-rotation(inp,2);assert(int(p.real+p.imag)+2)%2
   age2.append((a,xy(inp),(*xy(p),2)))
assert len(age2)==2
for h in(0,1):
 for b in(0,4,7):
  step=rotation(G[b][0],h);assert step.real>=0
  for inp in G[b][3]:
   p=2-rotation(inp,h);end=p+step;assert end.real>=2
   ends.append((b,xy(inp),h,xy(p),xy(end)))
AE={(r['retiring_base'],tuple(r['input']),r['heading'],tuple(r['start']),tuple(r['end']))for r in J['all16_retiring_base_endpoints']};assert set(ends)==AE and len(ends)==16
assert rotation(ce,1)==1
out=dict(status='PASS independent atomic common-output clock/endpoint assembly',manifest_sha256=hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),actual_atomic_roles=roles,shifted_clock_queries=184,age2_wrong_sector=age2,retirement_endpoints=ends,scope='Actual atomic cuts inside complete recurrent-eight factors only. Every atomic source freshly installs local(2,0), consumption atomic-age>=3 including second-C clock shift. E/N base cones remain valid when target cuts split a consuming packet C tail. Output persists before four-C N cuts X<=1, whose same-pose marker would require white. No factor-first exception; no arbitrary atomic-language license or higher-C recurrence/global capture result.')
P.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items()if k not in('actual_atomic_roles','retirement_endpoints')})
