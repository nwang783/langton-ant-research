"""Exact older-U zero-preforeign-C SECOND-contact slice.

Unbounded N runs are reduced by exact contact parallelogram endpoints, not an
arbitrary packet-depth cap. Four necessary words all have literal conflicts.
"""
from pathlib import Path
from fractions import Fraction as Q
from itertools import permutations
from collections import Counter
import hashlib
import importlib.util
import json
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location('lit',R/'word_stabilization/check_foreign_return_interfaces.py')
lit=importlib.util.module_from_spec(sp);sp.loader.exec_module(lit)
so=importlib.util.spec_from_file_location('owner',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py')
owner=importlib.util.module_from_spec(so);so.loader.exec_module(owner);W=owner.WORDS

def add(p,q):return p[0]+q[0],p[1]+q[1]
def sub(p,q):return p[0]-q[0],p[1]-q[1]
def det(p,q):return p[0]*q[1]-p[1]*q[0]
def pose_after(word,pose=(0,0,0)):
    p=pose[:2];h=pose[2]
    for c in word:
        h=(h+(1 if c=='R'else-1))%4;p=add(p,lit.DIRS[h])
    return(*p,h)
def z2(pose):return add((2*pose[0],2*pose[1]),lit.rot((-1,-1),pose[2]))
def chord(atom,pose):return z2(pose),z2(pose_after(W[atom],pose))
def hit(a,b,c,d):
    u,v,z=sub(b,a),sub(d,c),sub(c,a);den=det(u,v)
    assert den
    s,t=Q(det(z,v),den),Q(det(z,u),den)
    return(s,t)if 0<=s<=1 and 0<=t<=1 else None

def ceil(q):return -((-q.numerator)//q.denominator)
def floor(q):return q.numerator//q.denominator
u0,u1=chord('U',(0,0,0));assert(u0,u1)==((-1,-1),(-1,7))
oldvec=sub(u1,u0)
boxes=[];geometries=[];count_rows=[];words=[]
for A in'FQB':
    ep=pose_after(W[A]);b2pose=pose_after(W['C'],ep)
    for b2 in'DCV': # U is separately impossible by rawC->U in ANY history.
        c,d=chord(b2,b2pose);nv=sub(d,c)
        corners=[]
        for s in(0,1):
            for t in(0,1):
                corners.append(tuple(Q(u0[k]+s*oldvec[k]-c[k]-t*nv[k],2)for k in(0,1)))
        bounds=tuple((floor(min(p[k]for p in corners)),ceil(max(p[k]for p in corners)))for k in(0,1))
        boxes.append(dict(foreign=A,second=b2,exact_parallelogram_head_bounds=bounds))
        for x in range(bounds[0][0],bounds[0][1]+1):
            for y in range(bounds[1][0],bounds[1][1]+1):
                if x<0 or y<4 or(x+y)%2:continue
                cc=add(c,(2*x,2*y));dd=add(d,(2*x,2*y));h=hit(u0,u1,cc,dd)
                if h is None or not(0<=h[0]<1 and 0<h[1]<=1):continue
                # Actual source U RAW exits at(0,4,N). Every intervening old
                # packet is plain N D/V/U because n_beforeA=0.
                solutions=[]
                for v in range(x+1):
                    ds=x-v;res=y-4-ds-3*v
                    if res<0 or res%4:continue
                    us=res//4;solutions.append((ds,v,us))
                    counts=dict(D=ds,V=v,U=us)
                    all_orders=sorted(set(permutations('D'*ds+'V'*v+'U'*us)))
                    for oldrun in all_orders:
                        last='U'if not oldrun else oldrun[-1]
                        allowed=last in(('V','U')if A in'FQ'else('U',))
                        if not allowed:continue
                        assert pose_after(W['U']+''.join(W[a]for a in oldrun))==(x,y,0)
                        T=['U']+list(oldrun)+[A,'C',b2]
                        raw=''.join(W[a]for a in T);tr=lit.trace(raw+lit.M)
                        assert not tr['feasible']
                        is_R_conflict=tr['turn']=='R'
                        conflict_owner=owner.describe('V',12)if is_R_conflict else owner.describe('C',1)
                        previous_owner=owner.describe('U',21)if is_R_conflict else owner.describe('U',29)
                        assert tr['previous_read']==(21 if is_R_conflict else 29)
                        assert conflict_owner['turn']==tr['turn']
                        words.append(dict(tokens=T,foreign_entry=(x,y,0),
                            later_conflicting_actual_RAW='secondV'if is_R_conflict else'firstC',
                            later_physical_read_tick0=conflict_owner['owner_tick0'],
                            later_physical_read_number1=conflict_owner['owner_read_number1'],
                            previous_U_context_read_owner=previous_owner,

                            exact_old_N_count_solution=counts,
                            old_U_contact_parameters=dict(s=[h[0].numerator,h[0].denominator],t=[h[1].numerator,h[1].denominator]),
                            immutable_whole_word_conflict=tr))
                geometries.append(dict(foreign=A,first_returned='C',second_returned=b2,
                    foreign_entry=(x,y,0),old_U_contact_parameters=dict(s=[h[0].numerator,h[0].denominator],t=[h[1].numerator,h[1].denominator]),
                    all_nonnegative_endpoint_count_solutions=solutions))
                count_rows.extend(dict(foreign=A,second=b2,foreign_entry=(x,y,0),D=d,V=v,U=u)for d,v,u in solutions)
expected={('U','V','Q','C','V'),('U','D','V','Q','C','V'),('U','U','B','C','V'),('U','D','U','B','C','V')}
assert {tuple(q['tokens'])for q in words}==expected and len(words)==4
cu=lit.trace(W['C']+W['U']+lit.M);assert not cu['feasible']
angles=json.loads((H/'small_second_ordinary_geometry.json').read_text())['conditional217_old_source_angle_interfaces']
slice_angles=[q for q in angles if q['old_source']=='U'and q['actual_old_source_to_FOREIGN_C_age']==0]
assert slice_angles and all(q['first_ordinary']=='C'for q in slice_angles)
assert {q['second_ordinary']for q in slice_angles}==set('DCVU')

paths=[H/'small_second_ordinary_geometry_manifest.json',
       R/'audits/check_second_ordinary_small_interface_independent.json',
       R/'seven_word_spatial_return_2026-10-23/first_foreign_first_returned_atom_simplicity_manifest.json',
       R/'seven_word_spatial_return_2026-10-23/complete8_foreign_adjacency_manifest.json',
       R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py']
assert all(p.exists()for p in paths)
out=dict(status='AUTHOR_FROZEN_ZERO_PREFORIEGN_C_OLD_U_SECOND_CONTACT_SLICE_PENDING_REVIEW',
    scope='Chronological first new contact of SECOND ordinary RAW with a genuine preforeign old U BASE whose source-entry to foreign-entry C countn=0. Actual U/UC/UCC source completion forces plainU. Arbitrary earlier history and intervening N-run length allowed; endpoint equations force finite candidates. n>=1 and other old sources remainOPEN.',
    signed_angle_slice_forces_first_returned_raw_C=True,
    second_U_is_raw_C_U_literal_impossibility=cu,
    all9_exact_parallelogram_head_boxes=boxes,
    all_geometrically_possible_old_U_outgoing_contact_heads=geometries,
    all_nonnegative_N_endpoint_count_rows=count_rows,
    exactly4_actual_last_packet_compatible_whole_words=words,
    finite_bound_origin='Exact closed parallelogram of sourceU chord and translated b2E chord; not a guessed spatial box or packet cap.',
    no_postforeign_maturation_or_star_permanence_assumed=True,
    no_genuine_second_contact_attained=True,
    conclusion='No secondordinary first contact can have an oldU source with zero Cs before the firstforeign.',
    dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in paths})
(H/'zero_preforeign_C_old_U_slice.json').write_text(json.dumps(out,indent=2)+'\n')
print('9 exact contact boxes;unbounded N endpoints ->4 actual-last-packet whole words,all immutable conflicts.')
print('OldU n_beforeA=0 slice excluded;no postforeign age law,large catalogue or n>=1 extension.')
