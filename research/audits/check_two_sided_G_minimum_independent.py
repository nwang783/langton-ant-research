from pathlib import Path
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'global_attraction_bridge_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();M=D/'TWO_SIDED_G_MINIMUM_MANIFEST.json';assert sha(M)=='91af664533ebd13878a4754c8ddc1f337d431b0e6f92e0591216b98e6cb30b77'
for f,h in json.loads(M.read_text())['sha256'].items():assert sha(D/f)==h
J=json.loads((D/'TWO_SIDED_G_MINIMUM_CHECKED.json').read_text())
for f,h in J['source_hashes'].items():assert sha(D/f)==h
ns={'__file__':str(S.with_name('check_return_permanent_debt_independent.py'))};exec(Path(ns['__file__']).read_text().split('def check_case')[0],ns);future=ns['verify_future'];V=ns['vec'];xy=ns['pair'];G=ns['G'];key=lambda z:(z.real,z.imag)
H=json.loads((R/'recovered_bundle/ant_global/root/standard.json').read_text())['word'];phases={H[i:]+H[:i]for i in range(104)}
def rev(p,h):return p-V[h],(h+2)%4
assert rev(*rev(0j,1))==(0j,1)and rev(0j,1)==(-1+0j,3)
# Verify the inverse algebra on both colors and all headings by literal updates.
for h in range(4):
 for b in(0,1):
  p=2+3j;r=p-V[h];B={r}if b else set();q,g=rev(p,h);C=set(B);old=q in C;C.symmetric_difference_update({q});g=(g+(-1 if old else 1))%4;q+=V[g];q,g=rev(q,g)
  assert q==r and g==(h+(-1 if b else 1))%4 and C==B^{r}
def replay(z,p,h):
 B={q:-i-1 for i,q in enumerate(sorted(G,key=key))};states=[];poses=[];mass=[];word='';dead={};events=[];first={}
 for t in range(z['prefix_length']):
  states.append(set(B));poses.append([xy(p),h]);mass.append(len(B));first.setdefault(p,t);old=B.pop(p,None);events.append(old)
  if old is None:B[p]=t;word+='R';h=(h+1)%4
  else:dead[old]=t;word+='L';h=(h-1)%4
  p+=V[h]
 states.append(set(B));poses.append([xy(p),h]);mass.append(len(B));assert(word,poses,mass)==(z['prefix_word'],z['prefix_poses'],z['prefix_masses']);assert [xy(p),h]==z['tail_pose']
 w,d,fates,checks=future(B,p,h);assert w in phases and(w,xy(d),checks)==(z['tail_word'],z['tail_drift'],z['tail_parity_tests']);dead.update({i:len(word)+k for i,k in fates.items()})
 assert [dict(cell=xy(q),identity=i,future_consumption=dead.get(i))for q,i in sorted(B.items(),key=lambda x:key(x[0]))]==z['complete_terminal_field']
 sums=[0]
 for c in w:sums.append(sums[-1]+(1 if c=='R'else-1))
 assert sums[-1]==12 and(min(sums),max(sums))==(z['tail_relative_mass_min'],z['tail_relative_mass_max'])and len(B)+min(sums)>4
 return B,p,h,states,poses,mass,dead,events,first
f=replay(J['forward'],0j,1);r=replay(J['reverse_conjugate'],-1+0j,3)
assert [i for i,x in enumerate(f[5])if x==min(f[5])]==[0,2]and min(f[5])==4
assert [i for i,x in enumerate(r[5])if x==min(r[5])]==[0]and min(r[5])==4
B=set(r[0]);p,h=rev(r[1],r[2]);assert (p,h)==(12-16j,3)and len(B)==150
neg=J['original_negative_endpoint'];assert sorted(map(xy,B))==neg['black']and[xy(p),h]==neg['pose']
bw=''
for t in range(1040):
 n=1040-t;assert B==r[3][n]and(p,h)==rev(complex(*r[4][n][0]),r[4][n][1]);b=p in B;B.symmetric_difference_update({p});bw+='L'if b else'R';h=(h+(-1 if b else 1))%4;p+=V[h]
assert(B,p,h)==(G,0j,1)and bw==neg['full_forward_recovery_word']and bw==J['reverse_conjugate']['prefix_word'][::-1].translate(str.maketrans('LR','RL'))
assert sorted(f[8][q]for q in G)==[1,22,32,58]
# Reconstruct ENTIRE relevant count using each actual current lifetime's true future fate.
B={q:-i-1 for i,q in enumerate(sorted(G,key=key))};p=0j;h=1;profile=[]
for t in range(391):
 profile.append(sum(i in f[6]for i in B.values()))
 if t==390:break
 if p in B:B.pop(p);h=(h-1)%4
 else:B[p]=t;h=(h+1)%4
 p+=V[h]
assert profile==J['forward_relevant_profile']and min(profile)==4 and[i for i,x in enumerate(profile)if x==4]==[0,2]
C0=None;tail=[];tests=[]
for t in range(105):
 w,d,fates,n=future(B,p,h);assert w in phases;C={q for q,i in B.items()if i in fates};tail.append(len(C));tests.append(n)
 if t==0:C0=C;startp=p;starth=h
 if t==104:assert C=={q+d for q in C0}and(p,h)==(startp+d,starth);break
 if p in B:B.pop(p);h=(h-1)%4
 else:B[p]=390+t;h=(h+1)%4
 p+=V[h]
assert tail==J['forward_tail_relevant_profile']and tests==J['forward_tail_phase_parity_tests']and(min(tail),max(tail))==(11,22)
out=dict(status='PASS exact two-sided G minimum4 and no bidirectionally unread current black sites',manifest=sha(M),script=sha(S),full_prefix_reads=1430,negative_replay_reads=1040,tail_phase_checks=len(tail),reverse_endpoint=[xy(r[1]),r[2],len(r[0])],actual_negative_pose=[[12,-16],3],global_mass_minimum=4,global_mass_minimum_times=[0,2],global_relevant_minimum=4,global_relevant_minimum_times=[0,2],analytic_review=['R is the actual edge-reversal involution and changes the pose parity sector. Literal two-color/all-heading algebra verifies F inverse=RFR; the original negative pose is R of the reverse-conjugate pose, not the same cursor. Every complete field and pose in the1040-step forward recovery is independently matched.','Both complete terminal fields satisfy exact all-k canonical104 ray parity. Their mass has12 gain per period and finite phase minimum above4. The two finite prefixes cover every other integer time, so only original cuts0,2 attain full mass4.','At each negative cut, any current black lifetime is consumed before0 or survives into one of the four G inputs, all consumed later. Thus ENTIRE C*=B there, without a backward pruning assumption. At positive cuts a permanent current lifetime still has its actual R birth in the past. Hence no current black physical site is unread in both time directions at any cut.','Exact forward lifetime fates include terminal ray hits; phase pruning closes by actual drift after104 and its cardinalities11..22 repeat forever. Thus whole forward-relevant minimum is4 also only0,2. Prune2 never reaches its small-pruning branch anywhere in this capturing orbit.','This falsifies only reduction to at-most-two full or relevant cells by time shift or two-sided archive deletion. It is not a counterexample to canonical capture, larger-class basin arguments, compact recurrence or other well-founded mechanisms.'])
S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
