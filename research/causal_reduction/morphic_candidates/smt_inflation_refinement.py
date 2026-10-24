"""Exact finite refinement via the installed Z3 C API. SAT prefixes are replayed.
UNSAT refers only to the supplied fixed coarse prefix; UNKNOWN is not exclusion.
"""
import ctypes,json,pathlib,time,collections,re,sys
from free_inflation_generic_csp import trace,rotate,seed
HERE=pathlib.Path(__file__).resolve().parent
class Z3:
 def __init__(self):
  self.z=ctypes.CDLL('libz3.so.4')
  self.z.Z3_mk_config.restype=ctypes.c_void_p
  self.z.Z3_mk_context.argtypes=[ctypes.c_void_p];self.z.Z3_mk_context.restype=ctypes.c_void_p
  self.z.Z3_eval_smtlib2_string.argtypes=[ctypes.c_void_p,ctypes.c_char_p];self.z.Z3_eval_smtlib2_string.restype=ctypes.c_char_p
  self.z.Z3_del_context.argtypes=[ctypes.c_void_p]
  cfg=self.z.Z3_mk_config();self.ctx=self.z.Z3_mk_context(cfg)
 def run(self,s):return self.z.Z3_eval_smtlib2_string(self.ctx,s.encode()).decode()
 def close(self):self.z.Z3_del_context(self.ctx)
def refinement(coarse,fixed,opts,timeout=30000,save=None):
 start=time.time();lines=[f'(set-option :timeout {timeout})'];N=len(coarse);cells=collections.defaultdict(dict)
 for i,(x,y,h,c)in enumerate(trace(coarse)[0]):
  ws=opts[c]
  for j in range(len(ws)):lines.append(f'(declare-const c{i}_{j} Bool)')
  lines.append('(assert (or '+' '.join(f'c{i}_{j}'for j in range(len(ws)))+'))')
  for j in range(len(ws)):
   for k in range(j):lines.append(f'(assert (or (not c{i}_{j}) (not c{i}_{k})))')
  if i<len(fixed):lines.append(f'(assert c{i}_{ws.index(fixed[i])})')
  for j,w in enumerate(ws):
   by=collections.defaultdict(str)
   for X,Y,H,z in trace(w)[0]:X,Y=rotate(X,Y,h);by[3*x+X,3*y+Y]+=z
   for p,s in by.items():cells[p].setdefault(i,['']*len(ws))[j]=s
 for cell,(p,vv)in enumerate(sorted(cells.items())):
  entries=sorted(vv.items())
  for z in range(len(entries)+1):lines.append(f'(declare-const b{cell}_{z} Bool)')
  for z,(i,ss)in enumerate(entries):
   before=f'b{cell}_{z}';after=f'b{cell}_{z+1}'
   for j,s in enumerate(ss):
    if s:
     assert all(a!=b for a,b in zip(s,s[1:]))
     q=s[0]=='L';r=q^(len(s)%2==1)
     guard=f'(and {before if q else "(not "+before+")"} {after if r else "(not "+after+")"})'
    else:guard=f'(= {before} {after})'
    lines.append(f'(assert (=> c{i}_{j} {guard}))')
 lines.append('(check-sat)');smt='\n'.join(lines)
 if save:(HERE/(save+'.smt2')).write_text(smt+'\n')
 Z=Z3();status=Z.run(smt).strip();out=dict(status=status,variables=N,cells=len(cells),fixed=len(fixed),timeout_ms=timeout,seconds=time.time()-start)
 if status=='sat':
  model=Z.run('(get-value ('+' '.join(f'c{i}_{j}'for i,c in enumerate(coarse)for j in range(len(opts[c])))+'))')
  choices=[None]*N
  for i,j in re.findall(r'\(c(\d+)_(\d+) true\)',model):choices[int(i)]=opts[coarse[int(i)]][int(j)]
  assert all(choices);word=''.join(choices);black=seed(word);assert black is not None and word[:N]==coarse
  fine=[(x,y,h)for x,y,h,c in trace(word)[0]]+[trace(word)[1]]
  for n,(x,y,h,c)in enumerate(trace(coarse)[0]):assert fine[9*n]==(3*x,3*y,h)
  out.update(choices=choices,word=word,seed=black,seed_size=len(black))
 elif status!='unsat':out['reason']=Z.run('(get-info :reason-unknown)')
 Z.close();return out
if __name__=='__main__':
 opts=next(z['images']for z in json.load(open(HERE/'free_inflations_k9.json'))['results']if z['scale']==[3,0]);best=json.load(open(HERE/'palette_inflations_9_9.json'))['best']['choices'];fixed=best[:9];coarse=''.join(fixed)
 timeout=int(sys.argv[1])if len(sys.argv)>1 else 30000
 out=refinement(coarse,fixed,opts,timeout,'k9_first_coarse81')
 (HERE/'smt_k9_first_coarse81.json').write_text(json.dumps(out,indent=2));print(json.dumps({k:v for k,v in out.items()if k not in('choices','word','seed')},indent=2))
