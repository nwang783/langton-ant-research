"""Complete zero-preforeign-C oldD/V SECOND-contact slice.
Finite exact endpoints, all N-run count solutions/orders, no prefix-depth cap.
"""
from pathlib import Path
from fractions import Fraction as Q
from itertools import permutations
from collections import Counter
import json,importlib.util,hashlib
R=Path('/workspace/shared/langton');s=importlib.util.spec_from_file_location('lit',R/'word_stabilization/check_foreign_return_interfaces.py');lit=importlib.util.module_from_spec(s);s.loader.exec_module(lit)
J=json.load(open(R/'word_stabilization/shifted1_llrlrrrrlll_fold_coalesced_port_quotient.json'));W={a:r['word']for a,r in zip('DCVUFQB',J['macro_words'])};rank={'D':2,'C':2,'V':1,'U':0}
so=importlib.util.spec_from_file_location('owner',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py');owner=importlib.util.module_from_spec(so);so.loader.exec_module(owner)
def add(p,q):return p[0]+q[0],p[1]+q[1]
def sub(p,q):return p[0]-q[0],p[1]-q[1]
def det(p,q):return p[0]*q[1]-p[1]*q[0]
def pose(w,P=(0,0,0)):
 p=P[:2];h=P[2]
 for c in w:h=(h+(1 if c=='R'else-1))%4;p=add(p,lit.DIRS[h])
 return(*p,h)
def z2(p):return add((2*p[0],2*p[1]),lit.rot((-1,-1),p[2]))
def chord(a,P):return z2(P),z2(pose(W[a],P))
def hit(a,b,c,d):
 u,v,z=sub(b,a),sub(d,c),sub(c,a);den=det(u,v)
 if not den:
  if det(z,u):return None
  k=0 if u[0] else 1;lo,hi=sorted((Q(c[k]-a[k],u[k]),Q(d[k]-a[k],u[k])))
  if max(0,lo)>min(1,hi):return None
  return('collinear',max(0,lo),min(1,hi))
 s,t=Q(det(z,v),den),Q(det(z,u),den)
 return(s,t)if 0<=s<=1 and 0<=t<=1 else None
def floor(q):return q.numerator//q.denominator
def ceil(q):return-((-q.numerator)//q.denominator)
H=Path(__file__).resolve().parent
rows=[];positive=[];seen=set();boxrows=[];geomrows=[];boxes=0;geom=0
for old in'DV':
 oldc=chord(old,(0,0,0));uv=sub(oldc[1],oldc[0]);baseep=pose(W[old]);offset=baseep[:2]
 for A in'FQB':
  ep=pose(W[A]);pfx=pose(W['F']);verts=[z2((0,0,0)),z2(pfx)]
  if A!='F':verts.append(z2(ep))
  pcs=list(zip(verts,verts[1:]))
  for b1 in'DCVU':
   p2=pose(W[b1],ep);first=chord(b1,ep)
   for b2 in'DCVU':
    if b1=='C'and b2=='U':continue
    if b1!='C'and rank[old]<=rank[b2]:continue
    new=chord(b2,p2);nv=sub(new[1],new[0]);boxes+=1
    assert det(uv,nv)!=0 # no unexamined collinear case in this angle slice
    corners=[tuple(Q(oldc[0][k]+s*uv[k]-new[0][k]-t*nv[k],2)for k in(0,1))for s in(0,1)for t in(0,1)]
    bx=[(floor(min(p[k]for p in corners)),ceil(max(p[k]for p in corners)))for k in(0,1)]
    boxrows.append(dict(old_source=old,foreign=A,first_ordinary=b1,second_ordinary=b2,actual_corner_derived_integer_head_bounds=bx))
    for x in range(bx[0][0],bx[0][1]+1):
     for y in range(bx[1][0],bx[1][1]+1):
      if(x+y)%2 or x<offset[0]or y<offset[1]:continue
      tr=(2*x,2*y);nc=(add(new[0],tr),add(new[1],tr));h=hit(*oldc,*nc)
      if h is None or h[0]=='collinear'or not(0<=h[0]<1 and 0<h[1]<=1):continue
      # Old endpoint belongs to following atom, not old; foreign andfirst
      # must already be clear by signed prefix simplicity.
      bad=False
      for k,pc in enumerate(pcs):
       hh=hit(*oldc,add(pc[0],tr),add(pc[1],tr))
       if hh and not(hh==(Q(1),Q(0))and k==0 and(x,y)==offset and old in'VU'):bad=True
      hh=hit(*oldc,add(first[0],tr),add(first[1],tr))
      if hh:bad=True
      if bad:continue
      geom+=1
      geomrows.append(dict(old_source=old,foreign=A,first_ordinary=b1,second_ordinary=b2,foreign_head=(x,y,0),source_contact=dict(s=[h[0].numerator,h[0].denominator],t=[h[1].numerator,h[1].denominator]),foreign_and_b1_source_clear=True))
      X=x-offset[0];Y=y-offset[1]
      for v in range(X+1):
       d=X-v;res=Y-d-3*v
       if res<0 or res%4:continue
       u=res//4
       for run in sorted(set(permutations('D'*d+'V'*v+'U'*u))):
        last=old if not run else run[-1]
        if last not in(('V','U')if A in'FQ'else('U',)):continue
        T=[old]+list(run)+[A,b1,b2];key=tuple(T)
        if key in seen:continue
        seen.add(key);w=''.join(W[a]for a in T)+lit.M;t=lit.trace(w)
        row=dict(old_source=old,foreign=A,first_ordinary=b1,second_ordinary=b2,tokens=T,
            oldcontact=dict(s=[h[0].numerator,h[0].denominator],t=[h[1].numerator,h[1].denominator]),
            exact_N_run_counts=dict(D=d,V=v,U=u),foreign_pose=(x,y,0),result=t)
        rows.append(row)
        if t['feasible']:
         positive.append(row);print('PREPARED_POSITIVE',T,flush=True)
assert boxes==45 and geom==67 and len(rows)==106 and not positive
assert len({tuple(q['tokens'])for q in rows})==106

def raw_owner(T,tick):
 offset=0
 for i,a in enumerate(T):
  if tick<offset+len(W[a]):
   k=tick-offset;canonical=owner.describe(a,k);assert canonical['owner_tick0']==k
   role='old_source_RAW'if i==0 else('first_foreign_RAW'if i==len(T)-3 else('first_returned_RAW'if i==len(T)-2 else('second_returned_RAW'if i==len(T)-1 else'intervening_old_N_RAW')))
   return dict(role=role,actual_raw_name=a,RAW_tick0=k,physical_read_number1=canonical['owner_read_number1'],turn=W[a][k],canonical_literal_owner=canonical)
  offset+=len(W[a])
 k=tick-offset;assert 0<=k<len(lit.M)
 canonical=owner.describe(T[-1],len(W[T[-1]])+k)
 return dict(role='next_actual_word_RAW',actual_raw_name_NOT_assumed=True,RAW_tick0=k,physical_read_number1=canonical['owner_read_number1'],turn=lit.M[k],canonical_literal_owner=canonical)
for q in rows:
 t=q['result'];assert not t['feasible']
 a=raw_owner(q['tokens'],t['previous_read']);b=raw_owner(q['tokens'],t['conflict_read'])
 assert a['turn']==b['turn']==t['turn']
 q['previous_actual_physical_owner']=a;q['later_conflicting_actual_physical_owner']=b
paths=[H/'small_second_ordinary_geometry_manifest.json',R/'audits/check_second_ordinary_small_interface_independent.json',
       R/'seven_word_spatial_return_2026-10-23/first_foreign_first_returned_atom_simplicity_manifest.json',
       R/'seven_word_spatial_return_2026-10-23/complete8_foreign_adjacency_manifest.json',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py']
assert all(p.exists()for p in paths)
out=dict(status='AUTHOR_FROZEN_COMPLETE_ZERO_C_OLD_D_V_SECOND_CONTACT_SLICE_PENDING_REVIEW',
 scope='Only secondordinary FIRST new contacts with old outgoingD/V sources having zero actualCs before firstforeign. Fullsource types necessarilyplainD/V. Exact N-run endpoint exhaustion, no n>=1 or overallsecondsimplicity claim.',
 all45_angle_filtered_exact_contact_boxes=boxrows,
 all67_source_geometry_heads_clear_through_firstordinary=geomrows,
 all106_actual_N_run_whole_word_candidates=rows,
 candidate_counts_by_old_source=dict(Counter(q['old_source']for q in rows)),
 candidate_counts_by_foreign=dict(Counter(q['foreign']for q in rows)),
 no_literal_positive_word_exists_in_this_complete_slice=True,
 U_entry_ancestry_not_inferred_from_prepared_words=True,
 original_outgoing_endpoint_ownership_preserved='old parameter0<=s<1,new0<t<=1;sourceEND belongs to next outgoingoldatom, never reassigned.',
 earlier_U_entry_dependency='Only signed prefix simplicity/firstforeign completepacket last-type constraints. Every whole-word color conflict is immutable for ANY earlier/exterior complete board.',
 all_M11_reads_are_actual_following_word_prefix=True,
 no_postforeign_maturity_or_producer_reset=True,
 dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in paths})
(H/'zero_preforeign_C_old_DV_slice.json').write_text(json.dumps(out,indent=2)+'\n')
print('45 exact angle/contact boxes;67 cleared source geometries;106 actual N-run words,all immutable conflicts.')
print('No prepared positive or U-entry countercontrol in this completezeroC oldD/V slice; n>=1 remainsOPEN.')
