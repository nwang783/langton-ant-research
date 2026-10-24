"""Exhaustive literal check of short necessary macro-gap grammar.
This does not assert that every word allowed by the grammar is physically feasible.
"""
from verify_macro_word import check
import json
result={'gaps':{},'initial_C_runs':{},'terminal_C_runs':{}}
for a in 'UVQB':
 for b in 'UVQB':
  valid=[];conflicts={}
  for k in range(4):
   word=a+'C'*k+b
   try:check(word);valid.append(k)
   except AssertionError as e:conflicts[k]=e.args
  result['gaps'][a+b]={'allowed_k':valid,'conflicts':conflicts}
for b in 'UVQB':
 valid=[];conflicts={}
 for k in range(5):
  try:check('C'*k+b);valid.append(k)
  except AssertionError as e:conflicts[k]=e.args
 result['initial_C_runs'][b]={'allowed_k':valid,'conflicts':conflicts}
for a in 'UVQB':
 valid=[];conflicts={}
 for k in range(5):
  try:check(a+'C'*k);valid.append(k)
  except AssertionError as e:conflicts[k]=e.args
 result['terminal_C_runs'][a]={'allowed_k':valid,'conflicts':conflicts}
check('CCCC')
try:
 check('CCCCC')
except AssertionError as e:
 result['C5_conflict']=e.args
else:
 raise RuntimeError('C^5 unexpectedly passed physical replay')
expected={'UU':[0],'UV':[0,1,2],'UQ':[0],'UB':[0], 'VU':[0],'VV':[0,1,2],'VQ':[0],'VB':[], 'QU':[0],'QV':[0,1,2],'QQ':[],'QB':[], 'BU':[0],'BV':[0,1,2],'BQ':[0],'BB':[]}
assert {k:v['allowed_k'] for k,v in result['gaps'].items()}==expected
assert {k:v['allowed_k'] for k,v in result['initial_C_runs'].items()}=={'U':[0],'V':[0,1,2,3],'Q':[0,1],'B':[0,1]}
assert all(v['allowed_k']==[0,1,2,3] for v in result['terminal_C_runs'].values())
print(json.dumps({k:v['allowed_k'] for k,v in result['gaps'].items()}))
with open('/workspace/shared/langton/word_stabilization/macro_gap_certificate.json','w') as f:json.dump(result,f,indent=2)
