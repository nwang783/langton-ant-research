"""An unbounded actual-deletion boundary, not a finite-state frontier.

Every E external input avoids all recorded right-supported W deletion sites.
Physical color/core transit is not frozen and every actual birth is retained.
"""
from pathlib import Path
from collections import Counter
import hashlib
import importlib.util
import json
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location('lit',R/'word_stabilization/check_foreign_return_interfaces.py')
lit=importlib.util.module_from_spec(sp);sp.loader.exec_module(lit)
so=importlib.util.spec_from_file_location('owner',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py')
owner=importlib.util.module_from_spec(so);so.loader.exec_module(owner)
GP=R/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json'
G=json.loads(GP.read_text())['geometry'];KEEP=(0,1,4,5,6,7,8,9)
CP=R/'core_periodicity_new/chronology_dcuv/critical_ucc_count5/frozen_20261023_0813/01_closure.tsv'
COUNT={tuple(map(int,line.split()[:8]))for line in CP.read_text().splitlines()}

def add(p,q):return p[0]+q[0],p[1]+q[1]
ports=[];max_y=[];fresh=[];forbidden=[]
for sid in KEEP:
    g=G[sid];tr=lit.trace(g['word']);assert tr['feasible']
    ep=g['endpoint'];exitK={add(ep[:2],lit.rot(q,ep[2]))for q in lit.K}
    O={tuple(q)for q in g['outputs']}
    # Every export O is a genuine last-R site, including each own C tail.
    for q in O:
        assert tr['last'][q][0]=='R'
        fresh.append(dict(actual_fullproducer=g['name'],output=q,last_R_tick0=tr['last'][q][1]))
    actual=[(q,tick)for q,(turn,tick)in tr['last'].items()
            if turn=='L'and q[1]<=0 and q not in O and q not in exitK]
    expected={(-1,0):1,(-1,-1):2,(0,-1):3}
    if sid==1:expected.update({(0,0):12,(1,0):13})
    assert dict(actual)==expected
    for q,tick in sorted(actual):
        physical=lit.rot(q,3)
        assert physical[0]>=0 # on/right of its W producer head
        row=dict(actual_W_fullproducer=g['name'],deletion_cell_in_fullproducer_frame=q,
                 last_actual_L_tick0=tick,canonical_physical_owner=owner.describe(g['name'],tick),
                 absent_from_full_O=True,absent_from_FULL_exit_K=True,
                 W_physical_offset_from_producer_head=physical,
                 all_later_W_full_output_births_strictly_left=True)
        ports.append(row)
        for cid in(0,4,7):
            for inp in map(tuple,G[cid]['inputs']):
                z=lit.rot(inp,1)
                head=(physical[0]-z[0],physical[1]-z[1])
                # Relative to a valid W head the E heading differs by2.
                relN=(q[0]+inp[0],q[1]+inp[1])
                sector_active=sum(relN)%2==0
                forbidden.append(dict(W_fullproducer=g['name'],deleted_source_local_cell=q,
                    deleted_W_physical_offset=physical,E_plain_consumer=G[cid]['name'],
                    E_external_input=inp,forbidden_E_head_offset_from_W_head=head,
                    relative_heading_in_W_source_frame=2,sector_active=sector_active,
                    disposition='forbidden_actual_external_input'if sector_active else'already_sector_inactive'))
    ys=[q[1]for q in O]
    assert min(ys)>=0
    max_y.append(dict(actual_W_fullproducer=g['name'],all_full_output_local_y_nonnegative=True,
                      output_local_y_minimum=min(ys),
                      includes_all_actual_own_C_tail_outputs=True))
assert len(ports)==26 and len(fresh)==68 and len(forbidden)==208
assert Counter(q['sector_active']for q in forbidden)=={True:120,False:88}

# All later W packet heads move strictly left. The earlier full packet is
# plain: a positive C tail would already end the W stage.
steps=[]
for sid in(0,4,7):
    x,y=lit.rot(G[sid]['endpoint'][:2],3)
    assert x<0
    steps.append(dict(previous_plain_W_packet=G[sid]['name'],step=(x,y),strict_x_drop=-x))

# Reconstruct the ENTIRE signed young full-source input interface, including
# incomplete VCC/UCC cases. No source full age is changed to a birth clock.
young=[]
for age in(0,1):
    h=(-age)%4
    for sid in KEEP:
        for cid in KEEP:
            for out in map(tuple,G[sid]['outputs']):
                for inp in map(tuple,G[cid]['inputs']):
                    z=lit.rot(inp,h);p=(out[0]-z[0],out[1]-z[1])
                    key=(KEEP.index(sid),KEEP.index(cid),*p,h,*out,age)
                    reason='sector'if(sum(p)+h)%2 else None
                    full_Cs=G[sid]['name'].count('C')
                    if reason is None and full_Cs>age:reason='full_source_not_yet_completed'
                    if reason is None:
                        assert key in COUNT;reason='signed_COUNT5'
                    young.append(dict(source=G[sid]['name'],output=out,consumer=G[cid]['name'],
                        input=inp,full_source_entry_C_age=age,actual_source_C_tail_count=full_Cs,
                        exact_key=key,exclusion=reason))
assert len(young)==3128
# The signed existing interface gives the same semantic alternatives, though
# it records sector before or after completion in individual rows.
old=json.loads((H/'ordered_W_transport_bottleneck.json').read_text())
assert len(old['all3128_completed_source_young_input_queries'])==len(young)
assert all(q['reason']in('sector','signed_COUNT5','source_not_yet_full_complete')
    for q in old['all3128_completed_source_young_input_queries'])

deps=[GP,CP,CP.parent/'manifest.json',H/'ordered_W_transport_bottleneck_manifest.json',
      H/'ordered_W_portal_submatching_manifest.json',H/'ordered_W_marker_ownership_erratum_manifest.json',
      H/'first_returned_five_label_frontier_manifest.json',
      R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py']
out=dict(status='AUTHOR_FROZEN_ORDERED_W_DELETED_PORT_BOUNDARY_PENDING_REVIEW',
    scope='Exact C3 old-DC/C1 setting, arbitrary finite mixed W and S/E stages before the first foreign. Recorded actual W deletions cannot be any E external residual input. No physical WHITE permanence, core-influence elimination, firstforeign/returned extension, secondforeign iteration or decreasing resource is asserted.',
    all26_full_exit_right_supported_actual_deletion_ports=ports,
    all68_fresh_full_output_last_R_checks=fresh,
    all8_W_full_output_x_cone_certificates=max_y,
    all3_strict_later_W_head_x_steps=steps,
    all208_E_external_input_forbidden_head_roles=forbidden,
    sector_active_role_count=120,already_sector_inactive_role_count=88,
    all3128_reconstructed_young_completed_source_input_exclusions=young,
    current_identity_proof_cases=[
        'A pre-W or earlier-W identity is killed by the actual recorded L, so cannot be the later current input ID.',
        'The deleting full packet has no O or exit K at the recorded site.',
        'A later W full output is strictly left of the site, including all own C-tail output roles.',
        'Any core-to-residual export is in a genuine later full O, not an untracked exception.',
        'Only S/E source clocks2/3 remain; actual E consumer clock3 gives full-source age1/0, excluded when completed and impossible when not completed.'],
    ordered_representation='Retain every actual producer head and each of its three ports, plus the final DC two extra ports. List length is unbounded. No dormant port is dropped.',
    dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in deps})
(H/'W_deleted_port_boundary.json').write_text(json.dumps(out,indent=2)+'\n')
print('26 literal FULL-exit deletion roles,68 genuine last-R exports,208 E head roles,3128 young-source queries.')
print('Actual residual-input avoidance only; physical core/WHITE-guard effects and unbounded ports retained.')
