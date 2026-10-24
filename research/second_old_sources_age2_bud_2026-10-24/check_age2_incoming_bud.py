"""Exact common incoming-EXIT-bud interface for old D/C/V at true age two.

No unbounded-history enumeration and no postforeign maturation are used.
Every new contact pose and every actual combined first-read owner is retained.
"""
from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
import importlib.util
import hashlib
import json

ROOT = Path('/workspace/shared/langton')
HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('lit', ROOT/'word_stabilization/check_foreign_return_interfaces.py')
lit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lit)
spec = importlib.util.spec_from_file_location('owner', ROOT/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py')
owner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(owner)
WORDS = owner.WORDS
BETA = (1,-1)


def add(p,q): return p[0]+q[0],p[1]+q[1]
def sub(p,q): return p[0]-q[0],p[1]-q[1]
def det(p,q): return p[0]*q[1]-p[1]*q[0]
def raw(tokens): return ''.join(WORDS[a] for a in tokens)


def after(word, pose=(0,0,0)):
    p,h = pose[:2],pose[2]
    for turn in word:
        h = (h+(1 if turn=='R' else -1))%4
        p = add(p,lit.DIRS[h])
    return *p,h


def z2(pose): return add((2*pose[0],2*pose[1]),lit.rot((-1,-1),pose[2]))
def chord(atom,pose): return z2(pose),z2(after(WORDS[atom],pose))
def floor(q): return q.numerator//q.denominator

def ceil(q): return -((-q.numerator)//q.denominator)


def hit(a,b,c,d):
    u,v,z = sub(b,a),sub(d,c),sub(c,a)
    den = det(u,v)
    if den:
        s,t = Q(det(z,v),den),Q(det(z,u),den)
        return dict(kind='point',s=s,t=t) if 0<=s<=1 and 0<=t<=1 else None
    if det(z,u): return None
    k = 0 if u[0] else 1
    lo,hi = sorted((Q(c[k]-a[k],u[k]),Q(d[k]-a[k],u[k])))
    return dict(kind='collinear',old_interval=(max(Q(0),lo),min(Q(1),hi))) if max(0,lo)<=min(1,hi) else None


def physical_owner(tokens,tick):
    lo=0
    for index,atom in enumerate(tokens):
        if tick<lo+len(WORDS[atom]):
            return dict(actual_atom_index0=index,actual_atom=atom,
                        atom_start_tick0=lo,canonical=owner.describe(atom,tick-lo))
        lo+=len(WORDS[atom])
    j=tick-lo
    assert 0<=j<len(lit.M)
    return dict(actual_atom='next actual word',next_word_tick0=j,
                next_word_read_number1=j+1,turn=lit.M[j])


boxes=[]
poses=[]
rows=[]
for old in 'DCV':
    a,b=chord(old,(0,0,0))
    u=sub(b,a)
    for b1 in 'DCVU':
        N=2+int(b1=='C')
        heading=(2-N)%4
        for b2 in 'DCVU':
            if b1=='C' and b2=='U':
                continue
            c,d=chord(b2,(0,0,heading))
            v=sub(d,c)
            den=det(u,v)
            corners=[tuple(Q(a[k]+s*u[k]-c[k]-t*v[k],2) for k in(0,1))
                     for s in(0,1) for t in(0,1)]
            bounds=[(floor(min(p[k] for p in corners)),ceil(max(p[k] for p in corners))) for k in(0,1)]
            boxes.append(dict(old_source=old,first=b1,second=b2,
                rational_corners=[[[q.numerator,q.denominator] for q in p] for p in corners],integer_bounds=bounds))
            for x in range(bounds[0][0],bounds[0][1]+1):
                for y in range(bounds[1][0],bounds[1][1]+1):
                    if (x+y-N)%2: continue
                    z=sub(add(c,(2*x,2*y)),a)
                    if den:
                        s,t=Q(det(z,v),den),Q(det(z,u),den)
                        if not(0<=s<1 and 0<t<=1): continue
                    else:
                        if det(z,u): continue
                        k=0 if u[0] else 1
                        q,mul=Q(z[k],u[k]),Q(v[k],u[k])
                        assert mul>0
                        if q>=0: continue
                        s,t=Q(0),-q/mul
                        if not(0<t<=1): continue
                    p2=(x,y,heading)
                    poses.append(dict(old_source=old,first=b1,second=b2,second_pose=p2,
                        old_s=[s.numerator,s.denominator],new_t=[t.numerator,t.denominator]))
                    for foreign in 'FQB':
                        delta=after(WORDS[foreign]+WORDS[b1],(0,0,2))
                        pa=(x-delta[0],y-delta[1],2)
                        pF=after(WORDS['F'],pa)
                        end=after(WORDS[foreign],pa)
                        vertices=[z2(pa),z2(pF)]
                        if foreign!='F': vertices.append(z2(end))
                        tokens=foreign+b1+b2
                        tr=lit.trace(raw(tokens)+lit.M)
                        row=dict(old_source=old,foreign=foreign,first=b1,second=b2,
                                 foreign_pose=pa,second_pose=p2,true_preforeign_age=2,
                                 effective_geometric_N=N)
                        if any(hit(a,b,c0,d0) for c0,d0 in zip(vertices,vertices[1:])):
                            row['classification']='foreign_already_contacts_source'
                        elif hit(a,b,*chord(b1,end)):
                            row['classification']='first_return_already_contacts_source'
                        elif not tr['feasible']:
                            row.update(classification='immutable_local_context',conflict=tr)
                        else:
                            local=lit.rot(sub(BETA,pa[:2]),-pa[2])
                            first=tr['first'].get(local)
                            row.update(incoming_beta_FOREIGN_local=local,
                                       actual_combined_first_read=first)
                            if local in lit.K:
                                row['classification']='CURRENT_beta_in_foreign_entry_core'
                            elif first and first[0]=='R':
                                row.update(classification='CURRENT_beta_before_WHITE',
                                           actual_first_read_owner=physical_owner(tokens,first[1]))
                            else:
                                row['classification']='necessary_residue_only'
                        rows.append(row)

assert len(boxes)==45
assert Counter(r['old_source'] for r in poses)=={'D':19,'C':19,'V':24}
assert Counter(r['old_source'] for r in rows)=={'D':57,'C':57,'V':72}
residues=[r for r in rows if r['classification']=='necessary_residue_only']
assert {(r['foreign'],r['first'],r['second'],r['foreign_pose'],r['second_pose']) for r in residues}=={
    ('B','C','V',(-2,-4,2),(1,2,3)),
    ('F','C','V',(-2,-2,2),(2,1,3))}
assert all(r['old_source']=='V' for r in residues)
for old in 'DC':
    assert all(r['classification']=='CURRENT_beta_before_WHITE' for r in rows if r['old_source']==old)
assert sum(r['classification']=='CURRENT_beta_before_WHITE' and r['old_source']=='V' for r in rows)==60

# Base D/V sources follow an actual final full packet, with its actual
# final atomic EXIT at clock zero. Their prior full entry is at -c, not 0.
prior_final=[]
for previous in ('D','DC','V','VC','VCC','U','UC','UCC'):
    body=raw(previous)
    exit=after(body)
    beta=add(exit[:2],lit.rot(BETA,exit[2]))
    trace=lit.trace(body)
    geometry=lit.literal_geometry(body)
    assert trace['last'][beta]==('R',len(body)-2)
    assert list(beta) in geometry['outputs']
    c=previous.count('C')
    prior_final.append(dict(previous_actual_full=previous,
        previous_full_entry_clock=-c,previous_final_atomic_EXIT_clock=0,
        post_EXIT_age_at_FOREIGN=2,actual_full_entry_age_at_FOREIGN=2+c,
        full_output_cell=beta,actual_final_R_tick0=len(body)-2,
        valid_for_old_base_sources=['D','V']))
assert len(prior_final)==8

# An internal C gets beta from its actual previous BASE or C1 prefix.
# The seven containing roles include both nonfinal C1s and actual C2s.
prior_internal=[]
for full in ('DC','VC','VCC','UC','UCC'):
    for selected in range(1,full.count('C')+1):
        prefix=full[0]+'C'*(selected-1)
        entry=after(raw(prefix))
        beta=add(entry[:2],lit.rot(BETA,entry[2]))
        tick=len(raw(prefix))-2
        trace=lit.trace(raw(full))
        geometry=lit.literal_geometry(raw(full))
        assert trace['last'][beta]==('R',tick)
        assert list(beta) in geometry['outputs']
        j=selected-1
        prior_internal.append(dict(containing_actual_full=full,selected_C_index1=selected,
            actual_prefix_before_selected_C=prefix,actual_selected_C_pose=entry,
            actual_previous_atomic_EXIT_clock=0,post_EXIT_age_at_FOREIGN=2,
            containing_full_entry_clock=-j,containing_full_entry_age_at_FOREIGN=2+j,
            containing_full_completion_clock=full.count('C')-j,
            beta_in_actual_full_frame=beta,actual_beta_R_tick0=tick))
assert len(prior_internal)==7

cu=lit.trace(WORDS['C']+WORDS['U']+lit.M)
assert not cu['feasible'] and (cu['conflict_read'],cu['previous_read'])==(29,1)
paths=[
    ROOT/'second_ordinary_after_first_foreign_2026-10-24/small_second_ordinary_geometry_manifest.json',
    ROOT/'audits/check_second_ordinary_small_interface_independent.json',
    ROOT/'seven_word_spatial_return_2026-10-23/first_foreign_first_returned_atom_simplicity_manifest.json',
    ROOT/'audits/check_first_foreign_returned_simplicity_independent.json',
    ROOT/'core_periodicity_new/atomic_exit_bud_frozen_20261023_1325/manifest.json',
    ROOT/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py']
assert all(p.exists() for p in paths)
out=dict(
    status='AUTHOR_FROZEN_OLD_D_C_V_AGE2_INCOMING_BUD_INTERFACE_PENDING_REVIEW',
    scope='Chronological FIRST new SECOND ordinary RAW contact after actual U-entry complete-eight prefix, its FIRST foreign and first ordinary RAW, with actual final M11. Only old D/C/V sources at true source-entry-to-foreign age2. D/C excluded; two necessary oldV residues retained.',
    all45_exact_angle_contact_boxes=boxes,
    all62_outgoing_owned_contact_poses=poses,
    all186_foreign_typed_context_rows=rows,
    exact_row_classification=dict(Counter(r['classification'] for r in rows)),
    all8_actual_previous_full_FINAL_bud_roles_for_D_V_sources=prior_final,
    all7_actual_internal_C_previous_BASE_C1_bud_roles=prior_internal,
    guardian_theorem='Signed1325 applies to actual previous atomic EXIT at selected source-entry clock0. The same beta=(1,-1) is CURRENT outside K at foreign clock2, strictly before its minimum3 later consumer-entry age. Prior full ages are2+c or2+j; they are not incorrectly reset to2.',
    raw_C_U_omitted_interface_conflict=cu,
    exactly_two_necessary_old_V_residues=residues,
    conclusion='Every old D or C source at true preforeign age2 is excluded by the genuine incoming beta before-WHITE conflict. OldV age2 has sixty such literal cuts and ten earlier-contact/local conflicts, leaving exactly two necessary C,V returns. No endpoint history enumeration or postforeign age law is needed.',
    no_second_simplicity_or_attainment_or_arbitrary_tail_extension=True,
    dependencies={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths})
(HERE/'age2_incoming_bud.json').write_text(json.dumps(out,indent=2)+'\n')
print('Exact45 boxes/62 outgoing-owned poses/186 foreign types: all D57+C57 cut by the genuine age2 incoming EXIT bud.')
print('OldV72 gives60 beta-WHITE cuts and10 earlier/local exclusions; exactly two necessary C,V residues remain.')
print('All eight previous final-full and seven actual internal-C roles retain true postEXIT2 versus full-entry2+c/j clocks.')
