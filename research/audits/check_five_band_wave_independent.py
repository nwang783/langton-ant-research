from pathlib import Path
from collections import defaultdict
import json,hashlib
SELF=Path(__file__).resolve();S=SELF.with_name('check_exceptional_return_map_independent.py');exec(compile(S.read_text().split('author=json.loads')[0],str(S),'exec'));P=SELF
J=json.loads((R/'prepared_wave_five_band_normal_form.json').read_text());w=json.loads((R/'prepared_travelling_wave_certificate.json').read_text())['word'];B=set(map(tuple,J['full_black_orbit_profiles']));F={complex(*q)for q in J['finite_XOR_cap']};assert len(B)==60 and len(F)==2
orb=lambda q:(int(q.real-q.imag),int(q.real)%2)
bands=[(-40,-30),(-28,-18),(-16,-6),(-2,8),(14,24)];matches=[]
for lo,hi in bands:
 part={q for q in B if lo<=q[0]<=hi};assert len(part)==12;match=[]
 for sign in(1,-1):
  src={sign*q for q in W};readlo=min(int((sign*z).real-(sign*z).imag)for z in S)
  delta=lo-readlo
  for a in(0,1):
   trans=complex(a,a-delta)
   if {orb(q+trans)for q in src}==part:match.append((sign,delta,a))
 assert match;matches.append((lo,hi,match))
assert not any(max(a,c)<=min(b,d)for i,(a,b)in enumerate(bands)for c,d in bands[i+1:])
p=-6-6j;h=0;g=defaultdict(list)
for i,c in enumerate(w):
 x,y=int(p.real),int(p.imag);cl=(x-y,x%14);k=(x-cl[1])//14;g[cl].append((k,i,c));h=(h+(1 if c=='R'else-1))%4;p+=dirs[h]
assert(p,h)==(8+8j,0)and len(g)==557
bulk=lambda q:orb(q)in B
col=lambda q:bulk(q)^(q in F)
exceptions=[];bcount=ocount=odd=0;checks=0
for (t,a),ls in g.items():
 ls.sort(key=lambda z:z[1]-len(w)*z[0]);assert all(x[2]!=y[2]for x,y in zip(ls,ls[1:]));lo=min(z[0]for z in ls);hi=max(z[0]for z in ls);rep=complex(a,a-t)
 assert bulk(rep)==(ls[0][2]=='L');bcount+=ls[0][2]=='L';ocount+=ls[-1][2]=='R';odd+=len(ls)%2
 for n in range(lo,hi):
  first=next(z[2]for z in ls if z[0]<=n);q=rep+n*(14+14j);checks+=1
  if bulk(q)!=(first=='L'):exceptions.append(q)
  assert col(q)==(first=='L')
 # Every finite toggle in this orbit must lie below the complete-list future ray.
 for q in F:
  if(int(q.real-q.imag),int(q.real)%14)==(t,a):assert(int(q.real)-a)//14<hi
assert set(exceptions)==F and(bcount,ocount,odd)==(197,301,358)and checks==2
assert not bulk(complex(-5,-7))and bulk(complex(-5,-6))
tog=set();p=-6-6j;h=0
for c in w*3:
 assert col(p)^(p in tog)==(c=='L');tog.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p+=dirs[h]
out=dict(status='PASS independently reconstructed five settled standard bands and exact two-toggle infinite wave',note_sha256=hashlib.sha256((R/'five_standard_band_wave_normal_form.md').read_bytes()).hexdigest(),input_sha256=hashlib.sha256((R/'prepared_wave_five_band_normal_form.json').read_bytes()).hexdigest(),standard_profile_matches=matches,read_orbits=557,full_list_black_orbits=bcount,full_list_output_black=ocount,odd_write_orbits=odd,eligibility_exceptions=sorted(map(xy,exceptions)),scope='A distinct complete bi-infinite five-standard-band field with one black addition and one deletion; exact same1564 wave forever. Not full-field equality to the72-half-ray state or a finite-seed preparation. Exact197N+1 finite supply remains necessary.')
P.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
