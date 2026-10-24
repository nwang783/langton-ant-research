"""Unbounded-length ordered W archive matching, with real ports and birth IDs.

Finite literal/COUNT5 interfaces support an all-length argument. No dormant
ports are discarded and no global finite-state or decreasing-rank claim occurs.
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
PORT={0:(0,1),1:(0,1),4:(1,2),5:(1,2),6:(0,3),7:(-1,4),8:(-1,4),9:(-1,4)}


def add(p,q):return p[0]+q[0],p[1]+q[1]
def sub(p,q):return p[0]-q[0],p[1]-q[1]


full_ports=[]
for source_id in KEEP:
    port=PORT[source_id]
    assert list(port)in G[source_id]['inputs']and[2,0]in G[source_id]['outputs']
    raw=lit.trace(G[source_id]['word']);context=lit.trace(G[source_id]['word']+lit.M)
    assert raw['last'][(2,0)]==('R',8)
    assert context['first'][port][0]=='L'
    relative=lit.rot(port,3)
    delta=(-relative[0],2-relative[1])
    assert delta==({'D':(1,2),'DC':(1,2),'V':(2,1),'VC':(2,1),
                   'VCC':(3,2),'U':(4,3),'UC':(4,3),'UCC':(4,3)}[G[source_id]['name']])
    full_ports.append(dict(full_packet=G[source_id]['name'],specified_input=port,
                          input_offset_at_W=relative,common_output_offset_at_W=(0,2),
                          matching_displacement_NE=delta,
                          common_physical_birth=('R',8),
                          input_first_physical_read=context['first'][port],
                          input_first_read_inside_same_RAW=port in raw['first'],
                          marker_only_input_owner='next_actual_word_RAW_phase1'if port not in raw['first']else None))

# Every earlier W producer is plain: a C tail would already end that W epoch.
# Full consumer's specified port is explicit, INCLUDING VCC's distinct(0,3).
same_clock_queries=[]
for source_id in(0,4,7):
    for output in map(tuple,G[source_id]['outputs']):
        for consumer_id in KEEP:
            p=sub(output,PORT[consumer_id]);key=(COMPACT[source_id],COMPACT[consumer_id],*p,0,*output,0)
            reason='sector'if sum(p)%2 else'signed_COUNT5'
            if reason=='signed_COUNT5':assert key in COUNT
            same_clock_queries.append(dict(source=G[source_id]['name'],output=output,
                                           consumer=G[consumer_id]['name'],specified_input=PORT[consumer_id],
                                           pose=(*p,0),full_entry_C_age=0,reason=reason,count_key=key))
assert len(same_clock_queries)==128
assert Counter(r['reason']for r in same_clock_queries)=={'sector':64,'signed_COUNT5':64}

# Input and output x orders are strict for every adjacent possible pair. The
# previous base must be plain; the final consumer may carry real C tails.
ordering_rows=[]
for previous in(0,4,7):
    step_A=-lit.rot(G[previous]['endpoint'][:2],3)[0]
    previous_xi=-lit.rot(PORT[previous],3)[0]
    for following in KEEP:
        next_xi=-lit.rot(PORT[following],3)[0]
        decrease=step_A+next_xi-previous_xi
        assert decrease>0
        ordering_rows.append(dict(previous=G[previous]['name'],following=G[following]['name'],
                                  input_x_strict_decrease=decrease,
                                  output_x_strict_decrease=step_A))
assert len(ordering_rows)==24

# Future whole physical contexts for the three necessary returned-C residues.
future_rows=[];CONTEXTS={}
for foreign,pose in(('F',(2,-5,1)),('Q',(4,-5,1)),('B',(5,-4,1))):
    tr=lit.trace(WORDS[foreign]+WORDS['C']+lit.M);assert tr['feasible']
    context={add(pose[:2],lit.rot(q,pose[2])):read for q,read in tr['first'].items()}
    CONTEXTS[foreign]=context
    bounds=(min(x for x,y in context),max(x for x,y in context),
            min(y for x,y in context),max(y for x,y in context))
    assert bounds[0]==-3 and bounds[3]==1
    assert context[(0,1)][0]=='R'
    future_rows.append(dict(foreign=foreign,pose=pose,whole_context_bounds=bounds,
                            first_read_of_first_W_r=context[(0,1)],
                            all_context_sites=[dict(cell=q,first_read=read)for q,read in sorted(context.items())]))

# All W heads are(-A,1+B), with steps D:(A+1,B+1),V:(A+3,B+1),U:(A+4,B).
# Every full output has local y>=0. Future x>=-3 therefore forces A<=3.
assert all(y>=0 for source_id in KEEP for x,y in G[source_id]['outputs'])
small_heads=[('',(0,1)),('D',(-1,2)),('DD',(-2,3)),('DDD',(-3,4)),('V',(-3,2))]
small_head_count_solutions=[]
for d in range(4):
    for v in range(2):
        if d+3*v<=3:
            # No U can fit A<=3; d/v can coexist only when one is zero.
            assert not(d and v)
            small_head_count_solutions.append((d,v,0))
assert len(small_head_count_solutions)==5
visibility_queries=[];visible=[]
for foreign,context in CONTEXTS.items():
    for prefix,head in small_heads:
        for source_id in KEEP:
            for output in map(tuple,G[source_id]['outputs']):
                q=add(head,lit.rot(output,3));hit=q in context
                visibility_queries.append(dict(foreign=foreign,earlier_W_prefix=prefix,
                                               full_producer=G[source_id]['name'],output=output,
                                               physical_output=q,inside_future_context=hit))
                if hit:
                    assert prefix==''and source_id in(4,5,6,7,8,9)
                    assert output in((0,0),(0,1),(-1,2))
                    assert context[q][0]=='R'
                    visible.append(dict(foreign=foreign,full_producer=G[source_id]['name'],
                                        output=output,physical_output=q,first_future_read=context[q]))
assert len(visibility_queries)==1020 and len(visible)==45

# V-family r=(0,0) is still current at foreign age two. This small guard uses
# only preforeign full source clocks, never a returned consumer after foreign.
young_V_r_queries=[]
for source_id in(4,5,6):
    for age in range(3):
        h=(-age)%4
        for consumer_id in KEEP:
            for input_slot in map(tuple,G[consumer_id]['inputs']):
                z=lit.rot(input_slot,h);p=(-z[0],-z[1])
                key=(COMPACT[source_id],COMPACT[consumer_id],*p,h,0,0,age)
                reason='sector'if(sum(p)+h)%2 else'signed_COUNT5'
                if reason=='signed_COUNT5':assert key in COUNT
                young_V_r_queries.append(dict(source=G[source_id]['name'],source_r=(0,0),
                    consumer=G[consumer_id]['name'],input=input_slot,pose=(*p,h),
                    source_full_entry_C_age=age,reason=reason,count_key=key))
assert len(young_V_r_queries)==207
assert Counter(r['reason']for r in young_V_r_queries)=={'sector':120,'signed_COUNT5':87}

deps=[GP,WP,CP,CP.parent/'manifest.json',
      ROOT/'word_stabilization/check_foreign_return_interfaces.py',
      HERE/'returned_C_source_reduction_manifest.json',
      HERE/'first_foreign_all_source_join_manifest.json',
      ROOT/'core_periodicity_new/atomic_common_4C_frozen_20261023_1344/manifest.json',
      ROOT/'core_periodicity_new/U_left_star_permanence_frozen_20261023_1918/manifest.json']
out=dict(status='AUTHOR_FROZEN_ORDERED_W_ARCHIVE_MATCHING_PENDING_REVIEW',
    scope='Arbitrary finite W-run length in the three necessary actual old-C returned-raw-C residues, after the old containing source ends. Exact chosen-input/common-output submatching and all-length direct-visibility/first-D guard. All other ports retained. No second foreign, later return, full-ledger dominance or decreasing global resource claim.',
    full_packet_input_output_ports_and_physical_ownership=full_ports,
    all128_same_clock_produced_funding_queries=same_clock_queries,
    all24_strict_input_output_order_checks=ordering_rows,
    actual_future_complete_contexts=future_rows,
    exact_A_at_most3_head_prefixes=small_heads,
    all1020_output_visibility_queries=visibility_queries,
    all45_visible_first_base_output_roles=visible,
    all207_young_V_r_queries=young_V_r_queries,
    first_W_base_forced_to_be_D=True,
    all_W_full_outputs_miss_future_context_after_forced_first_D=True,
    protected_common_archive_geometry='head_i=(-A_i,1+B_i), common_i=(-A_i,3+B_i); A_i strictly increases,B_i never decreases.',
    matching_identity_claim='Every chosen input is an actual identity already current in the W-entry residual; pair it with that packet common fresh R8 output. Event-index bijection preserves strict x order and moves each matched site strictly NE. Common outputs remain original current identities through the first foreign+returned rawC+actualM11.',
    physical_order_caveat='R8 common production may precede the chosen input physical L read. Match uses the exact ordered fullpacket residual exchange, with marker-only physical read ownership retained; it does not assert that L happened first.',
    iteration_across_second_foreign_proved=False,
    dependencies={str(path.relative_to(ROOT)):hashlib.sha256(path.read_bytes()).hexdigest()for path in deps})
(HERE/'ordered_W_archive_matching.json').write_text(json.dumps(out,indent=2)+'\n')
print('128 sameclock exclusions,24 strict order checks,1020 exact visibility queries,207 young V-r exclusions.')
print('Unbounded ordered protected submatching; first W base D; entire W output support directly invisible to this future context.')
