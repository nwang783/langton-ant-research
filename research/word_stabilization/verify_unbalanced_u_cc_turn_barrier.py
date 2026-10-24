from verify_macro_word import D,check
assert D['V']['end_pose']==[1,3,0]
assert min(z['p'][1]for z in D['V']['trace'])==-1
assert max(z['p'][1]for z in D['V']['trace'])==3
assert not{(-1,4),(-1,3),(0,3)}&{tuple(z['p'])for z in D['V']['trace']}
assert min(z['p'][1]for z in D['C']['trace'])==-1
assert min(z['p'][0]for z in D['C']['trace'])==-1
for p,i,c in [((0,1),19,'R'),((0,2),20,'L'),((-1,2),21,'R')]:
 zs=[z for z in D['U']['trace']if tuple(z['p'])==p]
 assert (zs[-1]['i'],zs[-1]['c'])==(i,c)
for a in'CUVQB':
 i=12 if a in'CV'else 13;p=(0,2)if a in'CV'else(-1,2);c='R'if a in'CV'else'L'
 z=D[a]['trace'][i];assert tuple(z['p'])==p and z['c']==c
 assert not any(tuple(t['p'])==p for t in D[a]['trace'][:i])
for k in range(100):
 w='U'+'V'*k+'CC'+'V'*(k+1)+'C'
 check(w)
 for a in'CUVQB':
  try:check(w+a)
  except AssertionError:pass
  else:raise AssertionError(w+a)
print('Finite ingredients and 600 extra literal controls passed.')
