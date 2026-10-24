"""Source-relative ordinary two-turn separation and exact Q-C3 consequence.
No initial U/FOREIGN identity law or global-first assumption is imported.
"""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import importlib.util,json,hashlib
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent

def load(n,p):
 s=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
l=load('literal',R/'word_stabilization/check_foreign_return_interfaces.py');o=load('owner',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py');W=o.WORDS

def add(p,q):return p[0]+q[0],p[1]+q[1]
def sub(p,q):return p[0]-q[0],p[1]-q[1]
def mul(k,p):return k*p[0],k*p[1]
def cross(p,q):return p[0]*q[1]-p[1]*q[0]
def after(w,p=(0,0,0)):
 q,h=p[:2],p[2]
 for c in w:h=(h+(1 if c=='R'else-1))%4;q=add(q,l.DIRS[h])
 return (*q,h)
def center(p):return add(mul(2,p[:2]),l.rot((-1,-1),p[2]))
def local(g,p):return l.rot(sub(g,p[:2]),(-p[2])%4)
vec={'D':(2,2),'C':(2,2),'V':(2,6),'U':(0,8)}
order={'D':0,'C':0,'V':1,'U':2}
# In units pi/4 and gamma=atan(3)-pi/4 in (0,pi/4).
alpha={'D':(1,0),'C':(1,0),'V':(1,1),'U':(2,0)}
joins=[]
for A in'DCVU':
 for B in'DCVU':
  aa,ab=alpha[A];ba,bb=alpha[B];x=2*int(A=='C')+ba-aa;y=bb-ab
  assert min(x,x+y)>-4 and max(x,x+y)<4
  joins.append(dict(old=A,new=B,principal_join_coeff_pi_over4=x,principal_join_coeff_gamma=y,endpoint_values=(x,x+y)))
# Every S BASE chord strictly descends, E BASE strictly moves right, and N
# BASE/terminal C strictly ascends. Corrected-center geometry, not just heads.
stages=[]
for A in'DVU':
 ep=after(W[A]);assert ep[2]==0
 for h in[2,1,0]:
  d=l.rot(vec[A],h);hd=l.rot(ep[:2],h)
  assert(h==2 and d[0]<=0 and d[1]<0)or(h==1 and d[0]>0 and d[1]<=0)or(h==0 and d[0]>=0 and d[1]>0)
  stages.append(dict(atom=A,heading=h,head_delta=hd,corrected_center_delta=d))
for h,d in[(2,(-2,-2)),(1,(2,-2)),(0,(2,2))]:
 ep=after(W['C'],(0,0,h));assert sub(center(ep),center((0,0,h)))==d
 stages.append(dict(atom='C',heading=h,head_delta=ep[:2],corrected_center_delta=d))
# C1 holes: the same source-local L1/L2/L3 are WHITE after C1. Zero E is
# separate. In nonempty E, CU is impossible; first D/V has R_x>=0 and then
# drops heady once, so subsequent U's possible R_x=-1 still cannot reach.
Craw=l.trace(W['C']);c_holes=[]
for slot,t in[((-1,0),1),((-1,-1),2),((0,-1),3)]:
 assert Craw['first'][slot]==Craw['last'][slot]==('L',t)
 g=l.rot(slot,2);assert g[1]>=0
 c_holes.append(dict(source_C1_local=slot,S_world_hole=g,actual_last_L=o.describe('C',t)))
cu=l.trace(W['C']+W['U']+l.M);assert not cu['feasible']
firstE=[]
for A in'DV':
 p=(0,0,0);xs=[]
 for t,c in enumerate(W[A]):
  if c=='R':xs.append(p[0])
  p=after(c,p)
 assert min(xs)>=0 and after(W[A],(0,0,1))[1]==-1
 firstE.append(dict(atom=A,min_physical_local_R_x=min(xs),E_RAW_head_y_delta=-1))
# Exact closed intersections. Opposite-collinear onset is INCLUDED and routed
# by the earlier new endpoint or the outgoing old-terminal owner.
def hit(a,b,c,d):
 u=sub(b,a);v=sub(d,c);z=sub(c,a);det=cross(u,v)
 if det:
  s=F(cross(z,v),det);t=F(cross(z,u),det)
  return None if not(0<=s<=1 and 0<=t<=1)else dict(parallel=False,old_s=s,new_t=t)
 if cross(z,u):return None
 k=0 if v[0]else 1
 ts=[F(a[k]-c[k],v[k]),F(b[k]-c[k],v[k])];lo=max(F(0),min(ts));hi=min(F(1),max(ts))
 if lo>hi:return None
 point=add(c,mul(lo,v));kk=0 if u[0]else 1;s=F(point[kk]-a[kk],u[kk])
 return dict(parallel=True,old_s=s,new_t=lo,new_overlap_interval=(lo,hi),opposite_tangents=True)
records=[];Holes={(1,0),(1,1),(0,1)}
for source in'DCVU':
 a=(1,1);u=l.rot(vec[source],2);b=add(a,u)
 for actor in'DCVU':
  v=vec[actor]
  # From 2p=(2,2)+s*u-t*v with closed s,t in[0,1].
  corners=[add((1,1),sub(mul(F(s,2),u),mul(F(t,2),v)))for s in[0,1]for t in[0,1]]
  xmin,xmax=min(q[0]for q in corners),max(q[0]for q in corners)
  ymin,ymax=min(q[1]for q in corners),max(q[1]for q in corners)
  for x in range(int(xmin),int(xmax)+1):
   for y in range(int(ymin),int(ymax)+1):
    if(x+y)%2:continue
    p=(x,y,0);c=center(p);d=add(c,v);z=hit(a,b,c,d)
    if z is None:continue
    row=dict(old_source=source,new_actor=actor,N_ENTRY=p,old_segment=(a,b),new_segment=(c,d),closed_intersection=z)
    s,t=z['old_s'],z['new_t']
    if t==0:route='earlier_executed_new_endpoint'
    elif s==1:route='old_terminal_has_outgoing_owner'
    elif z['parallel']:
     raise AssertionError(('opposite overlap has no earlier endpoint/old-terminal route',row))
    elif order[actor]<=order[source]:route='relative_two_C_Jordan_angle'
    else:
     I=set(map(tuple,l.literal_geometry(W[actor])['inputs']));ctx=l.trace(W[actor]+l.M)
     witnesses=[dict(deleted_S_world=g,source_local=l.rot(g,2),actor_true_input=local(g,p),actual_BLACK_request=o.describe(actor,ctx['first'][local(g,p)][1]))for g in sorted(Holes)if local(g,p)in I]
     assert witnesses,(source,actor,p,s,t)
     assert any(ctx['first'][z['actor_true_input']][1]<len(W[actor])for z in witnesses)
     row['deleted_TRUE_input_witnesses']=witnesses
     row['hole_interface']='C1 zero/nonempty-E variant'if source=='C'else'signed cb606 S BASE deletion lemma'
     route='unavailable_deleted_true_input'
    row['route']=route;records.append(row)
counts=dict(Counter(z['route']for z in records));assert counts['unavailable_deleted_true_input']==8
assert any(z['old_source']=='U'and z['new_actor']=='U'and z['closed_intersection']['parallel']for z in records)
# Angle form at genuine source-to-contact subarc: exactly C1/C2 remain after
# an S BASE; for C1 source its own interval plus C2 are counted. Actor C's
# own outgoing interval is not counted at its partial contact tangent.
angles=[]
for source in'DCVU':
 for actor in'DCVU':
  sa,sb=alpha[source];ta,tb=alpha[actor];A=4+ta-sa;B=tb-sb
  assert min(A,A+B)>=3 and max(A,A+B)<=5
  possible=order[actor]>order[source]
  assert possible==(min(A,A+B)>=4 and max(A,A+B)>4)
  angles.append(dict(source=source,actor=actor,T_coeff_pi_over4=A,T_coeff_gamma=B,possible_T_strictly_above_pi=possible))
# The exact source-Q restoration goal, in real corrected-center coordinates.
qexit=after(W['Q']);assert qexit==(-4,-4,2)
goal=(-6,-2,0);gend=after(W['C'],goal);assert gend==(-6,-1,3)
zs,ze=center(qexit),center(gend);assert zs==(-7,-7)and ze==(-11,-3)
assert ze[0]<zs[0]and ze[1]>zs[1]
# Adversarial nominal Q-C3 path: full words do reach the geometric goal,
# but its first S/N contact's actor already fails an earlier real input.
probe_labels='DDDDVCDCVUUC';pose=qexit;pieces=[]
for i,A in enumerate(probe_labels):
 start=center(pose);end=add(start,l.rot(vec[A],pose[2]));pieces.append(dict(index=i,atom=A,ENTRY=pose,a=start,b=end));pose=after(W[A],pose);assert center(pose)==end
first_hits=[]
for j in range(len(pieces)):
 hits=[]
 for i in range(j):
  z=hit(pieces[i]['a'],pieces[i]['b'],pieces[j]['a'],pieces[j]['b'])
  if z is None:continue
  point_only=not z['parallel']or z['new_overlap_interval'][0]==z['new_overlap_interval'][1]
  if j==i+1 and point_only and z['old_s']==1 and z['new_t']==0:continue
  hits.append(dict(old_index=i,new_index=j,hit=z))
 if hits:
  t=min(z['hit']['new_t']for z in hits);first_hits=[z for z in hits if z['hit']['new_t']==t];break
assert first_hits and all(pieces[z['new_index']]['atom']=='U'for z in first_hits)
full='UQ'+probe_labels;lr=l.trace(''.join(W[A]for A in full)+l.M)
assert not lr['feasible']and lr['conflict_read']==221 and lr['previous_read']==133
adversarial=dict(nominal_labels=full,all_corrected_proxy_pieces_after_Q=pieces,first_nonadjacent_closed_contact_ties=first_hits,literal_failure=lr,actual_full_seed_and_all_read_cuts_dependency='S_E_N_deleted_core_port_guard_2026-10-24/deleted_S_core_ports.json',interpretation='Only nominal full geometry reaches C3. The genuine35-cell actual prefix fails Uq at221 before completing its first-contact U actor; no realized crossing or C3 funding is asserted.')
# Genuine prepared DCCC is retained: the separation theorem does not ban
# a third C or require an initial U/previous RAW. It only forbids a crossing.
poslabels='DCCC';posraw=''.join(W[A]for A in poslabels);pt=l.trace(posraw+l.M);assert pt['feasible']
seed={q for q,(c,t)in pt['first'].items()if c=='L'};BLACK=set(seed);p=(0,0,2);seedS={l.rot(q,2)for q in seed};BLACK=set(seedS);readrows=[]
for t,c in enumerate(posraw+l.M):
 q=p[:2];assert(q in BLACK)==(c=='L')
 if c=='L':BLACK.remove(q)
 else:BLACK.add(q)
 readrows.append(dict(tick0=t,cell=q,turn=c));p=after(c,p)
positive=dict(scope='PREPARED D-entry rotated S only; no previous RAW, FOREIGN or U-entry realization claimed',labels=poslabels,complete_seed=sorted(seedS),mass=len(seedS),all_actual_reads=readrows,RAW_EXIT=after(posraw,(0,0,2)),complete_final_BLACK=sorted(BLACK))
D=['S_E_N_deleted_core_port_guard_2026-10-24/manifest.json','audits/check_S_E_N_deleted_port_independent.json','word_stabilization/check_foreign_return_interfaces.py','literal_ownership_conventions_2026-10-24/canonical_read_ownership.py']
# Fractions are rendered exactly and never rounded to float.
def enc(v):
 if isinstance(v,F):return str(v)
 if isinstance(v,dict):return{k:enc(x)for k,x in v.items()}
 if isinstance(v,(tuple,list)):return[enc(x)for x in v]
 return v
out=dict(status='AUTHOR_FROZEN_PENDING_INDEPENDENT_REVIEW',scope='Any actual ordinary RAW S BASE rail, C1, E BASE rail, C2, N BASE rail and optional final N C3, with real complete contexts and no other C or FOREIGN. BASE means D/V/U; all three rails can be empty. The N part cannot have any nonadjacent proxy contact with the earlier S BASE rail or C1, and the whole indicated open proxy is simple. No U ancestry, globally simple earlier history or fresh-output age law is assumed. This relative ordinary-factor statement is NOT arbitrary-tail G7 simplicity.',all16_exact_principal_ordinary_joins=joins,all12_corrected_center_stage_displacements=stages,C1_source_hole_extension=dict(all3_source_holes=c_holes,literal_CU_conflict=cu,zero_E='C2 E R support has localRx>=0 and heady=Y-1, so every R lies below the deleted holes at y>=Y.',nonempty_E_first_DV=firstE,nonempty_E_proof='CU is an immutable literal conflict, so first E BASE is D/V. Its physicalR_x>=0 writes at/below headY=Y-1 and its E exit dropsY once. All later E R support y<=head+1<=Y-1; C2 also misses. Then signed cb606 zero-C N external-export argument applies unchanged. Only TRUE external inputs are excluded; CORE R births remain allowed.'),all_closed_oldS_newN_pair_rows=records,closed_pair_counts=counts,all16_source_relative_two_C_turn_forms=angles,adversarial_nominal_goal_and_actual_failed_prefix=adversarial,prepared_DCCC_positive_regression=positive,
 relative_earliest_contact_proof=[
 'Each S/E/N rail is injective and its corrected-center y/x monotonicity is strict in the indicated sweep. C1 lies below the last S endpoint except legitimate adjacency; E and C2 remain below all old S points. N starts strictly to the right of the maximum E x, so N cannot meet E or C2 again. C1 may still own its ENTRY (the old S terminal) and is explicitly retained as a source.',
 'If any N part first contacts S/C1, choose the earliest actual new piece. A contact at new ENTRY is already the previous executed E/C2/N endpoint, not discarded; C2 cannot have been the first such endpoint by the separating coordinates. Old S terminals belong to their outgoing next S piece or C1; C1 END belongs to E/C2, which N cannot meet. Reassign accordingly. Opposite-collinear approach either already touches at newENTRY or first meets an old terminal, so it has no missing strict onset.',
 'The resulting positive contact has old parameter s<1 and new t>0 on nonparallel source/actor tangents. Its source-to-contact executed subarc is simple by this RELATIVE first-contact choice, regardless of older FOREIGN/pre-source contacts. Closing gives a Jordan loop with principal closing delta in(-pi,pi). The16 exact ordinary joins telescope to T=pi+alpha_actor-alpha_source: two Cs, including sourceC1 own interval if selected, and excluding terminal actorC3 own interval. Here3pi/4<=T<=5pi/4, so negative Jordan orientation is impossible. T+delta=2pi forces T>pi, equivalently alpha_actor>alpha_source.',
 'The exact closed rational head catalogue leaves only eight angle-compatible positive source/actor poses. Every one requires one of its real S-source L1/L2/L3 holes as a TRUE external BLACK input. Signed cb606 handles D/V/U source holes; the C1 variant above handles C1. Thus none can execute its complete actual context. No such N contact exists, and all other segment pairs are already separated or legitimate adjacency.'
 ],Q_C3_funding_corollary=dict(source_Q_RAW_EXIT=qexit,initial_S_corrected_center_doubled=zs,desired_C3_ENTRY=goal,desired_C3_RAW_EXIT=gend,desired_C3_corrected_END_doubled=ze,proof='If the initial S rail is empty, E/C2/N/finalC3 corrected x is at least the initialS x, contradicting final x=-11<-7. Otherwise S is a continuous strictly descending graph xS(y). N+terminalC3 is a continuous strictly ascending graph xN(y), starting below the S terminal and at or right of its x. At the top S initial y=-7, xN is at most finalx=-11<initialSx=-7. At the bottom S terminal y, xN is at least terminalSx, with equality itself a contact assigned to outgoing C1. The intermediate value theorem forces an S/N contact. This contradicts relative two-turn separation. Therefore no completed ordinary C3 can reach ENTRY(-6,-2,N) after actual Q and exactly the first two ordinary Cs. Partial attempted C3 R8 repair is not ruled out before a later word failure.'),limits=['No all-C5 source-hook transfer: this closes the exact Q C3 repair gate only once independently audited.','No claim a foreign boundary can be crossed by this theorem, nor old output maturity carried across it.','No N physical WHITE permanence, CORE-input prohibition, exterior witness, arbitrary-tail simplicity, language coverage or capture.'],dependencies={p:hashlib.sha256((R/p).read_bytes()).hexdigest()for p in D})
(H/'two_turn_separation.json').write_text(json.dumps(enc(out),indent=2)+'\n')
print('16 exact principal joins;',len(records),'closed oldS/newN alignments',counts,';8 deleted-input cuts; Q C3(-6,-2,N) end(-11,-3) NW of start(-7,-7).')
