"""Executed automatic forced-color control along genuine nested occurrences.
This is one exact negative control, not the complete occurrence-cover compiler.
"""
import pathlib,sys,itertools,json,time
import sympy as S
HERE=pathlib.Path(__file__).parent
sys.path.insert(0,str(HERE.parent));sys.path.insert(0,str(HERE.parent/'unit_inductive_certificates'))
from automatic_relations import Rel,linear,FALSE
from cartier_controls import machine,evaluate
from ray_parity_extractor import extract_rationals,V
from check_read_sets import typed

def affine_pullback(M,variables,coeff,constant):
 """Exact Q(sum coeff_i*n+constant) on natural n; negative outputs give0.
 M uses digit index4*rbit+2*xbit+ybit, unlike Rel's variable order.
 """
 variables=tuple(variables);start=(0,tuple(constant));states=[start];ix={start:0};tr=[];ac=set()
 def tail(q,carry):
  if any(v<0 for v in carry):return False
  while any(carry):
   q=M['transitions'][q][sum((carry[i]%2)<<(2-i) for i in range(3))]
   carry=tuple(v//2 for v in carry)
  return bool(M['outputs'][q])
 for i,(q,c) in enumerate(states):
  if tail(q,c):ac.add(i)
  row=[]
  for a in range(1<<len(variables)):
   z=tuple(c[h]+sum(coeff[h][j]*((a>>j)&1) for j in range(len(variables))) for h in range(3))
   digit=sum((z[h]%2)<<(2-h) for h in range(3))
   ns=(M['transitions'][q][digit],tuple(v//2 for v in z))
   if ns not in ix:ix[ns]=len(states);states.append(ns)
   row.append(ix[ns])
  tr.append(row)
 return Rel(variables,tr,ac).minimal()

def parity_bounded(predicate,hidden,bound):
 if hidden==bound:raise ValueError('hidden and visible bound must differ')
 # The method supplies the guard, rather than trusting a padding promise.
 A=predicate&linear({bound:1,hidden:-1},1,'>=')
 at=A.vs.index(hidden);vs=A.vs[:at]+A.vs[at+1:]
 def insert(a,b):return (a&((1<<at)-1))|(b<<at)|((a>>at)<<(at+1))
 masks=[1<<A.start];ix={masks[0]:0};tr=[];ac=set();accept=sum(1<<s for s in A.ac)
 for i,mask in enumerate(masks):
  if (mask&accept).bit_count()%2:ac.add(i)
  row=[]
  for a in range(1<<len(vs)):
   new=0;bits=mask
   while bits:
    bit=bits&-bits;s=bit.bit_length()-1;bits-=bit
    for b in (0,1):new^=1<<A.tr[s][insert(a,b)]
   if new not in ix:ix[new]=len(masks);masks.append(new)
   row.append(ix[new])
  tr.append(row)
 return Rel(vs,tr,ac).minimal()

def main():
 start=time.monotonic();images=['RLLLLRRRR','LRRRRLLLL']*4;shift,rat=extract_rationals(images);assert shift==(1,1)
 machines={}
 for state in (0,3):
  _,_,p,h=rat[state];machines[state]=machine(p.monoms(),h.monoms())
 # The edge cycle (child1,child1) is a genuine 0→3→0 loop of displacement(1,1).
 phi=typed(images);assert phi[0][1]==(3,(1,0)) and phi[3][1]==(0,(0,1))
 # At the selected occurrence in depth2a, earlier siblings at repetitionq are
 # Q0(2(a-q)-1,a-q,a-q) and Q3(2(a-q)-2,a-q-1,a-q).
 # Put j=a-q and then k=j-1, so k ranges0..a-1. Linear spatial shift is(r,r).
 term0=affine_pullback(machines[0],('k',),((2,),(3,),(3,)),(1,2,2))
 term3=affine_pullback(machines[3],('k',),((2,),(3,),(3,)),(0,0,1))
 f=term0.both(term3,lambda a,b:a!=b)
 forced=parity_bounded(f,'k','a')
 # This is a required INITIAL black bit at(a,a): terminal state0 requires R.
 finite=forced.bounded();assert not finite
 numerical=0
 for a in range(257):
  expected=0
  for k in range(a):
   expected^=evaluate(machines[0],(2*k+1,3*k+2,3*k+2))
   expected^=evaluate(machines[3],(2*k,3*k,3*k+1))
  assert forced.eval(a=a)==bool(expected);numerical+=1
 # Independent literal polynomial recurrence, without Cartier, at all required
 # positions through depth48. Coefficients are read parity; no ant legality.
 Q=[{(0,0)} for _ in range(8)];values={};literal_checks=0
 for r in range(49):
  for k in range(24):
   if r==2*k+1:values[0,k]=int((k+1,k+1) in Q[0]);literal_checks+=1
   if r==2*k:values[3,k]=int((k,k+1) in Q[3]);literal_checks+=1
  if r<48:
   nxt=[]
   for row in phi:
    o=set()
    for t,p in row:o.symmetric_difference_update((x+p[0],y+p[1]) for x,y in Q[t])
    nxt.append(o)
   Q=nxt
 total=0
 for a in range(25):
  if a:total^=values[0,a-1]^values[3,a-1]
  assert forced.eval(a=a)==bool(total)
 out=dict(images=images,cycle_children=[1,1],cycle_weight=[1,1],
  parity_kernel_states={s:len(M['states']) for s,M in machines.items()},
  automatic_term_states=[len(term0.tr),len(term3.tr)],forced_color_states=len(forced.tr),
  required_black_ray_finite=finite,forced_black_depths_through64=[a for a in range(65) if forced.eval(a=a)],
  numeric_projection_checks=numerical,literal_polynomial_position_checks=literal_checks,
  forced_relation=dict(variables=forced.vs,transitions=forced.tr,accepting=sorted(forced.ac),start=forced.start),
  scope='Exact automatically certified infinite required initial-black set along genuine selected occurrences(a,a). This known excluded unit-nine control cannot have finite support. No complete cover compiler or growing positive model.',seconds=time.monotonic()-start)
 (HERE/'automatic_selected_ray_control.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({k:v for k,v in out.items() if k not in ('images','forced_relation')},indent=2))
if __name__=='__main__':main()
