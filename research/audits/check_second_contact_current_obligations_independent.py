from pathlib import Path
from fractions import Fraction as F
from collections import Counter,defaultdict
from itertools import product
import json,hashlib,math
P=Path(__file__);R=P.parent.parent;D=R/'second_contact_signed_obligations_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();mf=D/'manifest.json';assert sha(mf)=='bc2a9623bc2e3fc479a802ea11e01ef15112c91000a628dd6d8fa975ef8a2135';m=json.loads(mf.read_text())
for f,h in m['files'].items():assert sha(D/f)==h
for f,h in m['dependencies'].items():assert sha(R/f)==h
bp=P.with_name('check_old_V_second_age1_independent.py');ns={'__file__':str(bp)};exec(bp.read_text().split('# Universal')[0],ns);W,M,K,tr,rot,xy,center,G,meet,cross=[ns[k]for k in('W','M','K','tr','rot','xy','center','G','meet','cross')];raw=lambda s:''.join(W[a]for a in s);canon=lambda z:json.dumps(z,sort_keys=True);ref=json.loads((D/'signed_current_obligations.json').read_text());boxes=[];poses=[];bases=[];rank={'U':0,'V':1,'D':2,'C':2}
for old,n in(('D',3),('C',3),('V',3),('V',4)):
 a=center(0j,0);u=center(G[old]['p'],G[old]['h'])-a
 for b1,b2 in product('DCVU',repeat=2):
  N=n+(b1=='C');h=(2-N)%4
  if N>4 or(N==4 and rank[old]>=rank[b2])or(b1=='C'and b2=='U'):continue
  c=center(0j,h);v=center(G[b2]['p']*rot(h),(h+G[b2]['h'])%4)-c;den=cross(u,v);assert den
  cs=[(a+s*u-c-t*v)/2 for s in(0,1)for t in(0,1)];bounds=[(math.floor(min(z.real for z in cs)),math.ceil(max(z.real for z in cs))),(math.floor(min(z.imag for z in cs)),math.ceil(max(z.imag for z in cs)))];boxes.append(dict(old_source=old,true_preforeign_age=n,first=b1,second=b2,exact_corners=[[[F(z.real).numerator,F(z.real).denominator],[F(z.imag).numerator,F(z.imag).denominator]]for z in cs],integer_bounds=[list(z)for z in bounds]))
  for x in range(bounds[0][0],bounds[0][1]+1):
   for y in range(bounds[1][0],bounds[1][1]+1):
    if(x+y-N)%2:continue
    p=complex(x,y);z=c+2*p-a;s,t=F(cross(z,v),den),F(cross(z,u),den)
    if not(0<=s<1 and 0<t<=1):continue
    pose=[x,y,h];poses.append(dict(old_source=old,true_preforeign_age=n,first=b1,second=b2,second_pose=pose,old_s=[s.numerator,s.denominator],new_t=[t.numerator,t.denominator]))
    for A in'FQB':
     ha=(-n)%4;disp=tr(raw(A+b1),h=ha);ap=p-disp['p'];assert disp['h']==h;end=tr(W[A],ap,ha);ff=tr(W['F'],ap,ha);verts=[center(ap,ha),center(ff['p'],ff['h'])]
     if A!='F':verts.append(center(end['p'],end['h']))
     bbe=tr(W[b1],end['p'],end['h']);tt=tr(raw(A+b1+b2)+M);reason='foreign_contact'if any(meet(a,a+u,l,r)is not None for l,r in zip(verts,verts[1:]))else'b1_contact'if meet(a,a+u,center(end['p'],end['h']),center(bbe['p'],bbe['h']))is not None else'local_conflict'if tt['bad']else'keep';bases.append(dict(old=old,n=n,A=A,b1=b1,b2=b2,pa=[*xy(ap),ha],p2=pose,reason=reason,cuts=[]))
assert len(boxes)==44 and set(map(canon,boxes))==set(map(canon,ref['all44_angle_parallelograms']))and len(poses)==89 and set(map(canon,poses))==set(map(canon,ref['all89_outgoing_owned_contact_poses']))and len(bases)==267 and set(map(canon,bases))==set(map(canon,ref['all267_foreign_typed_base_rows']))
# Rebuild every real full-producer clock, final-R identity and independent signed currentness criterion.
roles={};facts_by_role={}
for z in ref['all15_genuine_source_role_current_fact_sets']:
 old,n,full=z['old_source'],z['true_preforeign_age'],z['actual_containing_full'];j=(z['selected_C_index1']-1)if old=='C'else 0;before=full[0]+'C'*j if old=='C'else'';entry=tr(raw(before));tau=-j;ft=tr(raw(full));exitK={ft['p']+q*rot(ft['h'])for q in K};O={q for q,(ch,t)in ft['last'].items()if ch=='R'and q not in exitK};transform=lambda q:(q-entry['p'])/rot(entry['h']);normO={transform(q)for q in O};assert[*xy(entry['p']),entry['h']]==z['selected_old_pose_in_full_frame']and z['actual_full_source_ENTRY_clock']==tau and z['full_entry_age_at_FOREIGN']==n-tau and z['actual_full_source_completion_clock']==tau+full.count('C')and set(map(tuple,z['all_normalized_full_output_cells']))==set(map(tuple,map(xy,normO)))
 expected=defaultdict(list)
 def add(q,rule,age):
  assert q in O and ft['last'][q][0]=='R';expected[transform(q)].append((rule,age,q,ft['last'][q][1]))
 for i,atom in enumerate(full):
  pre=tr(raw(full[:i]));post=tr(raw(full[:i+1]));ec=tau+i;ic=tau+max(i-1,0);beta=post['p']+(1-1j)*rot(post['h']);common=pre['p']+2*rot(pre['h']);assert ft['last'][beta]==('R',len(raw(full[:i+1]))-2)and ft['last'][common]==('R',len(raw(full[:i]))+8)
  if 0<=n-ec<=2:add(beta,'1325',n-ec)
  if 0<=n-ic<=2:add(common,'1344',n-ic)
 if full in('VCC','UCC')and n-tau<=4:
  pre=tr(raw(full[:2]));add(pre['p']+(1-1j)*rot(pre['h']),'1319',n-tau)
 if old=='V':
  if n<5:add(0j,'2036',n)
  if n<4:add(1+0j,'2043',n)
 supplied={complex(*f['cell']):f for f in z['guaranteed_CURRENT_facts']};assert set(supplied)==set(expected)
 for q,es in expected.items():
  f=supplied[q];assert f['actual_full_output_slot']==xy(es[0][2])and f['actual_full_last_R_tick0']==es[0][3];got=[]
  for p in f['proofs']:
   rule=p['signed_rule'][:4];age=p['true_post_EXIT_age']if rule=='1325'else p['true_atomic_ENTRY_age']if rule=='1344'else p['full_entry_age']if rule=='1319'else p['actual_full_source_entry_age'];got.append((rule,age))
  assert sorted(got)==sorted((rule,age)for rule,age,_,_ in es)
 roles[z['role_key']]=z;facts_by_role[z['role_key']]=set(expected)
assert len(roles)==15
# The true age2 cleanup helper's six V-base outputs, preserved by actual VC, at foreign3 age1.
v=tr(W['V']);vk={v['p']+q*rot(v['h'])for q in K};VO={q for q,(ch,t)in v['last'].items()if ch=='R'and q not in vk};helper={4j-q for q in VO};assert len(helper)==6
for source in('V','VC'):
 t=tr(raw(source));core={t['p']+q*rot(t['h'])for q in K}
 for q in VO:assert t['last'][q]==v['last'][q]and q not in core
assert set(map(tuple,map(xy,helper)))=={tuple(z['cell'])for z in ref['genuine_V_A_cleanup_helper_six_literal_base_outputs']}
queries=json.loads((R/'audits/dcuv_count5_replay/queries.json').read_text());assert min(z['certified_minimum_C_age']for z in queries['slots'].values())>=2
basekeys={(b['old'],b['n'],b['A'],b['b1'],b['b2'],tuple(b['pa']),tuple(b['p2'])):b for b in bases};summ=defaultdict(Counter);statecounts=Counter();ownerchecks=0

def own(T,t,z):
 global ownerchecks
 ownerchecks+=1;lo=0
 for i,a in enumerate(T):
  if t<lo+len(W[a]):assert(z['actual_atom_index0'],z['actual_atom'],z['atom_start_tick0'],z['canonical']['context_tick0'])==(i,a,lo,t-lo);return
  lo+=len(W[a])
 assert z['actual_atom']=='next actual word'and z['next_word_tick0']==t-lo and z['next_word_read_number1']==t-lo+1
for row in ref['all963_role_specific_causal_mask_obligations']:
 role=roles[row['source_role']];key=(row['old_source'],row['true_preforeign_age'],row['foreign'],row['first'],row['second'],tuple(row['foreign_pose']),tuple(row['second_pose']));b=basekeys[key];fixed=facts_by_role[row['source_role']];assert key[:2]==(role['old_source'],role['true_preforeign_age']);T=row['foreign']+row['first']+row['second'];tt=tr(raw(T)+M);p=complex(*row['foreign_pose'][:2]);h=row['foreign_pose'][2];first={}
 for i,(q,hh,ch)in enumerate(tt['reads']):first.setdefault(q,(ch,i))
 if b['reason']!='keep':assert row['classification']=='earlier_first_return_source_contact'and not row['states'];summ[row['source_role']][row['classification']]+=1;continue
 variants=[fixed|{1j},fixed|helper]if key[:2]==('V',3)else[fixed];assert len(variants)==len(row['states']);ex=[]
 for current,state in zip(variants,row['states']):
  hits=[]
  for q in current:
   local=(q-p)/rot(h);fr=first.get(local)
   if local in K:hits.append((tuple(xy(q)),'foreign ENTRY core',None))
   elif fr and fr[0]=='R':hits.append((tuple(xy(q)),'actual combined first read requires WHITE',fr[1]))
  supplied=[]
  for hh in state['exact_current_fact_conflicts']:
   t=hh.get('combined_tick0');supplied.append((tuple(hh['same_current_cell']),hh['conflict'],t))
   if t is not None:own(T,t,hh['actual_read_owner'])
  assert set(hits)==set(supplied);cut=bool(hits);assert state['classification']==('excluded_by_signed_CURRENT_fact'if cut else'necessary_unresolved_state');statecounts[state['state'],cut]+=1;ex.append(cut)
  if not cut:
   remaining={complex(*q)for q in role['all_normalized_full_output_cells']}-current;items=[z for z in state['unresolved_retirement_replacement_or_entry_core_obligations']if'original_full_source_cell'in z]+state['dormant_source_outputs_explicitly_retained'];assert{complex(*z['original_full_source_cell'])for z in items}==remaining
   for it in items:
    q=complex(*it['original_full_source_cell']);local=(q-p)/rot(h);fr=first.get(local)
    if fr:assert it['actual_combined_first_read']==list(fr)if local not in K else True
    if'actual_read_owner'in it:own(T,fr[1],it['actual_read_owner'])
 rowclass='all_causal_states_excluded'if all(ex)else'necessary_unresolved_state';assert row['classification']==rowclass;summ[row['source_role']][rowclass]+=1
assert{r:dict(s)for r,s in summ.items()}==ref['exact_summary_by_real_source_role']
# Priority V4 standalone projection, with literal read owners rather than ages afterforeign.
v4=[b for b in bases if(b['old'],b['n'])==('V',4)];assert len(v4)==18 and Counter(b['reason']for b in v4)=={'keep':12,'b1_contact':6}and all(b['p2']==[0,0,2]for b in v4)
for b in v4:
 if b['reason']!='keep':assert b['b1']=='U';continue
 T=b['A']+b['b1']+b['b2'];tt=tr(raw(T)+M);p=complex(*b['pa'][:2]);h=b['pa'][2];local=-p/rot(h);fr=next((i,ch)for i,(q,hh,ch)in enumerate(tt['reads'])if q==local);assert fr==(len(W[b['A']])+({'D':6,'V':14}[b['b1']]),'R')
err=D/'core_status_qualification_manifest.json';assert sha(err)=='389fec8938535834da396fd12cddceef681e45c3a1ada0bbc66f3b545858b8d2';em=json.loads(err.read_text())
for f,h in em['files'].items():assert sha(D/f)==h
out={'status':'PASS current-fact exclusions and exact role/geometry table; unresolved ENTRYCORE language qualified as same-original alive-CORE allowed','manifest_sha256':sha(mf),'mandatory_core_status_qualification_sha256':sha(err),'dependencies':m['dependencies'],'boxes':44,'poses':89,'base_rows':267,'real_roles':15,'role_mask_rows':963,'owner_checks':ownerchecks,'source_summary':{r:dict(s)for r,s in summ.items()},'state_counts':[{ 'state':k[0],'excluded':k[1],'count':v}for k,v in statecounts.items()],'analytic_review':['All44 exact angle windows/89 outgoing-owned poses/267 types regenerated with true age n and geometricN=n+[b1=C], source0<=s<1/new0<t<=1. All retained windows are nonparallel. Six oldV4 b1U cases already touch old source, not new secondcontacts.','Every one of15 actual full-source roles has independent last-R/output/core reconstruction and actual atomic entry/EXIT clocks. SelectedC2 full-entry-1 and foreignfullage4 retained;1325 own selectedC EXIT1 age2 is current atn3, whereas bareD/V EXIT0 age3 gives no protection.1344 commonentryage<3 and specific1319 VCC/UCC C1fullage<5 used only where valid.','AtV3 originalr andB remain current. IfA was retired, signed2043 uniquely forces genuine V/VC0,4S at2; all six actual base outputs are CURRENT atforeign3 by universal minimum2, with ownC preservation independently checked. This is a beforeFOREIGN disjunction, not a postforeign maturation law. All141 helper-state masks fail; originalA-current leaves27 per source tail.','All963 role rows and every stored exact first-read owner/current conflict recomputed. Unprotected sourceoutputs remain unresolved; ENTRYCORE must mean no longer CURRENT external, NOT necessarily physicaldeath: the same R-born identity can be alive insideCORE. This semantic qualification is mandatory and does not change any cut.','OldV4 closes independently of the larger unresolved table: all3 source tails preserve originalr throughage4<5; six placements are earlierb1contact, twelve have firstb1D tick6/read7 or b1V tick14/read15 requiring originalrWHITE. No postforeign age.','Only the stated first second-RAW contact slices/current-obligation table are certified. No arbitrary-tail induction, source-output seal, attained histories, or general second simplicity.']};P.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(P),sha(P.with_suffix('.json')))
