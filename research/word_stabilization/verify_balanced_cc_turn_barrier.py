"""Finite ingredients for the all-length geometry in balanced_cc_turn_barrier.md."""
from itertools import product
from verify_macro_word import D,check
for a in 'UV':
 t=D[a]['trace'];assert min(z['p'][1]for z in t)==-1
 assert max(z['p'][1]for z in t)==D[a]['end_pose'][1]
 assert [(z['i'],z['c'])for z in t if z['p']==[0,0]]==[(0,'L'),(4,'R')]
 assert [(z['i'],z['c'])for z in t if z['p']==[0,1]][-1]==(19 if a=='U' else 11,'R')
assert [-1,4]not in[z['p']for z in D['U']['trace']]
assert [0,3]not in[z['p']for z in D['V']['trace']]
assert min(z['p'][0]for z in D['C']['trace'])==-1
assert min(z['p'][1]for z in D['C']['trace'])==-1
assert [-1,1]not in[z['p']for z in D['C']['trace']]
assert [(z['i'],z['c'])for z in D['C']['trace']if z['p']==[-1,0]]==[(1,'L')]
for a in 'CUVQB':
 reads=[(z['i'],z['c'])for z in D[a]['trace']if z['p']==[0,1]]
 assert reads[0]==(11,'R')
assert D['C']['end_pose']==[0,1,3]
for w in ['VCCVC','VVCCVVC']:
 check(w)
 for a in 'CUVQB':
  try:check(w+a)
  except AssertionError:pass
  else:raise AssertionError(w+a)
controls=0
for n in range(1,6):
 words=[''.join(t)for t in product('UV',repeat=n)]
 for x in words:
  for y in words:
   if x.count('U')!=y.count('U'):continue
   for a in 'CUVQB':
    try:check(x+'CC'+y+'C'+a)
    except AssertionError:pass
    else:raise AssertionError((x,y,a))
    controls+=1
print('Finite footprint ingredients passed; additional regressions:',controls)
