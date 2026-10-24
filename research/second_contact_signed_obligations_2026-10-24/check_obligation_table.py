"""Finite contact masks matched against explicit signed causal CURRENT facts.

Every full producer and atomic clock is retained. A missing proof of CURRENT
is recorded as an unresolved retirement/replacement obligation, never WHITE.
"""
from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
import importlib.util, hashlib, json
R=Path('/workspace/shared/langton');sp=importlib.util.spec_from_file_location('l',R/'word_stabilization/check_foreign_return_interfaces.py');l=importlib.util.module_from_spec(sp);sp.loader.exec_module(l);sp=importlib.util.spec_from_file_location('o',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py');o=importlib.util.module_from_spec(sp);sp.loader.exec_module(o);W=o.WORDS

def add(p,q):return p[0]+q[0],p[1]+q[1]
def sub(p,q):return p[0]-q[0],p[1]-q[1]
def det(p,q):return p[0]*q[1]-p[1]*q[0]
def after(word,pose=(0,0,0)):
 p,h=pose[:2],pose[2]
 for t in word:h=(h+(1 if t=='R'else-1))%4;p=add(p,l.DIRS[h])
 return *p,h

def z(p):return add((2*p[0],2*p[1]),l.rot((-1,-1),p[2]))
def chord(a,p):return z(p),z(after(W[a],p))
def hit(a,b,c,d):
 u,v,z0=sub(b,a),sub(d,c),sub(c,a);den=det(u,v)
 if den:
  s,t=Q(det(z0,v),den),Q(det(z0,u),den)
  return(s,t)if 0<=s<=1 and 0<=t<=1 else None
 if det(z0,u):return None
 k=0 if u[0]else 1;lo,hi=sorted((Q(c[k]-a[k],u[k]),Q(d[k]-a[k],u[k])))
 return('parallel',max(0,lo),min(1,hi))if max(0,lo)<=min(1,hi)else None

def generate(old,n,guards):
 a,b=chord(old,(0,0,0));u=sub(b,a);rows=[];geos=[];boxes=[];rank={'U':0,'V':1,'D':2,'C':2}
 for b1 in'DCVU':
  N=n+int(b1=='C');h=(2-N)%4
  for b2 in'DCVU':
   if N>4 or(N==4 and rank[old]>=rank[b2]):continue
   if b1=='C'and b2=='U':continue
   c,d=chord(b2,(0,0,h));v=sub(d,c);den=det(u,v)
   corners=[tuple(Q(a[k]+s*u[k]-c[k]-t*v[k],2)for k in(0,1))for s in(0,1)for t in(0,1)]
   bounds=[(min(p[k]for p in corners).__floor__(),max(p[k]for p in corners).__ceil__())for k in(0,1)]
   boxes.append(dict(old_source=old,true_preforeign_age=n,first=b1,second=b2,exact_corners=[[[q.numerator,q.denominator] for q in p] for p in corners],integer_bounds=bounds))
   for x in range(bounds[0][0],bounds[0][1]+1):
    for y in range(bounds[1][0],bounds[1][1]+1):
     if(x+y-N)%2:continue
     zz=sub(add(c,(2*x,2*y)),a)
     if den:
      s,t=Q(det(zz,v),den),Q(det(zz,u),den)
      if not(0<=s<1 and 0<t<=1):continue
     else:raise AssertionError('Unexpected parallel')
     p2=(x,y,h);geos.append((b1,b2,p2,s,t))
     for A in'FQB':
      hA=(-n)%4;delta=after(W[A]+W[b1],(0,0,hA));pa=(x-delta[0],y-delta[1],hA);pF=after(W['F'],pa);end=after(W[A],pa);verts=[z(pa),z(pF)]
      if A!='F':verts.append(z(end))
      tr=l.trace(W[A]+W[b1]+W[b2]+l.M)
      reason='keep';cuts=[]
      if any(hit(a,b,c0,d0)for c0,d0 in zip(verts,verts[1:])):reason='foreign_contact'
      elif hit(a,b,*chord(b1,end)):reason='b1_contact'
      elif not tr['feasible']:reason='local_conflict'
      else:
       for guard in guards:
        q=l.rot(sub(guard,pa[:2]),-pa[2]);f=tr['first'].get(q)
        if q in l.K:cuts.append((guard,'core'))
        elif f and f[0]=='R':cuts.append((guard,'white',f[1]))
       if cuts:reason='guard'
      rows.append(dict(old=old,n=n,A=A,b1=b1,b2=b2,pa=pa,p2=p2,reason=reason,cuts=cuts))
 return boxes,geos,rows


HERE=Path(__file__).resolve().parent
ROOT=R
WORDS=W


def raw(tokens):
    return ''.join(WORDS[a] for a in tokens)


def full_frame_to_old(cell,old_entry):
    return l.rot(sub(cell,old_entry[:2]),-old_entry[2])


def physical_owner(tokens,tick):
    lo=0
    for index,atom in enumerate(tokens):
        if tick<lo+len(WORDS[atom]):
            return dict(actual_atom_index0=index,actual_atom=atom,
                        atom_start_tick0=lo,canonical=o.describe(atom,tick-lo))
        lo+=len(WORDS[atom])
    j=tick-lo
    assert 0<=j<len(l.M)
    return dict(actual_atom='next actual word',next_word_tick0=j,
                next_word_read_number1=j+1,turn=l.M[j])


queries=json.loads((ROOT/'audits/dcuv_count5_replay/queries.json').read_text())
assert queries['status'].startswith('PASS')
assert all(v['certified_minimum_C_age']>=2 for v in queries['slots'].values())


def source_role(old,n,full,selected_C=None):
    if old=='C':
        assert selected_C is not None and full.count('C')>=selected_C
        before=full[0]+'C'*(selected_C-1)
        old_entry=after(raw(before))
        tau=-(selected_C-1)
    else:
        assert selected_C is None and full[0]==old
        before=''
        old_entry=(0,0,0)
        tau=0
    body=raw(full)
    trace=l.trace(body)
    geometry=l.literal_geometry(body)
    source_outputs={tuple(q) for q in geometry['outputs']}
    normalized_outputs={full_frame_to_old(q,old_entry):q for q in source_outputs}
    facts={}

    def add_source_fact(full_cell,proof,details):
        assert full_cell in source_outputs
        turn,tick=trace['last'][full_cell]
        assert turn=='R'
        cell=full_frame_to_old(full_cell,old_entry)
        fact=facts.setdefault(cell,dict(cell=cell,
            SAME_identity='actual full-source final-R identity',
            actual_full_output_slot=full_cell,actual_full_last_R_tick0=tick,
            proofs=[]))
        fact['proofs'].append(dict(signed_rule=proof,**details))

    prefix=''
    for index,atom in enumerate(full):
        atom_entry=after(raw(prefix))
        atom_entry_clock=tau+max(index-1,0)
        prefix+=atom
        atomic_exit=after(raw(prefix))
        exit_clock=tau+index
        beta=add(atomic_exit[:2],l.rot((1,-1),atomic_exit[2]))
        assert trace['last'][beta]==('R',len(raw(prefix))-2)
        if 0<=n-exit_clock<=2:
            add_source_fact(beta,'1325 actual atomic EXIT bud minimum3',
                dict(actual_atomic_prefix=prefix,atomic_EXIT_clock=exit_clock,
                     true_post_EXIT_age=n-exit_clock,full_entry_age=n-tau))
        common=add(atom_entry[:2],l.rot((2,0),atom_entry[2]))
        assert trace['last'][common]==('R',len(raw(prefix[:-1]))+8)
        if 0<=n-atom_entry_clock<=2:
            add_source_fact(common,'1344 actual atomic common-R8 minimum3',
                dict(actual_atom=atom,actual_atomic_prefix=prefix,
                     atomic_ENTRY_clock=atom_entry_clock,
                     true_atomic_ENTRY_age=n-atom_entry_clock,
                     full_entry_age=n-tau,second_C_shift_explicit=(index==2)))
    if full in ('VCC','UCC') and n-tau<=4:
        prefix=full[:2]
        cut=after(raw(prefix))
        beta=add(cut[:2],l.rot((1,-1),cut[2]))
        expected=(2,5) if full=='VCC' else (1,6)
        assert beta==expected
        add_source_fact(beta,'1319 full VCC/UCC internal-C1 bud minimum5',
            dict(actual_atomic_prefix=prefix,full_entry_clock=tau,
                 full_entry_age=n-tau,minimum_full_source_age=5))
    if old=='V':
        assert (0,0) in source_outputs and (1,0) in source_outputs
        if n<5:
            add_source_fact((0,0),'2036 original V-r first retirement exact5',
                dict(actual_full_source_entry_age=n,source_C_tail_preservation=True))
        if n<4:
            add_source_fact((1,0),'2043 original V-B first retirement exact4',
                dict(actual_full_source_entry_age=n,source_C_tail_preservation=True))
    key=f'{old}_n{n}_{full}'+(f'_C{selected_C}' if old=='C' else '')
    meta=dict(role_key=key,old_source=old,true_preforeign_age=n,
        actual_containing_full=full,selected_C_index1=selected_C,
        actual_prefix_before_selected_old_atom=before,
        selected_old_pose_in_full_frame=old_entry,
        actual_full_source_ENTRY_clock=tau,full_entry_age_at_FOREIGN=n-tau,
        actual_full_source_completion_clock=tau+full.count('C'),
        all_normalized_full_output_cells=sorted(normalized_outputs),
        guaranteed_CURRENT_facts=list(facts.values()),
        no_other_source_output_is_assumed_CURRENT=True)
    return meta,facts


roles=[]
for full in ('D','DC'):
    roles.append(source_role('D',3,full))
for full in ('DC','VC','VCC','UC','UCC'):
    for selected in range(1,full.count('C')+1):
        roles.append(source_role('C',3,full,selected))
for n in (3,4):
    for full in ('V','VC','VCC'):
        roles.append(source_role('V',n,full))
assert len(roles)==15

# The only additional branch is a genuine original-V A identity. If it is
# absent at foreign3, signed2043 forces actual V/VC(0,4,S) at clock2.
# All SIX literal base outputs of that real helper are current at age1.
# No at-most-one seal, fabricated output slot or postforeign age is used.
helper_outputs=[]
for slot in l.literal_geometry(WORDS['V'])['outputs']:
    cell=add((0,4),l.rot(tuple(slot),2))
    helper_outputs.append(dict(cell=cell,SAME_identity='genuine age2 cleanup helper V-base output',
        actual_helper_base_slot=slot,
        proofs=[dict(signed_rule='2043 A only cleanup V/VC at exact2; canonical all-produced-input minimum2',
                     genuine_helper_pose=(0,4,2),genuine_helper_ENTRY_clock=2,
                     true_helper_full_ENTRY_age_at_FOREIGN=1,
                     possible_helper_full_types=['V','VC'],
                     own_helper_C_tail_preserves_base_outputs=True)]))
assert {tuple(f['cell']) for f in helper_outputs}=={(0,4),(0,3),(-1,4),(-2,4),(-2,3),(-2,2)}
for helper_full in ('V','VC'):
    htrace=l.trace(raw(helper_full))
    hgeometry=l.literal_geometry(raw(helper_full))
    vtrace=l.trace(WORDS['V'])
    for fact in helper_outputs:
        slot=tuple(fact['actual_helper_base_slot'])
        assert list(slot) in hgeometry['outputs']
        assert htrace['last'][slot]==vtrace['last'][slot]
        assert htrace['last'][slot][0]=='R'
        fact.setdefault('actual_last_R_preserved_by_each_real_helper_tail',{})[helper_full]=htrace['last'][slot]


all_boxes=[]
all_poses=[]
base_rows=[]
for old,n in [('D',3),('C',3),('V',3),('V',4)]:
    boxes,geos,rows=generate(old,n,[])
    all_boxes.extend(boxes)
    all_poses.extend(dict(old_source=old,true_preforeign_age=n,first=b1,second=b2,
        second_pose=p2,old_s=[s.numerator,s.denominator],new_t=[t.numerator,t.denominator])
        for b1,b2,p2,s,t in geos)
    base_rows.extend(rows)
assert len(all_boxes)==44 and len(all_poses)==89 and len(base_rows)==267
assert Counter((r['old'],r['n']) for r in base_rows)=={('D',3):54,('C',3):54,('V',3):141,('V',4):18}
assert Counter(r['reason'] for r in base_rows)=={'keep':261,'b1_contact':6}


def analyze_state(base,role,current_facts,state_name,retired_original_A=False):
    tokens=base['A']+base['b1']+base['b2']
    trace=l.trace(raw(tokens)+l.M)
    assert trace['feasible']
    pa=base['pa']
    hits=[]
    current_cells=set()
    for fact in current_facts:
        cell=tuple(fact['cell'])
        assert cell not in current_cells
        current_cells.add(cell)
        local=l.rot(sub(cell,pa[:2]),-pa[2])
        first=trace['first'].get(local)
        if local in l.K:
            hits.append(dict(same_current_cell=cell,conflict='foreign ENTRY core',fact=fact))
        elif first and first[0]=='R':
            hits.append(dict(same_current_cell=cell,conflict='actual combined first read requires WHITE',
                combined_tick0=first[1],actual_read_owner=physical_owner(tokens,first[1]),fact=fact))
    unresolved=[]
    dormant=[]
    if not hits:
        for cell in map(tuple,role['all_normalized_full_output_cells']):
            if cell in current_cells: continue
            local=l.rot(sub(cell,pa[:2]),-pa[2])
            first=trace['first'].get(local)
            item=dict(original_full_source_cell=cell,
                      original_A_already_retired_by_state=(retired_original_A and cell==(0,1)))
            if local in l.K:
                item['obligation']='Original identity must already be absent, while physical BLACK belongs to foreign ENTRY core; a real core history is required.'
            elif first and first[0]=='R':
                item['obligation']='Original identity must already be retired and the cell WHITE before foreign; no physical-WHITE permanence has been proved.'
            elif first:
                item['obligation']='Cell must be BLACK before foreign: surviving original or a genuine replacement/core export. Neither is inferred.'
            else:
                item['obligation']='Dormant full-source output misses this entire combined context; do not drop its possible current identity.'
                dormant.append(item)
                continue
            if first:
                item['actual_combined_first_read']=(first[0],first[1])
                item['actual_read_owner']=physical_owner(tokens,first[1])
            unresolved.append(item)
        # The prior actual EXIT bud remains a historical obligation at age3/4,
        # not a guaranteed current fact once its generic minimum is reached.
        beta=(1,-1)
        if beta not in current_cells:
            local=l.rot(sub(beta,pa[:2]),-pa[2])
            first=trace['first'].get(local)
            if local in l.K or first:
                unresolved.append(dict(historical_actual_prior_EXIT_bud=beta,
                    true_post_EXIT_age=base['n'],generic_minimum3_no_longer_suffices=True,
                    actual_combined_first_read=first,
                    obligation='Resolve an actual preforeign retirement or original survival; a full-producer clock reset is not allowed.'))
    return dict(state=state_name,classification='excluded_by_signed_CURRENT_fact' if hits else 'necessary_unresolved_state',
                exact_current_fact_conflicts=hits,
                unresolved_retirement_replacement_or_entry_core_obligations=unresolved,
                dormant_source_outputs_explicitly_retained=dormant)


role_rows=[]
for role,facts in roles:
    for base in base_rows:
        if (base['old'],base['n'])!=(role['old_source'],role['true_preforeign_age']): continue
        row=dict(source_role=role['role_key'],old_source=base['old'],true_preforeign_age=base['n'],
            foreign=base['A'],first=base['b1'],second=base['b2'],
            foreign_pose=base['pa'],second_pose=base['p2'])
        if base['reason']!='keep':
            row.update(classification='earlier_first_return_source_contact',states=[])
        else:
            current=list(facts.values())
            if base['old']=='V' and base['n']==3:
                A=dict(cell=(0,1),SAME_identity='original source V-A current branch',
                    proofs=[dict(signed_rule='2043 exhaustive original-A first retirement exact2',
                                 branch='original A not retired before foreign3')])
                states=[analyze_state(base,role,current+[A],'original_A_still_CURRENT'),
                        analyze_state(base,role,current+helper_outputs,'original_A_retired_at2_genuine_helper_cohort_CURRENT',True)]
            else:
                states=[analyze_state(base,role,current,'direct_signed_current_facts')]
            row.update(states=states,
                classification='all_causal_states_excluded' if all(s['classification']=='excluded_by_signed_CURRENT_fact' for s in states)
                               else 'necessary_unresolved_state')
        role_rows.append(row)
assert len(role_rows)==963
summary={}
for role,facts in roles:
    selected=[r for r in role_rows if r['source_role']==role['role_key']]
    summary[role['role_key']]=dict(Counter(r['classification'] for r in selected))
assert all(r['classification']!='necessary_unresolved_state' for r in role_rows if r['old_source']=='V' and r['true_preforeign_age']==4)
assert all(not(s['classification']=='necessary_unresolved_state' and s['state'].startswith('original_A_retired'))
           for r in role_rows for s in r['states'])

paths=[
    ROOT/'second_ordinary_after_first_foreign_2026-10-24/small_second_ordinary_geometry_manifest.json',
    ROOT/'audits/check_second_ordinary_small_interface_independent.json',
    ROOT/'seven_word_spatial_return_2026-10-23/first_foreign_first_returned_atom_simplicity_manifest.json',
    ROOT/'audits/check_first_foreign_returned_simplicity_independent.json',
    ROOT/'core_periodicity_new/atomic_exit_bud_frozen_20261023_1325/manifest.json',
    ROOT/'audits/check_atomic_exit_bud_independent.json',
    ROOT/'core_periodicity_new/atomic_common_4C_frozen_20261023_1344/manifest.json',
    ROOT/'audits/check_atomic_common_four_C_independent.json',
    ROOT/'core_periodicity_new/internal_C_prefix_bud_frozen_20261023_1319/manifest.json',
    ROOT/'audits/check_internal_C_bud_independent.json',
    ROOT/'core_periodicity_new/V_parallel_reproductive_supply_frozen_20261023_2036/manifest.json',
    ROOT/'audits/check_V_parallel_reproductive_supply_independent.json',
    ROOT/'core_periodicity_new/V_C_same_heading_exclusion_frozen_20261023_2043/manifest.json',
    ROOT/'audits/check_V_C_same_heading_exclusion_independent.json',
    ROOT/'audits/dcuv_count5_replay/queries.json',
    ROOT/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py']
assert all(p.exists() for p in paths)
out=dict(status='AUTHOR_FROZEN_SIGNED_CURRENT_OBLIGATION_TABLE_PENDING_REVIEW',
    scope='Only chronological first new SECOND ordinary RAW contact, original U-entry complete-eight prefix and first foreign. Full role-specific old D/C age3 and old V age3/4 masks; one actual final M11. No broader second simplicity.',
    all44_angle_parallelograms=all_boxes,
    all89_outgoing_owned_contact_poses=all_poses,
    all267_foreign_typed_base_rows=base_rows,
    all15_genuine_source_role_current_fact_sets=[meta for meta,facts in roles],
    genuine_V_A_cleanup_helper_six_literal_base_outputs=helper_outputs,
    all963_role_specific_causal_mask_obligations=role_rows,
    exact_summary_by_real_source_role=summary,
    conclusion='Old V at true preforeign age4 is excluded by source r (twelve placements) or earlier b1 contact (six). At age3, any surviving V state must retain ORIGINAL A; the genuine age2-cleanup-helper state is always contradicted. Old C age3 and remaining D/V age3 states retain explicit unproved retirement/replacement/core and dormant-output obligations.',
    no_unproven_CURRENT_or_WHITE_or_functional_reset_assumed=True,
    no_long_word_enumeration_or_finite_geometry_quotient=True,
    no_global_coverage_or_arbitrary_tail_claim=True,
    dependencies={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths})
(HERE/'signed_current_obligations.json').write_text(json.dumps(out,indent=2)+'\n')
print('44 exact angle boxes,89 outgoing-owned poses,267 foreign types; fifteen real source roles produce963 explicit causal mask rows.')
print(json.dumps(summary,sort_keys=True))
print('OldV4 closes; every surviving oldV3 branch has original A CURRENT. Other retirement/core/dormant obligations remain explicit.')
