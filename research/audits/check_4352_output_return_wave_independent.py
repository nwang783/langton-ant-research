"""Independent complete prepared-field 15324 return-wave certificate.
No author geometry, simulator, or certificate imports. Finite-original transfer
is deliberately not a premise or conclusion of this checker.
"""
from pathlib import Path
from collections import defaultdict,Counter
import hashlib,json
SELF=Path(__file__).resolve();ROOT=SELF.parents[1];U=ROOT/'causal_reduction/unit_scale';R=ROOT/'nonlinear_global_budget_2026-10-23'
A=json.loads((U/'prepared4352_output_return_wave.json').read_text());M=json.loads((U/'prepared4352_uniform_support_manifest.json').read_text());H=json.loads((ROOT/'deliverables/constant_184_capturing_family/family_data.json').read_text())['standard_word'];W=json.loads((R/'second_prepared_wave_certificate.json').read_text())['word'];D=(1j,1,-1j,-1)
xy=lambda q:(int(q.real),int(q.imag))
def trace(word,p,h):
 rows=[]
 for i,c in enumerate(word):rows.append((i,p,c));h=(h+(1 if c=='R'else-1))%4;p+=D[h]
 return rows,p,h
def cls(q,m=26):
 x,y=xy(q);a=x%m;return (x-y,a),(x-a)//m
full=set();rays=defaultdict(set);finite=set()
def ray(q):
 cl,k=cls(q);rays[cl].symmetric_difference_update({k})
def color(q,F=None):
 cl,k=cls(q);return (cl in full)^(sum(k<=j for j in rays.get(cl,()))%2)^(q in (finite if F is None else F))
# Reconstruct original canonical13 field from first-read requirements, not supplied mask.
start=113+88j;rows,_,_=trace(H*30,start,3);first={};last={}
for i,q,c in rows:
 if q not in first:first[q]=c
 else:assert last[q]!=c
 last[q]=c
finite={q for q,c in first.items()if c=='L'};assert len(finite)==13
# The original first writer has a semi-infinite SW wake. Thirteen residue rays
# exactly partition all nonnegative copy numbers, with ALL physical read toggles.
for i,q,c in trace(H,start,3)[0]:
 for residue in range(13):ray(q-2*residue*(1+1j))
flights=[s for s in M['stages']if s['kind']=='H'];assert len(flights)==5
for flight in flights[1:]:
 p=complex(flight['start_x_N_constant'][1],flight['start_y_N_constant'][1]);h=flight['heading'];count=Counter(cls(q,2)[0]for i,q,c in trace(H,p,h)[0])
 for(t,a),n in count.items():
  if n%2:
   for residue in range(a,26,2):full.symmetric_difference_update({(t,residue)})
# Complete4352 cycles k<=2, and exactly the first2331 reads of copy3.
for i,q,c in trace(W,-2+3j,3)[0]:ray(q+52*(1+1j))
partial,p,h=trace(W[:2331],76+81j,3)
for i,q,c in partial:finite.symmetric_difference_update({q})
assert(p,h)==(113+91j,2)
initial=dict(full=sorted(full),upper_rays=[[list(k),sorted(v)]for k,v in sorted(rays.items())if v],finite_xor=sorted(map(xy,finite)))
source=json.loads((U/'prepared4352_source_endpoint_limit.json').read_text());assert json.loads(json.dumps(initial))==source['initial_board']
assert len(A['prefix_word'])==142764
for i,c in enumerate(A['prefix_word']):
 assert color(p)==(c=='L'),(i,xy(p),h,c);finite.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p+=D[h]
assert(p,h)==(13+7j,0)
current=dict(full=sorted(full),upper_rays=[[list(k),sorted(v)]for k,v in sorted(rays.items())if v],finite_xor=sorted(map(xy,finite)))
assert json.loads(json.dumps(current))==A['complete_initial_ray_field']
word=A['word'];P=len(word);rows,end,eh=trace(word,p,h);f=end-p;assert(P,f,eh)==(15324,-78-78j,h)
assert all(word!=word[:n]*(P//n)for n in range(1,P)if P%n==0)
groups=defaultdict(list);index=defaultdict(set)
for i,q,c in rows:
 cl,k0=cls(q,78);k=-k0;rep=complex(cl[1],cl[1]-cl[0]);assert q==rep+k*f;groups[cl].append((k,i,c))
for q in finite:
 cl,k=cls(q,78);index[cl].add(-k)
for gs in groups.values():gs.sort(key=lambda z:z[1]-P*z[0])
def test_orbit(cl,gs,F,extra=()):
 rep=complex(cl[1],cl[1]-cl[0]);lo=min(k for k,i,c in gs);critical={lo}
 def add(n):
  for nn in(n-1,n,n+1):
   if nn>=lo:critical.add(nn)
 for k,i,c in gs:add(k)
 old,k0=cls(rep)
 for threshold in rays.get(old,()):add((threshold-k0)//(-3))
 for k in index.get(cl,()):add(k)
 for k in extra:add(k)
 for n in sorted(critical):
  active=[c for k,i,c in gs if k<=n];assert active
  if any(c==d for c,d in zip(active,active[1:])):return False,len(critical),('alternation',cl,n)
  if color(rep+n*f,F)!=(active[0]=='L'):return False,len(critical),('initial color',cl,n)
 return True,len(critical),None
checks=0;flips=0;orbit_records=[];spans=Counter();slope=constant=0
for cl,gs in sorted(groups.items()):
 ok,n,why=test_orbit(cl,gs,finite);assert ok,why;checks+=n
 lo=min(k for k,i,c in gs);hi=max(k for k,i,c in gs);span=hi-lo;spans[span]+=1
 # Exact complete-orbit late perturbation, using the same verifier including the
 # injected finite-point threshold, for EVERY physical orbit rather than a sample.
 far=hi+1000000;rep=complex(cl[1],cl[1]-cl[0]);q=rep+far*f
 assert not test_orbit(cl,gs,finite^{q},(far,))[0];flips+=1
 firstL=lambda sub:next(c for k,i,c in sub)=='L'
 a=int(firstL(gs));left=sum(firstL([r for r in gs if r[0]<=n])for n in range(lo,hi));right=sum(firstL([r for r in gs if r[0]>=n])for n in range(lo+1,hi+1))
 b=left+right-a*span;slope+=a;constant+=b
 orbit_records.append(dict(orbit=cl,copy_min=lo,copy_max=hi,reads=len(gs),checks=n if False else test_orbit(cl,gs,finite)[1],first_L_slope=a,first_L_constant=b))
assert len(groups)==3557 and flips==3557
# Controls independently infer minimal boards for finite copies; the all-N count
# is the preceding exact per-orbit fringe/mature partition, not extrapolation.
fuel=[]
for count in(1,2,3):
 tr,pp,hh=trace(word*count,p,h);fr={};la={}
 for i,q,c in tr:
  if q not in fr:fr[q]=c
  else:assert la[q]!=c
  la[q]=c
 mass=sum(c=='L'for c in fr.values());assert mass==slope*count+constant
 fuel.append([count,mass]);assert(pp,hh)==(p+count*f,h)
# Full physical field follows two complete periods, retaining all passive bands.
F=set(finite);pp=p;hh=h
for i,c in enumerate(word*2):
 assert color(pp,F)==(c=='L'),i;F.symmetric_difference_update({pp});hh=(hh+(1 if c=='R'else-1))%4;pp+=D[hh]
assert(pp,hh)==(p+2*f,h)
factors={(H*2)[i:i+10]for i in range(104)};bad=[(''.join(word[(i-9+j)%P]for j in range(10))not in factors)for i in range(P)];K=sum(bad[i]and bad[(i-1)%P]for i in range(P));net=word.count('R')-word.count('L')
assert net==408 and K==7353
out=dict(status='PASS exact complete prepared4352-output return wave',prepared_scope_only=True,transient_reads=142764,wave_entry=[13,7,0],period=P,drift=xy(f),primitive=True,word_sha256=hashlib.sha256(word.encode()).hexdigest(),read_orbits=len(groups),read_normal_hull=[min(k[0]for k in groups),max(k[0]for k in groups)],critical_checks=checks,all_orbit_far_flip_rejections=flips,literal_wave_reads=2*P,copy_span_histogram=dict(spans),minimum_entry_black_affine=[slope,constant],minimum_entry_formula_from_N=max(1,max(spans)),finite_fuel_controls=fuel,net_black_per_period=net,bad_ten_per_period=sum(bad),K_per_period=K,full_background_classes=len(full),ray_classes=sum(bool(v)for v in rays.values()),current_finite_XOR_mass=len(finite),complete_field_sha256=hashlib.sha256(json.dumps(current,sort_keys=True,separators=(',',':')).encode()).hexdigest(),source_artifact_sha256=hashlib.sha256((U/'prepared4352_output_return_wave.json').read_bytes()).hexdigest(),orbit_records=orbit_records,scope='Infinite complete prepared source-end field. All four passive writer profiles and original source wake retained. No finite-original transfer, iteration or infinite finite-seed orbit inferred. Fuel is current field at return-wave entry, not original seed mass.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items()if k!='orbit_records'},indent=2))
