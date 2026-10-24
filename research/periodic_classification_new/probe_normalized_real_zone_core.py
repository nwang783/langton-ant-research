#!/usr/bin/env python3
"""Order-free finite strict normalized-clock relaxation; exploratory.
Use scaled physical clocks X_e=N*t_e/P. If P>=N>0, a real successor
with seam k obeys -Nk < X_v-X_u <= 1-Nk. Local ranks strictly increase.
These necessary interval bounds forget the common positive 1/P and the
cyclic order. Real strict DBM projection is exact, finite clipping is safe.
No full-front theorem is inferred until the framework and graph are audited.
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

def transitions(paths,flat,old,new,p,splice,mod=2,M=16,N=8):
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
  D[ib][ia]=min(D[ib][ia],2*(1-N*k))
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
