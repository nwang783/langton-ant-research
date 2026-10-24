from pathlib import Path
import json,hashlib
P=Path(__file__).resolve().parents[1];src=P/'recovered_bundle/ant_global/root/standard.json';data=json.loads(src.read_text());word=data['word'];q=[];z=0j;h=1j
for c in word:q.append(z);h*=(-1j if c=='R' else 1j);z+=h
D=z;assert h==1j and D!=0;period=len(word)
def divdelta(z):
 k=z/D
 return int(k.real) if k.imag==0 and k.real==int(k.real) else None
classes=[];used=set()
for i,u in enumerate(q):
 if i in used:continue
 C=[]
 for j,v in enumerate(q):
  shift=divdelta(v-u)
  if shift is not None:C.append((j,shift));used.add(j)
 classes.append((u,C))
firstL=[];edgechecks=0
for u,C in classes:
 lo=min(s for j,s in C);hi=max(s for j,s in C)
 for r in range(lo,hi+1):
  visits=sorted((period*(r-s)+j,word[j])for j,s in C if r>=s)
  assert visits
  for a,b in zip(visits,visits[1:]):assert a[1]!=b[1];edgechecks+=1
  if visits[0][1]=='L':firstL.append((visits[0][0],u+r*D))
 # All larger translate cells have this same complete order and must start R.
 assert visits[0][1]=='R'
assert len({v for t,v in firstL})==len(firstL)
firstL.sort();times=[t for t,z in firstL];seed=sorted((int(z.real),int(z.imag))for t,z in firstL)
expected=sorted((y,-x)for x,y in data['seed']);assert seed==expected
reported=json.loads((P/'computability/check_matrix_standard_positive.json').read_text());assert reported['first_L_times']==times and sorted(map(tuple,reported['minimal_seed']))==seed
# Separate recurrence derivation and literal point checks.
def point(n):return (n//period)*D+q[n%period]
checks=0
for n in range(8192):
 for digit in [0,1]:
  s=n%period;r=(2*s+digit)%period;offset=((2*s+digit)//period)*D+q[r]-2*q[s]
  assert point(2*n+digit)==2*point(n)+offset;checks+=1
out={'status':'PASS independent exact periodic all-time first-L and alternation control','period':period,'drift':[int(D.real),int(D.imag)],'translation_classes':len(classes),'finite_boundary_alternation_checks':edgechecks,'first_L_times':times,'minimal_seed':seed,'matrix_recurrence_checks':checks,'reported_acceptance':'matches the separate matrix-automata positive output; this control does not reimplement its automata minimization','source_sha256':hashlib.sha256(src.read_bytes()).hexdigest()}
(P/'audits/standard_matrix_positive_independent.json').write_text(json.dumps(out,indent=2));print(json.dumps(out))
