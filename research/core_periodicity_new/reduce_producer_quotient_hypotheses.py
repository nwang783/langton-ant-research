"""Reduce H using a fixed quotient invariant; regenerate and verify afterward.
CLI QUOTIENT.json QUOTIENT.dat CERT.bdd PLAIN.json OUT.tsv
"""
from pathlib import Path
import json,runpy,sys
orig,dat,cert,plain,out=sys.argv[1:];J=json.loads(Path(orig).read_text());B=json.loads(Path(plain).read_text());assert J['n']==B['n']and J['start']==B['start'];W=Path('/workspace/shared/langton/word_stabilization');G=json.loads((W/'dcv_residual_core_resources.json').read_text())['geometry'];F={tuple(map(int,l.split()[:5]))for l in(W/'seven_sub_dcv_star4_kernel.tsv').read_text().splitlines()};FP={tuple(map(int,l.split()[:7]))for p in[W/'dcv_protected_patch2_kernel.tsv',Path(J['extra_guard_file'])]for l in p.read_text().splitlines()};H={tuple(r)for r in J['candidate_hypotheses']};sys.argv=['verify_protected_patch_bdd_labels.py',dat,cert];V=runpy.run_path(str(Path(__file__).with_name('verify_protected_patch_bdd_labels.py')));bad=V['violating'];roots=V['roots'];needed=set();tested=0;violating_edges=0

def rot(p,h):
 x,y=p;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
for sid,to,k,v,f,clear,reset,goal,a in B['transitions']:
 if not bad(roots[sid],0 if goal else roots[to],k,v,0 if goal else f,0 if goal else clear,0 if goal else reset):continue
 violating_edges+=1;x,y,h=J['poses'][sid]
 for L in J['producer_label_classes']:
  q=L['cell'];local=rot((q[0]-x,q[1]-y),-h)
  if list(local)not in G[a]['inputs']:continue
  lm=((1<<L['bits'])-1)<<L['offset']
  for code,cl in enumerate(L['classes']):
   if any(lab is None for lab in cl['members']):continue
   dep=set();allbad=True
   for lab in cl['members']:
    px,py,hh=lab['pose'];rel=rot((x-px,y-py),-hh);row=(lab['packet'],a,*rel,(h-hh)%4,*G[lab['packet']]['outputs'][lab['slot']])
    if row[:5]in F or row in FP:continue
    if row in H and(not goal or not lab['outer_origin']):dep.add(row)
    else:allbad=False;break
   lv=code<<L['offset']
   if not allbad or not dep or((v^lv)&k&lm):continue
   tested+=1
   if bad(roots[sid],0 if goal else roots[to],k|lm,(v&~lm)|lv,0 if goal else f,0 if goal else clear,0 if goal else reset):needed|=dep
Path(out).write_text(''.join(' '.join(map(str,r))+'\n'for r in sorted(needed)));print(json.dumps({'original_hypotheses':len(H),'retained':len(needed),'violating_plain_edges':violating_edges,'tested_classes':tested,'rows':sorted(needed)}))
