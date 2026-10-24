#!/usr/bin/env python3
"""No author imports. Full 4-variable Lyapunov solve, Schur criterion, carry replay."""
from fractions import Fraction as F
from pathlib import Path
import json,itertools,math,hashlib
BASE=Path(__file__).parent/'matrix_bridge_snapshot'

def gauss(a,b):
 a=[[F(z) for z in row]+[F(v)] for row,v in zip(a,b)]
 for j in range(len(a)):
  piv=next((i for i in range(j,len(a)) if a[i][j]),None)
  if piv is None:return None
  a[j],a[piv]=a[piv],a[j];v=a[j][j];a[j]=[z/v for z in a[j]]
  for i in range(len(a)):
   if i!=j:
    v=a[i][j];a[i]=[x-v*y for x,y in zip(a[i],a[j])]
 return [row[-1] for row in a]

def independent_norm(A):
 a,b=A[0];c,d=A[1];det=a*d-b*c
 if det==0:return False,None
 B=[[F(d,det),F(-b,det)],[F(-c,det),F(a,det)]]
 # Exact Schur criterion; for real roots the signs of (1-r1)(1-r2)
 # and (1+r1)(1+r2), plus |r1*r2|<1, force both into (-1,1).
 # For conjugate roots the product is their common squared modulus.
 tr=B[0][0]+B[1][1];dd=F(1,det)
 expansive=abs(dd)<1 and 1-tr+dd>0 and 1+tr+dd>0
 ids=list(itertools.product(range(2),repeat=2));eq=[];rhs=[]
 for i,j in ids:
  eq.append([F(i==u and j==v)-B[u][i]*B[v][j] for u,v in ids]);rhs.append(int(i==j))
 p=gauss(eq,rhs)
 if expansive:
  assert p is not None and p[1]==p[2]
  assert p[0]>0 and p[0]*p[3]>p[1]*p[2]
  return True,(p[0],p[1],p[3])
 if p is not None:assert not(p[0]>0 and p[0]*p[3]>p[1]*p[2])
 return False,None

def qform(P,v):return P[0]*v[0]**2+2*P[1]*v[0]*v[1]+P[2]*v[1]**2

def ceilroot(x):
 v=math.isqrt(x.numerator//x.denominator)
 return v+int(v*v<x)

def mat(A,v):return tuple(sum(A[i][j]*v[j] for j in range(2)) for i in range(2))
def plus(a,b):return tuple(x+y for x,y in zip(a,b))
def minus(a,b):return tuple(x-y for x,y in zip(a,b))

def carry_control(A,nxt,off,ref):
 _,P=independent_norm(A);q=F(ref['inverse_contraction_upper'])
 offsets=sum(off,[]);M=ceilroot(max(qform(P,minus(x,y)) for x in offsets for y in offsets))
 target=ceilroot(max(qform(P,v) for v in itertools.product((-1,1),repeat=2)))
 rr=q*M/(1-q);R=max(target,-((-rr.numerator)//rr.denominator))
 states=[(0,0,(0,0))];index={states[0]:0};edges=[]
 for s in states:
  row={}
  for a,b in itertools.product(range(2),repeat=2):
   child=None
   if s is not None:
    u,v,z=s;zz=plus(mat(A,z),minus(off[u][a],off[v][b]))
    if qform(P,zz)<=R*R:child=(nxt[u][a],nxt[v][b],zz)
   if child not in index:index[child]=len(states);states.append(child)
   row[a,b]=index[child]
  edges.append(row)
 assert len(states)==ref['raw_difference_states']
 assert M==ref['offset_difference_norm_ceiling'] and R==ref['carry_radius']
 def point(n):
  z=(0,0);s=0
  for char in bin(n)[2:]:
   a=int(char);z=plus(mat(A,z),off[s][a]);s=nxt[s][a]
  return z
 points=[point(n) for n in range(256)];checks=0
 for s in range(256):
  for t in range(256):
   ss=bin(s)[2:];tt=bin(t)[2:];L=max(len(ss),len(tt));state=0
   for a,b in zip(ss.zfill(L),tt.zfill(L)):state=edges[state][int(a),int(b)]
   actual=None if states[state] is None else states[state][2]
   expected=minus(points[s],points[t])
   for v in itertools.product(range(-1,2),repeat=2):
    assert (actual==v)==(expected==v);checks+=1
 return dict(matrix=A,states=len(states),radius=R,pair_target_checks=checks)

def main():
 rows=json.loads((BASE/'source_norms.json').read_text());nexp=0;nnon=0
 for A,ps,q in rows:
  expansive,P=independent_norm(A)
  assert expansive==(ps is not None)
  if not expansive:nnon+=1;continue
  nexp+=1;assert tuple(map(F,ps))==P;q=F(q);assert 0<q<1
  x=1-(1-q*q)*P[0];y=-(1-q*q)*P[1];z=1-(1-q*q)*P[2]
  assert x>=0 and z>=0 and x*z>=y*y
 assert nexp+nnon==2401
 refs=json.loads((BASE/'expanding_matrix_controls.json').read_text())['cases']
 cases=[(((2,0),(0,3)),[[0,0]],[[(0,0),(1,1)]]),(((2,3),(0,2)),[[0,0]],[[(0,0),(0,1)]]),(((0,-2),(3,0)),[[0,1],[1,0]],[[(0,0),(1,0)],[(0,1),(1,-1)]])]
 controls=[carry_control(*a,r) for a,r in zip(cases,refs)]
 out=dict(status='PASS',integer_matrices_tested=2401,expansive=nexp,nonexpansive=nnon,method='Independent full 4-variable rational Lyapunov solve versus exact Schur test; all source contraction bounds checked by PSD',carry_controls=controls,frozen_files={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in BASE.iterdir() if p.is_file()},scope='Exact analytic theorem and independently implemented norm/carry controls; no finite-seed counterexample and no claim to reverify all prior automata closure code.')
 Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
