"""Exact macro syllable bounds, using direct canonicalization rather than H search."""
import json
from pathlib import Path
R=Path('/workspace/shared/langton');D=json.loads((R/'continuation_2026-10-22/ant_continuation/factor_language/five_macro_footprints.json').read_text())
def red(w):
 st=[]
 for a in w:
  if st and st[-1][0]==a:
   e=st.pop()[1]+1
   if e<4:st.append((a,e))
  else:st.append((a,1))
 return tuple(st)
def canon(w):
 st=list(red(w))
 while st and st[-1][1]==3:
  st.pop()
  if not st:return (('R',3),)
  a,e=st.pop()
  if e>1:st.append((a,e-1))
 return tuple(st)
rows={};exits={}
for k,d in D.items():
 f=red(d['word']);assert f[0][0]=='R' and f[-1][0]=='L' and all(e<=2 for _,e in f)
 old=[canon(d['word'][:j]) for j in range(len(d['word']))]
 assert max(map(len,old))==len(f)+1
 rows[k]=dict(reduced_syllables=len(f),maximum_read_coset_syllables=max(map(len,old)))
 if k!='C':
  p=d['trace'][-1]['p'];j=next(z['i'] for z in d['trace'] if z['p']==p);e=canon(d['word'][:j])
  assert e[0][0]=='R' and all(n<=2 for _,n in e) and len(e)>=3
  exits[k]=dict(first_exit_phase=j,canonical_syllables=len(e))
# Every product F_a F_w E_t is S-canonical and has depth>=len(F_a)+3,
# greater than the earlier macro's maximum len(F_a)+1. Left cancellation
# of the common prior group prefix proves freshness for arbitrary lengths.
w=json.loads((R/'audits/v_reused_arbitrary_prefix.json').read_text());whole=w['whole_word'];start=tuple(w['start_pose'][0]);h=w['start_pose'][1];dirs=((0,1),(1,0),(0,-1),(-1,0));p=start;last={};blocks={};seen={};tips=[]
for t,c in enumerate(whole):
 a=canon(whole[:t]);b=c=='L'
 if p in last:assert last[p][1]!=b
 last[p]=(a,b)
 if p not in blocks:blocks[p]=[]
 if not blocks[p] or blocks[p][-1]!=a:
  assert a not in blocks[p],('ABA',t,p,a);blocks[p].append(a)
 if p==tuple(w['target']):tips.append(dict(t=t,letter=c,coset=a))
 h=(h+(1 if c=='R' else -1))%4;p=(p[0]+dirs[h][0],p[1]+dirs[h][1])
assert tips[0]['coset']!=tips[1]['coset']==tips[2]['coset']
out=dict(status='PASS',macro_bounds=rows,exit_bounds=exits,physical_reuse_control=tips,scope='Symbolic exit freshness holds for all five-macro words. The reuse control has an arbitrary non-macro prefix and is not a five-macro counterexample.')
(R/'audits/symbolic_exit_freshness.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
