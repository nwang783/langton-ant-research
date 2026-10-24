"""Prove symbolic exit-coset freshness for arbitrary five-macro concatenations.
Finite word-language check, not a bounded search in concatenation length.
"""
import json
from pathlib import Path
D=json.load(open('/workspace/shared/langton/continuation_2026-10-22/ant_continuation/factor_language/five_macro_footprints.json'))
def red(w):
 s=[]
 for a in w:
  if s and s[-1][0]==a:
   c=s.pop()[1]+1
   if c<4:s.append((a,c))
  else:s.append((a,1))
 return tuple(s)
def expand(s):return ''.join(a*n for a,n in s)
def canon(w):
 # Exact finite minimization in wH: h^k has 2|k| syllables; once |k|
 # exceeds len(red(w))+1, cancellation cannot beat the identity candidate.
 n=len(red(w));out=[]
 for k in range(-n-1,n+2):
  t=red(w+('RLLL'*k if k>=0 else 'LRRR'*(-k)));out.append(t)
 return min(out,key=lambda x:(len(x),x))
F={k:red(v['word']) for k,v in D.items()}; E={}
for k,v in D.items():
 assert F[k][0][0]=='R' and F[k][-1][0]=='L'
 assert all(n in (1,2) for a,n in F[k])
 if k=='C':continue
 q=v['trace'][-1]['p'];j=next(i for i,r in enumerate(v['trace']) if r['p']==q)
 assert v['word'][j]=='L' and v['word'][-1]=='R'
 E[k]=canon(v['word'][:j]);assert all(n in (1,2) for a,n in E[k])
 assert E[k][0][0]=='R'

checks=[]
for a,va in D.items():
 old={canon(va['word'][:j]) for j in range(len(va['word']))}
 # The whole candidate F_a F_w E_t is already a canonical S word.
 # Any matching old coset therefore has this exact syllable representative.
 for t,e in E.items():
  stack=[(F[a],'')];count=0;bound=max(map(len,old));matches=[]
  while stack:
   p,w=stack.pop();count+=1
   z=p+e
   if z in old:matches.append(a+w+t)
   for k,f in F.items():
    if len(p)+len(f)+len(e)<=bound:stack.append((p+f,w+k))
  assert not matches,(a,t,matches)
  checks.append({'earlier_macro':a,'exit_macro':t,'canonical_read_bound':bound,'candidate_prefixes_checked':count})
out={'status':'PASS','macro_reductions':{k:expand(v) for k,v in F.items()},'exit_cosets':{k:expand(v) for k,v in E.items()},'finite_language_checks':checks,'claim':'Every non-C exit cell is read in a coset not visited in any earlier macro of the concatenation. This is symbolic freshness only, not physical-cell freshness.'}
print(json.dumps(out,indent=2));Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
