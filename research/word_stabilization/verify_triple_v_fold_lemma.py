"""Exact finite ingredients of the all-parameter triple-V-fold proof.
The analytic parameter exhaustion is in triple_v_fold_lemma.md.
"""
import json,hashlib
from pathlib import Path
from itertools import product
SOURCE=Path('/workspace/shared/langton/continuation_2026-10-22/ant_continuation/factor_language/five_macro_footprints.json')
D=json.loads(SOURCE.read_text());VECT=((0,1),(1,0),(0,-1),(-1,0));T={};ENDS={}
for k in 'VBQ':
 x=y=h=0;tr={}
 for i,c in enumerate(D[k]['word']):
  tr.setdefault((x,y),[]).append((i,c));assert D[k]['trace'][i]['p']==[x,y] and D[k]['trace'][i]['c']==c
  h=(h+(1 if c=='R' else -1))%4;dx,dy=VECT[h];x+=dx;y+=dy
 T[k]=tr;ENDS[k]=(x,y,h)
assert ENDS=={'V':(1,3,0),'B':(-3,-5,2),'Q':(-4,-4,2)}
assert (min(x for x,y in T['V']),max(x for x,y in T['V']),min(y for x,y in T['V']),max(y for x,y in T['V']))==(-1,2,-1,3)
assert T['V'][-1,0]==[(1,'L')] and T['V'][0,2]==[(12,'R')] and (0,3) not in T['V']
# Every possible integer d comes from d=x+3 for some finite footprint point.
assert [(x+3,rs) for (x,y),rs in T['V'].items() if y==3*(x+3)-6]==[(2,[(1,'L')])]
for k in 'BQ':
 assert T[k][-1,2][0]==(13,'L') and T[k][-2,1][0]==(15,'R') and T[k][-1,0][0]==(1,'L')
assert T['B'][-2,-3][-1]==(67,'R') and T['B'][0,-1][-1]==(3,'L')
assert T['Q'][-3,-2][-1]==(57,'R') and T['Q'][-1,-1][-1]==(46,'R')
assert min(y for x,y in T['Q'])==-4 and (-3,-4) not in T['Q']
def conflict(w):
 x=y=h=0;last={}
 for t,c in enumerate(''.join(D[k]['word'] for k in w)):
  if (x,y) in last and last[x,y][1]==c:return (t,(x,y),last[x,y],c)
  last[x,y]=(t,c);h=(h+(1 if c=='R' else -1))%4;dx,dy=VECT[h];x+=dx;y+=dy
 return None
assert {w:conflict(w) for w in ('VB','BB','QB','QQ')}=={
 'VB':(77,(-1,0),(1,'L'),'L'),'BB':(142,(-1,-1),(46,'R'),'R'),
 'QB':(134,(-1,1),(30,'R'),'R'),'QQ':(122,(-1,-1),(46,'R'),'R')}
firstL={p for p,rs in T['V'].items() if rs[0][1]=='L'}
assert len(firstL)==6
fresh={(-1,0),(1,2)}
assert fresh<=firstL
assert all((x+1,y+3) not in T['V'] for x,y in fresh)
assert all(y+6>max(yy for xx,yy in T['V']) for x,y in fresh)
assert all((x+1,y+3) in T['V'] for x,y in firstL-fresh)
assert {k:D[k]['word'].count('R')-D[k]['word'].count('L') for k in 'VQB'}=={'V':4,'Q':6,'B':6}
N=0
for a,f,d in product('BQ',repeat=3):
 for n in range(20):
  for m in range(20):assert conflict(a+'V'*n+f+'V'*m+d);N+=1
out={'status':'PASS','source_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),'finite_footprint_facts':'all asserted','additional_parameter_regression_cases':N,'scope':'All-parameter proof is the explicit no-intervening-read case exhaustion, not the finite regression grid.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
