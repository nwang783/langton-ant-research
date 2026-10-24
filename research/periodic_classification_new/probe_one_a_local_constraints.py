#!/usr/bin/env python3
"""Exact local necessary constraints, no time or period bound.
UNSAT would exclude the one-A pattern via a finite neighborhood. SAT only
provides a locally consistent open-boundary patch, NOT an ant orbit.
Uses the already installed libz3 through ctypes; installs nothing.
"""
import ctypes as C,json,sys,time
from pathlib import Path
D=((0,1),(1,0),(0,-1),(-1,0))
LIB=C.CDLL('/usr/lib/x86_64-linux-gnu/libz3.so.4')
def fn(n,args,ret):
 f=getattr(LIB,'Z3_'+n);f.argtypes=args;f.restype=ret;return f
ptr=C.c_void_p;cs=C.c_char_p
mkconfig=fn('mk_config',[],ptr);mkcontext=fn('mk_context',[ptr],ptr);mksolver=fn('mk_solver',[ptr],ptr)
inc=fn('solver_inc_ref',[ptr,ptr],None);parse=fn('solver_from_string',[ptr,ptr,cs],None)
solve=fn('solver_check',[ptr,ptr],C.c_int);getmodel=fn('solver_get_model',[ptr,ptr],ptr)
modelstr=fn('model_to_string',[ptr,ptr],cs);reason=fn('solver_get_reason_unknown',[ptr,ptr],cs)
def disj(xs):return 'false' if not xs else xs[0] if len(xs)==1 else '(or '+' '.join(xs)+')'
def conj(xs):return 'true' if not xs else xs[0] if len(xs)==1 else '(and '+' '.join(xs)+')'
def states(p):
 axis=1 if sum(p)%2==0 else 0
 out=[('0',[])]
 for h in [axis,(axis+2)%4]:
  out += [('R'+str(h),[(1,h)]),('D'+str(h),[(1,h),(-1,h)]),('S'+str(h),[(1,h),(-1,(h+2)%4)]),('A'+str(h),[(1,h),(-1,h),(1,(h+2)%4)]),('B'+str(h),[(1,h),(-1,(h+2)%4),(1,(h+2)%4)])]
 return out
def make(r,timeout):
 ps=[(x,y) for x in range(-r,r+1) for y in range(-r,r+2)];ix={p:i for i,p in enumerate(ps)}; ss=[states(p) for p in ps]
 lines=['(set-logic QF_LIA)',f'(set-option :timeout {timeout})','(set-option :produce-models true)']
 def add(x):lines.append('(assert '+x+')')
 for i,p in enumerate(ps):
  lines.append(f'(declare-fun s{i} () Int)');add(f'(and (<= 0 s{i}) (< s{i} 11))')
  for j in range(3):lines.append(f'(declare-fun t{i}_{j} () Int)')
  add(f'(< t{i}_0 t{i}_1)');add(f'(< t{i}_1 t{i}_2)')
 # Every active event is globally distinct. It is harmless to keep inactive
 # placeholders distinct too, because the unbounded integers admit insertion.
 add('(distinct '+' '.join(f't{i}_{j}' for i in range(len(ps)) for j in range(3))+')')
 for p,name in [((0,0),'S3'),((0,1),'A0'),((-1,1),'D3')]:
  i=ix[p];k=[a for a,h in ss[i]].index(name);add(f'(= s{i} {k})')
 add(f'(= t{ix[(0,1)]}_0 0)')
 for p,i in ix.items():
  for out_h in range(4):
   # The fixed sector directs vertical edges out of even cells, horizontal
   # edges out of odd cells. Opposite directions on one axis are both allowed.
   if out_h%2 != sum(p)%2:continue
   dx,dy=D[out_h];q=p[0]+dx,p[1]+dy
   if q not in ix:continue
   k=ix[q]
   po=[[j for j,(c,h) in enumerate(hist) if (h+c)%4==out_h] for _,hist in ss[i]]
   qi=[[j for j,(c,h) in enumerate(hist) if h==out_h] for _,hist in ss[k]]
   opts=[]
   for a,oi in enumerate(po):
    for b,ij in enumerate(qi):
     if len(oi)!=len(ij):continue
     opts.append(conj([f'(= s{i} {a})',f'(= s{k} {b})']+[f'(= t{k}_{y} (+ t{i}_{x} 1))' for x,y in zip(oi,ij)]))
   add(disj(opts))
 return '\n'.join(lines)+'\n',ps,ss
if __name__=='__main__':
 r=int(sys.argv[1]) if len(sys.argv)>1 else 2
 timeout=int(sys.argv[2]) if len(sys.argv)>2 else 30000
 text,ps,ss=make(r,timeout)
 base=Path(__file__).with_name('one_a_local_r'+str(r));base.with_suffix('.smt2').write_text(text)
 cfg=mkconfig();ctx=mkcontext(cfg);sol=mksolver(ctx);inc(ctx,sol);parse(ctx,sol,text.encode());start=time.time();ans=solve(ctx,sol)
 result={'radius':r,'cells':len(ps),'timeout_ms':timeout,'result':{1:'SAT_LOCAL_ONLY',-1:'UNSAT_LOCAL',0:'UNKNOWN'}[ans],'seconds':time.time()-start}
 if ans==1:base.with_suffix('.model').write_text(modelstr(ctx,getmodel(ctx,sol)).decode())
 if ans==0:result['reason']=reason(ctx,sol).decode()
 base.with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True)
