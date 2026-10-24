"""Exact weighted index annotation of the signed actual portal submatching.

This is a finite-aperiodic matching annotation, not a new global clock.
"""
from pathlib import Path
from fractions import Fraction
import json
import hashlib
ROOT=Path('/workspace/shared/langton');HERE=Path(__file__).resolve().parent
G=json.loads((ROOT/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json').read_text())['geometry']
WEIGHT={'D':0,'V':1,'U':2}
# Actual zero-C steps at E and W, without assuming any periodic profile.
steps=[]
for a in(0,4,7):
    name=G[a]['name'];x,y,h=G[a]['endpoint'];assert h==0
    E=(y,-x);W=(-y,x);w=WEIGHT[name]
    assert sum(E)==2*w and sum(W)==-2*w
    assert E[0]>0 and W[0]<0
    steps.append(dict(actual_plain_base=name,E_step=E,W_step=W,weight=w,
                      E_x_plus_y_increment=2*w,W_x_plus_y_increment=-2*w))
rows=[]
for name,w,portaloffset in(('V',1,(-1,0)),('U',2,(-2,-1))):
    # W head(-A,1+B). E consumer head=portal-(3,0), then V's E step(3,-1).
    # Thus the consumer exit has normal B-A+portaloffset.x+portaloffset.y.
    c=portaloffset[0]+portaloffset[1]
    # T=(A-B)/2+w; require exit_normal=1-2T identically.
    assert c==1-2*w
    for foreign,entry in(('F',(2,-5)),('Q',(4,-5)),('B',(5,-4))):
        delta=Fraction(1-sum(entry),2);assert delta.denominator==1
        delta=int(delta)
        # Remaining E normal change=2Q, so Q=T-delta. With E total T_E
        # and consumer-through index J, Q=T_E-J and hence J+T=T_E+delta.
        last_requirement = 1 if foreign in ('F','Q') else 2
        minimum_T=delta+last_requirement
        assert minimum_T==({'F':3,'Q':2,'B':2}[foreign])
        rows.append(dict(W_source_base=name,source_base_weight=w,
            W_portal_offset=portaloffset,portal_consumer='E V input(0,3)',
            source_index_formula='T=(A-B)/2+source_base_weight',
            consumer_V_exit_normal_formula='x+y=1-2T',foreign=foreign,foreign_entry=entry,
            foreign_entry_normal=sum(entry),delta=delta,
            remaining_E_weight_formula=f'Q=T-{delta}',
            matched_index_formula=f'J+T=T_E+{delta}',
            actual_remaining_last_packet_requirement='V_or_U'if foreign in('F','Q')else'U',
            minimum_remaining_E_weight=last_requirement,minimum_source_weighted_index=minimum_T))
assert len(rows)==6
deps=[HERE/'ordered_W_portal_submatching_manifest.json',
      HERE/'complete8_foreign_adjacency_manifest.json',
      ROOT/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json']
out=dict(status='AUTHOR_FROZEN_ACTUAL_PORTAL_COMPLEMENTARY_INDEX_REFINEMENT_PENDING_REVIEW',
    scope='Same three first-foreign old-C returned-RAW-C residues and actual portal IDs as signed23f62a2c. Arbitrary W/S/E lengths; source N/W/S runs retained. Annotation of actual partial matching, not a new global positive clock.',
    all3_actual_base_steps=steps,all6_portal_type_foreign_index_identities=rows,
    definitions=dict(T='Cumulative W base weight through this actual portal source; V=1,U=2,D=0.',
        J='Cumulative E base weight through its actual consuming plain V.',
        T_E='Total E base weight before the first foreign.',
        Q='Remaining E base weight strictly after the consuming V.'),
    extra_ownership_fact='Consuming V exits x<=-2, whereas foreign entry x>=2, so at least one E packet remains and next-word RAWphase2 retirement occurs before foreign.',
    consequences=['Every actual match has complementary indices J+T=T_E+delta_foreign, delta_F=2,delta_Q=1,delta_B=0.',
        'The earliest possible V portal at T=1 cannot be spent in any of the three residues.',
        'The earliest possible U portal at T=2 cannot be spent in the F residue; Q/B are not excluded.',
        'D gaps have zero weight and remain unbounded. Skipped or dormant boundary ports are not deleted.'],
    dependencies={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()for p in deps})
(HERE/'W_portal_complementary_indices.json').write_text(json.dumps(out,indent=2)+'\n')
print('Exact actual complementary indices: F+2,Q+1,B+0;minimum source T=3/2/2;D gaps unbounded.')
