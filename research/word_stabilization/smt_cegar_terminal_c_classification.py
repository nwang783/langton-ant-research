"""Displacement-constrained counterexample search, never an all-length proof."""
import sys,time,json,re
from pathlib import Path
from smt_terminal_c_reuse import make,mkconfig,mkcontext,mksolver,inc,parse,solve,getmodel,modelstr,reason,eq,bv,conj
from verify_macro_word import check,rot
ROOT=Path(__file__).parent;names='CUVQB'
def forbidden(w,n):
 return '\n'.join('(assert (not '+conj([eq(f'k{i+j}',bv(names.index(c),3))for j,c in enumerate(w)])+'))'for i in range(n-len(w)+1))
def main():
 n=int(sys.argv[1]);k=0;timeout=int(sys.argv[2])if len(sys.argv)>2 else 30000
 code=make(n,timeout)
 code='\n'.join(s for s in code.splitlines()if not any(a in s for a in['(select b','(declare-fun b','(assert (= b']))
 learned={}
 for file in ['smt_cegar_folds_v_learned.json','smt_cegar_v_learned.json','smt_cegar_completed_c_learned.json','smt_cegar_terminal_c_learned.json']:
  p=ROOT/file
  if p.exists():learned.update(json.load(open(p)))
 for w in json.load(open(ROOT/'literal_short_grammar_8.json'))['forbidden']:learned.setdefault(w,{'source':'literal_short_grammar_8'})
 for w in learned:
  try:check(w)
  except AssertionError:pass
  else:raise AssertionError(('invalid learned factor',w))
 for w in learned:code+='\n'+forbidden(w,n)
 # Exclude only these terminal suffixes, not their feasible interior occurrences.
 for r in range(n):
  for w in [('V'*(r+1)+'CC'+'V'*(r+1)+'C'),('U'+'V'*r+'CC'+'V'*(r+1)+'C')]:
   if len(w)<=n:
    code+='\n(assert (not '+conj([eq(f'k{n-len(w)+j}',bv(names.index(c),3))for j,c in enumerate(w)])+'))'
 cfg=mkconfig();ctx=mkcontext(cfg);solver=mksolver(ctx);inc(ctx,solver);parse(ctx,solver,code.encode());start=time.time()
 stem=ROOT/f'smt_terminal_c_classification_{n}';stem.with_suffix('.smt2').write_text(code)
 for loop in range(100000):
  if time.time()-start>240:print('WALL CAP',n,loop,flush=True);break
  ans=solve(ctx,solver)
  if ans!=1:
   print('RESULT',n,k,ans,'iterations',loop,'seconds',time.time()-start,'reason',reason(ctx,solver).decode()if ans==0 else'',flush=True);break
  m=modelstr(ctx,getmodel(ctx,solver)).decode();found={int(i):int(v,2)for i,v in re.findall(r'k(\d+) -> #b([01]+)',m)};assert len(found)==n
  w=''.join(names[found[i]]for i in range(n))
  try:r=check(w)
  except AssertionError as e:
   j,a,t,q,old,c=e.args[0];bad=w[old[2]:j+1]
   assert bad not in learned,(w,bad)
   try:check(bad)
   except AssertionError as ee:conf=ee.args[0]
   else:raise AssertionError(('invalid learned conflict',bad))
   learned[bad]={'conflict':conf,'source_word':w};parse(ctx,solver,forbidden(bad,n).encode())
   if loop%25==0:print('REFINE',n,k,loop,bad,'seconds',round(time.time()-start,2),flush=True)
   continue
  j=n-k-1;b=r['blocks'][j];px,py,h=b['pose'];dx,dy=rot((-1,0),h);q=(px+dx,py+dy)
  prior=[t for t in r['trace']if t[4]<j and tuple(t[1:3])==q]
  assert w[0]!='C'and w[j-1]!='C'and w[j:]=='C'and prior
  r['terminal_C_marker']={'index':j,'site':q,'prior':prior}
  stem.with_suffix('.json').write_text(json.dumps(r,indent=2));print('PHYSICALLY VERIFIED',w,'fuel',r['fuel'],'prior',prior,flush=True);break
 (ROOT/'smt_cegar_terminal_c_learned.json').write_text(json.dumps(learned,indent=2))
if __name__=='__main__':main()
