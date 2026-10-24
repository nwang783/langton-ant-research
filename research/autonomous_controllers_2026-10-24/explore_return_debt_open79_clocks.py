import sys,json,re
from pathlib import Path
R=Path('/workspace/shared/langton/autonomous_controllers_2026-10-24');sys.path[:0]=[str(R),str(R.parent/'periodic_classification_new')]
from probe_one_a_local_constraints import mkconfig,mkcontext,mksolver,inc,parse,solve,getmodel,modelstr,reason
from partial_drift31_graph import graph
H={int(t):tuple(h)for t,h in json.load(open(R/'drift31_middle_short_T12_discovery.json'))['states'][8].items()};levels=sorted(H);kind,G=graph([H[t]for t in levels],levels);assert kind=='open';P=10002
lines=['(set-logic QF_LIA)','(set-option :timeout 30000)','(set-option :produce-models true)'];N=[]
def add(x):lines.append('(assert '+x+')')
for t,hs in sorted(H.items()):
 for j in range(len(hs)):
  n=f't{t}_{j}';lines.append(f'(declare-fun {n} () Int)');add(f'(= (mod {n} 4) {t%2})');N.append(n)
  if j:add(f'(>= (- {n} t{t}_{j-1}) 4)')
for ch in G['chains']:
 for((i,j),k),((a,b),l)in zip(ch,ch[1:]):add(f'(= (+ t{levels[i]}_{j} 1) (+ t{levels[a]}_{b} {(l-k)*P}))')
add('(distinct '+' '.join(f'(mod {n} {P})'for n in N)+')');add('(= t0_0 0)')
ctx=mkcontext(mkconfig());s=mksolver(ctx);inc(ctx,s);txt='\n'.join(lines);parse(ctx,s,txt.encode());status=solve(ctx,s);print('status',status)
if status==1:
 model=modelstr(ctx,getmodel(ctx,s)).decode();print(model[:200]);(R/'return_debt_open79_model.txt').write_text(model);(R/'return_debt_open79.smt2').write_text(txt)
 (R/'return_debt_open79_discovery.json').write_text(json.dumps({'scope':'Explicit positive OPEN clock model only; not a board factor or controller. No solver exhaustion.','period_parameter':P,'histories':H,'model':model,'graph':G}))
elif status==0:print(reason(ctx,s))
