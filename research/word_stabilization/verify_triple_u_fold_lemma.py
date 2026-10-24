"""Verify the finite footprint identities in the all-parameter proof.
The parameter argument is in triple_u_fold_lemma.md; the regression grid
at the end is additional checking, not a replacement for that argument.
"""
from verify_macro_word import D,check
from itertools import product
T={};ENDS={};DIR=((0,1),(1,0),(0,-1),(-1,0))
for k in 'UBQ':
 x=y=h=0;tr={}
 for phase,c in enumerate(D[k]['word']):
  tr.setdefault((x,y),[]).append((phase,c));h=(h+(1 if c=='R' else -1))%4;dx,dy=DIR[h];x+=dx;y+=dy
 T[k]=tr;ENDS[k]=(x,y,h)
assert ENDS=={'U':(0,4,0),'B':(-3,-5,2),'Q':(-4,-4,2)}
assert min(x for x,y in T['U'])==-1 and max(x for x,y in T['U'])==2
assert {y:v for (x,y),v in T['U'].items() if x==-1}=={0:[(1,'L')],-1:[(2,'L')],1:[(14,'L')],2:[(13,'L'),(21,'R')],3:[(22,'R')]}
assert T['U'][0,4]==[(24,'R')]
assert T['U'][0,3][0]==(23,'L')
assert max(y for x,y in T['U'])==4
firstL={p for p,reads in T['U'].items() if reads[0][1]=='L'}
assert len(firstL)==9
fresh={(-1,0),(-1,1),(-1,2),(0,2),(0,3)}
assert fresh<=firstL
assert all(y+4>max(yy for xx,yy in T['U'] if xx==x) for x,y in fresh)
assert all((x,y+4) in T['U'] for x,y in firstL-fresh)
assert {k:D[k]['word'].count('R')-D[k]['word'].count('L') for k in 'CUQB'}=={'C':3,'U':4,'Q':6,'B':6}
for k in 'BQ':
 assert T[k][-1,-1][-1]==(46,'R')
 assert T[k][-2,1][0]==(15,'R')
 assert T[k][-3,1][0]==(18,'L')
 assert min(y for x,y in T[k] if x==-1)==-1
assert T['Q'][-1,1][-1]==(30,'R')
assert T['B'][0,-1][-1]==(3,'L')
assert T['B'][-2,-3][-1]==(67,'R')
assert T['Q'][-3,-2][-1]==(57,'R')
assert min(y for x,y in T['B'])==-5 and min(y for x,y in T['Q'])==-4
assert (-3,-4) not in T['Q']
for w,phase in [('BB',68),('QQ',58),('QB',70)]:
 try:check(w)
 except AssertionError as err:
  bi,k,t,p,prev,c=err.args[0]
  assert bi==1 and t-len(D[w[0]]['word'])==phase and c==prev[1]=='R'
 else:raise AssertionError(w)
N=0
for a,f,d in product('BQ',repeat=3):
 for n in range(25):
  for m in range(25):
   try:check(a+'U'*n+f+'U'*m+d)
   except AssertionError:N+=1
   else:raise AssertionError((a,f,d,n,m))
for r in range(1,40):assert check('U'*r)['fuel']==4+5*r
print('All finite footprint identities verified;',N,'regression cases fail; U fuel verified for r<=39.')
