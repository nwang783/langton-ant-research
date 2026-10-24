"""Exact all-translation LOCAL stable-corner profile comparison.
Infinite profiles are limits of completed finite old sides, not proposed seeds.
A match would be a necessary clean no-extra-fuel interface, not a reachable pose.
"""
from pathlib import Path
import json,sys,time
P=Path(__file__).resolve().parent
sys.path.insert(0,str(P.parents[1]/'computability/unit_inductive_certificates'))
from presburger_read_set_solver import Context
from certify_highway_wake_reflector import trace,rot,xor
from probe_perpendicular_highway_wake import H
ctx=Context(max_operations=200000000)
def S(c):return ctx.set('[a,b]->{[x,y]:'+c+'}')
def points(ps,shift=False):return S(' or '.join(f'(x={"a+"if shift else""}{x} and y={"b+"if shift else""}{y})'for x,y in ps)or'false')
J=json.loads((P/'single_turn_highway_corner_certificate.json').read_text());K=list(map(tuple,J['corner_relative_black']));F=H[68:]+H[:68]
inrows,_,_=trace(F,(0,0),0);outrows,_,_=trace(H,(1,0),1)
# Completed limiting old field after entire incoming and outgoing rays.
old=points(K+[(0,0)])
for rows,d,cond in((inrows,(2,-2),'i<0'),(outrows,(2,2),'i>=0')):
 for q,h,c in rows:old=xor(old,S(f'exists(i:{cond} and x={q[0]}+{d[0]}*i and y={q[1]}+{d[1]}*i)'))
records=[]
for k in range(4):
 st=time.monotonic();ctx.reset_operations();reads=points([(0,0)],True)
 for rows,d,cond in((inrows,(2,-2),'i<0'),(outrows,(2,2),'i>=0')):
  d=rot(d,k)
  for q,h,c in rows:
   q=rot(q,k);reads=reads.union(S(f'exists(i:{cond} and x=a+{q[0]}+{d[0]}*i and y=b+{q[1]}+{d[1]}*i)'))
 target=points([rot(q,k)for q in K],True)
 assert target.subtract(reads).is_empty()
 missing=target.subtract(old);extra=old.intersect(reads).subtract(target)
 bad=missing.union(extra).params();good=ctx.set('[a,b]->{:true}').subtract(bad).coalesce()
 records.append(dict(rotation_ccw=k,matching_translations=str(good),is_empty=good.is_empty(),seconds=time.monotonic()-st))
 print(records[-1],flush=True)
out=dict(scope=__doc__,old_stable_black_relation=str(old),cases=records)
(P/'highway_corner_reuse_profile.json').write_text(json.dumps(out,indent=2)+'\n')
