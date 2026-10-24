"""Small local SECOND ordinary interface; no large old-source catalogue.

Use signed first-ordinary simplicity only. No inherited residual maturity,
postforeign fullproducer reset or secondforeign assumption is made.
"""
from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
import hashlib
import importlib.util
import json
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location('lit',R/'word_stabilization/check_foreign_return_interfaces.py')
lit=importlib.util.module_from_spec(sp);sp.loader.exec_module(lit)
so=importlib.util.spec_from_file_location('owner',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py')
owner=importlib.util.module_from_spec(so);so.loader.exec_module(owner)
W=owner.WORDS
assert all((W[b]+lit.M)[:len(lit.M)]==lit.M for b in'DCVU')

def add(p,q):return p[0]+q[0],p[1]+q[1]
def sub(p,q):return p[0]-q[0],p[1]-q[1]
def det(p,q):return p[0]*q[1]-p[1]*q[0]
def pose_after(word,pose=(0,0,0)):
    p=pose[:2];h=pose[2]
    for turn in word:
        h=(h+(1 if turn=='R'else-1))%4;p=add(p,lit.DIRS[h])
    return(*p,h)
def z2(pose):return add((2*pose[0],2*pose[1]),lit.rot((-1,-1),pose[2]))
def chord(atom,pose):return z2(pose),z2(pose_after(W[atom],pose))
def hit(a,b,c,d):
    u,v,z=sub(b,a),sub(d,c),sub(c,a);den=det(u,v)
    if den:
        s,t=Q(det(z,v),den),Q(det(z,u),den)
        return dict(kind='point',s=s,t=t)if 0<=s<=1 and 0<=t<=1 else None
    if det(z,u):return None
    k=0 if u[0] else 1
    x,y=sorted((Q(c[k]-a[k],u[k]),Q(d[k]-a[k],u[k])))
    lo,hi=max(Q(0),x),min(Q(1),y)
    return dict(kind='collinear',old_s_interval=(lo,hi))if lo<=hi else None

def foreign_pieces(a,pose):
    first=pose_after(W['F'],pose);end=pose_after(W[a],pose)
    vertices=[z2(pose),z2(first)]
    if a!='F':vertices.append(z2(end))
    return list(zip(vertices,vertices[1:])),end,vertices

triples=[]
for A in'FQB':
    pieces,ep,verts=foreign_pieces(A,(0,0,0))
    assert ep[2]==2
    assert min(p[1]for p in verts)==z2(ep)[1]
    for b1 in'DCVU':
        c1=chord(b1,ep);p2=pose_after(W[b1],ep)
        assert c1[1][1]<min(p[1]for p in verts)
        assert p2[2]==(1 if b1=='C' else 2)
        for b2 in'DCVU':
            c2=chord(b2,p2)
            assert c2[1][1]<=c2[0][1]
            assert max(c2[0][1],c2[1][1])<min(p[1]for p in verts)
            assert all(hit(*piece,*c2)is None for piece in pieces)
            adjacent=hit(*c1,*c2)
            assert adjacent==dict(kind='point',s=Q(1),t=Q(0))or adjacent==dict(kind='collinear',old_s_interval=(Q(1),Q(1)))
            literal=lit.trace(W[A]+W[b1]+W[b2]+lit.M)
            triples.append(dict(foreign=A,first_ordinary=b1,second_ordinary=b2,
                true_foreign_piece_vertices=verts,foreign_minimum_doubled_y=min(p[1]for p in verts),
                first_ordinary_pose=ep,second_ordinary_pose=p2,
                first_chord=c1,second_chord=c2,
                second_chord_strictly_below_foreign=True,
                second_meets_first_only_at_true_adjacency=True,
                local_whole_color_context_feasible=literal['feasible']))
assert len(triples)==48

# Independently record16 actual ordinary joins, not three copies per foreign.
adj=[]
for b1 in'DCVU':
    p=(0,0,2);c1=chord(b1,p);p2=pose_after(W[b1],p)
    for b2 in'DCVU':
        c2=chord(b2,p2);q=hit(*c1,*c2)
        assert q==dict(kind='point',s=Q(1),t=Q(0))or q==dict(kind='collinear',old_s_interval=(Q(1),Q(1)))
        adj.append(dict(first=b1,second=b2,first_chord=c1,second_chord=c2,adjacent_only=True))
assert len(adj)==16

# Last old full packet before firstforeign is plainV/U. These96 cases isolate
# only that IMMEDIATE old base, not all earlier old sources of the same type.
last=[];contacts=[]
for old in'VU':
    oc=chord(old,(0,0,0));fp=pose_after(W[old])
    for A in'FQB':
        pieces,ep,verts=foreign_pieces(A,fp)
        for b1 in'DCVU':
            p2=pose_after(W[b1],ep)
            for b2 in'DCVU':
                new=chord(b2,p2);h=hit(*oc,*new)
                relevant=h is not None and h['kind']=='point'and 0<=h['s']<1 and 0<h['t']<=1
                raw=lit.trace(W[old]+W[A]+W[b1]+W[b2]+lit.M)
                row=dict(immediate_old_plain_base=old,foreign=A,first_ordinary=b1,second_ordinary=b2,
                    old_base_chord=oc,second_ordinary_chord=new,positive_old_base_contact=relevant,
                    whole_literal_context_feasible=raw['feasible'])
                if relevant:
                    assert not raw['feasible']
                    row.update(contact={k:([v.numerator,v.denominator]if isinstance(v,Q)else v)for k,v in h.items()},
                               immutable_whole_context_conflict=raw)
                    contacts.append(row)
                last.append(row)
assert len(last)==96
assert {(q['immediate_old_plain_base'],q['foreign'],q['first_ordinary'],q['second_ordinary'])for q in contacts}=={('V','F','C','V'),('V','F','C','U'),('U','F','C','U'),('U','Q','C','U')}
# Raw C->U is independently a repeated-L contradiction; VF-CV has its own
# actual older V-entry-core deletion that neither foreign nor firstC repairs.
cu=lit.trace(W['C']+W['U']+lit.M);assert not cu['feasible']
assert cu['conflict_read']==29 and cu['previous_read']==1
vfcv=lit.trace(W['V']+W['F']+W['C']+W['V']+lit.M)
assert not vfcv['feasible']and vfcv['conflict_read']==102 and vfcv['previous_read']==2
assert vfcv['cell']==[-1,-1]

# Conditional old-source first-contact angle clock. This is NOT a new
# position catalogue, and n is kept at the FOREIGN entry funding cut.
rank={'U':0,'V':1,'D':2,'C':2};angles=[]
for b1 in'DCVU':
    c=int(b1=='C')
    for old in'DCVU':
        for b2 in'DCVU':
            for N in range(5):
                n=N-c
                if n<0 or(old=='C'and n<1):continue
                if N==0 and rank[old]<=rank[b2]:continue
                if N==4 and rank[old]>=rank[b2]:continue
                angles.append(dict(old_source=old,first_ordinary=b1,second_ordinary=b2,
                    actual_old_source_to_FOREIGN_C_age=n,
                    first_ordinary_C_increment=c,total_ordinary_C_before_second=N,
                    effective_one_foreign_quarter_clock=N+2,
                    second_heading_relative_old_source=(2-N)%4,
                    foreign_heading_relative_old_source=(-n)%4))
assert Counter(q['first_ordinary']for q in angles)=={'D':56,'C':49,'V':56,'U':56}
assert len(angles)==217

paths=[R/'seven_word_spatial_return_2026-10-23/first_foreign_first_returned_atom_simplicity_manifest.json',
       R/'audits/check_first_foreign_returned_simplicity_independent.json',
       R/'seven_word_spatial_return_2026-10-23/first_returned_catalogue_parent_mapping_manifest.json',
       R/'audits/check_returned_catalogue_parent_mapping_independent.json',
       R/'seven_word_spatial_return_2026-10-23/complete8_foreign_adjacency_manifest.json',
       R/'seven_word_spatial_return_2026-10-23/foreign_kinked_barrier_manifest.json',
       R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py']
assert all(p.exists()for p in paths)
out=dict(status='AUTHOR_FROZEN_SMALL_SECOND_ORDINARY_GEOMETRY_PENDING_REVIEW',
    scope='SECOND immediately successive ordinary RAW after one firstforeign, conditional on signed firstordinary proxy simplicity and actual two-RAW+M11 context. Only local source elimination and angle interface; no inherited maturity or general secondatom simplicity.',
    all48_foreign_first_second_chord_clearance_rows=triples,
    all16_adjacent_ordinary_join_rows=adj,
    all96_immediate_old_V_U_base_local_rows=last,
    four_possible_immediate_old_base_contacts_all_literal_conflicting=contacts,
    raw_C_U_immutable_conflict=cu,old_V_F_C_V_immutable_conflict=vfcv,
    conditional217_old_source_angle_interfaces=angles,
    angle_counts_by_first_ordinary=dict(Counter(q['first_ordinary']for q in angles)),
    exact_remaining_contact_sources='Any genuine new secondatom contact must be with a PREforeign old ordinary source STRICTLY EARLIER than the immediate old plainV/U beforeA. It cannot be A pieces,b1,or that lastV/U base.',
    no_large_old_source_position_catalogue_constructed=True,
    no_actual_U_entry_second_contact_countercontrol_claimed=True,
    remaining_causal_gap='Foreign outputs, R55 active-core identities and b1 births/absorptions can alter older tags; retain them explicitly. Old source funding age atA is n,not N, and no old8 age law is assumed across A.',
    dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in paths})
(H/'small_second_ordinary_geometry.json').write_text(json.dumps(out,indent=2)+'\n')
print('48 secondchord/foreign clearances;16 adjacent joins;96 lastoldV/U contexts with4 geometries all literal conflicts.')
print('Conditional angle interface217=56+49+56+56;funding clockn atforeign kept separate fromN=n+C(b1).')
