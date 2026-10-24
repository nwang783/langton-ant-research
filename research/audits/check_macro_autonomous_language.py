"""Finite adjacency tests for a proposed exact autonomous-language theorem."""
from pathlib import Path
from itertools import product
import json
R=Path('/workspace/shared/langton');D=json.loads((R/'continuation_2026-10-22/ant_continuation/factor_language/five_macro_footprints.json').read_text())
def red(w):
 s=[]
 for a in w:
  if s and s[-1][0]==a:
   n=s.pop()[1]+1
   if n<4:s.append((a,n))
  else:s.append((a,1))
 return tuple(s)
def canonical(s):
 s=list(s)
 while s and s[-1][1]==3:
  s.pop()
  if not s:return (('R',3),)
  a,n=s.pop()
  if n>1:s.append((a,n-1))
 return tuple(s)
def check(macros):
 w=''.join(D[m]['word'] for m in macros);last={}
 for t,c in enumerate(w):
  q=canonical(red(w[:t]))
  if q in last and last[q][1]==c:return dict(time=t,old=last[q],coset=q,letter=c)
  last[q]=(t,c)
 return None
facts={}
for name,d in D.items():
 f=red(d['word']);assert f and f[0][0]=='R' and f[-1][0]=='L' and all(e in (1,2) for _,e in f)
 reads=[canonical(red(d['word'][:j])) for j in range(len(d['word']))]
 assert max(map(len,reads))==len(f)+1
 kinds=[]
 for q in reads:
  if q in ((),(('L',1),),(('L',2),),(('R',3),)):continue
  assert q[0][0]=='R' and all(e in (1,2) for _,e in q), (name,q)
 facts[name]=dict(endpoint_syllables=len(f),max_read_syllables=max(map(len,reads)))
assert {k:v['endpoint_syllables'] for k,v in facts.items()}=={'C':2,'V':4,'U':6,'Q':16,'B':18}
bad=[]
for n in (1,2):
 for ww in product('CUVQB',repeat=n):
  w=''.join(ww);z=check(w)
  if z:bad.append((w,z))
for a,b in product('CUVQB',repeat=2):
 w=a+'C'+b;z=check(w)
 if z:bad.append((w,z))
assert not bad
out=dict(status='PASS: exact finite ingredients for all-length theorem',bad=bad,tests=55,local_normal_form_facts=facts)
print(json.dumps(out,indent=2))
(R/'audits/macro_autonomous_language.json').write_text(json.dumps(out,indent=2)+'\n')
