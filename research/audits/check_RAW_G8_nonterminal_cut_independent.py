from pathlib import Path
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'ordinary_RAW_G8_base_cut_bridge_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'nonterminal_cut_manifest.json';assert sha(MF)=='7ae212b4014f856b99c165a5020833d0c9f5725ec95817d6f22c8a96203baf52'
m=json.loads(MF.read_text())
for k,b in [('files',D),('dependencies',R)]:
 for f,h in m[k].items():assert sha(b/f)==h
ns={'__file__':str(S.with_name('check_old_V_second_age1_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Universal')[0],ns);W,M,K,tr,xy=[ns[k]for k in('W','M','K','tr','xy')]
J=json.loads((D/'nonterminal_cut_extension.json').read_text());spell=lambda s:''.join(W[a]for a in s);rows=[]
for a in'FQB':
 s='DCC'+a;z=tr(spell(s)+M);assert z['bad']==(52,12,0j,'L');assert len(spell('DCC'))==40 and W['C'][2]=='L'and W[a][12]=='L';seen=[(t,c)for t,(q,h,c)in enumerate(z['reads'])if q==0j and 12<=t<=52];assert seen==[(12,'L'),(52,'L')]
 ref=next(r for r in J['all3_additional_DCC_foreign_conflicts']if r['word']==s);assert ref['previous_owner']['packet']=='C'and ref['previous_owner']['context_tick0']==2 and ref['conflicting_foreign_owner']['packet']==a and ref['conflicting_foreign_owner']['context_tick0']==12
 rows.append({'word':s,'previous_tick':12,'conflict_tick':52,'cell':[0,0],'previous_owner':'first C own tick2/read3','new_owner':a+' own tick12/read13'})
# Regenerate every immediate next atom, not a depth cut.
for a in'DVU':assert tr(spell('DCC'+a)+M)['bad']is not None
for a in'DCVUFQB':assert tr(spell(a+'DCCC')+M)['bad']is not None
# A real next RAW+M supplies the marker, including D10 spilling by one.
for a in'DCVUFQB':assert (W[a]+M)[:11]==M
for s in['UDCC','UQUDCC']:assert tr(spell(s)+M)['bad']is None
# Statement and signed actual-field theorem retain the exact entry scope.
f=R/'core_periodicity_new/U_entry_simplicity_frozen_20261023_1616/00_U_entry_center_simplicity.md';t=f.read_text();assert 'Let an actual finite factor of the complete recurrent-eight language begin\nwith U, UC, or UCC.'in t
out=dict(status='PASS actual nonterminal ordinary RAW ending-C cut parses G8, with genuine next complete7 premise',manifest=sha(MF),script=sha(S),new_conflicts=rows,all7_next_atoms_reconstructed=True,analytic_review=[
'The signed arbitrary-length maximal-C-run proof leaves terminalDCC only. Its actual next word is one of seven; D/V/U conflict, C invokes actual incoming-budDCCC, F/Q/B give the newly reconstructed repeated ownL12. No word-depth bound is imposed.',
'If the selected first base isD, the actual preceding seven-atomRAW remains required. LaterD automatically has a real predecessor. For V/U, C-run<=2 already follows from actual followingM.',
'The terminal packet marker is physically supplied by the stipulated immediate next completeRAW plus its actualM11. D10 provides10 then that next actualfirstL; the selected G8 factor need not include the following foreign. The premise is strictly stronger than merely11 continuation reads.',
'The signed U-entry theorem has arbitrary actual entry field and no pre-factor ancestry premise. A fresh postforeignU starts the selected factor; actualG8 simplicity follows without assuming a simple prefix. It excludes only contacts internal to that selected factor, never with earlier sources.',
'Actual UDCC/UQUDCC+M remain positive terminal exceptions and have no complete next7 word. No arbitrary-ant coverage, unconditional terminal parse, pre-U-source exclusion, secondforeign extension or capture follows.'
]);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
