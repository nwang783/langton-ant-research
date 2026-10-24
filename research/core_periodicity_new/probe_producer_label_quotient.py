from pathlib import Path
import json,sys,collections
J=json.loads(Path(sys.argv[1]).read_text());B=json.loads(Path(J['base_model_file']).read_text());W=Path('/workspace/shared/langton/word_stabilization');G=json.loads((W/'dcv_residual_core_resources.json').read_text())['geometry'];F={tuple(map(int,l.split()[:5]))for l in(W/'seven_sub_dcv_star4_kernel.tsv').read_text().splitlines()};FP={tuple(map(int,l.split()[:7]))for p in[W/'dcv_protected_patch2_kernel.tsv',Path(J['extra_guard_file'])]for l in p.read_text().splitlines()};H={tuple(r)for r in J['candidate_hypotheses']}
def rot(p,h):
 x,y=p;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
for L in J['producer_labels']:
 sigs=[];q=L['cell']
 for lab in L['codes']:
  s=[]
  if lab:
   for ii,(sid,to,k,v,f,goal,a)in enumerate(B['transitions']):
    x,y,h=B['poses'][sid];z=rot((q[0]-x,q[1]-y),-h)
    if list(z)not in G[a]['inputs']:continue
    px,py,hh=lab['pose'];rel=rot((x-px,y-py),-hh);row=(lab['packet'],a,*rel,(h-hh)%4,*G[lab['packet']]['outputs'][lab['slot']]);signed=row[:5]in F or row in FP;induct=row in H and(not goal or not lab['outer_origin'])
    if signed or induct:s.append(ii)
  sigs.append(tuple(s))
 cs=collections.Counter(sigs);print(q,'codes',len(L['codes']),'classes',len(cs),'bits',(len(cs)-1).bit_length(),'empty',cs[()])
