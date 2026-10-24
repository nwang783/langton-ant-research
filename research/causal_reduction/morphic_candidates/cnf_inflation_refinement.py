"""Explicit CNF refinement, with native DRAT production and bound DIMACS export."""
import ctypes,json,collections,pathlib,time
from smt_inflation_refinement import HERE,Z3,trace,rotate

def cnf_refinement(coarse,fixed,opts):
 names=[];clauses=[];cells=collections.defaultdict(dict)
 def var(name):names.append(name);return len(names)
 cv=[[var(f'c{i}_{j}')for j in range(len(opts[c]))]for i,c in enumerate(coarse)]
 for i,(x,y,h,c)in enumerate(trace(coarse)[0]):
  ws=opts[c];clauses.append(cv[i][:])
  for j in range(len(ws)):
   for k in range(j):clauses.append([-cv[i][j],-cv[i][k]])
  if i<len(fixed):clauses.append([cv[i][ws.index(fixed[i])]])
  for j,w in enumerate(ws):
   by=collections.defaultdict(str)
   for X,Y,H,z in trace(w)[0]:X,Y=rotate(X,Y,h);by[3*x+X,3*y+Y]+=z
   for p,s in by.items():cells[p].setdefault(i,['']*len(ws))[j]=s
 for cell,(p,vv)in enumerate(sorted(cells.items())):
  entries=sorted(vv.items());bv=[var(f'b{cell}_{z}')for z in range(len(entries)+1)]
  for z,(i,ss)in enumerate(entries):
   before,after=bv[z:z+2]
   for j,s in enumerate(ss):
    c=cv[i][j]
    if s:
     assert all(a!=b for a,b in zip(s,s[1:]));q=s[0]=='L';r=q^(len(s)%2==1)
     clauses.append([-c,before if q else-before]);clauses.append([-c,after if r else-after])
    else:clauses.append([-c,-before,after]);clauses.append([-c,before,-after])
 return names,clauses

def prove(coarse,fixed,opts,stem,timeout=30000):
 names,clauses=cnf_refinement(coarse,fixed,opts);outdir=HERE/'k9_drat';outdir.mkdir(exist_ok=True)
 C=ctypes.c_void_p;S=ctypes.c_char_p;Z=Z3();z=Z.z
 for name,types,ret in [('Z3_mk_tactic',[C,S],C),('Z3_mk_solver_from_tactic',[C,C],C),('Z3_solver_inc_ref',[C,C],None),('Z3_solver_from_string',[C,C,S],None),('Z3_solver_to_dimacs_string',[C,C,ctypes.c_bool],S),('Z3_solver_check',[C,C],ctypes.c_int),('Z3_global_param_set',[S,S],None),('Z3_mk_params',[C],C),('Z3_mk_string_symbol',[C,S],C),('Z3_params_set_bool',[C,C,C,ctypes.c_bool],None),('Z3_params_set_uint',[C,C,C,ctypes.c_uint],None),('Z3_tactic_using_params',[C,C,C],C),('Z3_tactic_inc_ref',[C,C],None),('Z3_params_inc_ref',[C,C],None)]:
  f=getattr(z,name);f.argtypes=types;f.restype=ret
 proof=outdir/(stem+'.drat');dim=outdir/(stem+'.cnf');z.Z3_global_param_set(b'sat.drat.file',str(proof).encode());z.Z3_global_param_set(b'sat.drat.binary',b'false');z.Z3_global_param_set(b'timeout',str(timeout).encode())
 
 for key in ('scc','scc.tr','elim_vars','elim_vars_bdd','asymm_branch','ate','probing','subsumption','dyn_sub_res','minimize_lemmas'):
  z.Z3_global_param_set(('sat.'+key).encode(),b'false')
 z.Z3_global_param_set(b'sat.simplify.delay',b'1000000000')
 t=z.Z3_mk_tactic(Z.ctx,b'sat');z.Z3_tactic_inc_ref(Z.ctx,t);par=z.Z3_mk_params(Z.ctx);z.Z3_params_inc_ref(Z.ctx,par)
 for key in ('scc','scc.tr','elim_vars','elim_vars_bdd','asymm_branch','ate','probing','probing_binary','probing_cache','subsumption','dyn_sub_res','minimize_lemmas','enable_pre_simplify','gc.defrag'):
  z.Z3_params_set_bool(Z.ctx,par,z.Z3_mk_string_symbol(Z.ctx,key.encode()),False)
 for key in ('simplify.delay','burst_search','gc.initial'):
  z.Z3_params_set_uint(Z.ctx,par,z.Z3_mk_string_symbol(Z.ctx,key.encode()),1000000000)
 t=z.Z3_tactic_using_params(Z.ctx,t,par);solver=z.Z3_mk_solver_from_tactic(Z.ctx,t);z.Z3_solver_inc_ref(Z.ctx,solver)
 def lit(x):return f'v{x}'if x>0 else f'(not v{-x})'
 smt='\n'.join([f'(declare-const v{i} Bool)'for i in range(1,len(names)+1)]+['(assert '+(lit(c[0])if len(c)==1 else'(or '+' '.join(map(lit,c))+')')+')'for c in clauses])
 z.Z3_solver_from_string(Z.ctx,solver,smt.encode());dump=z.Z3_solver_to_dimacs_string(Z.ctx,solver,True).decode()
 # Independently bind every exported literal to the explicit input CNF.
 mapping={};dumpclauses=[]
 for line in dump.splitlines():
  if line.startswith('c '):_,a,b=line.split();mapping[int(a)]=int(b[1:])
  elif not line.startswith('p ')and line.strip():dumpclauses.append(list(map(int,line.split()))[:-1])
 canon=lambda c:tuple(sorted(set(c)))
 assert collections.Counter(canon(c)for c in clauses)==collections.Counter(canon([(1 if a>0 else-1)*mapping[abs(a)]for a in c])for c in dumpclauses)
 dim.write_text(dump);start=time.time();status=z.Z3_solver_check(Z.ctx,solver);Z.close()
 return dict(status={-1:'unsat',0:'unknown',1:'sat'}[status],variables=len(names),clauses=len(clauses),seconds=time.time()-start,proof_bytes=proof.stat().st_size,cnf=str(dim),proof=str(proof))
if __name__=='__main__':
 O=next(z['images']for z in json.load(open(HERE/'free_inflations_k9.json'))['results']if z['scale']==[3,0]);ws=O['R']+O['L'];ids=list(map(int,open(HERE/'free_nine_coarse81_prefixes.csv').readline().split(',')));fixed=[ws[i]for i in ids]
 print(json.dumps(prove(''.join(fixed),fixed,O,'case0000'),indent=2))
