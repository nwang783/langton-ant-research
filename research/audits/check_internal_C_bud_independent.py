from pathlib import Path
import json,hashlib
P=Path(__file__).resolve();S=P.with_name('check_U1_young3_shadow_independent.py');exec(compile(S.read_text().split('rows=[];cases=[]')[0],str(S),'exec'))
B=ROOT/'core_periodicity_new/internal_C_prefix_bud_frozen_20261023_1319';M=json.loads((B/'manifest.json').read_text())
for f in M['files']:assert hashlib.sha256((B/f['frozen']).read_bytes()).hexdigest()==f['sha256']
J=json.loads((B/'02_internal_C_prefix_bud_guard.json').read_text());D=ROOT/'core_periodicity_new'
for f,h in J['dependencies'].items():assert hashlib.sha256((D/f).read_bytes()).hexdigest()==h
C5={tuple(map(int,l.split()[:8]))for l in(D/'chronology_dcuv/critical_ucc_count5/frozen_20261023_0813/01_closure.tsv').read_text().splitlines()};HB={tuple(map(int,l.split()[:7]))for l in(D/'chronology_dcuv/protected_patch2.tsv').read_text().splitlines()};mp={a:i for i,a in enumerate(ids)}
rows=[];prefixes=[];ports=[]
for a,pre,o in((6,5,2+5j),(9,8,1+6j)):
 assert raws[a]==raws[pre]+C and C.startswith(mark)
 assert o in G[a][4] and o==G[pre][0]+rotation(1-1j,G[pre][1])
 assert counts[a]==2 and counts[pre]==1;prefixes.append((a,pre,xy(o),(*xy(G[pre][0]),G[pre][1])))
 for age in range(5):
  h=(-age)%4
  for b in ids:
   for inp in G[b][3]:
    pos=o-rotation(inp,h);key=(a,b,*xy(pos),h,*xy(o));ck=(mp[a],mp[b],*xy(pos),h,*xy(o),age)
    if(int(pos.real+pos.imag)+h)%2:why='SECTOR_IMPOSSIBLE'
    elif key in HB:why='SIGNED_HB_EXCLUDED'
    else:assert ck in C5;why='SIGNED_COUNT5_EXCLUDED'
    rows.append((a,b,xy(inp),age,(*xy(pos),h),key,ck,why))
for z,black in G[7][2].items():
 p=z-1-1j
 if(int(p.real+p.imag)+3)%2:continue
 role='INPUT'if z in G[7][3]else'CORE'if z in K else'WHITE'
 if role=='WHITE':assert not black
 ports.append((xy(p),xy(z),black,role))
AJ={(q['producer'],q['consumer'],tuple(q['input']),q['exact_age'],tuple(q['consumer_pose']),tuple(q['HB_key']),tuple(q['count5_key']),q['reason'])for q in J['queries']};assert set(rows)==AJ and len(rows)==230
AP={(tuple(q['internal_W_cut']),tuple(q['prefix_bud']),q['goal_required_black'],q['goal_role'])for q in J['internal_W_cut_U_goal_ports']};assert set(ports)==AP and len(ports)==11
assert sum(q[-1]=='SECTOR_IMPOSSIBLE'for q in rows)==104 and sum(q[-1]=='SIGNED_COUNT5_EXCLUDED'for q in rows)==126
assert sum(q[-1]=='CORE'for q in ports)==3 and(-3,2)not in[q[0]for q in ports]
out=dict(status='PASS independent full-producer typed ages and internal-C cut ports',manifest_sha256=hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),prefixes=prefixes,query_count=len(rows),sector_impossible=104,signed_count5=126,ports=ports,scope='Only VCC output(2,5), UCC output(1,6) full-producer roles; no consumption at exact source-included ages0..4. At internal first-C cut goalclock−3 the full packet starts goalclock−4 and finishes goalclock−2, so its actual fresh full output survives through goal. Every complete goal-context hit is impossible, including core via ordered residual disjointness. No standalone-C theorem, ordinary-boundary extension, q4/U1 closure or capture.')
P.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
