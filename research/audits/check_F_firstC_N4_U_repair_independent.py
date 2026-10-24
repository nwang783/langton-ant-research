from pathlib import Path
import hashlib,json
S=Path(__file__);R=S.parents[1];D=R/'F_firstC_N4_U_upper_repair_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'manifest.json';assert sha(MF)=='bebca8b7b68e3bd093f44b1997b494ed4ccf82ff1a82571bd518449139b9ae43';m=json.loads(MF.read_text())
for f,h in m['files'].items():assert sha(D/f)==h
for f,h in m['dependencies'].items():assert sha(R/f)==h
ns={'__file__':str(S.with_name('check_old_V_second_age1_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Universal')[0],ns);W,M,K,tr,rot,xy=[ns[k]for k in('W','M','K','tr','rot','xy')]
J=json.loads((D/'C_N4_U_repair.json').read_text());g=-1+2j;target=-1-1j
assert g-target==3j and 3j not in K
assert next((c,i)for i,(p,h,c)in enumerate(tr(W['U']+M)['reads'])if p==3j)==('L',23)
JO={tuple(r[:3]):r[3]for r in json.loads((R/'core_periodicity_new/chronology_dcuv/counted_input_age_rules_complete.json').read_text())};assert JO[7,0,3]==4
z=tr(W['F']+3*W['C']+M);assert z['bad']==(99,47,-2-1j,'R');assert 99-len(W['F'])-2*len(W['C'])==13
assert not tr(W['F']+2*W['C']+M)['bad']
rows=[]
for n in(1,2):
 pre=tr(W['C']*n);p,h=pre['p'],pre['h'];assert(p,h)==((1j,3)if n==1 else(-1+1j,2))
 assert tr(W['F']+n*W['C'])['last'][-2-1j]==('R',47)
 for a in'DVU':
  q=(g-p)/rot(h);t=tr(W[a]+M);first=next((c,i)for i,(v,hh,c)in enumerate(t['reads'])if v==q)
  assert(q,first,q in K)==((1+1j,('R',6),False)if n==1 else(-1j,('L',3),True))
  author=next(r for r in J['all6_real_first_BASE_guard_branches']if r['initial_leading_C_count']==n and r['first_actual_BASE']==a)
  assert author['local']==xy(q)and author['actual_first']==list(first)and author['first_BASE_pose']==[*xy(p),h]
  assert 4-n<JO[7,0,3]
  rows.append(dict(leading_C=n,BASE=a,pose=[*xy(p),h],g_local=xy(q),first=list(first),entryCORE=q in K,producer_max_age=4-n))
old=json.loads((R/'original_F_piece_firstpost_DC_2026-10-24/partial_scope_qualification.json').read_text())['all3_OPEN_N4_restoration_residues'];keys={(r['original_row']['first_post_RAW'],r['original_row']['actor'],*r['original_row']['pose'])for r in old};closed=('C','U',-1,-1,0);assert closed in keys;remaining=keys-{closed};assert remaining=={('D','V',-1,-1,0),('D','U',-1,-1,0)}
O={'status':'PASS ONLY separate first-C N4 U repair; original full84 still NOT PASSED','manifest':sha(MF),'script':sha(S),'actual_upper_minimum':4,'FCCC_RAW_conflict':[47,99,[-2,-1]],'six_first_BASE_cases':rows,'remaining_OPEN_original_labels':sorted(remaining),'analytic_review':['The third leading C fails inside its own RAW, not merely its supplied marker. An actual first BASE must therefore occur at clock1 or2 strictly before the proposed clock4 U. This is arbitrary-length exhaustion of the initial C run, not a depth cap.','At clock1 the target upper cell is WHITE at factor entry by every BASE own firstR6 outsideCORE. At clock2 its real initialCORE identity is physically L3-deleted. These facts remove only the old-entry exemption, not arbitrary R repairs or aliveCORE possibilities.','The actual factor from that first BASE through targetU ends at a BASE with real finalM11, so the signed grammar applies. A firstD has its real previousC, preventing the unmarked initialDCCC exception. No hypothetical terminalC factor is parsed.','The full residual/current partition in the actual G8 factor makes an external true input at targetU either an unconsumed entry residual or a genuine full-output identity. The former is eliminated by the explicit firstBASE cases; all actual CORE writes and exports remain in the latter bookkeeping. No original F lifetime is assumed CURRENT at the target.','Every possible fresh full producer enters at clock at least1 or2. Its actual produced-input age at clock4 is at most3, contradicting the signed U upper-slot minimumFOUR. No age law is transported across F, which is outside the selected actual factor.','Only the sourceC/U label is closed. The two sourceD/V,U restoration labels remain OPEN. The rejected original143d full84/pair-current statement is not restored.']}
S.with_suffix('.json').write_text(json.dumps(O,indent=2)+'\n');print(O['status']);print(sha(S.with_suffix('.json')))
