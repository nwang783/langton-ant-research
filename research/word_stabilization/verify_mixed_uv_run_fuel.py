from itertools import product
from collections import Counter
from verify_macro_word import D,check
for k,want in [('U',{(-1,0):-1,(0,-1):-1,(1,2):1,(2,1):1}),('V',{(-1,0):-1,(0,-1):-1,(2,1):1})]:
 delta=Counter()
 for z in D[k]['trace']:
  p=tuple(z['p'])
  if sum(p)%4==3:delta[p]+=1 if z['c']=='R' else -1
 assert {p:n for p,n in delta.items() if n}==want
for a,b in product('UV',repeat=2):
 r=check(a+b);fresh=set(map(tuple,r['blocks'][1]['new_fuel']));px,py,h=r['blocks'][1]['pose'];assert h==0
 fresh={(x-px,y-py) for x,y in fresh}
 assert fresh==({(-1,0),(-1,1),(-1,2),(0,2),(0,3)} if b=='U' else {(-1,0),(1,2)})
count=0
for n in range(1,11):
 for a in product('UV',repeat=n):
  w=''.join(a);r=check(w);assert r['fuel']==4+5*w.count('U')+2*w.count('V');count+=1
print('Exact pair and residue-flux facts passed; finite mixed-run controls:',count)
