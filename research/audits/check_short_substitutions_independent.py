#!/usr/bin/env python3
"""Independent enumeration by feasible-prefix DFS and literal morphism expansion.
Only finite conflicting read witnesses or the separately proved mass filter reject.
"""
from collections import defaultdict
from pathlib import Path
import json,time,hashlib
D=((0,1),(1,0),(0,-1),(-1,0));ROOT=Path(__file__).resolve().parents[1]
def generate(k):
 groups=defaultdict(list); seen={}; w=[]
 def walk(x,y,h):
  if len(w)==k:
   if h in(1,3) and x*x+y*y>1:groups[(x,y,h)].append(''.join(w))
   return
  old=seen.get((x,y))
  for c in ('L','R') if old is None else ('R' if old=='L' else 'L',):
   seen[x,y]=c;w.append(c);hh=(h+(1 if c=='R' else -1))%4;dx,dy=D[hh]
   walk(x+dx,y+dy,hh);w.pop()
   if old is None:del seen[x,y]
   else:seen[x,y]=old
 walk(0,0,0);return groups
def reject(u,v,limit=20000):
 prefix=u;done=0;x=y=h=0;last={}
 while True:
  for t in range(done,len(prefix)):
   c=prefix[t];old=last.get((x,y))
   if old is not None and old[1]==c:return t,old[0],x,y,c
   last[x,y]=(t,c);h=(h+(1 if c=='R' else -1))%4;dx,dy=D[h];x+=dx;y+=dy
  if len(prefix)>=limit:raise AssertionError(('Unresolved',u,v))
  done=len(prefix);nxt=''.join(u if c=='R' else v for c in prefix)[:limit]
  assert nxt[:done]==prefix
  prefix=nxt
start=time.time();allrows=[]
reference=json.loads((ROOT/'computability/short_selfsimilar_exclusion.json').read_text())['results']
for k in range(3,18,2):
 groups=generate(k);total=mass=failed=0;maximum=-1;example=None;dig=hashlib.sha256()
 for (x,y,h),us in sorted(groups.items()):
  if h!=1:continue
  norm=x*x+y*y
  for u in us:
   if u[0]!='R':continue
   eu=u.count('R')-u.count('L')
   for v in groups.get((-x,-y,3),[]):
    total+=1;ev=v.count('R')-v.count('L')
    if eu==-ev and (eu<0 or eu*eu<=norm):mass+=1;wit=('mass',eu,norm)
    else:
     wit=reject(u,v);failed+=1
     if wit[0]>maximum:maximum=wit[0];example={'u':u,'v':v,'conflict':wit}
    dig.update(repr((u,v,wit)).encode()+b'\n')
 row={'length':k,'pairs':total,'mass':mass,'finite_conflicts':failed,'latest_failure':maximum,'example':example,'record_digest':dig.hexdigest()}
 old=next(r for r in reference if r['length']==k)
 assert(total,mass,failed,maximum)==tuple(old[z] for z in('candidate_pairs','signed_mass_rejections','finite_alternation_rejections','latest_alternation_failure_time'))
 allrows.append(row);print(json.dumps(row),flush=True)
 out={'method':'Independent feasible-prefix DFS and literal repeated substitution, not a base-k letter oracle','results':allrows,'elapsed':time.time()-start,'status':'Every enumerated candidate rejected analytically or by explicit finite alternation conflict'}
 Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
