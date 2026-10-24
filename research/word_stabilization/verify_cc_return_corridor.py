from verify_macro_word import D,check
for a in'UQB':
 assert D[a]['trace'][12]['p']==[0,2] and D[a]['trace'][12]['c']=='L'
 assert D[a]['trace'][13]['p']==[-1,2] and D[a]['trace'][13]['c']=='L'
 assert not any(z['p']==[0,2]for z in D[a]['trace'][:12])
 assert not any(z['p']==[-1,2]for z in D[a]['trace'][:13])
assert [(z['i'],z['c'])for z in D['V']['trace']if z['p']==[-1,-1]]==[(2,'L')]
assert [(z['i'],z['c'])for z in D['U']['trace']if z['p']==[-1,0]]==[(1,'L')]
for n in range(1,101):
 for w in ['V'*n+'CC'+'V'*n, 'U'+'V'*(n-1)+'CC'+'V'*n]:
  check(w+'V')
  for a in'UQB':
   try:check(w+a)
   except AssertionError:pass
   else:raise AssertionError(w+a)
print('Finite ingredients and 800 extra literal controls passed.')
