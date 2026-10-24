from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import json,hashlib,math
S=Path(__file__).resolve();R=S.parents[1];D=R/'old_U_arbitrary_ordinary_tail_source_join_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'manifest.json';assert sha(MF)=='907021cf50f9eddedc53333033584e9a86ca4fc750d7731ceb48e320c3d8f817'
for f,h in json.loads(MF.read_text())['files'].items():assert sha(D/f)==h
J=json.loads((D/'source_join.json').read_text())
for f,h in J['dependencies'].items():assert sha(R/f)==h
lib=S.with_name('check_old_V_second_age1_independent.py');n={'__file__':str(lib)};exec(lib.read_text().split('# Universal')[0],n)
W,M,K,tr,rot,center,cross,xy=[n[k]for k in('W','M','K','tr','rot','center','cross','xy')];raw={a:tr(W[a])for a in'DCVU'};ctx={a:tr(W[a]+M)for a in raw}
angles=json.loads((R/'one_foreign_first_contact_compression_2026-10-24/first_contact_C_window.json').read_text())['all44_exact_source_target_C_window_rows'];ua=[r for r in angles if r['source_class']=='preFOREIGN_ordinary'and r['source_atom']=='U'];assert ua==J['all4_signed_arbitrary_tail_old_U_angle_rows']
assert {r['contact_atom']:r['allowed_C_counts_before_contact_ENTRY']for r in ua}=={'D':[1,2,3,4],'C':[1,2,3,4],'V':[1,2,3,4],'U':[1,2,3]}
a=center(0j,0);u=center(raw['U']['p'],0)-a;rows={};boxes=0;parallel=[]
for ar in ua:
 A=ar['contact_atom']
 for k in ar['allowed_C_counts_before_contact_ENTRY']:
  h=(2-k)%4;c=center(0j,h);v=center(rot(h)*raw[A]['p'],(h+raw[A]['h'])%4)-c;den=cross(u,v)
  corners=[(a+s*u-c-t*v)/2 for s in(0,1)for t in(0,1)];bd=[(math.floor(min(p.real for p in corners)),math.ceil(max(p.real for p in corners))),(math.floor(min(p.imag for p in corners)),math.ceil(max(p.imag for p in corners)))];boxes+=1
  rr=next(z for z in J['all15_exact_contact_head_boxes']if z['actor']==A and z['total_ordinary_C_before_actor_ENTRY']==k);assert rr['integer_bounds']==list(map(list,bd))
  for x in range(bd[0][0],bd[0][1]+1):
   for y in range(bd[1][0],bd[1][1]+1):
    if(x+y+h)%2:continue
    p=complex(x,y);q=c+2*p-a
    if den:
     s,t=F(cross(q,v),den),F(cross(q,u),den)
     if not(0<=s<1 and 0<t<=1):continue
    else:
     if cross(q,u):continue
     assert A=='U'and h==0 and v==u
     t=F(-int(q.imag),int(v.imag));s=F(0)
     if not(0<t<=1):continue
     parallel.append((A,x,y,h,k,str(t)))
    bad=[]
    for tag in(0j,1j):
     loc=(tag-p)/rot(h)
     if loc in K or ctx[A]['req'].get(loc)is False:bad.append(xy(tag))
    if bad:route='direct_SAME_LEFT_at_GLOBAL_first_contact_ENTRY'
    elif k==1:route='signed_e366_E1_physical_holes_CORE_inclusive'
    elif k==2:assert(A,p)==('U',-2j);route='signed_2df_N2_physical_deleted_hole_CORE_inclusive'
    elif k==3:route='signed_75c9_W3_PAIR_and_physical_hole_NEW_donor'
    elif A=='V':assert p==4j;route='conditional_0aad_S4V_plus_MANDATORY_1d47_immediate_FOREIGN_adjacency_repair'
    else:assert(A,k,p)==('D',4,2j);route='b224_S4D_coupled_d_arm_bud_reserve'
    rows[A,x,y,h,k]=(str(s),str(t),route)
ref={(r['actor'],*r['ENTRY'],r['total_ordinary_C_before_actor_ENTRY']):(r['old_source_outgoing_s'],r['new_positive_t'],r['route'])for r in J['all50_outgoing_owned_old_U_contact_geometries_and_routes']};assert rows==ref and boxes==15 and len(rows)==50
assert Counter(k[-1]for k in rows)=={1:18,2:8,3:18,4:6}and dict(Counter(v[2]for v in rows.values()))==J['route_counts']
for k,folder,file,key in [(1,'old_U_all_tail_E_hole_guard_2026-10-24','E_holes.json','all18_exact_outgoing_owned_E_geometries'),(2,'old_U_all_tail_N_hole_guard_2026-10-24','N_hole.json','all8_exact_outgoing_owned_N_geometries'),(3,'old_U_all_tail_W_pair_hole_2026-10-24','W_pair_hole.json','all18_exact_outgoing_owned_W_geometries')]:
 old=json.loads((R/folder/file).read_text())[key];assert{(a,x,y,h)for a,x,y,h,kk in rows if kk==k}=={(r['actor'],*r['ENTRY'])for r in old}
# Mandatory C wording qualification is an actual literal check, not just a hash.
P=R/'old_U_all_tail_S_D_coupled_reserve_2026-10-24';assert sha(P/'C_CORE_wording_manifest.json')=='f39355cf0b7c98376216eacb8e59ed438c415a40cac3bce4347343e5e6042700'
for f,h in json.loads((P/'C_CORE_wording_manifest.json').read_text())['files'].items():assert sha(P/f)==h
z=raw['C'];ek={z['p']+rot(z['h'])*q for q in K};assert len(ek-K)==3 and len(ek&K)==2
assert all(ctx['C']['req'][q]is False for q in ek-K)and all(ctx['C']['req'][q]is True for q in ek&K)and all(z['last'][q][0]=='R'for q in ek)
out=dict(status='PASS one-first-FOREIGN arbitrary ordinary-tail old-U SOURCE-CLASS join',manifest=sha(MF),dependencies=J['dependencies'],rational_boxes=boxes,exact_geometry_count=len(rows),heading_counts=dict(Counter(k[-1]for k in rows)),route_counts=J['route_counts'],parallel_positive_onsets=parallel,all50_rows=[dict(actor=k[0],ENTRY=list(k[1:4]),TOTAL_C=k[4],source_s=v[0],actor_t=v[1],route=v[2])for k,v in sorted(rows.items())],analytic=[
'The signed all-length one-FIRST-FOREIGN angle rows restrict total ordinary clock K to1..4 (U actor1..3). Genuine preFOREIGN funding age n is only a nonnegative subcount n<=K, including actual creator UC/UCC own Cs; source clock is its U-base/full-packet ENTRY. No postforeign age reset or fixed suffix index is used.',
'Signed complete early-effect and marker tables exclude firstFOREIGN hits of all four independently CURRENT original star identities at n<=4. Only after complete context MISS and GLOBAL-first stopping is conditional SAME LEFT persistence invoked at actor ENTRY. No LEFT guard is assumed through the actor or after an unexamined consuming foreign.',
'All15 rational boxes and50 actual-sector geometries reconstruct from literal endpoints. Old s=1 belongs to the outgoing successor, not incoming U; new t=0 was already an entry repeat on the preceding executed segment. The codirected parallel U/N2 case is retained at its genuine first overlap onset at old s0, with t>0. No strict nonparallel shortcut or endpoint erasure.',
'The exact E/N/W sets equal their independently signed entire universes. Disjoint count50=37 LEFT+4 E+1 N+6 W+1 S-V+1 S-D holds. Source ownC completion and true fullpacket contexts remain inherited from each actual lane proof, not a fresh post-U G8 reset.',
'S-V uses original0aad only under its actual ordinary-successor condition, plus the independently passed1d47 immediateUF/UQ/UB repair. Original0aad remains incomplete alone and original143d remains rejected; only qualified45abc strict-lower N4 pair scope is imported.',
'S-D uses b224 with8d68 physical SAME-identity internal-cut lift and mandatoryf393 C-site precision. All five C EXIT-CORE cells have final R, but only three external sites are first-WHITE; the other two already lie in ENTRY CORE. Current capture and physical death remain distinct.',
'Conclusion excludes only a preFOREIGN outgoing genuine U-base owner at GLOBAL first ordinary actor contact after exactly one FIRSTFOREIGN and arbitrary finite ordinary RAW suffix with actual M11. Old D/C/V source classes, secondFOREIGN and arbitrary-tail/global simplicity remain open.'
])
S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
