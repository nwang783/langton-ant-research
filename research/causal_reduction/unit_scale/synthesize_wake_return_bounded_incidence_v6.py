"""All-period chronology in the fixed13-row prepared104 wake cylinder.
Per-site caps and P<=224 are supplied by exact rational dual certificates of
an UNBOUNDED-count incidence relaxation. No arbitrary visit cap is imposed.
No physical cap/finite-seed connection follows even from a successful model.
"""
from pathlib import Path
import sys,json,time
P=Path(__file__).resolve().parent
sys.path.insert(0,str(P.parents[1]/'periodic_classification_new'))
from probe_one_a_local_constraints import D,mkconfig,mkcontext,mksolver,inc,parse,solve,getmodel,modelstr,reason,conj
from synthesize_axis_compact_clock import values
from synthesize_cap_three_cylinder import check_model
W=set(map(tuple,json.loads((P/'shifted_reverse104_bulk.json').read_text())['wake_black_classes']))
def make(timeout=300000,massdelta=None,control=False):
 cert=json.loads((P/'wake_return_flow_bounds_h13_off-4.json').read_text());ps=list(map(tuple,cert['positions']));ix={p:i for i,p in enumerate(ps)};caps=[r['integer_upper']for r in cert['bounds'][1:]];pmax=cert['bounds'][0]['integer_upper'];B=[int((x-y,x%2)in W)for x,y in ps]
 sector=0 if control else 1
 fixed={}
 if control:
  import ast
  z=json.loads((P/'wake_return_compact_cap10_h13_sector0.json').read_text())['certificate_normalized']['classes']
  fixed={(ast.literal_eval(q)[0],ast.literal_eval(q)[1]-4):tuple(map(int,v['kind']))for q,v in z.items()}
  caps=[len(fixed.get(p,()))for p in ps];pmax=104
 axis=lambda i:(sector-sum(ps[i]))%2
 lines=['(set-logic QF_UFLRA)',f'(set-option :timeout {timeout})','(set-option :produce-models true)','(declare-fun P () Real)','(declare-fun epsilon () Real)','(assert (> epsilon 0))']
 add=lambda s:lines.append('(assert '+s+')')
 def port(i,j,h,kind):
  incoming=h if kind=='i'else(h-(1 if(j+B[i])%2==0 else-1))%4
  assert incoming%2==axis(i)
  b=f'b{i}_{j}';return b if incoming==axis(i)+2 else f'(not {b})'
 for i,p in enumerate(ps):
  cap=caps[i];lines.append(f'(declare-fun n{i} () Real)');add('(or '+' '.join(f'(= n{i} {j})' for j in range(cap+1))+')')
  for j in range(cap):
   lines.extend((f'(declare-fun b{i}_{j} () Bool)',f'(declare-fun t{i}_{j} () Real)'));add(f'(=> (<= n{i} {j})(not b{i}_{j}))')
   if j:add(f'(=> (> n{i} {j})(>= t{i}_{j} (+ t{i}_{j-1} (* 4 epsilon))))')
  for kind in('i','o'):
   for h in range(4):
    if h%2!=(axis(i)if kind=='i'else 1-axis(i)):continue
    lines.append(f'(define-fun {kind}{i}_{h}_0 () Real 0)')
    for j in range(cap):lines.append(f'(define-fun {kind}{i}_{h}_{j+1} () Real (+ {kind}{i}_{h}_{j} (ite(and(> n{i} {j}) {port(i,j,h,kind)})1 0)))')
 add('(= P (+ '+' '.join(f'n{i}'for i in range(len(ps)))+'))');add('(or '+' '.join(f'(= P {j})' for j in range(4,pmax+1,4))+')')
 add('(or '+' '.join(f'(and(> n{i} 0)(= t{i}_0 0))'for i,c in enumerate(caps)if c)+')')
 if massdelta is not None:
  add('(<= (+ '+' '.join(f'(ite (> n{i} {j}) {1 if (j+B[i])%2==0 else -1} 0)'for i in range(len(ps))for j in range(caps[i]))+f') {massdelta})')
 for p,i in ix.items():
  for h,(ax,ay)in enumerate(D):
   if h%2==1-axis(i):
    x,y=p[0]+ax,p[1]+ay;k=x//2;v=-k;q=(x%2,y-2*k);z=ix.get(q)
    if z is None:add(f'(= o{i}_{h}_{caps[i]} 0)');continue
    add(f'(= o{i}_{h}_{caps[i]} i{z}_{h}_{caps[z]})')
    lines.append(f'(declare-fun T{i}_{h} (Real) Real)')
    for j in range(caps[i]):
     g=conj([f'(> n{i} {j})',port(i,j,h,'o')])
     add(f'(=> {g}(= (T{i}_{h} o{i}_{h}_{j}) t{i}_{j}))')
    for k in range(caps[z]):
     g=conj([f'(> n{z} {k})',port(z,k,h,'i')])
     add(f'(=> {g}(= (T{i}_{h} i{z}_{h}_{k}) (- (+ t{z}_{k} {v}) epsilon)))')
   else:
    xx=p[0]-ax;q=(xx%2,p[1]-ay-2*(xx//2))
    if q not in ix:add(f'(= i{i}_{h}_{caps[i]} 0)')
 # Explicit total seam winding1, equivalently displacement(-2,-2).
 for ax in range(2):
  terms=[]
  for i,p in enumerate(ps):
   for h in range(4):
    if h%2==1-axis(i)and D[h][ax]:
     term=f'o{i}_{h}_{caps[i]}'
     terms.append(term if D[h][ax]==1 else f'(- {term})')
  add('(= (+ '+' '.join(terms)+') -2)')
 if not control:
  # Exact aggregate count bounds imply local heading/turn restrictions.
  for rec in json.loads((P/'wake_return_individual_count_bounds.json').read_text())['bounds']:
   i,h,c=rec['key'];terms=[]
   for j in range(caps[i]):
    turn=1 if(j+B[i])%2==0 else -1
    if turn==c:terms.append(f'(ite(and(> n{i} {j}) {port(i,j,h,"i")})1 0)')
   if terms:add('(<= (+ '+' '.join(terms)+f') {rec["integer_upper"]})')
  # Constructive top-contact branch: the unique potential read at(1,-1).
  # No required-contact branch or selected output; all read subsets remain.
 else:
  for i,p in enumerate(ps):
   hs=fixed.get(p,());add(f'(= n{i} {len(hs)})')
   for j,h in enumerate(hs):add(f'(= b{i}_{j} '+('true' if h==axis(i)+2 else 'false')+')')
 return '\n'.join(lines)+'\n',ps,caps,B

def run(timeout=300000,massdelta=None,control=False):
 txt,ps,caps,B=make(timeout,massdelta,control);name=P/f'wake_return_complete_h13_mass{massdelta}_full_v6_realuf_control{int(control)}';name.with_suffix('.smt2').write_text(txt)
 ctx=mkcontext(mkconfig());sol=mksolver(ctx);inc(ctx,sol);parse(ctx,sol,txt.encode());st=time.monotonic();ans=solve(ctx,sol)
 out=dict(scope=__doc__,mass_delta_at_most=massdelta,branch='fixed inverse104 positive control' if control else 'all read subsets and outputs; exact real-UF ordinal clocks',positions=ps,caps=caps,status={1:'SAT_PENDING_REPLAY',-1:'UNSAT_FIXED_STRIP_SOLVER_ONLY',0:'UNKNOWN'}[ans],seconds=time.monotonic()-st)
 if ans==1:
  mt=modelstr(ctx,getmodel(ctx,sol)).decode();name.with_suffix('.model').write_text(mt);v=values(mt);vv={'P':int(v['P'])};ss=[]
  for i,p in enumerate(ps):
   n=int(v[f'n{i}']);axis=((0 if control else 1)-sum(p))%2;hs=[axis+2*int(v[f'b{i}_{j}'])for j in range(n)];hist=[(1 if(j+B[i])%2==0 else-1,h)for j,h in enumerate(hs)]
   ss.append([(''.join(map(str,hs)),hist)]);vv[f's{i}']=0
   for j in range(n):assert (v[f't{i}_{j}']/v['epsilon']).denominator==1;vv[f't{i}_{j}']=int(v[f't{i}_{j}']/v['epsilon'])
  assert v['epsilon']*vv['P']==1;out['epsilon']=str(v['epsilon']);out['certificate']=check_model(vv,ps,ss,(-2,-2));out['status']='SAT_RECONSTRUCTED_BULK_INPUT'
 if ans==0:out['reason']=reason(ctx,sol).decode()
 name.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out),flush=True);return out
if __name__=='__main__':
 run(30000,None,True)
 run()
