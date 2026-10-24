"""Current genuine U-star support, not an exterior-path assumption.

A connected current edge set attached to a known interior vertex cannot reach
or cross the loop's global support line while disjoint from that loop.
"""
from pathlib import Path
import hashlib
import importlib.util
import json
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location('lit',R/'word_stabilization/check_foreign_return_interfaces.py')
lit=importlib.util.module_from_spec(sp);sp.loader.exec_module(lit)
so=importlib.util.spec_from_file_location('owner',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py')
owner=importlib.util.module_from_spec(so);so.loader.exec_module(owner)
L=((0,0),(0,1),(1,0),(1,1));Z=((1,0),(1,1),(2,0),(2,1))
def add(p,q):return p[0]+q[0],p[1]+q[1]
def edge2(q):
    v=(1,1)if sum(q)%2==0 else(1,-1)
    return ((2*q[0]-v[0],2*q[1]-v[1]),(2*q[0]+v[0],2*q[1]+v[1]))
def connected(edges,start):
    seen={start}
    while True:
        old=set(seen)
        for a,b in edges:
            if a in seen or b in seen:seen|={a,b}
        if old==seen:break
    return all(a in seen and b in seen for a,b in edges)
def physical_context(foreign,pose):
    tr=lit.trace(owner.WORDS[foreign]+owner.WORDS['C']+lit.M);assert tr['feasible']
    return {add(pose[:2],lit.rot(q,pose[2]))for q in tr['first']}

rows=[];conditional=[]
for foreign,fp,bound in(('F',(3,-4,1),-7),('Q',(5,-4,1),-7),('B',(6,-3,1),-5)):
    for k in((1,2)if foreign in'FQ'else(1,)):
        P=(-5-k,-k);pose=(*P,1)
        star=[add(P,lit.rot(q,1))for q in L]
        edges=[edge2(q)for q in star]
        z=(2*P[0]-1,2*P[1]+1)
        assert connected(edges,z)
        support=min(q[1]for e in edges for q in e)
        assert support==-2*k-3
        assert not(set(star)&physical_context(foreign,fp))
        # All foreign / returned pieces have doubled x>=1. The current
        # permanent star is strictly left; only old ordinary disjointness
        # uses the genuine current-residual-edge barrier.
        assert max(q[0]for e in edges for q in e)<1
        row=dict(foreign=foreign,foreign_entry=fp,preceding_UC_D_power=k,
                 genuine_UC_entry_in_creating_D_frame=pose,
                 genuine_permanent_star_physical_cells=star,
                 exact_current_star_physical_edges_doubled=edges,
                 actual_U_entry_corrected_center_doubled=z,
                 connected_star_contains_known_inside_old_vertex=True,
                 foreign_and_returned_complete_context_miss_star=True,
                 star_minimum_doubled_y=support,whole_loop_minimum_doubled_y=bound)
        if support<=bound:
            row['disposition']='EXCLUDED_current_permanent_star_reaches_support_outside_strict_inside'
            rows.append(row)
        else:
            assert foreign in'FQ'and k==1
            cycle=[add(P,lit.rot(q,1))for q in Z]
            all_edges=edges+[edge2(q)for q in cycle]
            assert connected(all_edges,z)
            cycle_min=min(q[1]for e in all_edges for q in e)
            assert cycle_min==bound
            assert not(set(cycle)&physical_context(foreign,fp))
            breaker=add(P,lit.rot((3,-1),1));assert breaker==(-7,-4)
            dx=fp[0]-breaker[0];dy=fp[1]-breaker[1];assert dy==0
            row.update(intact_cycle_would_also_reach_support=True,
                actual_first_cycle_break_forced_before_foreign=True,
                exact_source_included_breaker_C_age=4,
                actual_breaker_entry=(*breaker,1),foreign_same_C_clock_as_breaker=True,
                full_breaker_must_be_plain_U=True,
                allowed_zero_C_E_run_D=0,allowed_zero_C_E_run_V=0,
                required_total_U_count_including_breaker_numerator=dx,
                required_total_U_count_denominator=4)
            if dx%4:
                assert foreign=='F'and dx==10
                row['disposition']='EXCLUDED_forced_breaker_same_y_gap10_not_multiple4'
                rows.append(row)
            else:
                assert foreign=='Q'and dx==12
                row.update(disposition='NECESSARY_ONLY_Q_rebirth_branch_OPEN',
                    forced_plain_U_run_including_breaker=3,
                    warning='The recycled q edge may touch its producing breaker chord at the loop support vertex. It cannot be treated as disjoint from the whole loop.')
                conditional.append(row)
assert len(rows)==4 and len(conditional)==1

# A suffix-only contradiction would be false: this actual prepared suffix
# has a consistent finite complete board, but no UC/DC ancestry is asserted.
suffix=owner.WORDS['U']*3+owner.WORDS['Q']+owner.WORDS['C']+lit.M
suf=lit.trace(suffix);assert suf['feasible']
seed=sorted(q for q,(turn,_)in suf['first'].items()if turn=='L')
B=set(seed);p=(0,0);h=0
for turn in suffix:
    assert(p in B)==(turn=='L');B.symmetric_difference_update({p})
    h=(h+(1 if turn=='R'else-1))%4;p=add(p,lit.DIRS[h])

family=json.loads((H/'Q_UC_D_empty_N_connector_family.json').read_text())
assert len(family['count_solutions'])==22 and len(family['rows'])==83
assert all(not q['result']['feasible']for q in family['rows'])
deps=[H/'DC_C1_prefix_height_horizon_manifest.json',
      H/'ordered_W_archive_matching_manifest.json',H/'ordered_W_marker_ownership_erratum_manifest.json',
      H/'ordered_W_U_role_label_erratum_manifest.json',
      H/'first_foreign_all_source_join_manifest.json',H/'foreign_kinked_barrier_manifest.json',
      R/'core_periodicity_new/U_left_star_permanence_frozen_20261023_1918/manifest.json',
      R/'core_periodicity_new/current_residual_barrier_frozen_20261023_1822/manifest.json',
      R/'core_periodicity_new/U_renewal_exact_clock_frozen_20261023_1902/manifest.json',
      R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py']
out=dict(status='AUTHOR_FROZEN_DC_C1_UC_CURRENT_SUPPORT_SEPARATOR_PENDING_REVIEW',
    scope='Actual C75/76/77 DC/C1 FIRST returned contact only. Finite connected CURRENT U star attached to known inside U-entry center excludes support-line-reaching UC parents. Q age4 renewal branch retained, with only empty-prebreaker-N subfamily exhausted.',
    four_excluded_UC_parent_interfaces=rows,
    one_open_Q_UC_D_actual_cycle_rebirth_interface=conditional,
    prepared_U3_Q_C_suffix_control=dict(tokens=['U','U','U','Q','C'],complete_finite_seed=seed,
        physical_read_count=len(suffix),full_read_consistency=True,
        scope='Suffix-only positive; no creating-UC/DC history or target contact is asserted.'),
    empty_prebreaker_N_family=dict(exact_count_solution_count=22,whole_word_count=83,
        all_words_immutable_conflict=True,
        restriction='No N-oriented ordinary atom between final E-to-N C and forced first breaker. Nonempty N stage remains OPEN.'),
    remaining_C_last_parent_interface_counts=dict(F=6,Q=7,B=4),
    no_path_to_infinity_assumed=True,
    dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in deps})
(H/'DC_C1_UC_support_separator.json').write_text(json.dumps(out,indent=2)+'\n')
print('Four finite UC-parent cuts from CURRENT support / forced-breaker gap; Q UC+D renewal retained.')
print('Prepared U3,Q,C suffix replays;83 empty-N connector words fail, without closing arbitrary N.')
