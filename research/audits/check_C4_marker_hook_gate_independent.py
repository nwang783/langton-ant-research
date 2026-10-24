from pathlib import Path
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'C4_marker_hook_foreign_gate_guard_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();mf=D/'manifest.json';assert sha(mf)=='b759ce46c8c2a98bad2ba156654ce64f63bbaa54899f7c1c8bbb47c027cae0b5';m=json.loads(mf.read_text())
for f,h in m['files'].items():assert sha(D/f)==h
for f,h in m['dependencies'].items():assert sha(R/f)==h
J=json.loads((D/'C4_marker_gate.json').read_text());ns={'__file__':str(S.with_name('check_old_V_second_age1_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Universal')[0],ns);W,M,K,tr,rot,xy=[ns[k]for k in('W','M','K','tr','rot','xy')];G={a:tr(W[a])for a in W};CT={a:tr(W[a]+M)for a in W};I={a:{q for q,b in CT[a]['req'].items()if b and q not in K}for a in'DCVU'};assert not I['C']and sum(len(I[a])for a in'DVU')==8
allrows=[]
for case in J['all5_source_gate_cases']:
 src=case['source_foreign'];tag=complex(*case['old_marker_tag']);g=complex(*case['guard_original']);target=complex(*case['candidate_FOREIGN_ENTRY'][:2]);assert case['candidate_FOREIGN_ENTRY'][2]==2
 assert G[src]['last'][tag]==('R',case['source_tag_R_tick0'])and G[src]['last'][g]==('R',case['source_guard_R_tick0'])
 ec={G[src]['p']+rot(G[src]['h'])*k for k in K};assert tag not in ec and g not in ec
 expected=(tag,g,target)
 assert expected==(-2-1j,-1-1j,-3-1j)or(src in'QB'and expected==(-3-2j,-3-1j,-4-2j))
 seen=set()
 for a in'DVU':
  for q in I[a]:
   p=g+q;ep=p-G[a]['p'];dx,dy=int((ep-target).real),int((ep-target).imag);models=[]
   for v in range(max(dx+1,0)):
    d=dx-v;num=dy-d-3*v
    if num>=0 and num%4==0:models.append((d,v,num//4))
   assert not models;row=next(z for z in case['all8_first_S4_guard_loss_exits']if z['consumer']==a and z['true_input']==xy(q));assert row['consumer_ENTRY']==[*xy(p),2]and row['actual_RAW_EXIT']==[*xy(ep),2]and row['remaining_S_weights']==[dx,dy]and not row['all_nonnegative_remaining_D_V_U_counts']
   t=next(t for t,(p0,h,c)in enumerate(CT[a]['reads'])if p0==q);assert CT[a]['reads'][t][2]=='L'and row['actual_physical_L']['context_tick0']==t
   if t>=len(W[a]):assert q in{G[a]['p']+rot(G[a]['h'])*k for k in K}
   seen.add((a,q));allrows.append((src,xy(g),a,xy(q),xy(p),xy(ep),t))
 assert len(seen)==8
 for row in case['all3_NEXT_FOREIGN_reader_conflicts']:
  a=row['actor'];q=target-tag;qg=target-g;ft=next((c,t)for t,(p,h,c)in enumerate(CT[a]['reads'])if p==q);fg=next((c,t)for t,(p,h,c)in enumerate(CT[a]['reads'])if p==qg);assert q==-1 and ft==('L',1)and row['actual_FOREIGN_old_tag_L']['owner_tick0']==1 and row['guard_local']==xy(qg)
  if target==-3-1j:assert qg==-2 and fg==('R',44)
  else:assert qg==-1-1j and qg in K
  assert row['guard_first_actual_read']['owner_tick0']==fg[1]
 for row in case['all3_genuine_marker_owned_predecessor_roles']:
  a=row['previous_atom'];p=target+G[a]['p'];slot=p-tag;assert row['actual_ENTRY']==[*xy(p),2]and row['actual_RAW_EXIT']==[*xy(target),2]and row['marker_only_original_tag_slot']==xy(slot)and slot not in G[a]['last'];t=next(t for t,(q,h,c)in enumerate(CT[a]['reads'])if q==slot);assert t==len(W[a])+1 and row['physical_L']['context_tick0']==t
O=dict(status='PASS two selected C4 next-FOREIGN marker-hook gates only',manifest=sha(mf),script=sha(S),source_cases=5,recipient_readers=15,all40_loss_roles=allrows,analytic_review=[
'Signed f24 sourceR46 for F/Q/B and signed528 sourceQ/B hookR50 are SAME CURRENT through ordinaryC3. Direct complete C context has no true external BLACK input: it cannot erase or capture an independent CURRENT original at C4. Only finalS4 DVU first-loss roles remain before the candidate entry.',
'Every eight-role true input interface is independently regenerated from firstL requirements minus actual entryK, including marker-only exitCORE captures. Exact nonnegative S displacement equations have no solution from any such RAW exit to either selected recipient. No epoch-length bound or order assumption is used.',
'At firstrecipient(-3,-1,S), guardR46 is first requested WHITE at ownR44 and excludes completion, although oldR47 can physically die at earlier ownL1. At secondrecipient(-4,-2,S), guardR50 is actual entryCORE and contradicts its stillCURRENT status. The guard stops at recipientENTRY, never claims through-contact permanence.',
'All fifteen recipient words and genuine D/V/U upper marker-only preceding roles retain exact raw-vs-marker ownership. D is conservatively retained even though a separate grammar may exclude it. These are two selected C4 target gates, not all C4 or a future foreign seal, source-F all-length persistence, pose-unreachability, global simplicity or capture.'])
S.with_suffix('.json').write_text(json.dumps(O,indent=2)+'\n');print(O['status']);print(sha(S.with_suffix('.json')))
