"""Bounded last N-run from actual first-contact Jordan enclosure.

Enclosing a finite prefix is NOT itself a contradiction. The valid consequence
is an explicit height bound, retaining arbitrary earlier history and W/S/E runs.
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
GP=R/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json'
G=json.loads(GP.read_text())['geometry']

def add(p,q):return p[0]+q[0],p[1]+q[1]
def det(p,q):return p[0]*q[1]-p[1]*q[0]
def z2(pose):
    q=lit.rot((-1,-1),pose[2]);return 2*pose[0]+q[0],2*pose[1]+q[1]
def pose_after(word,pose=(0,0,0)):
    p=pose[:2];h=pose[2]
    for c in word:
        h=(h+(1 if c=='R'else-1))%4;p=add(p,lit.DIRS[h])
    return (*p,h)
def predecessor_pose(full,k):
    end=G[full]['endpoint'];h=(-end[2])%4;q=lit.rot(end[:2],h)
    return (-k-q[0],-k-q[1],h)

# Creating D -> selected C1 -> return C, all in creating-D frame.
D0=(0,0,0);oldC=(1,1,0);returned=(1,0,3)
q=z2(oldC);out=z2(pose_after(owner.WORDS['C'],oldC));back=z2(D0)
assert (q,out,back)==((1,1),(3,3),(-1,-1))
r0=z2(returned);r1=z2(pose_after(owner.WORDS['C'],returned))
assert(r0,r1)==((3,-1),q)
outgoing=(out[0]-q[0],out[1]-q[1])
closing=(q[0]-r0[0],q[1]-r0[1]);earlier=(back[0]-q[0],back[1]-q[1])
assert outgoing==(2,2)and closing==(-2,2)and earlier==(-2,-2)
assert det(closing,earlier)==8 and det(outgoing,earlier)==0
assert sum(outgoing[i]*earlier[i]for i in (0,1))<0

# These are symbolic sign checks on every zero-C atomic step, not bounded runs.
stage=[]
for atom,idx in(('D',0),('V',4),('U',7)):
    ep=G[idx]['endpoint'];assert ep[2]==0
    W=lit.rot(ep[:2],3);S=lit.rot(ep[:2],2);E=lit.rot(ep[:2],1)
    assert W[1]>=0 and S[1]<=0 and E[1]<=0
    stage.append(dict(atom=atom,N_step=ep[:2],W_step=W,S_step=S,E_step=E))
assert pose_after(owner.WORDS['C'],oldC)==(1,2,3)
assert lit.rot((0,1),3)==(-1,0) # W -> S C changes no physical y.
assert lit.rot((0,1),2)==(0,-1) # S -> E C drops physical y by one.
assert {h:lit.rot((-1,-1),h)[1]for h in(1,2,3)}=={1:1,2:1,3:-1}

all_rows=[];targets=[];kept=[]
for foreign,fp,bound,kmax in(('F',(3,-4,1),-7,2),('Q',(5,-4,1),-7,2),('B',(6,-3,1),-5,1)):
    # Verify the TRUE F56 fine cut; it is not a new core or marker.
    prefix=pose_after(owner.WORDS['F'],fp)
    end=pose_after(owner.WORDS[foreign],fp)
    assert end==returned
    vertices=[z2(fp),z2(prefix)]
    if foreign!='F':vertices.append(z2(end))
    assert min(p[1]for p in vertices)==bound
    assert 2*fp[1]+1==bound
    assert min(1,3,2*fp[1]+1,-1)==bound
    # Previous N-run start has z2_y=-1-2*m, strictly larger than bound.
    exact=[m for m in range(10)if -1-2*m>bound]
    assert exact==list(range(kmax+1))
    count_solutions=[]
    for d in range(kmax+1):
        for v in range(kmax//3+1):
            for u in range(kmax//4+1):
                if d+3*v+4*u<=kmax:
                    assert v==u==0
                    count_solutions.append(dict(D=d,V=v,U=u))
    assert count_solutions==[dict(D=k,V=0,U=0)for k in range(kmax+1)]
    targets.append(dict(foreign=foreign,foreign_entry_in_creating_D_frame=fp,
        true_foreign_piece_vertices_doubled=vertices,returned_C=returned,
        loop_exact_minimum_doubled_y=bound,
        stage_lower_bounds_doubled_y=dict(old_C=1,W=3,S=2*fp[1]+3,E=bound,returned_C=-1),
        arbitrary_W_S_E_stage_lengths_retained=True,
        preceding_N_run_vertical_weight_maximum=kmax,
        exact_preceding_N_run_count_solutions=count_solutions,
        initial_factor_N_epoch_impossible='Creating U vertical displacement is at least4, giving an earlier z2_y<=-9 below the loop.'))
    for full in(1,5,8,6,9):
        for k in range(kmax+1):
            pp=predecessor_pose(full,k)
            after=pose_after(G[full]['word'],pp)
            assert after==(-k,-k,0)
            assert pose_after(owner.WORDS['D']*k,after)==D0
            tokens=[G[full]['name']]+['D']*k+['DC']
            tr=lit.trace(G[full]['word']+owner.WORDS['D']*k+G[1]['word']+lit.M)
            row=dict(foreign=foreign,last_positive_C_fullpacket=G[full]['name'],
                actual_last_C_index=2 if full in(6,9)else 1,
                intervening_plain_D_count=k,actual_predecessor_packet_entry_in_selected_D_frame=pp,
                necessary_whole_prefix_tokens=tokens,
                previous_full_source_entry_to_foreign_C_age=3+(2 if full in(6,9)else 1))
            if full in(6,9):
                assert not tr['feasible']
                off=tr['conflict_read']-len(G[full]['word']);assert off==11
                # k=0: the selected DC owns its first C read. k>0: the
                # first plain D's following actual word supplies that read.
                target='DC'if k==0 else'D'
                row.update(disposition='literal_double_tail_then_D_family_conflict',
                    immutable_conflict=tr,canonical_owner=owner.describe(target,off))
            else:
                assert tr['feasible']
                if full==8 and k==0:
                    row.update(disposition='signed_immediate_UC_bud_before_WHITE_guard',
                        dependency='D_family_immediate_UC_bud_guard_manifest.json')
                else:
                    row.update(disposition='NECESSARY_ONLY_OPEN',
                        predecessor_prefix_literal_feasible=True)
                    kept.append(row)
            all_rows.append(row)
assert len(all_rows)==40 and len(kept)==21
assert {f:sum(q['foreign']==f for q in kept)for f in'FQB'}=={'F':8,'Q':8,'B':5}

deps=[GP,H/'first_returned_five_label_frontier_manifest.json',
      H/'first_foreign_all_source_join_manifest.json',H/'first_returned_atom_contact_manifest.json',
      H/'foreign_kinked_barrier_manifest.json',H/'complete8_foreign_adjacency_manifest.json',
      H/'D_family_immediate_UC_bud_guard_manifest.json',
      R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py']
out=dict(status='AUTHOR_FROZEN_DC_C1_PREFIX_HEIGHT_HORIZON_PENDING_REVIEW',
    scope='Only the actual first returned raw-C contact at old C1 of a completed DC source, after exactly one first foreign. Jordan enclosure yields a finite last-N-run/last-C-packet reduction. No generic exterior witness, arbitrary earlier-history bound, returned simplicity or secondforeign extension.',
    reflex_vertex_doubled=q,old_C_outgoing_vector=outgoing,closing_returned_C_vector=closing,
    earlier_creating_D_backward_ray=earlier,open_turn_quarters=5,closing_turn_quarters=-1,
    Jordan_turn_quarters=4,earlier_prefix_strictly_in_bounded_component=True,
    all9_symbolic_zero_C_stage_step_signs=stage,
    three_actual_loop_height_and_last_N_run_certificates=targets,
    all40_complete_last_C_parent_and_short_D_run_rows=all_rows,
    all21_remaining_necessary_last_C_parent_rows=kept,
    remaining_counts_by_foreign={'F':8,'Q':8,'B':5},
    no_generic_exterior_contradiction_claimed=True,
    dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in deps})
(H/'DC_C1_prefix_height_horizon.json').write_text(json.dumps(out,indent=2)+'\n')
print('Three exact loop minima -7/-7/-5; preceding N-run D-only length<=2/2/1.')
print('40 last-C parent rows ->16 literal double-tail cuts,3 signed UC cuts,21 necessary open rows.')
