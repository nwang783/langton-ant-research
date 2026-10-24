"""Finite ingredients plus finite controls for the analytic balanced-run proof."""
from itertools import product
from verify_macro_word import D,check

def at(k,p):return [(z['i'],z['c']) for z in D[k]['trace'] if tuple(z['p'])==p]
for k,p,read in [('U',(-1,3),(22,'R')),('U',(0,4),(24,'R')),('V',(0,2),(12,'R')),('V',(1,3),(14,'R'))]:assert at(k,p)==[read]
assert not at('U',(-1,4)) and not at('V',(0,3))
assert D['U']['end_pose']==[0,4,0] and D['V']['end_pose']==[1,3,0]
for k,cap in [('U',4),('V',3)]:
 assert min(z['p'][0] for z in D[k]['trace'])==-1
 assert max(z['p'][1] for z in D[k]['trace'])==cap
for k in 'BQ':assert at(k,(-1,-1))[-1]==(46,'R')
assert at('Q',(-1,1))[-1]==(30,'R')
assert at('B',(0,-1))[-1]==(3,'L')
assert not at('Q',(-3,-4))
for k in D:assert at(k,(-1,0))[0]==(1,'L')
for k,y in [('B',-5),('Q',-4)]:assert min(z['p'][1] for z in D[k]['trace'])==y
for w in ['BB','QQ','QB']:
 try:check(w)
 except AssertionError:pass
 else:raise AssertionError(('Unexpected feasible seam',w))
# Independently derive the selected equal-read witnesses by literal motion.
def trace(w):
 p=(0,0);h=0;dirs=((0,1),(1,0),(0,-1),(-1,0));out=[]
 for j,k in enumerate(w):
  for phase,c in enumerate(D[k]['word']):
   out.append((p,c,j,k,phase));h=(h+(1 if c=='R' else -1))%4;dx,dy=dirs[h];p=p[0]+dx,p[1]+dy
 return out
count=0
for n in range(6):
 words=[''.join(w) for w in product('UV',repeat=n)]
 for X in words:
  for Y in words:
   if X.count('U')!=Y.count('U'):continue
   for A,F in product('BQ',repeat=2):
    q=(-1,-1) if A==F else ((-1,1) if A=='Q' else (0,-1))
    for end in 'CUVQB':
     w=A+X+F+Y+end;r=[z for z in trace(w) if z[0]==q]
     assert any(a[1]==b[1] for a,b in zip(r,r[1:])),(w,q,r)
     count+=1
print('Finite footprint identities passed; balanced controls:',count)
r=check('QUUUUQVVVQ');assert r['fuel']==75
print('Mixed unbalanced negative control passed:',r['word'],r['fuel'])
