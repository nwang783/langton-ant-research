"""Direct letter/last-read reconstruction, with no guarded-mask composition."""
from itertools import product
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[1]
P=ROOT/'periodic_classification_new/four_eight_unit_returns.certificate.json';J=json.loads(P.read_bytes())
def walk(word,h=1j,last=None):
 p=0j;last={}if last is None else dict(last);trace=[];conflict=None;ret=[]
 for t,c in enumerate(word):
  trace.append((p,h,c))
  if p in last and last[p]==c:conflict=(p,t);break
  last[p]=c;h*=(-1j if c=='R'else 1j);p+=h
  if p==0:ret.append(t+1)
 return p,h,last,trace,conflict,ret
programs=[]
for h in (1j,-1j):
 for size in (4,8):
  for letters in product('RL',repeat=size):
   word=''.join(letters);p,end,last,trace,bad,ret=walk(word,h)
   if bad is None and ret==[size]:programs.append((h,end,word,trace))
author={(1j*(-1j)**a['h0'],1j*(-1j)**a['h1'],a['word'])for a in J['programs']}
assert {(h,end,w)for h,end,w,_ in programs}==author
positions={p for h,end,w,trace in programs for p,heading,c in trace};assert len(positions)==21
assert positions=={complex(*p)for p in J['positions']}
levels=[[(1j,{},(),0)]];bad5=[]
for depth in range(1,6):
 nxt=[]
 for h,last,path,cost in levels[-1]:
  for start,end,w,trace in programs:
   if start!=h:continue
   p,h1,after,tr,bad,ret=walk(w,h,last)
   if bad is not None:
    if depth==5:bad5.append((path,w,bad[0]))
    continue
   assert p==0 and h1==end and ret==[len(w)]
   nxt.append((h1,after,path+(w,),cost+len(w)))
 levels.append(nxt)
 assert {path for h,last,path,cost in nxt}=={tuple(J['programs'][i]['word']for i in s['path'])for s in J['compatible_prefixes'][depth]}
assert list(map(len,levels))==[1,12,42,48,16,0]
assert [min([z[3]for z in lev],default=None)for lev in levels]==[0,4,8,12,20,None]
assert len(bad5)==192
# Check every supplied failure cell against a complete literal concatenation.
for rec in J['fifth_step_conflicts']:
 s=J['compatible_prefixes'][4][rec['parent']];words=[J['programs'][i]['word']for i in s['path']]+[J['programs'][rec['program']]['word']]
 word=''.join(words);p,h,last,trace,bad,ret=walk(word)
 assert bad is not None
 q=complex(*J['positions'][rec['conflict_cell']]);turns=[c for p,h,c in trace if p==q]
 # The producer may choose a conflict after the direct replay's first one:
 p=0j;h=1j;turns=[]
 for c in word:
  if p==q:turns.append(c)
  h*=(-1j if c=='R'else 1j);p+=h
 assert any(a==b for a,b in zip(turns,turns[1:]))
# Exact rational scalar inequalities used by the block density deduction.
from fractions import Fraction
for D in range(2,101):
 c=min(Fraction(6),3+Fraction(D,2));F=[0,4,8,12,20]
 assert all(F[q]-c*q>=12-3*c for q in range(5))
 assert 12-4*c+2*D>=0 and 24-4*c>=0
out=dict(status='PASS independent direct literal four/eight-return chronology',programs=len(programs),physical_read_positions=len(positions),prefix_counts=list(map(len,levels)),fifth_conflicts=len(bad5),minimum_costs=[min([z[3]for z in lev],default=None)for lev in levels],certificate_sha256=hashlib.sha256(P.read_bytes()).hexdigest(),scope='Arbitrary-input local first returns; analytic block summation gives all-n density. White axis-four period36 additionally depends on signed KR cap5 and LC packing. No full front exclusion.')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
