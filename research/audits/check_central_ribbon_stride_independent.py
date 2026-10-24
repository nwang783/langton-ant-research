from pathlib import Path
from collections import Counter,deque
import hashlib,json
ROOT=Path('/workspace/shared/langton');P=ROOT/'causal_reduction/unit_scale';A=ROOT/'new_constructive_2026-10-23';SELF=Path(__file__).resolve()
wave=json.loads((P/'prepared4352_output_return_wave.json').read_text());word=wave['word']
assert len(word)==15324 and hashlib.sha256(word.encode()).hexdigest()=='12c75ada3474e89e5fb99af4bb029ab9f7aa4de232d4fc6c213601d1c849db27'
normal=json.loads((P/'prepared15324_return_normal_form.json').read_text());base={tuple(q) for q in normal['bulk_mod26']};assert len(base)==964
initial={(t,r+26*k) for t,r in base for k in range(3)};assert len(initial)==2892
p=13+7j;heading=1j;reads=Counter()
for turn in word:
 reads[int(p.real-p.imag),int(p.real)%78]+=1
 heading*= -1j if turn=='R' else 1j;p+=heading
assert p==-65-71j and heading==1j and len(reads)==3557
odd={q for q,n in reads.items() if n%2};settled=initial^odd
assert len(odd)==1972 and len(initial&reads.keys())==1439 and len(settled&reads.keys())==1847 and len(settled)==3300
assert (min(t for t,a in settled),max(t for t,a in settled))==(-64,92)
DIV=(1,2,3,6,13,26,39,78);directions=(1,-1,1j,-1j);reports=[]
def compatible(t,a,g):return len({(t,r) in settled for r in range(a,78,g)})==1
def neighbors(v,g):
 t,a=v;p=complex(a,a-t)
 for step in directions:
  q=p+step;x,y=int(q.real),int(q.imag);v2=(x-y,x%g)
  if compatible(*v2,g):yield v2,x//g
reference=json.loads((A/'central_ribbon_stride_divisibility.json').read_text())
for g in DIV:
 seeds={(t,a)for t in range(8,25)for a in range(g)if compatible(t,a,g)}
 finite_allowed={(t,a)for t in range(-66,95)for a in range(g)if compatible(t,a,g)}
 ref=next(r for r in reference['results']if r['gcd']==g)
 assert len(finite_allowed)==ref['allowed_vertices'] and len(seeds)==ref['central_allowed_vertices']
 expected_mixed={(t,a) for t in range(-66,95)for a in range(g)}-finite_allowed
 reported=set()
 for t,a,black,white in ref['color_incompatibility_witnesses']:
  assert black%g==white%g==a and (t,black)in settled and(t,white)not in settled;reported.add((t,a))
 assert reported==expected_mixed
 if g==78:
  # Literal closed quotient walk with nonzero longitudinal lift, not an ant claim.
  start=8,0;v=start;lift=0
  for _ in range(g):
   for step in(1,1j):
    t,a=v;q=complex(a,a-t)+step;x,y=int(q.real),int(q.imag);v=(x-y,x%g);lift+=x//g;assert compatible(*v,g)
  assert v==start and lift==1
  reports.append(dict(g=g,central_vertices=len(seeds),positive_winding=lift));continue
 seen=set();components=[];edge_checks=0
 for start in sorted(seeds):
  if start in seen:continue
  pot={start:0};queue=deque([start]);seen.add(start)
  while queue:
   v=queue.popleft();assert -66<v[0]<94 # checked, never used to truncate adjacency
   for w,k in neighbors(v,g):
    edge_checks+=1
    if w in pot:assert pot[w]==pot[v]+k
    else:pot[w]=pot[v]+k;queue.append(w);seen.add(w)
  # Every actual infinite-graph allowed edge has been tested.
  components.append(pot)
 assert len(components)==len(ref['central_components'])
 for component in components:
  match=[c for c in ref['central_components']if {tuple(q[:2])for q in c['potential']}==set(component)]
  assert len(match)==1;c=match[0];other={(t,a):z for t,a,z in c['potential']};shifts={component[q]-other[q]for q in component};assert len(shifts)==1
  assert c['nonzero_winding_witness']is None and not c['touches_exterior_collar']
 reports.append(dict(g=g,central_vertices=len(seeds),components=len(components),all_edge_checks=edge_checks,full_potentials=[[[t,a,z]for(t,a),z in sorted(c.items())]for c in components]))
# Both signs of proposed stride enumerate the same residue classes.
from math import gcd
for s in range(-160,161):
 if not s:continue
 g=gcd(abs(s),78)
 for x in range(78):assert {(x+k*s)%78 for k in range(78)}==set(range(x%g,78,g))
sha=lambda f:hashlib.sha256(f.read_bytes()).hexdigest()
out=dict(status='PASS independent complete-profile and infinite-quotient closure audit',note_sha256=sha(A/'central_ribbon_stride_divisibility.md'),input_profile_classes=len(initial),full_output_classes=len(settled),read_classes=len(reads),untouched_black_classes=len(initial-reads.keys()),output_profile=sorted(settled),reports=reports,scope='Any eventual heading-return parallel translating word on this exact period78 field plus finite XOR cap that repeatedly reads central normals8..24 has stride divisible78. No finite-slab, finite-seed or existence theorem.',analytic_lemma='For each physical D orbit the maximal spatial slot offset fixes the earliest chronological first-read phase past a finite fringe. A finite prior transient/cap changes finitely many cells. Periodic initial colors therefore are constant on its gcd residue class. Every period is a nonzero-lift closed walk on allowed cells; full central components have exact potentials.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print([(r['g'],r['central_vertices'],r.get('components'))for r in reports])
