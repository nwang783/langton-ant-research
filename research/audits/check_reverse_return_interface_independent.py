from pathlib import Path
from collections import defaultdict
import json,hashlib
S=Path(__file__);R=S.parent.parent;P=R/'global_attraction_bridge_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();mf=P/'REVERSE_RETURN_INTERFACE_MANIFEST.json';m=json.loads(mf.read_text())
for f,h in m['files'].items():assert sha(P/f)==h
for f,h in m['retained_sources'].items():assert sha(R/f)==h
bp=S.with_name('check_tangential_cap_capture_independent.py');ns={'__file__':str(bp)};exec(bp.read_text().split('seed=set')[0],ns);geom,replay,tail,mul,cross,cx,xy=[ns[k]for k in('geom','replay','tail','mul','cross','cx','xy')]
z=json.loads((P/'REVERSE_RETURN_INTERFACE_CERTIFICATE.json').read_text());ref=json.loads((P/'REVERSE_RETURN_INTERFACE_CHECKED.json').read_text());bd=json.loads((P/'PRISTINE_COHORT_ADVANCE_CHECKED.json').read_text());C,H=bd['blank_prefix'],bd['blank_tail_word'];A,V,F,Z=[z[k]for k in('stable_word','reverse_word','new_post_hit_word','new_tail_word')];assert list(map(len,(C,H,A,V,F,Z)))==[9977,104,52262,104,12492,104];rots={H[i:]+H[:i]for i in range(104)};assert V in rots and Z in rots
E,ce,ch,CP=replay(set(),0j,0,C);HP,dd,htest=tail(E,ce,ch,H);d=-2-2j;assert(ce,ch,len(E),dd)==(-15+10j,3,715,d);pattern=E&{q for q,_,_ in HP};assert len(pattern)==13
shift=lambda B,v:{q+v for q in B};mask=lambda rr:{q for q in{q for q,_,_ in rr}if sum(p==q for p,_,_ in rr)%2}
FH,fp,fh,_=replay(pattern,ce,ch,H);CW=FH^shift(pattern,d);assert len(CW)==12
RB,rp,rh,AR=replay(pattern|{-39-20j},ce,ch,A);RN,np,nh,_=replay(RB,rp,rh,V);assert(np-rp,nh)==(-d,rh);RW=RN^shift(RB,-d);assert len(RW)==2436;L=shift(CW^shift(RW,d),4*d);assert len(L)==2438 and L==set(map(cx,z['layer']))
# Reconstruct the actual forward source chart and retained all-N theorem's layer convention.
AP,ae,ah=geom(A,-23+2j,3);VP,ve,vh=geom(V,ae,ah);assert(ae,ah,ve,vh)==(-8-57j,1,-6-55j,1);MH=mask(HP);MA=mask(AP);assert len(MH)==32
x=18-22j;anchors=[];hitboards={};farboards={}
for N,row in enumerate(z['singleton_anchors']):
 assert N in(0,1);q=-47-28j+N*d;pre=C+H*(4+N)+A+V*(14+N)+V[:89];B,p,h,rr=replay({q},0j,0,pre);assert len(pre)==64200+208*N and(p,h)==(20-22j,0);hitboards[N]=B
 farword=C+H*(4+N)+A;BF,pf,hf,_=replay({q},0j,0,farword);assert(pf,hf)==(-8-57j+N*d,1);farboards[N]=BF
 formula={q}^E^shift(MA,N*d)
 for j in range(4+N):formula^=shift(MH,j*d)
 assert formula==BF and B==set(map(cx,row['hit_black']))and BF==set(map(cx,row['far_black']));anchors.append(dict(N=N,hit_mass=len(B),far_mass=len(BF),far_time=len(farword)))
assert len(hitboards[0])==3145 and hitboards[1]^hitboards[0]==L
# Exact all-N first-read domains: forward/scatter nonnegative, reverse includes EVERY negative copy.
assert all(q!=x for q,_,_ in CP)
for rr,v in((HP,d),(AP,d)):
 for q,_,_ in rr:assert(k:=mul(x-q,v))is None or k<0
reverse_hits=[]
for i,(q,_,_)in enumerate(VP):
 k=mul(x-q,-d)
 if k is not None:reverse_hits.append([i,k]);assert k>14 or k==14 and i>=89
BF,pf,hf,FR=replay(hitboards[0]|{x},20-22j,0,F);assert(pf,hf,len(BF))==(-24+34j,0,3674)and BF==set(map(cx,z['final_anchor_black']));assert next((i,h,ch)for i,(q,h,ch)in enumerate(FR)if q==x)==(12,2,'L');ZT,zd,nt=tail(BF,pf,hf,Z);assert zd==-2+2j
# Complete finite-read ray closure and all future phase-ray intersections.
mins={}
for q,_,_ in FR:
 key=(int(q.real-q.imag),int(q.real)%2);mins[key]=min(mins.get(key,int(q.real)),int(q.real))
rays=[]
for b in L:
 key=(int(b.real-b.imag),int(b.real)%2);assert key not in mins or mins[key]>b.real
 for q,_,_ in ZT:
  delta=q-b;den=cross(d,zd);kn,jn=cross(delta,zd),cross(delta,d)
  if kn%den or jn%den:continue
  k,j=kn//den,jn//den;assert k<0 or j<0
 rays.append((xy(b),mins.get(key)))
assert len(rays)==2438
# Additional supplied controls are independently FULL physical replays, not formula-only comparisons.
large=[]
for row in z['larger_full_field_controls']:
 N=row['N'];assert N in(16,64,256);q=-47-28j+N*d;pre=C+H*(4+N)+A+V*(14+N)+V[:89];B,p,h,rr=replay({q,x},0j,0,pre);assert(p,h)==(20-22j,0)and all(a!=x for a,_,_ in rr);archive=set()
 for j in range(N):archive^=shift(L,j*d)
 assert B==hitboards[0]^archive^{x}==set(map(cx,row['hit_black_with_extra']));FF,pp,hh,ffr=replay(B,p,h,F);assert FF==BF^archive==set(map(cx,row['final_black']))and(pp,hh)==(pf,hf);assert len(FF)==3674+24*N;large.append(dict(N=N,full_replayed_updates=len(pre)+len(F),hit_mass=len(B),final_mass=len(FF)))
normal=[int(q.real-q.imag)for q,_,_ in CP+HP+AP+VP+FR];assert(min(normal),max(normal))==(-82,72)
# All-N cardinality is from literal turn balance, NOT extrapolation of finite mass samples.
imb=lambda w:w.count('R')-w.count('L');assert imb(H)==imb(V)==12
base_mass=2+imb(C)+4*imb(H)+imb(A)+14*imb(V)+imb(V[:89])+imb(F);assert base_mass==3674
assert 9977+52262+12492+3*375==75856
out={'status':'PASS exact causal two-cell all-N reverse-return perturbation captures with all archives retained','manifest_sha256':sha(mf),'dependencies':m,'anchors':anchors,'large_independent_full_replays':large,'clean_wake_size':12,'reverse_wake_size':2436,'affine_layer_size':2438,'reverse_first_read_possible_ray_indices':reverse_hits,'new_continuation_length':12492,'actual_extra_first_read_offset':12,'final_pose':[xy(pf),hf],'tail_drift':xy(zd),'tail_exact_parity_tests':nt,'mass_identity':{'base':base_mass,'per_parameter':imb(H)+imb(V)},'all_future_unread_layer_rays':2438,'uniform_transversal_range':[-82,72],'family_only_bad_pristine_timecuts':75856,'analytic_review':['Retained exceptional one-black theorem is an explicit premise: phaseHead=base(-15,10)+(-2,-8)=(-17,2), actual depth15+N, pristine depth11, lag4, localTime52262, hitCycles10, hitPhase89. Its pre_hit_exact and hit_normal concern true FORWARD ant dynamics and full XOR fields, not time reversal or an arbitrary unproved two-black classification. Sources and formulas were inspected directly.','The pristine13-field A replay and actual N0/N1 whole boards independently reconstruct cleanWake12, reverseWake2436 and L=(cleanWake XOR(reverseWake+d))+4d, exactly the formal source layer. Actual far endpoint fields are checked against the full initial-obstacle/E/M_H/M_A XOR expression, not active-support cropping. Historical-hit formula is the retained all-N theorem, with two independent anchor checks of orientation and layer.','Extra x is absent from blankC, every H phase ray with nonnegative copy, every A+Nd footprint and the ENTIRE reverse domain k<14 or k=14,phase<89, including arbitrarily negative k. Hence adding it at timezero preserves the full pre-hit orbit for everyN. Actual x read12 later is headingS/L; no late field edit.','Fresh12492 full physical continuation from B_hit XOR{x} and exact canonical104 infinite future are verified. All2438 L rays with nonnegative copy avoid every finite read and every nonnegative future phase ray. Thus all accumulated layers, including overlaps/cancellations, remain unread and the complete final field transfers. N16/64/256 supplied whole boards are additionally physically replayed, not used as all-N proof.','The all-N mass3674+24N follows directly from two extra standard blocks each R-L=12, after full word validity is established. Precertificate transverse range[-82,72] is invariant under parameter shifts along(-2,-2); final drift changes that normal and its later records are standard, not nonstandard progress.','Arbitrary pieces9977+52262+12492 plus THREE canonical standard pieces give75856 bad pristine TIME cuts only for this exact two-cell family. No earliest onset, arbitrary two-cell uniform bound, recurring amplifier, or universal attraction claim.']};S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S),sha(S.with_suffix('.json')))
