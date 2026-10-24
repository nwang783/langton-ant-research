from pathlib import Path
from collections import Counter
SELF=Path(__file__).resolve();S=SELF.with_name('check_D_first_W5_gate_independent.py');exec(compile(S.read_text().split('rows=[];late=[]')[0],str(S),'exec'))
B=ROOT/'core_periodicity_new/D_W5_helper_history_frozen_20261023_1548';MF=json.loads((B/'manifest.json').read_text())
for f in MF['files']:assert hashlib.sha256((B/f['frozen']).read_bytes()).hexdigest()==f['sha256']
J=json.loads((B/'02_D_W5_helper_history_exclusion.json').read_text());main=2+0j;final=1+0j;helpers=((4,4-1j),(7,5+0j));branches=[]
for src in(4,5,6,7,8,9):branches.append((src,1+1j,0j,1+1j,'PLAIN_D_NEXT_V_U'))
for src in(0,1):branches.append((src,1+1j,2+0j,3+1j,'PLAIN_D_NEXT_D_DC'))
branches.append((1,0j,3+1j,3+1j,'SOURCE_FULL_DC'));rows=[];case_facts=[]
# A preceding packet's terminal marker may overlap the helper, but neither
# possible helper's protected main input is in the common marker read set.
marker_cells=set(walk(mark)[2])
for bi,(src,sp,o,q,kind)in enumerate(branches):
 assert o in G[src][4] and sp+o==q
 for helper,hp in helpers:
  ml=rotation(main-hp,-3);ql=rotation(q-hp,-3)
  assert ml in G[helper][3] and ml not in marker_cells and ql not in G[helper][3]
  if kind=='PLAIN_D_NEXT_V_U':
   assert rotation(q-final,-3)==1 and 1 in K
   for dst in(4,7):assert G[dst][2][1] and 1 not in G[dst][3]
  else:assert G[helper][2][ql] is False
  case_facts.append((bi,helper,xy(ql),xy(ml)))
  for n in range(6):
   h=(-n)%4
   for dst in ids:
    for slot in G[dst][3]:
     pp=q-rotation(slot,h);rel=pp-sp;hb=(src,dst,*xy(rel),h,*xy(o));cq=(mp[src],mp[dst],*xy(rel),h,*xy(o),n)
     if n<counts[src]:why='BEFORE_SOURCE_FULL_EXIT'
     elif(int(pp.real+pp.imag)+h)%2:why='SECTOR'
     elif hb in HB:why='SIGNED_HB'
     elif cq in C5:why='SIGNED_COUNT5'
     else:
      ep=pp+rotation(G[base[dst]][0],h);start=2*pp+rotation(-1-1j,h);end=2*ep+rotation(-1-1j,h)
      if meet(-1-1j,1+1j,start,end):why='EARLIER_NONADJACENT_CLOSED_ORIGINAL_D_CONTACT'
      elif rotation(main-pp,-h)in G[dst][2]:why='PROTECTED_MAIN_CURRENT_THROUGH_CONSUMER_COMPLETE_CONTEXT'
      elif n+counts[dst]>5:why='CONSUMER_FULL_TAIL_FINISHES_AFTER_HELPER_ENTRY'
      elif n==5:
       assert h==3 and ep.imag==2 and ep.real<=3 and hp.real>=4 and hp.imag<=0
       # W zero-C displacements have x<=0,y>=0, incompatible in both coordinates.
       why='EXACT_ZERO_C_ENDPOINT_CONE_IMPOSSIBLE'
      elif n==4:
       assert h==0 and dst in(7,8) and ep==4+4j and hp.imag<=0
       # N zero-C, N->W C, and W zero-C all have nonnegative y;
       # the unique C increases y by1. The helper is below the start.
       why='EXACT_ONE_C_N_TO_W_ENDPOINT_CONE_IMPOSSIBLE'
      else:raise AssertionError(('OPEN',bi,helper,n,dst,pp,slot))
     rows.append((bi,helper,n,dst,xy(slot),(*xy(pp),h),hb,cq,why))
auth={(r['branch_index'],r['helper_full'],r['source_age'],r['consumer_full'],tuple(r['consumer_input'])):r for r in J['all2484_q_first_consumer_queries']}
assert len(rows)==len(auth)==2484
for bi,helper,n,dst,slot,pose,hb,cq,why in rows:
 r=auth[bi,helper,n,dst,slot];assert tuple(r['consumer_pose'])==pose and tuple(r['HB_key'])==hb and tuple(r['count5_key'])==cq and r['reason']==why
counts_=Counter(r[-1]for r in rows);assert counts_==J['counts']['query_reasons']
assert set(case_facts)=={(c['branch_index'],c['helper_full'],tuple(c['q_helper_local']),tuple(c['main_helper_input_local']))for c in J['cases']}
out=dict(status='PASS independent protected-main and second-cohort elimination of D/W5 helper histories',manifest_sha256=hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),branches=[(a,xy(p),xy(o),xy(q),k)for a,p,o,q,k in branches],helper_case_facts=case_facts,queries=rows,reason_counts=dict(counts_),marker_overlap_check='Both helper main inputs lie outside the common M11 read set, retaining protection if a previous full context includes the helper marker.',scope='Given the independently signed late-helper gate, all9 source branches and2 helpers are impossible with no earlier original-D closed contact. Hence the proper D/W5 FIRST contact is excluded. The same conditional helper-history lemma applies to finalU only if its late-helper premise is independently proved. No general later-transfer, fuel, V1/U1 or capture conclusion.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items()if k not in['queries','branches','helper_case_facts']})
