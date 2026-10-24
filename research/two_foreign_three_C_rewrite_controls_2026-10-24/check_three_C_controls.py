"""Three actual genuine U-entry, two-foreign, three-C rewrite controls.
These are fixed full-board histories, not a scan or an iterable state.
"""
from pathlib import Path
from fractions import Fraction
import importlib.util,json,hashlib
ROOT=Path('/workspace/shared/langton');HERE=Path(__file__).resolve().parent

def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module
lit=load('literal',ROOT/'word_stabilization/check_foreign_return_interfaces.py')
owner=load('owner',ROOT/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py')
W=owner.WORDS

def add(p,q):return p[0]+q[0],p[1]+q[1]
def sub(p,q):return p[0]-q[0],p[1]-q[1]
def after(word,pose=(0,0,0)):
    p,h=pose[:2],pose[2]
    for c in word:
        h=(h+(1 if c=='R'else-1))%4;p=add(p,lit.DIRS[h])
    return (*p,h)
def z(p):return add((2*p[0],2*p[1]),lit.rot((-1,-1),p[2]))
def det(p,q):return p[0]*q[1]-p[1]*q[0]
def meet(a,b,c,d):
    u,v,q=sub(b,a),sub(d,c),sub(c,a);den=det(u,v)
    if den:
        s,t=Fraction(det(q,v),den),Fraction(det(q,u),den)
        return dict(old_s=str(s),new_lo=str(t),new_hi=str(t)) if 0<=s<=1 and 0<=t<=1 else None
    if det(q,u):return None
    k=0 if v[0]else 1
    lo,hi=sorted((Fraction(a[k]-c[k],v[k]),Fraction(b[k]-c[k],v[k])))
    lo,hi=max(Fraction(0),lo),min(Fraction(1),hi)
    if lo>hi:return None
    point=add(c,(lo*v[0],lo*v[1]));j=0 if u[0]else 1
    return dict(old_s=str(Fraction(point[j]-a[j],u[j])),new_lo=str(lo),new_hi=str(hi))

PREFIX='UQCDDVCVUUC';HOOK={(-1,-1),(-2,-1),(-3,-1),(-3,-2)}
NE={(-1,-1),(-1,0),(-1,1),(0,0),(0,1),(1,0),(1,1),(1,2),(2,0),(2,1)}
STAR={(0,0),(0,1),(1,0),(1,1)}
controls=[]
for last,target,seed_mass,reads in [('V','F',65,454),('U','F',68,464),('U','Q',69,472)]:
    packet=PREFIX+'D'*12+last+target
    raw=''.join(W[a]for a in packet);trace=lit.trace(raw+lit.M)
    assert trace['feasible'] and len(raw)+11==reads and packet.count('C')==3
    seed={cell for cell,(c,_) in trace['first'].items() if c=='L'}
    assert len(seed)==seed_mass
    B={cell:('initial',cell)for cell in seed};p=(0,0,0);tick=0
    tracked=[];cut_states=[];deaths=[];pieces=[];atom_entries=[]
    for index,atom in enumerate(packet):
        start=p;start_tick=tick;atom_entries.append(dict(index0=index,atom=atom,ENTRY=p,global_start_tick0=tick))
        if index in (0,1,9):
            outputs=set(map(tuple,lit.literal_geometry(W[atom])['outputs']))
            local_trace=lit.trace(W[atom])
            for q in sorted(outputs):
                cell=add(p[:2],lit.rot(q,p[2]));birth=tick+local_trace['last'][q][1]
                tracked.append(dict(source_atom_index0=index,source_atom=atom,source_ENTRY=p,
                    source_local_cell=q,cell=cell,source_R_own_tick0=local_trace['last'][q][1],
                    source_R_global_tick0=birth,is_initial_U_star=index==0 and q in STAR,
                    is_first_Q_hook=index==1 and q in HOOK,is_first_Q_NE=index==1 and q in NE))
        for own_tick,c in enumerate(W[atom]):
            cell=p[:2];assert(cell in B)==(c=='L')
            if c=='L':
                old=B[cell]
                for identity in tracked:
                    if identity['cell']==cell and identity['source_R_global_tick0']==old:
                        deaths.append(dict(source_atom_index0=identity['source_atom_index0'],source_local_cell=identity['source_local_cell'],cell=cell,source_R_global_tick0=old,death_global_tick0=tick,reader_atom_index0=index,reader_atom=atom,actual_owner=owner.describe(atom,own_tick)))
                del B[cell]
            else:B[cell]=tick
            p=after(c,p);tick+=1
        end=p
        if atom in'FQB':
            mid=after(W['F'],start);pieces.append(dict(atom_index0=index,atom=atom,piece='actual_F56_prefix',start=z(start),end=z(mid)))
            if atom!='F':pieces.append(dict(atom_index0=index,atom=atom,piece='actual_tail',start=z(mid),end=z(end)))
        else:pieces.append(dict(atom_index0=index,atom=atom,piece='ordinary',start=z(start),end=z(end)))
        K={add(p[:2],lit.rot(q,p[2]))for q in lit.K}
        states=[]
        for identity in tracked:
            same=B.get(identity['cell'])==identity['source_R_global_tick0']
            states.append(dict(source_atom_index0=identity['source_atom_index0'],source_local_cell=identity['source_local_cell'],cell=identity['cell'],source_R_global_tick0=identity['source_R_global_tick0'],SAME_physically_BLACK=same,CURRENT=same and identity['cell']not in K,alive_CORE=same and identity['cell']in K,actual_present_R_identity=B.get(identity['cell'])))
        cut_states.append(dict(after_atom_index0=index,atom=atom,cut_tick0=tick,actual_head=p,tracked_original_ID_states=states))
    final_raw_pose=p;before_M_tick=tick
    first_q_hook=[i for i in tracked if i['is_first_Q_hook']]
    assert len(first_q_hook)==4 and all(B.get(i['cell'])==i['source_R_global_tick0']for i in first_q_hook)
    initial_star=[i for i in tracked if i['is_initial_U_star']]
    assert len(initial_star)==4 and all(B.get(i['cell'])==i['source_R_global_tick0']for i in initial_star)
    ne_deaths=[d for d in deaths if d['source_atom_index0']==1 and tuple(d['source_local_cell'])in NE]
    assert {(tuple(d['source_local_cell']),d['reader_atom_index0'],d['actual_owner']['owner_tick0'])for d in ne_deaths}=={((2,1),9,13),((2,0),9,14)}
    assert {(d['death_global_tick0'],tuple(d['cell']))for d in ne_deaths}=={(219,(2,5)),(220,(2,4))}
    assert B.get((2,5))==227 and (2,4)not in B
    assert (2,5) not in {add(p[:2],lit.rot(q,p[2])) for q in lit.K}
    assert all(r['CURRENT'] for r in cut_states[-1]['tracked_original_ID_states'] if r['source_atom_index0']==9)
    # The actual last foreign and its supplied physical M both MISS the
    # first Q hook; this is directly checked, not inferred by iteration.
    final_start=atom_entries[-1];last_trace=lit.trace(W[target]+lit.M)
    for identity in first_q_hook:
        q=lit.rot(sub(identity['cell'],final_start['ENTRY'][:2]),(-final_start['ENTRY'][2])%4)
        assert q not in last_trace['first']
    for marker_tick,c in enumerate(lit.M):
        cell=p[:2];assert(cell in B)==(c=='L')
        if c=='L':del B[cell]
        else:B[cell]=tick
        p=after(c,p);tick+=1
    assert all(B.get(i['cell'])==i['source_R_global_tick0']for i in initial_star+first_q_hook)
    pair_checks=[]
    for i,a in enumerate(pieces):
        for j in range(i+1,len(pieces)):
            b=pieces[j];intersection=meet(a['start'],a['end'],b['start'],b['end'])
            if j==i+1:assert intersection==dict(old_s='1',new_lo='0',new_hi='0')
            else:assert intersection is None
            pair_checks.append(dict(earlier_piece_index0=i,later_piece_index0=j,intersection=intersection,legal_adjacent_point=j==i+1))
    controls.append(dict(packet=packet,compact_packet='UQCDDVCVUUC D^12 '+last+target,complete_seed=sorted(seed),seed_mass=len(seed),all_actual_physical_reads=tick,RAW_length=before_M_tick,RAW_EXIT=final_raw_pose,after_actual_M_fine_pose=p,final_physical_mass=len(B),all_actual_atom_entries=atom_entries,all_original_output_definitions=tracked,all_original_output_deaths=deaths,all_marked_cut_ID_states=cut_states,first_Q_NE_pair_deaths=ne_deaths,new_recycled_q=dict(cell=(2,5),different_R_global_tick0=227,SAME_current_at_last_foreign_EXIT=True),initial_U_star_all4_SAME_at_end=True,first_Q_hook_all4_SAME_at_end=True,all_actual_repaired_proxy_pieces=pieces,all_closed_proxy_pair_checks=pair_checks,finite_OPEN_proxy_simple_through_second_foreign_RAW=True))

D=['Q_B_hook_three_C_foreign_transfer_2026-10-24/manifest.json','audits/check_QB_three_C_hook_transfer_independent.json','foreign_two_C_pair_hole_transfer_2026-10-24/manifest.json','audits/check_foreign_two_C_pair_hole_independent.json','word_stabilization/check_foreign_return_interfaces.py','literal_ownership_conventions_2026-10-24/canonical_read_ownership.py']
result=dict(status='AUTHOR_FROZEN_PENDING_INDEPENDENT_REVIEW',scope='Exactly three fixed complete genuine U-entry histories. First Q then three ordinary Cs and one actual next F/Q. Complete finite fields, every physical read, original births/deaths/core status and finite proxy intersections are direct checks. No depth scan or theorem iteration is used.',all3_complete_controls=controls,mechanism='The first Q genuinely loses its common R8 and q R7 through ordinary U index9; those originals die at219/220, and a new q is born at227. The remaining ordinary W rail and completed second foreign are real, unlike the earlier partial second-Q hole attempt. All four SAME first-Q hook IDs and all four SAME initial-U stars are retained. The next foreign is spatially separate; no protected-hook erosion is attained here.',construction='The fixed attained paired-NE rewrite prefix is followed by C3 and twelve actual W-oriented D bases, then V/U and F/Q. The choice12 is a prescribed spatial-separation control, not a minimality claim, an unbounded-family theorem, or an imposed search depth.',not_claimed=['No completed second-foreign erosion of the original hook or initial U-star.','No all-length D-rail family or finite-state quotient.','No first-foreign theorem is reset or iterated; every finite proxy pair is checked directly.','No arbitrary-tail simplicity, future continuation, language coverage, capture or decreasing foreign budget.'],dependencies={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest()for p in D})
(HERE/'three_C_controls.json').write_text(json.dumps(result,indent=2)+'\n')
print('Three actual two-FORE C3 controls: 65/68/69 seeds;454/464/472 reads; genuine Q pair deaths219/220/newq227; all old hook/star IDs retained; finite proxies directly simple.')
