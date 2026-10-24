from pathlib import Path
from collections import Counter
import json,hashlib,ast
S=Path(__file__);R=S.parents[1];D=R/'C4_foreign_original_hook_loss_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();mf=D/'manifest.json';assert sha(mf)=='b961b00983e47a7fdd72df064943a2003470b6edc5a5e3ceb6eee38a773c6958';m=json.loads(mf.read_text())
for f,h in m['files'].items():assert sha(D/f)==h
for f,h in m['dependencies'].items():assert sha(R/f)==h
J=json.loads((D/'C4_original_hook_loss.json').read_text());A=J['theorem_A_15_output_reserve_through_C3'];B=J['theorem_B_all_C4_original_hook_loss'];ns={'__file__':str(S.with_name('check_old_V_second_age1_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Universal')[0],ns);W,M,K,tr,rot,xy=[ns[k]for k in('W','M','K','tr','rot','xy')];G={a:tr(W[a])for a in W};C={a:tr(W[a]+M)for a in W};I={a:{q for q,b in C[a]['req'].items()if b and q not in K}for a in W};O={a:{q for q,(c,t)in z['last'].items()if c=='R'}-{z['p']+rot(z['h'])*q for q in K}for a,z in G.items()};pose=lambda p,h:[*xy(p),h];ff=lambda a,q:next(([c,i]for i,(v,h,c)in enumerate(C[a]['reads'])if v==q),None)
F15={complex(*q)for q in A['unspent_current_originals']};old13={complex(*q)for q in A['paired_retained13']};new9={complex(*q)for q in A['paired_new9']};hook={-1-1j,-2-1j,-3-1j,-3-2j};assert len(F15)==15 and old13==F15-{2+0j,2+1j}and new9=={3-1j+q for q in O['U']}and len(new9)==9 and not old13&new9 and max(q.imag for q in old13|new9)==2
for a,row in zip('FQB',A['all3_source_births']):
 assert F15<=O[a]and G[a]['last'][-4+3j]==('L',35)and G[a]['h']==2 and G[a]['p'].imag<=-2;assert row['EXIT']==pose(G[a]['p'],2)
 assert row['all15_actual_source_R_births']==[dict(cell=xy(q),own_tick0=G[a]['last'][q][1])for q in sorted(F15,key=lambda q:(q.real,q.imag))]
for q in old13:assert q-(3-1j)not in C['U']['req']and q-(3-1j)not in K
assert not I['C'];cnt=Counter();gates=[]
for h in(0,3):
 for tag in sorted(F15,key=lambda q:(q.real,q.imag)):
  for a in'DVU':
   for slot in I[a]:
    p=tag-rot(h)*slot;au=next(z for z in A['all240_joint_first_CURRENT_loss_rows']if z['heading']==h and z['original']==xy(tag)and z['consumer']==a and z['ENTRY']==pose(p,h));assert au['true_input']==xy(slot)and au['actual_L']['context_tick0']==ff(a,slot)[1]
    if(int(p.real+p.imag)+h)%2:why='sector'
    else:
     bad=[]
     for q in sorted(F15,key=lambda q:(q.real,q.imag)):
      loc=(q-p)/rot(h);f=ff(a,loc)
      if loc in K or f and f[0]=='R':bad.append(dict(original=xy(q),local=xy(loc),first=f,reason='ENTRY_CORE'if loc in K else'first_WHITE'))
     assert bad==au['conflicts'];why='held_field'if bad else'first_loss_gate'
     if not bad:gates.append((h,a,pose(p,h),xy(tag)))
    assert why==au['route'];cnt[h,why]+=1
assert len(gates)==5 and cnt==Counter({(0,'sector'):54,(0,'held_field'):64,(0,'first_loss_gate'):2,(3,'sector'):66,(3,'held_field'):51,(3,'first_loss_gate'):3})
# Every physical R support includes temporary and CORE writes; endpoint inequalities are universal per RAW.
for a,row in zip('DCVU',A['all_ordinary_physical_R_supports']):
 rr=[]
 for t,(q,h,c)in enumerate(G[a]['reads']):
  if c!='R':continue
  assert q.imag>=0 and q.real>=-1
  if a=='C':assert q.real>=0
  else:assert q.imag<=G[a]['p'].imag
  rr.append(dict(own_tick0=t,physical_local_cell=xy(q)))
 assert rr==row['all_physical_R_supports']
for a in'DVU':
 assert all(q.imag>=1 and q.real>=-1 for q in I[a])
 assert all(q.imag>=0 and q.real>=-1 for q,h,c in G[a]['reads']if c=='R')
# LeftWgate needs source physical L35 hole, without any preceding repair in that gate.
loc=(-4+3j-(-2+3j))/rot(3);assert loc==2j and ff('U',loc)==['L',12]
# Independently solve every cited S4 retirement equation, retaining UNKNOWN endpoints.
proofs={};proofrows=[]
for key,row in B['all_S4_tag_endpoint_proofs'].items():
 gg,pp=ast.literal_eval(key);g=complex(*gg);p=complex(*pp[:2]);assert row['tag']==list(gg)and row['S4_cut']==list(pp)and pp[2]==2;possible=False;seen=set()
 for a in'DVU':
  for slot in I[a]:
   ep=g+slot;xp=ep-G[a]['p'];sector=(int(ep.real+ep.imag)+2)%2==0;dx=int(xp.real-p.real);dy=int(xp.imag-p.imag);counts=[]
   if sector and dx>=0 and dy>=0:
    for v in range(dx+1):
     d=dx-v;rem=dy-d-3*v
     if rem>=0 and rem%4==0:counts.append([d,v,rem//4])
   counts.sort();au=next(z for z in row['all8_first_loss_exit_rows']if z['consumer']==a and z['input']==xy(slot));assert au['ENTRY']==pose(ep,2)and au['RAW_EXIT']==pose(xp,2)and au['active_sector']==sector and au['remaining_S_count_tuples']==counts and au['actual_L']['context_tick0']==ff(a,slot)[1];possible|=bool(counts);seen.add((a,slot))
 assert len(seen)==8 and row['guaranteed_CURRENT']==(not possible);proofs[g,p]=not possible;proofrows.append((key,not possible))
assert len(proofs)==650
used=set()
def guaranteed(g,p):
 assert(g,p)in proofs;used.add((g,p));return proofs[g,p]
def conflicts(a,p,field):
 ans=[]
 for g in sorted(field,key=lambda q:(q.real,q.imag)):
  if not guaranteed(g,p):continue
  loc=p-g;f=ff(a,loc)
  if loc in K or f and f[0]=='R':ans.append((g,loc,'ENTRY_CORE'if loc in K else'first_WHITE',f))
 return ans

def check_conflicts(ans,rows):
 assert[(xy(g),xy(loc),why,f)for g,loc,why,f in ans]==[(r['guaranteed_CURRENT_original'],r['local'],r['reason'],r['actual_first'])for r in rows]
 for g,loc,why,f in ans:assert any(B['all_S4_tag_endpoint_proofs'][r['current_endpoint_proof']]['tag']==xy(g)for r in rows)
summary=[];carried=[];allposes=0
for source in'FQB':
 selected={-1-1j,-2-1j}if source=='F'else hook;goals={}
 for a in'FQB':
  for g in sorted(selected,key=lambda q:(q.real,q.imag)):
   for slot,b in C[a]['req'].items():
    if not b:continue
    p=g+slot
    if(int(p.real+p.imag)+2)%2:continue
    goals.setdefault((a,p),[]).append((g,slot,ff(a,slot)[1]))
 assert len(goals)==(49 if source=='F'else 68)
 for branch,field0 in [('unspent',F15),('N2_paired',old13|new9)]:
  field=field0|selected;rr=next(z for z in B['source_branch_cases']if z['source']==source and z['C3_state_branch']==branch);assert sorted(map(xy,field))==rr['all_current_at_S4_start'];rows={(z['actor'],complex(*z['FOREIGN_ENTRY'][:2])):z for z in rr['all_recipient_pose_rows']};assert set(rows)==set(goals);counts=Counter()
  for(a,p),wits in goals.items():
   row=rows[a,p];assert[(xy(g),xy(q),tm)for g,q,tm in wits]==[(z['original_hook_cell'],z['first_L_slot'],z['actual_L']['context_tick0'])for z in row['possible_same_original_first_L']];bad=conflicts(a,p,field)
   if bad:assert row['route']=='FOREIGN_current_field';check_conflicts(bad,row['conflicts']);counts['FOREIGN_current_field']+=1;continue
   assert row['route']=='last_actual_base_split'
   for pre in'VU':
    au=next(z for z in row['previous_types']if z['previous']==pre);pair=tr(W[pre]+W[a]+M)
    if pair['bad']is not None:assert au['route']=='previous_FOREIGN_literal_conflict';counts['previous_FOREIGN_literal_conflict']+=1;continue
    pp=p+G[pre]['p'];assert au['previous_ENTRY']==pose(pp,2);alive=[(g,q,tm)for g,q,tm in wits if pp-g not in G[pre]['last']]
    if not alive:assert au['route']=='previous_RAW_already_touched_every_original_candidate';counts['previous_RAW_already_touched']+=1;continue
    bad=conflicts(pre,pp,field)
    if bad:assert au['route']=='previous_current_field';check_conflicts(bad,au['conflicts']);counts['previous_current_field']+=1;continue
    assert au['route']=='carried_SAME_BLACK_through_previous_RAW';carry=[]
    for g in sorted(field,key=lambda q:(q.real,q.imag)):
     if not guaranteed(g,pp):continue
     f=ff(a,p-g)
     if pp-g not in G[pre]['last']and f and f[0]=='R':carry.append((g,pp-g,p-g,f[1]))
    assert carry and [(xy(g),xy(lp),xy(la),tm)for g,lp,la,tm in carry]==[(z['original'],z['previous_local_cell'],z['FOREIGN_local_cell'],z['actual_first_WHITE']['context_tick0'])for z in au['conflicts']];assert a=='B'and pre=='U'and carry[0][0]==-1-1j and carry[0][3]==(70 if source=='F'else 80);carried.append((source,branch,pose(p,2),pose(pp,2),carry[0][3]));counts['carried_SAME_BLACK']+=1
  assert dict(counts)==rr['disjoint_cut_counts'];allposes+=len(goals);summary.append(dict(source=source,branch=branch,poses=len(goals),counts=counts))
assert allposes==370
for row in J['all15_FOREIGN_exitCORE_capture_checks']:
 a=row['actor'];q=complex(*row['RAW_EXIT_CORE_cell']);assert q in{G[a]['p']+rot(G[a]['h'])*k for k in K}and row['in_ENTRY_CORE']==(q in K);assert row['RAW_last_read']==(list(G[a]['last'][q])if q in G[a]['last']else None)and row['complete_first_read']==ff(a,q)
 if q not in K and q not in G[a]['last']:assert q in I[a]and ff(a,q)[0]=='L'
O=dict(status='PASS fifteen-tag ordinary-C3 reserve and next-complete-FORE original-hook physical-loss exclusion at exact ordinaryC4; conditional CURRENT transfer only',manifest=sha(mf),script=sha(S),first_loss_counts={str(k):v for k,v in cnt.items()},five_gates=gates,endpoint_proofs=len(proofs),source_branches=summary,carried_black_residues=carried,analytic_review=[
'All fifteen shared sourceoutputs are actual lastR externalidentities and leftfundinghole is genuinely lastL35. S0/E1 inputcones lie below these tags. The full240 N2/W3 firstloss roles retain simultaneoustrueinputs. The known N2pairedU leaves13old+9NEW outputs withy<=2, below remainingN/C/W inputs. The known rightWgate uses signedL28hole; leftU(-2,3) needs L35hole(-4,3) at ownL12. Every physicalR support, including temporary/COREwrites, gives completedN exit>=3 thenW>=4, or C3/W exitx<=-4 unable to reachgatex-2. No chronologicalfundingorigin was limited toresidualoutputs.',
'At S4start, F15 or13old+9new plus signedQBhook is CURRENT. FourthC I0 cannot absorbanexternalcurrenttag. Each of650 tag/cutfrontiers independently retains all8 actualDVU inputs and solves the exactnonnegativeS displacementsemigroup. Emptysets giveCURRENT; possiblelosses remainUNKNOWN. No wordlength/age/simpleprefix assumption enters.',
'Every physicallyalive original must firstreadL if nextFOREdeletesit. Goalcover includesENTRYCORE and markerfirstL, producing49F/68Q/68B poses perbothbranches=370. Signedintervalgrammar with fourCs guarantees an actual finalplainV/U. A previousRAWtouch destroys the OLD identity even if it recreatesBLACK; only physicalRAWmiss carriesanoldidentity forward. This is not an assumption that oldtags stayCURRENTthroughordinaryS4.',
'All sourcefield and previousword masks reconstruct. FinalB residues carry SAME sourceR46 from guaranteedCURRENTatpreviousU ENTRY through its physicallyunreadRAW. SourceF failsB ownR70; QB failscontextR80, the actualfollowingwordtick6/read7. A priorpartialmarkerL mayalreadydeleteanotherhook, but then the stipulatedcompleteM fails. Completion and firstphysicaldeletion, not poseunreachability, are the conclusions.',
'All15 exitCOREpositions independently checked. Conditional on allfourQB originals CURRENTatrecipientENTRY, no deletion plus these actualcaptureports givesCURRENTatRAWexit and sameBLACKthroughrealM. Signed715 can supplyENTRYonlyunderitsactualcontact-freeprefixhypothesis. No unconditionalC4seal, furtherFOREiteration, C5, initialUstar, wholefieldbound, simplicityorcapture follows.'])
S.with_suffix('.json').write_text(json.dumps(O,indent=2)+'\n');print(O['status']);print(summary);print(sha(S.with_suffix('.json')))
