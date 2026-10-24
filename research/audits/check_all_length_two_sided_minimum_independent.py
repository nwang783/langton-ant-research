from pathlib import Path
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'global_attraction_bridge_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'ALL_LENGTH_TWO_SIDED_MINIMUM_MANIFEST.json';assert sha(MF)=='124b47782e797e1136ee59b46f4fdc72d4d3fa0bddad5cf95172302c5fca2ffb'
for f,h in json.loads(MF.read_text())['sha256'].items():assert sha(D/f)==h
J=json.loads((D/'ALL_LENGTH_TWO_SIDED_MINIMUM_CHECKED.json').read_text())
for f,h in J['source_hashes'].items():assert sha(D/f)==h
ns={'__file__':str(S.with_name('check_return_permanent_debt_independent.py'))};exec(Path(ns['__file__']).read_text().split('def check_case')[0],ns);future=ns['verify_future'];V=ns['vec'];xy=ns['pair'];key=lambda z:(z.real,z.imag)
K={-1+2j,-1+3j,0j,4j,5j,6j,1+0j,1+1j,1+2j,1+5j,2+0j,2+3j,2+4j};assert sorted(map(xy,K))==J['base']
standard=json.loads((R/'recovered_bundle/ant_global/root/standard.json').read_text())['word'];phases={standard[i:]+standard[:i]for i in range(104)}
def geometry(p,h,w):
 pts=[];hs=[]
 for c in w:pts.append(p);hs.append(h);h=(h+(1 if c=='R'else-1))%4;p+=V[h]
 return pts,hs,p,h
def sim(seed,p,h,N,expected=None):
 B={q:-i-1 for i,q in enumerate(sorted(seed,key=key))};word='';mass=[len(B)];pts=[];first={};deaths={};snap={}
 for t in range(N):
  if t==4:snap=(dict(B),p,h)
  pts.append(p);first.setdefault(p,t);old=B.pop(p,None)
  if old is None:B[p]=t;c='R';h=(h+1)%4
  else:deaths[old]=t;c='L';h=(h-1)%4
  if expected is not None:assert c==expected[t]
  word+=c;p+=V[h];mass.append(len(B))
 return dict(B=B,p=p,h=h,word=word,mass=mass,pts=pts,first=first,deaths=deaths,snap=snap)
def cert(z,expected_phase=None):
 w,d,f,n=future(z['B'],z['p'],z['h']);assert w in phases
 if expected_phase is not None:assert w==expected_phase
 z.update(tail=w,drift=d,tests=n);z['deaths'].update({i:len(z['word'])+t for i,t in f.items()});return z
def balance(w):
 v=[0]
 for c in w:v.append(v[-1]+(1 if c=='R'else-1))
 return dict(length=len(w),gain=v[-1],minimum=min(v),maximum=max(v),minimum_cuts=[i for i,x in enumerate(v)if x==min(v)])
# Derive W from the actual complete13-cell source, then certify the same phase.
first=sim(K,0j,1,104);W=first['word'];assert W==J['base_word']and W in phases;cert(first,W);assert(first['p'],first['h'],first['drift'])==(2+2j,1,2+2j)
pts,heads,p,h=geometry(0j,1,W);assert(p,h)==(2+2j,1)
# Mature incoming phase13 field from exact negative-period parity in the closed x>=-3 guard.
M=set();j=13
for i,q in enumerate(pts):
 r=q-pts[j];lower=-((int(r.real)+3)//2);upper=0 if i<j else-1
 for k in range(lower,upper+1):M.symmetric_difference_update({r+k*(2+2j)})
assert 0j not in M;M.add(0j);assert len(M)==24 and sorted(map(xy,M))==J['rule']['input_kernel']
k=cert(sim(M,0j,heads[13],312),W[97:]+W[:97]);v=k['word'];assert v==J['rule']['recovery']and(k['p'],k['h'],k['drift'])==(2+6j,heads[97],2+2j)
assert sorted(map(xy,k['B']))==J['rule']['endpoint_black']and[xy(k['p']),k['h']]==J['rule']['endpoint_pose']and k['tests']==J['rule']['full_tail_tests']
kt=geometry(k['p'],k['h'],k['tail'])[0];assert min(q.real for q in k['pts'])==J['rule']['minimum_read_x']>=-3;assert max(q.real for q in k['pts'])==J['rule']['maximum_read_x'];assert min(q.real for q in kt)==J['rule']['future_minimum_x']>=-3
U=W*100+W[:13];F=W[97:]+W*100+W[:13];q0=202+201j;dmark=206+206j
z=sim(K|{q0},0j,1,len(U),U);assert(z['p'],z['h'])==(q0,heads[13])and q0 not in z['first'];inside={q for q in z['B']if q.real>=199};assert inside=={q+q0 for q in M}and sorted(map(xy,inside))==J['initial_interface']['full_inside_field'];assert max(q.real for q in z['pts'])==J['initial_interface']['maximum_read_x']<408
z2=sim(M|{dmark},0j,heads[13],len(v+F),v+F);assert(z2['p'],z2['h'])==(dmark,heads[13])and dmark not in z2['first'];inside2={q for q in z2['B']if q.real>=203};assert inside2=={q+dmark for q in M}and sorted(map(xy,inside2))==J['pair_interface']['full_inside_field'];assert min(q.real for q in z2['pts'])==J['pair_interface']['minimum_read_x']>=-3 and max(q.real for q in z2['pts'])==J['pair_interface']['maximum_read_x']<412;assert max(q.real for q in k['B'])<203
for name,w in [('W',W),('initial_flight',U),('recovery',v),('connector',F),('repeated_block',v+F),('final_tail',W[97:]+W[:97])]:assert balance(w)==J['balances'][name]
assert J['balances']['W']['minimum_cuts']==[4]and J['balances']['initial_flight']['minimum_cuts']==[4]
# Independent reverse source, exact actual phase and full future footprint bound.
r=cert(sim(K,-1+0j,3,2704));jr=J['reverse_base'];assert r['word']==jr['prefix_word']and r['mass']==jr['prefix_masses'];assert(r['p'],r['h'],len(r['B']),r['drift'])==(-11+28j,1,299,-2+2j)
assert r['tail']==jr['tail_word']and r['tests']==jr['tail_tests']and sorted(map(xy,r['B']))==jr['full_endpoint'];rt=geometry(r['p'],r['h'],r['tail'])[0];assert max(q.real for q in r['pts']+rt)==13 and r['drift'].real<0
assert min(r['mass'])==12 and[i for i,x in enumerate(r['mass'])if x==12]==[7,9]and len(r['B'])+balance(r['tail'])['minimum']>12
# All source inputs and all actual cut4 lifetimes, not just black cardinality.
base=cert(sim(K,0j,1,208,W*2),W);b4,p4,h4=base['snap'];assert len(b4)==11 and all(i in base['deaths']for i in b4.values());assert max(base['first'][q]for q in K)==99
assert sorted(map(xy,b4))==J['base_minimum4_black']and [xy(p4),h4]==J['base_minimum4_pose'];assert [dict(cell=xy(q),time=base['first'][q])for q in sorted(K,key=key)]==J['base_initial_first_reads']
controls=[]
for row in J['controls']:
 m=row['m'];markers={q0+i*dmark for i in range(m)};seed=K|markers;assert sorted(map(xy,seed))==row['seed']and len(seed)==13+m
 seq=U+(v+F)*(m-1)+v if m else W*2;N=len(seq);z=cert(sim(seed,0j,1,N,seq),W[97:]+W[:97]if m else W)
 assert N==row['positive_prefix_length']and seq==row['positive_prefix_word']and sorted(map(xy,z['B']))==row['positive_terminal_black']and [xy(z['p']),z['h']]==row['positive_terminal_pose'];assert(z['tail'],xy(z['drift']),z['tests'])==(row['positive_tail_word'],row['positive_tail_drift'],row['positive_tail_tests'])
 assert min(z['mass'])==m+11 and[i for i,x in enumerate(z['mass'])if x==m+11]==[4]and len(z['B'])+balance(z['tail'])['minimum']>m+11
 for i in range(m):assert z['first'][q0+i*dmark]==10413+10732*i
 assert [dict(cell=xy(q),time=z['first'][q])for q in sorted(seed,key=key)]==row['initial_first_consumptions'];bs,ps,hs=z['snap'];assert sorted(map(xy,bs))==row['minimum_full_black']and all(i in z['deaths']for i in bs.values())
 rz=cert(sim(seed,-1+0j,3,2704,r['word']),r['tail']);assert set(rz['B'])==set(r['B'])|markers and min(rz['mass'])==m+12 and sorted(map(xy,rz['B']))==row['reverse_terminal_black']and rz['tests']==row['reverse_tail_tests']
 np,nh=rz['p']-V[rz['h']],(rz['h']+2)%4;assert[xy(np),nh]==row['negative_endpoint_pose'];back=sim(set(rz['B']),np,nh,2704,r['word'][::-1].translate(str.maketrans('RL','LR')));assert(set(back['B']),back['p'],back['h'])==(seed,0j,1)
 controls.append(dict(m=m,positive_reads=N,minimum=m+11,reverse_minimum=m+12,all_initial_and_minimum_lifetimes_consumed=True))
# Separate exact m0 whole-forward-relevant minimum, a scope corollary only.
B={q:-i-1 for i,q in enumerate(sorted(K,key=key))};p=0j;h=1;profile=[];C0=None
for t in range(105):
 w,d,f,n=future(B,p,h);assert w==W[t%104:]+W[:t%104];C={q for q,i in B.items()if i in f};profile.append(len(C))
 if t==0:C0=C;assert C==K
 if t==104:assert C=={q+d for q in C0};break
 if p in B:B.pop(p);h=(h-1)%4
 else:B[p]=t;h=(h+1)%4
 p+=V[h]
assert min(profile)==11 and max(profile)==22
out=dict(status='PASS all-m full two-sided minimum m+11 at unique cut4; no two-sided invisible archive',manifest=sha(MF),script=sha(S),controls=controls,source_phase_word=W,recovery_phase=97,kernel_size=len(M),initial_flight=len(U),pair_interface=len(v+F),reverse_reads=2704,reverse_full_future_max_x=13,m0_independent_relevant_phase_profile=profile,m0_global_forward_relevant_minimum=11,analytic_review=['The13-cell source actual word, phase13 mature field,312-read recovery actual phase97 and exact reverse-source canonical phase are physically rebuilt, not merely tested for generic canonical membership. Complete all-k ray parity retains every black field cell at all certified ends.','At the first marker, the complete field on x>=199 is exactly the translated24-cell kernel. First-flight maximumx<408 leaves every later marker untouched. The complete kernel-plus-next-marker10732 interface reads onlyx>=-3 andx<412; at its next boundaryx>=203 the field is exactly the translated kernel. This gives an exact nested-guard induction: earlier archive is left of the advancing guard, and all later markers except next are unread. Every m is finite and paid initially.','After the final recovery, its entire future staysx>=-3 and drifts east, so all inherited western archive is irrelevant without deletion. No extra parameter fit or broad retained scattering-table exhaustion is needed.','Exact R-minus-L balances give positive-time unique minimum13+m-2=m+11 at4; accumulated gains1199 and repeated1236 dominate later dips2/3. Reverse-conjugate full read maxx13 excludes every markerx>=202 at once. Its mass minimum12 at7/9 gives original negative minimum m+12. Actual negative endpoint uses edge reversal and named full forward recoveries return exactly each original seed.','Every original input and every cut4 current lifetime is future-consumed. At any negative cut all current black survives to an original input or is consumed sooner; at positive cuts any nonoriginal current lifetime has a past R read. Therefore no black physical site is unread in BOTH directions at any cut, and two-sided pruning removes nothing.','Arbitrarily large full minima defeat a finite family of COMPLETE core states up to time shift/rigid motion plus only bidirectional-irrelevance deletion. No universal bounded forward-only pruning minimum, noncapture, infinite finite-input train or orbit-dependent compactness failure is claimed.','Separate independent corollary for m0 only: exact104 pruned phase fields have sizes11..22 and close by drift; all negative-cut fields are relevant and have mass>=12. Thus this single capturing K orbit has global whole-forward-relevant minimum11 and never enters any <=10 pruning class. This does not say the whole m-family has unbounded forward-relevant minima.'])
S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
