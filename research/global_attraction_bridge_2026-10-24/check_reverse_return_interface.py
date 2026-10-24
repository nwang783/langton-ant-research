"""One initially unread perturbation after a genuine unbounded historical return.
The all-N pre-hit recurrence depends on the retained signed exceptional theorem;
this checker reconstructs its exact layer, verifies causal noninterference,
and proves the new perturbed infinite continuation for every layer count.
"""
import json
from pathlib import Path
from blank_collision_operator import C,H,CP,HP,E,CE,CH,D,multiple,cross
from check_fresh_record_trap_bridge import geometry,replay,verify_tail
P=Path(__file__).parent;cert=json.loads((P/'REVERSE_RETURN_INTERFACE_CERTIFICATE.json').read_text())
A=cert['stable_word'];V=cert['reverse_word'];F=cert['new_post_hit_word'];Z=cert['new_tail_word'];x=(18,-22);d=(-2,-2)
assert len(A)==52262 and len(V)==104 and len(F)==12492 and len(Z)==104
shift=lambda B,v:{(q[0]+v[0],q[1]+v[1])for q in B}
# Reconstruct all finite retained ingredients directly, including the 13-cell
# active pattern and true forward reverse-drift word, not time reversal.
pattern=E&set(HP);assert len(pattern)==13
forward,p,h,_=replay(pattern,CE,CH,H);clean_wake=forward^shift(pattern,d);assert len(clean_wake)==12
RB,rp,rh,_=replay(pattern|{(-39,-20)},CE,CH,A)
RN,np,nh,_=replay(RB,rp,rh,V);assert np==(rp[0]+2,rp[1]+2) and nh==rh
reverse_wake=RN^shift(RB,(2,2));assert len(reverse_wake)==2436
L=shift(clean_wake^shift(reverse_wake,d),(-8,-8));assert len(L)==2438 and L==set(map(tuple,cert['layer']))
# The exceptional theorem is stated at E, whose absolute pose is (-15,10),W.
# Literal controls N0 and N1 verify its all-N formula's endpoints and orientation.
anchors=[];hit_boards={}
for N in(0,1):
 q=(-47-2*N,-28-2*N);preword=C+H*(4+N)+A+V*(14+N)+V[:89]
 B,p,h,events=replay({q},(0,0),0,preword)
 assert len(preword)==64200+208*N and(p,h)==((20,-22),0)
 hit_boards[N]=B
 far_time=9977+104*(4+N)+52262
 far_B,far_p,far_h,_=replay({q},(0,0),0,preword[:far_time])
 assert far_p==(-8-2*N,-57-2*N) and far_h==1
 anchors.append(dict(N=N,historical_hit_time=len(preword),historical_hit_mass=len(B),
                     reverse_entry_time=far_time,reverse_entry_pose=[far_p,far_h],reverse_entry_mass=len(far_B)))
 assert B==set(map(tuple,cert['singleton_anchors'][N]['hit_black']))
 assert far_B==set(map(tuple,cert['singleton_anchors'][N]['far_black']))
assert hit_boards[1]^hit_boards[0]==L
# Initially unread extra cell for ALL N, not only the anchor.
assert x not in CP
assert all((k:=multiple((x[0]-q[0],x[1]-q[1]),d))is None or k<0 for q in HP)
Apos,Aend,Ah=geometry((-23,2),3,A)
assert Aend==(-8,-57) and Ah==1
assert all((k:=multiple((x[0]-q[0],x[1]-q[1]),d))is None or k<0 for q in Apos)
Vpos,Vend,Vh=geometry(Aend,Ah,V);assert Vend==(-6,-55) and Vh==Ah
for i,q in enumerate(Vpos):
 k=multiple((x[0]-q[0],x[1]-q[1]),(2,2))
 assert k is None or k>14 or k==14 and i>=89
# Exact perturbed finite future and all-future tail at N0.
B,p,h,events=replay(hit_boards[0]|{x},(20,-22),0,F)
assert all(tuple(z[1])!=x for z in events[:12])and events[12][1]==list(x)and events[12][3]=='L'
assert(p,h)==((-24,34),0)and len(B)==3674
assert B==set(map(tuple,cert['final_anchor_black']))
T,td,tests=verify_tail(B,p,h,Z);assert td==(-2,2)
# All copies of every actual affine-layer cell miss the complete new future.
Q,qe,qh=geometry((20,-22),0,F)
mins={}
for q in Q:
 key=(q[0]-q[1],q[0]%2);mins[key]=min(mins.get(key,q[0]),q[0])
ray_rows=[]
for b in sorted(L):
 key=(b[0]-b[1],b[0]%2)
 assert key not in mins or mins[key]>b[0]
 for i,q in enumerate(T):
  z=(q[0]-b[0],q[1]-b[1]);det=cross(d,td);kn=cross(z,td);jn=cross(z,d)
  if kn%det or jn%det:continue
  k,j=kn//det,jn//det
  assert k<0 or j<0
 ray_rows.append(dict(cell=b,finite_read_min_x=mins.get(key)))
# Complete field transfer, rather than only matching turns.
for N in(16,64,256):
 row=next(r for r in cert['larger_full_field_controls']if r['N']==N)
 archive=set()
 for j in range(N):archive^=shift(L,(-2*j,-2*j))
 assert (hit_boards[0]^archive)|{x}==set(map(tuple,row['hit_black_with_extra']))
 assert B^archive==set(map(tuple,row['final_black']))
 assert len(B^archive)==3674+24*N
# The full path's transversal range before the chosen certificate is uniform:
# parameter-dependent translations are tangent to n=(1,-1).
all_geometry=CP+HP+Apos+Vpos+Q
normal_range=[min(q[0]-q[1]for q in all_geometry),max(q[0]-q[1]for q in all_geometry)]
assert normal_range==[-82,72]
result=dict(status='AUTHOR all-N scoped theorem; independent audit pending',retained_affine_dependency='OneBlack.Phase.hit_normal',
 original_seed='q_N=(-47-2N,-28-2N) plus (18,-22), N>=0',
 anchors=anchors,initial_extra_first_read='64212 + 208N',
 new_standard_certificate_time='76692 + 208N',final_pose=[(-24,34),0],final_drift=(-2,2),
 final_mass='3674 + 24N',complete_archive_layer_size=len(L),infinite_layer_ray_checks=ray_rows,
 infinite_tail_parity_tests=tests,uniform_pre_certificate_transversal_range=normal_range,
 uniform_bad_pristine_record_time_cut_bound=9977+52262+12492+3*375,
 standard_piece_count=3,arbitrary_piece_total_length=9977+52262+12492,
 no_minimal_onset_claim=True,no_universal_two_cell_record_budget_claim=True)
(P/'REVERSE_RETURN_INTERFACE_CHECKED.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(dict(layer_size=len(L),all_N_extra_unread=True,certificate='76692+208N',bad_pristine_bound=result['uniform_bad_pristine_record_time_cut_bound'])))
