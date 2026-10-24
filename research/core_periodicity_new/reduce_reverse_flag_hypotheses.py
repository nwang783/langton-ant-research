"""Read an exact reverse-flag invariant and retain only H rows needed by it.
CLI original.json original.dat certificate.bdd signed_only.json OUT.tsv
Always verify the regenerated reduced-H model against the fixed invariant afterward.
"""
from pathlib import Path
import json,runpy,sys
orig,dat,cert,plain,out=sys.argv[1:];J=json.loads(Path(orig).read_text());B=json.loads(Path(plain).read_text());assert J['n']==B['n'] and J['start']==B['start'] and len(J['transitions'])==len(B['transitions']);H={tuple(r)for r in J['candidate_hypotheses']};sys.argv=['verify_protected_patch_bdd_flags.py',dat,cert];V=runpy.run_path(str(Path(__file__).with_name('verify_protected_patch_bdd_flags.py')));bad=V['violating'];roots=V['roots'];needed=set();tx,ty,th=J['target_pose'];target=J['target'];n=J['base_n']
def rot(p,h):
 x,y=p;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
for t,b in zip(J['transitions'],B['transitions']):
 if t==b:continue
 src,dst,k,v,f,c,g,a=b;assert not g and a<99
 if not bad(roots[src],roots[dst],k,v,f,c):continue
 x,y,h=J['poses'][dst];rel=rot((tx-x,ty-y),-h)
 for j,q in enumerate(J['target_flag_cells']):
  bit=1<<(n+j)
  if not(t[2]&~k&bit):continue
  qp=rot((q[0]-x,q[1]-y),-h);row=(a,target,*rel,(th-h)%4,*qp);assert row in H
  if bad(roots[src],roots[dst],k|bit,v|bit,f,c):needed.add(row)
Path(out).write_text(''.join(' '.join(map(str,r))+'\n'for r in sorted(needed)));print(json.dumps({'original_hypotheses':len(H),'retained':len(needed),'rows':sorted(needed)}))
