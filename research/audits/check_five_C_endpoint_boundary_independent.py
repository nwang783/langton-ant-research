"""Independent actual-predecessor frames and complete first-retirement closure."""
from pathlib import Path
SELF=Path(__file__).resolve();S=SELF.with_name('check_five_C_center_touch_independent.py');exec(compile(S.read_text().split('primary=0;hardcases=0;gate=[]')[0],str(S),'exec'))
B=ROOT/'core_periodicity_new/five_C_endpoint_boundary_frozen_20261023_1557';M=json.loads((B/'manifest.json').read_text())
for f in M['files']:assert hashlib.sha256((B/f['frozen']).read_bytes()).hexdigest()==f['sha256']
J=json.loads((B/'02_five_C_endpoint_boundary.json').read_text());atomic=roles
roles=[('D',src,G[src][0],G[src][1],counts[src],0)for src in ids]
assert all((sh+c)%4==0 and sp+rotation(1-1j,sh)in G[src][4]for a,src,sp,sh,c,rem in roles)
for r,(a,src,sp,sh,c,rem)in zip(J['all_eight_completed_predecessor_roles'],roles):assert(r['source'],tuple(r['p']),r['h'],r['shift'],r['remaining'])==(src,xy(sp),sh,c,rem)
assert 1-1j not in K|G[0][3] and rotation((1-1j)-(-1j),1)in K
rows=retirement('D',1-1j,'C',-1j);opened=[r for r in rows if r['why']=='RESIDUAL_OPTION'];assert len(rows)==1104 and len(opened)==68
final_counts=Counter()
def reason(r):
 n,dst,p=r['n'],r['dst'],complex(*r['pose'][:2])
 if n==5:
  assert(dst in(4,5,6)and p==3-2j)or(dst in(7,8,9)and p==4-1j)
  why='NEEDS_OLD_MAIN_WHITE_BUT_EVERY_PRIOR_MAIN_CLEARER_LEAVES_IMMATURE_BUD'
 elif base[dst]==4:
  assert n==3 and p==-2-1j and 2*r['ep']+rotation(center,1)==-2j+rotation(center,3)
  why='CLEARING_V_EXIT_CENTER_REPEATS_AT_FINAL_C_ENTRY'
 else:
  assert n==3 and base[dst]==7 and r['src']in(6,9)
  if p==-3-2j:
   assert 2*r['ep']+rotation(center,1)==-2j+rotation(center,3)
   why='CLEARING_U_EXIT_CENTER_REPEATS_AT_FINAL_C_ENTRY'
  else:
   assert p==-1-2j and p+rotation(1j,1)==-2j and rotation(-2j-(-1j),1)in K
   why='FRESH_U_OUTPUT_0_1_STILL_CURRENT_IN_FINAL_C_CORE'
 final_counts[why]+=1;return why
compare(rows,J['all_1104_incoming_bud_retirement_cases'],reason)
assert sorted(final_counts.values())==[6,6,8,48]
roles=atomic;helper_rows=0
for tab in J['last_clock_helper_main_retirement_tables']:
 a=tab['helper_atom'];p=complex(*tab['helper_pose'][:2]);assert(a,p)in[('V',3-2j),('U',4-1j)]and need[a][rotation(2-p,1)]is False
 rs=retirement('D',2+0j,a,p);assert len(rs)==276 and sum(r['why']=='RESIDUAL_OPTION'for r in rs)==4
 def cut(r):
  assert r['n']==3 and r['dst']in(4,5)and r['pose']==(0,1,1)
  # Fresh atomic V exit bud persists through the remaining two Cs.
  local=rotation(2-1j-p,1)
  if a=='V':assert local==1+1j and need[a][local]is False
  else:assert local==2j and local in G[7][3]
  return'FRESH_V_EXIT_BUD_STILL_CURRENT_WHITE_OR_TOO_YOUNG_AT_HELPER'
 compare(rs,tab['rows'],cut);helper_rows+=len(rs)
# Reconstruct the full-source age0..2 guard on the newly installed U output(0,1).
queries=[]
for src in(7,8,9):
 assert 1j in G[src][4]
 for age in range(3):
  h=(-age)%4
  for dst in ids:
   for slot in G[dst][3]:
    pp=1j-rotation(slot,h);cq=(mp[src],mp[dst],*xy(pp),h,0,1,age);hb=(src,dst,*xy(pp),h,0,1)
    if age<counts[src]:why='BEFORE_FULL_SOURCE_EXIT'
    elif(int(pp.real+pp.imag)+h)%2:why='WRONG_SECTOR'
    elif hb in HB:why='SIGNED_HB_EXCLUDED'
    else:assert cq in C5;why='SIGNED_COUNT5_EXCLUDED'
    queries.append((cq,hb,why))
assert len(queries)==207 and set(queries)=={(tuple(r['query']),tuple(r['HB_query']),r['reason'])for r in J['all_207_fresh_U_output_0_1_age_zero_to_two_cases']}
# Frozen old JO lower bounds suffice for the helper's upper input of age2.
jo={(r[0],r[1],r[2]):r[3]for r in json.loads((B/'06_counted_input_age_rules_complete.json').read_text())};assert jo[7,0,2]>=4
out=dict(status='PASS independent five-C D-to-C FIRST-contact boundary classification',manifest_sha256=hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),completed_predecessors=8,predecessor_retirement_rows=1104,residual_options=68,residual_final_cuts=dict(final_counts),helper_main_rows=helper_rows,U_fresh_output_rows=len(queries),scope='The normalized first-contact D0N to C(0,-1,W) at atomic entry gap5 requires D to be factor-first, containing full source D or DC. Target C may be internal; no following complete packet is inferred. No arbitrary later-transfer, global self-avoidance or capture claim.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
