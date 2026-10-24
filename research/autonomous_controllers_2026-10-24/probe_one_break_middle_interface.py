#!/usr/bin/env python3
"""Discovery-only one SSNS middle-R landing on a single-used F4 boundary."""
from itertools import combinations,product
from collections import Counter
import enumerate_g8_cycle_two_outer_rows as core
from check_extremal_read_coupling import D,quotient
DRIFT=(2,-2)
def cwords(I,J):
 out=[]
 for n in range(max(I,J),2*(I+J)+2):
  z=I+J-n//2
  if z%2:continue
  a=z//2;b=I-a
  if not 0<=a<=(n+1)//2 or not 0<=b<=n//2:continue
  for rr,ll in product(combinations(range(0,n,2),a),combinations(range(1,n,2),b)):
   E=set(rr)|set(ll);hs=tuple(1 if k in E else 3 for k in range(n));ee=sorted(E);ss=[k for k,h in enumerate(hs)if(h+(1 if k%2==0 else-1))%4==2]
   if ee[1]==ss[0]+1:out.append(hs)
 return out

def qwords(I,J,rels):
 out=[];total=0
 for odd in(0,1):
  for X in range(I+1):
   n=2*(J-I+2*X)-odd
   if n<max(I,J)or n<1:continue
   if not 0<=X<=(n+1)//2 or not 0<=I-X<=n//2:continue
   for rr,ll in product(combinations(range(0,n,2),X),combinations(range(1,n,2),I-X)):
    N=set(rr)|set(ll);hs=tuple(0 if k in N else 2 for k in range(n));nn=sorted(N);ww=[k for k,h in enumerate(hs)if(h+(1 if k%2==0 else-1))%4==3];assert len(ww)==J;total+=1
    if all(nn[b]==ww[a]+1 for a,b,L in rels):out.append(hs)
 return out,total

def lower(a,b):
 core.PTS=[(r,t-r)for t in range(-1,2)for r in(0,1)];core.IX={p:i for i,p in enumerate(core.PTS)}
 H=[(3,),(3,),(2,2,0,2),(2,2,0),a,b];kind,wit=core.assess(H);assert kind=='open_survivor';rels=[[],[]]
 for chain in wit['chains']:
  (i,j),k0=chain[0];assert k0==0;h=H[i][j];p=core.PTS[i];sp=(p[0]-D[h][0],p[1]-D[h][1]);sr,sk=quotient(sp,DRIFT)
  (ii,jj),kk=chain[-1];ho=(H[ii][jj]+(1 if jj%2==0 else-1))%4;q=core.PTS[ii];tp=(q[0]+kk*2+D[ho][0],q[1]-kk*2+D[ho][1]);tr,tk=quotient(tp,DRIFT)
  assert sum(sp)==sum(tp)==2 and h==3 and ho==0
  if sp==tp:
   aord=[z for z,hh in enumerate(H[i])if hh==h].index(j)
   bord=[z for z,hh in enumerate(H[ii])if(hh+(1 if z%2==0 else-1))%4==ho].index(jj)
   rels[sr[0]].append((aord,bord,len(chain)+1))
 return H,rels
if __name__=='__main__':
 A=cwords(2,3);B=cwords(3,2);total=0;out=[]
 for i,a in enumerate(A):
  for j,b in enumerate(B):
   H,rel=lower(a,b);q,nq=qwords(len(a)-3,len(b)-3,rel[0]);r,nr=qwords(len(b)-2,len(a)-2,rel[1]);total+=len(q)*len(r)
   out.append({'A0':i,'A1':j,'relations':rel,'counts':[nq,nr],'filtered':[len(q),len(r)],'pairs':len(q)*len(r)})
 print('filtered pairs',total)
 for x in out:print(x)
