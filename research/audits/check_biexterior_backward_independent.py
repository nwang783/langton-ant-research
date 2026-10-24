from pathlib import Path
from collections import Counter
import json,hashlib
SELF=Path(__file__).resolve();ROOT=SELF.parents[1];D=ROOT/'global_biexterior_2026-10-23'
base=SELF.with_name('check_biexterior_return_independent.py').read_text();exec(base.split('stats=Counter();maxdelay=0')[0])
stats=Counter();maximum=0

def forward(B,p,h):
 h=(h+(-1 if p in B else 1))%4;B.symmetric_difference_update({p});return p+dirs[h],h

def backward(B,p,h):
 q=p-dirs[h];hh=(h-1 if q in B else h+1)%4;B.symmetric_difference_update({q});return q,hh

def connected_black(B,u,v):
 graph={}
 for q in B:
  for e in (1+1j,1-1j):
   a,b=2*q-e,2*q+e;graph.setdefault(a,set()).add(b);graph.setdefault(b,set()).add(a)
 seen={u};todo=[u]
 while todo:
  a=todo.pop()
  for b in graph.get(a,()):
   if b not in seen:seen.add(b);todo.append(b)
 return v in seen

def check(B0,p0,h0):
 global maximum
 stats['starts']+=1;B=set(B0);p=p0;h=h0;m=len(B)
 if all(exterior(B,p,h)):return
 stats['non_biexterior']+=1;rs=rectangles(B);r,=[r for r in rs if inside(p,r)];k=len(r[4]);a=r[1]-r[0]+1;b=r[3]-r[2]+1;area=a*b;rad=(a+b-1)//2;c=(r[0]+r[2]+r[1]+r[3])//2
 bound=(area+2)*(3**rad-1)+1;outside={q for q in B if not inside(q,r)};initial=clock2(B,p,h,c);t=0
 while True:
  assert inside(p,r);old=(set(B),p,h);oldclock=clock2(B,p,h,c)
  assert initial-oldclock<=2*(area+2)*(3**rad-1)
  p,h=backward(B,p,h);t+=1;stats['inverse_steps']+=1
  f=set(B);pp,hh=forward(f,p,h);assert(f,pp,hh)==old
  assert oldclock-clock2(B,p,h,c)>=2
  assert len(B)<=m-k+area+1<=m*m+1
  assert abs(p.real-p0.real)+abs(p.imag-p0.imag)<=a+b-1<=2*m-1
  out={q for q in B if not inside(q,r)}
  if inside(p,r):assert out==outside
  else:assert out==outside|{p} and all(not inside(p,s)for s in rs);stats['last_step_outside']+=1
  if all(exterior(B,p,h)):break
  assert inside(p,r) and out==outside
 assert t<=bound;maximum=max(maximum,t)
 # First positive return from the computed negative section is exactly our
 # original nonsection state followed by its signed forward section.
 return t
cells=[complex(x,y)for x in range(-1,2)for y in range(-1,2)]
for mask in range(512):
 B={q for i,q in enumerate(cells)if mask>>i&1};rs=rectangles(B)
 for p in cells:
  for h in range(4):check(B,p,h)
 for x in range(-2,3):
  for y in range(-2,3):
   q=complex(x,y)
   if any(inside(q,r)for r in rs):continue
   old=white_components(B);new=white_components(B|{q})
   for e in(1+1j,1-1j):
    assert not connected_black(B,2*q-e,2*q+e);stats['no_new_cycle']+=1
   # Compare actual finite/infinite status at all nearby vertices, including
   # both diagonal lattices, not only the two active vertices.
   for xx in range(-5,6,2):
    for yy in range(-5,6,2):assert old(complex(xx,yy))==new(complex(xx,yy))
   for h in range(4):
    assert all(exterior(B,q,h));copy=set(B);p,hh=forward(copy,q,h);assert all(exterior(copy,p,hh));stats['exterior_writer_steps']+=1
for B in [{complex(x,y)for x in range(-2,3)for y in range(-2,3)}|{100+100j,101+100j,100+101j,101+101j}]:
 for p in(0j,1,1j,-1,-1j):
  for h in range(4):check(B,p,h)
note=D/'backward_section_and_hull_growth.md';expected='6c69dc044317f07cc2a4a8d843a0aeda76477909185ddf033421324c3787cd9b';assert hashlib.sha256(note.read_bytes()).hexdigest()==expected
out={'status':'PASS: backward section recurrence, complete-state bijection and topology-free outside-hull writer step','note_sha256':expected,'counts':dict(stats),'maximum_backward_delay':maximum,'analytic_review':['A newly closed black cycle minus the outside edge would be an old black path. Adjacent old edge midpoints are Chebyshev-near, so the path is in one separated rectangle. The outward endpoint of the new edge lies strictly beyond every old endpoint, impossible.','Planar duality makes both white edges nonbridges. Existing black cycles remain inside the old rectangles; neither active opposite-lattice vertex based at an outside integer head can be enclosed, including the extreme-line equality case.','The inverse map toggles the previous head q=p-dir(h). Current black implies undone R and h-1; current white implies undone L and h+1. Pre-return heads stay in the same old rectangle. Only the final inverse update may add one outside black.','Exactly tau_minus-1 internal inverse transitions fit the same strict-clock range. Displacement<=a+b-1<=2m-1 and mass<=m-k+ab+1<=m^2+1. Initial section states use tau0; m0/m1 are already section states.','Invertibility and finite-support recurrence in both directions make first positive and first negative returns mutual inverses on the full section. This is not a finite quotient or a capture theorem.','Any section R step outside the current rectangle union removes two nonbridge white edges. Both active vertices retain their infinite component, so the step stays on the section and births no black cycle. A nontrivial trapped excursion must begin at an interior white cell.']}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(stats,maximum)
