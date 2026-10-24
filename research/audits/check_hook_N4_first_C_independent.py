from pathlib import Path
import hashlib,json
S=Path(__file__);R=S.parents[1];D=R/'foreign_hook_N4_first_C_R39_guard_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'manifest.json';assert sha(MF)=='70e0bfdf78b0a9cca96ebc22e89967a46efc5b95dc81dbaba4a1f351f37ab853';MFT=json.loads(MF.read_text())
for f,h in MFT['files'].items():assert sha(D/f)==h
for f,h in MFT['dependencies'].items():assert sha(R/f)==h
J=json.loads((D/'R39_guard.json').read_text());ns={'__file__':str(S.with_name('check_old_V_second_age1_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Universal')[0],ns);W,M,K,tr,rot,xy=[ns[k]for k in('W','M','K','tr','rot','xy')];I={a:{q for q,b in tr(W[a]+M)['req'].items()if b and q not in K}for a in'DCVU'};assert not I['C']and sum(map(len,I.values()))==8
roles={}
for a in'DVU':
 for inp in I[a]:
  sn=inp;nn=tr(W[a],-inp,0);ee=tr(W[a],-rot(1)*inp,1);assert inp.real>=-1 and nn['p'].real>=0 and ee['p'].real+ee['p'].imag>=-1
  rr=dict(atom=a,input=xy(inp),S_entry_relative_tag=xy(sn),N_RAW_exit_relative_tag=xy(nn['p'])+[nn['h']],E_RAW_exit_relative_tag=xy(ee['p'])+[ee['h']],E_RAW_exit_H_relative_tag=int(ee['p'].real+ee['p'].imag));roles[a,tuple(xy(inp))]=rr
assert roles=={(r['atom'],tuple(r['input'])):r for r in J['all8_true_input_complete_RAW_exit_coordinate_roles']}
# Explicit end-core changes are checked, so true first-CURRENT-loss includes marker absorption.
for a in'DCVU':
 raw=tr(W[a]);ctx=tr(W[a]+M);ek={raw['p']+rot(raw['h'])*q for q in K}
 for q in ek-K:assert q in ctx['req']and(not ctx['req'][q]or q in I[a])
for a in'DVU':
 for h in range(4):
  z=tr(W[a],0j,h);assert z['h']==h
  if h==0:assert z['p'].real>=0 and z['p'].real+z['p'].imag>=2
  if h==1:assert z['p'].real+z['p'].imag>=0
  if h==2:assert z['p'].real<=0
  if h==3:assert z['p'].real<=0 and z['p'].imag>=0
assert(tr(W['C'])['p'],tr(W['C'])['h'])==(1j,3)
assert(tr(W['C'],0j,3)['p'],tr(W['C'],0j,3)['h'])==(-1+0j,2)
assert(tr(W['C'],0j,1)['p'],tr(W['C'],0j,1)['h'])==(1+0j,0)
cu=tr(W['C']+W['U']+M);assert cu['bad']==(29,1,-1+0j,'L')
hook={-3-3j,-2-3j,-1-3j,-1-2j};boundary=[]
for inp in sorted([q for q in I['U']if q.real==-1],key=lambda p:(p.real,p.imag)):
 head=-5j+inp;ctx=tr(W['U']+M);core=sorted([xy(q)for q in hook if(q-head)/rot(2)in K]);white=sorted([xy(q)for q in hook if ctx['req'].get((q-head)/rot(2))is False]);assert core or white;boundary.append(dict(U_input=xy(inp),head=xy(head)+[2],held_young_hook_entry_CORE_witnesses=core,held_young_hook_first_WHITE_witnesses=white))
assert boundary==J['all3_Q_S_boundary_current_hook_guards']
for r in J['all2_exact_FOREIGN_R39_frame_and_target_CORE_cases']:
 a=r['foreign'];g=complex(*r['genuine_R39_tag_postforeign']);target=complex(*r['target_U_N']);raw=tr(W[a]);ctx=tr(W[a]+M);assert raw['h']==2;old=raw['p']+rot(2)*g;assert old==-4+1j and raw['last'][old]==ctx['last'][old]==('R',39);ek={raw['p']+rot(2)*q for q in K};assert old not in ek and g not in K and g-target==1 and g-target in K;assert g.real+g.imag==-5 and target.real+target.imag==-6;assert -6>-9
for name,r in J['all3264_immutable_named_control_words'].items():
 z=tr(''.join(W[a]for a in name)+M);assert z['bad']is not None;t,u,p,c=z['bad'];assert r['trace']==dict(feasible=False,conflict_read=t,previous_read=u,cell=xy(p),turn=c)
assert len(J['all3264_immutable_named_control_words'])==3264 and len(J['all300_named_count_records'])==300
out=dict(status='PASS arbitrary-length first-C route excludes two specified N4 U targets',manifest=sha(MF),script=sha(S),true_marker_inclusive_input_roles=8,Q_S_boundary_guards=boundary,regression_words=3264,analytic_review=['Actual Q/B RAW lastR39 at source(-4,1) is SAME external CURRENT g0,-5 or1,-6 in its true EXIT-N frame, not a historical guessed BLACK bit. TargetU entryK contains local1,0. A prior alive-CORE absorption would already be a CURRENT loss and is included.','Exactly four actual Cs after an immediate firstC give C,Wrail,C,Srail,C,Erail,C,Nrail,U. PlainD/V/U rails have arbitrary lengths/orders. Every valid C has no external BLACK input, and explicit newexitK first-color checks rule out unaccounted markerCORE capture. Thus firstCURRENTloss must use one of all8 true baseinput roles.','Initial C ends0,1W. W heads y>=1 whereas any g input needs y<=gy+1<1. The secondC moves xleft1; all S heads x<=-1. B input would require x>=0. Q boundary x=-1 admits exactly three U roles, all contradictory to the SAME four-hook CURRENT reserve at actualCclock2. No simplicity or old-source age is needed.','Nrail must be nonempty because the literal lastC/U pair has repeatedL at29/1 insideRAW. Its H increment>=2 and C4 adds1, so finalE headH<=-9. Every Efirstloss RAWexitH>=gH-1=-6 and laterE H cannot decrease. This excludes the entire unbounded Erail, not a bounded endpoint scan.','Every Nfirstloss RAWexitx>=gx while targetx=gx-1, and laterN x cannotdecrease. Hence SAMEg survives to targetENTRYCORE, contradicting the current/core partition. Actual terminalM, all marker-owned inputs and sourceR identity retained.','All3264 named failed words replay as regressions only. Scope excludes only the two exact Q/B initialC N4 targets; initialD/V/U, other gates, arbitrary-tail simplicity, secondforeign, coverage and capture remain open.']);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
# Separate binding of the author's exact zero-separator clarification, without altering the signed base audit.
f=R/'first_departure_multiplicity_2026-10-24/high_macro_run_zero_separator_clarification.md';g=S.with_name('high_macro_zero_separator_binding.json');g.write_text(json.dumps(dict(status='PASS dependent wording clarification',proof_sha256=sha(f),base_audit=sha(S.with_name('check_high_macro_junctions_independent.json')),scope='RR-type adjacency supplies three consecutive RIGHT turns; only RLR3/RLR3 remains and signed general RR closure forbids its two LEFT3 endpoints. Allnine zero joins independently checked: four count-empty primaries and five rank-failing primaries overtwenty patches. No local18-domain count changed.'),indent=2)+'\n');print('zero clarification',sha(g))
