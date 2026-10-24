"""Complete white/black stable-profile guard test for nine black-stencil matches.
No pose reachability or finite-side renewal is inferred from a static match.
"""
from pathlib import Path
import sys,json,time
P=Path(__file__).resolve().parent
sys.path.insert(0,str(P.parents[1]/'computability/unit_inductive_certificates'))
from presburger_read_set_solver import Context
from certify_highway_wake_reflector import trace,rot
from probe_perpendicular_highway_wake import H
ctx=Context(max_operations=200000000)
def S(c):return ctx.set('[a,b]->{[x,y]:'+c+'}')
old=ctx.set(json.loads((P/'highway_corner_reuse_profile.json').read_text())['old_stable_black_relation'])
cases=json.loads((P/'corner_phase_alternation_black.json').read_text())['black_stencil_matches'];records=[]
for c in cases:
 ctx.reset_operations();st=time.monotonic();d=c['phase_data'];k=c['rotation_ccw'];ha=d['input_head'];a=d['in_phase'];b=d['out_phase'];turn=d['cap']
 inrows,di,hi=trace(H[a:]+H[:a],(0,0),ha)
 _,p,h=trace(turn,(0,0),ha);outrows,pe,he=trace(H[b:]+H[:b],p,h);do=(pe[0]-p[0],pe[1]-p[1])
 reads=S('x=a and y=b')
 for rows,v,cond in((inrows,di,'i<0'),(outrows,do,'i>=0')):
  v=rot(v,k)
  for q,hh,tt in rows:
   q=rot(q,k);reads=reads.union(S(f'exists(i:{cond} and x=a+{q[0]}+{v[0]}*i and y=b+{q[1]}+{v[1]}*i)'))
 K=[rot(q,k)for q in d['extra_relative_cap']];target=S(' or '.join(f'(x=a+{x} and y=b+{y})'for x,y in K))
 extra=old.intersect(reads).subtract(target).coalesce()
 good=ctx.set(c['translations']).subtract(extra.params()).coalesce()
 # Exact all-bounds test: each compatible black-only placement needs infinitely
 # many white corrections, not merely a missed local cap bit.
 lifted=ctx.set(str(extra).replace('[a, b]', '[a,b,N]',1))
 outside=lifted.intersect(ctx.set('[a,b,N]->{[x,y]:N>=0 and (x>N or -x>N or y>N or -y>N)}')).params()
 wanted=ctx.set(c['translations'].replace('[a, b]', '[a,b,N]',1)).intersect(ctx.set('[a,b,N]->{:N>=0}'))
 every_bound_has_error=wanted.subtract(outside).is_empty()
 records.append(dict(case=c['case'],rotation_ccw=k,matching_translations=str(good),is_empty=good.is_empty(),every_translation_has_unbounded_white_corrections=every_bound_has_error,seconds=time.monotonic()-st))
 print(records[-1],flush=True)
(P/'corner_phase_alternation_full.json').write_text(json.dumps(dict(scope=__doc__,cases=records),indent=2)+'\n')
