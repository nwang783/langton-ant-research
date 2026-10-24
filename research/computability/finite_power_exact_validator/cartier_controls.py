"""Exact F2 Cartier automata, independently compared with formal coefficients.
These controls do not implement the full quantified given-seed decision procedure.
"""
from collections import deque
import itertools,json,pathlib,time
HERE=pathlib.Path(__file__).parent
O=(0,0,0)

def mul(A,B):
 C=set()
 for a in A:
  for b in B:
   e=tuple(a[i]+b[i] for i in range(3))
   if e in C:C.remove(e)
   else:C.add(e)
 return frozenset(C)

def cartier(P,H,digit):
 return frozenset(tuple((e[i]-digit[i])//2 for i in range(3)) for e in mul(P,H)
  if all(e[i]%2==digit[i] for i in range(3)))

def machine(P,H):
 assert O in H
 P=frozenset(P);H=frozenset(H);states=[P];ids={P:0};trans=[]
 bounds=tuple(max([e[i] for e in P|H]+[0]) for i in range(3))
 digits=list(itertools.product(range(2),repeat=3))
 for state in states:
  row=[]
  for d in digits:
   out=cartier(state,H,d)
   assert all(e[i]<=bounds[i] for e in out for i in range(3))
   if out not in ids:ids[out]=len(states);states.append(out)
   row.append(ids[out])
  trans.append(row)
 return dict(states=states,transitions=trans,outputs=[int(O in p) for p in states],bounds=bounds)

def evaluate(M,index):
 assert all(n>=0 for n in index)
 state=0;n=list(index)
 while any(n):
  d=4*(n[0]%2)+2*(n[1]%2)+n[2]%2
  state=M['transitions'][state][d];n=[v//2 for v in n]
 return M['outputs'][state]

def direct_coefficients(P,H,shape):
 F={};other=set(H)-{O}
 for n in itertools.product(*(range(b) for b in shape)):
  ans=int(n in P)
  for h in other:
   if all(h[i]<=n[i] for i in range(3)):ans^=F[tuple(n[i]-h[i] for i in range(3))]
  F[n]=ans
 return F

def literal_right_five(r):
 # Entire prescribed word R^(5^r), not assumed ant-legal.
 p=(0,0);h=0;D=((0,1),(1,0),(0,-1),(-1,0));odd=set()
 for _ in range(5**r):
  if p in odd:odd.remove(p)
  else:odd.add(p)
  h=(h+1)%4;p=(p[0]+D[h][0],p[1]+D[h][1])
 return odd

def main():
 start=time.monotonic()
 cases=[
  ('trinomial_parity',{O},{O,(1,0,0),(1,1,0),(1,0,1)}),
  ('positive_glider',{O},{O,(1,1,0)}),
  ('geometric_R5_read_parity_shifted_y',{(0,0,1),(1,1,1),(1,1,0),(1,0,0)},{O,(2,0,0)}),
  ('two_dimensional_grid',{O},{O,(0,1,0),(0,0,1),(0,1,1)}),
 ]
 records=[];checks=0
 for name,P,H in cases:
  M=machine(P,H);F=direct_coefficients(P,H,(32,17,17))
  for idx,c in F.items():assert evaluate(M,idx)==c,(name,idx);checks+=1
  records.append(dict(name=name,numerator=sorted(P),denominator=sorted(H),states=len(M['states']),degree_bounds=M['bounds'],
   transitions=M['transitions'],outputs=M['outputs']))
 P,H=cases[2][1:];M=machine(P,H);literal_checks=0;letters=0
 for r in range(9):
  odd=literal_right_five(r);letters+=5**r
  for x in range(-2,4):
   for y in range(-3,3):
    got=evaluate(M,(r,x,y+1)) if x>=0 and y+1>=0 else 0
    assert got==int((x,y) in odd),(r,x,y)
    literal_checks+=1
 # The literal geometric R5 model is deliberately not an ant model: root white
 # first read changes origin to black, but its fifth prescribed R needs white.
 B=set();p=(0,0);h=0;D=((0,1),(1,0),(0,-1),(-1,0));bad=None
 for t in range(5):
  if p in B:bad=t;break
  B.add(p);h=(h+1)%4;p=(p[0]+D[h][0],p[1]+D[h][1])
 assert bad==4
 out=dict(formal_coefficient_checks=checks,literal_parity_checks=literal_checks,literal_letters=letters,
 geometric_control_first_conflict=bad,records=records,
 scope='Cartier coefficient/parity layer only; not an end-to-end automata/frame validator.',seconds=time.monotonic()-start)
 (HERE/'cartier_controls.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2))
if __name__=='__main__':main()
