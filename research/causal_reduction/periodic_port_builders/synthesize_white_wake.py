"""Bounded white-input front synthesis, with an exact prescribed settled wake.
A SAT result must pass literal replay. UNKNOWN is not an exclusion.
"""
import sys,pathlib,time,json,re
P=pathlib.Path(__file__).resolve().parent;sys.path.insert(0,str(P.parent/'morphic_candidates'))
from smt_inflation_refinement import Z3
D=((0,1),(1,0),(0,-1),(-1,0))
def OR(xs):return '(or '+' '.join(xs)+')'
def AND(xs):return '(and '+' '.join(xs)+')'
def NOT(x):return '(not '+x+')'
def EQ(a,b):return '(= '+a+' '+b+')'
def XOR(a,b):return '(xor '+a+' '+b+')'
def ITE(c,a,b):return '(ite '+c+' '+a+' '+b+')'
def solve(T,H=10,W=4,timeout=10000,wake=(513,519)):
 C=H*W;K=4*C;L=[f'(set-option :timeout {timeout})'];start=time.time()
 B=[[f'b{t}_{c}'for c in range(C)]for t in range(T+1)];Q=[[f'q{t}_{q}'for q in range(K)]for t in range(T+1)];F=[f'f{t}'for t in range(T+1)];S=[f's{t}'for t in range(T)]
 def add(s):L.append('(assert '+s+')')
 for t in range(T+1):
  L.extend('(declare-const '+v+' Bool)'for v in B[t]+Q[t]+[F[t]])
  add(OR(Q[t]));add('((_ at-most 1) '+' '.join(Q[t])+')')
 for s in S:L.append('(declare-const '+s+' Bool)')
 for q in range(K):
  if q//4//H!=W-1 or q%4!=1:add(NOT(Q[0][q]))
 for y in range(H):add(NOT(B[0][(W-1)*H+y]))
 for t in range(T):
  for q in range(K):
   c=q//4;x,y=c//H,c%H;h=q%4
   for black in(0,1):
    guard=AND([Q[t][q],B[t][c]if black else NOT(B[t][c])]);hh=(h+(-1 if black else 1))%4;dx,dy=D[hh];xx,yy=x+dx,y+dy
    if xx<0 or yy<0 or yy>=H:add(NOT(guard));continue
    shift=xx==W
    if shift:xx-=1
    qq=(xx*H+yy)*4+hh;add('(=> '+guard+' '+Q[t+1][qq]+')');add('(=> '+guard+' '+(S[t]if shift else NOT(S[t]))+')')
  add(EQ(F[t+1],XOR(F[t],S[t])));read=[OR(Q[t][4*c:4*c+4])for c in range(C)]
  for c in range(C):
   shifted=XOR(B[t][c+H],read[c+H])if c+H<C else'false'
   add(EQ(B[t+1][c],ITE(S[t],shifted,XOR(B[t][c],read[c]))))
  for phase in(0,1):
   mask=wake[phase^((W-1)%2)];guard=AND([S[t],F[t]if phase else NOT(F[t])])
   for y in range(H):add('(=> '+guard+' '+(B[t][y]if mask>>y&1 else NOT(B[t][y]))+')')
 add(EQ(F[T],F[0]));add(AND([EQ(a,b)for a,b in zip(B[T]+Q[T],B[0]+Q[0])]))
 add('(= (+ '+' '.join('(ite '+s+' 1 0)'for s in S)+') 8)')
 Z=Z3();answer=Z.run('\n'.join(L)+'\n(check-sat)').strip();r=dict(period=T,H=H,W=W,drift=8,wake=wake,status=answer,seconds=time.time()-start)
 if answer=='sat':
  names=B[0]+Q[0]+[F[0]];model=Z.run('(get-value ('+' '.join(names)+'))');v=dict(re.findall(r'\((\w+) (true|false)\)',model));board=sum(1<<c for c in range(C)if v[B[0][c]]=='true');q=next(q for q in range(K)if v[Q[0][q]]=='true');phase=int(v[F[0]]=='true');initial=(board,q,phase);word='';drift=0
  for t in range(T):
   c=q//4;x,y=c//H,c%H;h=q%4;b=bool(board>>c&1);word+='L'if b else'R';board^=1<<c;hh=(h+(-1 if b else 1))%4;dx,dy=D[hh];x+=dx;y+=dy;assert x>=0 and 0<=y<H
   if x==W:
    assert board&((1<<H)-1)==wake[phase^((W-1)%2)];drift+=1;phase^=1;board>>=H;x-=1
   q=(x*H+y)*4+hh
  assert(board,q,phase)==initial and drift==8;r.update(word=word,initial=initial)
 elif answer=='unknown':r['reason']=Z.run('(get-info :reason-unknown)')
 Z.close();return r
if __name__=='__main__':
 results=[]
 for T in(40,48,56,64,72,80,88,96,104,112,120,128):
  r=solve(T);results.append(r);print(r,flush=True);(P/'white_wake_search.json').write_text(json.dumps(results,indent=2))
  if r['status']=='sat':break
