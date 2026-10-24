"""Explicit returned-C corollaries of signed preforeign deleted-cell lemmas.

No first-contact conclusion is transferred between source atoms. Only the
source/target-specific rebirth obstruction and its premises are reused.
"""
from pathlib import Path
import json
import hashlib
import importlib.util
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location('lit',R/'word_stabilization/check_foreign_return_interfaces.py')
lit=importlib.util.module_from_spec(sp);sp.loader.exec_module(lit)
so=importlib.util.spec_from_file_location('owner',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py')
owner=importlib.util.module_from_spec(so);so.loader.exec_module(owner)
GP=R/'core_periodicity_new/chronology_dcuv/literal_residual_geometry.json'
G=json.loads(GP.read_text())['geometry'];W=owner.WORDS
VP=R/'returned_V_source_residual_guards_2026-10-23/V_residual_guards.json'
UP=R/'returned_U_source_deleted_guard_2026-10-23/returned_U_deleted_guard.json'
V=json.loads(VP.read_text());U=json.loads(UP.read_text())
K=lit.K
def add(p,q):return p[0]+q[0],p[1]+q[1]
def sub(p,q):return p[0]-q[0],p[1]-q[1]

def all_E_endpoint_counts(endpoint,target,foreign):
    dx=target[0]-endpoint[0];down=endpoint[1]-target[1];rows=[]
    allowed=('V','U')if foreign in('F','Q')else('U',)
    for v in range(max(0,down+1)):
        d=down-v;fouru=dx-d-3*v
        if fouru<0 or fouru%4:continue
        u=fouru//4
        last=[a for a,n in(('D',d),('V',v),('U',u))if n and a in allowed]
        assert not last
        rows.append(dict(D=d,V=v,U=u,allowed_last_packets=last))
    return rows

rows=[]
for source,base,guard,oldCpose,foreigns in((
    5,4,(1,1),(1,3),('F','Q','B')),
    (8,7,(0,2),(0,4),('Q','B'))):
    base_trace=lit.trace(G[base]['word']);full_trace=lit.trace(G[source]['word'])
    assert base_trace['pose']==(*oldCpose,0)
    assert base_trace['last'][guard][0]=='L'
    assert full_trace['last'][guard]==base_trace['last'][guard]
    assert list(guard)not in G[source]['outputs']
    ep=G[source]['endpoint'];exitK={add(ep[:2],lit.rot(q,ep[2]))for q in K}
    assert guard not in exitK
    for foreign,old_relative in(('F',(2,-5)),('Q',(4,-5)),('B',(5,-4))):
        if foreign not in foreigns:continue
        entry=add(oldCpose,old_relative);pose=(*entry,1)
        actual_return=add(oldCpose,(0,-1))
        end=lit.trace(W[foreign])['pose'];assert add(entry,lit.rot(end[:2],1))==actual_return
        assert(end[2]+1)%4==3
        raw=lit.trace(W[foreign]);combined=lit.trace(W[foreign]+W['C']+lit.M)
        assert raw['feasible']and combined['feasible']
        local=lit.rot(sub(guard,entry),-1)
        assert local not in raw['first']and local not in K
        assert combined['first'][local]==('L',len(W[foreign])+1)
        canonical=owner.describe(foreign,len(W[foreign])+1)
        assert canonical['owner_tick0']==1 and canonical['owner_read_number1']==2
        if source==5:
            witnesses=[q for q in V['all18_residual_rows']if q['exclusion']=='source_deleted_11_has_no_possible_preforeign_rebirth'and q['foreign']==foreign and q['foreign_pose']==list(pose)]
            assert witnesses
            witness=witnesses[0]
            obs=[q for q in V['twelve_deleted_guard_endpoint_obligations']if q['case']==witness['case']]
            assert len(obs)==2
            origins=[tuple(q['endpoint'])for q in obs]
            signed_case=witness['case'];lemma='0135df7f source-deleted V(1,1) preforeign rebirth obstruction'
        else:
            witnesses=[q for q in U['seven_existing_U_source_contact_rows']if q['foreign']==foreign and q['foreign_pose']==list(pose)]
            assert witnesses
            witness=witnesses[0]
            obs=[q for q in U['twenty_one_unbounded_E_endpoint_obligations']if q['catalogue_case']==witness['catalogue_case']]
            assert len(obs)==3
            origins=[tuple(q['origin_endpoint'])for q in obs]
            signed_case=witness['catalogue_case'];lemma='992a5459 source-deleted U(0,2) preforeign rebirth obstruction'
        endpoints=[dict(origin_endpoint=q,target=entry,all_nonnegative_E_counts=all_E_endpoint_counts(q,entry,foreign))for q in origins]
        rows.append(dict(old_actual_fullsource=G[source]['name'],old_C_index=1,
            old_C_entry_in_creating_base_frame=(*oldCpose,0),foreign_entry_in_old_C_frame=(*old_relative,1),
            foreign=foreign,foreign_entry_in_creating_base_frame=pose,
            returned_RAW_C_entry_in_creating_base_frame=(*actual_return,3),
            genuine_source_deleted_guard=guard,source_last_deletion=base_trace['last'][guard],
            source_own_C_tail_preserves_deletion=True,foreign_RAW_never_reads_guard=True,
            guard_outside_foreign_entry_K=True,combined_first_L=combined['first'][local],
            canonical_physical_owner=canonical,signed_rebirth_lemma=lemma,signed_witness_case=signed_case,
            independently_rechecked_final_origin_endpoint_obligations=endpoints,
            first_contact_with_creating_base_NOT_assumed=True))
assert len(rows)==5

deps=[GP,VP,UP,R/'returned_V_source_residual_guards_2026-10-23/manifest.json',
      R/'returned_U_source_deleted_guard_2026-10-23/manifest.json',
      R/'audits/check_returned_V_residual_guards_independent.json',
      R/'audits/check_returned_U_deleted_guard_independent.json',
      H/'returned_C_source_reduction_manifest.json',H/'returned_C_UC_F_core_guard_manifest.json',
      H/'returned_C_double_tail_source_manifest.json',H/'earliest_W_portal_ancestry_guard_manifest.json',
      H/'earliest_W_D_family_clarification_manifest.json',
      R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py']
assert all(p.exists()for p in deps)
out=dict(status='AUTHOR_FROZEN_EXPLICIT_RETURNED_C_DELETED_GUARD_COROLLARIES_PENDING_REVIEW',
    scope='Three actual C3 residues, old C1 in VC or UC, actual U-entry old-eight history before first foreign. Reuses target-specific source-deletion rebirth lemmas, NOT their source-firstcontact conclusions. No returned simplicity or secondforeign import.',
    all5_explicit_literal_and_prebirth_premise_lifts=rows,
    conclusions=['Old C1 of VC is excluded for F,Q,B by signed V-deleted(1,1) rebirth obstruction.',
        'Old C1 of UC is excluded for Q,B by signed U-deleted(0,2) rebirth obstruction; F was separately excluded by original-star/entrycore guard.',
        'Combined with signed double-tail source-role exclusions, only old C1 of DC remains for the three coarse C labels.'],
    dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in deps})
(H/'returned_C_VC_UC_deleted_guard_lift.json').write_text(json.dumps(out,indent=2)+'\n')
print('Five exact returned-C premise lifts;all actual owner reads next tick1/read2;old VC/UC roles excluded conditionally on signed rebirth lemmas.')
