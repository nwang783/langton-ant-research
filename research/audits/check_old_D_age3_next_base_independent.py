from pathlib import Path
import json,hashlib
from collections import Counter
R=Path('/workspace/shared/langton');P=R/'old_D_second_age3_next_base_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();mf=P/'manifest.json';assert sha(mf)=='18d9148a8d2c780c54c528c750d6019fd30713508cff6b231f9281aa3f3ee2c1';M0=json.loads(mf.read_text())
for f,h in M0['files'].items():assert sha(P/f)==h
J=json.loads((P/'next_base_guard.json').read_text())
for f,h in J['dependencies'].items():assert sha(R/f)==h
base=R/'audits/check_old_V_second_age1_independent.py';ns={'__file__':str(base)};exec(base.read_text().split('# Universal')[0],ns);W,M,K,tr,rot,xy=[ns[k]for k in('W','M','K','tr','rot','xy')];raw=lambda s:''.join(W[a]for a in s)
t=tr(W['D']);assert(t['p'],t['h'])==(1+1j,0)
roles={};count=0
for role in J['all8_genuine_actual_next_full_sources_and_tag_births']:
 full=role['actual_next_full'];base=full[0];tt=tr(raw(full));bt=tr(W[base]);outcore={tt['p']+q*rot(tt['h'])for q in K};tags={'D':{2+0j},'V':{0j,1+0j},'U':{0j,1j,1+0j,1+1j}}[base]
 assert role['actual_full_entry_pose']==[1,1,0]and role['actual_full_entry_clock']==0 and role['actual_full_completion_clock']==full.count('C')and role['true_full_entry_to_foreign_age']==3
 assert{complex(*z['actual_next_base_slot'])for z in role['genuine_current_tags']}==tags
 for z in role['genuine_current_tags']:
  q=complex(*z['actual_next_base_slot']);assert q not in outcore and tt['last'][q]==bt['last'][q]and tt['last'][q][0]=='R'and all(tick<len(W[base])for tick,(cell,h,ch)in enumerate(tt['reads'])if cell==q)
  assert z['SAME_current_cell']==xy(q+1+1j)and z['actual_base_last_R_tick0']==tt['last'][q][1]
 roles[full]={q+1+1j for q in tags}
assert set(roles)=={'D','DC','V','VC','VCC','U','UC','UCC'}
prior=json.loads((R/'old_D_second_age3_common_beta_2026-10-24/D_age3_common_beta.json').read_text());res=prior['remaining12_necessary_states'];keys=lambda r:(r['base_row_index0'],r['foreign'],r['first'],r['second'],tuple(r['foreign_pose']),tuple(r['second_pose']));basekeys=set(map(keys,res))
def masks(r,tags):
 global count
 T=r['foreign']+r['first']+r['second'];t=tr(raw(T)+M);assert not t['bad'];p=complex(*r['foreign_pose'][:2]);h=r['foreign_pose'][2];first={}
 for i,(q,hh,ch)in enumerate(t['reads']):first.setdefault(q,(ch,i))
 got=[]
 for q in tags:
  z=(q-p)/rot(h);fr=first.get(z)
  if z in K:got.append((tuple(xy(q)),tuple(xy(z)),None))
  elif fr and fr[0]=='R':got.append((tuple(xy(q)),tuple(xy(z)),fr[1]))
 assert got;return got

def owner(T,tick,z):
 global count
 count+=1;lo=0
 for i,a in enumerate(T):
  if tick<lo+len(W[a]):assert(z['actual_atom_index0'],z['actual_atom'],z['canonical']['context_tick0'])==(i,a,tick-lo);return
  lo+=len(W[a])
 assert z['actual_atom']=='next actual word'and z['next_word_tick0']==tick-lo and z['next_word_read_number1']==tick-lo+1
rows=J['all96_actual_full_tail_mask_checks'];assert len(rows)==96
for full,tags in roles.items():
 subset=[r for r in rows if r['actual_next_full']==full];assert set(map(keys,subset))==basekeys
 for r in subset:
  got=masks(r,tags);assert set(got)=={(tuple(z['fact']['SAME_current_cell']),tuple(z['foreign_local']),z.get('combined_tick0'))for z in r['exact_genuine_current_tag_conflicts']}
  # This is the narrower disjunction actually needed, not independent fuel.
  special=3+1j if full[0]=='D'else 1+1j;assert any(g[0]==tuple(xy(special))and g[2]is not None for g in got)
  for z in r['exact_genuine_current_tag_conflicts']:
   if 'combined_tick0'in z:owner(r['foreign']+r['first']+r['second'],z['combined_tick0'],z['actual_owner'])
assert J['all36_next_BASE_type_mask_checks']==[r for r in rows if r['actual_next_full']in'DVU']
dct=tr(raw('DC'));assert dct['last'][3+1j]==('R',18)
sourceDC=J['all12_actual_source_DC_C1_guard_lifts'];assert len(sourceDC)==12
for z,r in zip(sourceDC,res):
 assert z['base_row_index0']==r['base_row_index0']and z['SAME_current_source_cell']==[3,1]and z['genuine_source_C1_common_birth_tick0']==18 and z['source_full_entry_clock']==0 and z['source_full_completion_clock']==1 and z['foreign_clock']==3
 got=masks(r,{3+1j});assert len(got)==1 and got[0][2]==z['actual_combined_first_read'][1]and z['actual_combined_first_read'][0]=='R';owner(r['foreign']+r['first']+r['second'],got[0][2],z['actual_owner'])
assert len(J['all108_actual_source_role_contact_cases'])==108
for full in('D','DC'):
 subset=[r for r in J['all108_actual_source_role_contact_cases']if r['actual_full_source']==full];assert len(subset)==54 and set(map(keys,subset))==set(map(keys,prior['all54_foreign_typed_masks']))
report={'status':'PASS all genuine oldD/DC age3 FIRST SECOND-RAW source cases closed','manifest_sha256':sha(mf),'script_sha256':sha(Path(__file__)),'dependencies':J['dependencies'],'next_base_checks':36,'actual_next_full_tail_checks':96,'sourceDC_C1_lifts':12,'source_role_cases':108,'actual_owner_checks':count,'analytic_review':['Source plainD exits(1,1,N) at clock0; because three C turns remain before FIRSTforeign, actual next COMPLETE old-eight word exists and begins a genuine D/V/U base. No standalone C or invented marker is substituted','Reader-independent common-through-three sublemma66aa applies to actual next D/DC at the SAME clock0 and complete foreign age3; its real immediate-next-atom crossing proof is not recursion or contact-owner relabeling','Next V source r/B trueages5/4 and next U star permanence hold only in preforeign uninterrupted factor. All8 own-tail preservation and actual final-R births independently replayed','SourceDC is a SEPARATE genuine ownC1 common(3,1)R18, protected by signed fullDC cohort2b32 at full source age3 complete boundary, not the next-base alternative','Exact96+12 masks and every physical owner rebuilt. Same-current disjunction (3,1) or(1,1) is not an injective resource or postforeign reserve','Composition is all54 masks for each actual D/DC source,36common+6beta+12guardian. Global second simplicity requires the separate geometric/source assembly, not this local certificate alone']}
f=R/'audits/old_D_age3_next_base_independent.json';f.write_text(json.dumps(report,indent=2)+'\n');print(sha(f));print(report['status'])
