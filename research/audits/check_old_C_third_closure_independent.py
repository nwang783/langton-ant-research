from pathlib import Path
from itertools import product
from fractions import Fraction as F
from collections import Counter
import json,hashlib,math
S=Path(__file__);R=S.parents[1];D=R/'third_old_C_monotone_reserves_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(D/'manifest.json')=='ab2565a276109a4828e65f869fc3336e0ff191d5e102c3019e8a3e25f137a3fd'
ma=json.loads((D/'manifest.json').read_text())
for f,h in ma['files'].items():assert sha(D/f)==h
for f,h in ma['dependencies'].items():assert sha(R/f)==h
J=json.loads((D/'old_C_third_closure.json').read_text());C=json.loads((R/'second_old_C_age3_2026-10-24/C_age3_source_reserve.json').read_text())
ns={'__file__':str(S.with_name('check_old_V_second_age1_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Universal')[0],ns)
W,M,K,tr,G,rot,center,cross,xy,meet=[ns[k]for k in('W','M','K','tr','G','rot','center','cross','xy','meet')];raw=lambda seq:''.join(W[a]for a in seq)
roles={(r['actual_full'],r['selected_C_index1']):r for r in C['all7_genuine_C_roles_and18_same_identity_source_reserves']};qu=C['all1794_exact_source_output_consumer_queries'];subsets=[]
for key,role in roles.items():
 full,j=key;src=tr(raw(full));before=tr(raw(full[0]+'C'*(j-1)));tau=1-j
 assert role['actual_full_ENTRY_clock']==tau and role['actual_full_completion_clock']==tau+full.count('C')
 for q in role['selected_reserves']:
  cell=complex(*q['full_output_slot']);assert src['last'][cell]==('R',q['actual_last_R_tick0']);assert xy((cell-before['p'])/rot(before['h']))==q['normalized_selected_C_cell']
 for n in(1,2,3):
  deadline=n-tau;valid=role['actual_full_completion_clock']<=n;got=[]
  if valid:
   for reserve in role['selected_reserves']:
    for k in reserve['all_query_indices']:
     q=qu[k]
     if q['actual_full_source_age']<=deadline and q['consumer_full_completion_age']<=deadline:
      assert q['exclusion']!='consumer_full_cannot_complete_before_actual_FOREIGN_entry';got.append(k)
  ref=next(v for v in J['all21_actual_full_role_deadline_subset_certificates']if(v['actual_full_source'],v['selected_C_index1'],v['true_atomic_preFOREIGN_age'])==(full,j,n))
  assert got==ref['exact_subset_of_signed_max_deadline_query_indices']and valid==ref['source_fully_completed_before_FOREIGN']
  subsets.append((full,j,n,deadline,valid,len(got)))
angles=[v for v in json.loads((R/'third_ordinary_local_interface_2026-10-24/third_local_interface.json').read_text())['all831_conditional_preFOREIGN_old_source_angle_interfaces']if v['old_source']=='C']
assert len(angles)==160
a=center(0,0);b=center(G['C']['p'],G['C']['h']);geos=[];rows=[]
for ai,g in enumerate(angles):
 n=g['true_old_source_ENTRY_to_FOREIGN_ENTRY_C_age'];N=g['total_ordinary_C_before_third'];b1,b2,b3=(g[k]for k in('first','second','third'));h=g['third_heading_relative_old'];assert N==n+(b1+b2).count('C')and h==(2-N)%4
 c=center(0,h);d=center(G[b3]['p']*rot(h),(G[b3]['h']+h)%4);v=d-c;u=b-a;den=cross(u,v)
 corners=[(a+s*u-c-t*v)/2 for s,t in product((0,1),repeat=2)]
 for x in range(math.floor(min(z.real for z in corners)),math.ceil(max(z.real for z in corners))+1):
  for y in range(math.floor(min(z.imag for z in corners)),math.ceil(max(z.imag for z in corners))+1):
   if(x+y+h)%2:continue
   p3=complex(x,y);z=c+2*p3-a
   if den:
    s,t=F(cross(z,v),den),F(cross(z,u),den)
    if not(0<=s<1 and 0<t<=1):continue
   else:
    if cross(z,u):continue
    co=lambda z:int(z.real)if u.real else int(z.imag)
    q,mul=F(co(z),co(u)),F(co(v),co(u));assert mul>0
    if q>=0:continue
    s,t=F(0),-q/mul
    if not 0<t<=1:continue
   geos.append((ai,(x,y,h),s,t))
   for A in'FQB':
    ha=(-n)%4;delta=tr(raw(A+b1+b2),h=ha);pa=p3-delta['p'];assert delta['h']==h
    # Every executed foreign bend and earlier returned piece, at actual cuts.
    z=tr(W['F'],pa,ha);verts=[center(pa,ha),center(z['p'],z['h'])]
    if A!='F':z=tr(W[A],pa,ha);verts.append(center(z['p'],z['h']))
    for at in(b1,b2):z=tr(W[at],z['p'],z['h']);verts.append(center(z['p'],z['h']))
    assert z['p']==p3
    early=any(meet(a,b,c,d)is not None for c,d in zip(verts,verts[1:]));ctx=tr(raw(A+b1+b2+b3)+M)
    for(role,j),rr in roles.items():
     cuts=[]
     if rr['actual_full_completion_clock']>n:why='source_uncompleted'
     elif early:why='earlier_contact'
     elif ctx['bad']:why='local_immutable'
     else:
      for reserve in rr['selected_reserves']:
       q=complex(*reserve['normalized_selected_C_cell']);local=(q-pa)/rot(ha)
       if local in K or ctx['req'].get(local)is False:cuts.append(tuple(xy(q)))
      why='signed_current_cut'if cuts else'NECESSARY'
     rows.append(dict(role=(role,j),n=n,b1=b1,b2=b2,b3=b3,A=A,pa=(*xy(pa),ha),p3=(x,y,h),why=why,cuts=cuts))
assert len(geos)==225 and len(rows)==4725
assert set(geos)=={(v['local_C_angle_index0'],tuple(v['third_pose']),F(*v['old_s']),F(*v['new_t']))for v in J['all225_outgoing_owned_contact_poses']}
def key(r):return(tuple(r['role']),r['n'],r['b1'],r['b2'],r['b3'],r['A'],tuple(r['pa']),tuple(r['p3']))
refrows={key(r):r for r in J['all4725_actual_containing_role_foreign_masks']};assert len(refrows)==4725
cnt=Counter()
for r in rows:
 ref=refrows[key(r)];assert r['why']==ref['why']and set(r['cuts'])==set(map(tuple,ref['cuts']));cnt[r['why']]+=1
assert dict(cnt)==J['exact_initial_guard_classification'];assert all(r['why']=='signed_current_cut'for r in rows if r['n']==3)
def perms(d,v,u):
 if not d+v+u:return ['']
 ans=[]
 if d:ans+=['D'+s for s in perms(d-1,v,u)]
 if v:ans+=['V'+s for s in perms(d,v-1,u)]
 if u:ans+=['U'+s for s in perms(d,v,u-1)]
 return ans
words={};tuples=[];empty=0
for r in rows:
 if r['why']!='NECESSARY':continue
 full,j=r['role'];n=r['n'];x,y,h=r['pa'];models=[]
 if n==1:
  assert h==3
  for v in range(max(y,0)):
   d=y-1-v;rem=-x-d-3*v
   if rem>=0 and rem%4==0 and d+v+rem//4>0:models.append((0,0,0,d,v,rem//4))
 else:
  assert n==2 and h==2;B=-1-x
  # x is a nonnegative budget: enumerate W-U, W-V, S-V, W-D; solve S-D.
  for uw in range(max(0,B//4+1)):
   for vw in range(max(0,(B-4*uw)//3+1)):
    for vs in range(max(0,B-4*uw-3*vw+1)):
     for dw in range(max(0,B-4*uw-3*vw-vs+1)):
      ds=B-4*uw-3*vw-vs-dw
      if(full in('VCC','UCC')and j==1)!=(dw+vw+uw==0):continue
      rem=1+dw+vw-ds-3*vs-y
      if rem>=0 and rem%4==0 and ds+vs+rem//4>0:models.append((dw,vw,uw,ds,vs,rem//4))
 ref=refrows[key(r)];rid=ref['typed_role_mask_index0'];given=[]
 for k in ref['all_exact_endpoint_count_tuple_indices']:
  t=J['all1614_remaining_exact_endpoint_count_tuples'][k];assert t['typed_role_mask_index0']==rid
  given.append(tuple(t[c][a]for c in('first_rail_counts','final_rail_counts')for a in'DVU'))
 assert set(models)==set(given)and len(models)==len(given);tuples.extend(models);ks=set()
 for dw,vw,uw,ds,vs,us in models:
  for X,Y in product(perms(dw,vw,uw),perms(ds,vs,us)):
   if Y[-1]not in('VU'if r['A']in'FQ'else'U'):continue
   before=full[0]+'C'*(j-1);tail='C'+(X+'C'if n==2 else'')+Y;old=before+tail;seq=old+r['A']+r['b1']+r['b2']+r['b3'];wk=(full,j,n,seq);ks.add(wk)
   entry=tr(raw(before));p=tr(raw(old));assert (*xy((p['p']-entry['p'])/rot(entry['h'])),(p['h']-entry['h'])%4)==tuple(r['pa'])
   p=tr(raw(old+r['A']+r['b1']+r['b2']));assert (*xy((p['p']-entry['p'])/rot(entry['h'])),(p['h']-entry['h'])%4)==tuple(r['p3'])
   assert tail.count('C')==n and seq.startswith(full)
   if wk not in words:
    z=tr(raw(seq)+M);assert z['bad']and z['bad'][0]<len(raw(seq));words[wk]=z['bad']
 assert ks==set(map(tuple,ref['all_ordered_valid_last_packet_word_keys']));empty+=not ks
assert len(tuples)==1614 and len(words)==10152 and max(map(sum,tuples))==10 and empty==14
sup=J['all10152_ordered_genuine_full_source_word_conflicts'];assert set(words)=={(v['actual_full_source'],v['selected_C_index1'],v['true_atomic_preFOREIGN_age'],''.join(v['tokens']))for v in sup}
for r in sup:
 seq=''.join(r['tokens']);bad=words[r['actual_full_source'],r['selected_C_index1'],r['true_atomic_preFOREIGN_age'],seq]
 assert bad[:2]==(r['immutable_conflict']['conflict_read'],r['immutable_conflict']['previous_read'])
 for tt,k in((bad[0],'later_actual_owner'),(bad[1],'previous_actual_owner')):
  off=0
  for ai,a in enumerate(seq):
   if tt<off+len(W[a]):assert r[k]['actual_atom_index0']==ai and r[k]['actual_atom']==a and r[k]['canonical']['context_tick0']==tt-off;break
   off+=len(W[a])
out=dict(status='PASS old-C chronological FIRST THIRD-RAW source closure only',manifest=sha(D/'manifest.json'),angles=160,outgoing_owned_poses=225,roles=7,role_deadline_subsets=subsets,mask_classification=dict(cnt),exact_count_tuples=1614,derived_maximum_rail_atoms=10,ordered_full_source_cases=10152,no_solution_obligations=14,analytic_review=[
'Signed complete-boundary age3 reserve proof restricts to earlier actual foreign deadlines by exact query subset. Real full source completion is retained, including C2 full-entry shift -1 and unfinished double-tail C1 at true age1. No hypothetical extension to a later history is used.',
'All160 signed angular interfaces and all225 exact rational outgoing-owned contact heads independently rebuilt, including parallel first positive onset. Earlier real foreign/first/second contacts invalidate first-third contact. All4725 containing-role masks are reconstructed; only guaranteed SAME external CURRENT facts test entryK/firstWHITE, not unresolved physical identity death.',
'Age1 W and age2 W/C/S endpoint equations give finite NONNEGATIVE coordinate budgets. Mandatory ownC2 makes first W rail empty exactly for nonfinal double-tail C1; every other real producer needs a nonempty base before an additional C. Last actual V/U foreign rule and nonempty final rail retained.',
'Independent alternate count loop/all-order enumeration matches all1614 tuples and10152 full-source word keys. Every complete containing source is literally present, selected-C frame/actual foreign/third poses and atomic clocks replayed. All immutable conflicts occur inside RAW, with both actual owners rechecked.',
'Only preforeign old C can no longer own the stipulated first new third contact. Old D/V/U, third simplicity, arbitrary-tail induction, another foreign and language coverage are not concluded.'
]);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
