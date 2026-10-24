from pathlib import Path
from collections import Counter
SELF=Path(__file__).resolve();S=SELF.with_name('check_D_first_W5_gate_independent.py');exec(compile(S.read_text().split('rows=[];late=[]')[0],str(S),'exec'))
B=ROOT/'core_periodicity_new/six_C_successor_cohort_frozen_20261023_1538';M=json.loads((B/'manifest.json').read_text())
for f in M['files']:assert hashlib.sha256((B/f['frozen']).read_bytes()).hexdigest()==f['sha256']
J=json.loads((B/'02_six_C_successor_cohort_exclusion.json').read_text())
# Fresh complete masks, not copied output assertions. Global q is installed by
# the immediate successor at4i and is a CORE cell at final V(4i,S).
q=4j;source=4j;target=4j;assert 0 in K and G[4][2][0]
for src in (4,5,6,7,8,9):assert 0 in G[src][4]
# Exact original U chord, with all coordinates doubled.
start=-1-1j;end=start+8j
rows=[]
for src in(4,5,6,7,8,9):
 for n in range(7):
  h=(-n)%4
  for dst in ids:
   for slot in G[dst][3]:
    pp=q-rotation(slot,h);rel=pp-source
    hb=(src,dst,*xy(rel),h,0,0);cq=(mp[src],mp[dst],*xy(rel),h,0,0,min(n,5))
    if n<counts[src]:why='BEFORE_SUCCESSOR_FULL_EXIT'
    elif(int(pp.real+pp.imag)+h)%2:why='SECTOR'
    elif hb in HB:why='SIGNED_HB'
    elif cq in C5:why='SIGNED_COUNT5'
    else:
     ep=pp+rotation(G[base[dst]][0],h)
     a=2*pp+rotation(start,h);b=2*ep+rotation(start,h)
     if meet(start,end,a,b):why='EARLIER_NONADJACENT_CLOSED_CONTACT_WITH_ORIGINAL_U'
     elif n+counts[dst]>6:why='CONSUMER_FULL_TAIL_ENDS_AFTER_TARGET_FULL_ENTRY'
     elif n==5:
      assert h==3 and ep in(5j,-2+5j)
      # Every W-zero and S-zero run weakly decreases x; required W->S C
      # decreases x by exactly1. Thus final x<0, not target x0.
      assert ep.real<=target.real
      why='EXACT_ONE_C_W_TO_S_ENDPOINT_CONE_IMPOSSIBLE'
     elif n==6:
      assert h==2 and dst==7 and ep==2j
      # Every S-zero atom weakly decreases y, never from2 to4.
      assert ep.imag<target.imag
      why='EXACT_ZERO_C_ENDPOINT_CONE_IMPOSSIBLE'
     else:raise AssertionError(('OPEN',src,n,dst,pp,slot))
    rows.append((src,dst,xy(slot),n,(*xy(pp),h),why))
author={(r['successor_full'],r['consumer_full'],tuple(r['consumer_input']),r['source_included_C_age']):r for r in J['all966_first_consumer_queries']}
assert len(rows)==len(author)==966
for src,dst,slot,n,pose,why in rows:
 r=author[src,dst,slot,n];assert tuple(r['consumer_pose'])==pose and r['reason']==why
count=Counter(r[-1]for r in rows)
assert count=={'BEFORE_SUCCESSOR_FULL_EXIT':138,'SECTOR':436,'SIGNED_COUNT5':251,'EARLIER_NONADJACENT_CLOSED_CONTACT_WITH_ORIGINAL_U':57,'CONSUMER_FULL_TAIL_ENDS_AFTER_TARGET_FULL_ENTRY':30,'EXACT_ONE_C_W_TO_S_ENDPOINT_CONE_IMPOSSIBLE':48,'EXACT_ZERO_C_ENDPOINT_CONE_IMPOSSIBLE':6}
out=dict(status='PASS independent second-generation exclusion of the sole six-C first center contact',manifest_sha256=hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),query_count=len(rows),reason_counts=dict(count),queries=rows,scope='Inside actual complete-eight factors, every canonical first center contact with atomic entry-C gap6 is impossible after the signed1454/1505 reductions. Immediate successor fresh output at(0,4) cannot retire before the final V core. Exact complete producer ages and full-entry target timing retained. This does not exclude arbitrary later6C contacts, prove center selfavoidance, or close global V1/U1.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items()if k!='queries'})
