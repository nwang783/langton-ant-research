"""All-length W full-output residual archive, across exactly the first return.

Residual I/O ancestry is distinguished from physical RAW/core influence.
The exceptional V(0,3) input is physically read by next-word RAW phase2.
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
def add(p,q):return p[0]+q[0],p[1]+q[1]

# A plain V/U source candidate into V(0,3) at age2 has exactly the net
# displacement of its own two immediate C tails. For either source, writing
# N counts d,v,u and W counts e,f,g gives d+3v+4u+e+f=0 and d+v=e+3f+4g.
# Nonnegativity forces all six counts zero. Thus the source would be VCC/UCC,
# not plain V/U, with no standalone C fullpacket introduced.
plain_source_equations=dict(
    variables=['N_D','N_V','N_U','W_D','W_V','W_U'],
    zero_y_equation_coefficients=[1,3,4,1,1,0],
    x_equation_left_coefficients=[1,1,0,0,0,0],
    x_equation_right_coefficients=[0,0,0,1,3,4],
    only_nonnegative_solution=[0,0,0,0,0,0],
    reason='Immediate C,C belongs to the actual containing full source; a plain source cannot be followed by standalone C packets.')
assert all(c>0 for c in plain_source_equations['zero_y_equation_coefficients'][:5])

all_queries=[];possible=[];raw_conflicts=[]
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
                elif source in(4,7):
                    assert consumer==4 and slot==(0,3)
                    assert(source,output,p)in((4,(0,1),(0,4)),(7,(-1,2),(-1,5)))
                    row['reason']='plain_source_would_have_to_be_own_double_tail'
                    row['all_length_endpoint_equations']=plain_source_equations
                else:
                    assert source in(6,9)
                    exitp=tuple(G[source]['endpoint'][:2]);assert G[source]['endpoint'][2]==2
                    delta=(p[0]-exitp[0],p[1]-exitp[1]);row['after_full_completion_S_displacement']=delta
                    if delta[0]>0 or delta[1]>0:
                        row['reason']='zero_C_S_endpoint_cone'
                    elif consumer==0:
                        assert delta==(0,-2)
                        row['reason']='unchanged_x_S_U_step4_cannot_drop_y2'
                    else:
                        assert delta in((0,0),(-1,-1))
                        middle=[]if delta==(0,0)else[0]
                        seq=[source]+middle+[consumer]
                        tr=lit.trace(''.join(G[a]['word']for a in seq)+lit.M)
                        row['unique_actual_full_packet_sequence']=[G[a]['name']for a in seq]
                        if tr['feasible']:
                            assert consumer==4 and slot==(0,3)and not middle
                            row['reason']='allowed_last_W_double_tail_to_immediate_first_E_V'
                            possible.append(row)
                        else:
                            assert consumer==7
                            row['reason']='immutable_RAW_conflict_in_unique_endpoint_word'
                            row['literal_conflict']=tr
                            assert tr['conflict_read']<sum(len(G[a]['word'])for a in seq)
                            raw_conflicts.append(row)
                all_queries.append(row)
assert len(all_queries)==544
assert Counter(r['reason']for r in all_queries)=={
    'sector':264,'signed_COUNT5':266,
    'plain_source_would_have_to_be_own_double_tail':2,
    'zero_C_S_endpoint_cone':4,'unchanged_x_S_U_step4_cannot_drop_y2':2,
    'immutable_RAW_conflict_in_unique_endpoint_word':4,
    'allowed_last_W_double_tail_to_immediate_first_E_V':2}

allowed_pairs=[]
for source,tag in((6,(0,1)),(9,(-1,2))):
    w=G[source]['word']+G[4]['word'];tr=lit.trace(w+lit.M);assert tr['feasible']
    assert lit.trace(G[4]['word']+lit.M)['first'][(0,3)]==('L',19)
    reads=[];p=(0,0);h=0
    for t,c in enumerate(w+lit.M):
        if p==tag:reads.append((c,t))
        h=(h+(1 if c=='R'else-1))%4;d=lit.DIRS[h];p=add(p,d)
    birth=lit.trace(G[source]['word'])['last'][tag]
    assert birth[0]=='R'
    first_after=next((c,t)for c,t in reads if t>=len(G[source]['word']))
    assert first_after==('L',len(G[source]['word'])+19)
    allowed_pairs.append(dict(source=G[source]['name'],source_tag=tag,full_packet_pair=[G[source]['name'],'V'],
        actual_minimal_pair_seed=[q for q,(c,t)in sorted(tr['first'].items())if c=='L'],
        source_tag_physical_reads=reads,source_tag_last_birth=birth,
        consuming_V_input=(0,3),V_context_read=('L',19),V_raw_length=len(G[4]['word']),
        physical_read_owner='next_actual_word_RAW_phase2',U_entry_attainment_claimed=False))

contexts={}
for foreign,pose in(('F',(2,-5,1)),('Q',(4,-5,1)),('B',(5,-4,1))):
    tr=lit.trace(WORDS[foreign]+WORDS['C']+lit.M);assert tr['feasible']
    contexts[foreign]={add(pose[:2],lit.rot(q,pose[2])):v for q,v in tr['first'].items()}
    assert min(x for x,y in contexts[foreign])==-3
assert max(y for x,y in G[4]['outputs'])==2
# Boundary VCC at W head(-A,1+B) exits at(-A-4,1+B,E), UCC at(-A-5,B,E).
# A future-visible output of the first E V requires respectively A<=1 or A<=0.
# First-W-D excludes A=0 for either boundary. A=1 forces prefix exactly D,
# B=1, boundary VCC and first-E-V head(-5,2). Its entire output misses.
first_E_V_visibility=[]
for foreign,context in contexts.items():
    for output in map(tuple,G[4]['outputs']):
        q=add((-5,2),lit.rot(output,1));assert q not in context
        first_E_V_visibility.append(dict(foreign=foreign,last_W_prefix='D',last_W_full_packet='VCC',
            last_W_head=(-1,2),first_E_V_head=(-5,2),V_output=output,physical_V_output=q,
            inside_actual_future_context=False))
assert len(first_E_V_visibility)==18

deps=[GP,WP,CP,CP.parent/'manifest.json',ROOT/'word_stabilization/check_foreign_return_interfaces.py',
      HERE/'ordered_W_archive_matching_manifest.json',HERE/'ordered_W_transport_bottleneck_manifest.json',
      HERE/'ordered_W_U_role_label_erratum_manifest.json']
out=dict(status='AUTHOR_FROZEN_ALL_LENGTH_W_FULL_OUTPUT_RESIDUAL_SEAL_PENDING_REVIEW',
    scope='Three necessary actual old-C returned-RAW-C residues, arbitrary W length, before and through exactly first complete foreign and immediate RAW C+actualM11. Residual I/O ancestry is not all physical RAW/core/color influence.',
    all544_W_output_to_plain_E_packet_input_age2_queries=all_queries,
    two_literal_possible_boundary_pairs_and_real_physical_ownership=allowed_pairs,
    all18_only_potential_first_E_V_visibility_queries=first_E_V_visibility,
    conclusions=[
        'The only possible W-full-output into E external-residual-input transfers are final W VCC original A or UCC recycled q into(0,3) of the immediately first E V.',
        'At most one W full-output identity is spent in all later preforeign fullpacket residual I/O. All other W full-output birth identities remain current through first foreign+returnedRAW_C+M11.',
        'Every W full-output site and every output site of that exceptional first E V misses the actual future combined context.',
        'The residual I/O graph has no W-output descendant at a future-visible E output; this is not a physical core-ancestry or functional-color independence theorem.'
    ],
    mandatory_ownership_caution='Exceptional plain V input(0,3) is marker-only, physical L at context tick19 owned by NEXT actual word RAW phase2. The active K can carry that identity until then. Do not infer all raw causal/color influence is absent.',
    second_foreign_iteration_proved=False,
    dependencies={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()for p in deps})
(HERE/'ordered_W_full_output_seal.json').write_text(json.dumps(out,indent=2)+'\n')
print('544 exact E-input queries:14 non-COUNT5 cases reduce to2 boundary->first-V transfers;18 visibility checks miss.')
