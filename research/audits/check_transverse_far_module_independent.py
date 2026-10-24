from pathlib import Path
from collections import Counter
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'global_attraction_bridge_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'TRANSVERSE_FAR_MODULE_MANIFEST.json';assert sha(MF)=='1abb9100e92eba1fb40d38cc8945e9f54739325a8ff1c1dc3294d658fc95758d';M=json.loads(MF.read_text())
for grp in('files','signed_dependencies'):
 for f,h in M[grp].items():assert sha(D/f)==h
J=json.loads((D/'TRANSVERSE_FAR_MODULE_CHECKED.json').read_text());SRC=json.loads((D/'TRANSVERSE_FAR_MODULE_SOURCE.json').read_text())
ns={};exec((S.parent/'check_return_permanent_debt_independent.py').read_text().split('def check_case')[0],ns);verify=ns['verify_future'];vec=ns['vec'];xy=ns['pair'];ray=ns['ray_k'];G=ns['G'];B=set(G);p=0j;h=1;trace=[];heads=[];word=''
for t in range(286):
 trace.append(p);heads.append(h);c='L'if p in B else'R';word+=c;B.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p+=vec[h]
AP=trace[:182];Q=trace[182:];A=word[:182];U=word[182:];delta=2+2j;assert len({U[i:]+U[:i]for i in range(104)})==104 and all(trace.index(q)<59 for q in G)
# Symbolic affine COMPLEX positions (coefficient ofk, constant), with independent exact domain test.
add=lambda a,b:tuple(x+y for x,y in zip(a,b));minus=lambda a,b:tuple(x-y for x,y in zip(a,b));mul=lambda a,z:tuple(z*x for x in a);C=lambda z:(0j,complex(z))
poses=[C(0),(14+14j,-1),(10+18j,-4j),(2+10j,5)];rot=[1,1j,-1,-1j];counts=[(7,-4),(2,-5),(4,-6),(2,-6)];parts=[61,71,61,56];target=(6+6j,3j)
pt=lambda i,q,j=(0,0):add(add(poses[i],C(rot[i]*q)),mul(j,rot[i]*delta));dot=lambda q,n:tuple(int((z*n.conjugate()).real)for z in q);rel=lambda q:minus(q,target)
ineq=[]
def nonneg(f,label):
 a,b=f;assert a>=0 and 10*a+b>=0,(f,label);ineq.append(dict(label=label,affine=list(f),at_k10=10*a+b,slope=a))
V=[]
for i in range(4):
 nonneg(minus(counts[i],(0,1)),f'positive_R{i}');v=[pt(i,q)for q in AP]
 for q in Q:v.extend([pt(i,q),pt(i,q,minus(counts[i],(0,1)))])
 v.extend(pt(i,Q[t],counts[i])for t in range(parts[i]));V.append(v)
 assert pt(i,Q[parts[i]],counts[i])==(poses[i+1]if i<3 else target)
 assert vec[heads[182+parts[i]]]*rot[i]==(rot[i+1]if i<3 else-1j)
seps=[(0,1,1j,(14,0)),(2,0,1-1j,(0,-3)),(3,0,1-1j,(0,-3)),(2,1,1,(10,1)),(3,1,1j,(14,0)),(3,2,1j,(10,1))]
for a,b,n,beta in seps:
 for j,q in enumerate(V[a]):nonneg(minus(minus(beta,dot(q,n)),(0,1)),f'sep{a}{b}_a{j}')
 for j,q in enumerate(V[b]):nonneg(minus(dot(q,n),beta),f'sep{a}{b}_b{j}')
for q in V[1]:nonneg(minus(dot(rel(q),1+1j),(0,18)),'stage1_above')
for q in V[2]:nonneg(minus(dot(rel(q),-1+1j),(0,21)),'stage2_left')
for q in AP+list(G):
 nonneg(minus(dot(rel(pt(0,q)),-1-1j),(0,74)),'source_launch_below')
 nonneg(minus(dot(rel(pt(3,q)),-1+1j),(0,21)),'return_launch_left')
for i in range(parts[0]):nonneg(minus(dot(rel(pt(0,Q[i],counts[0])),1+1j),(0,18)),'outgoing_partial_above')
omega=lambda z:-73<=z.real+z.imag<=17 and z.real-z.imag>=-20
protected=set()
def toggle(q):
 if q in protected:protected.remove(q)
 else:protected.add(q)
for v in range(-30,36):
 for q in Q:toggle(q-3j+v*delta)
for v in range(-20,-6):
 for q in Q:toggle(-1j*q+5-3j+v*(2-2j))
for q in Q[:56]:toggle(-1j*q+5-3j-6*(2-2j))
protected={q for q in protected if omega(q)};assert len(protected)==330 and sorted(map(xy,protected))==J['protected_black']==SRC['protected_black']
for q in Q:
 assert (q-3j-31*delta).real+(q-3j-31*delta).imag<-73
 assert (q-3j+36*delta).real+(q-3j+36*delta).imag>17
 z=-1j*q+5-3j-21*(2-2j);assert z.real-z.imag<-20
 assert rel(pt(0,q,(3,0)))==C(q-3j)and rel(pt(3,q,(2,0)))==C(-1j*q+5-3j)
suffix=[pt(0,Q[t],(3,-3))for t in range(72,104)]
for q in Q:suffix.extend([pt(0,q,(3,-2)),pt(0,q,minus(counts[0],(0,1)))])
suffix.extend(pt(0,Q[t],counts[0])for t in range(parts[0]));suffix+=V[1]+V[2]+V[3]+[target]
for q in suffix:nonneg(minus(dot(q,1),(2,3)),'marked_x_ge_n_plus3');nonneg(minus(dot(q,1j),(6,-5)),'marked_y_ge_3n_minus5')
assert len(ineq)==10096 and Counter(json.dumps(z,sort_keys=True)for z in ineq)==Counter(json.dumps(z,sort_keys=True)for z in J['affine_inequalities'])
assert Q[71]==6+9j and U[71]=='R';hits=[]
for i,q in enumerate(Q):
 m=ray(Q[71]-q,delta)
 if m is not None and m>=0:hits.append([m,i]);assert 104*m+i<=71
assert hits==[[0,71]]==J['marked_source_phase71_alignments'];assert Q[56]==9+7j and U[56]=='R'
assert sum(a for a,b in counts)==15 and sum(b for a,b in counts)==-21 and 4*182-21*104+sum(parts)==-1207
# Independent full330 protected recovery, actual lifetime fates and infinite tail parity.
F,Z=SRC['post_contact_word'],SRC['tail_word'];assert len(F)==8986 and len(Z)==104 and F[-1]!=Z[-1]and Z in[U[i:]+U[:i]for i in range(104)]
B={q:-i-1 for i,q in enumerate(sorted(protected,key=lambda q:(q.real,q.imag)))};p=0j;h=2;death={};births={};events=[];terminal_at_onset=None
for t,ch in enumerate(F+Z*2):
 if t==8986:terminal_at_onset=(dict(B),p,h)
 assert omega(p)and(ch=='L')==(p in B);events.append(ch)
 if ch=='L':death[B.pop(p)]=t;h=(h-1)%4
 else:B[p]=t;births[t]=p;h=(h+1)%4
 p+=vec[h]
assert terminal_at_onset[1:]==(17-13j,2);onsetword,d,ff,tests0=verify(*terminal_at_onset);assert onsetword==Z and d==2-2j
N=len(F)+208;tw,dd,ff,tests=verify(B,p,h);assert tw==Z and dd==2-2j;death.update({tag:N+t for tag,t in ff.items()});L=sum(tag in death for tag in range(-330,0));assert L==285;profile=[L]
for t,ch in enumerate(events):L+=int(t in death)if ch=='R'else-1;profile.append(L)
assert max(profile)==432 and L==13
rc=J['protected_reference'];assert rc['physical_updates']==N and rc['terminal_pose']==[xy(p),h]and rc['relevant_mass_max']==432 and rc['all_period_parity_tests']==tests
assert {(complex(*q['cell']),q['lifetime'])for q in rc['terminal_black']}==set(B.items())
for r in rc['initial_read_fates']:
 q=complex(*r['cell']);tag=next(t for t,z in enumerate(sorted(protected,key=lambda q:(q.real,q.imag)),1)if z==q);assert r['death']==death.get(-tag)
# Pruned relevance and its complete within-period profile repeat, while the full archive is retained in both parity tests.
C0={q for q,tag in B.items()if tag in ff};B0=dict(B);p0=p;h0=h;laterdeath={};ev=[]
for i in range(104):
 old=B.pop(p,None);ev.append(old)
 if old is None:B[p]=N+i;h=(h+1)%4
 else:laterdeath[old]=i;h=(h-1)%4
 p+=vec[h]
w1,d1,f1,tests1=verify(B,p,h);laterdeath.update({tag:104+t for tag,t in f1.items()});C1={q for q,tag in B.items()if tag in f1};assert w1==tw and d1==dd and C1=={q+dd for q in C0}
L=len(C0);pp=[L]
for i,old in enumerate(ev):L+=int(N+i in laterdeath)if old is None else-1;pp.append(L)
assert pp==J['pruned_period_relevance_profile']and max(pp)<=432
controls=[]
for row in J['controls']:
 n=row['n'];k=n//2;value=lambda q:q[0]*k+q[1];seed={value(pt(s,q))for s in range(4)for q in G};assert len(seed)==16 and sorted(map(xy,seed))==row['initial_black']
 c=780*n-1207;b=156*n-59;q=3*n+(3*n+3)*1j;expected=''.join(A+U*int(value(counts[i]))+U[:parts[i]]for i in range(4));assert len(expected)==c
 B={q:-i-1 for i,q in enumerate(sorted(seed,key=lambda q:(q.real,q.imag)))};p=0j;h=1;marked_read=[]
 for t,ch in enumerate(expected+F+Z*2):
  if p==q:marked_read.append(t)
  if t==b:assert p==q and p not in B
  if t==c:assert p==q and h==2 and B[p]==b and {at-q for at in B if omega(at-q)}==protected
  if b<t<=c:assert p.real>=n+3 and p.imag>=3*n-5
  assert(ch=='L')==(p in B)
  if ch=='L':B.pop(p);h=(h-1)%4
  else:B[p]=t;h=(h+1)%4
  p+=vec[h]
 assert marked_read[marked_read.index(b)+1]==c
 tw,d,ff,tests=verify(B,p,h);assert tw==Z and d==2-2j
 terminal=sorted((xy(q)[0],xy(q)[1],tag)for q,tag in B.items());assert hashlib.sha256(json.dumps(terminal).encode()).hexdigest()==row['full_terminal_sha256']and len(B)==row['full_terminal_black_count']and[xy(p),h]==row['full_terminal_pose']
 controls.append(dict(n=n,updates=len(expected+F+Z*2),birth=b,death=c,age=c-b,first_canonical=c+8986,full_terminal_mass=len(B),all_future_parity_tests=tests))
out=dict(status='PASS all-even-n>=20 sixteen-cell moving long-lived return-module family, with exact finite-to-infinite scope',manifest=sha(MF),proof=M['files']['SIXTEEN_CELL_TRANSVERSE_MOVING_MODULE.md'],affine_inequalities=10096,all_six_complete_read_set_separators=True,all_ports_first59=True,protected_full_field_size=330,protected_initial_relevant=285,all_future_exact_relevant_max=432,protected_recovery_length=8986,marked_source_all_ray_equalities=hits,controls=controls,analytic_review=[
'All affine inequalities were rebuilt using fresh literalG reference and complex coefficient pairs. Endpoint extrema cover each nonempty arithmetic read segment for everyintegerk>=10. Six strict separators plus first59 own-port reads establish literal full-board first-difference execution with all16 inputs and every earlier archive retained.',
'Originalq=(6k,6k+3) is phase71 copy3k-3, actualbirth312k-59 and sole nonnegative reference ray equality at its ownphase. Otherstage read sets miss it until finalendpoint1560k-1207, which is excluded from V3 and demandsR in freshreference butactuallyreadsL. Marked suffix inequalities cover everycutb+1..c, not the earlier origin launch.',
'Normalized protectedOmega has sum[-73,17],difference>=-20. Allinitial inputs and three irrelevant prefix pieces are excluded by exact affineguards. Reindexed outgoingv=-30..35 andreturnv=-20..-7 pluspartialv=-6 give exactly330cells byXOR; all omitted actualparametercopies lie outsideOmega. Exactcentering formulas hold symbolically, not byinterpolation.',
'Independent330-cell full recovery and every read stayOmega; after8986actualreads the exact104rayparity tail hasdrift2,-2. Its positive difference drift keepsALLfuture readsOmega. Full exteriorarchive is thus neverread. The precedingletter mismatch with distinctcyclic104phases proves exactfirstonsetc+8986, not merely a sufficient observedrepeat.',
'All initial330 lifetimefates and full terminalfields checked. Initialrelevant285, complete finiteprofilemaximum432 and translatedpruned104closure prove ALLFUTURE432. Beforec,16initial+22same-stagefuturecontacts+330survivors bound368; afterc actualrelevance equalsprotectedreference. Everyfamilymemberattains432, unlike promoting named-control maxima.',
'Fresh fullboardsn20/40/80 retain everyidentity and wholefutureparity. This is a real R-born, actuallyconsumed moving module across a constant-massfamily, with entiremarked excursion escaping everyfixed AXIALband asn grows. Birthslieon x-y=-3, so no diagonalescapeclaim. Eachmembercaptures; no singleorbitwithinfinitelymanyunbounded-ageepisodes, eventualper-orbitlocalizationfailure, pristine-recordbudgetcounterexample or globalattractionclaim.'
]);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
