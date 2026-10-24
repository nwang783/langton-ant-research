from pathlib import Path
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'foreign_two_C_north_frontier_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'manifest.json';assert sha(MF)=='eece2a65529ef7973d73b477491a952ba94e0128ca2199cbca251e97c50efe62';mf=json.loads(MF.read_text())
for k,b in [('files',D),('dependencies',R)]:
 for f,h in mf[k].items():assert sha(b/f)==h
J=json.loads((D/'foreign_N2_frontier.json').read_text());ns={'__file__':str(S.with_name('check_old_V_second_age1_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Universal')[0],ns);W,M,K,tr,rot,xy=[ns[k]for k in('W','M','K','tr','rot','xy')];raw={a:tr(W[a])for a in W};ctx={a:tr(W[a]+M)for a in W};first=lambda z,q:next((c,t)for t,(p,h,c)in enumerate(z['reads'])if p==q);I={a:{q for q,b in ctx[a]['req'].items()if b and q not in K}for a in 'DCVU'};NE={-1-1j,-1+0j,-1+1j,0j,1j,1+0j,1+1j,1+2j,2+0j,2+1j}
for r in J['all3_actual_source_foreign_NE_birth_interfaces']:
 a=r['actual_foreign'];z=raw[a];oo={q for q,(c,t)in z['last'].items()if c=='R'and(q-z['p'])/rot(z['h'])not in K};assert {q for q in oo if q.real>=-1 and q.imag>=-1}==NE and z['p'].real<=-3 and z['p'].imag<=-2 and z['h']==2 and r['actual_EXIT']==xy(z['p'])+[2]
 assert {tuple(q['cell']):q['actual_own_last_R_tick0']for q in r['all10_SAME_ne_outputs']}=={tuple(xy(q)):z['last'][q][1]for q in NE}
ports=[];capture=[]
for a in 'DCVU':
 z=raw[a];ko={z['p']+rot(z['h'])*q for q in K}
 for q in ko:
  if q not in K and q not in z['last']:assert q in I[a]and first(ctx[a],q)[0]=='L'
  capture.append((a,tuple(xy(q)),q in K,z['last'].get(q),first(ctx[a],q)if q in ctx[a]['req']else None))
 for q in I[a]:
  delta=z['p']-q;assert -q.real<=1 and delta.imag>=0 and(delta.imag>0 or delta.real==1);ports.append((a,tuple(xy(q)),first(ctx[a],q)[1],-int(q.real),tuple(xy(delta)),delta.imag==0))
assert not I['C']and len(ports)==8 and len(capture)==20
assert set(ports)=={(r['atom'],tuple(r['true_input']),r['physical_L_owner']['context_tick0'],r['S_input_x_minus_head_x'],tuple(r['N_RAW_EXIT_minus_original_tag']),r['equality_y_requires_exit_x_tag_plus1'])for r in J['all8_complete_input_to_RAW_EXIT_supports']}
assert set(capture)=={(r['atom'],tuple(r['actual_EXIT_CORE_cell']),r['in_ENTRY_CORE'],tuple(r['actual_RAW_last_read'])if r['actual_RAW_last_read']else None,tuple(r['complete_first_requirement'])if r['complete_first_requirement']else None)for r in J['all20_exitCORE_capture_checks']}
for a in 'DVU':assert tr(W[a],0j,2)['p'].real<=0 and tr(W[a],0j,2)['p'].imag<0 and tr(W[a],0j,1)['p'].imag<=0 and raw[a]['p'].imag>0
assert(tr(W['C'],0j,2)['p'],tr(W['C'],0j,2)['h'])==(-1j,1)and(tr(W['C'],0j,1)['p'],tr(W['C'],0j,1)['h'])==(1+0j,0)
seen=set()
for r in J['all9_portable_two_C_foreign_gate_exclusions']:
 a,b=r['source_foreign'],r['next_foreign'];seen.add((a,b));assert raw[a]['last'][2+0j]==('R',8)and first(ctx[b],-1+1j)==('R',14)and -1+1j not in K and r['target_relative_source_ENTRY']==[3,-1,0]and r['actual_target_first_R']['owner_tick0']==14
assert seen=={(a,b)for a in 'FQB'for b in 'FQB'}
for r in J['finite_predicate_examples_NOT_ant_histories']:
 x,y=r['N2_cut_HEAD'];keep={g for g in NE if g.imag>y or(g.imag==y and x!=g.real+1)};assert sorted(map(xy,keep))==r['guaranteed_SAME_CURRENT']and sorted(map(xy,NE-keep))==r['unresolved_original_ports_NOT_discarded']
O={'status':'PASS source-entry-frame ten-output CURRENT frontier through arbitrary ordinary zero/one/two-C connectors','manifest':sha(MF),'script':sha(S),'source_fields':3,'protected_tags':10,'true_inputs':8,'exit_CORE_roles':20,'next_foreign_gates':9,'analytic_review':['All ten selected tags are genuinely lastR-born outputs of each actual F/Q/B, outside actual exitCORE, with individual clocks rebuilt. This is a FOREIGN ENTRY0N frame: exits are southwest facingS. Their birth ownership is independent of any older input field, U ancestry or foreign count.','First CURRENT loss, including alive-CORE capture, is covered by every actual external input and twenty exitCORE cells. In S0 headx<=-3 and inputx<=headx+1 exclude tagsx>=-1; after real C, E1 heady<=-3 and inputy<=heady+1 exclude tagsy>=-1. C has no external input. No age/simplicity theorem is imported.','For N2 first loss every RAW exit is at or above the original tagrow; equality is exactly(gx+1,gy), including marker-owned D/V/U upper slots. Every subsequent N base strictlyraisesy and no C remains. Thus a later marked cut below the row, or on it at a differentx, cannot follow that loss. The exception is kept unresolved: equality is not silently treated as CURRENT, dead or absent. Replacement cannot evade a first-loss argument.','All nine next F/Q/B letters at source-relative(3,-1,N) demandWHITE at actual ownR14 where SAME sourceR8(2,0) remainsCURRENT. This does not imply persistence through a later foreign, any consumption order, three-C frontier, arbitrary gate classification or capture. The finite predicate examples are merely data-level tests, not ant histories.']};S.with_suffix('.json').write_text(json.dumps(O,indent=2)+'\n');print(O['status']);print(sha(S.with_suffix('.json')))
