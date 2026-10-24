"""Old-C THIRD-source closure from existing reserves and finite endpoint budgets.

No longer closure or guessed history cap. Current-fact reuse is checked as an
exact subset of signed source queries at earlier full foreign deadlines.
"""
from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
import json,importlib.util,hashlib
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent
s=importlib.util.spec_from_file_location('l',R/'word_stabilization/check_foreign_return_interfaces.py');l=importlib.util.module_from_spec(s);s.loader.exec_module(l);s=importlib.util.spec_from_file_location('o',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py');o=importlib.util.module_from_spec(s);s.loader.exec_module(o);W=o.WORDS
J=json.load(open(R/'third_ordinary_local_interface_2026-10-24/third_local_interface.json'))
C=json.load(open(R/'second_old_C_age3_2026-10-24/C_age3_source_reserve.json'))

def add(p,q):return p[0]+q[0],p[1]+q[1]
def sub(p,q):return p[0]-q[0],p[1]-q[1]
def det(p,q):return p[0]*q[1]-p[1]*q[0]
def after(w,p=(0,0,0)):
 q,h=p[:2],p[2]
 for t in w:h=(h+(1 if t=='R'else-1))%4;q=add(q,l.DIRS[h])
 return *q,h

def raw(t):return ''.join(W[a]for a in t)
def z(p):return add((2*p[0],2*p[1]),l.rot((-1,-1),p[2]))
def chord(a,p):return z(p),z(after(W[a],p))
def hit(a,b,c,d):
 u,v,zz=sub(b,a),sub(d,c),sub(c,a);den=det(u,v)
 if den:
  s,t=Q(det(zz,v),den),Q(det(zz,u),den)
  return(s,t)if 0<=s<=1 and 0<=t<=1 else None
 if det(zz,u):return None
 k=0 if u[0] else 1;lo,hi=sorted((Q(c[k]-a[k],u[k]),Q(d[k]-a[k],u[k])))
 return('parallel',max(0,lo),min(1,hi))if max(0,lo)<=min(1,hi)else None

angles=[r for r in J['all831_conditional_preFOREIGN_old_source_angle_interfaces']if r['old_source']=='C'];rows=[];geos=[];boxes=[]
a,b=chord('C',(0,0,0));u=sub(b,a)
for ai,angle in enumerate(angles):
 n=angle['true_old_source_ENTRY_to_FOREIGN_ENTRY_C_age'];N=angle['total_ordinary_C_before_third'];b1,b2,b3=(angle[k]for k in['first','second','third']);hh=angle['third_heading_relative_old'];c,d=chord(b3,(0,0,hh));v=sub(d,c);den=det(u,v)
 corners=[tuple(Q(a[k]+ss*u[k]-c[k]-tt*v[k],2)for k in(0,1))for ss in(0,1)for tt in(0,1)];bounds=[(min(p[k]for p in corners).__floor__(),max(p[k]for p in corners).__ceil__())for k in(0,1)];boxes.append(dict(old_C_angle_index0=ai,exact_original_angle=angle,rational_corners=[[[q.numerator,q.denominator] for q in p] for p in corners],integer_bounds=bounds))
 for x in range(bounds[0][0],bounds[0][1]+1):
  for y in range(bounds[1][0],bounds[1][1]+1):
   if(x+y-N)%2:continue
   zz=sub(add(c,(2*x,2*y)),a)
   if den:
    ss,tt=Q(det(zz,v),den),Q(det(zz,u),den)
    if not(0<=ss<1 and 0<tt<=1):continue
   else:
    if det(zz,u):continue
    k=0 if u[0] else 1;q,mul=Q(zz[k],u[k]),Q(v[k],u[k]);assert mul>0
    if q>=0:continue
    ss,tt=Q(0),-q/mul
    if not(0<tt<=1):continue
   p3=(x,y,hh);geos.append((ai,p3,ss,tt))
   for A in'FQB':
    ha=angle['true_FOREIGN_heading_relative_old'];delta=after(raw(A+b1+b2),(0,0,ha));pa=(x-delta[0],y-delta[1],ha);fcut=after(W['F'],pa);ep=after(W[A],pa);verts=[z(pa),z(fcut)]
    if A!='F':verts.append(z(ep))
    for bb in[b1,b2]:ep=after(W[bb],ep);verts.append(z(ep))
    assert ep==p3
    tr=l.trace(raw(A+b1+b2+b3)+l.M)
    early=any(hit(a,b,c0,d0)for c0,d0 in zip(verts,verts[1:]));base='earlier_contact'if early else('local_immutable'if not tr['feasible']else'live')
    for role in C['all7_genuine_C_roles_and18_same_identity_source_reserves']:
     why=base;cuts=[];tau=role['actual_full_ENTRY_clock'];complete=role['actual_full_completion_clock']
     if n<complete:why='source_uncompleted'
     elif why=='live':
      for f in role['selected_reserves']:
       g=tuple(f['normalized_selected_C_cell']);q=l.rot(sub(g,pa[:2]),-pa[2]);fr=tr['first'].get(q)
       if q in l.K or(fr and fr[0]=='R'):cuts.append(g)
      why='signed_current_cut'if cuts else'NECESSARY'
     rows.append(dict(role=(role['actual_full'],role['selected_C_index1']),n=n,b1=b1,b2=b2,b3=b3,A=A,pa=pa,p3=p3,why=why,cuts=cuts))

assert len(angles)==160 and len(geos)==225 and len(rows)==4725
assert Counter(r['why'] for r in rows)=={
    'source_uncompleted':540,'local_immutable':462,'earlier_contact':40,
    'signed_current_cut':3140,'NECESSARY':543}
assert all(r['why']=='signed_current_cut' for r in rows if r['n']==3)
role_lookup={(r['actual_full'],r['selected_C_index1']):r
             for r in C['all7_genuine_C_roles_and18_same_identity_source_reserves']}
assert len(role_lookup)==7

# Exact monotonicity of the proof domain, not a hypothetical extension of
# the earlier field. A real prior input consumer before deadline Nnew is
# among the signed max-deadline rows and cannot have been discarded solely
# because it exceeds that max deadline. Source completion is retained.
monotone=[]
for key,role in role_lookup.items():
    full,selected=key
    tau=role['actual_full_ENTRY_clock']
    for n in (1,2,3):
        Nnew=n-tau
        valid=n>=role['actual_full_completion_clock']
        subset=[]
        if valid:
            for reserve in role['selected_reserves']:
                for index in reserve['all_query_indices']:
                    query=C['all1794_exact_source_output_consumer_queries'][index]
                    if (query['actual_full_source_age']>Nnew
                            or query['consumer_full_completion_age']>Nnew):
                        continue
                    assert query['exclusion']!='consumer_full_cannot_complete_before_actual_FOREIGN_entry'
                    subset.append(index)
        monotone.append(dict(actual_full_source=full,selected_C_index1=selected,
            true_atomic_preFOREIGN_age=n,actual_full_ENTRY_clock=tau,
            actual_full_ENTRY_age_at_FOREIGN=Nnew,
            actual_full_completion_clock=role['actual_full_completion_clock'],
            source_fully_completed_before_FOREIGN=valid,
            exact_subset_of_signed_max_deadline_query_indices=subset,
            no_future_history_extension_assumed=True))
assert len(monotone)==21


def physical_owner(T,tick):
    lo=0
    for index,atom in enumerate(T):
        if tick<lo+len(W[atom]):
            return dict(actual_atom_index0=index,actual_atom=atom,atom_start_tick0=lo,
                        canonical=o.describe(atom,tick-lo))
        lo+=len(W[atom])
    j=tick-lo
    assert 0<=j<len(l.M)
    return dict(actual_atom='next actual word',next_word_tick0=j,
                next_word_read_number1=j+1,turn=l.M[j])


# Attach literal CURRENT witnesses and actual read owners. Unknown outputs
# are not assumed dead/WHITE; only the selected signed reserve is used.
for index,row in enumerate(rows):
    row['typed_role_mask_index0']=index
    full,selected=row['role']
    role=role_lookup[full,selected]
    if row['why']=='signed_current_cut':
        trace=l.trace(raw(row['A']+row['b1']+row['b2']+row['b3'])+l.M)
        assert trace['feasible']
        proof=[]
        for cell0 in row['cuts']:
            cell=tuple(cell0)
            local=l.rot(sub(cell,row['pa'][:2]),-row['pa'][2])
            first=trace['first'].get(local)
            fact=next(r for r in role['selected_reserves'] if tuple(r['normalized_selected_C_cell'])==cell)
            fact=dict(actual_full_source=full,selected_C_index1=selected,
                signed_C3_reserve_index0=role['selected_reserves'].index(fact),
                full_output_slot=fact['full_output_slot'],actual_last_R_tick0=fact['actual_last_R_tick0'],
                normalized_selected_C_cell=fact['normalized_selected_C_cell'])
            if local in l.K:
                proof.append(dict(SAME_current_cell=cell,source_reserve=fact,
                    conflict='external CURRENT cannot occupy actual FOREIGN entryK'))
            else:
                assert first and first[0]=='R'
                proof.append(dict(SAME_current_cell=cell,source_reserve=fact,
                    conflict='actual combined first R requires WHITE beforeFOREIGN',
                    combined_tick0=first[1],actual_read_owner=physical_owner(
                        row['A']+row['b1']+row['b2']+row['b3'],first[1])))
        assert proof
        row['guaranteed_CURRENT_witnesses']=proof
    elif row['why']=='local_immutable':
        T=row['A']+row['b1']+row['b2']+row['b3']
        tr=l.trace(raw(T)+l.M)
        assert not tr['feasible']
        row.update(immutable_local_conflict=tr,
            previous_actual_owner=physical_owner(T,tr['previous_read']),
            later_actual_owner=physical_owner(T,tr['conflict_read']))


def permutations(d,v,u):
    if d+v+u==0:
        yield ''
        return
    if d:
        for suffix in permutations(d-1,v,u): yield 'D'+suffix
    if v:
        for suffix in permutations(d,v-1,u): yield 'V'+suffix
    if u:
        for suffix in permutations(d,v,u-1): yield 'U'+suffix


# Only the reserve-surviving age1/2 cases need an actual old word. Each has
# one W rail, or W/C/S. x/y endpoints bound every count; all orders are kept.
count_tuples=[]
word_cases={}
for row in rows:
    if row['why']!='NECESSARY': continue
    full,selected=row['role']
    n=row['n']
    x,y,heading=row['pa']
    assert n in (1,2)
    count_start=len(count_tuples)
    counts=[]
    if n==1:
        assert heading==3
        for d in range(max(y,0)):
            v=y-1-d
            numerator=-d-3*v-x
            if numerator<0 or numerator%4: continue
            u=numerator//4
            if not d+v+u: continue
            counts.append((0,0,0,d,v,u))
    else:
        assert heading==2
        budget=-1-x
        for dw in range(max(0,budget+1)):
            for vw in range((budget-dw)//3+1):
                for uw in range((budget-dw-3*vw)//4+1):
                    mandatory_source_C2=(full in ('VCC','UCC') and selected==1)
                    if mandatory_source_C2!=(dw+vw+uw==0): continue
                    remaining=budget-dw-3*vw-4*uw
                    for ds in range(remaining+1):
                        vs=remaining-ds
                        numerator=1+dw+vw-ds-3*vs-y
                        if numerator<0 or numerator%4: continue
                        us=numerator//4
                        if not ds+vs+us: continue
                        counts.append((dw,vw,uw,ds,vs,us))
    row_word_keys=[]
    for dw,vw,uw,ds,vs,us in counts:
        tuple_index=len(count_tuples)
        count_tuples.append(dict(typed_role_mask_index0=row['typed_role_mask_index0'],
            actual_full_source=full,selected_C_index1=selected,n=n,
            first_rail_counts=dict(D=dw,V=vw,U=uw),
            final_rail_counts=dict(D=ds,V=vs,U=us)))
        for X in permutations(dw,vw,uw):
            for Y in permutations(ds,vs,us):
                if Y[-1] not in ('VU' if row['A'] in 'FQ' else 'U'): continue
                before=full[0]+'C'*(selected-1)
                old_tail='C'+(X+'C' if n==2 else '')+Y
                old=before+old_tail
                T=old+row['A']+row['b1']+row['b2']+row['b3']
                # Every full source role and literal endpoint remains real.
                old_entry=after(raw(before))
                actual_FOREIGN=after(raw(old))
                normalized_FOREIGN=(*l.rot(sub(actual_FOREIGN[:2],old_entry[:2]),-old_entry[2]),
                                    (actual_FOREIGN[2]-old_entry[2])%4)
                assert normalized_FOREIGN==tuple(row['pa'])
                actual_third=after(raw(old+row['A']+row['b1']+row['b2']))
                normalized_third=(*l.rot(sub(actual_third[:2],old_entry[:2]),-old_entry[2]),
                                 (actual_third[2]-old_entry[2])%4)
                assert normalized_third==tuple(row['p3'])
                assert old_tail.count('C')==n
                key=(full,selected,n,T)
                row_word_keys.append(key)
                if key not in word_cases:
                    tr=l.trace(raw(T)+l.M)
                    assert not tr['feasible']
                    word_cases[key]=dict(actual_full_source=full,selected_C_index1=selected,
                        true_atomic_preFOREIGN_age=n,tokens=list(T),
                        first_old_rail=list(X),last_old_rail=list(Y),
                        actual_old_full_source_prefix=before+'C',
                        immutable_conflict=tr,
                        previous_actual_owner=physical_owner(T,tr['previous_read']),
                        later_actual_owner=physical_owner(T,tr['conflict_read']))
    row['all_exact_endpoint_count_tuple_indices']=list(range(count_start,len(count_tuples)))
    row['all_ordered_valid_last_packet_word_keys']=[list(key) for key in sorted(set(row_word_keys))]
    row['final_exclusion']=('exact_endpoint_or_last_packet_grammar_has_no_solution'
        if not row_word_keys else 'all_endpoint_exhaustive_genuine_full_source_words_immutable_inconsistent')
assert len(count_tuples)==1614 and len(word_cases)==10152
assert max(sum(r['first_rail_counts'].values())+sum(r['final_rail_counts'].values()) for r in count_tuples)==10
assert all(r['immutable_conflict']['conflict_read']<len(raw(r['tokens'])) for r in word_cases.values())
paths=[
    R/'third_ordinary_local_interface_2026-10-24/manifest.json',
    R/'audits/third_local_interface_independent.json',
    R/'second_old_C_age3_2026-10-24/manifest.json',
    R/'audits/old_C_age3_reserve_independent.json',
    R/'first_foreign_two_ordinary_simplicity_2026-10-24/manifest.json',
    R/'audits/two_RAW_simplicity_independent.json',
    R/'seven_word_spatial_return_2026-10-23/complete8_foreign_adjacency_manifest.json',
    R/'second_contact_signed_obligations_2026-10-24/core_status_qualification_manifest.json',
    R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py']
assert all(p.exists() for p in paths)
out=dict(status='AUTHOR_FROZEN_OLD_C_THIRD_SOURCE_MONOTONE_RESERVE_AND_ENDPOINT_CLOSURE_PENDING_REVIEW',
    scope='Only outgoing actual preFOREIGN old C source in a genuine full G8 producer, chronological FIRST new THIRD ordinary RAW contact after original U-entry G8 prefix and FIRST foreign, with actual terminalM11. All160 angular/source-age interfaces, no third simplicity.',
    all160_exact_original_C_angle_boxes=boxes,
    all225_outgoing_owned_contact_poses=[dict(local_C_angle_index0=ai,third_pose=p3,
        old_s=[ss.numerator,ss.denominator],new_t=[tt.numerator,tt.denominator]) for ai,p3,ss,tt in geos],
    all21_actual_full_role_deadline_subset_certificates=monotone,
    all4725_actual_containing_role_foreign_masks=rows,
    exact_initial_guard_classification=dict(Counter(r['why'] for r in rows)),
    all1614_remaining_exact_endpoint_count_tuples=count_tuples,
    all10152_ordered_genuine_full_source_word_conflicts=[word_cases[key] for key in sorted(word_cases)],
    endpoint_bounds='At true age1, only W rail: xA=-d-3v-4u,yA=1+d+v. At true age2, W/C/S: xA=-1-dW-3vW-4uW-dS-vS,yA=1+dW+vW-dS-3vS-4uS. These bound all counts from each finite target, not by a guessed prefix depth. C1 in VCC/UCC forces empty first rail; every other completed-source role requires a nonempty first rail before the later C.',
    genuine_U_entry_probe='All potential initial-UCC C2 age1 contact words are included; none succeeds. No prepared positive is being mistaken for genuine U ancestry, and no reverse depth search is used.',
    conclusion='All old-C THIRD first-contact alternatives are excluded:540 source-completion failures,462 local literal failures,40 already-earlier contacts,3140 existing signed-current reserve cuts, and543 finite endpoint obligations whose10152 source-bearing words all fail inside actual RAW.',
    no_postFOREIGN_maturity_physical_WHITE_permanence_or_forgotten_CORE=True,
    no_old_D_V_U_closure_or_global_THIRD_simplicity=True,
    dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths})
(H/'old_C_third_closure.json').write_text(json.dumps(out,indent=2)+'\n')
print('160 oldC angles/225 poses/4725 actual role masks:540 incomplete+462 local+40 earlier+3140 signed reserve cuts+543 endpoint obligations.')
print('Exact old W or W/C/S budgets:1614 count tuples,derived maximum10 rail atoms,10152 full-source-bearing all-order words,ALL fail inside actual RAW.')
print('No positive genuine initialUCC realization; all old-C THIRD-source alternatives closed without ancestry-depth or postforeign maturation.')
