from pathlib import Path
import hashlib,json
S=Path(__file__);R=S.parents[1];D=R/'postforeign_V_twoC_cleanup_cone_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'manifest.json';assert sha(MF)=='7ace2b4160a5835b340efa2f735ebf62c97aa2e2efb0a56df596a26bb6b4dbe6'
for f,h in json.loads(MF.read_text())['files'].items():assert sha(D/f)==h
J=json.loads((D/'cleanup_cone.json').read_text())
for f,h in J['dependencies'].items():assert sha(R/f)==h
ns={'__file__':str(S.with_name('check_old_V_second_age1_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Universal')[0],ns)
W,M,tr,rot,K,xy=[ns[k]for k in('W','M','tr','rot','K','xy')];raw=lambda ts:''.join(W[a]for a in ts)
seen=set()
for r in J['all56_zero_C_RAW_read_support_records']:
 a,t=r['atom'],r['tick0'];seen.add((a,t));z=tr(W[a]);p,h,c=z['reads'][t];assert(r['cell'],r['turn'])==(xy(p),c)
 bounds=(int(3+p.imag),int(4+p.real),int(4+z['p'].imag-p.imag));assert bounds==(r['N_head_y_at_least3_cell_y_at_least'],r['W_head_y_at_least4_cell_y_at_least'],r['S_actual_EXIT_y_at_least4_cell_y_at_least'])and all(x>=y for x,y in zip(bounds,(2,3,4)));assert z['h']==0 and z['p'].imag in(1,3,4)and z['p'].real in(0,1)
assert seen=={(a,t)for a in'DVU'for t in range(len(W[a]))}
c=tr(W['C']);assert(c['p'],c['h'])==(1j,3)
for r in J['all15_C_RAW_read_support_records']:
 p,h,ch=c['reads'][r['tick0']];assert(r['cell'],r['turn'])==(xy(p),ch);assert 3+p.imag==r['first_C_N_head_y_at_least3_cell_y_at_least']>=2 and 4+p.real==r['second_C_W_head_y_at_least4_cell_y_at_least']>=3
helper=tr(W['V'],4j,2);assert(helper['p'],helper['h'])==(-1+1j,2);source=tr(W['V']);assert(source['p'],source['h'])==(1+3j,0)
for t,r in enumerate(J['all18_final_helper_RAW_read_records']):assert xy(helper['reads'][t][0])==r['actual_helper_cell']and helper['reads'][t][0].imag>=1
assert 1j not in [q for q,h,c in helper['reads']];assert 1j in{helper['p']+rot(2)*q for q in K}and source['last'][1j]==('R',11);assert tr(W['V']+M,4j,2)['reads'][19][0]==1j
ob=[]
for r in J['all21_terminal_guard_obligations']:
 a,b=r['foreign'],r['next_seven_atom'];g=complex(*r['actual_first_V_chart_guard']);assert g.imag<=0;black=r['actual_guard_BLACK'];origin=r['actual_guard_origin'];tick=r['actual_guard_origin_tick0']
 if origin=='first_V_entry_CORE_hole':assert source['last'][g]==('L',tick)and not black
 elif origin=='SAME_foreign_R_shadow':
  z=tr(W[a]);phys=z['p']+rot(z['h'])*g;assert z['last'][phys]==('R',tick)and g not in source['req']and black
 else:
  assert origin=='actual_mandatory_preFOREIGN_U_entry_CORE_hole'and a=='B'and b=='V'and not black;z=tr(raw('UB'));phys=z['p']+rot(z['h'])*g;assert phys==-1 and z['last'][phys]==('L',1)and g not in source['req']
 z=tr(W[b]+M,helper['p'],helper['h']);indices=[t for t,(q,h,c)in enumerate(z['reads'])if q==g];t=indices[0];ch=z['reads'][t][2];req=r['actual_first_required_read'];assert(t,ch)==(req['context_tick0'],req['turn'])and black!=(ch=='L')
 assert rot(-2)*(g-helper['p'])==complex(*r['next_atom_local_guard']);can=req['canonical'];assert can['context_tick0']==t and can['turn']==ch
 if t>=len(W[b]):assert can['next_word_tick0']==t-len(W[b])and can['next_word_read_number1']==t-len(W[b])+1
 ob.append([a,b,xy(g),black,t,ch,'RAW'if t<len(W[b])else'M11'])
assert len(ob)==21 and{tuple(r[:2])for r in ob}=={(a,b)for a in'FQB'for b in'DCVUFQB'};assert[g for g in('D','DC','V','VC','VCC','U','UC','UCC')if tr(raw(g+'B')+M)['bad']is None]==['U']
out=dict(status='PASS all-length exactly-two-C cleanup endpoint inherits 21 marked-terminal physical guards',manifest=sha(MF),script=sha(S),zeroC_offsets=len(seen),C_offsets=15,helper_offsets=18,all21_guard_demands=ob,analytic_review=['ExactlytwoC gives a unique N/W/S chronological decomposition. FirstV actualRAW exit1,3N and nonnegative Nincrements bound Nheady>=3; firstC raisesy1, W D/V raise y andU keepsy, so Wheady>=4. SecondC atW changesx only. Every completed Sbase before helper0,4S exitsy>=4 because remaining S motion only decreasesy. Exact RAW offsets relativetoEXIT therefore bound every Sread>=4. No finite count or run-order bound is used.','Connector RAW minimumy>=2 and helper minimumy>=1 preserve every designated y<=0 hole/shadow, including any potential CORE repair: physical repair necessarily entails a read. Original A0,1 is separately missed byhelperRAW and is aliveEXITCORE, not residualCURRENT or dead.','All21 first guard demands reconstructed independently with actual RAW/M11 owners. The unique preparedB/V escape uses genuine mandatorypreFOREIGN U L1 hole instead; all8 fullG8 adjacency types leaveonlyplainU. Some nextRAWs complete and only their actual markerfails, retained. Internal markerreads already belongto successive actualRAWs; no extra unexecuted tail is inserted.','Conditional endpoint family only: immediate postfirstFOREIGN V, exactlytwo ordinaryCs, specified helperV0,4S. It is not a classification of all A losses, arbitrary erosion, arbitrary cleanup endpoints, moreCs, anotherforeign or globalproxy simplicity.']);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
