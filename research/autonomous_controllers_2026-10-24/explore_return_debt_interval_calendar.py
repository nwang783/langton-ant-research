#!/usr/bin/env python3
"""One supplied OPEN79 positive clock probe using whole-chain occupied intervals.
A SAT model is named-clock compatibility only, not physical outside completion.
"""
import sys,json,time
from pathlib import Path
R=Path(__file__).resolve().parent;sys.path.insert(0,str(R.parent/'periodic_classification_new'))
from probe_one_a_local_constraints import mkconfig,mkcontext,mksolver,inc,parse,solve,getmodel,modelstr,reason
from partial_drift31_graph import graph
H={t:tuple('NESW'.index(c)for c in s)for t,s in enumerate(['S','W','S','EEWE','SSNS','EEWE','NNNSS','EEEWW','NNSNSSSS','WWWEWW','SNSSSN','WEEEEEEWWEEEWEWE','SSNNNSNSSSSSSSSSSS'])}|{-3:(),-2:(),-1:()}
levels=sorted(H);kind,G=graph([H[t]for t in levels],levels);assert kind=='open';P=10002;chains=G['chains'];where={};lines=['(set-logic QF_LIA)','(set-option :timeout 30000)','(set-option :produce-models true)']
def add(x):lines.append('(assert '+x+')')
for c,ch in enumerate(chains):
 phase=levels[ch[0][0][0]]%2
 for name in('x','s','z'):lines.append(f'(declare-fun {name}{c} () Int)')
 add(f'(= x{c} (+ s{c} (* {P} z{c})))');add(f'(and (<= 0 s{c}) (<= s{c} {P-len(ch)}))');add(f'(= (mod x{c} 4) {phase})')
 for a,((i,j),k)in enumerate(ch):where[levels[i],j]=(c,a,k)
 for cc,old in enumerate(chains[:c]):add(f'(or (<= (+ s{c} {len(ch)}) s{cc}) (<= (+ s{cc} {len(old)}) s{c}))')
for t,hs in H.items():
 for j in range(len(hs)-1):
  u,a,ka=where[t,j];v,b,kb=where[t,j+1];add(f'(>= (- x{v} x{u}) {4+a-b+(kb-ka)*P})')
add(f'(= x0 {levels[chains[0][0][0][0]]%2})');txt='\n'.join(lines)+'\n';(R/'return_debt_interval_calendar.smt2').write_text(txt)
ctx=mkcontext(mkconfig());s=mksolver(ctx);inc(ctx,s);parse(ctx,s,txt.encode());st=time.time();ans=solve(ctx,s)
out={'scope':__doc__,'period_parameter':P,'status':{1:'SAT_NAMED_CLOCKS_ONLY',-1:'UNSAT_FOR_THIS_PROBE_ONLY',0:'UNKNOWN'}[ans],'seconds':time.time()-st,'histories':H,'chains':chains,'levels':levels}
if ans==1:out['model']=modelstr(ctx,getmodel(ctx,s)).decode()
if ans==0:out['reason']=reason(ctx,s).decode()
(R/'return_debt_interval_calendar_result.json').write_text(json.dumps(out));print(out['status'],out['seconds'])
