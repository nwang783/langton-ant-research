"""Exact old-C true-age2 SECOND-contact slice.

The selected C itself supplies the first counted C turn. Only W and S rails
remain before the foreign, so endpoint x bounds all W counts and S D/V,
and endpoint y then fixes S U. All orders and all seven real source roles
are retained. No raw-C prepared board is substituted for a genuine source.
"""
from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
from itertools import permutations
import importlib.util,json,hashlib
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location('lit',R/'word_stabilization/check_foreign_return_interfaces.py');l=importlib.util.module_from_spec(sp);sp.loader.exec_module(l)
sp=importlib.util.spec_from_file_location('own',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py');o=importlib.util.module_from_spec(sp);sp.loader.exec_module(o);W=o.WORDS

def add(p,q):return p[0]+q[0],p[1]+q[1]
def sub(p,q):return p[0]-q[0],p[1]-q[1]
def det(p,q):return p[0]*q[1]-p[1]*q[0]
def raw(t):return ''.join(W[a] for a in t)
def after(w,p=(0,0,0)):
 x,y,h=p
 for c in w:
  h=(h+(1 if c=='R'else-1))%4;dx,dy=l.DIRS[h];x+=dx;y+=dy
 return x,y,h

def z(p):return add((2*p[0],2*p[1]),l.rot((-1,-1),p[2]))
def chord(a,p):return z(p),z(after(W[a],p))
def hit(a,b,c,d):
 u,v,zz=sub(b,a),sub(d,c),sub(c,a);den=det(u,v)
 if den:
  s,t=Q(det(zz,v),den),Q(det(zz,u),den)
  return(s,t)if 0<=s<=1 and 0<=t<=1 else None
 if det(zz,u):return None
 k=0 if u[0] else 1
 lo,hi=sorted((Q(c[k]-a[k],u[k]),Q(d[k]-a[k],u[k])))
 return ('collinear',max(0,lo),min(1,hi))if max(0,lo)<=min(1,hi)else None

def perms(d,v,u):
 if not d+v+u:yield '';return
 if d:
  for q in perms(d-1,v,u):yield'D'+q
 if v:
  for q in perms(d,v-1,u):yield'V'+q
 if u:
  for q in perms(d,v,u-1):yield'U'+q

a,b=chord('C',(0,0,0));u=sub(b,a);geos=[];boxes=[];types=[];counts=[];words={};maxsize=0
for b1 in'DCVU':
 N=2+int(b1=='C');h=(2-N)%4
 for b2 in'DCVU':
  if b1=='C'and b2=='U':continue
  c,d=chord(b2,(0,0,h));v=sub(d,c);den=det(u,v)
  corners=[tuple(Q(a[k]+s*u[k]-c[k]-t*v[k],2)for k in(0,1))for s in(0,1)for t in(0,1)]
  bounds=[(min(q[k]for q in corners).__floor__(),max(q[k]for q in corners).__ceil__())for k in(0,1)]
  boxes.append(dict(first=b1,second=b2,exact_rational_corners=[[[q.numerator,q.denominator] for q in p] for p in corners],integer_bounds=bounds))
  for x in range(bounds[0][0],bounds[0][1]+1):
   for y in range(bounds[1][0],bounds[1][1]+1):
    if(x+y-N)%2:continue
    zz=sub(add(c,(2*x,2*y)),a)
    if den:
     s,t=Q(det(zz,v),den),Q(det(zz,u),den)
     if not(0<=s<1 and 0<t<=1):continue
    else:
     if det(zz,u):continue
     k=0 if u[0] else 1
     q,mul=Q(zz[k],u[k]),Q(v[k],u[k]);assert mul>0
     if q>=0:continue
     s,t=Q(0),-q/mul
     if not(0<t<=1):continue
    p2=(x,y,h);geos.append((b1,b2,p2,s,t))
    for A in'FQB':
     dp=after(W[A]+W[b1],(0,0,2));pa=(x-dp[0],y-dp[1],2)
     if pa[0]>-1:continue
     # Actual signed foreign+b1 prefix must have no earlier source contact.
     pfx=after(W['F'],pa);end=after(W[A],pa);verts=[z(pa),z(pfx)]
     if A!='F':verts.append(z(end))
     if any(hit(a,b,c0,d0)for c0,d0 in zip(verts,verts[1:])):continue
     if hit(a,b,*chord(b1,end)):continue
     tr=l.trace(W[A]+W[b1]+W[b2]+l.M)
     if not tr['feasible']:continue
     types.append((A,b1,b2,pa,p2))
     L=-1-pa[0]
     for dw in range(L+1):
      for vw in range((L-dw)//3+1):
       for uw in range((L-dw-3*vw)//4+1):
        xres=L-dw-3*vw-4*uw
        for ds in range(xres+1):
         vs=xres-ds
         yres=1+dw+vw-ds-3*vs-pa[1]
         if yres<0 or yres%4:continue
         us=yres//4
         if ds+vs+us==0:continue
         counts.append((A,b1,b2,pa,dw,vw,uw,ds,vs,us));maxsize=max(maxsize,dw+vw+uw+ds+vs+us)
         for X in perms(dw,vw,uw):
          for Y in perms(ds,vs,us):
           if Y[-1]not in('VU'if A in'FQ'else'U'):continue
           T='C'+X+'C'+Y+A+b1+b2
           assert after(raw(T[:-3]))==pa
           if T in words:continue
           old=l.trace(raw(T[:-3]));tr=l.trace(raw(T)+l.M)
           cls='positive'if tr['feasible']else('old_conflict'if not old['feasible']else'whole_conflict')
           words[T]=dict(classification=cls,trace=tr,X=X,Y=Y,foreign_pose=pa,second_pose=p2)

# The omitted sixteenth angle interface is exactly raw C,U, already an
# immutable RAW contradiction. This is not an assertion that C cannot be
# the previous final atom of a genuine full producer in other contexts.
raw_cu = l.trace(W['C'] + W['U'] + l.M)
assert not raw_cu['feasible']
assert (raw_cu['conflict_read'], raw_cu['previous_read']) == (29, 1)
assert len(boxes) == 15 and len(geos) == 19 and len(types) == 57
assert len(counts) == 438 and maxsize == 9
assert len(words) == 1510
assert Counter(q['classification'] for q in words.values()) == {
    'old_conflict': 749, 'whole_conflict': 674, 'positive': 87}
positives = sorted(T for T, q in words.items() if q['classification'] == 'positive')


def physical_owner(tokens, tick):
    lo = 0
    for index, atom in enumerate(tokens):
        if tick < lo + len(W[atom]):
            return dict(actual_atom_index0=index, actual_atom=atom,
                        atom_start_tick0=lo, canonical=o.describe(atom, tick-lo))
        lo += len(W[atom])
    j = tick - lo
    assert 0 <= j < len(l.M)
    return dict(actual_atom='next actual word', next_word_tick0=j,
                next_word_read_number1=j+1, turn=l.M[j])


def immutable_record(tokens, tr):
    assert not tr['feasible']
    return dict(exact_conflict=tr,
                previous_actual_owner=physical_owner(tokens, tr['previous_read']),
                failing_actual_owner=physical_owner(tokens, tr['conflict_read']))


# A C source has exactly seven containing roles. Five literal prefixes
# suffice: the first C of a double tail uses V/U and additionally forces
# an empty W rail; the second C uses VC/UC. The full/source clocks are
# reconstructed rather than copied from a D base or reset at C2.
roles = []
for full in ('DC', 'VC', 'VCC', 'UC', 'UCC'):
    for selected in range(1, full.count('C') + 1):
        prefix = full[0] + 'C' * (selected - 1)
        j = selected - 1
        actual_entry = after(raw(prefix))
        roles.append(dict(
            containing_full_packet=full, selected_C_index1=selected,
            actual_literal_prefix_before_selected_C=prefix,
            actual_selected_C_pose_in_full_frame=actual_entry,
            selected_C_atomic_entry_clock=0,
            containing_full_entry_clock=-j,
            containing_full_entry_age_at_FOREIGN=2+j,
            containing_full_completion_clock=full.count('C')-j,
            mandatory_empty_W_rail=(full.count('C') == 2 and selected == 1),
            literal_prefix_query=prefix,
            frame_normalization='Translate actual selected C entry to zero and rotate its actual heading to N; literal feasibility is covariant.'))
assert len(roles) == 7
assert {r['literal_prefix_query'] for r in roles} == {'D','V','U','VC','UC'}
assert all(r['containing_full_completion_clock'] <= 2 for r in roles)

prefix_queries = []
for T in positives:
    for prefix in ('D', 'V', 'U', 'VC', 'UC'):
        trial = prefix + T
        tr = l.trace(raw(trial) + l.M)
        assert not tr['feasible']
        prefix_queries.append(dict(
            raw_C_body_tokens=list(T), literal_containing_prefix=prefix,
            trial_tokens=list(trial), **immutable_record(trial, tr)))
assert len(prefix_queries) == 435


def replay_complete_raw_C_board(tokens):
    body = raw(tokens)
    tr = l.trace(body + l.M)
    assert tr['feasible']
    seed = {p for p, (turn, tick) in tr['first'].items() if turn == 'L'}
    assert l.K <= seed
    # These are prepared RAW-C entries, not a completed full-eight source.
    black = set(seed)
    p, h = (0, 0), 0
    cut = None
    for tick, turn in enumerate(body + l.M):
        assert (p in black) == (turn == 'L')
        if turn == 'L':
            black.remove(p)
        else:
            black.add(p)
        h = (h + (1 if turn == 'R' else -1)) % 4
        p = add(p, l.DIRS[h])
        if tick + 1 == len(body):
            cut = dict(pose=(*p,h), complete_BLACK=sorted(black), mass=len(black))
    return dict(
        tokens=list(tokens), initial_mass=len(seed), complete_initial_BLACK=sorted(seed),
        all_unlisted_initial_cells_WHITE=True,
        physical_reads=len(body)+len(l.M), RAW_exit=cut,
        actual_final_M11_exit=dict(pose=(*p,h), complete_BLACK=sorted(black), mass=len(black)),
        prepared_RAW_C_entry_only=True,
        no_genuine_containing_full_source_or_U_entry_ancestry=True)


# All 87 prepared controls are actual complete finite-board histories.
# None is a genuine C source in one of the seven containing roles: the
# exhaustive literal-prefix table rejects every necessary source prefix.
controls = [replay_complete_raw_C_board(T) for T in positives]
word_records = []
for T, record in sorted(words.items()):
    tr = record['trace']
    row = dict(tokens=list(T), old_W_run=list(record['X']), old_S_run=list(record['Y']),
               foreign_pose=record['foreign_pose'], second_pose=record['second_pose'],
               classification=record['classification'])
    if not tr['feasible']:
        row.update(immutable_record(T, tr))
    word_records.append(row)

paths = [
    R/'second_ordinary_after_first_foreign_2026-10-24/small_second_ordinary_geometry_manifest.json',
    R/'audits/check_second_ordinary_small_interface_independent.json',
    R/'seven_word_spatial_return_2026-10-23/first_foreign_first_returned_atom_simplicity_manifest.json',
    R/'audits/check_first_foreign_returned_simplicity_independent.json',
    R/'seven_word_spatial_return_2026-10-23/complete8_foreign_adjacency_manifest.json',
    R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py']
assert all(p.exists() for p in paths)
out = dict(
    status='AUTHOR_FROZEN_OLD_C_AGE2_SECOND_CONTACT_PENDING_REVIEW',
    scope='Only outgoing genuine old C inside a real containing full-eight packet, atomic source-C-entry to FIRSTforeign age2, chronological FIRST new SECOND ordinary RAW contact and actual final M11. No other source/age or second simplicity.',
    raw_C_U_sixteenth_interface_immutable_conflict=raw_cu,
    all15_exact_remaining_contact_parallelograms=boxes,
    all19_outgoing_owned_b1_typed_contact_poses=[
        dict(first=b1,second=b2,second_pose=p2,old_s=[s.numerator,s.denominator],new_t=[t.numerator,t.denominator])
        for b1,b2,p2,s,t in geos],
    all57_local_feasible_source_clear_FOREIGN_alignments=[
        dict(foreign=A,first=b1,second=b2,foreign_pose=pa,second_pose=p2)
        for A,b1,b2,pa,p2 in types],
    all438_exact_W_S_endpoint_count_tuples=[
        dict(foreign=A,first=b1,second=b2,foreign_pose=pa,
             W_counts=dict(D=dw,V=vw,U=uw),S_counts=dict(D=ds,V=vs,U=us))
        for A,b1,b2,pa,dw,vw,uw,ds,vs,us in counts],
    endpoint_identity='After selected C: (0,1,W). Then W rail X, one C, S rail Y: xA=-1-dW-3vW-4uW-dS-vS; yA=1+dW+vW-dS-3vS-4uS. Bound -1-xA fixes a finite budget for all W counts and S D/V; yA fixes S U. All orders retained; nonempty final S rail ends V/U for F/Q, U for B.',
    derived_maximum_total_intervening_rail_atoms=9,
    no_length_cutoff_was_assumed=True,
    all1510_distinct_all_order_body_words=word_records,
    exact_word_counts=dict(Counter(q['classification'] for q in words.values())),
    all87_actual_complete_prepared_RAW_C_controls=controls,
    all7_real_containing_source_roles=roles,
    all435_necessary_literal_containing_prefix_queries=prefix_queries,
    conclusion='Every possible age2 raw-C body is either immutable-inconsistent or one of 87 complete prepared RAW-C controls. Every one of those controls rejects each necessary genuine containing prefix. Hence no genuine old C at atomic preforeign age2 realizes the stipulated first SECOND-contact. No ancestry-depth search is used.',
    important_scope='Prepared RAW-C controls are not genuine full-eight C sources or U-entry counterexamples. No physical WHITE permanence or postforeign maturity is used; all reads are actual RAW or one actual final M11.',
    no_second_simplicity_or_arbitrary_tail_extension=True,
    dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths})
(H/'C_age2_first_contact.json').write_text(json.dumps(out,indent=2)+'\n')
print('15 exact boxes + raw-CU cut; 19 outgoing-owned poses, 57 locally feasible prefix-clear foreign alignments.')
print('Exact 438 endpoint count tuples give 1,510 all-order words: 1,423 immutable failures and 87 actual prepared RAW-C positives.')
print('All 435 necessary source-prefix queries fail. Seven genuine C1/C2 roles covered; no ancestry cutoff or postforeign maturity.')
