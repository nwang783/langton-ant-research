from pathlib import Path
import ctypes as C,json,time
R=Path(__file__).resolve().parent
lines=(R/'unlocked_potential.smt2').read_text().splitlines();S=['(set-option :produce-unsat-cores true)'];clauses={};i=0
for line in lines:
 if line.startswith('(assert '):
  clauses[f'a{i}']=line[8:-1];line='(assert (! '+line[8:-1]+f' :named a{i}'+'))';i+=1
 S.append(line)
L=C.CDLL('/usr/lib/x86_64-linux-gnu/libz3.so.4');p=C.c_void_p;s=C.c_char_p
def f(n,a,r):
 x=getattr(L,'Z3_'+n);x.argtypes=a;x.restype=r;return x
cfg=f('mk_config',[],p)();ctx=f('mk_context',[p],p)(cfg);sol=f('mk_solver',[p],p)(ctx);f('solver_inc_ref',[p,p],None)(ctx,sol);f('solver_from_string',[p,p,s],None)(ctx,sol,'\n'.join(S).encode());assert f('solver_check',[p,p],C.c_int)(ctx,sol)==-1
core=f('solver_get_unsat_core',[p,p],p)(ctx,sol);n=f('ast_vector_size',[p,p],C.c_uint)(ctx,core);rows=[]
for j in range(n):
 a=f('ast_vector_get',[p,p,C.c_uint],p)(ctx,core,j);name=f('ast_to_string',[p,p],s)(ctx,a).decode();rows.append({'name':name,'clause':clauses[name]})
(R/'unsat_core.json').write_text(json.dumps(dict(scope='Contradictory clauses of a conservative local ansatz, not an actual ant word.',clauses=rows),indent=2)+'\n')
print(json.dumps(dict(count=n,rows=rows),indent=2))
