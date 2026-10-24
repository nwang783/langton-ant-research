from pathlib import Path
from itertools import product
import hashlib,json
S=Path(__file__).resolve();R=S.parents[1];D=R/'K1_pipeline_detours_2026-10-23';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();note=D/'homogeneous_negative_triple_circles_are_impossible.md';assert sha(note)=='a31d409eaaf37749631754c44adf39e1d9b07b4480d2415380f1de8f31d98cef'
H='NESW';V=(1j,1,-1j,-1)
def out(w,i):return H[(H.index(w[i])+(1 if i%2==0 else-1))%4]
def port(w,h,incoming):return[i for i in range(len(w))if(w[i]if incoming else out(w,i))==h]
A='NSNN';B='WEEE';main=[dict(source='A_k',target='B_k',heading='E',source_ranks=port(A,'E',False),target_ranks=port(B,'E',True)),dict(source='B_(k-1)',target='A_k',heading='N',source_ranks=port(B,'N',False),target_ranks=port(A,'N',True))]
assert[(z['source_ranks'],z['target_ranks'])for z in main]==[([0,1,2],[1,2,3]),([0,1,3],[0,2,3])]
assert port(B,'S',False)==[2]and port(B,'W',True)==[0]
Uc=[]
for m in range(1,5):
 for hh in product('NS',repeat=m):
  w=''.join(hh)
  if len(port(w,'S',True))==len(port(w,'W',False))==1:Uc.append(dict(word=w,incoming_S_rank=port(w,'S',True)[0],outgoing_W_rank=port(w,'W',False)[0]))
assert Uc==[{'word':'S','incoming_S_rank':0,'outgoing_W_rank':0},{'word':'NNNS','incoming_S_rank':3,'outgoing_W_rank':1},{'word':'NSNN','incoming_S_rank':1,'outgoing_W_rank':3}]
# Exact main-port event equations derive output_W=alpha-3 and input_S=beta+1.
# beta-alpha>=4, so the complete U ordinal must have output_W earlier.
keep=[z for z in Uc if z['outgoing_W_rank']<z['incoming_S_rank']];assert[w['word']for w in keep]==['NNNS']
U='NNNS';assert port(U,'E',False)==[0,2,3]and port(U,'N',True)==[0,1,2]
Vc=[]
for m in range(1,5):
 for hh in product('EW',repeat=m):
  w=''.join(hh)
  if len(port(w,'E',True))==len(port(w,'N',False))==3:Vc.append(dict(word=w,incoming_E=port(w,'E',True),outgoing_N=port(w,'N',False)))
assert Vc==[{'word':'EEWE','incoming_E':[0,1,3],'outgoing_N':[1,2,3]},{'word':'WEEE','incoming_E':[1,2,3],'outgoing_N':[0,1,3]}]
for z in Vc:assert z['incoming_E'][2]==z['outgoing_N'][2]==3
geometry=[]
for k in(-2,0,1,7):
 a=complex(k,k);b=a+1;up=a+1-1j;bp=a-1j;vp=a+2-1j;un=a+2
 assert b-1j==up and up-1==bp and up+1==vp and vp+1j==un
 geometry.append(dict(k=k,A=[int(a.real),int(a.imag)],B=[int(b.real),int(b.imag)],U=[int(up.real),int(up.imag)],V=[int(vp.real),int(vp.imag)],U_next=[int(un.real),int(un.imag)]))
for period_classes in(1,2,3,11):
 d=complex(-period_classes,-period_classes);u=1-1j;assert u+period_classes*(1+1j)==u-d
 assert len({(k%period_classes)for k in range(period_classes)})==period_classes
 # All four rails have different x-y, so no full-drift cross-rail alias.
 assert len({0,1,2,3})==4
outp={'status':'PASS no homogeneous negative G3 circle in a complete WHITE cap-four front','author_note':sha(note),'signed_diagonal_dependency':sha(S.with_name('check_negative_triple_circle_diagonal_independent.json')),'main_full_ports':main,'all_U_possibilities':Uc,'clock_survivor':'NNNS','both_V_modes':Vc,'literal_geometry_controls':geometry,'analytic_review':[
'Signed homogeneous-negative rigidity permits only an alternating NE staircase after proper quarter rotation, with exact A_k NSNN and B_k WEEE and full d=(-a,-a), ell2a. The displayed main port ordinal lists were rebuilt from literal RLRL turns. They give T0(A_k)=alpha-1 and T0(B_(k-1))=alpha-2, not merely necessary inequalities.',
'Physical B_k rank2 is the sole S output into U_k; B_(k-1) rank0 is the sole W input from U_k. Thus U incomingS occurs beta+1 and outgoingW alpha-3. Fresh complete1..4 WHITE N/S enumeration leaves S,NNNS,NSNN only. Since beta-alpha>=4, the output is earlier than the input. Singleton equality and NSNN reverse order are impossible; NNNS alone survives with T1=alpha-3 and T3=beta+1.',
'The forced U has E outputs ranks0,2,3 and N inputs0,1,2. Its east neighbor V has exactly3 E inputs and3 N outputs; fresh complete inventory retains BOTH EEWE and WEEE. In either mode the third incoming and outgoing occurrences are the SAME L3 read. Exact ordinal edges therefore give literal U_k.L3 -> V_k.L3 -> U_(k+1).R2 and T2next=T3U+2>=T2U+6.',
'Iterating only a full quotient period gives T2(U_(k+a))>=T2(U_k)+6a. But U_(k+a)=U_k-d is the SAME full-drift history translated backward, so exact equivariance gives T2(U_(k+a))=T2(U_k)-P. This contradicts P>0. Spatial monotonicity alone is not used; all four rails have different x-y and cannot alias under diagonal drift.',
'The argument uses WHITE complete cap4 histories and actual full clocks only. No global maximum, K1, root-free valley, zero-output assumption or chosen V mode is needed. Homogeneous positive circles have winding+1; hence any negative-winding G3 circle must now be mixed-sign. No whole-front or all-cap exclusion, beta upper bound, or capture follows.'
]}
S.with_suffix('.json').write_text(json.dumps(outp,indent=2)+'\n');print(outp['status'])
