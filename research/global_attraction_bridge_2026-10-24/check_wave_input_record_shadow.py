"""One genuine BLACK input shadows all interior-copy record events in three supplied words."""
from pathlib import Path
import json,hashlib
from record_event_projection import trace,dot,U,load
from check_return_permanent_output_debt import DXY,future
P=Path(__file__).parent;D=json.load(open(U/'prepared1564_uniform_support_manifest.json'));E=json.load(open(U/'prepared4352_capture_manifest.json'))
specs=[('1564',D['stages'][-1],1455),('4352',E['stages'][11],1687),('15324',E['stages'][13],4264)];proofs=[]
for name,s,i in specs:
 w=s['word'];Q,d,eh=trace(w,(0,0),s['heading']);q=Q[i];assert eh==s['heading']and w[i]=='L'
 hits=[];groups={}
 for j,z in enumerate(Q):
  r=z[0]%abs(d[0]);a=(z[0]-r)//d[0];rep=(r,z[1]-a*d[1]);groups.setdefault(rep,[]).append((a,j))
  x,y=z[0]-q[0],z[1]-q[1]
  if x%d[0]==0 and y==(x//d[0])*d[1]:hits.append([j,x//d[0],w[j]])
 assert all(m<=0 for j,m,c in hits)and min(j for j,m,c in hits if m==0)==i
 # Last-copy q+(N-1)d cannot have appeared in an earlier block copy.
 leadingL=[]
 for rep,z in sorted(groups.items()):
  a=max(x[0]for x in z);j=min(x[1]for x in z if x[0]==a)
  if w[j]=='L':leadingL.append(j)
 expected={'1564':197,'4352':406,'15324':1439};assert len(leadingL)==expected[name]
 bound=[max(dot(z,a)for z in Q)for a in range(4)];positive={}
 for a in range(4):
  delta=dot(d,a)
  if delta>0:
   diff=bound[a]-dot(q,a);C=(diff+delta-1)//delta;assert C==1
   assert all(dot(z,a)-dot(q,a)<=delta for z in Q)
   positive[a]=dict(delta=delta,maximum=bound[a],input_projection=dot(q,a),fringe=C,slack=delta-diff)
 proofs.append(dict(word=name,period=len(w),heading=s['heading'],word_sha256=hashlib.sha256(w.encode()).hexdigest(),drift=d,
  leading_first_L_orbits=len(leadingL),selected_phase=i,selected_relative_cell=q,all_same_drift_orbit_visits=hits,
  exact_positive_normal_inequalities=positive,first_last_only=True))
controls=[]
for family,n in [('184',4),('184',10),('394',1),('394',3)]:
 file='prepared1564_uniform_support_manifest.json'if family=='184'else'prepared4352_capture_manifest.json'
 seed,p,h,stages=load(file,n);B={q:-i-1 for i,q in enumerate(sorted(seed))};t=0;rows=[];births={};owned={}
 targets={'15:wave':proofs[0]}if family=='184'else{'11:wave':proofs[1],'13:return-wave':proofs[2]}
 for name,w,C in stages:
  if C is None:break
  target=targets.get(name)
  if target:
   assert h==target['heading']
   q=target['selected_relative_cell'];d=target['drift'];cell=(p[0]+q[0]+(C-1)*d[0],p[1]+q[1]+(C-1)*d[1]);owner=B[cell]
   due=t+len(w)*(C-1)+target['selected_phase'];rec=dict(stage=name,copies=C,block_start=t,block_pose=[p,h],input_cell=cell,input_owner=owner,
    first_block_read=due,full_entry_black_mass=len(B),full_entry_sha256=hashlib.sha256(json.dumps(sorted(B),separators=(',',':')).encode()).hexdigest(),prior_R_birth=births.get(owner))
   assert owner<0 or owner<t;pending=True
  for _ in range(C):
   for c in w:
    if target and p==cell and pending:
     assert t==due and B[p]==owner and c=='L';pending=False
    old=B.pop(p,None);assert(old is None)==(c=='R')
    if old is None:B[p]=t;births[t]=p
    h=(h+(1 if c=='R'else-1))%4;p=(p[0]+DXY[h][0],p[1]+DXY[h][1]);t+=1
  if target:assert not pending;rows.append(rec)
 # Exact complete final-board infinite parity, with no support truncation.
 tw,dr,_,tests=future(B,p,h);assert tw==stages[-1][1]
 controls.append(dict(family=family,parameter=n,physical_reads=t,initial_black=sorted(seed),targets=rows,terminal_pose=[p,h],terminal_full_black=sorted(B),terminal_word=tw,terminal_drift=dr,tail_parity_tests=tests));print(family,n,t,flush=True)
files=['COMPLETED_DROUGHT_COUNTS_MANIFEST.json','record_event_projection.py',
 '../causal_reduction/unit_scale/prepared1564_uniform_support_manifest.json','../causal_reduction/unit_scale/prepared1564_source_endpoint_family.json',
 '../causal_reduction/unit_scale/prepared4352_capture_manifest.json',
 '../audits/check_1564_constant_mass_family_independent.json','../audits/check_1564_family_endpoint_capture_independent.json',
 '../audits/check_4352_allM_capture_independent.json']
out=dict(status='AUTHOR exact general input-shadow lemma and three full-word specializations; audit pending',
 source_hashes={f:hashlib.sha256((P/f).read_bytes()).hexdigest()for f in files},word_proofs=proofs,literal_controls=controls,
 total_physical_reads=sum(z['physical_reads']for z in controls),scope='Any actual finite-board occurrence of N copies of each supplied word, any prior history and retained exterior. Union record cuts inside the half-open repeated block lie in its first or last copy. No arbitrary-word cover, no simultaneous arbitrary-wave concatenation theorem, no bound on number of separately generated blocks.')
(P/'WAVE_INPUT_RECORD_SHADOW_CHECKED.json').write_text(json.dumps(out,indent=2)+'\n')
