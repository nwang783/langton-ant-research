from pathlib import Path
import hashlib,json
from collections import Counter
S=Path(__file__);R=S.parents[1];D=R/'foreign_hook_N4_R39_R54_guard_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'manifest.json';assert sha(MF)=='7eed4e6ac49cd7147df8e58c5759753535d955091eb874ca8b5a8d84fd8fde97';MFT=json.loads(MF.read_text())
for f,h in MFT['files'].items():assert sha(D/f)==h
for f,h in MFT['dependencies'].items():assert sha(R/f)==h
J=json.loads((D/'R39_R54_guard.json').read_text());ns={'__file__':str(S.with_name('check_old_V_second_age1_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Universal')[0],ns);W,M,K,tr,rot,xy=[ns[k]for k in('W','M','K','tr','rot','xy')];I={a:{q for q,b in tr(W[a]+M)['req'].items()if b and q not in K}for a in'DCVU'};assert not I['C']and sum(map(len,I.values()))==8
for row in J['all8_true_input_RAW_exit_coordinate_inequalities']:
 a=row['atom'];q=complex(*row['input']);assert q in I[a];nn=tr(W[a],-q,0);ee=tr(W[a],-rot(1)*q,1);assert xy(nn['p'])+[nn['h']]==row['N_RAW_exit_relative_tag'];assert xy(ee['p'])+[ee['h']]==row['E_RAW_exit_relative_tag'];assert nn['p'].real>=0 and ee['p'].real+ee['p'].imag>=-1 and q.imag>=1 and q.real>=-1
assert len({(r['atom'],tuple(r['input']))for r in J['all8_true_input_RAW_exit_coordinate_inequalities']})==8
for a in'DCVU':
 raw=tr(W[a]);ctx=tr(W[a]+M);ek={raw['p']+rot(raw['h'])*q for q in K}
 for q in ek-K:assert q in ctx['req']and(not ctx['req'][q]or q in I[a])
for a in'DVU':
 for h in range(4):
  z=tr(W[a],0j,h);assert z['h']==h
  if h==0:assert z['p'].real>=0 and z['p'].imag>=0 and z['p'].real+z['p'].imag>=2
  if h==1:assert z['p'].real+z['p'].imag>=0
  if h==3:assert z['p'].imag>=0
for h in range(4):assert tr(W['C'],0j,h)['p']==rot(h)*1j and tr(W['C'],0j,h)['h']==(h-1)%4
assert tr(W['C']+W['U']+M)['bad']==(29,1,-1+0j,'L')
checked=[]
for case in J['source_cases']:
 a=case['foreign'];off=0j if a=='Q'else 1-1j;g=off-5j;r=off+1-3j;hook={off+q for q in[-3-3j,-2-3j,-1-3j,-1-2j]};raw=tr(W[a]);ctx=tr(W[a]+M);ek={raw['p']+rot(raw['h'])*q for q in K}
 for name,tag,old,tick in [('g_R39',g,-4+1j,39),('r_R54',r,-5-1j,54)]:
  assert raw['p']+rot(raw['h'])*tag==old and raw['last'][old]==ctx['last'][old]==('R',tick)and old not in ek and tag not in K
  birth=next(b for b in case['actual_FOREIGN_R39_R54_births']if b['name']==name);assert birth['postforeign_cell']==xy(tag)and birth['actual_A_cell']==xy(old)and birth['actual_last_R_tick0']==tick
  rows={}
  for atom in'DVU':
   for inp in I[atom]:
    head=tag+inp;rec=dict(atom=atom,input=xy(inp),S_head=xy(head)+[2])
    if int(head.real+head.imag+2)%2:rec['reason']='sector'
    else:
     core=sorted([xy(q)for q in hook if (q-head)/rot(2)in K]);white=sorted([xy(q)for q in hook if tr(W[atom]+M)['req'].get((q-head)/rot(2))is False])
     if core or white:rec.update(reason='young_hook_CURRENT_core_or_first_WHITE',hook_CORE=core,hook_WHITE=white)
     else:
      assert name=='g_R39'and atom=='D'and inp==1j and (r-head)/rot(2)==-1-1j and -1-1j in K
      rec.update(reason='same_r_R54_CURRENT_in_D_entry_CORE',r_local=[-1,-1])
    rows[atom,tuple(xy(inp))]=rec
  author={(v['atom'],tuple(v['input'])):v for v in case['all16_clock2_tag_input_alignments'][name]};assert rows==author
  expected={'sector':6,'young_hook_CURRENT_core_or_first_WHITE':2}if name=='r_R54'else{'sector':2,'young_hook_CURRENT_core_or_first_WHITE':5,'same_r_R54_CURRENT_in_D_entry_CORE':1};assert Counter(x['reason']for x in rows.values())==expected
 for idx,t in enumerate(case['two_N4_target_obligations']):
  target=off+[-1-5j,-4j][idx];tag=[g,r][idx];assert t['target_U_N']==xy(target)and t['E_terminal_H_max']==target.real+target.imag-3 and t['minimum_E_tag_loss_RAW_exit_H']==tag.real+tag.imag-1 and t['minimum_E_tag_loss_RAW_exit_H']>t['E_terminal_H_max']and tag.real==target.real+1
  if idx==0:assert tag-target==1 and 1 in K
  else:
   assert tag-target==1+1j and tr(W['U']+M)['req'][1+1j]is False
   assert next((i,c)for i,(q,h,c)in enumerate(tr(W['U'])['reads'])if q==1+1j)==(6,'R')
 checked.append(dict(foreign=a,r_S_role_counts={'sector':6,'hook':2},g_S_role_counts={'sector':2,'hook':5,'rCORE':1},targets=[q['target_U_N']for q in case['two_N4_target_obligations']]))
out=dict(status='PASS four specified N4 hook-loss targets excluded for arbitrary initial ordinary preparation',manifest=sha(MF),script=sha(S),checked=checked,analytic_review=['All eight true external BLACK inputs and every new exit-core slot reconstructed from actual RAW+M. Alive CORE absorption is CURRENT loss and is not confused with death. C has no such external input.','Initial negative-y g/r cannot first lose in N0 or W1 by exact input and head cones. At S2 the signed hook through C3 protects r first (six sectors/two hook conflicts), then g (two sectors/five hook conflicts/sole D whose entry core contains protected r). This dependency is sequential, not circular.','Exactly four actual Cs produce arbitrary N/W/S/E/N rails. Final N is nonempty by immutable raw CU 29/1 conflict. E losses exit H>=tagH-1, whereas final E H<=targetH-3, which contradicts for the appropriate g/r tag. Final N loss exits x>=tagx>targetx with nondecreasing later x.','At the first Q/B target SAME g lies in U entry core; at the second SAME r is BLACK against actual U first R6. Both source birth ticks39/54 and complete foreign outputs checked. No first-letter, U ancestry, simple proxy, postforeign age, length cap or future-output premise.','Only these four N4 targets close. W5, hook-missing contacts, arbitrary-tail simplicity, second foreign, global coverage and capture remain open.']);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
