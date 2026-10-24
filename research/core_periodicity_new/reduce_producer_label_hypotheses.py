"""Retain only H rows occurring in a signed-only transition that leaves a fixed invariant.
The regenerated reduced-H graph MUST be independently invariant-verified afterward.
CLI original.json original.dat certificate.bdd signed_only.json OUT.tsv
"""
import json,runpy,sys
from pathlib import Path
orig,dat,cert,plain,out=sys.argv[1:];J=json.loads(Path(orig).read_text());B=json.loads(Path(plain).read_text());assert J['producer_labels']==B['producer_labels'];assert J['poses']==B['poses'];assert J['start']==B['start'];assert J['n']==B['n'];H={tuple(r)for r in J['candidate_hypotheses']};sys.argv=['verify_protected_patch_bdd_labels.py',dat,cert];V=runpy.run_path(str(Path(__file__).with_name('verify_protected_patch_bdd_labels.py')));bad=V['violating'];roots=V['roots'];G=json.loads(Path('/workspace/shared/langton/word_stabilization/dcv_residual_core_resources.json').read_text())['geometry'];needed=set();tested=0;violating_edges=0

def rot(p,h):
 x,y=p;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
for sid,to,k,v,f,clear,reset,goal,a in B['transitions']:
 if not bad(roots[sid],0 if goal else roots[to],k,v,0 if goal else f,0 if goal else clear,0 if goal else reset):continue
 violating_edges+=1;x,y,h=J['poses'][sid]
 for L in J['producer_labels']:
  q=L['cell'];local=rot((q[0]-x,q[1]-y),-h)
  if list(local)not in G[a]['inputs']:continue
  lm=((1<<L['bits'])-1)<<L['offset']
  for code,lab in enumerate(L['codes']):
   if not code or(goal and lab['outer_origin']):continue
   px,py,hh=lab['pose'];rel=rot((x-px,y-py),-hh);row=(lab['packet'],a,*rel,(h-hh)%4,*G[lab['packet']]['outputs'][lab['slot']]);lv=code<<L['offset']
   if row not in H or((v^lv)&k&lm):continue
   tested+=1
   if bad(roots[sid],0 if goal else roots[to],k|lm,(v&~lm)|lv,0 if goal else f,0 if goal else clear,0 if goal else reset):needed.add(row)
Path(out).write_text(''.join(' '.join(map(str,r))+'\n'for r in sorted(needed)));print(json.dumps({'original_hypotheses':len(H),'retained':len(needed),'violating_plain_edges':violating_edges,'tested_label_codes':tested,'rows':sorted(needed)}))
