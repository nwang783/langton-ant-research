"""Exact bounded V-tip-reuse CEGAR: symbolic geometry, literal color refinement.
Every learned factor has an independently replayable same-cell flip conflict.
UNSAT after such refinements is a valid bounded exclusion, never all-length.
"""
import sys,time,json,re
from pathlib import Path
from smt_v_lastwriter import make,mkconfig,mkcontext,mksolver,inc,parse,solve,getmodel,modelstr,reason,eq,bv,conj
from verify_macro_word import check
from smt_fold_lemmas import constraints
ROOT=Path(__file__).parent
names='CUVQB'
def modelword(m,n):
 found={int(i):int(v,2) for i,v in re.findall(r'k(\d+) -> #b([01]+)',m)}
 assert len(found)==n,(len(found),m[:500])
 return ''.join(names[found[i]] for i in range(n))
def forbidden(w,n):
 return '\n'.join('(assert (not '+conj([eq(f'k{i+j}',bv(names.index(c),3)) for j,c in enumerate(w)])+'))' for i in range(n-len(w)+1))
def main():
 n=int(sys.argv[1]);timeout=int(sys.argv[2]) if len(sys.argv)>2 else 60000;limit=int(sys.argv[3]) if len(sys.argv)>3 else 100000
 mode=sys.argv[4] if len(sys.argv)>4 else 'raw'
 code=make(n,timeout,mode)
 code='\n'.join(s for s in code.splitlines() if not any(a in s for a in ['(select b','(declare-fun b','(assert (= b']))
 code+='\n'+constraints(n)
 decl='\n'.join(f'(declare-fun k{i} () (_ BitVec 3))' for i in range(n))
 file=ROOT/'smt_cegar_folds_v_learned.json';learned=json.loads(file.read_text()) if file.exists() else {}
 for w in learned:
  try:check(w)
  except AssertionError:pass
  else:raise AssertionError(("persisted factor is feasible",w))
 for w in learned:code+='\n'+forbidden(w,n)
 cfg=mkconfig();ctx=mkcontext(cfg);solver=mksolver(ctx);inc(ctx,solver);parse(ctx,solver,code.encode());start=time.time()
 (ROOT/f'smt_cegar_folds_v_{n}_{mode}.smt2').write_text(code)
 for loop in range(limit):
  ans=solve(ctx,solver)
  if ans!=1:
   print('RESULT',n,mode,ans,'iterations',loop,'elapsed',time.time()-start, 'reason', reason(ctx,solver).decode() if ans==0 else '',flush=True);break
  m=modelstr(ctx,getmodel(ctx,solver)).decode();w=modelword(m,n)
  try:r=check(w)
  except AssertionError as e:
   j,k,t,q,old,c=e.args[0];bad=w[old[2]:j+1]
   assert bad not in learned,(w,bad)
   try:check(bad);assert False
   except AssertionError as ee:conf=ee.args[0]
   learned[bad]={'conflict':conf,'source_word':w}
   parse(ctx,solver,(forbidden(bad,n)).encode())
   if loop%10==0:print('REFINE',n,loop,'learned',len(learned),'new',bad,'word',w,'elapsed',round(time.time()-start,2),flush=True)
   if loop%100==0:file.write_text(json.dumps(learned,indent=2))
   continue
  assert r['blocks'][-1]['target_previous'] is not None
  (ROOT/f'smt_cegar_v_counterexample_{n}.json').write_text(json.dumps(r,indent=2));print('PHYSICALLY VERIFIED',w,r['fuel'],flush=True);break
 else:print('ITERATION CAP',n,limit,flush=True)
 file.write_text(json.dumps(learned,indent=2))
if __name__=='__main__':main()
