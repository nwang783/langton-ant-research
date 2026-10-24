"""Chronology of one exact minimum integer circulation from the H/LR/Q discovery target.
No claim about other incidence assignments or added read support.
"""
from pathlib import Path
import sys,json,collections,time,re
P=Path(__file__).resolve().parent
sys.path.insert(0,str(P.parent/'morphic_candidates'))
from smt_inflation_refinement import Z3
sys.path.insert(0,str(P.parents[1]/'periodic_classification_new'))
from synthesize_cap_three_cylinder import check_model
D=((0,1),(1,0),(0,-1),(-1,0))
control=len(sys.argv)>1 and sys.argv[1]=='H'
name='pipeline_fixed_flow_chronology_H_control'if control else'pipeline_fixed_flow_chronology'
flow=collections.Counter()
if control:
 import certify_short_refinement_rup as core
 H=json.loads((P/'short_refinement_scaffold_inputs.json').read_text())['H']
 for p,h,c in core.trace(H,(0,10),1)[0]:flow[(p[0]%2,p[1]-2*(p[0]//2)),h,c]+=1
else:
 j=json.loads((P/'pipeline_integer_flow.json').read_text())
 for e in j['flows']:flow[tuple(e['position']),e['heading'],e['turn']]=e['count']
ps=sorted({p for p,h,c in flow});ix={p:i for i,p in enumerate(ps)};ns=[sum(z for(p,h,c),z in flow.items()if p==q)for q in ps];period=sum(ns)
lines=['(set-logic QF_LIA)','(set-option :timeout 30000)','(set-option :produce-models true)']
def add(x):lines.append('(assert '+x+')')
def plus(xs):return '(+ '+' '.join(xs)+')'if xs else'0'
def pred(i,r,h,kind):
 axis=(1-sum(ps[i]))%2;g=h if kind=='i'else(h-(1 if r%2==0 else -1))%4
 assert g%2==axis
 return f'b{i}_{r}' if g==axis+2 else f'(not b{i}_{r})'
for i,p in enumerate(ps):
 for r in range(ns[i]):
  lines.extend([f'(declare-const b{i}_{r} Bool)',f'(declare-const t{i}_{r} Int)'])
  if r:add(f'(< t{i}_{r-1} t{i}_{r})')
 axis=(1-sum(p))%2
 for h in (axis,axis+2):
  for c in('R','L'):
   js=[r for r in range(ns[i])if ('R'if r%2==0 else'L')==c]
   add(f'(= {plus([f"(ite {pred(i,r,h,'i')} 1 0)"for r in js])} {flow[p,h,c]})')
 for kind in('i','o'):
  for h in range(4):
   if h%2!=(axis if kind=='i'else 1-axis):continue
   lines.append(f'(define-fun {kind}{i}_{h}_0 () Int 0)')
   for r in range(ns[i]):lines.append(f'(define-fun {kind}{i}_{h}_{r+1} () Int (+ {kind}{i}_{h}_{r} (ite {pred(i,r,h,kind)} 1 0)))')
add('(= t0_0 0)')
for i,p in enumerate(ps):
 axis=(1-sum(p))%2
 for h,(dx,dy) in enumerate(D):
  if h%2==axis:continue
  x,y=p[0]+dx,p[1]+dy;k=x//2;q=(x%2,y-2*k);z=ix.get(q)
  if z is None:add(f'(= o{i}_{h}_{ns[i]} 0)');continue
  add(f'(= o{i}_{h}_{ns[i]} i{z}_{h}_{ns[z]})')
  for r in range(ns[i]):
   for s in range(ns[z]):
    guard=f"(and {pred(i,r,h,'o')} {pred(z,s,h,'i')} (= o{i}_{h}_{r} i{z}_{h}_{s}))"
    add(f'(=> {guard} (= (+ t{z}_{s} {k*period}) (+ t{i}_{r} 1)))')
 for h,(dx,dy) in enumerate(D):
  if h%2!=axis:continue
  x,y=p[0]-dx,p[1]-dy;q=(x%2,y-2*(x//2))
  if q not in ix:add(f'(= i{i}_{h}_{ns[i]} 0)')
txt='\n'.join(lines)+'\n';(P/(name+'.smt2')).write_text(txt)
z=Z3();z.run(txt);t=time.monotonic();a=z.run('(check-sat)').strip();o=dict(scope=__doc__,status=a,seconds=time.monotonic()-t,period=period,counts=ns)
if a=='sat':
 names=[f'{p}{i}_{r}'for i in range(len(ps))for r in range(ns[i])for p in('b','t')]
 m=z.run('(get-value ('+' '.join(names)+'))');(P/(name+'.model')).write_text(m)
 bs={k:v=='true'for k,v in re.findall(r'\((b\d+_\d+) (true|false)\)',m)}
 ts={k:int(v)if neg==''else-int(v)for k,neg,v in re.findall(r'\((t\d+_\d+) (\(- )?(\d+)\)?\)',m)}
 vv=dict(P=period);ss=[]
 for i,p in enumerate(ps):
  axis=(1-sum(p))%2;hs=[axis+2*int(bs[f'b{i}_{r}'])for r in range(ns[i])];ss.append([('',[(1 if r%2==0 else-1,h)for r,h in enumerate(hs)])]);vv[f's{i}']=0
  for r in range(ns[i]):vv[f't{i}_{r}']=ts[f't{i}_{r}']
 o['certificate']=check_model(vv,ps,ss,(2,2));o['status']='SAT_REPLAYED'
if a=='unknown':o['reason']=z.run('(get-info :reason-unknown)')
z.close();(P/(name+'.json')).write_text(json.dumps(o,indent=2)+'\n');print(o)
