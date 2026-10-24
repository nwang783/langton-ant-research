"""Weakened ordered W portal submatching, retaining arbitrary post-C2 S runs.

The rejected at-most-one seal is not a dependency. Its two genuine plain-source
countercontrols are deliberately retained among the four necessary port cases.
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
G=json.loads(GP.read_text())['geometry'];KEEP=(0,1,4,5,6,7,8,9)
COMPACT={a:i for i,a in enumerate(KEEP)}
COUNT={tuple(map(int,line.split()[:8]))for line in CP.read_text().splitlines()}
WORDS={a:r['word']for a,r in zip('DCVUFQB',json.loads(WP.read_text())['macro_words'])}
PORTALS={4:(0,1),6:(0,1),7:(-1,2),9:(-1,2)}
def add(p,q):return p[0]+q[0],p[1]+q[1]

queries=[];potential=[]
for source in KEEP:
    for output in map(tuple,G[source]['outputs']):
        for consumer in(0,4,7):
            for slot in map(tuple,G[consumer]['inputs']):
                z=lit.rot(slot,2);p=(output[0]-z[0],output[1]-z[1])
                key=(COMPACT[source],COMPACT[consumer],*p,2,*output,2)
                row=dict(source=G[source]['name'],output=output,consumer=G[consumer]['name'],
                    actual_input=slot,pose=(*p,2),full_source_entry_C_age=2,count_key=key)
                if(sum(p)+2)%2:row['reason']='sector'
                elif key in COUNT:row['reason']='signed_COUNT5'
                elif consumer==4 and slot==(0,3):
                    assert source in PORTALS and output==PORTALS[source]
                    row['reason']='necessary_portal_transfer_POST_C2_S_RUN_RETAINED'
                    row['plain_source_intermediate_N_W_S_runs_not_classified']=source in(4,7)
                    row['boundary_source_must_be_last_W_and_consumer_first_E']=source in(6,9)
                    potential.append(row)
                else:
                    assert source in(6,9)
                    exitp=tuple(G[source]['endpoint'][:2]);assert G[source]['endpoint'][2]==2
                    delta=(p[0]-exitp[0],p[1]-exitp[1]);row['after_full_completion_S_displacement']=delta
                    if delta[0]>0 or delta[1]>0:
                        row['reason']='completed_double_tail_zero_C_S_endpoint_cone'
                    elif consumer==0:
                        assert delta==(0,-2)
                        row['reason']='completed_double_tail_unchanged_x_U_step4_cannot_drop_y2'
                    else:
                        assert consumer==7 and delta in((0,0),(-1,-1))
                        seq=[source]+([]if delta==(0,0)else[0])+[consumer]
                        tr=lit.trace(''.join(G[a]['word']for a in seq)+lit.M)
                        assert not tr['feasible']and tr['conflict_read']<sum(len(G[a]['word'])for a in seq)
                        row['reason']='immutable_RAW_conflict_in_unique_completed_source_S_word'
                        row['unique_word']=[G[a]['name']for a in seq];row['literal_conflict']=tr
                queries.append(row)
assert len(queries)==544 and len(potential)==4
assert Counter(q['reason']for q in queries)=={'sector':264,'signed_COUNT5':266,
    'necessary_portal_transfer_POST_C2_S_RUN_RETAINED':4,
    'completed_double_tail_zero_C_S_endpoint_cone':4,
    'completed_double_tail_unchanged_x_U_step4_cannot_drop_y2':2,
    'immutable_RAW_conflict_in_unique_completed_source_S_word':4}

# At head(-A,1+B), portal sites are V:(-A-1,1+B), U:(-A-2,B).
# Any transfer into E V(0,3) has consumer head portal-(3,0).
portal_geometry=[]
for source,portal in PORTALS.items():
    r=lit.rot(portal,3);offset=(r[0]-3,1+r[1])
    assert offset==((-4,1)if source in(4,6)else(-5,0))
    portal_geometry.append(dict(source=G[source]['name'],actual_output=portal,
        W_head_formula='(-A,1+B)',portal_offset_at_W=r,
        E_V_head_formula='(-A-4,1+B)'if source in(4,6)else'(-A-5,B)',
        actual_E_V_input=(0,3),actual_E_V_first_physical_read=('L',19),
        physical_owner='next_actual_word_RAW_phase2'))

# Adjacent potential portal sources have only d>=0 plain D bases between them.
# The previous source is plain V/U; a nonplain source ends W.
order=[]
for previous in(4,7):
    prev=PORTALS[previous];Astep,Bstep=(3,1)if previous==4 else(4,0)
    kp,tp=(1,1)if previous==4 else(2,0)
    for following in(4,7):
        kn,tn=(1,1)if following==4 else(2,0)
        xdecrease=Astep+kn-kp;yincrease=Bstep+tn-tp
        assert xdecrease>=3 and yincrease>=0
        order.append(dict(previous_source_base=G[previous]['name'],following_source_base=G[following]['name'],
            intervening_plain_D_count='d>=0',portal_x_decrease_constant=xdecrease,
            portal_x_decrease_d_coefficient=1,portal_y_increase_constant=yincrease,
            portal_y_increase_d_coefficient=1))

contexts={}
for foreign,pose in(('F',(2,-5,1)),('Q',(4,-5,1)),('B',(5,-4,1))):
    tr=lit.trace(WORDS[foreign]+WORDS['C']+lit.M);assert tr['feasible']
    contexts[foreign]={add(pose[:2],lit.rot(q,pose[2])):v for q,v in tr['first'].items()}
    assert min(x for x,y in contexts[foreign])==-3
assert max(y for x,y in G[4]['outputs'])==2
# First-W-D gives A>=1 for every portal source. U visibility would need A<=0,
# impossible. V visibility needs A<=1, forcing earlier prefix exactly D,B=1.
# This applies to PLAIN V as well as VCC; no post-C2 S run is omitted.
visibility=[]
for foreign,context in contexts.items():
    for output in map(tuple,G[4]['outputs']):
        q=add((-5,2),lit.rot(output,1));assert q not in context
        visibility.append(dict(foreign=foreign,E_V_head=(-5,2),V_output=output,
            physical_output=q,in_actual_future_context=False,
            possible_W_source_at_A1_B1=['V','VCC']))
assert len(visibility)==18
protected_counts=[]
for source in KEEP:
    p=PORTALS.get(source);assert p is None or list(p)in G[source]['outputs']
    protected_counts.append(dict(full_source=G[source]['name'],all_full_outputs=len(G[source]['outputs']),
        possibly_spent_portal=p,nonportal_genuine_output_IDs_protected=len(G[source]['outputs'])-(p is not None)))

# Replay both genuine U-entry controls inside this checker as positive scope
# controls. They need not attain the three foreign endpoints, and are NEVER
# rejected by a missing-S plain-source argument.
positive_controls=[]
control_data=json.loads((HERE/'ordered_W_seal_withdrawal_controls.json').read_text())['controls']
BYNAME={G[a]['name']:a for a in KEEP}
for control in control_data:
    seq=[BYNAME[n]for n in control['full_packet_sequence']]
    word=''.join(G[a]['word']for a in seq)+lit.M
    assert lit.trace(word)['feasible']
    B={tuple(q)for q in control['complete_finite_seed']};p=(0,0);h=0;reads=[]
    tag=tuple(control['source_tag_physical_site'])
    for tick,c in enumerate(word):
        assert(p in B)==(c=='L')
        if p==tag:reads.append((c,tick))
        if c=='L':B.remove(p)
        else:B.add(p)
        h=(h+(1 if c=='R'else-1))%4;p=add(p,lit.DIRS[h])
    assert reads==[tuple(q)for q in control['source_tag_all_actual_reads']]
    assert control['source_kind']in('V','U')and control['source_to_consumer_C_age']==2
    positive_controls.append(control)
assert len(positive_controls)==2

deps=[GP,WP,CP,CP.parent/'manifest.json',ROOT/'word_stabilization/check_foreign_return_interfaces.py',
      HERE/'ordered_W_archive_matching_manifest.json',HERE/'ordered_W_transport_bottleneck_manifest.json',
      HERE/'ordered_W_U_role_label_erratum_manifest.json',HERE/'ordered_W_seal_withdrawal_controls_manifest.json']
out=dict(status='AUTHOR_FROZEN_WEAKENED_ORDERED_W_PORTAL_SUBMATCHING_PENDING_REVIEW',
    scope='Exactly three necessary old-C returned-RAW-C residues; arbitrary W length and arbitrary N/W/S runs for plain sources. Only first foreign and immediate returned RAW C+M11. No at-most-one-spending, second foreign, whole-color independence or finite boundary quotient.',
    all544_W_full_output_to_E_input_age2_queries=queries,
    all4_necessary_portal_transfer_cases=potential,
    exact_portal_and_consumer_head_geometry=portal_geometry,
    all4_symbolic_unbounded_D_gap_order_checks=order,
    all18_potential_pop_V_future_visibility_queries=visibility,
    protected_nonportal_counts_per_actual_fullproducer=protected_counts,
    conclusions=[
        'Each actual W producer has at most one potentially spent output portal: V/VCC A or U/UCC q. All other W full-output birth IDs remain current and unread through this first return.',
        'The actually used portals form an injective reverse-chronological partial matching to E V input(0,3). Skipped portals remain physically retained; strict LIFO completeness is not asserted.',
        'Each such E V also spends its distinct older W-entry input(1,2), as independently signed in ef645520.',
        'Every portal-consuming E V full-output site misses the actual combined future context. Residual I/O descendants do not reach a future-visible E output; RAW/core/WHITE-guard effects are not removed.'
    ],
    both_genuine_U_entry_positive_controls_physically_replayed=positive_controls,
    mandatory_core_ownership_caution='E V input(0,3) is physically read by NEXT word RAW phase2, after V RAW; active core carry and raw causal influence are not excluded.',
    dependencies={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()for p in deps})
(HERE/'ordered_W_portal_submatching.json').write_text(json.dumps(out,indent=2)+'\n')
print('544 exact E-input cases;4 portal cases retained;unbounded reverse-order submatching;18 pop-output checks miss.')
