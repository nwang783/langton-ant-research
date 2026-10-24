#!/usr/bin/env python3
import json
from pathlib import Path
OUT=Path(__file__).resolve().parent
src=(OUT/'search_standard_wake_small_caps.py').read_text(); g={'__file__':str(OUT/'search_standard_wake_small_caps.py')};exec(src[:src.index('# Positive controls')],g)
D=g['D'];H=g['H'];base=g['base'];certify=g['certify']

def forced_cap(w,p,h):
 q=[];pp=p;hh=h
 for a in w:
  q.append(pp);hh=(hh+(-1 if a=='L' else 1))%4;dx,dy=D[hh];pp=(pp[0]+dx,pp[1]+dy)
 assert hh==h
 d=(pp[0]-p[0],pp[1]-p[1]);assert d!=(0,0)
 def multiple(v):
  if d[0]:
   if v[0]%d[0]:return None
   k=v[0]//d[0];return k if v[1]==k*d[1] else None
  if v[0] or v[1]%d[1]:return None
  return v[1]//d[1]
 done=set();E=set();guards=[]
 for i,qi in enumerate(q):
  if i in done:continue
  data=[]
  for j,qj in enumerate(q):
   k=multiple((qj[0]-qi[0],qj[1]-qi[1]))
   if k is not None:data.append((j-len(w)*k,j,k));done.add(j)
  data.sort();turns=''.join(w[j] for _,j,_ in data)
  if any(a==b for a,b in zip(turns,turns[1:])):return None
  lo=min(k for _,_,k in data);hi=max(k for _,_,k in data)
  # Two stable longitudinal parities cover the standard-wake input.
  for n in (hi,hi+1):
   b=(qi[0]+n*d[0],qi[1]+n*d[1])
   if base(b)!=(turns[0]=='L'):return None
  for n in range(lo,hi):
   active=[w[j] for _,j,k in data if k<=n]
   assert active and all(a!=b for a,b in zip(active,active[1:]))
   b=(qi[0]+n*d[0],qi[1]+n*d[1])
   if base(b)!=(active[0]=='L'):E.add(b)
  guards.append((qi,turns))
 assert certify(E,p,h,w)
 return E,d,len(guards)

V=''.join('L' if a=='R' else 'R' for a in H[::-1])
E,d,n=forced_cap(V,(-1,-2),1)
assert d==(2,2) and n==22
# This is deliberately the opposite sector, an essential nonvacuous control.
reverse={'opposite_sector_exact_reverse':{'pose':[[-1,-2],1],'drift':d,'orbits':n,'finite_cap':sorted(E),'cap_count':len(E),'tail_oracle':True}}
white=forced_cap(H,(0,-100),3)
assert white is not None
reverse['off_rail_standard_control']={'pose':[[0,-100],3],'drift':white[1],'cap_count':len(white[0]),'tail_oracle':True}
# Same-sector sector-repair shifts of exact reverse are excluded, even with
# arbitrary finite caps: no stable profile compatibility survives.
fail=0
for t in range(-14,15,2):
 for a in (0,1):
  assert forced_cap(V,(a,a-t),1) is None
  fail+=1
reverse['same_sector_reverse_guard_rejections']=fail
(OUT/'wake_rewriter_positive_controls.json').write_text(json.dumps({'status':'PASS nonvacuous exact prepared-input and white-front controls','controls':reverse},indent=2)+'\n')
print((OUT/'wake_rewriter_positive_controls.json').read_text())
