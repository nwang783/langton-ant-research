#!/usr/bin/env python3
"""Algebraic even-gap transfer and an unbounded OPEN three-cell clock family.
This is not a complete front, board factor, controller, or reachable-prefix proof.
"""
import json,hashlib,itertools
from pathlib import Path
from partial_drift31_graph import graph
from certify_drift31_read_minimum import depart
R=Path(__file__).resolve().parent
A=((1,-2,2),(2,0,1),(1,1,-1))
def mul(B,C):return [[sum(B[i][k]*C[k][j]for k in range(3))for j in range(3)]for i in range(3)]
def mv(v):return tuple(sum(a*b for a,b in zip(row,v))for row in A)
def h_opts(I,J):return range(min(I,J,(I+J)//3)+1)
def v_opts(I,J):return range(max(0,(2*I-J+2)//3,I-J),I+1)
def phase(p):return(p[0]%2)if p[1]%2==0 else 3-p[0]%2

def open_family(k):
 H=[tuple([0,0,2,2]*k),tuple([1,1,3,3]*k),tuple([0,0,2,2]*k)];T=[[],[],[]]
 for b in range(k):
  T[0]+=[128*b+60,128*b+64,128*b+96,128*b+100]
  T[1]+=[128*b+1,128*b+33,128*b+65,128*b+97]
  T[2]+=[128*b,128*b+4,128*b+8,128*b+32]
 P=128*k+2;kind,G=graph(H,[0,1,2]);assert kind=='open'
 assert len(set(sum(T,[])))==12*k and all(0<=t<P for t in sum(T,[]))
 for i,hs in enumerate(H):
  assert len(hs)==4*k
  assert all(T[i][r+1]-T[i][r]>=4 and(T[i][r+1]-T[i][r])%4==0 for r in range(4*k-1))
  for lift in range(-3,4):
   p=(-i+3*lift,lift)
   assert all((t+lift*P)%4==phase(p)for t in T[i])
  assert {h:hs.count(h)for h in set(hs)}=={(i%2):2*k,(i%2)+2:2*k}
  assert all(len(depart(hs,h))==2*k for h in((1-i%2),(1-i%2)+2))
 for chain in G['chains']:
  clocks=[T[i][j]+v*P for((i,j),v)in chain];assert all(b==a+1 for a,b in zip(clocks,clocks[1:]))
 assert len(G['chains'])==8*k
 return{'k':k,'period_parameter':P,'missing_phases':P-12*k,'complete_histories':H,'clocks_at_representatives':T,'open_graph':G}

def main():
 assert mul(mul(A,A),A)==[[-3,0,0],[0,-3,0],[0,0,-3]]
 # Fresh finite checks of the algebra. The proof uses the displayed formulae,
 # not extrapolation from these bounded controls.
 checked=0
 for I,J in itertools.product(range(12),repeat=2):
  bruteH=[];bruteV=[]
  for m in range(I+J+1):
   for r in range(m+1):
    for l in range(m+1):
     if r+l!=I:continue
     if m-r+l==J:bruteH.append((m,l))
     if m+r-l==J:bruteV.append((m,l))
  exactH=[(I+J-2*l,l)for l in h_opts(I,J)]
  exactV=[(J-I+2*h,h)for h in v_opts(I,J)]
  assert sorted(bruteH)==sorted(exactH)and sorted(bruteV)==sorted(exactV);checked+=1
 trans=0
 for w,n,s in itertools.product(range(9),repeat=3):
  far=w+n-s
  if far<0:continue
  for l in h_opts(w,s):
   e=2*s+w-4*l;nn=s+2*w-4*l
   for h in v_opts(n,e):
    ww=e-2*n+4*h;ss=2*e-3*n+4*h
    v=(ww,nn,far);assert ww+nn-far==ss and min(*v,ss)>=0
    base=mv((w,n,s));assert v==(base[0]+4*(h-l),base[1]-4*l,base[2]);trans+=1
 residues=[];seen=set()
 for v in itertools.product(range(4),repeat=3):
  if v in seen:continue
  cy=[];at=v
  while at not in seen:seen.add(at);cy.append(at);at=tuple(x%4 for x in mv(at))
  assert at==v and len(cy)in(1,3);residues.append(cy)
 assert sum(len(c)==1 for c in residues)==4 and sum(len(c)==3 for c in residues)==20
 controls=[open_family(k)for k in(1,2,3,5,10,25)]
 result={'scope':__doc__,'matrix':A,'matrix_cube':mul(mul(A,A),A),'local_count_formula_control_pairs':checked,'two_cell_transfer_controls':trans,'all64_residue_states_as_cycles':residues,'unbounded_open_family_formula':{'histories':['(NNSS)^k','(EEWW)^k','(NNSS)^k'],'T0_block_clocks':[60,64,96,100],'T1_block_clocks':[1,33,65,97],'T2_block_clocks':[0,4,8,32],'add_per_block':128,'period_parameter':'128*k+2','each_physical_port_count':'2*k','named_odd_output_count':0,'named_events':'12*k','open_chains':'8*k'},'literal_family_controls':controls,'dependency_hashes':{f:hashlib.sha256((R/f).read_bytes()).hexdigest()for f in ['partial_drift31_graph.py','certify_drift31_read_minimum.py']},'warning':'Reachability from the signed lower prefix, full boundary closure and one actual event-cycle are NOT established. No positive controller or impossibility of every finite abstraction is claimed.'}
 (R/'drift31_even_gap_transfer_certificate.json').write_text(json.dumps(result,separators=(',',':'))+'\n');print('PASS',checked,trans,'residue cycles',len(residues),'open controls',[z['k']for z in controls])
if __name__=='__main__':main()
