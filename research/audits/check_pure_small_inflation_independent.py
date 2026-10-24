"""Independent literal geometry for pure, arbitrary-choice inflation k<=6."""
from itertools import product
import json
from pathlib import Path
OUT=Path(__file__).with_suffix('.json')
def trace(w):
 p=0j;h=1j;last={}
 for t,c in enumerate(w):
  if p in last and last[p][1]==c:return None,{'cell':[int(p.real),int(p.imag)],'earlier':last[p][0],'later':t,'turn':c}
  last[p]=(t,c);h*=(-1j if c=='R' else 1j);p+=h
 return (p,h),None
rows=[]
for k in [3,5]:
 R={};L={}
 for letters in product('RL',repeat=k):
  w=''.join(letters);e,fail=trace(w)
  if fail:continue
  p,h=e
  if h==1:R.setdefault(p,[]).append(w)
  if h==-1:L.setdefault(-p,[]).append(w)
 scales=sorted((a for a in R.keys()&L.keys() if abs(a)**2>1),key=lambda a:(a.real,a.imag))
 expected={3:{2-1j,2+1j},5:{-1-2j,-1+2j,1-2j,1+2j,3-2j,3+0j,3+2j}}[k]
 assert set(scales)==expected
 for a in scales:
  if k==5 and a==-1+2j:
   assert R[a]==['LRLRR'] and L[a]==['RRLRR'];kind='first-turn contradiction'
  elif k==5 and a==1+2j:
   assert set(R[a])=={'RLLRR','LRRLR'} and set(L[a])=={'RRRLR','LLLRR'}
   failures=[]
   for first in ['RLLRR','LLLRR']:
    assert first[1]=='L'
    for second in L[a]:
     e,f=trace(first+second);assert f and f['later']<=8
     failures.append({'word':first+second,**f})
   kind='two-macro chronology contradiction'
  else:
   assert all(w.count('R')-w.count('L')<=1 for w in R[a])
   assert all(w.count('R')-w.count('L')<=-1 for w in L[a])
   kind='nonincreasing scale mass'
  row={'k':k,'a':[int(a.real),int(a.imag)],'R':R[a],'L':L[a],'exclusion':kind}
  if kind=='two-macro chronology contradiction':row['conflicts']=failures
  rows.append(row)
report={'status':'passed','rows':rows,'scope':'Pure position AND heading inflation for every n, arbitrary occurrence-dependent images, expanding Gaussian scale; k2..6 excluded by these odd cases and heading parity.'}
OUT.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
