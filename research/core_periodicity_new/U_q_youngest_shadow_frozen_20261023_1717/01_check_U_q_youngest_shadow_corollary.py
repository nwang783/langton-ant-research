"""Dependency-bound exact assembly: retirement shadow versus same-clock cohorts.
No path search, age threshold, reachability or component theorem.
"""
from pathlib import Path
import json,hashlib
W=Path(__file__).resolve().parent
GP=W/'chronology_dcuv/literal_residual_geometry.json'
MP=W/'u1_minclock_cohort_frozen_20261023_1118/02_u_minimum_clock_cohort_by_phase.json'
SP=W/'U_white_shadow_frozen_20261023_1709/02_U_white_shadow_retirement.json'
AP=W/'atomic_core_record_interface_frozen_20261023_1359/02_atomic_core_record_interface.json'
G=json.loads(GP.read_text())['geometry'];M=json.loads(MP.read_text());S=json.loads(SP.read_text());A=json.loads(AP.read_text())
inputs=[(-1,1),(-1,2),(-1,4),(0,2),(0,3)];z=(-1,3)
def rot(p,h):
 x,y=p;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def output_cells(r):
 p=r['head'];return{(p[0]+rot(o,p[2])[0],p[1]+rot(o,p[2])[1])for o in G[r['packet']]['outputs']}
assert S['target']['inputs']==[list(p)for p in inputs]and S['target']['white_shadow']==list(z)
pairs=[set(map(tuple,p))for p in S['minimal_blocking_pairs']]
assert {inputs[1],inputs[4]}in pairs
for a in[7,8,9]:
 assert list(map(tuple,G[a]['inputs']))==inputs
 assert next(r for r in G[a]['requirements']if tuple(r[:2])==z)[2]is False
 # A preceding packet's terminal M11 cannot consume a final input here.
 assert all(tuple(r[:2])not in inputs for r in G[a]['requirements']if r[3]<11)

def annotate(c,h):
 r=c['last_producer'];O=output_cells(r);got=sum(1<<i for i,p in enumerate(inputs)if p in O)
 assert got==r['output_mask']
 # All five final identities are current after this sole minimum-clock birth.
 assert c['birth_packets']==1 and (c['older_input_mask']|got)==31
 blockers=[sorted(p)for p in pairs if p<=O]
 cut=z in O and bool(blockers)
 return dict(heading=h,source_packet=r['packet'],source_pose=r['head'],older_input_mask=c['older_input_mask'],minimum_age_input_mask=c['minimum_age_input_mask'],source_outputs=sorted(O),fresh_z=z in O,co_born_cover_pairs=blockers,excluded_by_shadow=cut)
raw2=next(p for p in M['phases']if p['heading']==2)
assert raw2['summary']['completed_states']==3 and raw2['summary']['max_relevant_birth_packets']==1
rawrows=[annotate(c,2)for c in raw2['completed_abstract_states']]
assert[(r['source_packet'],r['source_pose'],r['older_input_mask'],r['minimum_age_input_mask'])for r in rawrows]==[(a,[1,3,2],5,26)for a in[7,8,9]]
assert all(r['excluded_by_shadow']for r in rawrows)
strict=[]
for p in M['U1_strict_record_phases']:
 strict += [annotate(c,p['heading'])for c in p['completed_abstract_states']]
assert len(strict)==16
before=[sum(r['heading']==h for r in strict)for h in range(4)]
after=[sum(r['heading']==h and not r['excluded_by_shadow']for r in strict)for h in range(4)]
assert before==[4,3,3,6]and after==[4,3,0,4]
# The signed enlarged-history interface removes precisely its four phase-zero rows.
removed=A['removed_q_youngest_templates']
assert len(removed)==4
# All such rows are the residue-zero q-youngest cohort, as signed by that interface.
assert {(r['source_packet'],tuple(r['source_pose']),r['minimum_age_input_mask'])for r in strict if r['heading']==0}=={(r['source'],tuple(r['pose']),r['youngest_input_mask'])for r in removed}
assert all(r['C_age_residue']==0 and r['atomic_source_peak']==30 and r['excluded_under_enlarged_history']for r in removed)
enlarged=[r for r in strict if not r['excluded_by_shadow']and r['heading']!=0]
assert len(enlarged)==7
D=[GP,MP,SP,AP,W/'u1_minclock_cohort_frozen_20261023_1118/manifest.json',W/'U_white_shadow_frozen_20261023_1709/manifest.json',W/'atomic_core_record_interface_frozen_20261023_1359/manifest.json',Path(__file__).resolve()]
O=dict(status='AUTHOR_DEPENDENCY_BOUND_ASSEMBLY_PASS_PENDING_INDEPENDENT_REVIEW',scope='Actual complete recurrent-eight factors only. Global produced-q-youngest age residue-two exclusion; original strict U1 sixteen-to-eleven necessary-template reduction; seven under separately enlarged atomic-history premise. No U count, component merger, record closure or capture.',raw_heading_two_templates=rawrows,strict_U1_templates=strict,before_phase_counts=before,after_shadow_phase_counts=after,enlarged_history_remaining_templates=enlarged,dependencies={str(p.relative_to(W)):hashlib.sha256(p.read_bytes()).hexdigest()for p in D})
(W/'chronology_dcuv/U_q_youngest_shadow_corollary.json').write_text(json.dumps(O,indent=2)+'\n')
print(json.dumps(dict(raw_phase_two_excluded=len(rawrows),strict_before=before,strict_after=after,enlarged_remaining=len(enlarged)),indent=2))
