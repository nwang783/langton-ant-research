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
# One positive attempt with the phase order found by the first interval model.
order=[0,1,8,9,10,5,11,12,13,14,4,17,2,3,15,6,7,16]
from check_extremal_read_coupling import D
for c,b in zip(order,order[1:]+order[:1]):
 wrap=int(b==order[0]); ch=chains[c]; nxt=chains[b]
 (i,j),k=ch[-1]; t=levels[i]; h0=(H[t][j]+(1 if j%2==0 else-1))%4
 (ii,jj),kk=nxt[0]; tt=levels[ii];h1=H[tt][jj]
 # Distance from last named read to next named read, with both endpoint moves fixed.
 gap=f'(- (+ s{b} {wrap*P}) (+ s{c} {len(ch)-1}))'
 add(f'(>= {gap} 2)')
 for axis in (0,1):
  endpoint_a=((-t+3*k),k)[axis];endpoint_b=(-tt,0)[axis]
  const=endpoint_b-endpoint_a+wrap*(3,1)[axis]-D[h0][axis]-D[h1][axis]
  residual=f'(+ {const} (* {(3,1)[axis]} (- z{c} z{b})))'
  first_remaining_axis=(h0+1)%2 # headings parity0=vertical,1=horizontal
  starts_axis=(first_remaining_axis==(1 if axis==0 else 0))
  for sg in(-1,1):add(f'(>= {gap} (+ {2-int(starts_axis)} (* {2*sg} {residual})))')
add(f'(= x0 {levels[chains[0][0][0][0]]%2})');txt='\n'.join(lines)+'\n';(R/'return_debt_interval_calendar_travel.smt2').write_text(txt)
ctx=mkcontext(mkconfig());s=mksolver(ctx);inc(ctx,s);parse(ctx,s,txt.encode());st=time.time();ans=solve(ctx,s)
out={'scope':__doc__,'period_parameter':P,'status':{1:'SAT_NAMED_CLOCKS_ONLY',-1:'UNSAT_FOR_THIS_PROBE_ONLY',0:'UNKNOWN'}[ans],'seconds':time.time()-st,'histories':H,'chains':chains,'levels':levels}
if ans==1:out['model']=modelstr(ctx,getmodel(ctx,s)).decode()
if ans==0:out['reason']=reason(ctx,s).decode()
(R/'return_debt_interval_calendar_travel_result.json').write_text(json.dumps(out));print(out['status'],out['seconds'])
