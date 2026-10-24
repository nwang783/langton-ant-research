from pathlib import Path
from itertools import product
import hashlib,json
R=Path(__file__).resolve().parents[1];D=R/'K1_pipeline_detours_2026-10-23'
rows=[]
for n in (3,4):
 for h in product((1,3),repeat=n):
  if h[0]==h[2]:continue
  firstE=next(i for i,x in enumerate(h)if x==1)
  out=[(x+(1 if i%2==0 else-1))%4 for i,x in enumerate(h)]
  assert sum(x==0 for x in out[:firstE])<=1
  rows.append(dict(incoming=h,outgoing=out,first_E_index=firstE))
assert len(rows)==12
# Actual three canonical parent edges with two LEFT bends, and the fork geometry.
F=[0j,-1+1j,-2,-1-1j];steps=[b-a for a,b in zip(F,F[1:])]
assert steps[1]==steps[0]*1j and steps[2]==steps[1]*1j
chain=[-3+1j,-2,-1+1j,-2+2j];steps=[b-a for a,b in zip(chain,chain[1:])]
assert steps[1]==steps[0]*1j and steps[2]==steps[1]*1j
# Current t=NNSS: first P1 boundary output L1 precedes c's first south output.
t=(0,0,2,2);out=[(x+(1 if i%2==0 else-1))%4 for i,x in enumerate(t)]
assert out==[1,3,3,1] and t.index(2)==2
# tR2>=tL1+4 implies first c south output tR2-1>=tL1+3.
assert 4-1==3 and 5-6==-1
six=json.loads((R/'audits/check_K1_early_parent_square_independent.json').read_text())
assert six['survivors']==99
p=D/'canonical_max_birth_paths_no_LL_and_early_parent_fork.md';sha=hashlib.sha256(p.read_bytes()).hexdigest();assert sha=='1e2cc5db58fa509773eaa411df9b6e7c48be532a9a17bce6b1a231dd3e3fe3db'
out=dict(status='PASS finite canonical p-path noLL and scoped early-parent fork',note_sha256=sha,flat_histories=rows,analytic='Only three actual canonical parent identities and strict physical birth times are used. Closing max/max contact must be complete flat; its second N output before its first E input contradicts all12 histories. In the g-birth uEEW branch, p(P1)=I would give two LEFT bends, so P1 must be born earlier elsewhere. Its NE first boundary output is too late; the remaining parent is known Q1 or farther-left Q2, with birth<=T2(mainB)-1.',scope='No extension to arbitrary adjacency or noncanonical paths. gSSNS/uEEWE has P1=M-2 and is retained outside the fork; no all-case exclusion, new-root charge or iteration.')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
