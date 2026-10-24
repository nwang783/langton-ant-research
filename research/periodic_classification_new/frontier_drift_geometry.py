#!/usr/bin/env python3
"""Finite row geometry for full drift(a,b), a>0, |b|<=a, a+b even.
Representatives (i, row+floor(b*i/a)). Every physical edge changes row by <=1.
"""
D=[(0,1),(1,0),(0,-1),(-1,0)]
class Geometry:
 def __init__(self,a,b):
  assert a>0 and abs(b)<=a and (a+b)%2==0
  self.a=a;self.b=b;self.base=[b*i//a for i in range(a)];self.arcs=[[],[]]
  for p in (0,1):
   for c in range(a):
    par=(c+self.base[c]+p)%2
    for h in ((0,2) if par==0 else (1,3)):
     dx,dy=D[h];x=c+dx;k=x//a;cc=x-k*a;dr=self.base[c]+dy-k*b-self.base[cc]
     assert -1<=dr<=1
     self.arcs[p].append((c,cc,h,k,dr))
 def parity(self,p,c):return (c+self.base[c]+p)%2
 def splice_arcs(self,p):
  out=[]
  for c,cc,h,k,dr in self.arcs[p]:
   if dr==1:out.append((0,c,1,cc,h,k))
  for c,cc,h,k,dr in self.arcs[1-p]:
   if dr==0:out.append((1,c,1,cc,h,k))
   elif dr==-1:out.append((1,c,0,cc,h,k))
  return out
