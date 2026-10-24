from pathlib import Path
from collections import Counter
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'foreign_Q_W5_deleted_core_guard_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'manifest.json';assert sha(MF)=='d3f96db60a6e0cfefa70315d97278360d346a8ebbbe33009e61f5cacdec78a71';mf=json.loads(MF.read_text())
for f,h in mf['files'].items():assert sha(D/f)==h
for f,h in mf['dependencies'].items():assert sha(R/f)==h
J=json.loads((D/'Q_W5_deleted_core_guard.json').read_text());ns={'__file__':str(S.with_name('check_old_V_second_age1_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Universal')[0],ns);W,M,K,tr,rot,xy,center,meet,pieces=[ns[k]for k in('W','M','K','tr','rot','xy','center','meet','pieces')]
qraw=tr(W['Q']);hole=-2j;physical=qraw['p']+rot(qraw['h'])*hole;assert physical==-4-2j and qraw['last'][physical]==tr(W['Q']+M)['last'][physical]==('L',56)and hole not in K;fore=[((a-2*qraw['p'])/rot(qraw['h']),(b-2*qraw['p'])/rot(qraw['h']))for a,b in pieces('Q')];hook={-3-3j,-2-3j,-1-3j,-1-2j};target=-1j;th=3
pre=[]
for a in'DCVU':
 raw=tr(W[a]);h=(th-raw['h'])%4;p=target-rot(h)*raw['p'];z=tr(W[a],p,h);assert z['p']==target and z['h']==th
 if a=='C':assert tr(W['C']+W['U']+M)['bad']is not None;continue
 loc=(hole-p)/rot(h);ctx=tr(W[a]+M);first=next((t,c)for t,(q,hc,c)in enumerate(ctx['reads'])if q==loc);assert loc not in K and first==(len(W[a])+1,'L')and loc not in tr(W[a])['last'];pre.append((a,p,h,loc))
assert [(a,xy(p)+[h],xy(loc))for a,p,h,loc in pre]==[(r['actual_previous_RAW'],r['actual_previous_head'],r['needed_hole_input'])for r in J['all3_actual_immediate_previous_RAW_BLACK_hole_obligations']]
rows={(r['atom'],r['k'],tuple(r['write'])):r for r in J['all208_last_RAW_R_origin_deadline_and_hook_FOREIGN_constraints']};seen=set();counts=Counter();remain=[]
for a in'DCVU':
 raw=tr(W[a]);ctx=tr(W[a]+M);writes={q:t for q,(c,t)in raw['last'].items()if c=='R'}
 for clock in range(6):
  if a=='C'and clock==5:continue
  h=(-clock)%4
  for q,t in writes.items():
   key=(a,clock,tuple(xy(q)));r=rows[key];seen.add(key);p=hole-rot(h)*q;assert r['head']==xy(p)and r['h']==h and r['R_tick']==t;z=tr(W[a],p,h);ch=(center(p,h),center(z['p'],z['h']))
   if(int(p.real+p.imag)+h)%2:why='sector'
   elif clock==0 and p.imag<0:why='N0_y_negative'
   elif clock==1 and p.imag<1:why='W1_below_y1'
   elif any((tag-p)/rot(h)in K or(tag-p)/rot(h)in ctx['req']for tag in hook):why='current_hook_context_hit'
   else:
    contacts=[(j,meet(*f,*ch))for j,f in enumerate(fore)if meet(*f,*ch)is not None]
    if contacts:why='earlier_FOREIGN_contact';assert p==-1j and h==1 and clock==3 and contacts==[(1,(1,0))]
    else:why='NECESSARY';remain.append((a,clock,p,h,q,t,z['p'],z['h']));assert r['exit']==xy(z['p'])+[z['h']]
   assert r['why']==why;counts[why]+=1
assert seen==set(rows)and len(seen)==208 and counts==J['counts'];assert{(a,c,p,t)for a,c,p,h,q,t,e,eh in remain}=={('C',2,2-2j,8),('V',2,2-2j,8),('U',2,2-2j,8),('V',4,-4j,12),('U',4,1-5j,22)}
cases=[]
for a,c,p,h,q,t,e,eh in remain:
 if c==4:
  assert e==1-1j and eh==0 and(hole-e)/rot(eh)==-1-1j and -1-1j in K
  for nxt in'DCVU':assert next((i,ch)for i,(z,hh,ch)in enumerate(tr(W[nxt]+M)['reads'])if z==-1-1j)==(2,'L')
  # Donor exits N atclock4. It cannot itself be the W clock5 predecessor.
  assert eh==0 and all((e,eh)!=(rp,rh)for ra,rp,rh,ri in pre)
 else:
  assert c==2 and p==2-2j and h==2 and q==2;ek={e+rot(eh)*z for z in K};assert hole not in ek and tr(W[a],p,h)['last'][hole]==('R',8)
  sch=(center(p,h),center(e,eh))
  for ra,rp,rh,ri in pre:
   re=tr(W[ra],rp,rh);rch=(center(rp,rh),center(re['p'],re['h']));row=next(x for x in J['all9_S2_donor_by_actual_predecessor_cases']if x['donor_RAW']==a and x['reader_previous_RAW']==ra);assert list(map(xy,sch))==row['actual_donor_chord']and list(map(xy,rch))==row['actual_reader_chord'];assert xy((rp-p)/rot(h))+[(rh-h)%4]==row['source_relative_reader']
   if a in'VU'and ra=='D':
    assert (rp-p)/rot(h)==1 and(rh-h)%4==1 and(p-rp)/rot(rh)==-1j and -1j in K
    # Actual fresh source origin is a last R external output: V r or U LEFT.
    sr=tr(W[a]);assert sr['last'][0j][0]=='R'and 0j not in{sr['p']+rot(sr['h'])*z for z in K};assert 5-c==3;kind='fresh_CURRENT_entry_CORE'
   else:
    contact=meet(*sch,*rch);assert contact is not None
    if a=='C'and ra=='D':assert contact==(1,0)and c+1==3<5;kind='nonadjacent_repeated_completed_C_EXIT'
    else:assert contact[1]>0 and str(contact[0])==row['old_s']and str(contact[1])==row['new_t'];kind='earlier_reader_RAW_contact'
   cases.append((a,ra,kind))
assert Counter(k for a,b,k in cases)=={'fresh_CURRENT_entry_CORE':2,'nonadjacent_repeated_completed_C_EXIT':1,'earlier_reader_RAW_contact':6}
out=dict(status='PASS Q W5 U-target funding exclusion under SIMPLE executed prefix through target ENTRY',manifest=sha(MF),script=sha(S),origin_counts=dict(counts),reader_cases=cases,analytic_review=['The actual Q hole is last ownL56 and remains physically WHITE, outside O/exitCORE. Exact inverse endpoints give all immediate predecessors D1,-2W,V3,-2W,U4,-1W; C is excluded by the actual CU literal conflict, not geometry. In all three, the hole is an UNREAD external input before predecessor ENTRY, captured into its exit CORE and physically consumed at the next actual U tick1. No unexecuted producer tail or initial BLACK funding is used.','Choose the LAST physical R before the required predecessor-entry cut. Every older update belongs to a completed RAW, and a last-R source must end R at this cell. All208 roles include every CORE write, actual marker ownership and source-C completion deadline. Hook715 under the stipulated SIMPLE Q/ordinary prefix excludes all earlier complete-context hits, including true external inputs.','The four geometric exclusions are nonadjacent returns to Q EXIT at a later clock3 ENTRY, not the legitimate clock0 successor. Two N4 CORE R births must undergo actual next-wordL2 while still before the clock5 W reader. Rebirth cannot evade the exhaustive LAST-R choice.','Remaining S2 donors are actual C/V/U commonR8 at2,-2S. Seven of nine reader pairs contradict already executed simplicity; the C EXITclock3 equals D ENTRYclock5 and is not immediate adjacency. The two fresh V/U-to-D cases have true source-relative age3 and D1,0E entryCORE contains SAME fresh origin. Signed9cf guards apply because the donor is AFTER Q and its whole intervening ordinary subarc is genuinely simple; no old-eight age crosses the foreign.','Conclusion applies only to this U0,-1W target atclock5 with actual terminal M, under simplicity THROUGH target ENTRY. Earlier ordinary selfcontacts are not allowed. It does not automatically cover a V target, whose immediate C-reader possibility requires a separate check, nor five hook-MISS gates, b1 owners, arbitrary-tail simplicity or capture.']);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
