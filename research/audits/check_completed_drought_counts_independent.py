from pathlib import Path
from collections import defaultdict
import json,hashlib
S=Path(__file__).resolve();R=S.parents[1];D=R/'global_attraction_bridge_2026-10-24';U=R/'causal_reduction/unit_scale';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'COMPLETED_DROUGHT_COUNTS_MANIFEST.json'
assert sha(MF)=='6ef8a4682c7e9f6908b9653385c58d366d630d6153af2432b17ecd4962826a17'
for f,h in json.loads(MF.read_text())['files'].items():assert sha(D/f)==h
J=json.loads((D/'COMPLETED_DROUGHT_COUNTS_CHECKED.json').read_text())
for f,h in J['source_hashes'].items():assert sha(D/f)==h
lib=S.with_name('check_phase13_double_scatter_independent.py');ns={'__file__':str(lib)};exec(lib.read_text().split('# Canonical source')[0],ns);future,phases=ns['future'],ns['phases']
V=(1j,1,-1j,-1);xy=lambda p:[int(p.real),int(p.imag)];dot=lambda p,a:int((p.imag,p.real,-p.imag,-p.real)[a])
def geo(w,h):
 p=0j;qs=[]
 for c in w:qs.append(p);h=(h+(1 if c=='R'else-1))%4;p+=V[h]
 return qs,p,h
add=lambda a,b:(a[0]+b[0],a[1]+b[1]);neg=lambda a:(-a[0],-a[1]);mul=lambda a,k:(a[0]*k,a[1]*k);ev=lambda a,n:a[0]*n+a[1]
proj=lambda p,a:(p[1],p[0],neg(p[1]),neg(p[0]))[a]
def model(name):
 if name in('184','394'):
  f='prepared1564_uniform_support_manifest.json'if name=='184'else'prepared4352_capture_manifest.json';z=json.loads((U/f).read_text());st=[(str(i)+':'+q['kind'],q['word'],tuple(q['count_N_constant']))for i,q in enumerate(z['stages'])]
  if name=='184':e=json.loads((U/'prepared1564_source_endpoint_family.json').read_text());st +=[('endpoint_response',e['after_checkpoint_word'],(0,1)),('tail',e['capture_word'],None)]
  else:st +=[('tail',z['tail_word'],None)]
  return dict(name=name,n0=4 if name=='184'else 1,seed=z['seed_families'],pose=[z['initial_pose']['x_N_constant'],z['initial_pose']['y_N_constant']],h=z['initial_pose']['heading'],stages=st)
 g={-1j,1+1j,1+3j,2+2j};B=set(g);p=0j;h=1;w=''
 for i in range(286):
  c='L'if p in B else'R';w+=c;B.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p+=V[h]
 A,W=w[:182],w[182:];poses=[((0,0),(0,0)),((14,-1),(14,0)),((10,0),(18,-4)),((2,5),(10,0))];hs=[1,0,3,2];cts=[(7,-4),(2,-5),(4,-6),(2,-6)];parts=[61,71,61,56];seed=[];st=[]
 for j in range(4):
  for q in g:
   q*=(-1j)**(hs[j]-1);seed.append([add(poses[j][0],(0,int(q.real))),add(poses[j][1],(0,int(q.imag)))])
  st +=[(f'port{j}',A,(0,1)),(f'flight{j}',W,cts[j]),(f'partial{j}',W[:parts[j]],(0,1))]
 z=json.loads((D/'TRANSVERSE_FAR_MODULE_SOURCE.json').read_text());st +=[('recovery',z['post_contact_word'],(0,1)),('tail',z['tail_word'],None)]
 return dict(name='16',n0=10,seed=seed,pose=((0,0),(0,0)),h=1,stages=st)
models={name:model(name)for name in('184','394','16')}

def affine(m):
 n0=m['n0'];checks=[]
 def ge(a):assert a[0]>=0 and ev(a,n0)>=0,a;checks.append(a)
 def maxa(xs):
  best=max(xs,key=lambda a:(ev(a,n0),a[0]))
  for a in xs:ge(add(best,neg(a)))
  return best
 def gt(a):
  if a[0]>=0 and ev(a,n0)>0:ge(add(a,(0,-1)));return True
  assert a[0]<=0 and ev(a,n0)<=0,a;ge(neg(a));return False
 p=tuple(map(tuple,m['pose']));h=m['h'];T=(0,0);seed=[tuple(map(tuple,q))for q in m['seed']];M=[maxa([proj(q,a)for q in seed+[p]])for a in range(4)];initial=M[:];st=[];geometry=[]
 for name,w,C in m['stages']:
  Q,d,hh=geo(w,h);P=len(w);first=[];rays=[];old=M[:]
  if C is None or C!=(0,1):assert hh==h
  if C is not None:ge(add(C,(0,-1)))
  for a in range(4):
   vals=[dot(q,a)for q in Q];B=max(vals);dd=dot(d,a);start=proj(p,a);rec=-10**30
   for i,v in enumerate(vals):
    if v>rec and gt(add(add(start,(0,v)),neg(M[a]))):first.append([i,a])
    rec=max(rec,v)
   if dd>0 and C!=(0,1):
    rec=B-dd
    for i,v in enumerate(vals):
     if v>rec:
      z=add(M[a],neg(add(start,(0,v))));assert z[0]%dd==0;lo=maxa([(0,1),(z[0]//dd,z[1]//dd+1)])
      if C is None or gt(add(C,neg(lo))):rays.append(dict(phase=i,normal=a,lo=list(lo),hi=None if C is None else list(C)))
     rec=max(rec,v)
   if C is not None:
    bound=add(start,(0,B))
    if dd>0:bound=add(bound,mul(add(C,(0,-1)),dd))
    M[a]=maxa([M[a],bound])
  st.append(dict(stage=name,start=list(T),period=P,count=None if C is None else list(C),first=sorted(first),rays=rays));geometry.append(dict(stage=name,start_pose=list(map(list,p)),heading=h,drift=xy(d),old_hull=list(map(list,old)),end_hull=list(map(list,M))))
  if C is None:break
  T=add(T,mul(C,P));p=(add(p[0],mul(C,int(d.real))),add(p[1],mul(C,int(d.imag))));h=hh
 ref=next(r for r in J['all_parameter_proofs']if r['name']==m['name']);assert st==ref['stages']and geometry==ref['geometry']and list(map(list,initial))==ref['initial_hull']
 for label,a in ref['inequalities']:assert a[0]>=0 and ev(a,n0)>=0
 events=[];tails=[]
 for r in st:
  T=tuple(r['start']);P=r['period']
  events +=[(add(T,(0,i)),a)for i,a in r['first']]
  for z in r['rays']:
   t=add(add(T,mul(tuple(z['lo']),P)),(0,z['phase']))
   if z['hi']is None:tails.append((t,z['normal'],z['phase'],tuple(z['lo'])))
   else:assert add(tuple(z['hi']),neg(tuple(z['lo'])))==(0,1);events.append((t,z['normal']))
 events.sort(key=lambda z:ev(z[0],n0));tails.sort(key=lambda z:ev(z[0],n0));times=[z[0]for z in events]+[tails[0][0]];gaps=[add(b,neg(a))for a,b in zip(times,times[1:])]
 for a,b in zip(times,times[1:]):assert gt(add(b,neg(a)))
 for z in tails:ge(add(z[0],neg(tails[0][0])))
 assert list(map(list,gaps))==ref['record_inventory']['all_pre_tail_completed_gaps']
 return dict(name=m['name'],independent_affine_checks=len(checks),bound_author_inequalities=ref['inequality_count'],initial_hull=initial,events=events,tail_rays=tails,completed_pre_tail_gaps=gaps)
proofs=[affine(m)for m in models.values()]

def spec(m,n):return({complex(ev(q[0],n),ev(q[1],n))for q in m['seed']},complex(*[ev(q,n)for q in m['pose']]),m['h'],[(name,w,None if C is None else ev(C,n))for name,w,C in m['stages']])
def numeric(seed,p,h,st):
 M=[max(dot(q,a)for q in seed|{p})for a in range(4)];T=0;regions=[]
 for name,w,C in st:
  Q,d,hh=geo(w,h);Q=[q+p for q in Q];P=len(w);fst=[];activation=defaultdict(list)
  for a in range(4):
   vals=[dot(q,a)for q in Q];B=max(vals);dd=dot(d,a);old=M[a]
   for i,v in enumerate(vals):
    if v>old:fst.append((i,a));old=v
   if dd>0 and C!=1:
    rec=B-dd
    for i,v in enumerate(vals):
     if v>rec:
      lo=max(1,(M[a]-v)//dd+1)
      if C is None or lo<C:activation[lo].append((i,a))
     rec=max(rec,v)
   M[a]=max(M[a],B+(C-1)*dd if C and dd>0 else B)
  if fst:regions.append(dict(stage=name,start=T,period=P,lo=0,hi=1,phases=list(map(list,sorted(fst)))))
  act=[];ks=sorted(activation)
  for j,k in enumerate(ks):
   act=sorted(act+activation[k]);hi=ks[j+1]if j+1<len(ks)else C
   if hi is None or k<hi:regions.append(dict(stage=name,start=T,period=P,lo=k,hi=hi,phases=list(map(list,act))))
  if C is None:break
  T+=P*C;p+=d*C;h=hh
 return regions

def counts(reg,H):
 last=None;n=0;lengths=[]
 for r in reg:
  P,T,lo,hi,ph=[r[x]for x in('period','start','lo','hi','phases')];first=T+P*lo+ph[0][0]
  if last is not None and first-last>H:n+=1;lengths.append(first-last)
  copies=None if hi is None else hi-lo
  for u,v in zip(ph,ph[1:]):
   if v[0]-u[0]>H:
    assert copies is not None;n+=copies;lengths.extend([v[0]-u[0]]*copies)
  gap=P+ph[0][0]-ph[-1][0]
  if gap>H and(copies is None or copies>1):assert copies is not None;n+=copies-1;lengths.extend([gap]*(copies-1))
  if hi is None:break
  last=T+P*(hi-1)+ph[-1][0]
 return n,lengths

def control_spec(r):
 name=r['name']
 if name.startswith('184'):
  n=int(name.split('N')[1]);seed,p,h,st=spec(models['184'],n)
  if n<4:
   e=json.loads((U/f'prepared1564_endpoint_N{n}.json').read_text());st[-2:]=[('end_response',e['continuation_word'],1),('tail',e['capture_word'],None)]
  else:st[-2]=( 'end_response',st[-2][1],1)
  return seed,p,h,st
 if name.startswith('394'):return spec(models['394'],int(name.split('M')[1]))
 if name.startswith('16'):return spec(models['16'],int(name.split('n')[1])//2)
 n=int(name.rsplit('n',1)[1]);rr=next(c for c in json.loads((D/'TWO_TRANSVERSE_MODULES_CHECKED.json').read_text())['controls']if c['n2']==n);m=models['16'];st0=spec(m,10)[3][:-2];st1=spec(m,n//2)[3][1:-2];F=m['stages'][-2][1];W=m['stages'][1][1]
 return {complex(*q)for q in rr['initial_black']},0j,1,st0+[('first_recovery',F,1),('interflight',W,rr['spacing_periods'])]+st1+[('second_recovery',F,1),('tail',W,None)]
controls=[];total=0
for r in J['full_field_controls']+J['paid_concatenations']:
 seed,p,h,st=control_spec(r);assert sorted(map(xy,seed))==r['initial_black']and[xy(p),h]==r['initial_pose'];reg=numeric(seed,p,h,st);assert reg==r['event_regions'];B=set(seed);hull=[max(dot(q,a)for q in seed|{p})for a in range(4)];rec=[];t=0;snaps=[]
 for name,w,C in st:
  if C is None:tail=w;break
  for _ in range(C):
   for c in w:
    for a in range(4):
     z=dot(p,a)
     if z>hull[a]:assert z==hull[a]+1;hull[a]=z;rec.append([t,a])
    assert(p in B)==(c=='L'),(r['name'],t,p);B.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p+=V[h];t+=1
  digest=hashlib.sha256(json.dumps(sorted(map(tuple,map(xy,B))),separators=(',',':')).encode()).hexdigest();snaps.append(dict(stage=name,cut=t,pose=[xy(p),h],full_mass=len(B),full_field_sha256=digest))
 assert snaps==r['stage_full_field_checks']and t==r['terminal_cut']and[xy(p),h]==r['terminal_pose']and sorted(map(xy,B))==r['terminal_full_black']
 tw,dr,dead,tests=future({q:i for i,q in enumerate(sorted(B,key=lambda q:(q.real,q.imag)))},p,h);assert tw==tail and tw in phases and xy(dr)==r['tail_drift']
 for c in tail*2:
  for a in range(4):
   z=dot(p,a)
   if z>hull[a]:hull[a]=z;rec.append([t,a])
  assert(p in B)==(c=='L');B.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p+=V[h];t+=1
 assert t==r['physical_updates']and rec==r['record_cuts'];total+=t
 cs={str(H):counts(reg,H)for H in(104,3390)}
 for H in(104,3390):assert cs[str(H)][0]==r[f'long_gap{H}']['count']
 controls.append(dict(name=r['name'],reads=t,records=rec,gaps=cs,terminal_mass=len(r['terminal_full_black']),infinite_tests=tests));print(r['name'],'PASS',t,flush=True)
assert total==3177971==J['total_physical_updates']
for name,m in models.items():
 seed,p,h,st=spec(m,10**9);reg=numeric(seed,p,h,st);r=next(r for r in J['huge_parameter_geometry_controls']if r['name']==name);assert reg==r['event_regions']and counts(reg,104)[0]==(3 if name=='16'else 4)
# Exact changed-initial-hull qualification for both finite concatenations.
base=next(r for r in J['full_field_controls']if r['name']=='16_n20');seed0={complex(*q)for q in base['initial_black']}
for r in J['paid_concatenations']:
 seed={complex(*q)for q in r['initial_black']};assert seed0<seed;mask=r['prefix_hull_mask'];assert sorted(map(xy,seed-seed0))==mask['added_cells']
 old=[max(dot(q,a)for q in seed0)for a in range(4)];new=[max(dot(q,a)for q in seed)for a in range(4)];assert old==mask['old_initial_hull']and new==mask['new_initial_hull']
 assert[(z['cut'],z['normal'])for z in mask['removed_record_events']]==[(3,2),(7074,1)]and[(z['cut'],z['normal'])for z in mask['retained_record_events']]==[(8863,0),(8877,0)]
 for z in mask['removed_record_events']:assert dot(complex(*z['pose']),z['normal'])<=new[z['normal']]
 for z in mask['retained_record_events']:assert dot(complex(*z['pose']),z['normal'])>new[z['normal']]
out=dict(status='PASS exact completed augmented-record drought inventories and scoped finite-template bound',manifest=sha(MF),source_hashes=J['source_hashes'],independent_all_parameter_proofs=proofs,full_controls=controls,total_literal_reads=total,analytic=[
'Read-position cuts include each block entry and exclude its endpoint; the next block includes that endpoint. Initial hull includes ENTIRE original support and initial head. Initial waiting before the first strict event is not a completed gap. All12 whole-field runs and infinite canonical parity are independent.',
'For each axis, positive drift stable phase requires beating both earlier same-copy phases and previous-copy maximum B-delta, plus the initial hull threshold. Nonpositive drift has no later-copy records. Every phase is inspected, and all affine max/sign comparisons are proved on the entire half-line from the stated lower bound; divisible slopes make floors exactly affine with no missing residues. All stage geometries/hulls/events/rays equal the frozen data, including empty waves.',
'The exact184 family has4 gaps>104 and2>3390, retaining literal N1/2/3 exceptional tails. The signed394 subfamily M>=1 likewise has4 and2; no other originalN is included. Sixteen-cell even n=2k>=20 has exactly3 gaps>104 with lengths728k-209,208k-291,936k+7756; all3 can exceed any prescribed H by a sufficiently large member.',
'Both paid28 controls have exactly3 gaps>104. Added unread original cells raise the E/S support bounds and erase the unchanged first-module S3/E7074 pristine events, while N8863/8877 remain. This proves nonadditivity of this particular concatenation, not an all-length concatenation count law.',
'For a fixed legal finite template with repeated periods<=H, a repeated block has at most one internal>H gap: first-copy events span<P; once the first stable ray starts it recurs everyP until the block ends. A one-copy lengthL block has at most floor((L-1)/(H+1)) such gaps. At mostf+r-1 gaps bridge nonempty blocks, even across empty blocks. With tail included inr this gives f+2r-1+sum floor((L-1)/(H+1)). Heading restoration, finite stage count and bounded finite lengths are hypotheses, not inferred for general ants.',
'Neither the geometric projector nor the huge-parameter10^9 checks prove legality by themselves; whole-word legality and full infinite fields come from bound signed source families and the fresh literal controls. No universal seed-mass renewal budget, nontranslator occurrence, lifetime-age bound or canonical uniqueness follows.'
])
S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
