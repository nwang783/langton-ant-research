from pathlib import Path
import json,hashlib
from collections import Counter
P=Path(__file__).resolve();S=P.with_name('check_U1_young3_shadow_independent.py');exec(compile(S.read_text().split('rows=[];cases=[]')[0],str(S),'exec'))
B=ROOT/'core_periodicity_new/atomic_exit_bud_frozen_20261023_1325';M=json.loads((B/'manifest.json').read_text())
for f in M['files']:assert hashlib.sha256((B/f['frozen']).read_bytes()).hexdigest()==f['sha256']
J=json.loads((B/'02_atomic_exit_bud_maturation.json').read_text());D=ROOT/'core_periodicity_new'
for f,h in J['dependencies'].items():assert hashlib.sha256((D/f).read_bytes()).hexdigest()==h
C5={tuple(map(int,l.split()[:8]))for l in(D/'chronology_dcuv/critical_ucc_count5/frozen_20261023_0813/01_closure.tsv').read_text().splitlines()};HB={tuple(map(int,l.split()[:7]))for l in(D/'chronology_dcuv/protected_patch2.tsv').read_text().splitlines()};mp={a:i for i,a in enumerate(ids)}
ce,ch,_,odd=walk(C);need=walk(C+mark)[2];assert C.startswith(mark)and{z for z,b in need.items()if b}==K
co=(K^odd)-{ce+rotation(z,ch)for z in K};assert co=={1+2j,2+0j,2+1j}and(ce,ch)==(1j,3)
assert ce+rotation(1-1j,ch)==1+2j
rows=[];roles=[]
for a in ids:
 for pref in range(counts[a]+1):
  word=raws[base[a]]+C*pref;p,h,_,_=walk(word);o=p+rotation(1-1j,h);assert o in G[a][4]
  roles.append((a,pref,(*xy(p),h),xy(o)))
  for n in range(pref,pref+3):
   gh=(-n)%4
   for b in ids:
    for inp in G[b][3]:
     pos=o-rotation(inp,gh);hk=(a,b,*xy(pos),gh,*xy(o));ck=(mp[a],mp[b],*xy(pos),gh,*xy(o),n)
     if n<counts[a]:why='CONSUMER_PRECEDES_FULL_PRODUCER_EXIT'
     elif(int(pos.real+pos.imag)+gh)%2:why='SECTOR_IMPOSSIBLE'
     elif hk in HB:why='SIGNED_HB_EXCLUDED'
     else:assert ck in C5;why='SIGNED_COUNT5_EXCLUDED'
     rows.append((a,pref,xy(o),b,xy(inp),n,n-pref,(*xy(pos),gh),hk,ck,why))
AR={(q['full_producer'],q['atomic_prefix_C'],tuple(q['atomic_exit']),tuple(q['bud_full_output_slot']))for q in J['roles']};assert set(roles)==AR and len(roles)==15
AQ={(q['producer'],q['prefix_C'],tuple(q['output']),q['consumer'],tuple(q['input']),q['source_included_age'],q['post_atomic_exit_C'],tuple(q['consumer_pose']),tuple(q['HB_key']),tuple(q['count5_key']),q['reason'])for q in J['queries']};assert set(rows)==AQ and len(rows)==1035
stats=Counter(q[-1]for q in rows);assert stats==dict(CONSUMER_PRECEDES_FULL_PRODUCER_EXIT=207,SECTOR_IMPOSSIBLE=469,SIGNED_COUNT5_EXCLUDED=359)
assert sorted([*xy(z),bit]for z,bit in need.items())==J['C_entry_requirements']
out=dict(status='PASS independent atomic C ledger, full-source roles and exact maturation clauses',manifest_sha256=hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),C_endpoint=[*xy(ce),ch],C_input_count=0,C_outputs=sorted(map(xy,co)),roles=roles,raw_cases=len(rows),counts=stats,scope='Every actual D/V/U/C atomic exit installs a fresh residual beta; C has no residual inputs and preserves older current identities. Fifteen full-source output roles exclude consumption within0..2 post-atomic Cs by actual full-source exact ages<=4, with within-source tails handled literally. Thus all buds in any consecutive clock-span<=2 window are distinct and current. No standalone-C counted theorem, global head-path selfavoidance, uniform packing/fuel or record/capture closure.')
P.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
