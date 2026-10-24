from pathlib import Path
from collections import Counter
SELF=Path(__file__).resolve();S=SELF.with_name('check_D_first_W5_gate_independent.py');exec(compile(S.read_text().split('rows=[];late=[]')[0],str(S),'exec'))
B=ROOT/'core_periodicity_new/atomic_three_C_left_boundary_frozen_20261023_1530';M=json.loads((B/'manifest.json').read_text())
for f in M['files']:assert hashlib.sha256((B/f['frozen']).read_bytes()).hexdigest()==f['sha256']
J=json.loads((B/'02_atomic_three_C_left_step_boundary.json').read_text());rows=[]
for a in ids:
 for j in range(counts[a]+1):
  A,ah,_,_=walk(raws[base[a]]+C*j);bud=A+rotation(1-1j,ah);assert bud in G[a][4]
  target=A+rotation(-1,ah);bh=(ah+1)%4;assert rotation(bud-target,-bh)==1+2j
  for dst in(4,5,6):
   key=(a,dst,*xy(target),bh,*xy(bud));cq=(mp[a],mp[dst],*xy(target),bh,*xy(bud),min(j+3,5))
   if key in HB:why='SIGNED_HB'
   elif cq in C5:why='SIGNED_COUNT5'
   elif j<counts[a]:
    assert(a,j,dst)in((1,0,4),(1,0,5));why='SIGNED_C_E3_SOURCE_FULL_DC_MUST_BE_FACTOR_FIRST'
   elif counts[a]==2:
    cp,ch,_,_=walk(raws[base[a]]+C);assert(cp,ch)==(target,bh)
    assert 1-counts[a]==-1 and 3-(-1)==4
    why='SIGNED_ATOMIC_FOUR_C_FULL_POSE_NONRETURN'
   else:
    assert(a,j,dst)in((0,0,4),(0,0,5));why='PLAIN_D_MUST_BE_FACTOR_FIRST_BY_ITS_OLDER_BUD_WHITE'
   rows.append((a,j,dst,(*xy(A),ah),(*xy(target),bh),xy(bud),j+3,key,cq,why))
for b in(4,5):assert G[b][2][2+1j]is False and -1+rotation(2+1j,1)==-2j
assert len(rows)==45
au={(r['previous_full'],r['atomic_prefix_C'],ids[r['count5_key'][1]]):r for r in J['all45_actual_incoming_atom_role_queries']}
for a,j,b,A,T,o,n,key,cq,why in rows:
 r=au[a,j,b];assert tuple(r['A_full_relative_pose'])==A and tuple(r['B_full_relative_pose'])==T and tuple(r['incoming_bud_full_output'])==o and r['full_source_included_C_age']==n and tuple(r['HB_key'])==key and tuple(r['count5_key'])==cq and r['reason']==why
counts_=Counter(r[-1]for r in rows);assert counts_==J['query_counts']
out=dict(status='PASS independent actual-atom three-C left-step boundary assembly',manifest_sha256=hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),queries=rows,reason_counts=dict(counts_),scope='Actual atomic cuts inside complete-eight factors only. The source is factor first entry, second complete entry after factor-first plainD, or firstC inside factor-firstDC; hence factor-entry C clock. Last two alternatives require V/VC targets. No first-contact or funding premise, arbitrary atomic language or global nonreturn.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items()if k!='queries'})
