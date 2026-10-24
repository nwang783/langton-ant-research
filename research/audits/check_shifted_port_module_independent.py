from pathlib import Path
import json,hashlib
S=Path(__file__); R=S.parents[1]; P=R/'global_attraction_bridge_2026-10-24'; sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
MF=P/'SHIFTED_PORT_MODULE_OBSTRUCTION_MANIFEST.json';assert sha(MF)=='4f883b73c3c8976e499af71575bead1af93c14affb45750ed15ec1c71ed17dd6';M=json.loads(MF.read_text())
for group in ('files','signed_dependencies'):
 for name,h in M[group].items():assert sha(P/name)==h
J=json.loads((P/'SHIFTED_PORT_MODULE_OBSTRUCTION_CHECKED.json').read_text())
ns={};exec((S.parent/'check_return_permanent_debt_independent.py').read_text().split('def check_case')[0],ns)
verify=ns['verify_future']; vec=ns['vec']; pair=ns['pair']; ray=ns['ray_k'];G=ns['G']
B={q:-i-1 for i,q in enumerate(sorted(G,key=lambda q:(q.real,q.imag)))};p=0j;h=1;pos=[];heads=[];words=[];cuts=[];deaths={}
for t in range(800):
 cuts.append((dict(B),p,h));pos.append(p);heads.append(h)
 if p in B:deaths[B.pop(p)]=t; words.append('L');h=(h-1)%4
 else:B[p]=t;words.append('R');h=(h+1)%4
 p+=vec[h]
A=''.join(words[:182]);U=''.join(words[182:286]);Q=pos[182:286];delta=2+2j
assert verify(*cuts[182])[:2]==(U,delta)
assert all(pos.index(q)<59 for q in G)
assert pos[60]==2j and words[60]=='R' and 60 not in deaths and 60 not in verify(*cuts[182])[2]
# Affine COMPLEX positions are coefficient triples (k,K,1), not evaluated parameter samples.
add=lambda a,b:tuple(x+y for x,y in zip(a,b));mul=lambda a,z:tuple(z*x for x in a);C=lambda z:(0j,0j,complex(z))
poses=[C(0), (2+2j,2+2j,-1),(-2+6j,2+2j,-4j),(-10-2j,2+2j,5),(-6-6j,2+2j,8j)]
rot=[1,1j,-1,-1j,1]; Rcnt=[(1,1,-4),(2,0,-5),(4,0,-6),(2,0,-7),(3,-1,-4)]; part=[61,71,61,71,14]
def pt(s,q,j=(0,0,0)):return add(add(poses[s],C(rot[s]*q)),mul(j,rot[s]*delta))
def scalar(z,n):return tuple(int((x*n.conjugate()).real) for x in z)
def minus(a,b):return tuple(x-y for x,y in zip(a,b))
ineq=[]
def check(f,label):
 a,b,c=f; bounds=[10*a+c,a,a+3*b];assert min(bounds)>=0,(label,f,bounds);ineq.append(dict(label=label,affine=list(f),vertex=bounds[0],ray_slopes=bounds[1:]))
sets=[]
for s in range(5):
 check(minus(Rcnt[s],(0,0,1)),f'positive_R{s}')
 Z=[pt(s,q) for q in pos[:182]]
 for q in Q:Z += [pt(s,q),pt(s,q,minus(Rcnt[s],(0,0,1)))]
 Z += [pt(s,Q[i],Rcnt[s]) for i in range(part[s])];sets.append(Z)
 assert pt(s,Q[part[s]],Rcnt[s])==(poses[s+1] if s<4 else C(2j))
 assert vec[heads[182+part[s]]]*rot[s]==(rot[s+1] if s<4 else 1)
seps=[(0,1,1j,(2,2,0)),(2,0,1-1j,(0,0,-3)),(3,0,1,(0,0,0)),(4,0,1,(0,0,0)),(2,1,1,(-2,2,1)),(3,1,1j,(2,2,0)),(4,1,1j,(2,2,0)),(3,2,1j,(-2,2,1)),(2,4,1-1j,(0,0,-11)),(3,4,1,(-6,2,0))]
for a,b,n,beta in seps:
 for j,z in enumerate(sets[a]):check(minus(minus(beta,scalar(z,n)),(0,0,1)),f'sep{a}{b}_left{j}')
 for j,z in enumerate(sets[b]):check(minus(scalar(z,n),beta),f'sep{a}{b}_right{j}')
for s,n,bound in [(1,1+1j,13),(3,-1-1j,15),(2,-1+1j,45)]:
 for j,z in enumerate(sets[s]):check(minus(scalar(z,n),(0,0,bound)),f'outside_Omega_{s}_{j}')
check(minus(Rcnt[0],(0,0,6)),'six_stage0_epochs');check(minus(Rcnt[4],(0,0,26)),'twentysix_stage4_epochs')
omega=lambda q:q.real>=-16 and -14<=q.real+q.imag<=12
protected=set(G)
def toggle(q):
 if q in protected:protected.remove(q)
 else:protected.add(q)
for q in pos[:182]:toggle(q)
for j in range(6):
 for q in Q:toggle(q+j*delta)
for j in range(-26,0):
 for q in Q:toggle(q-8+j*delta)
for q in Q[:14]:toggle(q-8)
protected={q for q in protected if omega(q)};assert len(protected)==90 and sorted(map(pair,protected))==J['protected90']
for q in Q:assert (q+6*delta).real+(q+6*delta).imag>12 and (q-8-27*delta).real+(q-8-27*delta).imag<-14
for q in pos[:182]:check(minus(scalar(pt(4,q),-1-1j),(0,0,15)),'stage4_prefix_below')
for q in G:check(minus(scalar(pt(4,q),-1-1j),(0,0,15)),'stage4_input_below')
from collections import Counter
assert len(ineq)==10478
assert Counter(json.dumps(z,sort_keys=True)for z in ineq)==Counter(json.dumps(z,sort_keys=True)for z in J['affine_inequalities'])
assert all(pt(4,q,Rcnt[4])==C(q-8) for q in Q)
old=json.loads((P/'RETURN_PERMANENT_OUTPUT_DEBT_CHECKED.json').read_text());rec=next(z for z in old['controls']if z['name']=='protected_recovery90');assert {q-2j for q in protected}=={complex(*q) for q in rec['initial_black']}
assert sum(z[0] for z in Rcnt)==12 and sum(z[1]for z in Rcnt)==0 and sum(z[2]for z in Rcnt)==-26
balance=lambda w:w.count('R')-w.count('L');assert balance(U)==12
assert 20+5*balance(A)-26*12+sum(balance(U[:j])for j in part)==-88
assert 5*182-26*104+sum(part)==-1516
hits=[]
assert Q[90]==6+8j and U[90]=='R'
for i,q in enumerate(Q):
 m=ray(Q[90]-q,delta)
 if m is not None and m>=0:hits.append([m,i]);assert 104*m+i<=90
assert hits==J['marker_phase90_ray_equalities']
controls=[]
for supplied in J['controls']:
 n,K=supplied['n'],supplied['K'];k=n//2;evaluate=lambda z:z[0]*k+z[1]*K+z[2]
 seed={evaluate(pt(s,q))for s in range(5)for q in G};assert len(seed)==20 and sorted(map(pair,seed))==supplied['initial_black']
 expected=''.join(A+U*int(evaluate(Rcnt[s]))+U[:part[s]] for s in range(5));e=624*n-1516;assert len(expected)==e
 B={q:-i-1 for i,q in enumerate(sorted(seed,key=lambda q:(q.real,q.imag)))};p=0j;h=1;death={};actual=[];marker=104*K-40;target=2*K+(2*K+2)*1j;recovery=None
 for t in range(e+983):
  if t==e:
   assert p==2j and h==1 and B[p]==60 and len(B)==72*n-88 and {q for q in B if omega(q)}==protected
  if t==e+774:recovery=(dict(B),p,h)
  if p in B:death[B.pop(p)]=t;ch='L';h=(h-1)%4
  else:B[p]=t;ch='R';h=(h+1)%4
  if t<e:assert ch==expected[t]
  if t==e:assert ch=='L' and U[14]=='R'
  if t==marker:assert p==target and ch=='R'
  actual.append(ch);p+=vec[h]
 tail,d,ff,tests=verify(B,p,h);death.update({tag:e+983+j for tag,j in ff.items()})
 assert B[target]==marker and marker not in death and death[60]==e
 assert sorted((pair(q)[0],pair(q)[1],tag)for q,tag in B.items()) and sha(P/'SHIFTED_PORT_MODULE_OBSTRUCTION_CHECKED.json')==M['files']['SHIFTED_PORT_MODULE_OBSTRUCTION_CHECKED.json']
 terminal=sorted((pair(q)[0],pair(q)[1],tag)for q,tag in B.items());assert hashlib.sha256(json.dumps(terminal).encode()).hexdigest()==supplied['full_terminal_black_sha256']
 assert len(B)==supplied['full_terminal_black_count'] and [pair(p),h]==supplied['tail_pose'] and pair(d)==supplied['tail_drift']
 recovery_word,_,_,_=verify(*recovery);assert recovery_word in [U[i:]+U[:i]for i in range(104)] and actual[e+773]!=recovery_word[-1]
 L=sum(tag in death for tag in range(-20,0));Lmax=L
 for t,ch in enumerate(actual):L+=int(t in death) if ch=='R' else -1;Lmax=max(Lmax,L)
 assert Lmax==supplied['observed_relevant_peak']==77
 controls.append(dict(n=n,K=K,updates=e+983,return_time=e,first_canonical=e+774,full_terminal_mass=len(B),full_future_tests=tests,relevant_peak=Lmax,nominal_marker=pair(target),permanent_marker_birth=marker))
out=dict(status='PASS exact two-parameter shifted-port architecture obstruction',manifest=sha(MF),proof=M['files']['SHIFTED_PORT_RETURN_MODULE_OBSTRUCTION.md'],affine_inequalities_independently_rebuilt=len(ineq),all10_stage_separators=True,each_port_inside_own_first59=True,protected_exact90=True,all_future_marker_phase_equalities=hits,controls=controls,analytic_review=[
'The domain cone vertex(10,0), rays(1,0),(1,3) exactly covers k>=10 and0<=K<=3k-30. Every segment is nonempty, so endpoint bounds certify every physical read without a length cap. Complete initial ports lie in their own first59 reads; ten strict disjoint-read separators ensure distinct initial cells and full-field chronological induction.',
'Stage0 extra periods lie above Omega, stages1/3 on opposite x+y sides and stage2 has x-y<=-45 while Omega implies x-y>=-44. Their initial ports are in those read sets. Stage4 centering is exactly Q-8+(j-R4)delta and all earlier copies/prefix/input are below Omega. Thus the complete protected field equality, not only cardinality, holds for ALL parameters with external archives untouched.',
'R60 is never reread by standalone launch reference and lies in stage0 only. At the final endpoint the same physical identity is BLACK and forces L opposite nominal continuing phase14 R. K>0 nominal translated return first fails here. K>=3 nominal target is an actual outgoing phase90 R; complete future-ray equalities certify permanence, later stages miss and recovery remains in Omega.',
'Signed protected recovery supplies canonical tail at e+774, and its preceding mismatch excludes ANY earlier canonical onset because all cyclic104 phases are distinct. Named complete-field replays independently recover this onset and whole-tail parity. The universal relevant cap132 follows the previously signed20 initial+22 same-stage+90 recovery survivors partition; observed77 is only a named-control maximum.',
'All members in the stated domain capture. This refutes only the precise remote-four-port translation as a migrating long-lived module construction, not arbitrary moving modules, bounded-relevant-stock nontranslation or global attraction.'
]);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
