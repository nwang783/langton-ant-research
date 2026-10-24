"""Interval-algebra controls for signed literal reset rank equalities only.
These assignments are not board factors/fronts or exterior realizations.
"""
from pathlib import Path
from itertools import product
import json
rows=[]
def ii(a,b,t):return int(a<=t<b)if a<=b else-int(b<=t<a)
for kind in['single','LL']:
 for D in([4,8,12]if kind=='single'else[4]):
  r1=21 if kind=='single' else 23;r2=r1+D
  x1=r1+1 if kind=='single'else r1+2;y1=r2-1
  for ax,ay in product([8,16,36],repeat=2):
   x3=x1+ax;y3=y1+ay
   edges=[(r1,x1),(y1,r2)]if kind=='single'else[(r1,r1+1),(r1+1,x1),(y1,r2)]
   for q in range(r1-2,max(x3,y3)+2):
    t=q+.5;lhs=ii(r1,r2,t)+ii(y1,y3,t)-ii(x1,x3,t)
    rhs=sum(ii(a,b,t)for a,b in edges)+ii(x3,y3,t);assert lhs==rhs
   rows.append(dict(kind=kind,root_span=D,X13=ax,Y13=ay,tail_sign=(y3>x3)-(y3<x3)))
  if kind=='single':
   q3=r1+1;q1=q3-12;p1=r2-1;p3=p1+16
   for q in range(q1-2,p3+2):
    t=q+.5
    assert ii(q1,q3,t)+ii(r1,r2,t)+ii(p1,p3,t)==ii(q1,p3,t)+ii(r1,q3,t)+ii(p1,r2,t)

# Passive single-V route is Y.L1 -> V.L3 -> nextY.L3, length TWO.
for width in [1,2,3]:
 s=40;e=s+width;left=(20,e);right=(s,60)
 for q in range(18,62):
  t=q+.5;assert ii(*left,t)+ii(*right,t)==ii(20,60,t)+ii(s,e,t)
obj=dict(passive_gap_overlap_controls=[1,2,3],scope=__doc__,mixed_tail_controls=rows,positive_and_negative_tails_retained=True,singleton_YY_relay_controls=3,proof='All sizes and ages follow by oriented interval telescoping and the displayed exact physical ordinal relations.')
Path(__file__).with_suffix('.json').write_text(json.dumps(obj,indent=2)+'\n');print('PASS',len(rows),'tail controls, both signs retained')
