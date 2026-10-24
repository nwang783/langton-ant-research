from pathlib import Path
import random,json,hashlib
P=Path(__file__).resolve().parents[1];f=P/'causal_reduction/matrix_candidates/rectangular_k17_full_domains.txt';it=iter(f.read_text().split());k,a,b=map(int,[next(it),next(it),next(it)]);domains=[]
for _ in range(4):domains.append([tuple(map(int,next(it)))for _ in range(int(next(it)))])
assert not list(it)
vec=[1j,1,-1j,-1];rng=random.Random(314159)
def turn(u,v):
 z=vec[v]/vec[u];assert z in (1j,-1j);return 1 if z==-1j else -1
def curvature(w):return sum(turn(u,v)for u,v in zip(w,w[1:]))
checks=letters=0
for trial in range(8):
 old=[(d,)for d in range(4)];S=D=0
 for r in range(1,5):
  N=rng.choice(domains[0]);E=rng.choice(domains[1]);phi=[N,E,tuple((d+2)%4 for d in N),tuple((d+2)%4 for d in E)]
  new=[sum((old[z] for z in w),())for w in phi]
  seams=[sum(turn(old[u][-1],old[v][0])for u,v in zip(w,w[1:]))for w in phi]
  T=list(map(curvature,new));assert T[0]==T[2] and T[1]==T[3]
  assert T[0]+T[1]==k*S+seams[0]+seams[1]
  assert T[1]-T[0]==D+seams[1]-seams[0]
  assert max(map(abs,seams))<=k-1
  for d,w in enumerate(new):
   p=0j;xs=[0];ys=[0]
   for z in w:p+=vec[z];xs.append(int(p.real));ys.append(int(p.imag))
   expected=complex(vec[d].real*a**r,vec[d].imag*b**r);assert p==expected
   assert max(map(abs,xs))<=k*(a**r-1)//(a-1)
   assert max(map(abs,ys))<=k*(b**r-1)//(b-1)
   letters+=len(w);checks+=1
  old=new;S=T[0]+T[1];D=T[1]-T[0]
note=P/'causal_reduction/matrix_candidates/halfturn_area_curvature_obstruction.md'
out={'status':'PASS independent directive curvature and prefix geometry controls','schedules':8,'levels':4,'word_checks':checks,'literal_letters':letters,'radix':k,'matrix':[a,b],'note_sha256':hashlib.sha256(note.read_bytes()).hexdigest(),'limits':'Finite controls supplement analytic all-level proof; no candidate is claimed legal.'}
(P/'audits/halfturn_curvature_independent.json').write_text(json.dumps(out,indent=2));print(json.dumps(out))
