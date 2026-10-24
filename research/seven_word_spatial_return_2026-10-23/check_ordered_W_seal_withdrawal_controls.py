"""Exact genuine U-entry controls exposing omitted post-C2 S transport."""
from pathlib import Path
import json
import hashlib
import importlib.util
ROOT=Path('/workspace/shared/langton');HERE=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location('lit',ROOT/'word_stabilization/check_foreign_return_interfaces.py')
lit=importlib.util.module_from_spec(sp);sp.loader.exec_module(lit)
GP=ROOT/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json'
G=json.loads(GP.read_text())['geometry']
controls=[]
for seq,source_index,tag,expected_seed in((
    [7,4,6,4,4],1,(0,5),16),([7,6,4,4],0,(-1,2),14)):
    raw=''.join(G[a]['word']for a in seq);whole=raw+lit.M
    tr=lit.trace(whole);assert tr['feasible']
    seed={q for q,(c,t)in tr['first'].items()if c=='L'};assert len(seed)==expected_seed
    B=set(seed);p=(0,0);h=0;tick=0;clock=0;entries=[];reads=[];source_exit=None
    for i,a in enumerate(seq):
        entries.append(dict(full_packet=G[a]['name'],entry=(*p,h),tick=tick,C_clock=clock))
        for c in G[a]['word']:
            assert(p in B)==(c=='L')
            if p==tag:reads.append((c,tick))
            if c=='L':B.remove(p)
            else:B.add(p)
            h=(h+(1 if c=='R'else-1))%4;d=lit.DIRS[h];p=(p[0]+d[0],p[1]+d[1]);tick+=1
        if i==source_index:source_exit=dict(tick=tick,pose=(*p,h),tag_current=tag in B)
        clock += 2 if a in (6,9) else 1 if a in (1,5,8) else 0
    raw_exit=dict(tick=tick,pose=(*p,h),mass=len(B),tag_current=tag in B)
    for j,c in enumerate(lit.M):
        assert(p in B)==(c=='L')
        if p==tag:reads.append((c,tick))
        if c=='L':B.remove(p)
        else:B.add(p)
        h=(h+(1 if c=='R'else-1))%4;d=lit.DIRS[h];p=(p[0]+d[0],p[1]+d[1]);tick+=1
    assert entries[-1]['C_clock']-entries[source_index]['C_clock']==2
    source=entries[source_index];consumer=entries[-1]
    normalized_consumer=(consumer['entry'][0]-source['entry'][0],
                         consumer['entry'][1]-source['entry'][1],2)
    assert normalized_consumer==((0,4,2)if source_index==1 else(-1,5,2))
    actual_lower=(consumer['entry'][0],consumer['entry'][1]-3)
    assert actual_lower==tag and source_exit['tag_current']and raw_exit['tag_current']
    assert reads[-1]==('L',len(raw)+1)
    controls.append(dict(full_packet_sequence=[G[a]['name']for a in seq],
        complete_finite_seed=sorted(seed),entry_mass=len(seed),unlisted_cells_WHITE=True,
        full_packet_entries=entries,source_index=source_index,source_kind=G[seq[source_index]]['name'],
        source_tag_physical_site=tag,source_tag_normalized_output=(0,1)if source_index==1 else(-1,2),
        source_tag_all_actual_reads=reads,source_full_exit=source_exit,
        consumer_V_pose_in_source_frame=normalized_consumer,consumer_input=(0,3),source_to_consumer_C_age=2,
        consumer_input_physical_owner='word_after_final_V_RAW_phase2; here the actual M11 phase2',
        actual_RAW_exit=raw_exit,after_actual_M11=dict(pose=(*p,h),mass=len(B)),
        genuine_U_entry_eight_factor=True,foreign_or_three_C_residue_attainment_claimed=False))
assert controls[0]['source_tag_all_actual_reads']==[('R',39),('L',131)]
assert controls[1]['source_tag_all_actual_reads']==[('L',13),('R',21),('L',113)]
deps=[GP,ROOT/'word_stabilization/check_foreign_return_interfaces.py',HERE/'ordered_W_full_output_seal_manifest.json']
out=dict(status='POSITIVE_U_ENTRY_CONTROLS_AND_WITHDRAWAL_OF_PENDING_PLAIN_SOURCE_CUT',
    rejected_manifest='6ea48d5dc26b7265ad55e83a99c5282a71fdbfc41f86f88b94934844306c3ac1',
    reason='Its two plain-source endpoint equations omit the post-C2 S run. Both purported ownership contradictions have genuine U-entry eight countercontrols.',
    controls=controls,
    valid_results_unchanged=['signed bf616fdc ordered matching/first-D/direct visibility','signed ef645520 older-entry reproductive cost with role-label erratum f2ff1b4d'],
    exact_three_C_residue_seal_proved=False,
    dependencies={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()for p in deps})
(HERE/'ordered_W_seal_withdrawal_controls.json').write_text(json.dumps(out,indent=2)+'\n')
print('Genuine U-entry controls replayed from16/14 black cells; pending6ea48d5 plain-source cut withdrawn.')
