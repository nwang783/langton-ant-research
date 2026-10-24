from pathlib import Path
import json,hashlib
P=Path(__file__);R=P.parent.parent;S=R/'U_first_V_preforeign_shadow_ports_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();mf=S/'manifest.json';assert sha(mf)=='1dc72572ce5eb34c18958ea7b8aff35bdccbd566579f3717ad06c48316ae4382';m=json.loads(mf.read_text())
for f,h in m['files'].items():assert sha(S/f)==h
ref=json.loads((S/'preforeign_shadow_ports.json').read_text())
for f,h in ref['dependencies'].items():assert sha(R/f)==h
assert sha(P.with_name('check_second_V_first_helper_closure_independent.json'))=='27a48e0a4c8db00d486e8b9e676b6f1401964f633d75a50a9b927784d763ab77'
ns={'__file__':str(P.with_name('check_second_V_first_helper_closure_independent.py'))};exec(Path(ns['__file__']).read_text().split('maskrows=[]')[0],ns)
W,M,K,walk,xy,center,continuations=[ns[k]for k in('W','M','K','walk','xy','center','continuations')];full=lambda seq:walk(''.join(W[a]for a in seq));r=4j;B=1+4j;q=-1+2j;G=-1+4j
entry=-1+5j;ek={entry-z for z in K};assert not{r,B,q}&ek
old=json.loads((R/'U_second_V_first_helper_cohort_closure_2026-10-24/first_helper_cohort_closure.json').read_text());reused=ref['first_V_A_cleanup_continuation_reused_from_signed_nine'];assert reused['plainV_all8']==old['plain_V_A_cleanup_all8_continuations']and reused['VC_all8']==old['VC_A_cleanup_all8_continuations']
adj=[]
for A in'FQB':
 z=walk(W['V']+W['C']+W[A]+M);assert not z['feasible'];adj.append(dict(foreign=A,conflict_tick=z['i'],cell=xy(z['q'])))
# Same original q consumer at(-1,5,S) installs a genuine full-output A, preserved by own C.
for C in('V','VC'):
 t=full(C);assert [(i,c)for i,(p,h,c)in enumerate(t['reads'])if p==1j][-1]==(11,'R')and(-1+5j)-1j==G
# The only possible shadow consumer before age4 is translated relative A cleanup.
helper=-1+1j;ht=0;t=full('V');end=helper+t['p'];assert center(end,t['h'])==center(4j,0)==-1+7j
assert center(helper,0)==-3+1j and center(end,t['h'])==-1+7j # nonadjacent old-U exit, not a source-start relabel.
f=walk(W['F']+M);effects=[]
for name,z in [('q',q),('r',r),('q_cleanup_shadow_A',G),('first_V_A',5j),('first_V_B',B)]:
 local=z-(4+5j);reads=[(i,c)for i,(p,h,c)in enumerate(f['reads'])if p==local];x=dict(port=name,cell=list(xy(z)),FOREIGN_local=list(xy(local)),before_BLACK=f['req'].get(local),all_combined_reads=list(map(list,reads)));effects.append(x)
assert effects==ref['FOREIGN_F4_5N_corollary']['effect_rows'];assert effects[0]['all_combined_reads'][0]==[62,'R']and effects[2]['all_combined_reads'][0]==[54,'R'];assert effects[1]['all_combined_reads']==[[51,'L'],[55,'R'],[59,'L']]
assert len(W['F'])==56 and 62-56==6 and 59-56==3
qmf=R/'old_V_age1_scope_qualification_2026-10-24/manifest.json';assert sha(qmf)=='b6642b71d66d70d1b95b573ae97438deaa55f463fa6074b6b22a9970bab365b8'
out=dict(status='PASS portable genuine preforeign q-current/r-current or q-lost/cleanup-A-current boundary through age4; F4,5N excluded with actual M11',manifest_sha256=sha(mf),dependencies=ref['dependencies'],independent_all16_cleanup_continuations=continuations,immediate_plainV_foreign_exception=dict(pose=[-1,5,2],clock=2,held_q_r_B_outside_core=True,original_B_first_retirement_clock=4),VC_foreign_literal_cuts=adj,shadow_consumer_repeated_oldU_exit=list(xy(center(end,t['h']))),exact_F_context_effects=effects,old_V_age1_scope_addendum=sha(qmf),analytic_review=['Assumes the actual plainU then genuine V/VC/VCC at0,4N; no first-helper funnel is silently extended to arbitrary histories. Old factor simplicity and true source-clock<=4 are explicit.','The signed all-age A/B tables and r lock are used only inside old complete-eight history. If originalq remains current, both cleanup continuations use the signed deleted-g/full-output min3 argument or actual q absorption. Direct foreign after plainV atclock2 is RETAINED; B cannot retire before4 and is outside actual entryK, so r stays current.','After VC cleanup atclock3, any old fullpacket commonR8 needs qWHITE, and direct F/Q/B is genuinely literal pair-forbidden. This does not insert standalone C or silently execute a marker.','First originalq loss includes ordered core absorption, not just physical death; signed1954/2027 gives actual V/VC cleanup atclock2 and its NEW A identity. Its only possible first retirement atclock4 repeats old creatingU exit in actual old simple path. Thus genuine shadow stays current through foreignentry; no replacement identified with originalq.','At F4,5N q requiresWHITE only in actual following-word tick6/read7; shadow requiresWHITE in FRAW54/read55. These are full-context compatibility constraints, not already executed future reads. Actual r can L51/R55 enterEXITCORE and nextL3 retire replacement, explicitly retained.','No postforeign r/shadow persistence, no arbitrary-tail beforemask reuse, no foreign-star or allsource closure. The separate oldVage1 addendum only clarifies U-before-selectedVC; all four laterU occurrences remain genuine and outside that ancestry claim.'])
P.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
