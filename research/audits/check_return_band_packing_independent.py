from pathlib import Path
from collections import Counter
import json,hashlib
S=Path(__file__);R=S.parents[1];P=R/'global_attraction_bridge_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
ns={'__file__':str(S.with_name('check_return_permanent_debt_independent.py'))};exec(Path(ns['__file__']).read_text().split('results=[check_case')[0],ns)
twenty,verify_future,vec,pair=[ns[x] for x in ('twenty','verify_future','vec','pair')]
M=json.loads((P/'RETURN_BAND_PACKING_MANIFEST.json').read_text())
for group in ('files','signed_dependencies'):
 for f,v in M[group].items():assert sha(P/f)==v
J=json.loads((P/'RETURN_BAND_PACKING_CHECKED.json').read_text());N=249067;seed=twenty(400);B={q:-i-1 for i,q in enumerate(sorted(seed,key=lambda z:(z.real,z.imag)))};initial=dict(B);p=0j;h=1;poses=[];born={};dead={};events=[]
for t in range(N):
 poses.append(p)
 if p in B:old=B.pop(p);dead[old]=t;h=(h-1)%4
 else:old=None;B[p]=t;born[t]=p;h=(h+1)%4
 events.append((p,old));p+=vec[h]
poses.append(p);word,d,tail,tests=verify_future(B,p,h);dead.update({i:N+k for i,k in tail.items()})
band=lambda q:-1000<=q.real<=-1
L=[sum(i in dead for i in initial.values())];LJ=[sum(i in dead and band(q) for q,i in initial.items())];PJ=[0];perm=[]
for t,(q,old) in enumerate(events):
 ch=int(t in dead) if old is None else -1;L.append(L[-1]+ch);LJ.append(LJ[-1]+ch*band(q));isperm=old is None and t not in dead and band(q);PJ.append(PJ[-1]+isperm)
 if isperm:perm.append((t,q))
cap=max(L);assert cap==77
size=1<<(N+1).bit_length();tree=[(float('inf'),N+1)]*(2*size)
for i,q in enumerate(poses):tree[size+i]=(int(q.real),i)
for i in range(size-1,0,-1):tree[i]=min(tree[2*i],tree[2*i+1])
def peak(l,r):
 l+=size;r+=size+1;ans=(float('inf'),N+1)
 while l<r:
  if l&1:ans=min(ans,tree[l]);l+=1
  if r&1:r-=1;ans=min(ans,tree[r])
  l//=2;r//=2
 return ans
selected=[];delta=[0]*(N+1)
for b,q in born.items():
 dd=dead.get(b)
 if dd is None or dd>N or q.real<0 or poses[b+1].real<0:continue
 px,tau=peak(b+1,dd)
 if px>=-1000:continue
 a=b+1;stock=LJ[a]+2*LJ[tau]+LJ[dd];paid=PJ[dd]-PJ[a];assert stock+paid>=4000 and paid>=4*(1000-cap)
 selected.append(dict(birth=b,death=dd,cell=pair(q),peak_cut=tau,peak_x=px,band_relevant_at_three_cuts=[LJ[a],LJ[tau],LJ[dd]],permanent_band_births=paid,exact_stock_debt=stock));delta[a]+=1;delta[dd]-=1
assert selected==J['selected_returns'] and len(selected)==23
mult=[];active=0
for t in range(N):active+=delta[t];assert active<=L[t];mult.append(active)
used=[(t,q) for t,q in perm if mult[t]];Q=max(mult[t] for t,q in perm);weighted=sum(mult[t] for t,q in perm)
assert len({q for t,q in used})==len(used)==12006 and weighted==275949 and Q==23
assert weighted==sum(r['permanent_band_births'] for r in selected)
dis=[];last=-1
for r in sorted(selected,key=lambda r:r['death']):
 if r['birth']+1>=last:dis.append(r['birth']);last=r['death']
assert dis==[60] and dis==J['disjoint_selected_births']
assert [int(min(q.imag for t,q in used)),int(max(q.imag for t,q in used))]==J['permanent_output_y_range']==[-999,1199]
assert J['lower_bound']==4*23*(1000-cap)==84916 and J['upper_bound']==cap*len(used)
report=dict(status='PASS fixed-band permanent-output packing and fixed-module transverse-spread consequence',manifest_sha256=sha(P/'RETURN_BAND_PACKING_MANIFEST.json'),proof_sha256=sha(P/'RETURN_BAND_PERMANENT_PACKING.md'),independent_checker_sha256=sha(S),full_control_updates=N,all_future_parity_tests=tests,selected_returns=selected,distinct_permanent_band_cells=len(used),weighted_charges=weighted,maximum_multiplicity=Q,disjoint_selected_births=dis,analytic_scope=['Summing signed per-line debt on the SAME w strict crossing lines costs4(w-M) actual permanent births per returning lifetime. Every charge at s corresponds to a distinct marked member of ENTIRE C*(s), so multiplicity<=M; disjoint half-open intervals give1. Permanent births cannot revisit one physical cell, making|S| an actual finite spatial capacity.','Infinitely many late-born completed returns in one FIXED finite birth module with unbounded radii have an unbounded axis/sign subsequence. Any fixed sufficiently outward band is crossed by infinitely many; arbitrary finite subcollections force unbounded transverse permanent support. Finite past prefixes cannot supply an unbounded-radius late subsequence, and finite deaths allow a disjoint extraction if desired.','No recurrent fixed module, width bound, relevant cap or universal contradiction is supplied. Migrating birth modules and unbounded permanent output remain escapes. The named23 overlapping returns contain only ONE greedily disjoint interval, not23 independent charges.'])
S.with_suffix('.json').write_text(json.dumps(report,indent=2)+'\n');print('PASS',sha(S.with_suffix('.json')))
