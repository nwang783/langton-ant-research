from pathlib import Path
from collections import Counter
import json,hashlib
S=Path(__file__).resolve();R=S.parents[1];D=R/'Q_C5_next_FOREIGN_loss_frontier_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'manifest.json';assert sha(MF).startswith('1c2ec933');mf=json.loads(MF.read_text())
for f,h in mf['files'].items():assert sha(D/f)==h
for f,h in mf['dependencies'].items():assert sha(R/f)==h
J=json.loads((D/'Q_C5_frontier.json').read_text());lib=S.with_name('check_old_V_second_age1_independent.py');ns={'__file__':str(lib)};exec(lib.read_text().split('# Universal')[0],ns);W,M,K,tr,rot,center,xy,pieces=[ns[k]for k in('W','M','K','tr','rot','center','xy','pieces')];G={a:tr(W[a])for a in W};C={a:tr(W[a]+M)for a in W};sort=lambda z:sorted(z,key=lambda p:(p.real,p.imag));first=lambda a,q:next(([c,t]for t,(p,h,c)in enumerate(C[a]['reads'])if p==q),None)
F15={-1-1j,-1+0j,-1+1j,0j,1j,1+0j,1+1j,1+2j,2+0j,2+1j,-4+1j,-4+2j,-3+2j,-2+1j,-2-1j};HK={-1-1j,-2-1j,-3-1j,-3-2j};field=(F15-{2+0j,2+1j})|HK;assert len(field)==15
# Actual Q reset/output identities and exact independently signed first completed repair candidates.
assert G['Q']['last'][-2]==('L',48)and G['Q']['last'][-4-2j]==('L',56)and G['Q']['last'][-3-2j]==('R',57)
prior=json.loads((R/'audits/check_FOREIGN_C5_rewrite_independent.json').read_text());assert prior['status'].startswith('PASS')
funders=prior['five_possible_hole_funders'];assert len(funders)==5 and all(z[0]==[-4,-2]for z in funders)
assert[z for z in funders if z[5][0]=='R']==[[[-4,-2],'C',[-6,-2,0],[-6,-1,3],8,['R',8],'possible_funder']]
assert all(z[2][2]==3 and z[4]==9 and z[5]==['L',5]for z in funders if z[5][0]=='L')
assert not[z for z in prior['all288_hole_final_R_origins']if z[0]==[-2,0]and z[-1]=='possible_funder']
# Same source-only ordinary two-turn theorem excludes the only COMPLETE C3 funding word.
sep=json.loads((R/'audits/check_two_turn_separation_independent.json').read_text());assert 'exact completed Q-C3 gate'in sep['status']
goals={}
for a in'FQB':
 for q,b in C[a]['req'].items():
  if not b:continue
  for g in HK:
   p=g-rot(1)*q
   if(int(p.real+p.imag)+1)%2:continue
   goals.setdefault((a,p),[]).append((g,q,first(a,q)[1]))
ref={(z['actor'],complex(*z['ENTRY'][:2])):z for z in J['all71_intact_pre_rewrite_recipient_rows']};assert set(goals)==set(ref)and len(goals)==71
counts=Counter();rows=[];opens=[]
for(a,p),hits in sorted(goals.items(),key=lambda z:(z[0][0],z[0][1].real,z[0][1].imag)):
 z=ref[a,p];assert {(tuple(xy(g)),tuple(xy(q)),t)for g,q,t in hits}=={(tuple(w['original_hook']),tuple(w['local']),w['actual_first_L']['context_tick0'])for w in z['possible_original_hook_first_L']}
 bad=[]
 for g in sort(field):
  q=(g-p)/rot(1);f=first(a,q)
  if q in K or f and f[0]=='R':bad.append((xy(g),xy(q),f,'ENTRY_CORE'if q in K else'first_WHITE'))
 if bad:why='intact_pre_field'
 elif p==-5-4j:
  assert first(a,(-2-p)/rot(1))==['L',35];why='SOURCE_L48_no_funder'
 elif p in(-6-5j,-3-6j):
  assert first(a,(-4-2j-p)/rot(1))==['L',17 if p==-6-5j else 51];why='SOURCE_L56_only_C3_repair_excluded'
 else:
  assert p==-4-7j and hits==[(-3-2j,-5+1j,38)] and G[a]['last'][-5+1j]==('L',38)
  ep=p+rot(1)*G[a]['p'];eh=(1+G[a]['h'])%4
  for g in field-{-3-2j}:assert (g-p)/rot(1)not in C[a]['req']and (g-ep)/rot(eh)not in K
  why='OPEN_exact_lower_hook_loss_gate';opens.append((a,p))
 assert why==z['route'];counts[why]+=1;rows.append((a,xy(p),[(xy(g),xy(q),t)for g,q,t in hits],why,bad))
assert counts==dict(intact_pre_field=59,SOURCE_L48_no_funder=3,SOURCE_L56_only_C3_repair_excluded=6,OPEN_exact_lower_hook_loss_gate=3)
interfaces=[]
for a,p in opens:
 for b in'VU':
  q=p-rot(1)*G[b]['p'];zz=tr(W[b]+W[a]+M,q,1)
  if zz['bad']is not None:assert b=='V'and a=='B';kind='literal_VB_conflict'
  else:kind='OPEN_actual_plain_BASE_interface';assert q==(-7-6j if b=='V'else-8-7j)
  ar=next(z for z in J['all6_last_BASE_types']if z['actor']==a and z['previous']==b);assert ar['previous_ENTRY']==[*xy(q),1]and ar['route']==kind;interfaces.append((b,a,xy(q),kind,zz['bad']))
separations=[]
for a,p in opens:
 for k,(c,d)in enumerate(pieces(a)):
  c=2*p+rot(1)*c;d=2*p+rot(1)*d
  for j,(u,v)in enumerate(pieces('Q')):
   assert max(c.real,d.real)<=-9<-7<=min(u.real,v.real)
   ar=next(z for z in J['all10_exact_SOURCE_Q_proxy_MISS_checks']if z['actor']==a and z['actor_piece']==k and z['old_Q_piece']==j);assert ar['actor_segment']==[xy(c),xy(d)]and ar['old_segment']==[xy(u),xy(v)];separations.append((a,k,j,xy(c),xy(d),xy(u),xy(v)))
assert len(separations)==10
controls=[]
for a,p0 in opens:
 ar=next(z for z in J['all3_prepared_recipient_only_positive_controls']if z['actor']==a);seed={p0+rot(1)*q for q,b in C[a]['req'].items()if b}|field;assert list(map(xy,sort(seed)))==ar['complete_seed'];assert len(seed)==ar['mass']
 board={q:['prepared_initial',xy(q)]for q in seed};p=p0;h=1;boards=[]
 for t,c in enumerate(W[a]+M):
  rr=ar['all_actual_reads'][t];assert rr['tick0']==t and rr['cell']==xy(p)and rr['turn']==c and rr['prior_identity']==board.get(p);assert(p in board)==(c=='L')
  if c=='L':del board[p]
  else:board[p]=['new_R',t]
  h=(h+(1 if c=='R'else-1))%4;p+=rot(h)*1j;boards.append(dict(cut=t+1,pose=[*xy(p),h],whole_BLACK=list(map(xy,sort(board)))))
  if t+1 in(len(W[a]),len(W[a]+M)):
   cc=next(z for z in ar['all_RAW_and_M_fields']if z['actual_read_count']==t+1);assert cc['pose']==[*xy(p),h]and cc['complete_BLACK']==list(map(xy,sort(board)))
   for g in field-{-3-2j}:assert board[g]==['prepared_initial',xy(g)]and (g-p)/rot(h)not in K
 assert -3-2j not in board and ar['all_actual_reads'][38]['prior_identity']==['prepared_initial',[-3,-2]]
 controls.append(dict(actor=a,seed_mass=len(seed),complete_seed=list(map(xy,sort(seed))),all_complete_boards=boards))
report=dict(status='PASS Q-only C5 next-FOREIGN original-hook physical-loss necessary single-head frontier, with OPEN ancestry',manifest=sha(MF),dependencies=mf['dependencies'],counts=dict(counts),all71_recipient_rows=rows,six_previous_plain_BASE_interfaces=interfaces,all10_old_Q_piece_separations=separations,three_prepared_complete_controls=controls,analytic_review=[
'Signedff4 is used as an exact two-state E5 split, not a generic hook-survival assertion. After ordinary U(-4,-3,E), lower originalR57 is already physically dead, and the signed71 renewed-field/exit rows exclude a later first deletion of the remaining originals. In the intact branch all15 selected old IDs remain CURRENT at completed ordinary cuts.',
'The existing288 physical final-R inventory is CORE-inclusive. L48 has no compatible completed repair. Q L56 has one first-R origin, actual completed C3(-6,-2,N)R8; every other W candidate begins with L5 and requires an earlier BLACK cut. Signed238 relative separation excludes this completed C3 for ANY source-Q ordinary section, without U ancestry or global simplicity. Partial attempted C3 can write before failure but is not a completed atom in the stipulated actual section.',
'Every possible firstL of an original hook in the next actual FOREIGN plus realM, including ENTRYCORE/marker roles, is reconstructed.71 exact poses split59 held-field,3 L48,6 Q-onlyL56,3 OPEN at(-4,-7,E). No sourceB lift: B really writes the Q-hole coordinate atR64.',
'The five real V/U predecessor interfaces follow the separately signed interval grammar; V/B alone is literal-impossible. These are local necessities, not a source-to-gate construction. Actual recipient F/Q/B first and last read of the lower hook isL38; every other selected original is complete-context-MISS and outside recipient RAW exitCORE.',
'All ten source-Q/recipient-piece pairs are strictly separated in doubled x, using actual corrected-center pieces. This proves only original-Q proxy MISS, not history simplicity, no ordinary contact, or GLOBALfirst contact.',
'Three complete33/34/37-cell recipient-only prepared boards independently replay all reads and every entire physical field. The lower input is prepared initialBLACK, not an attained sourceQ R57. Fourteen others remain SAME and CURRENT at RAW exit, physically SAME throughM; no missing source ancestry is silently supplied.',
'Only an OPEN necessary gate for first physical deletion by the completed nextFOREIGN is established. Earlier ordinary rewrite, failed partial deletion, reborn identities, furtherFOREIGN iteration and genericC5 transfer remain separate; no period/capture/controller conclusion.'
])
S.with_suffix('.json').write_text(json.dumps(report,indent=2,default=lambda z:xy(z)if isinstance(z,complex)else str(z))+'\n');print(report['status']);print(sha(S.with_suffix('.json')));print(counts,[(z['actor'],z['seed_mass'])for z in controls])
