"""Finite controls for the no-ABA constraint, deliberately without physical colors."""
from pathlib import Path
from itertools import product
import json
R=Path('/workspace/shared/langton');D=json.loads((R/'continuation_2026-10-22/ant_continuation/factor_language/five_macro_footprints.json').read_text());dirs=((0,1),(1,0),(0,-1),(-1,0))
def push(st,a):
 st=list(st)
 if st and st[-1][0]==a:
  c=st.pop()[1]+1
  if c<4:st.append((a,c))
 else:st.append((a,1))
 return tuple(st)
def canon(st):
 st=list(st)
 while st and st[-1][1]==3:
  st.pop()
  if not st:return (('R',3),)
  a,e=st.pop()
  if e>1:st.append((a,e-1))
 return tuple(st)
def test(word):
 p=(0,0);h=0;g=();past={};last={};Vreuse=[];conflicts=[];t=0
 for mi,m in enumerate(word):
  start=p;sh=h;oldsites=set(past)
  for j,c in enumerate(D[m]['word']):
   a=canon(g)
   if p in past and past[p][-1]!=a:
    if a in past[p]:return None
    past[p].append(a)
   elif p not in past:past[p]=[a]
   if p in last and last[p][1]==c:conflicts.append((t,p,c,last[p]))
   if m=='V' and j==13 and p in oldsites:Vreuse.append((mi,t,p))
   last[p]=(t,c);g=push(g,c);h=(h+(1 if c=='R' else -1))%4;p=(p[0]+dirs[h][0],p[1]+dirs[h][1]);t+=1
 return Vreuse,conflicts
count=0
for k in range(9):
 for pre in product('CUVQB',repeat=k):
  w=''.join(pre)+'V';r=test(w);count+=1
  if r and r[0]:
   out=dict(status='no-ABA geometric witness, not physically feasible unless conflicts empty',word=w,reused_V_tips=r[0],same_letter_conflicts=r[1],tested_words=count)
   (R/'audits/macro_noaba_vreuse.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit
print('No witness in finite control',count)
