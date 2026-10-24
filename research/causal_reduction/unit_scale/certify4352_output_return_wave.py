"""Exact supplied15324 return wave on the complete4352 source-end field.
This is a prepared infinite source-end interface. Finite-original family
realization for a growing number of return periods is a separate obligation.
"""
from pathlib import Path
from collections import defaultdict
import json,hashlib,time
from probe4352_source_endpoint_limit import build,trace,V,key,z
P=Path(__file__).resolve().parent
A=json.loads((P/'prepared4352_source_endpoint_limit.json').read_text())
START=142764;PERIOD=15324;word=A['word'][START:START+PERIOD]
b,p,h=build();starttime=time.time()
for i,c in enumerate(A['word'][:START]):
 assert b.color(p)==(c=='L'),(i,p,h)
 b.toggle(p);h=(h+(1 if c=='R'else-1))%4;v=V[h];p=(p[0]+v[0],p[1]+v[1])
assert(p,h)==((13,7),0)

def certificate(b,p,h,word):
 rr=list(trace(word,p,h));f=(rr[-1][1][0]-p[0],rr[-1][1][1]-p[1]);assert rr[-1][2]==h and f[0]==f[1] and f[0]!=0 and f[0]%26==0
 stride=abs(f[0]);groups=defaultdict(list);index=defaultdict(list)
 for i,q,hh,c in rr[:-1]:
  a=q[0]%stride;k=(q[0]-a)//f[0];groups[(q[0]-q[1],a)].append((k,i,c))
 for q in b.F:
  a=q[0]%stride;index[(q[0]-q[1],a)].append((q[0]-a)//f[0])
 records=[];checks=0
 for j,g in sorted(groups.items()):
  g.sort(key=lambda v:(-v[0],v[1]));mn=min(x[0]for x in g);mx=max(x[0]for x in g);c=(j[1],j[1]-j[0]);slope=f[0]//26
  if any(a[2]==v[2]for a,v in zip(g,g[1:])):return None
  local=0
  for n in range(mn,mx):
   first=next(a for a in g if a[0]<=n);q=(c[0]+n*f[0],c[1]+n*f[1]);checks+=1;local+=1
   if b.color(q)!=(first[2]=='L'):return None
  tests={mx};kk=key(c);zc=z(c)
  for cut in b.rays.get(kk,()):
   n=(cut-zc)//slope
   for nn in(n-1,n,n+1):
    if nn>=mx:tests.add(nn)
  for n in index.get(j,()):
   for nn in(n-1,n,n+1):
    if nn>=mx:tests.add(nn)
  want=g[0][2]=='L'
  for n in sorted(tests):
   q=(c[0]+n*f[0],c[1]+n*f[1]);checks+=1;local+=1
   if b.color(q)!=want:return None
  records.append([list(j),mn,mx,len(g),int(want),len(tests),local])
 return {'period':len(word),'drift':list(f),'read_orbits':len(groups),'total_color_checks':checks,'read_normal_hull':[min(j[0]for j in groups),max(j[0]for j in groups)],'orbit_records':records}

cert=certificate(b,p,h,word);assert cert
# Two complete literal cycles and one remote perturbation on EVERY physical orbit.
initial=b.manifest();F0=set(b.F);pp=p;hh=h
for i,c in enumerate(word*2):
 assert b.color(pp)==(c=='L');b.toggle(pp);hh=(hh+(1 if c=='R'else-1))%4;v=V[hh];pp=(pp[0]+v[0],pp[1]+v[1])
assert (pp,hh)==((p[0]-156,p[1]-156),h);b.F=F0
recs=cert['orbit_records'];selected=range(len(recs));rejected=0
for i in selected:
 (t,a),mn,mx,*_=recs[i];n=mx+1000000;q=(a-78*n,a-t-78*n);b.toggle(q);assert certificate(b,p,h,word)is None;b.toggle(q);rejected+=1
from check4352_noncrossing_producer import H
factors={(H*2)[i:i+10]for i in range(104)};bad=[(''.join(word[(i-9+j)%PERIOD]for j in range(10))not in factors)for i in range(PERIOD)]
K=sum(bad[i]and bad[(i-1)%PERIOD]for i in range(PERIOD))
primitive=all(word!=word[:m]*(PERIOD//m)for m in range(1,PERIOD)if PERIOD%m==0)
out={'scope':__doc__,'status':'EXACT_ALL_FUTURE_PREPARED_RETURN_WAVE','entry_after_source_contact':START,'pose':[list(p),h],'word':word,'word_sha256':hashlib.sha256(word.encode()).hexdigest(),'prefix_word':A['word'][:START],'complete_initial_ray_field':initial,'certificate':cert,'charge_per_period':word.count('R')-word.count('L'),'bad_ten_per_period':sum(bad),'adjacent_K_per_period':K,'primitive_word':primitive,'far_flip_rejections':rejected,'literal_checked_reads':2*PERIOD,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'seconds':time.time()-starttime}
(P/'prepared4352_output_return_wave.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items()if k not in('word','prefix_word','complete_initial_ray_field','certificate')},indent=2));print({k:v for k,v in cert.items()if k!='orbit_records'})
