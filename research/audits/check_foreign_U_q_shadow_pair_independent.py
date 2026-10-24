from pathlib import Path
from collections import Counter
import json,hashlib
P=Path(__file__);R=P.parent.parent;D=R/'foreign_U_star_q_shadow_pair_cuts_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();mf=D/'manifest.json';assert sha(mf)=='6a4c8f23688ba5efe031edc9749a096420c8bc0b9d73e21ae3fd6eae6962271e';m=json.loads(mf.read_text())
for f,h in m['files'].items():assert sha(D/f)==h
ref=json.loads((D/'q_shadow_pair_cuts.json').read_text())
for f,h in ref['dependencies'].items():assert sha(R/f)==h
bp=P.with_name('check_old_V_second_age1_independent.py');ns={'__file__':str(bp)};exec(bp.read_text().split('# Universal')[0],ns);W,M,K,tr,rot,xy=[ns[k]for k in('W','M','K','tr','rot','xy')];raw=lambda s:''.join(W[a]for a in s)
gates=json.loads((R/'foreign_U_port_interfaces_2026-10-23/foreign_U_ports.json').read_text())['interfaces']['star']['gates'];assert len(gates)==69
sup={(z['foreign'],tuple(z['pose'])):z for z in ref['all69_local_gate_reserve_interfaces']};typed={(z['source_full'],z['foreign'],tuple(z['pose'])):z for z in ref['all207_source_tail_typed_cases']};assert len(sup)==69 and len(typed)==207
counts=Counter();branches=Counter();universal=[]
for g in gates:
 A=g['foreign'];p=complex(*g['pose'][:2]);h=g['pose'][2];t=tr(W[A]+M);assert not t['bad'];z=sup[A,tuple(g['pose'])];good={}
 for name,q in(('original_q',-1+2j),('cleanup_A',-1+4j),('cleanup_r',-1+5j)):
  local=(q-p)/rot(h);rr=[(i,ch)for i,(r,hh,ch)in enumerate(t['reads'])if r==local];req=t['req'].get(local);core=local in K;ok=not core and req is not False;good[name]=ok;s=z['ports'][name]
  assert s['global_cell']==xy(q)and s['FOREIGN_local']==xy(local)and s['before_BLACK']==req and s['in_actual_FOREIGN_entryK']==core and s['positive_CURRENT_compatible']==ok
  assert [(v['combined_tick0'],v['turn'])for v in s['all_physical_reads']]==rr
  for i,v in enumerate(s['all_physical_reads']):
   tick=rr[i][0];owner=v['owner'];within=tick<len(W[A]);assert owner['tick0']==(tick if within else tick-len(W[A]))and owner['read_number1']==owner['tick0']+1
   assert owner['owner']==('own FOREIGN RAW'if within else'next actual word M11 prefix; not an extra marker word')
 qgood=good['original_q'];sgood=good['cleanup_A']and good['cleanup_r'];branch='both_genuine_ancestry_branches_necessary_only'if qgood and sgood else'must_retain_SAME_original_q_before_FOREIGN'if qgood else'must_have_had_age2_qcleanup_and_hold_SAME_r_A_shadows'if sgood else'impossible_for_ALL_source_tail_types';assert z['plain_U_necessary_ancestry']==branch;branches[branch]+=1
 if not(qgood or sgood):universal.append((A,tuple(g['pose'])))
 for source,ok in(('U',qgood or sgood),('UC',qgood),('UCC',sgood)):
  cl='necessary_only_not_cut_by_this_reserve'if ok else'all_age_genuine_reserve_conflict';assert typed[source,A,tuple(g['pose'])]['classification']==cl;counts[source,cl]+=1
assert branches==ref['plain_U_branch_counts']and set(universal)=={(A,(-5,3,2))for A in'FQB'}
nexts=[];ucce=tr(raw('UCC'));assert[*xy(ucce['p']),ucce['h']]==[-1,5,2]
for source,z in zip(('D','DC','V','VC','VCC','U','UC','UCC','F','Q','B'),ref['UCC_genuine_shadow_forcing_all8_plus3_foreign_successors']):
 t=tr(raw('UCC'+source)+M);ok=not t['bad'];assert z['next_word']==source and z['feasible']==ok
 if ok:nexts.append(source)
 else:
  i,j,p,ch=t['bad'];s=z['conflict'];first=next((k,c)for k,(q,hh,c)in enumerate(t['reads'])if q==p);assert(i,xy(p),list(first))==(s['tick'],s['cell'],s['first_read'])
assert nexts==['V','VC']
for A in'FQB':
 t=tr(W[A]+M)
 for q,i in((-4+1j,39),(-4-2j,52)):
  assert t['req'][q]is False and next((j,c)for j,(p,h,c)in enumerate(t['reads'])if p==q)==(i,'R')and i<len(W[A])
 assert next((j,c)for j,(p,h,c)in enumerate(t['reads'])if p==-4-1j)==(51,'L')
out={'status':'PASS bounded 69-gate all-age original-q / BOTH-shadow reserve intersection','manifest_sha256':sha(mf),'dependencies':ref['dependencies'],'counts':[{ 'source':k[0],'classification':k[1],'count':v}for k,v in sorted(counts.items())],'plain_U_branch_counts':dict(branches),'all_source_obstructions':universal,'UCC_only_successors':nexts,'analytic_review':['This is an intersection of signed existing69 actual firstforeign star gates, not an independently new geometric catalogue. Each complete RAW plus genuine followingM11 mask and every physical read owner is freshly reconstructed. TRUE outsideK or MISS is allowed, not mistaken for permanence.','Signed all-age e19a yields q CURRENT or both exact cleanup r/A CURRENT beforeFOREIGN; UC forcesq, and all8+3 actual UCC successors leave only V/VC at(-1,5,S), forcing the genuine cleanup branch. CORE incompatibility concerns the preforeign external CURRENT definition; it does not declare an alive core cell physically dead.','Exactly3U/10UC/13UCC cuts,181 necessary states. The universal F/Q/B(-5,3,S) cut uses originalq firstR39 or shadowr firstR52 in actual commonF56 RAW. ShadowA firstL51 does not rescue r: no earlier read of r occurs, so its original BLACK funding state contradictsR52. No r-lock is imported across foreign.','The all-age guarantee is only within the preceding uninterrupted U-entry complete-eight factor; completion of the named foreign is excluded, not every arbitrary ant continuation or partial fine prefix. No novelty count, attainment, cycle-fuel, or capture conclusion.']};P.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(P),sha(P.with_suffix('.json')))
