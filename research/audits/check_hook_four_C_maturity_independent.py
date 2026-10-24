from pathlib import Path
from collections import Counter
import hashlib,json
S=Path(__file__);R=S.parents[1];D=R/'foreign_hook_four_C_maturity_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'manifest.json';assert sha(MF)=='528c463ab89e01317f2accaae17d2978e3d7875f8690b228ef8b9aa5e512566e';mf=json.loads(MF.read_text())
for f,h in mf['files'].items():assert sha(D/f)==h
for f,h in mf['dependencies'].items():assert sha(R/f)==h
ns={'__file__':str(S.with_name('check_old_V_second_age1_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Universal')[0],ns)
W,M,tr,K,rot,xy=[ns[k]for k in('W','M','tr','K','rot','xy')];raw=lambda ts:''.join(W[a]for a in ts);J=json.loads((D/'hook_maturity.json').read_text());I={a:{q for q,b in tr(W[a]+M)['req'].items()if b and q not in K}for a in'DCVU'};assert not I['C']and sum(map(len,I.values()))==8
for a in'DCVU':
 z=tr(W[a]);ctx=tr(W[a]+M);ek={z['p']+rot(z['h'])*q for q in K}
 for q in ek-K:assert q in ctx['req']and(q in I[a]if ctx['req'][q]else q not in I[a])
ports=[]
for a in'DVU':
 for inp in I[a]:
  Sx=tr(W[a],-rot(2)*inp,2);Ex=tr(W[a],-rot(1)*inp,1);assert Sx['p'].real<=0 and Sx['p'].imag<=0 and Ex['p'].imag<=0 and inp.imag>=1 and inp.real>=-1
  r=next(r for r in J['universal8_input_to_RAW_exit_coordinate_bounds']if r['atom']==a and r['input']==xy(inp));assert r['S_RAW_exit_relative_tag']==xy(Sx['p'])+[2]and r['E_RAW_exit_relative_tag']==xy(Ex['p'])+[1];ports.append([a,xy(inp),xy(Sx['p']),xy(Ex['p'])])
assert tr(W['C'])['p']==1j and tr(W['C'])['h']==3
hooks={'Q':{-3-3j,-2-3j,-1-3j,-1-2j},'B':{-2-4j,-1-4j,-4j,-3j}};summaries=[]
for A,hook in hooks.items():
 ar=tr(W[A]);ctxA=tr(W[A]+M);ep=ar['p'];ah=ar['h'];ek={ep+rot(ah)*q for q in K};O={(q-ep)/rot(ah)for q,(ch,t)in ar['last'].items()if ch=='R'and q not in ek};assert hook<=O and not hook&K
 ref=next(r for r in J['source_cases']if r['foreign']==A);rows={(r['atom'],r['heading'],tuple(r['tag']),tuple(r['input'])):r for r in ref['all128_direct_first_loss_input_alignments']};seen=set();counts=Counter();reserve=[]
 for a in'DVU':
  ctx=tr(W[a]+M)
  for h in range(4):
   for tag in hook:
    for inp in I[a]:
     key=(a,h,tuple(xy(tag)),tuple(xy(inp)));seen.add(key);r=rows[key];head=tag-rot(h)*inp;assert r['head']==xy(head)and r['actual_postforeign_C_clock']==(-h)%4
     core={g for g in hook if(g-head)/rot(h)in K};white={g for g in hook if ctx['req'].get((g-head)/rot(h))is False}
     if(int(head.real+head.imag)+h)%2:why='sector'
     elif core:why='held_hook_CURRENT_entry_CORE';assert set(map(tuple,r['witnesses']))=={tuple(xy(g))for g in core}
     elif white:why='held_hook_BLACK_first_WHITE';assert set(map(tuple,r['witnesses']))=={tuple(xy(g))for g in white}
     elif h==0:why='clock0_N_head_y_negative';assert head.imag<0
     elif h==3:why='clock1_W_head_below_y1';assert head.imag<1
     else:
      g=head+(-1-3j if h==2 else 1-1j);assert g in O and g not in K and g.imag<=-1
      if h==2:why='clock2_S_left_lower_FOREIGN_output_endpoint_reserve';assert g.real<head.real;tick=26;loc=1+3j;assert a=='U'
      else:why='clock3_E_lower_FOREIGN_output_endpoint_reserve';assert g.imag<head.imag;tick=6;loc=1+1j
      phys=ep+rot(ah)*g;birth=ar['last'][phys];assert birth[0]=='R'and birth[1]<len(W[A])and ctxA['last'][phys]==birth
      assert (g-head)/rot(h)==loc and ctx['reads'][tick][0]==loc and ctx['reads'][tick][2]=='R'and all(q!=loc for q,hh,ch in ctx['reads'][:tick]);assert xy(g)==r['actual_FOREIGN_same_id_reserve']['postforeign_cell']and xy(phys)==r['actual_FOREIGN_same_id_reserve']['A_cell']and birth[1]==r['actual_FOREIGN_same_id_reserve']['last_R_tick0'];assert r['actual_first_incompatible_R']['context_tick0']==tick and r['actual_first_incompatible_R']['turn']=='R'
      reserve.append([a,h,xy(head),xy(g),birth[1],tick])
     assert r['reason']==why;counts[why]+=1
 assert seen==set(rows)and len(seen)==128 and dict(counts)==ref['counts'];summaries.append(dict(foreign=A,counts=dict(counts),exact_reserve_witnesses=reserve))
for r in J['all286_complete_named_two_C_immutable_control_words']:
 z=tr(raw(r['word'])+M);assert z['bad']is not None;t,u,q,ch=z['bad'];assert(t,u,xy(q),ch)==(r['trace']['conflict_read'],r['trace']['previous_read'],r['trace']['cell'],r['trace']['turn'])
assert len(J['all286_complete_named_two_C_immutable_control_words'])==286
out=dict(status='PASS arbitrary ordinary suffix Q/B hook first CURRENT loss needs base-entry C clock >=4',manifest=sha(MF),script=sha(S),universal8ports=ports,all256=summaries,named_regression_replays=286,analytic_review=['The clock is actual ordinaryC count AFTER foreignRAW EXIT. Source-field R IDs are independently born within actual foreignRAW and survive its real marker; no earlier-source age is reused. All initial hook/guard tags are externalCURRENT.','Trueinput table includes firstL outsideentryK in actualRAW+M, and every newexitK cell is explicitly first-color constrained; external->CORE capture counts as CURRENT loss even if oldphysicalBLACK dies only nextread2. C has no such input. The statement is at marked RAW cuts/ordinary entries, not a claim about every intermediate fine-cut geometric core.','For any initialtaggy<=-1, N heads y>=0 and positiveinputy exclude loss; W heads y>=1 and inputx>=-1 likewise exclude it. A prior S loss has RAWexitx<=gx,y<=gy. Remaining S heads cannot increasex; if targetE, the intervening S-to-E C decreasesy1 and laterE heads cannot increase y. A prior E loss also exitsy<=gy. Thus S targetheadx>gx or E targetheady>gy cannot follow any earlier originalCURRENT loss, regardless of subsequent rebirths or proxycontacts.','All128 first-hook-loss alignments perforeign are independently rebuilt. RemainingN/W heads violatecones; S2 roles require the protected left/lower foreigntagWHITE at U ownR26, and E3 roles require the protected lower tagWHITE at ownR6. These are trueRAW conflicts, not hypothetical postforeign maturity laws.','The286 named controls replay but are not premises for arbitrary run lengths. AllhookIDs remainCURRENT at markedcuts with actualCclock<=3; firstlossatclock>=4 remainsOPEN. No foreign-proxy simplicity, U ancestry, secondforeign, whole-outputpermanence or globalcapture theorem follows.']);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
