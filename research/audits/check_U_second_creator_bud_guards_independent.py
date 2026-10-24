from pathlib import Path
from collections import Counter
import json,hashlib
S=Path(__file__).resolve();R=S.parents[1];D=R/'U_second_contact_creator_bud_guards_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();man=D/'manifest.json';assert sha(man)=='48646d833e63863b1538abe37d45e8a206f2373d4a751ae4ad1f63cbd54b3894'
for p,h in json.loads(man.read_text())['files'].items():assert sha(D/p)==h
ref=json.loads((D/'creator_bud_guards.json').read_text())
for p,h in ref['dependencies'].items():assert sha(R/p)==h
ns={'__file__':str(S.with_name('check_returned_U_deleted_guard_independent.py'))};exec(Path(ns['__file__']).read_text().split('\nC=json.loads')[0],ns);W,M,K,L,walk,xy,raw,AR,AC,AO,roles,sur=[ns[k]for k in('W','M','K','L','walk','xy','raw','AR','AC','AO','roles','sur')];bud=1+3j;g=2j
source=[]
for typ in('U','UC','UCC'):
 rr=raw[typ];bs=[(i,c)for i,(q,h,c)in enumerate(rr['reads'])if q==bud];gs=[(i,c)for i,(q,h,c)in enumerate(rr['reads'])if q==g];assert bs[-1]==(26,'R')and gs[-1]==(20,'L');source.append(dict(type=typ,bud_reads=bs,deleted_g_reads=gs))
# Fresh atomic output fields, including exact last-R identity and exitK removal.
for b in'DCVU':
 for q in AO[b]:
  rr=[(i,c)for i,(z,h,c)in enumerate(AR[b]['reads'])if z==q];assert rr and rr[-1][1]=='R'
 assert {q for q,h,c in AR[b]['reads'][:6]}==K
ports=[]
for b,p,ep in sur:
 local=(bud-p)/(-1j);req=AC[b]['req'].get(local);rr=[(i,c)for i,(q,h,c)in enumerate(AC[b]['reads'])if q==local];assert rr
 if req:
  assert(b,local,rr[0])in(('V',1+2j,(13,'L')),('U',3j,(23,'L')));why='genuine_s_age3_below_min5'
 else:assert(b,p,local,rr[0])==('U',-1+4j,1+2j,(17,'R'));why='genuine_s_BLACK_before_R'
 ports.append(dict(atom=b,entry=[*xy(p),1],exit=[*xy(ep),1],s_local=xy(local),first_s_read=rr[0],reason=why))
assert len(ports)==3 and len(roles)==38
# Bind independently signed full-source age law, not an anatomical-slot guess.
age=R/'word_stabilization/U_foreign_prefix_bud_cuts_frozen_20261023_2201/manifest.json';assert sha(age)=='adf3dfa34019a3ff443b22b6ca664fe918f4a8ce755b358fc61e5db16f14c956';signed_age=sha(S.with_name('check_U_foreign_prefix_buds_independent.json'))
F=json.loads((R/'second_ordinary_after_first_foreign_2026-10-24/old_U_second_contact_LEFT_frontier.json').read_text())['exact60_necessary_only_remaining_states'];rows=[];counts=Counter();remain=[]
for z in F:
 A,b1,b2=z['foreign'],z['first'],z['second'];p=complex(*z['foreign_pose'][:2]);h=z['foreign_pose'][2];r=(-1j)**h;clock=z['true_preforeign_age'];assert clock in(3,4);word=W[A]+W[b1]+W[b2];full=walk(word+M);assert full['feasible'];s=(bud-p)/r;sg=full['req'].get(s)
 if sg is False:
  why='genuine_s_BLACK_vs_combined_before_WHITE';first=next((i,c)for i,(q,hh,c)in enumerate(full['reads'])if q==s);assert first[1]=='R';t=first[0];off=0;owner=None
  for symbol in(A,b1,b2):
   if off<=t<off+len(W[symbol]):owner=(symbol,t-off,t-off+1);break
   off+=len(W[symbol])
  if owner is None:owner=('next actual word M11',t-len(word),t-len(word)+1)
 elif full['req'].get((g-p)/r)is True:
  why='source_deleted_g_no_rebirth_through_clock3';assert clock==3 and(g-p)/r not in K;first=None;owner=None
 else:why='necessary_only_not_excluded_here';remain.append(z);first=None;owner=None
 row=dict(foreign=A,first=b1,second=b2,foreign_pose=z['foreign_pose'],second_pose=z['second_pose'],classification=why,first_s_required_R=first,owner=owner);rows.append(row);counts[why]+=1
 rr=next(a for a in ref['all60_typed_cases']if all(a[k]==row[k]for k in('foreign','first','second','foreign_pose','second_pose')));assert rr['classification']==why
assert counts==ref['classification_counts']and len(remain)==12 and all(z['second']=='V'and z['second_pose']==[0,4,2]for z in remain)
assert Counter(z['true_preforeign_age']for z in remain)=={3:3,4:9}
p=4-3j;r=-1j;loc=(bud-p)/r;fc=walk(W['F']);allctx=walk(W['F']+W['D']+W['U']+M);assert loc not in fc['req'];assert next((i,c)for i,(q,h,c)in enumerate(allctx['reads'])if q==loc)==(63,'R')and 63-len(W['F'])==7
out={'status':'PASS48 of60 old-U second-contact frontier states excluded by preforeign creator cohort','manifest':sha(man),'signed_age_report':signed_age,'source_birth_deletion':source,'residual_origin_count':len(roles),'three_E3_origins_excluded':ports,'classification_counts':dict(counts),'all60_rows':rows,'remaining12':remain,'analytic_review':[
'The signed full-source U bud law is about exact s=(1,3), born U R26, entryclock0 shared by U/UC/UCC. Source tails preserve it. Signed1325 handles ages0..2 and actual full-input COUNT5 queries ages3/4, including core absorption. This law is used ONLY at preforeign cuts, never after A. The same source actually deletes g=(0,2) at L20 and its own tails preserve that deletion.',
'All60 complete A+b1+b2+actualM masks are recomputed from physical XOR reads.36 require s WHITE at FOREIGN entry, contradicting its original currentBLACK at clock3/4. All later toggles are already encoded in that entry mask. The F4,-3E,D,U1,2W prepared control truly misses s duringF and requires R at D7/read8, combined63; this identifies missing creating ancestry without invalidating the prepared replay.',
'Fresh exact atomic output fields and38 S/E alignments reproduce the signed deleted-g origin inventory. N0 y>=4 and W1 y-x>=5 exclude earlier origins; all S2 roles conflict with sector/held genuine star. E C4 cannot complete before clock3. Three E3 plain origins remain, but two physically consume original s at sourceclock3 and the third requires itWHITE, all forbidden by the separate genuine s law.',
'Residual-output exhaustiveness is valid at the final full foreign-entry cut with g outsideK. If a last-R birth is in its atomic exitK, the next actual atomic base reads allK within six RAW updates and deletes that very identity. If no next atom intervenes, g remains in foreignentryK, excluded by target premise. Any later R rebirth is a different last-R origin and is tested afresh. Thus no permanent core-to-residual identity export or omitted CORE writer bypasses the residual table.',
'Twelve further clock3 states require gBLACK outside foreignentryK and are excluded. The12 survivors all have secondV0,4S, three trueage3 with firstC and nine trueage4 otherwise. They remain necessary-only; no second simplicity, returned age law or universal tail permanence is asserted.'
]}
S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],counts)
