from collections import defaultdict
from verify_macro_word import D
import sympy as s
A,B=s.symbols('A B')
M={}
for k in 'UV':
 v=[defaultdict(int) for _ in range(4)]
 for z in D[k]['trace']:
  x,y=z['p'];t=(y-3*x)%4;b=(y-3*x-t)//4;v[t][x,b]+=1 if z['c']=='R' else -1
 M[k]=[s.expand(sum(n*A**a*B**b for (a,b),n in d.items())) for d in v]
 print(k)
 for i,p in enumerate(M[k]):print(i,s.factor(p))
print('Curl of UV minus VU:')
for i in range(4):
 p=s.expand((1-A)*M['U'][i]-(1-B)*M['V'][i]);print(i,s.factor(p))
