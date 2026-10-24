"""Exact preforeign identity-ancestry interfaces following the W archive.

All W lengths are retained. No postforeign maturity rule, finite boundary
quotient, or claim about all counterfactual color influence is made.
"""
from pathlib import Path
from collections import Counter
import importlib.util
import json
import hashlib

ROOT=Path('/workspace/shared/langton');HERE=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location('lit',ROOT/'word_stabilization/check_foreign_return_interfaces.py')
lit=importlib.util.module_from_spec(sp);sp.loader.exec_module(lit)
GP=ROOT/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json'
WP=ROOT/'word_stabilization/shifted1_llrlrrrrlll_fold_coalesced_port_quotient.json'
CP=ROOT/'core_periodicity_new/chronology_dcuv/critical_ucc_count5/frozen_20261023_0813/01_closure.tsv'
G=json.loads(GP.read_text())['geometry']
WORDS={a:r['word']for a,r in zip('DCVUFQB',json.loads(WP.read_text())['macro_words'])}
KEEP=(0,1,4,5,6,7,8,9);COMPACT={a:i for i,a in enumerate(KEEP)}
COUNT={tuple(map(int,line.split()[:8]))for line in CP.read_text().splitlines()}
TAIL={0:0,1:1,4:0,5:1,6:2,7:0,8:1,9:2}
def add(p,q):return p[0]+q[0],p[1]+q[1]

young_queries=[]
for age in(0,1):
    h=(-age)%4
    for source in KEEP:
        for output in map(tuple,G[source]['outputs']):
            for consumer in KEEP:
                for input_slot in map(tuple,G[consumer]['inputs']):
                    z=lit.rot(input_slot,h);p=(output[0]-z[0],output[1]-z[1])
                    key=(COMPACT[source],COMPACT[consumer],*p,h,*output,age)
                    reason=('sector'if(sum(p)+h)%2 else'signed_COUNT5'if key in COUNT
                            else'source_not_yet_full_complete'if age<TAIL[source]else'UNRESOLVED')
                    assert reason!='UNRESOLVED'
                    young_queries.append(dict(source=G[source]['name'],output=output,
                        consumer=G[consumer]['name'],input=input_slot,pose=(*p,h),
                        full_source_entry_C_age=age,source_full_completion_C_age=TAIL[source],
                        reason=reason,count_key=key))
assert len(young_queries)==3128
assert Counter(r['reason']for r in young_queries if r['full_source_entry_C_age']==0)=={
    'sector':760,'signed_COUNT5':770,'source_not_yet_full_complete':34}
assert Counter(r['reason']for r in young_queries if r['full_source_entry_C_age']==1)=={
    'sector':804,'signed_COUNT5':748,'source_not_yet_full_complete':12}

# E reproduction uses V's real distinguished port(1,2), U's lower a(0,3).
# U(-1,4) belongs to the DIFFERENT W archive submatching, not this claim.
reproductive_queries=[]
for source in KEEP:
    for output in map(tuple,G[source]['outputs']):
        for consumer,port in((4,(1,2)),(7,(0,3))):
            assert list(port)in G[consumer]['inputs']
            z=lit.rot(port,2);p=(output[0]-z[0],output[1]-z[1])
            key=(COMPACT[source],COMPACT[consumer],*p,2,*output,2)
            if(sum(p)+2)%2:reason='sector'
            elif key in COUNT:reason='signed_COUNT5'
            elif source==6 and output==(0,1):reason='signed_V_original_A_no_parallel_VU_distinguished_consumer'
            elif source==9 and output==(-1,2):reason='signed_U_recycled_q_only_V_VC_lower0_3'
            else:raise AssertionError((source,output,consumer,port,p))
            reproductive_queries.append(dict(source=G[source]['name'],output=output,
                consumer=G[consumer]['name'],distinguished_input=port,pose=(*p,2),
                full_source_entry_C_age=2,reason=reason,count_key=key))
assert len(reproductive_queries)==136
assert Counter(r['reason']for r in reproductive_queries)=={'sector':64,'signed_COUNT5':68,
    'signed_V_original_A_no_parallel_VU_distinguished_consumer':2,
    'signed_U_recycled_q_only_V_VC_lower0_3':2}

# An E D takes input p+rot_E(0,1) and produces p+rot_E(2,0),
# hence maps an actual W input identity at q to a fresh output at q+(-1,-2).
# If that new site meets a future context with min x=-3, q.x>=-2.
# Since W outputs have x=-A-local_y and local_y>=0, A<=2.
# Only heads reached by empty,D,DD prefixes occur. The first base is D-family.
contexts={}
for foreign,pose in(('F',(2,-5,1)),('Q',(4,-5,1)),('B',(5,-4,1))):
    tr=lit.trace(WORDS[foreign]+WORDS['C']+lit.M);assert tr['feasible']
    contexts[foreign]={add(pose[:2],lit.rot(q,pose[2])):v for q,v in tr['first'].items()}
    assert min(q[0]for q in contexts[foreign])==-3
assert all(y>=0 for a in KEEP for x,y in G[a]['outputs'])
relay_visibility_queries=[];visible_relays=[]
for foreign,context in contexts.items():
    for prefix,head in(('',(0,1)),('D',(-1,2)),('DD',(-2,3))):
        for source in KEEP:
            if not prefix and source not in(0,1):continue
            for output in map(tuple,G[source]['outputs']):
                qW=add(head,lit.rot(output,3));qE=add(qW,(-1,-2));hit=qE in context
                row=dict(foreign=foreign,earlier_W_prefix=prefix,source=G[source]['name'],
                    output=output,W_output=qW,possible_E_D_output=qE,
                    E_output_in_future_context=hit)
                if hit:
                    p=(output[0],output[1]+1)
                    assert(sum(p)+2)%2==1
                    row.update(source_relative_D_pose=(*p,2),full_source_entry_C_age=2,
                               reason='sector')
                    visible_relays.append(row)
                relay_visibility_queries.append(row)
assert len(visible_relays)==24

deps=[GP,WP,CP,CP.parent/'manifest.json',ROOT/'word_stabilization/check_foreign_return_interfaces.py',
      HERE/'ordered_W_archive_matching_manifest.json',
      ROOT/'core_periodicity_new/V_parallel_reproductive_supply_frozen_20261023_2036/manifest.json',
      ROOT/'core_periodicity_new/U_recycled_q_consumer_frozen_20261023_1954/manifest.json']
out=dict(status='AUTHOR_FROZEN_PREFOREIGN_IDENTITY_TRANSPORT_BOTTLENECK_PENDING_REVIEW',
    scope='The three necessary old-C returned-RAW-C residues and arbitrary W length. All transfer exclusions are before first foreign; literal combined future context is used only for direct visibility. No second foreign or full color/functional-dependence exclusion.',
    all3128_completed_source_young_input_queries=young_queries,
    all136_age2_W_to_E_VU_distinguished_input_queries=reproductive_queries,
    all_finite_head_E_D_relay_visibility_queries=relay_visibility_queries,
    all24_visible_E_D_relay_sector_exclusions=visible_relays,
    identity_ancestry_conclusions=[
        'No completed fullproducer output can supply an actual input at full source-entry C age0 or1.',
        'W outputs cannot fund S or later W inputs; S outputs cannot fund E or later S inputs; E outputs cannot fund later E inputs.',
        'Every E V/U distinguished input is a distinct older residual identity already current at W entry, disjoint from the W archive chosen inputs.',
        'An E D whose actual input identity came from a W full output has its only fresh output outside the future combined context.',
        'Any black-output ancestry edge from W directly into an E producer with a future-visible output must target V or U, and that producer also spends an older W-entry distinguished input.'
    ],
    limitation='All output/input incidence is actual once-only identity spending. This does not remove color guard effects, unchosen boundary ports, arbitrary S/E work, or establish decreasing resource.',
    dependencies={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()for p in deps})
(HERE/'ordered_W_transport_bottleneck.json').write_text(json.dumps(out,indent=2)+'\n')
print('3128 young-input queries;136 reproductive port queries;24 future-visible E-D relays all sector-inactive.')
