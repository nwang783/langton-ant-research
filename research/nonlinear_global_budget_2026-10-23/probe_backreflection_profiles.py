#!/usr/bin/env python3
import contextlib,io,runpy,json
from pathlib import Path
from collections import Counter
with contextlib.redirect_stdout(io.StringIO()):g=runpy.run_path(str(Path(__file__).with_name('endpoint_catalog.py')))
results=json.loads(Path(__file__).with_name('endpoint_catalog_results.json').read_text())['results'];out=[]
for rr in results:
 if rr['drift']!=[2,2]:continue
 rows,F,p,h,tau,phi=g['make_initial'](rr['channel']);old={j for j,r in rows.items()if len(r)%2};assert len(old)==36
 seen=[]
 for _ in range(rr['entry']):
  seen.append(p)
  ch='L'if g['initial_color'](p,rows,F)else'R'
  if p in F:F.remove(p)
  else:F.add(p)
  h=(h+(-1 if ch=='L'else 1))%4;v=g['V'][h];p=(p[0]+v[0],p[1]+v[1])
 assert p==tuple(rr['pose'][0])and h==rr['pose'][1]
 periods=[];hh=h;pp=p
 for ch in rr['tail_word']:
  periods.append(pp);hh=(hh+(-1 if ch=='L'else 1))%4;v=g['V'][hh];pp=(pp[0]+v[0],pp[1]+v[1])
 counts=Counter(g['old_orbit'](q)[0]for q in periods);new={j for j,c in counts.items()if c%2};read=set(counts)
 assert len(new)==12 and old.isdisjoint(read)
 bulk=old|new;assert len(bulk)==48
 out.append({'channel':rr['channel'],'prior_bulk_classes':sorted(old),'new_return_classes':sorted(new),'after_round_trip_bulk_count':len(bulk),'old_bulk_t_range':[min(t for t,a in old),max(t for t,a in old)],'new_bulk_t_range':[min(t for t,a in bulk),max(t for t,a in bulk)],'finite_recovery_read_t_range':[min(x-y for x,y in seen),max(x-y for x,y in seen)],'post_collision_finite_XOR_t_range':[min(x-y for x,y in F),max(x-y for x,y in F)],'all_old_bulk_avoided_by_return_read_classes':True})
Path(__file__).with_suffix('.json').write_text(json.dumps({'status':'PASS','scope':'Finite profile controls, not repeatability or a further global rank.','results':out},indent=2)+'\n')
print(json.dumps([{k:v for k,v in r.items()if k not in{'prior_bulk_classes','new_return_classes'}}for r in out],indent=2))
