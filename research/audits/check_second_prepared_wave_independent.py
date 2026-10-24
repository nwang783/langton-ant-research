from pathlib import Path
from collections import defaultdict,Counter
import json,hashlib
SELF=Path(__file__).resolve();S=SELF.with_name('check_changed_endpoint_catalog_independent.py');exec(compile(S.read_text().split('results=[];nchecks=')[0],str(S),'exec'))
P=SELF
J=json.loads((R/'second_prepared_wave_probe.json').read_text());closure=json.loads((R/'endpoint_return_closure_results.json').read_text());node=next(z for z in closure['states']if z['state_sha256']==J['node'])

def settle(rows,F,p,h,word):
 # Append all outgoing odd-read translates, then normalize by direct finite level evaluation.
 pp=p;hh=h;odd=set()
 for c in word:
  odd.symmetric_difference_update({pp});hh=(hh+(1 if c=='R'else-1))%4;pp+=dirs[hh]
 assert pp-p==-d and hh==h
 rr={cl:set(v)for cl,v in rows.items()}
 for q in odd:
  cl,k=old(q);rr.setdefault(cl,set()).symmetric_difference_update({k})
 oc={cl for cl,v in rr.items()if len(v)%2};cap2=set(F)
 for (t,a),v in rr.items():
  if not v:continue
  for k in range(min(min(v),0),max(max(v),0)+1):
   if(sum(k<=b for b in v)%2)^((t,a)in oc and k<=0):cap2.symmetric_difference_update({complex(a-2*k,a-2*k-t)})
 return {cl:[0]for cl in oc},cap2
both=[]
for source,inc in [((34,1),(50,0))]:
 rows,C1=make_changed(source);rr,p,h,tau,phi=incoming(rows,C1,inc);r=next(r for r in capsup[source]['results']if tuple(r['channel'])==inc);F=set(C1);p,h,_,_=replay(rr,F,p,h,r['entry']);assert certify(rr,F,p,h,r['tail_word'])[0]
 nrows,ncap=settle(rr,F,p,h,r['tail_word']);assert set(nrows)==set(map(tuple,node['profiles']))and ncap=={complex(*q)for q in node['cap']};assert len(nrows)==72 and len(ncap)==5733;both.append((nrows,ncap))
assert len(both)==1
frozen=json.loads((R/'second_prepared_wave_input.json').read_text());assert frozen['profiles']==node['profiles'] and frozen['cap']==node['cap'] and frozen['state_sha256']==node['state_sha256']
standalone=json.loads((R/'second_prepared_wave_certificate.json').read_text());assert standalone['word']==J['word'] and standalone['wave_entry']==J['wave_entry']
rows,C2=both[0];assert not ({(t+20,(a+1)%2)for t,a in rclasses}&rows.keys())
rr,p,h,tau,phi=incoming(rows,C2,(20,1));initialpose=(*xy(p),h);F=set(C2);p,h,path,prefix=replay(rr,F,p,h,6820,True)
assert (p,h)==(68+73j,3)
finite_hash=hashlib.sha256(json.dumps(sorted(map(xy,F)),separators=(',',':')).encode()).hexdigest()
pp,hh,slots,word=replay(rr,set(F),p,h,4352,True);assert word==J['word']and pp-p==26+26j and hh==h
assert hashlib.sha256(word.encode()).hexdigest()==J['word_sha256']
PER=len(word);f=pp-p;stride=26;groups=defaultdict(list)
for i,q in enumerate(slots):
 x,y=xy(q);cl=(x-y,x%stride);rep=complex(cl[1],cl[1]-cl[0]);level=(x-cl[1])//stride;assert q==rep+level*f;groups[cl].append((level,i,word[i],rep))
assert len(groups)==1162
# Generic chronological full-orbit validation, not a test of repeated blocks or an assumed standard period.
for gs in groups.values():gs.sort(key=lambda z:z[1]-PER*z[0])
def generic(finite):
 idx=defaultdict(set)
 for q in finite:
  x,y=xy(q);cl=(x-y,x%stride);idx[cl].add((x-cl[1])//stride)
 checked=0
 for cl,gs in groups.items():
  rep=gs[0][3];lower=min(g[0]for g in gs);critical={lower}
  def add(n):
   for a in(n-1,n,n+1):
    if a>=lower:critical.add(a)
  for k,i,c,_ in gs:add(k)
  oc,k0=old(rep);slope=-13
  for th in rr.get(oc,()):add((th-k0)//slope)
  for n in idx.get(cl,()):add(n)
  for n in sorted(critical):
   active=[c for k,i,c,_ in gs if k<=n];assert active;checked+=1
   if any(a==b for a,b in zip(active,active[1:])):return False,checked,('alternation',cl,n)
   if color(rep+n*f,rr,finite)!=(active[0]=='L'):return False,checked,('first_color',cl,n)
 return True,checked,None
ok,ncheck,why=generic(F);assert ok,why
controls=0
for gs in groups.values():
 q=gs[0][3]+(max(g[0]for g in gs)+1000000)*f;changed=F^{q};assert not generic(changed)[0];controls+=1
# Additional no-formula exact controls for three full successive periods and whole-field head/heading.
pp,hh,_,literal=replay(rr,set(F),p,h,PER*3);assert literal==word*3 and pp==p+3*f and hh==h
bad=[(''.join(word[(i-9+j)%PER]for j in range(10))not in factor10)for i in range(PER)]
assert sum(bad)==2320 and sum(bad[i]and bad[(i-1)%PER]for i in range(PER))==1972
# Report all complete geometric facts, keeping prepared input separate from finite input.
profilehash=hashlib.sha256(json.dumps({'profiles':sorted(rows),'cap':sorted(map(xy,C2))},sort_keys=True,separators=(',',':')).encode()).hexdigest()
out=dict(status='PASS independent complete inherited72-profile field and arbitrary-period ray certificate',author_certificate_sha256=hashlib.sha256((R/'second_prepared_wave_probe.json').read_bytes()).hexdigest(),node=J['node'],full_field_derivation=[34,1,50,0],profiles=72,finite_cap=5733,initial_first_contact_pose=initialpose,first_contact_time=tau,first_contact_phase=phi,transient=6820,wave_pose=(*xy(p),h),period=PER,drift=xy(f),read_orbits=len(groups),complete_critical_level_checks=ncheck,far_flip_rejections=controls,read_normal_hull=[min(int(q.real-q.imag)for q in slots),max(int(q.real-q.imag)for q in slots)],bad_ten_per_period=sum(bad),K_per_period=1972,word_sha256=J['word_sha256'],finite_XOR_mass=len(F),finite_XOR_sha256=finite_hash,bound_source_hashes={name:hashlib.sha256((R/name).read_bytes()).hexdigest()for name in ['three_band_4352_prepared_wave.md','second_prepared_wave_input.json','second_prepared_wave_certificate.json','three_standard_band_wave_normal_form.json']},scope='An actual infinite prepared background with72 half-ray classes plus finite cap and causal incoming front. Exact nonstandard travelling wave with infinite K. No finite-original itinerary, finite-seed noncapture, or all-future lifting from finite truncations.')
P.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2),flush=True)
