from pathlib import Path
from collections import defaultdict
import json
P0=Path(__file__).resolve();S=P0.with_name('check_changed_endpoint_catalog_independent.py');exec(compile(S.read_text().split('results=[];nchecks=')[0],str(S),'exec'))
source=(34,1);ch=(50,0);rows,C=make_changed(source);rr,p,h,tau,phi=incoming(rows,C,ch);row=next(r for r in capsup[source]['results']if tuple(r['channel'])==ch);F=set(C);p,h,path,_=replay(rr,F,p,h,row['entry'],True)
def normals(rays,finite):
 critical=defaultdict(set)
 for cl,v in rays.items():
  for b in v:critical[cl].update((b-1,b,b+1))
 for q in finite:
  cl,k=old(q);critical[cl].update((k-1,k,k+1))
 support=set()
 for (t,a),ks in critical.items():
  for k in ks:
   if color(complex(a-2*k,a-2*k-t),rays,finite):support.add(t);break
 return support
oldns=normals(rows,C);newns=normals(rr,F);assert(min(oldns),max(oldns))==(-82,56)and(min(newns),max(newns))==(-82,70)
ext={complex(59,-11),complex(66,-4),complex(67,-3),complex(68,-2)};assert all(color(q,rr,F)for q in ext)
_,_,tail,_=replay(rr,set(F),p,h,104,True);assert(min(int(z.real-z.imag)for z in tail),max(int(z.real-z.imag)for z in tail))==(56,66)
out=dict(status='PASS complete support on all finite and half-ray classes',source=source,incoming=ch,old_support_hull=[-82,56],new_support_hull=[-82,70],permanent_extremes=sorted(map(xy,ext)),scope='One supplied infinite changed-endpoint response, not finite-original itinerary or amortized-width disproof.')
P0.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
