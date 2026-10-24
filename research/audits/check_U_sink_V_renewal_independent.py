from pathlib import Path
import hashlib,json
from check_dcuv_patch_model_independent import ROOT,raws,mark,walk,rotation,xy
SELF=Path(__file__).resolve();D=ROOT/'causal_archive_frontier_2026-10-23';ids=(0,1,4,5,6,7,8,9);K={p for p,b in walk(mark)[2].items()if b};G={}
for s in ids:
 e,h,_,fl=walk(raws[s]);bb={p for p,b in walk(raws[s]+mark)[2].items()if b};G[s]=(bb-K,(bb^fl)-{e+rotation(q,h)for q in K})
rows=[];sel={0:1j,1:1j,4:1+2j,5:1+2j,6:3j,7:3j,8:3j,9:3j}
for s in ids:
 b=0 if s<2 else 4 if s<7 else 7;c=0 if s in(0,4,7)else 1 if s in(1,5,8)else 2
 base=G[b][1];full=G[s][1];assert base<=full;extra=full-base
 odd=lambda cells:sorted([list(xy(q))for q in cells if sum(xy(q))%2])
 assert len(odd(base))=={0:0,4:3,7:5}[b];assert len(odd(extra))=={0:0,1:2,2:3}[c];assert sel[s]in G[s][0]
 rows.append(dict(packet=s,base=b,odd_base=odd(base),odd_extra=odd(extra),C_tails=c,selected=list(xy(sel[s]))))
ref=json.loads((D/'U_sink_V_renewal_controls.json').read_text())
for a,b in zip(rows,ref['rows']):assert all(a[k]==b[k]for k in a)
role=json.loads((SELF.parent/'check_U_parallel_selected_supply_independent.json').read_text());assert role['forced_full_source_entry_C_age']==6 and role['gates']==[[7,0,1,3,2],[8,0,1,3,2],[9,0,1,3,2]]
E=list(range(2,295,2));assert len(E)==147;A=4851+3*len(E)
assert A==5292 and 2*A==10584 and 2*3*len(E)==882
# Interval union endpoints: [L-294,H-2] has (H-L+1)+292 clocks.
assert -2-(-294)==292;assert 4851+3==4854 and 3*292==876
assert sorted(set(E)|{e+6 for e in E})==list(range(2,301,2))
p=D/'U_sink_V_renewal.md';sha=hashlib.sha256(p.read_bytes()).hexdigest();assert sha=='bf610a8ba9efe29419721a49caf345c781c7f09d342656113e97c8ec44473ae9'
out=dict(status='PASS U-base sink and V-specific causal renewal necessity',note_sha256=sha,rows=rows,source_ages=E,constant=A,pointwise=['N_j<=5292+3 sum_even2..294 v_(j-e)+u_(j-6)','v_j+u_j<=5292+3 sum_even2..294 v_(j-e)'],block='sum_I(v+u)<=4854m+876+3 sum_[L-294,H-2] v; all packets add sum_[L-6,H-6]u',eventual='If late v<=M then late N<=10584+882M; hence infinite U-entry factors have unbounded V counts and V transverse sweep.',analytic='Each post-entry nonperpendicular consumer spends one distinguished identity. Odd V-base supply is three per genuine V producer; odd tail supply at mostthree across the unique positive-C boundary packet in an epoch. Signed universal U-base role contributes only one arm to plainD at exactlyage6, never to V/U. Whole-block accounting spends each identity onlyonce across all consumer clocks, yielding m+292 source clocks. The two pointwise windows combine to even ages2..300. These are exact capacities, not sufficient realizability or contraction.',scope='No original historical-component separation, uniform V bound, periodic-profile assumption, mass-only budget, or universal capture. Numerical growing-V budgets are relaxations, not physical controls.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
