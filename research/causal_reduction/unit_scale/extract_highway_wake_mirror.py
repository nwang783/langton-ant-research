"""Remove only never-read old-wake cells from the exact reflector family.
This is a finite one-shot scatterer, not regenerative mirror memory.
"""
from pathlib import Path
import sys,json,hashlib,time
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parents[1]/'computability/unit_inductive_certificates'))
from presburger_read_set_solver import Context
from certify_highway_wake_reflector import trace,rot,xor
from probe_perpendicular_highway_wake import shifted_seed,step,H
st=time.monotonic();ctx=Context(max_operations=100000000);cert=json.loads(HERE.joinpath('highway_wake_reflector_certificate.json').read_text());col=json.loads(HERE.joinpath('highway_wake_reflector_collision.json').read_text())
def S(cond):return ctx.set('[n,m]->{[x,y]:n>=30 and m>=30 and ('+cond+')}')
def pts(ps):return S(' or '.join(f'(x={x} and y={y})'for x,y in ps)or'false')
standard=json.loads(Path('/workspace/shared/langton/recovered_bundle/ant_global/root/standard.json').read_text());incoming=S(' or '.join(f'(x=-2*m+1+{rot(q,1)[0]} and y=2*m+{rot(q,1)[1]})'for q in standard['seed']))
initial=ctx.set(cert['initial_relation']);old=initial.subtract(incoming);entry=ctx.set(cert['entry_relation']);after=ctx.set(cert['postcollision_relation'])
rr,_,_=trace(col['collision_word'],(-19,20),2);reads=pts({q for q,h,c in rr});tr,_,_=trace(H,(-31,-10),0)
for q,h,c in tr:reads=reads.union(S(f'exists(i:i>=0 and x={q[0]}-2*i and y={q[1]}+2*i)'))
needed=old.intersect(reads).coalesce();sample_old=shifted_seed(2,(-60,-60));p=(-60,-60);h=1
for c in H*60:p,h,a=step(sample_old,p,h);assert a==c
kept=[]
for q in sample_old:
 if not needed.intersect(pts([q])).intersect(ctx.set('[n,m]->{[x,y]:n=30 and m=30}')).is_empty():kept.append(q)
kept.sort();assert needed.is_equal(pts(kept))
removed=old.subtract(needed);assert removed.intersect(reads).is_empty()
newinitial=initial.subtract(removed).coalesce();newentry=entry.subtract(removed).coalesce();newafter=after.subtract(removed).coalesce()
# Entire omitted field is never read after the cut; prefix absence was certified.
assert newinitial.is_equal(needed.union(incoming))
# Concrete postcollision board at m=30, for exact local interface controls.
B=set(kept)|shifted_seed(1,(-59,60));p=(-59,60);h=2
for c in H*20+col['collision_word']:p,h,a=step(B,p,h);assert a==c
assert(p,h)==((-31,-10),0)
out=dict(status='EXACT_ALL_M_FINITE_SCATTERER',domain='integers m>=30',mirror_black_cells=kept,mirror_mass=len(kept),total_initial_mass=len(kept)+13,mirror_bbox=[min(q[a]for q in kept)for a in(0,1)]+[max(q[a]for q in kept)for a in(0,1)],incoming_seed='CCW rotation of standard seed translated to(-2m+1,2m)',initial_relation=str(newinitial),entry_relation=str(newentry),postcollision_relation=str(newafter),same_path_as_certified_family=True,tail_time='104*m+18832',tail_pose=[-31,-10,'N'],tail_drift=[-2,2],complete_collision_xor_count=1260,postcollision_m30=sorted(B),m30_postmass=len(B),source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),seconds=time.monotonic()-st)
HERE.joinpath('highway_wake_mirror_minimal.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items()if k not in('mirror_black_cells','initial_relation','entry_relation','postcollision_relation','postcollision_m30')})
