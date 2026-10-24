#!/usr/bin/env python3
"""Adaptive-upper-bound finite strict normalized-clock relaxation.
The N argument is one fixed clock scale S: X_e=S*t_e/P, not a period bound.
Given a proved current lower bound P>=L, choose U>=S/L. A real successor
with seam k obeys -S*k < X_v-X_u <= U-S*k. Local ranks strictly increase.
The caller may increase L as distinct full-drift events are exposed without
rescaling S; older weaker inequalities remain valid. Forgetting the common
S/P increment and cyclic order enlarges the model. Strict real DBM projection
is exact; outward clipping is safe. Complete graph claims need audit.
"""
INF=10**9

def plus(a,b):
 return a+b+((a&1) and (b&1))

def close(D):
 n=len(D)
 for k in range(n):
  for i in range(n):
   a=D[i][k]
   if a>=INF:continue
   ai=a&1;Di=D[i];Dk=D[k]
   for j in range(n):
    b=Dk[j]
    if b>=INF:continue
    z=a+b+(ai and (b&1))
    if z<Di[j]:Di[j]=z
   if Di[i]<0:return False
 return True

def transitions(paths,flat,old,new,p,splice,mod=2,M=16,N=8,U=1):
 sp=splice(paths,old,new,p,mod)
 if sp is None:return [],'sealed_cycle'
 nodes,physical,pieces,terminal=sp
 if not pieces:return [((),())],None
 oldvars=sorted({j for a,b,w in paths for j in (a,b)});nv=len(oldvars);assert len(flat)==nv*nv
 ns=sorted(nodes);ix={a:i for i,a in enumerate(ns)}
 D=[[0 if i==j else INF for j in range(len(ns))] for i in range(len(ns))]
 for i,a in enumerate(oldvars):
  for j,b in enumerate(oldvars):D[ix[0,a]][ix[0,b]]=flat[i*nv+j]
 for a,b,k in physical:
  ia,ib=ix[a],ix[b]
  # Bound encoding 2*c for <=c, 2*c-1 for <c. D[a][b] bounds X_a-X_b.
  D[ib][ia]=min(D[ib][ia],2*(U-N*k))
  D[ia][ib]=min(D[ia][ib],2*N*k-1)
 for c,h in enumerate(new):
  for j in range(len(h)-1):D[ix[1,(c,j)]][ix[1,(c,j+1)]]=min(D[ix[1,(c,j)]][ix[1,(c,j+1)]],-1)
 if not close(D):return [],'normalized_real_clock'
 if terminal:return ['POTENTIAL_COMPLETE_FRONT'],None
 pieces.sort(key=lambda c:c['walk'][0])
 nxt=tuple((c['walk'][0][1],c['walk'][-1][1],c['voltage']) for c in pieces)
 vs=sorted({j for a,b,w in nxt for j in (a,b)})
 def abstract(x):return INF if x>2*M else max(x,-2*M)
 mat=tuple(abstract(D[ix[1,a]][ix[1,b]]) for a in vs for b in vs)
 return [(nxt,mat)],None
