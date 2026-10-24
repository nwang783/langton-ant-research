"""Finite-to-geometric exactly THREE immediate ordinary RAW assembly.

The original831 angle keys and all actual oldD source/nextFULL masks are
compared directly. No new prefix search and no automatic tail induction.
"""
from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
import importlib.util,json,hashlib
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent
s=importlib.util.spec_from_file_location('l',R/'word_stabilization/check_foreign_return_interfaces.py');l=importlib.util.module_from_spec(s);s.loader.exec_module(l)
s=importlib.util.spec_from_file_location('o',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py');o=importlib.util.module_from_spec(s);s.loader.exec_module(o);W=o.WORDS
read=lambda p:json.load(open(R/p))
J=read('third_ordinary_local_interface_2026-10-24/third_local_interface.json')
D=read('old_D_third_young_endpoint_2026-10-24/D_third_young_endpoint.json')
D3=read('old_D_third_age3_beta_loss_2026-10-24/D_third_age3_beta_loss.json')
C=read('third_old_C_monotone_reserves_2026-10-24/old_C_third_closure.json')
U=read('old_U_third_source_join_2026-10-24/U_third_join.json')
V01=read('old_V_third_young_complete_ancestry_2026-10-24/young_ancestry.json')
V2=read('old_V_third_age2_genuine_field_2026-10-24/age2_field.json')
V34=read('V_postforeign_pair_rail_reserve_2026-10-24/pair_rail_reserve.json')
VJOIN=read('old_V_third_source_join_2026-10-24/V_third_join.json')

def add(p,q):return p[0]+q[0],p[1]+q[1]
def sub(p,q):return p[0]-q[0],p[1]-q[1]
def det(p,q):return p[0]*q[1]-p[1]*q[0]
def raw(T):return ''.join(W[a]for a in T)
def after(w,p=(0,0,0)):
 q,h=p[:2],p[2]
 for a in w:h=(h+(1 if a=='R'else-1))%4;q=add(q,l.DIRS[h])
 return *q,h
def z(p):return add((2*p[0],2*p[1]),l.rot((-1,-1),p[2]))
def hit(a,b,c,d):
 u,v,zz=sub(b,a),sub(d,c),sub(c,a);den=det(u,v)
 if den:
  ss,tt=Q(det(zz,v),den),Q(det(zz,u),den)
  return dict(old_s=ss,new_t=tt,kind='point')if 0<=ss<=1 and 0<=tt<=1 else None
 if det(zz,u):return None
 k=0 if v[0]else 1;lo,hi=sorted((Q(a[k]-c[k],v[k]),Q(b[k]-c[k],v[k])));lo,hi=max(Q(0),lo),min(Q(1),hi)
 if lo>hi:return None
 pt=tuple(Q(c[k])+lo*v[k]for k in(0,1));j=0 if u[0]else 1;ss=Q(pt[j]-a[j],u[j])
 return dict(old_s=ss,new_t=lo,new_t_upper=hi,kind='collinear')
def qjson(x):
 if isinstance(x,Q):return[x.numerator,x.denominator]
 if isinstance(x,dict):return{k:qjson(v)for k,v in x.items()}
 if isinstance(x,(tuple,list)):return[qjson(v)for v in x]
 return x

local=[];bad=[]
for h in range(4):
 for A in'FQB':
  p=(0,0,h);f=after(W['F'],p);e=after(W[A],p);vv=[z(p),z(f)];labels=['F56prefix']
  if A!='F':vv.append(z(e));labels.append(A+'tail')
  for b1 in'DCVU':
   for b2 in'DCVU':
    for b3 in'DCVU':
     v=list(vv);p=e
     for j,b in enumerate((b1,b2,b3)):p=after(W[b],p);v.append(z(p))
     segs=list(zip(v,v[1:]));new=segs[-1];contacts=[]
     adj=hit(*segs[-2],*new);assert adj['old_s']==1 and adj['new_t']==0
     if adj['kind']=='collinear':assert adj['new_t_upper']==0
     for j,old in enumerate(segs[:-2]):
      hh=hit(*old,*new)
      if hh:
       # A positive collinear overlap already at the new entry would violate
       # the executed two-RAW prefix; in fact none occurs among these types.
       assert not(hh['kind']=='collinear'and hh['new_t']==0 and hh['new_t_upper']>0)
       if hh['new_t']>0:contacts.append((hh['new_t'],j,hh))
     rec=dict(heading=h,foreign=A,first=b1,second=b2,third=b3,true_piece_vertices=v,adjacent_b2_only_at_actual_endpoint=True)
     if contacts:
      t,j,hh=min(contacts,key=lambda x:x[0]);owner=j+1 if hh['old_s']==1 else j
      T=A+b1+b2+b3;tr=l.trace(raw(T)+l.M);assert not tr['feasible'] and tr['conflict_read']<len(raw(T))
      rec.update(first_local_contact_time=t,outgoing_owner_index0=owner,immutable_RAW_conflict=tr);bad.append(rec)
     local.append(rec)
assert len(local)==768 and len(bad)==16
assert Counter((r['foreign'],r['first'],r['second'],r['third'])for r in bad)=={('F','C','C','V'):4,('F','C','C','U'):4,('Q','C','C','U'):4,('B','C','C','U'):4}
marker=[]
for b1 in'DCVU':
 for b2 in'DCVU':
  for b3 in'DCVU':
   fine=raw(b1+b2+b3)+l.M
   assert fine[len(W[b1]):len(W[b1])+11]==l.M
   assert fine[len(W[b1])+len(W[b2]):len(W[b1])+len(W[b2])+11]==l.M
   marker.append(dict(first=b1,second=b2,third=b3,b1_context_supplied_by_actual_b2_b3=True,two_RAW_terminal_context_supplied_by_actual_b3_and_if_D10_one_real_next_read=True))
assert len(marker)==64

# Direct original831 IDs, not previous217 IDs, coarse first-return label15,
# historical D14 parent counts, D28 role counts, or counts of contact positions.
a=J['all831_conditional_preFOREIGN_old_source_angle_interfaces']
def ak(x):return json.dumps(x,sort_keys=True)
assert len(a)==len({ak(x)for x in a})==831
oldC=[x['exact_original_angle']for x in C['all160_exact_original_C_angle_boxes']]
oldU=U['all236_signed_old_U_angle_rows']
oldV=[x['angle']for x in V01['all101_signed_angle_boxes']]+[x['angle']for x in V2['all62_signed_angle_contact_boxes']]+V34['all66_signed_angle_cases']
assert {ak(r['angle'])for r in VJOIN['all229_exact_V_angle_routes']}=={ak(x)for x in oldV}
for old,claimed in [('C',oldC),('U',oldU),('V',oldV)]:
 assert len(claimed)==len({ak(x)for x in claimed})
 assert {ak(x)for x in claimed}=={ak(x)for x in a if x['old_source']==old}

def dk(r):return(r['n'],r['b1'],r['b2'],r['b3'],r['A'],tuple(r['pa']),tuple(r['p3']),r['source'],r['nextfull'])
assert len(D['typed_rows'])==len({dk(r)for r in D['typed_rows']})==7911
assert {dk(r)for r in D['typed_rows']if r['n']==3}=={dk(r)for r in D3['typed_rows']}
assert len(D3['typed_rows'])==1458 and len(D3['remaining_physical_targets'])==18
assert Counter(r['why']for r in D3['typed_rows'])=={'CURRENT_cut':1296,'NECESSARY':162}
assert not any(r['why']=='NECESSARY'and r['n']==2 for r in D['typed_rows'])
assert len(D['whole_words'])==3757 and sum(r['feasible']for r in D['whole_words'].values())==326
assert len(D['reverse_closed_nodes'])==652 and len(D['complete_reverse_relation'])==5216
roles={(r['source'],r['nextfull'])for r in D['typed_rows']}
assert roles=={('DC',None)}|{('D',x)for x in('D','DC','V','VC','VCC','U','UC','UCC')}

routes=[]
for i,x in enumerate(a):
 old=x['old_source'];n=x['true_old_source_ENTRY_to_FOREIGN_ENTRY_C_age']
 assert n+x['first_returned_C_indicator']+x['second_returned_C_indicator']==x['total_ordinary_C_before_third']
 if old=='D':proof='old_D_third_age3_beta_loss'if n==3 else'old_D_third_young_endpoint'
 elif old=='C':proof='third_old_C_monotone_reserves'
 elif old=='U':proof='old_U_third_source_join'
 else:proof='old_V_third_young_complete_ancestry'if n<=1 else('old_V_third_age2_genuine_field'if n==2 else'V_postforeign_pair_rail_reserve WITH simultaneous-input qualification')
 routes.append(dict(original831_angle_index0=i,exact_original_angle=x,source_exclusion=proof))
assert Counter(x['old_source']for x in a)=={'D':206,'C':160,'V':229,'U':236}

out=dict(status='AUTHOR_FROZEN_ALL_SOURCE_DEPENDENCIES_INDEPENDENTLY_PASSED_PENDING_FINAL_GEOMETRIC_REVIEW',theorem='An actual U-entry complete-eight prefix, FIRST F/Q/B, and exactly THREE immediate ordinary RAW atoms with actual finalM11 have a SIMPLE OPEN corrected-center proxy through the third RAW exit.',
 all768_rotation_checked_local_closed_segment_interfaces=qjson(local),all16_rotated_local_contacts_fail_in_actual_RAW=qjson(bad),all64_actual_context_supply_cases=marker,all831_original_angle_IDs_and_exact_source_exclusions=routes,
 exact_source_angle_counts=dict(Counter(x['old_source']for x in a)),direct7911_genuine_old_D_source_nextFULL_keys=[list(dk(r))for r in D['typed_rows']],direct1458_old_D_age3_keys=[list(dk(r))for r in D3['typed_rows']],
 finite_to_geometric_bridge='The already-actual two-RAW prefix is simple using b3 plus the real finalM as its following context. Local closed intersections remove true foreign and b1 contacts and leave b2 actual adjacency. Any first positive remaining contact has an outgoing genuine old D/C/V/U owner, with s in[0,1), t in(0,1]; foreign-entry terminal is already locally covered. The repaired first-contact Jordan lift yields one of the unchanged831 exact keys. Every source slice excludes it, so no third contact exists.',
 physical_CORE_qualification='CURRENT external absence is not physical death: an original BLACK identity can remain alive in CORE. Only actual CURRENT/core conflicts or exact first-WHITE requirements are used. No old-eight age law crosses the foreign.',
 positive_controls_and_withdrawn_claims='All signed prepared positive controls remain real. Natural reverse closures exclude only eligible U-entry factors containing the selected old source, not later internal U. Genuine UQVCCV/UBVCCV fourth-atom CORE erosion remains real. False full-output seal6ea48d5 remains withdrawn; no automatic finite-state or spending claim.',
 no_fourth_RAW_full_later_tail_second_foreign_fine_walk_selfavoidance_global_language_coverage_or_capture=True)
(H/'three_ordinary_simplicity.json').write_text(json.dumps(out,indent=2)+'\n')
print('768 rotated local checks /16 RAW conflicts /64 actual context supplies; original831 source IDs covered D206+C160+V229+U236.')
print('D7911 full-role keys and D3 exact1458 subset agree. All source dependencies are passed; final geometric review is separate. No fourth or secondforeign extension.')
