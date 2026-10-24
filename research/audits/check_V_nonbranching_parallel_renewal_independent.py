from pathlib import Path
import json,hashlib
SELF=Path(__file__).resolve();ns={'__file__':str(SELF.parent/'check_U_first_helper_ports_independent.py')};exec((SELF.parent/'check_U_first_helper_ports_independent.py').read_text().split('rows=[];gates=[];adjacent_rejects=[]')[0],ns)
globals().update({k:ns[k]for k in('ROOT','G','IDS','xy','rotation','chords','edge')})
D=ROOT/'causal_archive_frontier_2026-10-23';roles={4:1+2j,5:1+2j,6:3j,7:3j,8:3j,9:3j};rows=[];C=2+1j
for a,q in roles.items():
 assert q in G[a]['I']and sum(xy(q))==3
 for h in(0,2):
  p=C-rotation(q,h);mu=sum(xy(p))+(3 if h==0 else-3);assert mu==3
  entry,exit=chords(a,p,h)[0];assert sum(xy(exit))==2*mu and(int(exit.real-exit.imag)%4)==0
  assert all(sum(xy(v))==2*mu for v in edge(C))
  rows.append(dict(consumer=a,pose=[*xy(p),h],selected=xy(q),base_exit=xy(exit),mu=mu))
# All four actual axes: rotate AND translate a real sector-compatible root to0,N.
for h in range(4):
 p=complex(2+h%2,2);q=p+rotation(C,h)
 assert(sum(xy(p))+h)%2==0
 transformed={rotation(v-2*p,-h)for v in edge(q)}
 assert transformed==set(edge(C))and all(sum(xy(v))==6 for v in transformed)
 for a in roles:
  ex=chords(a,p,h)[0][1];ex0=rotation(ex-2*p,-h)
  assert sum(xy(ex0))==6 and int(ex0.real-ex0.imag)%4==0
E=list(range(2,295,2));A=4851+3*len(E);assert len(E)==147 and A==5292 and 2*A==10584 and 2*len(E)+1==295
for L in range(-5,8):
 for m in range(1,20):
  H=L+m-1;source=set(range(L-294,H-1));target=set(range(L,H+1));assert len(source)==m+292
  assert source-target<=set(range(L-294,L));assert target-source<=set(range(H-1,H+1))
  assert 4851*m+3*len(source)==4854*m+876
# Input capacities are genuine identity capacities, never reused by different consumers.
reports=['check_U_parallel_selected_supply_independent','check_V_parallel_reproductive_supply_independent','check_parallel_width_and_infinite_epoch_independent','check_full_context_horizon_independent']
deps={}
for name in reports:
 p=SELF.parent/(name+'.json');assert json.loads(p.read_text())['status'].startswith('PASS');deps[p.name]=hashlib.sha256(p.read_bytes()).hexdigest()
p=D/'V_nonbranching_parallel_renewal.md';sha=hashlib.sha256(p.read_bytes()).hexdigest();assert sha=='a0c512a14a0579b69270cb89902ccc0bd81f3b33bd1498bd6a7f60031b7195af'
out=dict(status='PASS coefficient-one nonbranching V renewal and physical rail synthesis',note_sha256=sha,rows=rows,dependencies=deps,inequalities={'Q':'v_j+u_j<=5292+sum_even2..294 v','N':'N_j<=5292+sum_even2..294 v+v_(j-4)+u_(j-6)','bounded_V':'N eventually<=10584+295M','block_Q':'sum_Q<=4854m+876+sum_padded_V','block_U':'sum_U<=4854m+876+sum_left_boundary_V','bounded_depth':'v_j<=r0+5292*(294*(L-1)+1)'},analytic='Graph edges follow the one original V-base C identity into a parallel reproductive distinguished input. Actual once-only spending gives outdegree<=1, unique selected input gives indegree<=1, even positive age gives acyclic finite ancestor chains and U terminal. Produced roots are perpendicular-selected or boundary-tail-selected, at most5292 per clock, and entry-selected roots total at most r0. After rotating AND translating a path root to0,N, actual shared support edges and base exits lie on invariant physical diagonal mu=x+y+3s; simplicity makes exits distinct with normal separation2. Epoch heads progress strictly in z, so vertices in an epoch are on distinct rails and paths. Uniform path depth bounds parent clock window, hence V counts; signed infinite-factor epoch necessity then demands unbounded depth unless a stronger role exclusion closes it.',scope='Simple U-entry complete-eight factors, growing frontier. No uniform root count over all clocks or universal capture claim. Later same-heading ordinary-child exclusion is separate.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
