"""Third-RAW foreign/b1 first-contact split, exact ownership and true clock.

Only finite local geometry and immutable color constraints. No new old-source
position campaign, postforeign maturity or third-simplicity theorem.
"""
from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
import importlib.util,json,hashlib
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent
s=importlib.util.spec_from_file_location('l',R/'word_stabilization/check_foreign_return_interfaces.py');l=importlib.util.module_from_spec(s);s.loader.exec_module(l);s=importlib.util.spec_from_file_location('o',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py');o=importlib.util.module_from_spec(s);s.loader.exec_module(o);W=o.WORDS

def add(p,q):return p[0]+q[0],p[1]+q[1]
def sub(p,q):return p[0]-q[0],p[1]-q[1]
def det(p,q):return p[0]*q[1]-p[1]*q[0]
def raw(t):return ''.join(W[a]for a in t)
def after(word,pose=(0,0,0)):
 p,h=pose[:2],pose[2]
 for c in word:h=(h+(1 if c=='R'else-1))%4;p=add(p,l.DIRS[h])
 return *p,h

def z(p):return add((2*p[0],2*p[1]),l.rot((-1,-1),p[2]))
def hit(a,b,c,d):
 u,v,zz=sub(b,a),sub(d,c),sub(c,a);den=det(u,v)
 if den:
  s,t=Q(det(zz,v),den),Q(det(zz,u),den)
  return dict(old_s=s,new_t=t,kind='point')if 0<=s<=1 and 0<=t<=1 else None
 if det(zz,u):return None
 k=0 if v[0]else 1
 lo,hi=sorted((Q(a[k]-c[k],v[k]),Q(b[k]-c[k],v[k])))
 lo,hi=max(0,lo),min(1,hi)
 if lo>hi:return None
 pt=tuple(Q(c[k])+lo*v[k]for k in(0,1));j=0 if u[0]else 1;s=Q(pt[j]-a[j],u[j])
 return dict(old_s=s,new_t=Q(lo),new_t_upper=Q(hi),kind='collinear')

rows=[];contacts=[];positive=[]
for A in'FQB':
 for b1 in'DCVU':
  for b2 in'DCVU':
   for b3 in'DCVU':
    T=A+b1+b2+b3;fcut=after(W['F']);end=after(W[A]);verts=[z((0,0,0)),z(fcut)];labels=['F56prefix']
    if A!='F':verts.append(z(end));labels.append(A+'tail')
    p=end
    for ix,b in enumerate([b1,b2,b3]):p=after(W[b],p);verts.append(z(p));labels.append('b'+str(ix+1)+':'+b)
    segs=list(zip(verts,verts[1:]));new=segs[-1];local=[]
    for i,old in enumerate(segs[:-1]):
     h=hit(*old,*new)
     if h and h['new_t']>0:local.append((h['new_t'],i,h))
    record=dict(tokens=T,true_foreign_piece_and_ordinary_doubled_vertices=verts,actual_outgoing_piece_labels=labels)
    if local:
     t,i,h=min(local,key=lambda x:x[0]);owner=i+1 if h['old_s']==1 else i
     assert owner<len(segs)-2 # b2 cannot be a nonadjacent old owner
     tr=l.trace(raw(T)+l.M);fpred={P:l.trace(raw(P+T)+l.M)['feasible'] for P in('VU'if A in'FQ'else'U')}
     # Every closed contact at the earliest time has one outgoing owner.
     first_owners={j+1 if hh['old_s']==1 else j for tt,j,hh in local if tt==t}
     assert first_owners=={owner}
     record.update(first_local_owner=labels[owner],first_old_owned_piece_index0=owner,
                   first_new_t=[t.numerator,t.denominator],literal_feasible=tr['feasible'],
                   all_closed_contacts=[dict(old_piece_index0=j,
                       old_piece_label=labels[j],kind=hh['kind'],
                       old_s=[hh['old_s'].numerator,hh['old_s'].denominator],
                       new_t=[tt.numerator,tt.denominator],
                       outgoing_owner_piece_index0=j+1 if hh['old_s']==1 else j)
                       for tt,j,hh in local])
     if not tr['feasible']:record['conflict']=tr
     contacts.append(record)
     if tr['feasible']:positive.append(record)
    rows.append(record)

assert len(rows)==192 and len(contacts)==4 and not positive
assert {r['tokens'] for r in contacts}=={'FCCV','FCCU','QCCU','BCCU'}
assert Counter(r['first_local_owner'] for r in contacts)=={'F56prefix':1,'b1:C':3}


def physical_owner(T,tick):
    lo=0
    for index,atom in enumerate(T):
        if tick<lo+len(W[atom]):
            return dict(actual_atom_index0=index,actual_atom=atom,
                        canonical=o.describe(atom,tick-lo))
        lo+=len(W[atom])
    j=tick-lo
    assert 0<=j<len(l.M)
    return dict(actual_atom='next actual word',next_word_tick0=j,
                next_word_read_number1=j+1,turn=l.M[j])


for row in contacts:
    T=row['tokens']
    tr=row['conflict']
    assert tr['conflict_read']<len(raw(T))
    row['previous_actual_read_owner']=physical_owner(T,tr['previous_read'])
    row['later_conflicting_actual_read_owner']=physical_owner(T,tr['conflict_read'])
    if T=='FCCV':
        assert (tr['conflict_read'],tr['previous_read'],tr['cell'],tr['turn'])==(101,45,[-1,0],'R')
    else:
        start=len(W[T[0]])
        assert (tr['conflict_read']-start,tr['previous_read']-start,tr['turn'])==(42,2,'L')
        assert row['first_new_t']==[1,2] and row['first_local_owner']=='b1:C'

# The already signed two-RAW prefix is actually recognizable in this
# three-RAW context, including b3=D10 and one real terminal prefix read.
marker=[]
for b3 in'DCVU':
    assert (W[b3]+l.M)[:11]==l.M
    marker.append(dict(third=b3,actual_RAW_reads_used=min(11,len(W[b3])),
        actual_terminal_M_reads_used=max(0,11-len(W[b3]))))

# The arbitrary-tail first-contact clock already telescopes ordinary
# directions. Its specialization here retains the two returned indicators
# separately from genuine preforeign source age n.
rank={'U':0,'V':1,'D':2,'C':2}
angles=[]
for b1 in'DCVU':
    for b2 in'DCVU':
        c1,c2=int(b1=='C'),int(b2=='C')
        for old in'DCVU':
            for b3 in'DCVU':
                for N in range(5):
                    n=N-c1-c2
                    if n<0 or(old=='C' and n<1): continue
                    if N==0 and rank[old]<=rank[b3]: continue
                    if N==4 and rank[old]>=rank[b3]: continue
                    angles.append(dict(old_source=old,first=b1,second=b2,third=b3,
                        true_old_source_ENTRY_to_FOREIGN_ENTRY_C_age=n,
                        first_returned_C_indicator=c1,second_returned_C_indicator=c2,
                        total_ordinary_C_before_third=N,
                        true_FOREIGN_heading_relative_old=(-n)%4,
                        third_heading_relative_old=(2-N)%4))
assert len(angles)==831
assert Counter(r['old_source'] for r in angles)=={'D':206,'C':160,'V':229,'U':236}
assert all(r['true_old_source_ENTRY_to_FOREIGN_ENTRY_C_age']+r['first_returned_C_indicator']+r['second_returned_C_indicator']==r['total_ordinary_C_before_third'] for r in angles)
paths=[
    R/'first_foreign_two_ordinary_simplicity_2026-10-24/manifest.json',
    R/'audits/two_RAW_simplicity_independent.json',
    R/'one_foreign_first_contact_compression_2026-10-24/manifest.json',
    R/'audits/check_one_foreign_contact_C_window_independent.json',
    R/'third_atom_CCV_adversarial_2026-10-24/manifest.json',
    R/'audits/third_CCV_independent.json',
    R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py']
assert all(p.exists() for p in paths)
out=dict(status='AUTHOR_FROZEN_THIRD_LOCAL_FOREIGN_B1_CONTACT_INTERFACE_PENDING_REVIEW',
    scope='THIRD immediate ordinary RAW after the FIRST F/Q/B and original U-entry G8 prefix, with actual terminalM11. Local foreign/b1 source elimination and831 necessary older-source angles only, no third simplicity.',
    all192_exact_foreign_b1_b2_b3_local_geometries=rows,
    exactly4_possible_local_first_contacts_all_RAW_literal_conflicts=contacts,
    all4_actual_second_context_marker_supplies=marker,
    all831_conditional_preFOREIGN_old_source_angle_interfaces=angles,
    angle_counts_by_old_source=dict(Counter(r['old_source'] for r in angles)),
    exact_local_source_conclusion='A valid third RAW cannot first meet either true foreign piece or b1. FCCV is the only owned foreign-prefix candidate and fails in its RAW. A CCU first meets the foreign-exit vertex owned by outgoing b1=C; all three are RAW-impossible. The b2 chord is adjacent only by the signed ordinary-join calculation.',
    remaining_source_scope='Any further third first-contact must be with a genuine PREforeign D/C/V/U source. This includes the immediate last plainV/U beforeA; it has NOT been excluded by this interface. True n is beforeFOREIGN only and never includes either returned C.',
    no_new_source_ancestry_or_maturity_or_finite_geometry_quotient=True,
    no_third_simplicity_or_fourth_atom_or_second_foreign_extension=True,
    dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths})
(H/'third_local_interface.json').write_text(json.dumps(out,indent=2)+'\n')
print('192 local geometries have exactly4 first contacts: FCCV foreign-prefix, A CCU outgoing b1C at foreign-exit vertex. All4 fail inside thirdRAW.')
print('Conditional older-source angle interface831 retains true n and both returned C indicators separately. No third simplicity.')
