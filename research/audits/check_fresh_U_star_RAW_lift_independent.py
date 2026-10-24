from pathlib import Path
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'ordinary_RAW_G8_base_cut_bridge_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'U_star_RAW_lift_manifest.json';assert sha(MF)=='c3b0a0b8a1ddb652047eec49ea804ed7e412d454c6c9192b1532c0b6bcd9de4e'
m=json.loads(MF.read_text())
for k,b in [('files',D),('dependencies',R)]:
 for f,h in m[k].items():assert sha(b/f)==h
ns={'__file__':str(S.with_name('check_old_V_second_age1_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Universal')[0],ns);W,M,K,tr,xy,rot=[ns[k]for k in('W','M','K','tr','xy','rot')]
J=json.loads((D/'fresh_U_star_RAW_lift.json').read_text());STAR={0j,1j,1+0j,1+1j};u=tr(W['U']);births={q:u['last'][q][1]for q in STAR};assert births=={0j:4,1j:19,1+0j:9,1+1j:18};assert all(u['last'][q][0]=='R'and q not in{u['p']+rot(u['h'])*z for z in K}for q in STAR)
assert J['source_births']==[dict(cell=xy(q),last_R_tick0=t)for q,t in sorted(births.items(),key=lambda z:(z[0].real,z[0].imag))]
# Full C context proves both no old external physical consumption and no silent CORE capture.
c=tr(W['C']);ctx=tr(W['C']+M);assert {q for q,v in ctx['req'].items()if v}==K;exitK={c['p']+rot(c['h'])*q for q in K};assert len(exitK)==5
for q in exitK:
 if q not in K:assert c['last'][q][0]=='R'and ctx['req'][q]is False
 r=next(z for z in J['all5_C_EXIT_CORE_capture_checks']if z['C_EXIT_CORE_cell']==xy(q));first=next(((ch,t)for t,(qq,hd,ch)in enumerate(ctx['reads'])if qq==q),None);assert r['in_ENTRY_CORE']==(q in K)and r['actual_RAW_last_read']==(list(c['last'][q])if q in c['last']else None)and r['actual_first_requirement']==(list(first)if first else None)
# Read precise retained theorem and bind all immutable theorem source files.
P=R/'core_periodicity_new/U_left_star_permanence_frozen_20261023_1918';mf=json.loads((P/'manifest.json').read_text())
for f in mf['files']:assert sha(P/f['path'])==f['sha256']
text=(P/'left_star_permanence.md').read_text();assert 'Take any actual finite or infinite context-complete recurrent-eight factor.'in text and 'These four exact identities remain CURRENT until the end of that same complete-eight factor.'in text
# Actual U internal own tails keep the same four birth IDs.
for s in['U','UC','UCC']:
 z=tr(''.join(W[a]for a in s)+M);assert not z['bad']
 for q,t in births.items():assert z['last'][q]==('R',t)
controls=[]
for rr in J['all4_complete_finite_regressions']:
 word=rr['word'];idx=rr['selected_new_U_index0'];raw=''.join(W[a]for a in word)+M;z=tr(raw);assert not z['bad'];seed={q for q,v in z['req'].items()if v};assert sorted(map(xy,seed))==rr['complete_seed'];B={q:('initial',xy(q))for q in seed};p=0j;h=0;t=0;ids={};cuts=[]
 for i,a in enumerate(word):
  if i==idx:
   assert a=='U'and xy(p)+[h]==rr['source_entry']and t==rr['source_start_tick0'];ids={p+rot(h)*q:t+b for q,b in births.items()}
  for ch in W[a]:
   assert(p in B)==(ch=='L')
   if ch=='L':del B[p]
   else:B[p]=t
   h=(h+(1 if ch=='R'else-1))%4;p+=rot(h)*1j;t+=1
  if i>=idx:
   core={p+rot(h)*q for q in K};assert all(B.get(q)==b and q not in core for q,b in ids.items());cuts.append(dict(after_atom_index0=i,atom=a,RAW_cut_tick0=t,head=xy(p)+[h],all4_SAME_CURRENT=True))
 assert cuts==rr['all_actual_selected_RAW_cuts']and rr['SAME_star_births']==[dict(cell=xy(q),birth_tick0=b)for q,b in sorted(ids.items(),key=lambda z:(z[0].real,z[0].imag))]
 for ch in M:
  assert(p in B)==(ch=='L')
  if ch=='L':del B[p]
  else:B[p]=t
  h=(h+(1 if ch=='R'else-1))%4;p+=rot(h)*1j;t+=1
 assert t==rr['all_physical_reads'];controls.append(dict(word=word,source_index=idx,seed=len(seed),reads=t,protected_cuts=cuts,full_final_black=sorted(map(xy,B))))
assert {r['word']for r in controls}=={'UDCC','UQUDCC','UBUDCC','UQUCCV'}
out=dict(status='PASS all four SAME fresh-U star IDs through arbitrary ordinary RAW suffix, no simple-prefix premise',manifest=sha(MF),script=sha(S),C_CORE_roles=5,controls=controls,analytic_review=[
'For each desired actual cut, the local maximal-C-run proof gives exactG8 or one terminalDCC. EveryD has an actual priorRAW inside the selectedU factor; no prepared firstD exception. Every intermediate prefix has actualM from the ensuing RAW, including D10 spill and the stipulated terminalM. No unexecuted full consumer tail is assumed.',
'The frozen1918 theorem explicitly concerns ANY actual context-complete recurrent-eight factor and genuinely born U-family star. It assumes neither pre-factor ancestry nor globally simple external history nor WHITE entry. Exact parsed factor ending at this cut can treat the selectedU/UC/UCC as its real initial packet. Source ownC tails retain identical birth IDs.',
'If terminalDCC occurs, remove only finalC: preceding factor is actualU-entry...DC, with endingM supplied by the real removedC.1918 gives all four SAMECURRENT before it. C completecontext has all firstBLACK cells exactlyentryK and no external input; every new exitCORE cell is actualRAW lastR with firstWHITE. Thus an external currentBLACK cell can neither be read nor silently absorbed, and all four remain current at the finalcut.',
'Whole finite fields, original birth timestamps and every selectedRAWcut independently replayed for four positive controls, including earlierQ/B and actualterminalDCC. The no-simple-prefix conclusion is a grammar+oldtheorem lift, not a silent strengthening of the independent conditionalLEFT Jordan proof.',
'No foreign AFTER selectedU, no carrying an original preforeign star across foreign, no arbitrary ant coverage, no disjointness from earlier sources, no complete ordinary-tail simplicity, no physicalWHITE permanence, no whole-output seal or capture.'
]);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
