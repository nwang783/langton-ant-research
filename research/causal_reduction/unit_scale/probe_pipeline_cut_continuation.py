"""One deterministic continuation from the exact disconnected schedule's H-end cut.
Its semi-infinite entry field is prepared, NOT a finite seed. Tail matches below
are only discovery controls until complete future histories are certified.
"""
import json,collections,hashlib
from pathlib import Path
import certify_short_refinement_rup as core
P=Path(__file__).resolve().parent
j=json.loads((P/'forward108_domino_repair.json').read_text());ev=collections.defaultdict(list)
for kind,(w,(x,y,h))in enumerate(zip(j['words'],j['starts'])):
 for t,(p,g,c)in enumerate(core.trace(w,(x,y),h)[0]):ev[p[0]-p[1],p[0]%2].append((p[0]//2,kind,t))
def initial(p):
 k=p[0]//2
 return sum(k-q<0 or(k-q==0 and a==0)for q,a,t in ev[p[0]-p[1],p[0]%2])%2
D=((0,1),(1,0),(0,-1),(-1,0));p=(2,12);h=1;xor=set();rows=[];word='';contacts=[]
poses={tuple(z):k for k,z in enumerate(j['starts'])}
for t in range(20000):
 b=initial(p)^(p in xor);c='L'if b else'R';rows.append((p,h,c));word+=c
 for k,(x,y,g)in enumerate(j['starts']):
  if h==g and p[0]-x==p[1]-y and(p[0]-x)%2==0:
   if len(contacts)<100:contacts.append(dict(time=t,piece=k,period=(p[0]-x)//2))
 if p in xor:xor.remove(p)
 else:xor.add(p)
 h=(h+(-1 if b else 1))%4;dx,dy=D[h];p=(p[0]+dx,p[1]+dy)
cs=[]
for n in range(4,1201,4):
 if word[-n:]==word[-2*n:-n]==word[-3*n:-2*n]:
  a=rows[-n];b=rows[-2*n];c=rows[-3*n]
  if a[1]==b[1]==c[1]and(a[0][0]-b[0][0],a[0][1]-b[0][1])==(b[0][0]-c[0][0],b[0][1]-c[0][1]):
   cs.append(dict(period=n,drift=[a[0][0]-b[0][0],a[0][1]-b[0][1]],word=word[-n:]));break
out=dict(scope=__doc__,steps=len(word),first_contacts=contacts,tail_discovery=cs,endpoint=[*p,h],first_word=word[:1000],source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
(P/'pipeline_cut_continuation.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items()if k not in ['first_word','source_sha256']})
