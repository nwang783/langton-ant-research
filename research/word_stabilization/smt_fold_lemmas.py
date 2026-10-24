"""Bounded SMT instantiations of already audited all-parameter fold lemmas."""
from smt_v_lastwriter import bv,eq,ite,conj,disj

def constraints(n):
 out=[]
 def add(x):out.append('(assert '+x+')')
 # No three folds in an uninterrupted alphabet {U,Q,B} or {V,Q,B}.
 for name,reset in [('uf',('C','V')),('vf',('C','U'))]:
  for i in range(n+1):
   out.append(f'(declare-fun {name}{i} () (_ BitVec 2))');add(f'(bvult {name}{i} {bv(3,2)})')
  add(eq(f'{name}0',bv(0,2)))
  for i in range(n):
   r=disj([eq(f'k{i}',bv('CUVQB'.index(a),3))for a in reset]);f=disj([eq(f'k{i}',bv(3,3)),eq(f'k{i}',bv(4,3))])
   add(eq(f'{name}{i+1}',ite(r,bv(0,2),ite(f,f'(bvadd {name}{i} {bv(1,2)})',f'{name}{i}'))))
 # Equal-length mixed runs have equal U/V counts iff their V counts agree.
 for name in ['nv','nx']:
  for i in range(n+1):out.append(f'(declare-fun {name}{i} () (_ BitVec 8))')
  add(eq(f'{name}0',bv(0,8)))
 for i in range(n):
  isv=eq(f'k{i}',bv(2,3));isuv=disj([eq(f'k{i}',bv(1,3)),isv])
  add(eq(f'nv{i+1}',f'(bvadd nv{i} {ite(isv,bv(1,8),bv(0,8))})'))
  add(eq(f'nx{i+1}',f'(bvadd nx{i} {ite(isuv,bv(0,8),bv(1,8))})'))
 for i in range(n):
  for j in range(i+1,n):
   k=2*j-i
   if k>=n:break
   foldi=disj([eq(f'k{i}',bv(3,3)),eq(f'k{i}',bv(4,3))]);foldj=disj([eq(f'k{j}',bv(3,3)),eq(f'k{j}',bv(4,3))])
   test=[foldi,foldj,eq(f'nx{j}',f'nx{i+1}'),eq(f'nx{k}',f'nx{j+1}'),eq(f'(bvsub nv{j} nv{i+1})',f'(bvsub nv{k} nv{j+1})')]
   add('(not '+conj(test)+')')
 return '\n'.join(out)
