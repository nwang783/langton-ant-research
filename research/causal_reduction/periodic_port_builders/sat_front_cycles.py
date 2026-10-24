"""Bounded periodic-front synthesis on an infinite periodic input.
SAT models are literally replayed in the exact frontier transducer; UNSAT here
is a solver result, not a separately proof-certified exclusion.
"""
import json,pathlib,sys,time,re
HERE=pathlib.Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'morphic_candidates'))
from smt_inflation_refinement import Z3
D=((0,1),(1,0),(0,-1),(-1,0))
def OR(xs):return '(or '+' '.join(xs)+')'
def NOT(x):return '(not '+x+')'
def AND(xs):return '(and '+' '.join(xs)+')'
def EQ(x,y):return '(= '+x+' '+y+')'
def XOR(x,y):return '(xor '+x+' '+y+')'
def ITE(c,a,b):return '(ite '+c+' '+a+' '+b+')'
def solve(H=10,W=4,T=64,masks=(0,819),timeout=5000):
 cells=H*W;ports=4*cells;lines=[f'(set-option :timeout {timeout})']
 B=[[f'b_{t}_{c}'for c in range(cells)]for t in range(T+1)]
 P=[f'p_{t}'for t in range(T+1)];F=[f'f_{t}'for t in range(T+1)];S=[f's_{t}'for t in range(T)]
 def add(x):lines.append('(assert '+x+')')
 for t in range(T+1):
  lines.extend(f'(declare-const {b} Bool)'for b in B[t]);lines.append(f'(declare-const {P[t]} Int)');lines.append(f'(declare-const {F[t]} Bool)');add(AND([f'(<= 0 {P[t]})',f'(< {P[t]} {ports})']))
 for s in S:lines.append(f'(declare-const {s} Bool)')
 add(OR([EQ(P[0],str(((W-1)*H+y)*4+1))for y in range(H)]))
 for y in range(H):add(EQ(B[0][(W-1)*H+y],ITE(F[0],str(bool(masks[1]>>y&1)).lower(),str(bool(masks[0]>>y&1)).lower())))
 for t in range(T):
  shifts=[]
  for p in range(ports):
   c=p//4;x,y=c//H,c%H;h=p%4
   for black in(0,1):
    guard=AND([EQ(P[t],str(p)),B[t][c]if black else NOT(B[t][c])]);hh=(h+(-1 if black else 1))%4;dx,dy=D[hh];xx,yy=x+dx,y+dy
    if xx<0 or yy<0 or yy>=H:add(NOT(guard));continue
    shift=xx>=W
    if shift:xx-=1;shifts.append(guard)
    q=(xx*H+yy)*4+hh;add(f'(=> {guard} {EQ(P[t+1],str(q))})')
  add(EQ(S[t],OR(shifts)));add(EQ(F[t+1],XOR(F[t],S[t])))
  read=[OR([EQ(P[t],str(4*c+h))for h in range(4)])for c in range(cells)]
  for c in range(cells):
   same=XOR(B[t][c],read[c]);src=c+H
   if src<cells:shifted=XOR(B[t][src],read[src])
   else:
    y=c%H;shifted=ITE(F[t+1],str(bool(masks[1]>>y&1)).lower(),str(bool(masks[0]>>y&1)).lower())
   add(EQ(B[t+1][c],ITE(S[t],shifted,same)))
 Z=Z3();out=Z.run('\n'.join(lines));assert not out.strip(),out;results=[]
 for period in range(4,T+1,4):
  guards=[EQ(F[period],F[0]),EQ(P[period],P[0]),OR(S[:period])]+[EQ(B[period][c],B[0][c])for c in range(cells)]
  start=time.time();answer=Z.run('(push)\n(assert '+AND(guards)+')\n(check-sat)').strip();r=dict(period=period,status=answer,seconds=time.time()-start)
  if answer=='sat':
   model=Z.run('(get-value ('+' '.join(B[0]+[P[0],F[0]])+'))');vals=dict(re.findall(r'\((\w+) (true|false|\d+)\)',model));board=sum(1<<c for c in range(cells)if vals[B[0][c]]=='true');p=int(vals[P[0]]);phase=int(vals[F[0]]=='true');initial=(board,p,phase);word='';drift=0
   for t in range(period):
    c=p//4;x,y=c//H,c%H;h=p%4;black=bool(board>>c&1);word+='L'if black else'R';board^=1<<c;hh=(h+(-1 if black else 1))%4;dx,dy=D[hh];x+=dx;y+=dy;assert x>=0 and 0<=y<H
    if x==W:drift+=1;phase^=1;x-=1;board=(board>>H)|(masks[phase]<<(H*(W-1)))
    p=(x*H+y)*4+hh
   assert (board,p,phase)==initial and drift>0;r.update(word=word,drift=drift,initial=initial)
  elif answer=='unknown':r['reason']=Z.run('(get-info :reason-unknown)')
  results.append(r);print(r,flush=True);Z.run('(pop)')
  if answer=='sat':break
 Z.close();return dict(H=H,W=W,T=T,input_masks=masks,results=results)
if __name__=='__main__':
 out=solve();(HERE/'three_band_sat_fronts.json').write_text(json.dumps(out,indent=2))
