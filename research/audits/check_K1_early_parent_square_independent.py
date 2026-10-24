from pathlib import Path
from itertools import product
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'K1_pipeline_detours_2026-10-23'
# The already independent complete old/new-port checker supplies our own solver.
s=(SELF.parent/'check_K1_bit11_two_branch_waits_independent.py').read_text().split('results={}')[0]
ns={'__file__':str(SELF.parent/'check_K1_bit11_two_branch_waits_independent.py')};exec(s,ns)
# Recompile the same independent equation solver with the additional physical square.
base=ns['s'];extra="""
 firstP=[next((v,k)for k,x in enumerate(out(hs[v]))if x==di)for v,di in [('x',0),('g',1),('u',2),('e',3)]]
 pb=(parent_birth,1)
 if pb not in firstP:return None
 for x in firstP:
  if x!=pb and not lower(pb,x,1):return None
 if not lower(('e',0),('A',1),4):return None
 if not lower(('A',1),('B',1),15):return None
"""
base=base.replace('nc=len(set(comp.values()));dist=[0]*nc',extra+'\n nc=len(set(comp.values()));dist=[0]*nc')
exec(base,ns);solve=ns['solve'];choices=ns['choices'];H=ns['H'];T=ns['T'];ns['mode']='new'
ns['order']=[('A',1),('B',0),('A',2),('B',1),('D',0),('B',2),('D',1)]
prior=json.loads((D/'bit11_new_first_branch_full_ports.json').read_text())['rows']
# Prior complete rows were independently reconstructed and compared, not guessed.
assert json.loads((SELF.parent/'check_K1_bit11_two_branch_waits_independent.json').read_text())['results']['new']['survivors']==324
baseports=ns['baseports']+[('e',3,'x'),('x',0,'g'),('g',1,'u')]
rows=[];attempts=0
for pr in prior:
 if not pr['headings']['e'].startswith('S'):continue
 ns['ports']=baseports+([('v',1,'D')]if pr['kind']=='S'else[('v',1,'w'),('w',2,'D'),('D',3,'B')]);ns['birth']=(pr['birth'],1)
 for xm,gm,pb in product(('strict','equal'),('strict','equal'),('x','g')):
  for x,g in product(choices(3,xm),choices(0,gm)):
   if pb=='x'and not T(x).startswith('EEW'):continue
   if pb=='g'and not T(g).startswith('SSN'):continue
   attempts+=1;ns['parent_birth']=pb;hs={v:H(h)for v,h in pr['headings'].items()};hs.update(x=x,g=g);sol=solve(hs)
   if sol is None:continue
   cp,de=sol
   def eq(a,b,k):assert cp[a]==cp[b]and de[a]-de[b]==k,(pb,a,b,k)
   assert xm==gm=='equal';eq((pb,1),('e',0),-3 if pb=='x'else-2)
   if pb=='g':
    for a,k in [(('x',2),9),(('g',2),10),(('u',1),11),(('t',0),12),(('a',0),13),(('Y',1),14),(('B',1),15)]:eq(a,('A',1),k)
   else:eq(('x',3),('A',1),9)
   rows.append(dict(kind=pr['kind'],headings={v:T(h)for v,h in hs.items()},parent_birth=pb,xother=xm,gother=gm))
ref=json.loads((D/'bit11_early_parent_left_square_ports.json').read_text());key=lambda r:(r['kind'],r['parent_birth'],r['xother'],r['gother'],tuple(sorted(r['headings'].items())))
assert attempts==10206 and len(rows)==99 and{key(r)for r in rows}=={key(r)for r in ref['rows']}
profiles=sorted({(r['headings']['e'],r['headings']['u'],r['headings']['x'],r['headings']['g'],r['parent_birth'])for r in rows});assert len(profiles)==6
# Minimum xL3(W) -> uL1(E), displacement(1,1), forced initial L then alternating axes.
dirs=(1j,1,-1j,-1);minimum=None
for n in range(1,7):
 for w in product('LR',repeat=n):
  if w[0]!='L':continue
  p=0j;h=3
  for a in w:h=(h+(1 if a=='R'else-1))%4;p+=dirs[h]
  if(p,h)==(1+1j,1):minimum=n;break
 if minimum:break
assert minimum==6
note=D/'K1_early_parent_six_left_square_profiles.md';assert hashlib.sha256(note.read_bytes()).hexdigest()=='8592d1c4875c7683470d00ba00c8d3d8a8b3070bc92dc16165f90455d4038e6b'
out=dict(status='PASS six early-parent physical-square profiles, actual birth directions and main clocks',note_sha256=hashlib.sha256(note.read_bytes()).hexdigest(),candidates=attempts,survivors=len(rows),profiles=profiles,analytic='Both further-left faces are max. Birth at x gives canonical STRAIGHT chain and beta-alpha>=19 from the actual xL3alpha+9 event and six-step minimum. Birth at g gives canonical LEFT chain and the exact consecutive suffix beta-alpha=15. Parent birth times delta-3/delta-2 preserve all physical lifts. No Gamma K1 pipeline is imported off the main curve.',scope='One further necessary square, no exterior realization, iterated parent, original fuel, or noLL extension. Section5 remains explicitly unsigned speculation.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(attempts,len(rows),profiles)
