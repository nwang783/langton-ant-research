from pathlib import Path
from collections import Counter
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'global_attraction_bridge_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'PHASE13_DOUBLE_SCATTER_MANIFEST.json';assert sha(MF)=='ed0470780a9194585a0a04395b29f696ac9e81228a269984bba07665ccd034b0'
for f,h in json.loads(MF.read_text())['sha256'].items():assert sha(D/f)==h
J=json.loads((D/'PHASE13_DOUBLE_SCATTER_CHECKED.json').read_text());G=json.loads((D/'COMPARISON_PERTURBATION_EVENT_CHECKED.json').read_text())
for f,h in J['source_hashes'].items():assert sha(D/f)==h
assert G['reference_source_sha256']==sha(D/G['reference_source'])
ns={'__file__':str(S.with_name('check_all_length_two_sided_minimum_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Derive W')[0],ns);K,V,xy,future,phases,geometry=[ns[k]for k in('K','V','xy','future','phases','geometry')];key=lambda z:(z.real,z.imag)
def sim(seed,N,p=0j,h=1,expected=None,cuts=()):
 B={q:-i-1 for i,q in enumerate(sorted(seed,key=key))};pts=[];heads=[];first={};dead={};events=[];word=[];snap={}
 for t in range(N):
  if t in cuts:snap[t]=(dict(B),p,h)
  pts.append(p);heads.append(h);first.setdefault(p,t);i=B.pop(p,None);events.append(i)
  if i is None:B[p]=t;c='R';h=(h+1)%4
  else:dead[i]=t;c='L';h=(h-1)%4
  if expected is not None:assert c==expected[t],(t,c,expected[t])
  word.append(c);p+=V[h]
 return dict(B=B,p=p,h=h,pts=pts,heads=heads,first=first,dead=dead,events=events,word=''.join(word),snap=snap)
def cert(z,word=None):
 w,d,f,n=future(z['B'],z['p'],z['h']);assert w in phases
 if word is not None:assert w==word
 z.update(tail=w,d=d,tests=n);z['dead'].update({i:len(z['word'])+t for i,t in f.items()});return z
# Canonical source, complete first-visit ray and exact mature southern restriction.
z=cert(sim(K,104));W=z['word'];assert W==json.loads((D/'ALL_LENGTH_TWO_SIDED_MINIMUM_CHECKED.json').read_text())['base_word'];assert z['tail']==W and z['d']==2+2j
Q,HH,_,_=geometry(0j,1,W);phase=13;assert Q[phase]==2+1j and HH[phase]==0
for i,q in enumerate(Q):
 delta=Q[phase]-q
 if int(delta.real)%2==0 and delta.imag==delta.real:
  a=int(delta.real)//2;assert i+104*a>=phase,(i,a)
M=set();write_sources=[]
for i,q in enumerate(Q):
 r=q-Q[phase];lo=-((int(r.imag)+12)//2);hi=0 if i<phase else-1
 for a in range(lo,hi+1):M.symmetric_difference_update({r+a*(2+2j)});write_sources.append((i,a,r+a*(2+2j)))
assert 0j not in M and 2+2j not in M
kernel=M|{0j,2+2j};assert len(kernel)==96 and sorted(map(xy,kernel))==J['kernel']
z=cert(sim(kernel,5915,0j,0,J['post_word']),J['tail_word']);assert(z['p'],z['h'],z['d'],z['tests'])==(-18+17j,1,-2+2j,J['full_future_parity_tests'])
assert sorted(map(xy,z['B']))==J['terminal_full_black']
TQ,TH,_,_=geometry(z['p'],z['h'],z['tail']);assert min(q.imag for q in z['pts']+TQ)==-12 and z['d'].imag==2
assert [int(min(q.real for q in z['pts'])),int(max(q.real for q in z['pts'])),int(min(q.imag for q in z['pts'])),int(max(q.imag for q in z['pts']))]==J['prefix_bbox']
C={q for i,q in enumerate(sorted(kernel,key=key))if -i-1 in z['dead']};assert len(C)==71 and sorted(map(xy,C))==J['kernel_entire_pruning'];assert max(max(abs(q.real),abs(q.imag))for q in C)==14
births={}
for q in M:
 cand=[]
 for i,r in enumerate(Q):
  v=q+Q[phase]-r
  if int(v.real)%2==0 and v.imag==v.real:
   a=int(v.real)//2;t=104*a+i-phase
   if t<0:cand.append((t,a,i))
 t,a,i=max(cand);assert W[i]=='R'and a>=-9;births[q]=t
assert [dict(cell=xy(q),time=t)for q,t in sorted(births.items(),key=lambda x:key(x[0]))]==J['kernel_old_birth_offsets']
imports=[dict(cell=xy(q),birth_relative=births[q],death_relative=z['dead'][-i-1])for i,q in enumerate(sorted(kernel,key=key))if q in M and -i-1 in z['dead']];assert imports==J['old_wake_consumptions']and len(imports)==69 and all(x['death_relative']<5915 for x in imports)
hits={}
for t,q in enumerate(z['pts']):
 if q.real==q.imag and int(q.real)%2==0 and q.real>=4:hits.setdefault(int(q.real)//2,t)
tailhits=[]
for i,q in enumerate(TQ):
 x,y=map(int,(q.real,q.imag))
 if (x+y)%4:continue
 a=(x+y)//4
 if a<2 or(x-2*a)%2:continue
 k=(x-2*a)//2
 if k>=0:tailhits.append((a,k,i))
assert not tailhits and hits=={2:632,3:672,4:844,5:1248,6:1272}and hits=={int(a):t for a,t in J['remaining_ray_first_reads'].items()}
# Directly check the changed guard and isolated-rule interface, not merely ideal replay.
old=json.loads((D/'ALL_LENGTH_TWO_SIDED_MINIMUM_CHECKED.json').read_text());isolated=set(map(lambda q:complex(*q),old['rule']['input_kernel']));v=old['rule']['recovery'];sm=sim(isolated|{2+2j},203,0j,0,z['word'][:203]);assert(sm['p'],sm['h'])==(-4-1j,3)and sm['p']not in sm['B'];assert z['pts'][203]==-4-1j and z['word'][203]=='L'and births[-4-1j]==-17
vp=geometry(0j,HH[13],v)[0];assert max(q.imag for q in vp)<=20
assert max(q.imag-Q[13].imag for q in Q)<=20
synthetic=6+max(Q[i].imag-Q[97].imag+(0 if i<97 else-2)for i in range(104));assert synthetic==11<=20<194
assert max(q.imag for q in K)==6 and max(q.imag for q in Q)-2==6
# The actual final free flight starts at (2,6), phase97; reconstruct full endpoint displacement.
F=W[97:]+W*100+W[:13];fp,fh,ep,eh=geometry(2+6j,HH[97],F);assert(ep,eh)==(206+206j,HH[13]);assert min(q.real for q in fp)>=-3
for k in [9,10,100]:assert 2*k+1-12>=7
controls=[]
for row in J['controls']:
 k=row['k'];m=row['isolated_prefix_count'];q=complex(*row['entry_pose'][0]);A={q+2*a*(1+1j)for a in row['extra_indices']}
 if m is None:assert q==2*k+2+(2*k+1)*1j;prefix=W*k+W[:13];markers=set()
 else:assert q==202+201j+m*(206+206j);prefix=W*100+W[:13]+(v+F)*m;markers={202+201j+i*(206+206j)for i in range(m)}
 seed=K|markers|{q,q+2+2j}|A;assert sorted(map(xy,seed))==row['seed'];T=len(prefix);u=cert(sim(seed,T+5915,expected=prefix+z['word'],cuts={T}),z['tail']);B,p,h=u['snap'][T]
 assert(p,h)==(q,0)and T==row['entry_time'];assert u['first'][q]==T and u['first'][q+2+2j]==T+124
 assert{r-q for r in B if r.imag>=q.imag-12 and r not in A}==kernel
 contact=[dict(cell=xy(r),identity=i,death=u['dead'].get(i))for r,i in sorted(B.items(),key=lambda x:key(x[0]))];assert contact==row['entry_complete_field']
 relevant={r for r,i in B.items()if i in u['dead']};assert relevant=={q+r for r in C}and sorted(map(xy,relevant))==row['entry_entire_pruning']
 assert all(B[q+r]==T+t for r,t in births.items());assert u['events'][T+203]==T-17
 imp=[dict(cell=xy(r),birth=i,death=u['dead'][i])for r,i in B.items()if i>=0 and i in u['dead']];assert sorted(imp,key=lambda r:r['death'])==row['old_wake_imports']
 assert all(r not in u['first']for r in A)and all(-i-1 not in u['dead']for i,r in enumerate(sorted(seed,key=key))if r in A)
 assert sorted(map(xy,u['B']))==row['terminal_full_black']and [xy(u['p']),u['h']]==row['terminal_pose']and xy(u['d'])==row['tail_drift']and u['tests']==row['full_future_parity_tests']
 controls.append(dict(name=row['name'],reads=T+5915,entry_population=len(relevant),old_imports=len(imp),all_extras_never_read=True))
# Independently reconstruct generic exact first-hit and complete XOR successor fields.
def firsthit(A):
 ans=[]
 for q in A:
  if q in z['first']:ans.append((z['first'][q],q))
  for i,r in enumerate(TQ):
   dx,dy=map(int,(q.real-r.real,q.imag-r.imag));ddx,ddy=map(int,(z['d'].real,z['d'].imag))
   if dx%ddx==0 and dy==(dx//ddx)*ddy and dx//ddx>=0:ans.append((5915+104*(dx//ddx)+i,q))
 return min(ans,key=lambda x:x[0])if ans else None
odd=set()
for q in TQ:odd.symmetric_difference_update({q})
def terms(t,A):
 if t<=5915:
  B=set(kernel)
  for q in z['pts'][:t]:B.symmetric_difference_update({q})
  raw=[(q,0j,1)for q in sorted(B,key=key)]
 else:
  k,r=divmod(t-5915,104);raw=[(q,0j,1)for q in sorted(z['B'],key=key)]
  if k:raw +=[(q,z['d'],k)for q in sorted(odd,key=key)]
  part=set()
  for q in TQ[:r]:part.symmetric_difference_update({q+k*z['d']})
  raw +=[(q,0j,1)for q in sorted(part,key=key)]
 return raw+[(q,0j,1)for q in sorted(A,key=key)]
def encode(ts):return [[xy(q),xy(d),n]for q,d,n in ts]
def contains(ts,q):
 bit=0
 for p,d,n in ts:
  if not d:bit^=int(q==p and n>0)
  else:
   dx,dy=map(int,(q.real-p.real,q.imag-p.imag));sx,sy=map(int,(d.real,d.imag))
   if dx%sx==0 and dy==(dx//sx)*sy and 0<=dx//sx<n:bit^=1
 return bit
eventchecks=[]
for row in G['controls']+[G['huge_control']]:
 A={complex(*q)for q in row['extra']};assert not A&kernel;hit=firsthit(A);r=row['result']
 if hit is None:assert r['kind']=='CERTIFIED unchanged complete future'and r['retained_unread_extra']==sorted(map(xy,A));eventchecks.append(dict(nohit=True));continue
 t,q=hit;assert r['time']==t and r['cell']==xy(q);hin=z['heads'][t]if t<5915 else TH[(t-5915)%104];hout=(hin-1)%4;assert r['incoming_heading']==hin and r['new_pose']==[xy(q+V[hout]),hout]
 ts=terms(t,A);assert contains(ts,q)==1 and contains(terms(t,set()),q)==0;ts.append((q,0j,1));assert encode(ts)==r['new_full_field_terms']
 if t<100000:
  u=sim(kernel|A,t+1,0j,0);assert(u['p'],u['h'])==(q+V[hout],hout)
  B=set()
  for p,d,n in ts:
   for k in range(n):B.symmetric_difference_update({p+k*d})
  assert B==set(u['B'])and sorted(map(xy,B))==r['literal_final_black']
 else:assert t==104000005907 and len(ts)==613
 eventchecks.append(dict(time=t,terms=len(ts)))
out=dict(status='PASS exact phase13 double-scatter southern interface and generic first-event emitter',manifest=sha(MF),script=sha(S),kernel_size=96,relevant_input_size=71,relevant_radius=14,old_wake_imports=69,full_future_parity_checks=z['tests'],controls=controls,generic_event_controls=eventchecks,analytic_review=[
'Actual canonical K word and genuine phase13 first-visit ordering rebuilt. Southern mature field is the exact XOR of all eligible prior translated reads, not an assumed infinite preparation. Every surviving kernel birth lies at relative period index>=-9; all omitted prestart writes and original K cells have y<=6, below the actual guard2k-11>=7 for k>=9.',
'The96-cell complete kernel executes all5915 reads and exact NW104 future against its ENTIRE537-cell terminal field. Prefix and every tail ray stay y>=-12. All71 initial relevant cells and69 actual old-wake births/deaths are checked. The isolated western crop first fails at203 by consuming genuineR-17 at(-4,-1); it cannot be carried unchanged into the double-input rule.',
'For a finite isolated-scatter prefix, all older nonmarker history before the last free flight and the replacement synthetic past lie below previous-marker y+20. This follows from the complete canonical phase span,312-read recovery footprint and earlier stage separation206, not merely the old western crop. The next SOUTHERN guard is previous-marker y+194. Thus no older omitted archive enters the new protected half-plane, and the actual last flight supplies the exact mature southern field. All later markers remain unread by exact first-visit ordering and connector coordinate bounds.',
'Exact ray equations over all104 tail phases add no forward NE-ray contacts. Only indices2..6 are exposed, at632/672/844/1248/1272. Any finite arbitrary suffix at indices>=7 is retained and never read; those bits were already absent from TRUE C* at contact, not relevance erased without consumption. No close-cohort or arbitrary-inside-guard field is covered.',
'Generic comparison module verifies the supplied finite-prefix/full canonical tail first, then minimizes exact prefix/ray hits for every extra initially-WHITE cell. Until the first omitted input, the actual complete trajectory agrees; its reference color is necessarily WHITE and actual turnL. Complete successor XOR terms retain every old bit, the entire long generated wake and partial period. The huge104000005907 event is checked with613 terms without materializing the wake.',
'The closed class permits any finite number of paid isolated markers before the terminal adjacent pair, plus an arbitrary finite permitted unread ray suffix. It is not autonomous regeneration, unrestricted perturbation coverage, a finite-state representation of arbitrary geometry, or termination of repeated generic collision iteration.'
]);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
