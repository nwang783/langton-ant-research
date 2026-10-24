#!/usr/bin/env python3
"""Exact all-n same-PHYSICAL-cell cover for five four-heading neutral extensions.
Symbolic affine event positions include every module instance and router read.
"""
from pathlib import Path
from fractions import Fraction
from itertools import combinations
M='RRRRLLLLRL';G=['RLRRRRL','RRRRL','RRRRLRLRLRRRRL','LRRL'];V=[(0,1),(1,0),(0,-1),(-1,0)]
def add(a,b):return(a[0]+b[0],a[1]+b[1])
def sc(x,a):return(x*a[0],x*a[1])
def geom(w,h):
 p=(0,0);E=[]
 for r,c in enumerate(w):
  E.append((p,h,c));h=(h+(1 if c=='R'else-1))%4;p=(p[0]+V[h][0],p[1]+V[h][1])
 return E,p,h

def templates(cut):
 pos=[(0,0),(0,0)];T=(0,0);h=0;out=[]
 def word(w,name,count=(0,1)):
  nonlocal pos,T,h
  es,d,hh=geom(w,h)
  for r,(p,hi,c)in enumerate(es):out.append({'name':name,'phase':r,'count':count,'x':add(pos[0],(0,p[0])),'y':add(pos[1],(0,p[1])),'step':d,'time':add(T,(0,r)),'time_step':len(w),'turn':c,'heading':hi})
  pos=[add(pos[k],sc(d[k],count))for k in[0,1]];T=add(T,sc(len(w),count));h=hh
 word(M,'M0',(1,2));word(G[0],'A');word(M,'M1',(1,1));word(G[1],'B');word(M,'M2',(1,1));word(G[2][:cut],'Cpre');assert h==1;word(M,'ME',(1,0));word(G[2][cut:],'Cpost');word(M,'M3');word(G[3],'D');assert h==0 and pos==[(0,4),(0,4)]and T==(40,80)
 return out

def restrict(L,U,A,B):
 if A>0:L=max(L,(-B+A-1)//A)
 elif A<0:U=min(U,B//(-A))if U is not None else B//(-A)
 elif B<0:return None
 if U is not None and L>U:return None
 return L,U

def match(z,Q,L=1,U=None):
 v=z['step']
 # Fixed words have only j=0, even though their total displacement is recorded.
 if z['count']==(0,1):jn=jc=0
 else:
  k=0 if v[0] else 1
  assert abs(v[k])==1
  A=z['x']if k==0 else z['y'];jn=(Q[k][0]-A[0])//v[k];jc=(Q[k][1]-A[1])//v[k]
 for k,key in enumerate(['x','y']):
  A=z[key][0]+v[k]*jn-Q[k][0];B=z[key][1]+v[k]*jc-Q[k][1]
  if A:
   if (-B)%A:return None
   n=(-B)//A;L=max(L,n);U=n if U is None else min(U,n)
  elif B:return None
 if U is not None and L>U:return None
 rr=restrict(L,U,jn,jc)
 if rr is None:return None
 rr=restrict(*rr,z['count'][0]-jn,z['count'][1]-1-jc)
 if rr is None:return None
 return {'template':z['name'],'phase':z['phase'],'j':[jn,jc],'n_interval':rr,'time':add(z['time'],sc(z['time_step'],(jn,jc))),'turn':z['turn']}

def cover(cut,Q,L=1,U=None):
 ts=templates(cut);matches=[m for z in ts if(m:=match(z,Q,L,U))]
 points={L}
 if U is not None:points.add(U+1)
 for m in matches:
  points.add(m['n_interval'][0]);up=m['n_interval'][1]
  if up is not None:points.add(up+1)
 for a,b in combinations(matches,2):
  da=a['time'][0]-b['time'][0];db=a['time'][1]-b['time'][1]
  if da:
   f=(-db)//da
   for p in[f,f+1]:
    if p>=L and(U is None or p<=U+1):points.add(p)
 points=sorted(points);pieces=[]
 for i,lo in enumerate(points):
  if U is not None and lo>U:continue
  hi=points[i+1]-1 if i+1<len(points)else U
  if hi is not None and hi<lo:continue
  hh=[m for m in matches if m['n_interval'][0]<=lo and(m['n_interval'][1]is None or lo<=m['n_interval'][1])]
  hh.sort(key=lambda m:m['time'][0]*lo+m['time'][1])
  for a,b in zip(hh,hh[1:]):
   A=b['time'][0]-a['time'][0];B=b['time'][1]-a['time'][1]
   assert A*lo+B>0 and(hi is not None and A*hi+B>0 or hi is None and A>=0)
  bad=next(((a,b)for a,b in zip(hh,hh[1:])if a['turn']==b['turn']),None)
  assert bad,(cut,Q,lo,hi,hh)
  pieces.append({'interval':[lo,hi],'complete_history':hh,'bad_phases':[(z['template'],z['phase'])for z in bad]})
 return {'cut':cut,'Q':Q,'range':[L,U],'all_templates':ts,'all_matching_templates':matches,'pieces':pieces}
rows=[cover(3,[(-1,0),(1,2)]),cover(5,[(0,1),(0,1)]),cover(7,[(0,3),(0,1)]),cover(9,[(0,1),(0,1)],1,1),cover(9,[(0,2),(0,0)],2),cover(13,[(0,1),(0,1)],1,1),cover(13,[(-1,3),(1,0)],2)]
for r in rows:
 print('CUT',r['cut'],'Q',r['Q'],'pieces',len(r['pieces']))
 for z in r['pieces']:print(z['interval'],[(x['template'],x['phase'],x['time'],x['turn'])for x in z['complete_history']],z['bad_phases'])
import json
R=Path(__file__).resolve().parent
J={'status':'AUTHOR ALL-n PHYSICAL HISTORY EXCLUSION; independent audit pending','scope':'Five specified E-heading insertions into the long router of the prepared80 neutral-count extension, n>=1. Not all four-heading templates or arbitrary routers.','M':M,'routers':G,'base_exponents':[2,1,1,1],'increased_runs':['first N','W','S'],'inserted_run':'n E-heading modules at cut k of C','cuts':[3,5,7,9,13],'n_domain':'every integer n>=1','drift':[4,4],'period':'80+40n','growth':12,'symbolic_physical_cell_covers':rows}
(R/'prepared80_neutral_four_heading_obstruction_certificate.json').write_text(json.dumps(J,indent=2)+'\n')
print('PASS all n>=1, five exact cuts, nine affine complete-history pieces')
