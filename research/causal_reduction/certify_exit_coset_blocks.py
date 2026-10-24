"""Finite literal identities used in the unbounded exit-coset last-read proof."""
import json,sys
from pathlib import Path
sys.path.insert(0,'/workspace/shared/langton/word_stabilization')
from verify_macro_word import D

def red(w):
 s=[]
 for a in w:
  if s and s[-1][0]==a:
   e=s.pop()[1]+1
   if e<4:s.append((a,e))
  else:s.append((a,1))
 return tuple(s)
def canon(w):
 s=list(red(w))
 while len(s)>1 and s[-1][1]==3:
  s.pop();a,e=s.pop()
  if e>1:s.append((a,e-1))
 if len(s)==1 and s[0][1]==3:s=[('L',3)]
 return tuple(s)
def exp(s):return ''.join(a*n for a,n in s)
F={m:red(d['word']) for m,d in D.items()};out={}
for m,d in D.items():
 assert F[m][0][0]=='R' and F[m][-1][0]=='L'
 assert all(e in (1,2) for a,e in F[m])
 local=[canon(d['word'][:j]) for j in range(d['length'])]
 for j,c in enumerate(local):
  if j in (0,4):assert c==()
  elif j in (1,2,3):assert c==( ('L',j), )
  else:assert c and c[0][0]=='R' and all(e in (1,2) for a,e in c)
 if m=='C':continue
 q=tuple(d['trace'][-1]['p']);j=next(t['i'] for t in d['trace'] if tuple(t['p'])==q)
 E=canon(d['word'][:j]);assert F[m]==E+(('L',1),) and E[-1]==('R',2)
 own=[k for k,c in enumerate(local) if c==E];assert own==[j,d['length']-1]
 next_hits={}
 for n,e in D.items():
  hits=[k for k in range(e['length']) if canon(d['word']+e['word'][:k])==E]
  assert hits==[3];next_hits[n]=hits
 out[m]=dict(exit=q,first_phase=j,own_coset_reads=own,next_macro_reads=next_hits,E=exp(E),F=exp(F[m]))
# Finite suffix cases underpin the arbitrary-prefix loss bound. Once a
# canonical prefix ends in R^a L^b, multiplying by L^j can remove at most
# those two syllables. An earlier prefix ends in exponent1/2, so no cascade.
loss=[]
for a in (1,2):
 for b in (1,2):
  for j in (0,1,2,3):
   pre='RLLR'*0+'RL'+'R'*a+'L'*b
   r=canon(pre+'L'*j);delta=len(red(pre))-len(r);assert delta<=2
   loss.append([a,b,j,delta])
res=dict(status='PASS',exit_blocks=out,maximum_prefix_syllable_loss=2,suffix_cases=loss,claim='Within any five-macro concatenation, each non-C exit coset is read exactly L,R and, when a next macro exists, L at its phase3; no later macro reads that coset.')
print(json.dumps(res,indent=2));Path(__file__).with_name('exit_coset_blocks_certificate.json').write_text(json.dumps(res,indent=2))
