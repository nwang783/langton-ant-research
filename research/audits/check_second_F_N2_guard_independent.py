from pathlib import Path
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'second_F_N2_common_output_guard_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'manifest.json';assert sha(MF)=='956b495cd4fb9876c6ce6b6b06fcc78c39d9a2f98bbb3af3558cb142b6970e32';mf=json.loads(MF.read_text())
for k,b in [('files',D),('dependencies',R)]:
 for f,h in mf[k].items():assert sha(b/f)==h
J=json.loads((D/'second_F_N2_gate.json').read_text());ns={'__file__':str(S.with_name('check_old_V_second_age1_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Universal')[0],ns);W,M,K,tr,rot,xy,center,meet,pieces=[ns[k]for k in('W','M','K','tr','rot','xy','center','meet','pieces')];raw={a:tr(W[a])for a in W};ctx={a:tr(W[a]+M)for a in W};first=lambda z,q:next((c,t)for t,(p,h,c)in enumerate(z['reads'])if p==q);I={a:{q for q,b in ctx[a]['req'].items()if b and q not in K}for a in 'DCVU'};assert sum(map(len,I.values()))==8 and not I['C']
b=2+4j;s=1+3j;target=3+3j;u=raw['U'];assert(u['p'],u['h'])==(4j,0)and u['last'][s]==('R',26)
for r in J['all3_actual_first_FOREIGN_b_and_s_birth_interfaces']:
 a=r['first_foreign'];z=tr(W[a],4j,0);exitK={z['p']+rot(z['h'])*q for q in K};assert z['last'][b]==('R',8)and s-4j not in ctx[a]['req']and b not in exitK and s not in exitK and z['p'].real<=-3 and z['p'].imag<=2 and z['h']==2 and r['actual_EXIT']==xy(z['p'])+[2]
ports=[];captures=[]
for a in 'DCVU':
 z=raw[a];ko={z['p']+rot(z['h'])*q for q in K}
 for q in ko:
  if q not in K and q not in z['last']:assert q in I[a] and first(ctx[a],q)[0]=='L'
  captures.append((a,tuple(xy(q)),q in K,z['last'].get(q),first(ctx[a],q)if q in ctx[a]['req'] else None))
 for q in I[a]:
  delta=z['p']-q;assert -q.real<=1 and delta.imag>=0
  if delta.imag==0:assert delta.real==1
  ports.append((a,tuple(xy(q)),first(ctx[a],q)[1],-int(q.real),tuple(xy(delta))))
assert set(ports)=={(r['atom'],tuple(r['input_slot']),r['first_L_owner']['context_tick0'],r['S_input_x_minus_head_x'],tuple(r['N_loss_EXIT_minus_tag']))for r in J['all8_plain_true_input_loss_supports']}
assert len(captures)==20 and set(captures)=={(r['atom'],tuple(r['actual_EXIT_CORE_cell']),r['in_ENTRY_CORE'],tuple(r['actual_RAW_last_read'])if r['actual_RAW_last_read']else None,tuple(r['actual_first_requirement'])if r['actual_first_requirement']else None)for r in J['all20_plain_RAW_EXIT_CORE_capture_checks']}
assert(tr(W['C'],0j,2)['p'],tr(W['C'],0j,2)['h'])==(-1j,1)and(tr(W['C'],0j,1)['p'],tr(W['C'],0j,1)['h'])==(1+0j,0)
for r in J['all3_ordinary_zero_C_drifts']:
 a=r['atom'];zs=[tr(W[a],0j,h)for h in (2,1,0)];assert zs[0]['p'].real<=0 and zs[0]['p'].imag<0 and zs[1]['p'].imag<=0 and zs[2]['p'].real>=0 and zs[2]['p'].imag>0
 for k,z in zip(('S_increment','E_increment','N_increment'),zs):assert r[k]==xy(z['p'])+[z['h']]
assert first(ctx['F'],b-target)==('R',14)and first(ctx['F'],s-target)==('R',44)
letters='UFCDDVCDU';word=''.join(W[a]for a in letters);z=tr(word+M);assert not z['bad'] and len(word)==190 and (tr(word)['p'],tr(word)['h'])==(target,0);seed={q for q,b in z['req'].items()if b};assert len(seed)==32 and 3+5j not in z['req'];new=seed|{3+5j};ready=tr(word+W['F'][:14]);assert {q for q,b in ready['req'].items()if b}==new and not ready['bad']
controls=[]
for rr,seed0,failtick in zip(J['all2_complete_pre_entry_fields'],[seed,new],[12,14]):
 assert sorted(map(xy,seed0))==rr['complete_seed'];B={q:['initial',xy(q)]for q in seed0};p=0j;h=0;t=0;hist={q:[]for q in [0j,1j,1+0j,1+1j,2+0j,2+1j,b,s]};cuts=[]
 for ix,a in enumerate(letters):
  for tick,c in enumerate(W[a]):
   assert(p in B)==(c=='L')
   if p in hist:hist[p].append((t,ix,a,tick,c,B.get(p)))
   if c=='R':B[p]=t
   else:del B[p]
   h=(h+(1 if c=='R'else-1))%4;p+=rot(h)*1j;t+=1
  if ix>=1:
   ko={p+rot(h)*q for q in K};assert B.get(b)==36 and B.get(s)==26 and b not in ko and s not in ko
   for q in [0j,1j,1+0j,1+1j]:assert B.get(q)==u['last'][q][1]and q not in ko
   cut=rr['all_b_s_CURRENT_marked_cut_states'][len(cuts)];assert cut['RAW_cut_tick0']==t and cut['head']==xy(p)+[h]
   for e in cut['original_east_pair_states']:q=complex(*e['cell']);assert e['actual_present_R_identity']==B.get(q)and e['same_original_physically_BLACK']==(B.get(q)==u['last'][q][1])
   cuts.append(t)
 assert (p,h,t)==(target,0,190)
 for tick,c in enumerate(W['F']):
  if (p in B)!=(c=='L'):break
  if c=='R':B[p]=t
  else:del B[p]
  h=(h+(1 if c=='R'else-1))%4;p+=rot(h)*1j;t+=1
 fail=rr['first_unmatched_second_F_request'];assert tick==failtick==fail['candidate_F_own_tick0']and fail['cell']==xy(p)and fail['global_tick0']==t and fail['required_turn']==c and fail['SAME_R_identity_before']==B.get(p)
 for r in rr['selected_source_and_cycle_physical_reads']:
  q=complex(*r['cell']);got=[(v['global_tick0'],v['atom_index0'],v['atom'],v['own_tick0'],v['turn'],v['SAME_R_birth_before'])for v in r['reads']];assert hist[q]==got
 assert [(v[0],v[4])for v in hist[2+0j]]==[(8,'R'),(176,'L')]and[(v[0],v[4])for v in hist[2+1j]]==[(7,'R'),(175,'L'),(183,'R')]
 controls.append({'seed':len(seed0),'prefix_reads':190,'first_mismatch_F_tick':tick,'cell':xy(p),'same_birth':B.get(p)})
ps=pieces(letters);assert len(ps)==len(J['finite_reached_prefix_proxy'])
for (a,b),r in zip(ps,J['finite_reached_prefix_proxy']):assert xy(a)==r['start']and xy(b)==r['end']
for i in range(len(ps)):
 for j in range(i+1,len(ps)):
  hit=meet(*ps[i],*ps[j]);assert hit==(1,0)if j==i+1 else hit is None
O={'status':'PASS arbitrary-length exactly-two-C secondF(3,3,N) common-output gate and two distinct reached fields','manifest':sha(MF),'script':sha(S),'true_input_roles':8,'core_roles':20,'controls':controls,'analytic_review':['Actual U then F/Q/B gives genuine new foreign R8 at(2,4), outside exitCORE; original U R26 at(1,3) is separately missed by every foreign context. No assumed preforeign-output survival is used for the primary guard.','Every first CURRENT loss is a literal external input, including marker-owned exitCORE absorption. All20 exitCORE cells and all8 input roles are rebuilt, not merely physical Ls in the RAW. C has no external inputs. S heads x<=-3 and S input offset<=1 exclude loss; E heads y<=1 and input offset<=1 exclude loss. N2 loss RAW exits y>=4, then no C remains and every later N base raises y, so targety3 cannot be reached. This permits arbitrary cancellation of earlier S and later N lengths.','The secondary originalU bud has equality N exits(2,3,N), never target(3,3,N); any interveningN raisesy. Its own targetR44 is a necessary hypothetical later request, not a read asserted after the primaryR14 failure.','Literal190-read UFCDDVCDU has a complete32-cell field plus actualM. The distinct33-cell field adds exactly unread(3,5), preserving all earlier reads. The fixed32 board fails candidateL12; the33 board first failsR14 on SAME firstF R8. Every marked cut retains the four oldU starIDs and both guards. The original east pair really dies175/176, and the R183 black at(2,1) is a new identity.','Every exact finite proxy segment pair is checked: adjacent endpoint only, otherwise disjoint. This is a named reached-prefix control, not a global simplicity premise or induction. No completed secondF, all-two-C classification, foreign-count budget or physical ant termination claim.']};S.with_suffix('.json').write_text(json.dumps(O,indent=2)+'\n');print(O['status']);print(sha(S.with_suffix('.json')))
