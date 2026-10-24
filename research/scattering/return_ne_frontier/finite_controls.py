"""Independent finite-seed controls, not universal proof by sampling."""
import sys,json
from pathlib import Path
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1]
sys.path.insert(0,str(ROOT/'continuation_2026-10-22/ant_continuation'))
from ant_exact import W,plan,step,certify_period
fresh=plan(W,(0,0),1)[0];rows=[]
for m,n in [(100,200),(101,201),(100,201)]:
 for r in json.loads((HERE/'bridge.json').read_text())['rows']:
  phase=r['phase'];q=(-2*n-33,-2*n-14);s=(6-2*m+fresh[phase][0],-43-2*m+fresh[phase][1]);B={q,s};p=(0,0);h=0;t=r['capture_time_n_constant'][0]*n+r['capture_time_n_constant'][1]
  for _ in range(t):p,h,ch=step(B,p,h)
  assert [list(p),h]==r['capture_pose'];tw=W[r['capture_phase']:]+W[:r['capture_phase']];proof=certify_period(B,p,h,tw);assert proof
  rows.append(dict(m=m,n=n,phase=phase,capture=t,pose=[p,h],tail=proof));print(json.dumps(rows[-1]),flush=True)
(HERE/'finite_controls.json').write_text(json.dumps(dict(status='fifteen complete literal finite-seed controls; not an extrapolation proof',rows=rows),indent=2)+'\n')
