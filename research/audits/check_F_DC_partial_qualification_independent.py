from pathlib import Path
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'original_F_piece_firstpost_DC_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'partial_scope_qualification_manifest.json';assert sha(MF)=='45abc7fa94ad82eb0b96c9cd726a1cd8621d26dc0d53a2d824ff8af291e451c1';mf=json.loads(MF.read_text())
for f,h in mf['files'].items():assert sha(D/f)==h
assert sha(D/'manifest.json')==mf['original_manifest_sha256'];base=S.with_name('check_original_F_piece_DC_independent.json');assert sha(base)=='45e79b98ccd9ca3159c7b566bd71ba7140903209beef641d4fe6ae68d279e108'and json.loads(base.read_text())['status'].startswith('HOLD')
J=json.loads((D/'partial_scope_qualification.json').read_text());orig=json.loads((D/'F_piece_DC.json').read_text());key=lambda r:(r['first_post_RAW'],r['actor'],*r['pose']);allkeys={key(r)for r in orig['all84_firstpostD_C_proper_F_contact_closures']};opened={key(r['original_row'])for r in J['all3_OPEN_N4_restoration_residues']};kept={key(r['original_row'])for r in J['all81_retained_exclusions']};assert opened=={('D','V',-1,-1,0),('D','U',-1,-1,0),('C','U',-1,-1,0)}and not opened&kept and opened|kept==allkeys and len(kept)==81
ns={'__file__':str(S.with_name('check_old_V_second_age1_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Universal')[0],ns);W,M,K,tr,rot,xy=[ns[k]for k in('W','M','K','tr','rot','xy')]
for rr in J['all81_retained_exclusions']:
 r=rr['original_row'];a=r['actor'];p=complex(*r['pose'][:2]);h=r['pose'][2]
 if p==-1-1j and h==0:
  assert key(r)==('C','V',-1,-1,0);local=(1+2j-p)/rot(h);f=next((c,t)for t,(q,hh,c)in enumerate(tr(W[a]+M)['reads'])if q==local);assert f==('R',15)and rr['independent_source_C_bud_guard']['actual_first']==list(f)
 else:assert r['K']in(2,3)or(r['K']==4 and p.imag<=-2)or(r['K']==5 and p.imag<=-1)
pairs=[]
for row in J['all6_literal_colour_consistent_loss_actor_pairs']:
 a,b=row['loss_RAW'],row['actor_RAW'];word=W[a]+W[b]+M;z=tr(word);assert not z['bad'];seed={q for q,v in z['req'].items()if v};assert sorted(map(xy,seed))==row['complete_minimal_seed'];g=complex(*row['old_input_local']);assert g in seed and g not in K;B={q:-i-1 for i,q in enumerate(sorted(seed,key=lambda q:(q.real,q.imag)))};old=B[g];p=0j;h=0
 for t,c in enumerate(word):
  if t==len(W[a]):assert B[g]==old and(g-p)/rot(h)in K
  if t==len(W[a])+1:assert p==g and c=='L'and B[g]==old
  assert(p in B)==(c=='L')
  if c=='R':B[p]=t
  else:del B[p]
  h=(h+(1 if c=='R'else-1))%4;p+=rot(h)*1j
 pairs.append((a,b,len(seed),len(word)))
assert {(a,b)for a,b,_,_ in pairs}=={(a,b)for a in 'DVU'for b in 'VU'}
O={'status':'PASS ONLY qualified81 exclusions and explicit3 OPEN active-CORE restoration residues; original full84 remains HOLD','manifest':sha(MF),'script':sha(S),'original_hold_report':sha(base),'retained_count':81,'open_keys':sorted(opened),'complete_local_pairs':pairs,'analytic_review':['The immutable original143d full84 and universal pair-current claims remain unsigned. Mandatory45abc7fa explicitly withdraws the false targetN4 y<=-2 statement and restricts the pair reserve to actual lowerN4 or negativeW5 targets and K2/3. All finite inventories and independent analytic checks in45e79b98 remain usable under that restricted premise.','Exact set equality84=81+3 is reconstructed. The special sourceC/V head closes by independent SAME C bud ownV R15; the other three same-entry V/U cases have no such anchor cut and remain necessary, not attained or excluded.','All six lossD/V/U thenactorV/U local full seeds are physically replayed. The old true-input identity is outside initialCORE, survives the lossRAW into its exitCORE, and dies at actual next-word tick1/read2. These prepared local positives show a genuine CORE-status gap, not a harmless endpoint convention, but supply no F/U ancestry.','The sourceD common reserve, lower negative-y guards, exact JO minimumFOUR plus zero-clock origin exclusion, and same-entry beta lift retain their independently reviewed scopes. No originalF-piece complete closure, arbitrary-tail simplicity or capture conclusion is promoted.']};S.with_suffix('.json').write_text(json.dumps(O,indent=2)+'\n');print(O['status']);print(sha(S.with_suffix('.json')))
