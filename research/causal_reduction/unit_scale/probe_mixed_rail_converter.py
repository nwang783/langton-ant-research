"""One concrete constructive target, not an increasing period search.
Input: odd-x black row1. Output: solid rows0,2 and odd-x black row3.
Full drift(8,0), length32, five read rows, arbitrary backwards reach.
The complete drift-class chronology is constrained, not a finite time horizon.
UNSAT/UNKNOWN remain scoped solver controls, not independently signed theorems.
"""
import sys,json,time,re,pathlib
HERE=pathlib.Path(__file__).parent
sys.path.insert(0,str(HERE.parent/'morphic_candidates'))
from smt_inflation_refinement import Z3
N=32;D=8;H=5
A=lambda xs:'(and '+' '.join(xs)+')'
O=lambda xs:'(or '+' '.join(xs)+')'
E=lambda x,y:f'(= {x} {y})'
lines=['(set-option :timeout 60000)']
def put(s):lines.append('(assert '+s+')')
for t in range(N+1):
 for a in ('x','y','h'):lines.append(f'(declare-const {a}{t} Int)')
 put(A([f'(<= 0 h{t})',f'(< h{t} 4)',f'(<= 0 y{t})',f'(< y{t} {H})']))
for t in range(N):lines.append(f'(declare-const b{t} Bool)')
put(O([E('x0','0'),E('x0','1')]));put(E('h0','1'));put(E(f'x{N}',f'(+ x0 {D})'));put(E(f'y{N}','y0'));put(E(f'h{N}','h0'))
for t in range(N):
 put(E(f'h{t+1}',f'(mod (+ h{t} (ite b{t} 3 1)) 4)'))
 put(E(f'x{t+1}',f'(+ x{t} (ite (= h{t+1} 1) 1 (ite (= h{t+1} 3) (- 1) 0)))'))
 put(E(f'y{t+1}',f'(+ y{t} (ite (= h{t+1} 0) 1 (ite (= h{t+1} 2) (- 1) 0)))'))
 for j in range(N):
  lines.append(f'(declare-const e{t}_{j} Bool)')
  put(E(f'e{t}_{j}',A([E(f'y{t}',f'y{j}'),E(f'(mod x{t} {D})',f'(mod x{j} {D})')])) )
for t in range(N):
 inp=A([E(f'y{t}','1'),E(f'(mod x{t} 2)','1')])
 out=O([E(f'y{t}','0'),E(f'y{t}','2'),A([E(f'y{t}','3'),E(f'(mod x{t} 2)','1')])])
 earlier=[];allc=[]
 for j in range(N):
  allc.append(f'(ite e{t}_{j} 1 0)')
  earlier.append(f'(ite (and e{t}_{j} (< (- {D*j} (* {N} x{j})) (- {D*t} (* {N} x{t})))) 1 0)')
 par=lambda terms:E('(mod (+ '+' '.join(terms)+') 2)','1')
 put(E(f'b{t}',f'(xor {inp} {par(earlier)})'))
 put(E(out,f'(xor {inp} {par(allc)})'))
for y in (0,1,2,3):
 for x in range(D):
  if y in(1,3) and x%2==0:continue
  put(O([A([E(f'y{t}',str(y)),E(f'(mod x{t} {D})',str(x))])for t in range(N)]))
put(E('(+ '+' '.join(f'(ite b{t} (- 1) 1)'for t in range(N))+')','16'))
smt='\n'.join(lines);HERE.joinpath('mixed_rail_converter_n32.smt2').write_text(smt+'\n(check-sat)\n')
z=Z3();z.run(smt);st=time.monotonic();answer=z.run('(check-sat)').strip();out=dict(status=answer,seconds=time.monotonic()-st,scope=__doc__,length=N,drift=[D,0],height=H)
if answer=='sat':
 model=z.run('(get-value ('+' '.join([f'b{t}'for t in range(N)]+['x0','y0','h0'])+'))');out['model']=model
 vals=dict(re.findall(r'\((\w+) (true|false|\d+)\)',model));w=''.join('L'if vals[f'b{t}']=='true'else'R'for t in range(N));out['word']=w
elif answer=='unknown':out['reason']=z.run('(get-info :reason-unknown)')
z.close();HERE.joinpath('mixed_rail_converter_n32.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
