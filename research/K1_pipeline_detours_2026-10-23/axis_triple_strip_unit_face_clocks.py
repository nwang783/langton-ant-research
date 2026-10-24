"""Eight complete axis-strip G3 profiles and their two literal unit-sheet faces.
Fixed local clocks only; no front, period or drift search.
"""
from pathlib import Path
import json
H='NESW';prof={'Z+':'SSNS','Z-':'NSSS','A+':'EEEW','A-':'EWEE','B+':'SSSN','B-':'SNSS','Y+':'WWEW','Y-':'EWWW'}
portC_EW={'E':'SW','W':'NE','N':'NE','S':'SW'}
portC_NS={'N':'SE','S':'NW','E':'SE','W':'NW'}
def output(h,r):return H[(H.index(h[r])+(1 if r%2==0 else-1))%4]
def faceheights(h):
 if h[0]in'EW':
  rE=sum(x=='E'for x in h[::2]);rW=2-rE;lE=sum(x=='E'for x in h[1::2]);lW=2-lE;a=-max(rE,rW)
  return dict(NE=a+rW,SW=a+rE,NW=a-lE,SE=a-lW),portC_EW
 rN=sum(x=='N'for x in h[::2]);rS=2-rN;lN=sum(x=='N'for x in h[1::2]);lS=2-lN;a=-max(rN,rS)
 return dict(SE=a+rN,NW=a+rS,SW=a-lN,NE=a-lS),portC_NS
# Incoming movement direction, outgoing movement direction for F=C strip, Q=L strip.
faces={'C':{'Z':('N','E'),'A':('E','S'),'B':('S','W'),'Y':('W','N')},'L':{'Z':('S','E'),'A':('E','N'),'B':('N','W'),'Y':('W','S')}}
rows=[]
for name,h in prof.items():
 level,pc=faceheights(h);outs=[output(h,r)for r in range(4)]
 labelsin={};labelsout={}
 for r,x in enumerate(h):labelsin[r]=level[pc[x]]-sum(y==x for y in h[:r])+0
 for r,x in enumerate(outs):labelsout[r]=level[pc[x]]-sum(y==x for y in outs[:r])+0
 # Labels = h(C)-ordinal+1, so first occurrence is exactly h(C).
 for r in range(4):
  rr=3-r if r in(1,2)else r
  assert labelsin[r]==labelsout[rr]
 unit={}
 for typ,ports in faces.items():
  j=0 if typ=='C'else-2;pin,pout=ports[name[0]]
  ins=[r for r,x in enumerate(h)if x==pin and labelsin[r]==j]
  assert len(ins)==1
  r=ins[0];q=3-r if r in(1,2)else r
  assert outs[q]==pout and labelsout[q]==j
  clock=-1 if q==1 else 1 if q==2 else 0
  unit[typ]=dict(sheet=j,incoming_rank=r,outgoing_rank=q,clock_sign=clock,ports=[pin,pout])
 rows.append(dict(role=name,headings=h,heights=level,unit_faces=unit))
expectedC={'Z+':-1,'Z-':0,'A+':0,'A-':0,'B+':0,'B-':0,'Y+':0,'Y-':1}
expectedL={'Z+':0,'Z-':0,'A+':-1,'A-':0,'B+':0,'B-':1,'Y+':0,'Y-':0}
assert all(r['unit_faces']['C']['clock_sign']==expectedC[r['role']]and r['unit_faces']['L']['clock_sign']==expectedL[r['role']]for r in rows)
obj=dict(scope=__doc__,rows=rows,forced='C square: deltaZ=4+1{Yprev negative}deltaYprev, so Z positive. L square: deltaA=4+1{B negative}deltaB, so A positive.',global_clock='Pw=12a+sum_{positive Y/B}delta, forcing winding+1 for every RRLL axis G3 circle.',warning='Free B/Y negative gates remain possible necessary profiles; their parallel two-edge unit nodes are not erased as matched sigma-image pairs.')
Path(__file__).with_suffix('.json').write_text(json.dumps(obj,indent=2)+'\n');print('PASS',len(rows),'fixed profiles')
