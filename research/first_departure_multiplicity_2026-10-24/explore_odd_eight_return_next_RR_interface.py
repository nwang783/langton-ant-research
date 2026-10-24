"""Fixed odd eight-step return plus its forced following RR gate.
Necessary complete WHITE cap-four neighborhood; no period, length or front scan.
"""
from pathlib import Path
from itertools import product
from collections import Counter
base=Path(__file__).parent
ss=(base/'flat_flow2_symbolic_row_with_odd_left.py').read_text().split('rows=[];n=0')[0]
# The selected root clockwise face has LL(0,1), normalized global M=0.
ss=ss.replace("val={(0,-1):0};q=deque([(0,-1)])", "val={(0,1):0};q=deque([(0,1)])")
ns={};exec(ss,ns);check=ns['check'];out=ns['out']
words=lambda axis,first:[first+''.join(x)for n in range(1,5)for x in product(axis,repeat=n-1)]
counts=Counter();rows=[]
for b,d,e,p,q in product(['WWE','WWEE'],words('NS','N'),words('EW','E'),['NNSS','NSSN'],['EEWW','EWWE']):
 hs={(0,1):'WEE',(0,2):'NNSS',(-1,1):'NSSN',(-1,2):b,(-1,3):d,(0,3):e,(1,2):'WWEE',(1,3):p,(2,3):q,(2,2):'NNSS'}
 ans=check(hs);counts[ans]+=1
 if ans=='open':rows.append(dict(B=b,D=d,E=e,P=p,Q=q))
print('1800 candidates',dict(counts),'open rows',len(rows))
for r in rows:print(r)
# Inspect the first-return obligations of EVERY external physical helper,
# with arbitrary complete WHITE histories still allowed there.
V={'N':(0,1),'E':(1,0),'S':(0,-1),'W':(-1,0)}
def add(p,dr,sgn=1):return(p[0]+sgn*V[dr][0],p[1]+sgn*V[dr][1])
def rr(h,dr,kin):return[i for i in range(len(h))if(h[i]if kin=='in'else out(h,i))==dr]
def outer_check(hs):
 succ={};starts=[];ends={};ext=set()
 for p,h in hs.items():
  for dr in 'NESW':
   q=add(p,dr);sr=rr(h,dr,'out')
   if q in hs:
    tr=rr(hs[q],dr,'in');assert len(sr)==len(tr)
    for a,b in zip(sr,tr):succ[p,a]=(q,b)
   else:
    ext.add(q)
    for j,a in enumerate(sr):ends[p,a]=(q,dr,j)
   q0=add(p,dr,-1)
   if q0 not in hs:
    ext.add(q0)
    for j,a in enumerate(rr(h,dr,'in')):starts.append((q0,dr,j,(p,a)))
 loops=[]
 for x,dr,j,cur in starts:
  route=[]
  while True:
   assert cur not in route;route.append(cur)
   if cur not in succ:break
   cur=succ[cur]
  y,di,k=ends[cur]
  if x==y:loops.append(dict(cell=x,depart_heading=dr,depart_ordinal=j,arrive_heading=di,arrive_ordinal=k,steps=len(route)+1,route=route))
 candidates={}
 for x in sorted(ext):
  req=[]
  for dr in 'NESW':
   y=add(x,dr)
   if y in hs:req.append(('out',dr,len(rr(hs[y],dr,'in'))))
   y=add(x,dr,-1)
   if y in hs:req.append(('in',dr,len(rr(hs[y],dr,'out'))))
  aa='NS'if sum(x)%2==0 else'EW';good=[]
  for n in range(1,5):
   for hh in product(aa,repeat=n):
    h=''.join(hh)
    if any(len(rr(h,d,k))!=m for k,d,m in req):continue
    ok=True
    for lp in loops:
     if lp['cell']!=x:continue
     a=rr(h,lp['depart_heading'],'out')[lp['depart_ordinal']]
     b=rr(h,lp['arrive_heading'],'in')[lp['arrive_ordinal']]
     if b!=a+1:ok=False;break
    if ok:good.append(h)
  candidates[x]=good
 return candidates,loops
for r in rows:
 hs={(0,1):'WEE',(0,2):'NNSS',(-1,1):'NSSN',(-1,2):r['B'],(-1,3):r['D'],(0,3):r['E'],(1,2):'WWEE',(1,3):r['P'],(2,3):r['Q'],(2,2):'NNSS'}
 cc,ll=outer_check(hs)
 print('outer',r,'empty',[x for x,y in cc.items()if not y],'singletons',{str(x):y[0]for x,y in cc.items()if len(y)==1},'returns',[(x['cell'],x['depart_heading'],x['depart_ordinal'],x['arrive_heading'],x['arrive_ordinal'],x['steps'])for x in ll])
