from pathlib import Path
from collections import Counter
import json,hashlib
P=Path(__file__);R=P.parent.parent;D=R/'old_V_second_age3_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();mf=D/'manifest.json';assert sha(mf)=='23cd0aaee1e1f6149d46f265b83456cbf8affda8e2672484add3e2b6d5722828';m=json.loads(mf.read_text())
for f,h in m['files'].items():assert sha(D/f)==h
ref=json.loads((D/'V_age3_ports.json').read_text())
for f,h in ref['dependencies'].items():assert sha(R/f)==h
bp=P.with_name('check_old_V_second_age1_independent.py');ns={'__file__':str(bp)};exec(bp.read_text().split('# Universal')[0],ns);W,M,K,tr,rot,xy=[ns[k]for k in('W','M','K','tr','rot','xy')];raw=lambda s:''.join(W[a]for a in s)
G=json.loads((R/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json').read_text())['geometry'];ids=(0,1,4,5,6,7,8,9);compact={i:j for j,i in enumerate(ids)};COUNT={tuple(map(int,line.split()[:8]))for line in(R/'core_periodicity_new/chronology_dcuv/critical_ucc_count5/frozen_20261023_0813/01_closure.tsv').read_text().splitlines()}
for i in ids:
 g=G[i];t=tr(raw(g['name'])+M);assert not t['bad']and set(map(tuple,g['inputs']))=={tuple(xy(q))for q,b in t['req'].items()if b and q not in K}
sup={(z['actual_full_source'],z['consumer'],z['input_slot0'],z['true_full_source_ENTRY_C_age']):z for z in ref['all276_original_C_port_age0_through3_queries']};assert len(sup)==276;counts=Counter();roles=[]
for si in(4,5,6):
 name=G[si]['name'];ft=tr(raw(name));rr=[(i,ch)for i,(q,h,ch)in enumerate(ft['reads'])if q==2+1j];assert rr==[(7,'R')]and 2+1j not in{ft['p']+q*rot(ft['h'])for q in K};roles.append(name)
 for age in range(4):
  h=(-age)%4
  for ci in ids:
   for j,cell in enumerate(G[ci]['inputs']):
    p=2+1j-complex(*cell)*rot(h);x,y=xy(p);key=(compact[si],compact[ci],x,y,h,2,1,age);why='sector'if(x+y+h)%2 else'signed_COUNT5'if key in COUNT else'UNEXCLUDED';assert why!='UNEXCLUDED';counts[why]+=1;z=sup[name,G[ci]['name'],j,age];assert z['reason']==why and z['key']==list(key)and z['consumer_pose']==[x,y,h]and z['input_cell']==cell
assert counts=={'sector':138,'signed_COUNT5':138}
# Reuse signed independent geometry reconstruction, NOT any new author scan.
bo=R/'second_contact_signed_obligations_2026-10-24/signed_current_obligations.json';geom=json.loads(bo.read_text());audit=P.with_name('check_second_contact_current_obligations_independent.json');a=json.loads(audit.read_text());assert a['manifest_sha256']=='bc2a9623bc2e3fc479a802ea11e01ef15112c91000a628dd6d8fa975ef8a2135'and a['mandatory_core_status_qualification_sha256']=='389fec8938535834da396fd12cddceef681e45c3a1ada0bbc66f3b545858b8d2'
bases=[b for b in geom['all267_foreign_typed_base_rows']if(b['old'],b['n'])==('V',3)];assert len(bases)==141 and all(b['reason']=='keep'for b in bases)
ours={(b['A'],b['b1'],b['b2'],tuple(b['pa']),tuple(b['p2']))for b in bases};theirs={(b['foreign'],b['first'],b['second'],tuple(b['foreign_pose']),tuple(b['second_pose']))for b in ref['all141_foreign_typed_two_branch_cases']};assert ours==theirs
v=tr(W['V']);core={v['p']+q*rot(v['h'])for q in K};VO={q for q,(ch,i)in v['last'].items()if ch=='R'and q not in core};helper={4j-q for q in VO};assert len(helper)==6
for source in('V','VC'):
 t=tr(raw(source));ck={t['p']+q*rot(t['h'])for q in K}
 for q in VO:assert t['last'][q]==v['last'][q]and q not in ck
priority=Counter();owner_count=0
for row in ref['all141_foreign_typed_two_branch_cases']:
 T=row['foreign']+row['first']+row['second'];tt=tr(raw(T)+M);p=complex(*row['foreign_pose'][:2]);h=row['foreign_pose'][2];first={}
 for i,(q,hh,ch)in enumerate(tt['reads']):first.setdefault(q,(ch,i))
 def checkcells(cells,supplied):
  global owner_count
  got=[]
  for q in cells:
   local=(q-p)/rot(h);fr=first.get(local)
   if local in K:got.append((tuple(xy(q)),tuple(xy(local)),'CURRENT identity in foreign ENTRY core',None))
   elif fr and fr[0]=='R':got.append((tuple(xy(q)),tuple(xy(local)),'first read requires WHITE',fr[1]))
  assert set(got)=={(tuple(z['SAME_current_cell']),tuple(z['foreign_local']),z['reason'],z.get('combined_tick0'))for z in supplied}
  for z in supplied:
   if'combined_tick0'not in z:continue
   owner_count+=1;i=z['combined_tick0'];o=z['actual_owner'];lo=0;found=False
   for j,aa in enumerate(T):
    if i<lo+len(W[aa]):assert(o['actual_atom_index0'],o['actual_atom'],o['canonical']['context_tick0'])==(j,aa,i-lo);found=True;break
    lo+=len(W[aa])
   if not found:assert o['actual_atom']=='next actual word'and o['next_word_tick0']==i-lo and o['next_word_read_number1']==i-lo+1
  return bool(got)
 z=row['original_A_CURRENT_branch'];old=checkcells({0j,1+0j,1j},z['existing_original_r_B_A_conflicts']);new=checkcells({2+1j},z['genuine_C_port_conflicts']);help=checkcells({0j,1+0j}|helper,row['original_A_retired_branch']['genuine_helper_current_conflicts']);assert help and(old or new);why='r_or_B_or_original_A'if old else'genuine_C_port_276_query_guard';assert why==z['priority_reason'];priority[why]+=1
assert priority=={'r_or_B_or_original_A':114,'genuine_C_port_276_query_guard':27}and len(ref['all423_actual_source_typed_cases'])==423
for src in roles:
 subset=[r['base_case']for r in ref['all423_actual_source_typed_cases']if r['actual_full_source']==src];assert subset==ref['all141_foreign_typed_two_branch_cases']
out={'status':'PASS all genuine old V/VC/VCC true-age3 FIRST SECOND-RAW source contacts excluded','manifest_sha256':sha(mf),'dependencies':ref['dependencies'],'independent_geometry_report_sha256':sha(audit),'source_roles':roles,'query_counts':dict(counts),'geometry_counts':[14,47,141],'A_current_priority':dict(priority),'actual_read_owner_checks':owner_count,'analytic_review':['Genuine C=(2,1) is read exactly once at sourceV RAW R7/read8; actual VC/VCC preserve SAME output outside finalK. All eight fullpacket input sets are independently recovered from literal complete contexts, including marker-owned input/core capture. All276 source-tail/age0..3/true-input alignment keys are regenerated:138 sector,138 members of the signed exhaustive COUNT5 closure. Source/consumer compact IDs and true full-entry ages checked; no output-slot/input-name substitution.','The COUNT5 premise excludes an initial CURRENT loss in any complete old-eight consumer, including core absorption, not just physical residual-output retirement. Completion-incompatible earlier entries are harmless extra necessary queries. Consequently original C is CURRENT at foreign3; no assertion crosses foreign.','Exact14/47/141 geometry is matched bijectively to the separately independently signed full table bc2a+389. All actual before masks/owner labels regenerated:114 originalr/B/A-current cuts and27 additionalC cuts; every retiredA branch fails the genuine age2 helper six-output cohort at age1. SourceV/VC/VCC expansion is exact423, not new physical geometries.','Signed2043 supplies the ONLY all-age first-A cleanup V/VC0,4S at2, so no missing later retirement branch. Universal produced-input minimum2 protects its six actual outputs to foreign3, and actual ownC preserves each sameR identity. No at-most-one seal, postforeign maturity, or long prefix search is used.','Only oldV at true age3 chronological FIRST SECOND-RAW contact is closed. Combined with prior independently signed ages0/1/2/4 this removes oldV from that limited source interface, not every secondcontact or arbitrary-tail simplicity.']};P.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(P),sha(P.with_suffix('.json')))
