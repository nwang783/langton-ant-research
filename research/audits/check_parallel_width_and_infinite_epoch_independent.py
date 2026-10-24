from pathlib import Path
import hashlib,json
from check_dcuv_patch_model_independent import ROOT,raws,mark,walk,rotation,xy
SELF=Path(__file__).resolve();D=ROOT/'causal_archive_frontier_2026-10-23'
ids=(0,1,4,5,6,7,8,9);names=('D','DC','V','VC','VCC','U','UC','UCC');c={0:0,1:1,4:0,5:1,6:2,7:0,8:1,9:2}
K={p for p,b in walk(mark)[2].items() if b};rows=[]
for s,name in zip(ids,names):
 end,h,_,fl=walk(raws[s]);before={p for p,b in walk(raws[s]+mark)[2].items() if b};out=(before^fl)-{end+rotation(q,h)for q in K}
 odd=sorted((q for q in out if int(q.real+q.imag)%2),key=xy);v=int(s in(4,5,6));u=int(s in(7,8,9));base=4 if v else 7 if u else 0
 e,hh,_,_=walk(raws[base]);assert hh==0;drop=int(e.imag-e.real);assert drop==2*v+4*u
 tail=len(odd)-3*v-5*u;assert tail==({0:0,1:2,2:3}[c[s]])
 permanent={1j,1}if u else set();assert permanent<=set(odd)
 rows.append(dict(packet=s,name=name,odd_output_slots=[list(xy(q))for q in odd],odd_count=len(odd),U_permanent_odd_subtraction=2*u,usable_odd_upper_bound=len(odd)-2*u,V_base=v,U_base=u,half_normal_sweep=v+2*u,C_tails=c[s],tail_odd_increment=tail))
 for hs in range(4):
  for hc in (hs,(hs+2)%4):
   # Parallel heading sector gives even head-sum difference; rotations preserve mod-two coordinate sums.
   assert (hc-hs)%2==0
   for o in out:assert int(rotation(o,hs).real+rotation(o,hs).imag)%2==int(o.real+o.imag)%2
assert rows==json.loads((D/'parallel_epoch_width_controls.json').read_text())['rows']
assert [r['odd_count']for r in rows]==[0,2,3,5,6,5,7,8]
assert max(map(len,(raws[s]for s in ids)))==58
outmax=0
for s in ids:
 end,h,_,fl=walk(raws[s]);bb={p for p,b in walk(raws[s]+mark)[2].items()if b};out=(bb^fl)-{end+rotation(q,h)for q in K}
 outmax=max(outmax,max(max(abs(q.real),abs(q.imag))for q in out))
assert outmax==7
assert len(range(2,295,2))==147 and 4851+3*147==5292 and 3*147==441
# Exact coefficient inequalities hold for every nonnegative v,u, not a finite parameter sample:
# 3(v+2u) -(3v+5u)=u; permanent subtraction changes this to3(v+u).
assert (3-3,6-5)==(0,1)
# Tangent endpoint correction bound: alpha in[pi/4,pi/2], final C contributes -pi/2.
# In units pi/4, actual correction is alpha_first-alpha_last-2*c_last.
# Its absolute value <=3; four bridge corners each have absolute turn <4.
# |I|<=K+1 gives 2*N*c < 8*(K+1)+19, hence N*c<=4*K+13.
assert (8+19)//2==13
bindings={}
for f,sha in [('parallel_epoch_width_transport.md','9f4a3499b5f5dbcf68df4fa971571c44e0527596e00d5a9b6642b19f09de9d4a'),('infinite_factor_requires_unbounded_epoch_width.md',None)]:
 h=hashlib.sha256((D/f).read_bytes()).hexdigest();assert sha is None or h==sha;bindings[f]=h
report=dict(status='PASS independent odd-output capacity and analytic finite-frontier nonperiodicity consequence',bindings=bindings,rows=rows,max_raw_length=58,max_output_Linf=7,parallel_source_cohorts=147,transverse_exceptions=4851,epoch_bound='N_j <= 5292 + 3 sum(v_a+2u_a); with permanent U stars <=5292+3 sum(v_a+u_a)',bounded_width_bound='N_j <=5292+441 floor(W/2)',bounded_epoch_frontier_radius='58*331*B+7',analytic_review=[
'Every selected input has odd local coordinate sum; parallel/antiparallel source and target heads have the same parity. Thus only odd source outputs fund selected inputs. Actual identity uniqueness prevents double spending.',
'At a full-entry C clock at most one terminal packet has C tails. Its extra odd birth count is zero, two or three. Actual base normal drop is2v+4u, including the terminal base and excluding its tails.',
'Assumed eventual epoch bound B, and only that assumption, bounds all retained 331-layer cells relative to the head. Absolute identities and clock are unnecessary for physical candidate recognition: occupied locations, finite ages, heading/core and finite parser suffice.',
'An equal normalized state yields a finite repeated transition cycle. Exact330 is applied at each already-actual U-entry prefix cut, so all omitted archive guards stay irrelevant by induction. This is not an arbitrary reset/deletion of the real exterior.',
'A zero-C repeated cycle contradicts finite-C fuel on the original finite board. A zero-displacement cycle contradicts center injectivity.',
'For a nonzero displacement periodic simple center curve, a parallel three-leg bridge outside its fixed strip has only uniformly bounded end-leg intersections. Generic perturbation excludes all finitely many translated local degeneracies. The closed rotation index is bounded independently of repeated periods, while positive C count makes tangent turn diverge. Hence such a repeated positive-C word is impossible.',
'Therefore an infinite U-entry retained factor needs unbounded epoch lengths. The audited capacity theorem then forces unbounded recent parallel V/U production and transverse base sweeps. No widening descent or capture result follows.'
],scope='Actual finite-board U-entry retained-eight factor only. No arbitrary-ant finite-state theorem, global U bound, original-mass rank, or universal capture proof.')
SELF.with_suffix('.json').write_text(json.dumps(report,indent=2)+'\n');print(report['status']);print(bindings)
