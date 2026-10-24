"""Verify all-N endpoint stabilization, all small exceptions and complete standard tails."""
from pathlib import Path
from collections import defaultdict,Counter
import json,hashlib
from common import periodic
SELF=Path(__file__).resolve();DATA=json.loads(SELF.with_name('family_data.json').read_text());M=DATA['family'];A=DATA['uniform_endpoint'];H=DATA['standard_word'];W=M['stages'][-1]['word'];word=A['after_checkpoint_word'];V=((0,1),(1,0),(0,-1),(-1,0))
assert len(word)==56504 and len(W)==1564
def trace(w,p,h):
 rows=[]
 for c in w:
  rows.append((p,c));h=(h+(1 if c=='R'else-1))%4;v=V[h];p=p[0]+v[0],p[1]+v[1]
 return rows,p,h

def replay_prefix(n):
 seed={(x[0]*n+x[1],y[0]*n+y[1])for x,y in M['seed_families']};assert len(seed)==184
 b=set(seed);p=(33+14*n,70+14*n);h=3;letters=[]
 # True inverse history, not an arbitrary standard prehistory.
 back=set(seed);q=p;hh=h;rev=[]
 for _ in range(10):
  d=V[hh];q=q[0]-d[0],q[1]-d[1];post=q in back;rev.append('R'if post else'L');hh=(hh+(-1 if post else 1))%4;back.symmetric_difference_update({q})
 assert ''.join(rev[::-1])=='LRLRRRRLLL'
 for st in M['stages']:
  assert p==(st['start_x_N_constant'][0]*n+st['start_x_N_constant'][1],st['start_y_N_constant'][0]*n+st['start_y_N_constant'][1])and h==st['heading']
  count=st['count_N_constant'][0]*n+st['count_N_constant'][1]
  for c in st['word']*count:
   assert (p in b)==(c=='L');letters.append(c);b.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;d=V[h];p=p[0]+d[0],p[1]+d[1]
 assert len(letters)==91747+25588*n and p==(14*n-6,14*n-6)and h==0 and len(b)==10805+2876*n
 return seed,b,p,h,''.join(letters)
seed,B4,p4,h4,pre4=replay_prefix(4);checkpoint={(x-56,y-56)for x,y in B4};assert (p4,h4)==((50,50),0)
rows,exitp,exith=trace(word,(-6,-6),0);assert(exitp,exith)==((-104,-24),0);Q=sorted({q for q,c in rows});assert len(Q)==11684
# A complete normalized seed/read family has coordinates b+a*N+d*k.
families=defaultdict(list)
for st in M['stages']:
 b=(st['start_x_N_constant'][1],st['start_y_N_constant'][1]);a=(st['start_x_N_constant'][0]-14,st['start_y_N_constant'][0]-14);ss,end,eh=trace(st['word'],b,st['heading']);count=tuple(st['count_N_constant']);d=(end[0]-b[0],end[1]-b[1])if count!=(0,1)else(0,0)
 assert a[0]==a[1]and d[0]==d[1]
 for q,c in ss:families[q[0]-q[1]].append((q,a,d,count))
for x,y in M['seed_families']:
 b=(x[1],y[1]);a=(x[0]-14,y[0]-14);assert a[0]==a[1];families[b[0]-b[1]].append((b,a,(0,0),(0,1)))

def interval(q,f):
 b,a,d,count=f
 if d==(0,0):
  candidates=[]
  for j in (0,1):
   diff=q[j]-b[j]
   if a[j]:
    if diff%a[j]:return None
    candidates.append(diff//a[j])
   elif diff:return None
  if not candidates:return(1,None)
  if min(candidates)!=max(candidates)or candidates[0]<1:return None
  return candidates[0],candidates[0]
 # Exact integral k=alpha*N+beta; verify both coordinates, not just normal.
 assert a[0]%d[0]==0
 if (q[0]-b[0])%d[0]:return None
 alpha=-a[0]//d[0];beta=(q[0]-b[0])//d[0]
 if b[1]+d[1]*beta!=q[1]or a[1]+d[1]*alpha!=0:return None
 lower=1;upper=None
 for slope,constant in [(alpha,beta),(count[0]-alpha,count[1]-1-beta)]:
  if slope>0:lower=max(lower,(-constant+slope-1)//slope)
  elif slope<0:
   u=constant//(-slope);upper=u if upper is None else min(upper,u)
  elif constant<0:return None
 if upper is not None and lower>upper:return None
 # Non-vacuous endpoint check of all repeat bounds.
 for n in [lower]+([]if upper is None else[upper]):
  k=alpha*n+beta;assert 0<=k<count[0]*n+count[1]and tuple(b[j]+a[j]*n+d[j]*k for j in (0,1))==q
 return lower,upper

proof=[];eligible=0;lastbad=0;exceptioncells=0
for q in Q:
 events=Counter()
 for f in families.get(q[0]-q[1],()):
  bounds=interval(q,f)
  if bounds is None:continue
  eligible+=1;l,u=bounds;events[l]+=1
  if u is not None:events[u+1]+=1
 cuts=sorted({1}|{n for n,c in events.items()if c%2});bit=False;wanted=q in checkpoint;exceptions=[]
 for i,n in enumerate(cuts):
  bit^=bool(events[n]%2);end=cuts[i+1]-1 if i+1<len(cuts)else None
  if bit!=wanted:
   assert end is not None;exceptions.append([n,end]);lastbad=max(lastbad,end)
 if exceptions:exceptioncells+=1
 proof.append([list(q),int(wanted),exceptions])
assert eligible==33568 and exceptioncells==514 and lastbad==3
proofhash=hashlib.sha256(json.dumps(proof,separators=(',',':')).encode()).hexdigest();assert proofhash=='2bf62f8023e078e36a818a179b8e7c5d3800fe9cfd1256e121aa2b7a9e79129b'
# Literal continuation from independently reconstructed N4 field.
b=set(checkpoint);p=(-6,-6);h=0;X=set()
for q,c in rows:
 assert p==q and (p in b)==(c=='L');b.symmetric_difference_update({p});X.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;d=V[h];p=p[0]+d[0],p[1]+d[1]
assert(p,h)==(exitp,exith)
missing=(31,71);assert all(interval(missing,f)is None for f in families[missing[0]-missing[1]])
extra=W*3+W[:854];assert word.startswith(extra)and word[len(extra)]=='R'and W[854]=='L';er,ep,eh=trace(extra,(-6,-6),0);assert (ep,eh)==(missing,2)and missing not in {q for q,c in er}
tail=A['capture_word'];assert tail in {H[i:]+H[:i]for i in range(104)};tr,te,th=trace(tail,p,h);norms=[q[0]-q[1]for q,c in tr];hull=[min(norms),max(norms)];prodmin=min(families);assert hull==[-86,-76]and prodmin==-72
restricted={q for q in X if hull[0]<=q[0]-q[1]<=hull[1]};assert len(restricted)==508 and restricted=={q for q in b if hull[0]<=q[0]-q[1]<=hull[1]}
earliest,d,groups,critical=periodic(restricted,p,h,tail);assert earliest is None and d==(-2,-2)
for q in groups:
 far=(q[0]-2000000,q[1]-2000000);assert periodic(restricted^{far},p,h,tail)[0]is not None
# Exact seam K and final charge, independent packed detector.
allowed={int(''.join('1'if c=='L'else'0'for c in (H*2)[i:i+10]),2)for i in range(104)}
def cost(previous,w):
 state=int(''.join('1'if c=='L'else'0'for c in previous),2);old=state not in allowed;K=0
 for c in w:
  state=((state<<1)|(c=='L'))&1023;new=state not in allowed;K+=old and new;old=new
 return K,old
additional,finalbad=cost(W[-10:],word);assert additional==25416 and not finalbad
charge=word.count('R')-word.count('L');assert charge==2332 and len(b)==24641
# Complete finite original-seed exceptions, with the same exact infinite-tail oracle.
controls=[]
for n in (1,2,3,4):
 J=DATA['small_endpoints'][str(n)];seed,B,p,h,pre=(seed,B4,p4,h4,pre4)if n==4 else replay_prefix(n);B=set(B);continuation=J['continuation_word'];events={e['time']:e for e in J['events']};start=len(pre)
 for i in range(len(continuation)+1):
  now=start+i
  if now in events:
   e=events[now];assert[list(p),h]==e['pose']and len(B)==e['mass'];mm,dd,gg,cc=periodic(B,p,h,e['word']);assert mm==e['next_mismatch']
  if i==len(continuation):break
  c=continuation[i];assert(p in B)==(c=='L');B.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;d0=V[h];p=p[0]+d0[0],p[1]+d0[1]
 assert start+len(continuation)==J['capture_time']and[list(p),h]==J['capture_pose']and len(B)==J['capture_mass']
 assert hashlib.sha256(json.dumps(sorted(B),separators=(',',':')).encode()).hexdigest()==J['final_field_sha256']
 mm,dd,gg,cc=periodic(B,p,h,J['capture_word']);assert mm is None
 K,fb=cost('LRLRRRRLLL',pre+continuation);assert not fb
 assert K=={1:23473,2:78226,3:49897,4:27964}[n]
 if n==4:assert continuation==word and p==(14*n-104,14*n-24)and len(B)==13137+2876*n
 controls.append(dict(N=n,capture_time=J['capture_time'],pose=J['capture_pose'],mass=len(B),drift=dd,actual_total_K=K,complete_field_sha256=J['final_field_sha256']))
out=dict(status='PASS independent ALL-N original184-cell family endpoint capture',data_sha256=hashlib.sha256(SELF.with_name('family_data.json').read_bytes()).hexdigest(),uniform_threshold=4,fixed_continuation_length=len(word),fixed_read_cells=len(Q),exact_family_eligibility_intervals=eligible,exceptional_read_cells=exceptioncells,parameter_color_proof_sha256=proofhash,parameter_color_proof=proof,uniform_capture_time=[25588,148251],uniform_capture_pose=[[14,-104],[14,-24],0],uniform_mass=[2876,13137],uniform_total_K=[614,25508],continuation_K=additional,missing_fuel_unread_all_N=True,tail_normal_hull=hull,prior_data_min_normal=prodmin,tail_restricted_black=len(restricted),tail_orbits=len(groups),tail_critical_levels=critical,far_flip_rejections=len(groups),literal_controls=controls,scope='EVERY member of this supplied original184-cell affine family captures. No universal finite-seed capture theorem or renewable nonstandard word follows.')
SELF.with_name('capture_result.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items()if k!='parameter_color_proof'},indent=2))
