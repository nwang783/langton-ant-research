from pathlib import Path
import json,hashlib
P=Path(__file__).resolve();S=P.with_name('check_U1_young3_shadow_independent.py');exec(compile(S.read_text().split('rows=[];cases=[]')[0],str(S),'exec'))
B=ROOT/'core_periodicity_new/second_C_clock_guard_frozen_20261023_1340';M=json.loads((B/'manifest.json').read_text())
for f in M['files']:assert hashlib.sha256((B/f['frozen']).read_bytes()).hexdigest()==f['sha256']
J=json.loads((B/'02_second_C_common_output_clock_guard.json').read_text());D=ROOT/'core_periodicity_new'
for f,h in J['dependencies'].items():assert hashlib.sha256((D/f).read_bytes()).hexdigest()==h
C5={tuple(map(int,l.split()[:8]))for l in(D/'chronology_dcuv/critical_ucc_count5/frozen_20261023_0813/01_closure.tsv').read_text().splitlines()};HB={tuple(map(int,l.split()[:7]))for l in(D/'chronology_dcuv/protected_patch2.tsv').read_text().splitlines()};mp={a:i for i,a in enumerate(ids)}
rows=[];roles=[]
for a,pre,o in((6,5,1+6j),(9,8,7j)):
 assert raws[a]==raws[pre]+C and counts[pre]==1 and counts[a]==2
 assert o==G[pre][0]+rotation(2,G[pre][1])and o in G[a][4]
 roles.append((a,pre,(*xy(G[pre][0]),G[pre][1]),xy(o),1))
 for age in range(4):
  h=(-age)%4
  for b in ids:
   for inp in G[b][3]:
    pos=o-rotation(inp,h);key=(a,b,*xy(pos),h,*xy(o));ck=(mp[a],mp[b],*xy(pos),h,*xy(o),age)
    if(int(pos.real+pos.imag)+h)%2:why='SECTOR_IMPOSSIBLE'
    elif key in HB:why='SIGNED_HB_EXCLUDED'
    else:assert ck in C5;why='SIGNED_COUNT5_EXCLUDED'
    rows.append((a,b,xy(inp),age,(*xy(pos),h),key,ck,why))
AJ={(q['producer'],q['consumer'],tuple(q['input']),q['exact_full_source_age'],tuple(q['consumer_pose']),tuple(q['HB_key']),tuple(q['count5_key']),q['reason'])for q in J['queries']};assert set(rows)==AJ and len(rows)==184
assert sum(q[-1]=='SECTOR_IMPOSSIBLE'for q in rows)==92 and sum(q[-1]=='SIGNED_COUNT5_EXCLUDED'for q in rows)==92
out=dict(status='PASS independent second-C actual clock-shift bridge',manifest_sha256=hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),roles=roles,raw_cases=184,sector_impossible=92,signed_count5=92,scope='Only full VCC(1,6)/UCC(0,7) outputs representing second-C atomiclocal(2,0). Full producer starts one C before second atom, so atomic age=fullage−1. No fullage<=3 consumption implies atomicage>=3. Internal tail C has no residual inputs. No standalone-C kernel or separate return/global theorem.')
P.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
