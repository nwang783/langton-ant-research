"""Algebraic all-f one-use endpoint domains; finite controls only verify
the closed-form formulas, not infer them from a multiplicity cutoff.
"""
from pathlib import Path
import json
H='NESW'
def out(h,r):return H[(H.index(h[r])+(1 if r%2==0 else-1))%4]
def count(h,d,k):return sum((x if k=='in'else out(h,r))==d for r,x in enumerate(h))
rows=[]
for f in [1,2,3,4,7,13]:
 sources=['E']if f==1 else['E'+'W'*(2*f-3),'E'+'W'*(2*f-2)]
 sinks=['E']if f==1 else['EE'+'WE'*(f-2),'EE'+'WE'*(f-2)+'W']
 for side,words in [('source',sources),('sink',sinks)]:
  for h in words:
   fi,fo=count(h,'E','in'),count(h,'S','out')
   assert(fi,fo)==((1,f)if side=='source'else(f,1))
   bal=sum(x=='E'for r,x in enumerate(h)if r%2==0)-sum(x=='W'for r,x in enumerate(h)if r%2==0)
   assert bal==(3-f if len(h)%2==0 else 2-f)
   rows.append(dict(f=f,type=side,word=h,flows=[fi,fo],R_balance=bal,length=len(h)))
for h in ['WWE','WWEW']:assert count(h,'E','in')==count(h,'N','out')==1
Path(__file__).with_suffix('.json').write_text(json.dumps(dict(scope=__doc__,all_f_proof='Ein1 makes all postR0 W; Sout1 makes allL E and postR0 R W. CountingL gives floor(n/2)=f-1.',formula_controls=rows,LEFT_flow1_words=['WWE','WWEW'],warning='No all-cap firstR maximum or cycle height constancy claimed; stream sign is an independent premise.'),indent=2)+'\n');print('PASS exact formulasallf, rotationsimplicit; controls only')
