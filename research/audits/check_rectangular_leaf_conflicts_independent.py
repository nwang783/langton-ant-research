from pathlib import Path
import json,hashlib
P=Path(__file__).resolve().parents[1];source=P/'causal_reduction/matrix_candidates/rectangular_all_direction_images_k17.leaves.json';records=json.loads(source.read_text())
def key(r):return (r['heading'],*r['images'])
author={key(r):r for r in records};assert len(author)==len(records)==3572
independent=[]
for line in (P/'audits/rectangular_independent_leaves.txt').read_text().splitlines():
 h,*words=line.split();independent.append((int(h),*words))
assert len(set(independent))==len(independent) and set(independent)==set(author)
dirs=[1j,1,-1j,-1];latest=0
for r in records:
 words=[tuple(map(int,w))for w in r['images']];stack=[(1,4)];p=0j;h=dirs[r['heading']];colors={};last={};found=False
 for t in range(10000):
  while stack[-1][1]:
   z,d=stack.pop();stack.extend((a,d-1)for a in reversed(words[z]))
  z,d=stack.pop();assert not d;move=dirs[z];assert move/h in (1j,-1j);bit=move==h*1j
  if p in colors and colors[p]!=bit:
   actual=(t,last[p],[int(p.real),int(p.imag)],3 if bit else 1)
   expected=(r['time'],r['previous'],r['cell'],r['turn']);assert actual==expected,(key(r),actual,expected);latest=max(latest,t);found=True;break
  colors[p]=not bit;last[p]=t;p+=move;h=move
 assert found
files=['causal_reduction/matrix_candidates/rectangular_all_direction_images_k17.leaves.json','causal_reduction/matrix_candidates/rectangular_k17_full_domains.txt','audits/check_rectangular_independent_images.cpp','audits/rectangular_independent_leaves.txt','causal_reduction/matrix_candidates/README.md']
out={'status':'PASS complete independent inventory, leaf set and literal first-conflict replay','enumeration':json.loads((P/'audits/rectangular_independent_enumeration.json').read_text()),'matched_records':len(records),'latest_conflict':latest,'sha256':{f:hashlib.sha256((P/f).read_bytes()).hexdigest()for f in files}}
(P/'audits/rectangular_independent_complete.json').write_text(json.dumps(out,indent=2));print(json.dumps(out))
