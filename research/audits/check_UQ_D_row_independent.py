from pathlib import Path
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'UQ_initial_D_row_C5_hook_transfer_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'manifest.json';assert sha(MF).startswith('7c8cbeac');mf=json.loads(MF.read_text())
for f,h in mf['files'].items():assert sha(D/f)==h
for f,h in mf['dependencies'].items():assert sha(R/f)==h
ref=json.loads((D/'UQ_D_row.json').read_text());assert ref['dependencies']==mf['dependencies']
ns={'__file__':str(S.with_name('check_old_V_second_age1_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Universal')[0],ns);W,M,K,tr,rot,xy,meet=[ns[k]for k in['W','M','K','tr','rot','xy','meet']];V=(1j,1,-1j,-1);G={a:tr(W[a])for a in W};CTX={a:tr(W[a]+M)for a in W}
def pose(p,h):return[*xy(p),h]
def first(a,q):
 t=next(j for j,e in enumerate(CTX[a]['reads'])if e[0]==q);return[CTX[a]['reads'][t][2],t]
row=[]
for i in range(6):
 q=tr(W['Q']+W['D']*i);p,h=q['p'],q['h'];assert(p,h)==(-4-i+(-4-i)*1j,2)
 g=p+rot(h)*2;assert g==-6-i+(-4-i)*1j
 assert G['D']['reads'][8][0]==2 and G['D']['reads'][8][2]=='R' and G['D']['last'][2]==('R',8)
 rr=ref['all6_real_initial_D_common_births'][i];assert rr['actual_D_ENTRY']==pose(p,h)and rr['SAME_common_cell']==xy(g)
 row.append((p,h,g))
ports=[]
for a in'DVU':
 for q,b in CTX[a]['req'].items():
  if not b or q in K:continue
  p=2-q;e=p+G[a]['p'];active=(int(p.real+p.imag)%2==0)
  rr=next(z for z in ref['all8_parity_refined_N4_first_CURRENT_loss_ports']if z['consumer']==a and z['input']==xy(q));assert rr['ENTRY']==pose(p,0)and rr['RAW_EXIT']==pose(e,G[a]['h'])and rr['active_sector']==active
  assert rr['actual_first_L']['context_tick0']==first(a,q)[1]
  if active:assert e.imag>=2
  ports.append([a,xy(q),pose(p,0),pose(e,G[a]['h']),active])
assert len(ports)==8 and [(a,p)for a,q,p,e,b in ports if b]==[('U',[2,-2,0]),('U',[3,-1,0])]
for a in W:
 p=0j;h=0
 for c in W[a]:
  h=(h+(1 if c=='R'else-1))%4;p+=V[h];assert(int(p.real+p.imag)+h)%2==0
# No C external BLACK input, so a silent C capture does not evade the loss roles.
ek={G['C']['p']+rot(G['C']['h'])*q for q in K};assert not[q for q,b in CTX['C']['req'].items()if b and q not in K];assert len(ek-K)==3 and all(G['C']['req'][q]is False for q in ek-K)
T=-4-7j;lp=T-rot(1)*G['V']['p'];cp=lp-rot(2)*G['C']['p'];sp,sh,g=row[1]
assert(lp,cp)==(-7-6j,-7-5j)and(cp-sp)/rot(sh)==2 and (g-cp)/rot(2)in K
assert ref['sole_E5_V_case']['actual_C5_ENTRY']==pose(cp,2)
assert tr(W['C']+W['U']+M)['bad']is not None
interfaces=[]
for last in'VU':
 lp=T-rot(1)*G[last]['p']
 for pen in'DVU':
  pp=lp-rot(1)*G[pen]['p'];slot=1 if pen=='D'else 2+1j;g=pp+rot(1)*slot
  matches=[i for i,(sp,sh,gg)in enumerate(row)if gg==g];assert len(matches)==1;i=matches[0];sp,sh,_=row[i];rel=(pp-sp)/rot(sh)
  assert rel==(2-1j if pen=='D'else 3-2j)and(1-sh)%4==3
  assert first(pen,slot)==(['L',5]if pen=='D'else['R',7])
  if pen=='D':assert slot in K
  rr=next(z for z in ref['all6_penultimate_last_E5_BASE_interfaces']if z['penultimate_BASE']==pen and z['last_BASE']==last)
  assert rr['penultimate_ENTRY']==pose(pp,1)and rr['last_ENTRY']==pose(lp,1)and rr['held_initial_D_index']==i and rr['SAME_old_common_cell']==xy(g)and rr['reader_in_D_frame']==pose(rel,3)
  interfaces.append([pen,last,pose(pp,1),pose(lp,1),i,xy(g),pose(rel,3)])
assert {z[4]for z in interfaces}=={2,3,4,5}
hooks=[]
for a in'QB':
 assert W[a][:11]==M
 ep,eh=G[a]['p'],G[a]['h'];r=next(z for z in ref['special_UQ_UB_all_length_ordinary_same_hook_lift']if z['selected_prefix']=='U'+a)
 for z in r['all4_actual_same_R_births']:
  q=complex(*z['original_A_cell']);assert q in{-1-1j,-2-1j,-3-1j,-3-2j};assert G[a]['last'][q]==('R',z['last_R_tick0'])and(q-ep)/rot(eh)not in K
  hooks.append([a,xy(q),z['last_R_tick0']])
assert meet(-7-3j,-7-7j,-9-5j,-1-5j) is not None
caps=[]
for a in'FQB':
 assert W[a][:11]==M
 ep,eh=G[a]['p'],G[a]['h'];ek={ep+rot(eh)*q for q in K}
 for q in ek:
  assert q not in K
  ff=first(a,q);rr=next(z for z in ref['all15_next_FOREIGN_exitCORE_capture_sites']if z['actor']==a and z['RAW_EXIT_CORE_cell']==xy(q));assert ff==rr['actual_first']
  if q not in G[a]['req']:assert CTX[a]['req'][q]and len(W[a])<=ff[1]<len(W[a])+len(M)
  elif ff[0]=='R':assert G[a]['req'][q]is False
  else:assert G[a]['req'][q]is True
  caps.append([a,xy(q),ff])
assert len(caps)==15
out=dict(status='PASS named all-length U Q initial-D-row C5 hook transfer, m>=6, one next FOREIGN only',manifest=sha(MF),script=sha(S),all8_N4_ports=ports,all6_final_pairs=interfaces,all15_exitCORE_sites=caps,all8_QB_hook_births=hooks,analytic_review=[
'The signed715 first-CURRENT-loss contact implication and signed488 special UQ/UB ordinary-tail simplicity compose at every actual ordinary cut. The next actual RAW supplies the same M11, including the final next FOREIGN first11. This yields only the special selected UQ/UB ordinary-hook persistence, not generic source-FOREIGN permanence or through-next-FOREIGN simplicity.',
'Fresh-D common-through-C3 and W5 negative-y guards are the separately retained source-only sublemma under mandatory45abc. Original143d full84/universal F-pair remains rejected. Each selected initial D has a real preceding Q/D RAW, no later FOREIGN before its reader, and a simple executed subarc supplied by488. Own DC tails are genuine later Cs and are counted from RAW entry, never reset at full exit.',
'New N4 extension is exact relative fine-step parity: x+y+h is even from the real source entry; six of eight true external-input/marker ports are impossible. The two active U losses exit y3/y2. Remaining N bases cannot lower y to the target y<=1. C has I0 and only external first-WHITE captures, so it adds no CURRENT-loss role.',
'At the only possible next-FOREIGN physical hook-loss head T=(-4,-7,E), signed interval grammar makes the E5 rail nonempty and terminal V/U. One base is either forbidden CU or sole V with C5 entry N4(2,0) in the second initial D frame, putting its CURRENT common into entry CORE. With at least two bases, all six penultimate D/V/U and terminal V/U pairs pick initial D indices2..5 and force negative-y W5 CORE/first-WHITE conflicts. Coordinates and case split are independent of m>=6 and all earlier rail lengths.',
'The entire ordinary prefix is actually completed before next FOREIGN, so all selected source-to-reader premises are real, including the last ordinary marker supplied by that FOREIGN. Contradictions occur before the recipient executes; no hypothetical completed next ordinary word is added.',
'Signed1c2 is used only on its original source Q and five-Cs scope. After excluding its sole open head, no old hook is physically first-deleted in actual next RAW+M. Fifteen complete exitCORE sites show an old external CURRENT identity could not be silently captured without a BLACK first read in that same actual context; first-R sites would already conflict. Thus CURRENT at next RAW EXIT and SAME physically BLACK through M are distinct justified conclusions.',
'The retained80-cell570-read control is bound, not rerun or inflated to attain the seven final interfaces. This is one named infinite-prefix family, not arbitrary initial mixed rails, m<6, all-Q C5, renewed whole-field equality, further-FOREIGN iteration, capture or universal language entry.'
],dependencies=mf['dependencies'])
S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(MF));print(sha(S.with_suffix('.json')))
