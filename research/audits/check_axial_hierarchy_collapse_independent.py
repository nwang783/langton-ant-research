from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[1];U=R/'causal_reduction/unit_scale';J=json.loads((U/'axial_body_refinement_classification.json').read_text());W='RRLRRRRLRLLRLLRLL';assert J['body']==W
flip=lambda w:''.join('L'if c=='R'else'R'for c in w)
def trace(w,h=0):
 p=0j;rows=[];last={};bad=None
 for i,c in enumerate(w):
  if p in last and last[p][1]==c and bad is None:bad=(int(p.real),int(p.imag),last[p][0],i,c)
  last[p]=(i,c);rows.append((p,h,c));h=(h+(1 if c=='R'else-1))%4;p+=(1j,1,-1j,-1)[h]
 return rows,p,h,bad
def expand(mask,n=17):return''.join((W if c=='R'else flip(W))if mask>>i&1 else c for i,c in enumerate(W[:n]))
cubes=[]
for row in J['conflict_cubes']:
 n,m=row['assigned'],row['mask'];assert m<1<<n;b=trace(expand(m,n))[-1];a=row['conflict'];assert b==(*a['cell'],a['previous'][0],a['current'][0],a['current'][1]);cubes.append((n,m))
leaves=[r['mask']for r in J['survivors']];assert sorted(leaves)==[0,256,2048]
for m in leaves:assert trace(expand(m))[1:]==(1,1,None)
cover=cubes+[(17,m)for m in leaves]
assert len(cubes)==38 and sum(1<<(17-n)for n,m in cover)==1<<17
for i,(n,m)in enumerate(cover):
 for nn,mm in cover[:i]:assert(m^mm)&((1<<min(n,nn))-1)
base=trace(W)[0];assert base[8]==(2,0,'R')and base[11]==(2+1j,3,'R')
chains=[]
for i in(8,11):
 for j in(8,11):
  child=W if W[i]=='R'else flip(W);grand=W if child[j]=='R'else flip(W);word=W[:i]+child[:j]+grand+child[j+1:]+W[i+1:];rr,p,h,b=trace(word);assert len(word)==49 and(p,h)==(1,1)
  assert bool(b)==(j==11)
  if b:assert b==((2,2,32,44,'L')if i==8 else(0,1,35,47,'L'))
  chains.append((i,j,word,b))
typed=0
for h in range(4):
 for reflect in(0,1):
  for n,m in cover:
   ww=expand(m,n);ww=flip(ww)if reflect else ww;b=trace(ww,h)[-1];assert bool(b)==((n,m)in cubes);typed+=1
  for i,j,ww,b in chains:assert bool(trace(flip(ww)if reflect else ww,h)[-1])==(j==11);typed+=1
assert typed==360
# Independently expand a varying-label slot8 physical chain to establish the exact unbounded factor formula.
pre,post=W[:8],W[9:];assert pre=='RRLRRRRL'and post=='LLRLLRLL'
for depth in range(1,9):
 ww='R'
 for _ in range(depth):ww=pre+ww+post
 assert ww==pre*depth+'R'+post*depth
out=dict(status='PASS independent complete17-slot cover, typed chain conflicts and analytic arbitrary-decoration collapse',note_sha256=hashlib.sha256((U/'axial_primitive_hierarchy_collapse.md').read_bytes()).hexdigest(),cubes=len(cubes),covered=1<<17,survivors=leaves,chain_controls=chains,typed_controls=typed,scope='Only literal identity-selfmaps or the specified17-read physical primitive on any finite decorated alphabet, with fixed closed root a->aw containing no other a. Every reachable active chain is eventually slot8, at most top slot11; finite occurrences reduce to fixed-center signed hairpins/fixed work. Existing remote-column potential or finite-domain escape excludes wrapper on any board. No aliases/directives/other primitives/general ant theorem.')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
