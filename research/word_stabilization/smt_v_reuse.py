"""Exact bounded physical macro synthesis, using system libz3 through ctypes.
No solver installation. Bitvector coordinates are safe for n < 250 (12-bit).
Every returned word is independently replayed by verify_macro_word.check.
"""
import ctypes as C, json, sys, time, re
from pathlib import Path
from verify_macro_word import D, check
LIB=C.CDLL('/usr/lib/x86_64-linux-gnu/libz3.so.4')
def fn(n,args,ret):
 f=getattr(LIB,'Z3_'+n);f.argtypes=args;f.restype=ret;return f
ptr=C.c_void_p;cs=C.c_char_p
mkconfig=fn('mk_config',[],ptr);setpar=fn('set_param_value',[ptr,cs,cs],None)
mkcontext=fn('mk_context',[ptr],ptr);mksolver=fn('mk_solver',[ptr],ptr)
inc=fn('solver_inc_ref',[ptr,ptr],None);parse=fn('solver_from_string',[ptr,ptr,cs],None)
solve=fn('solver_check',[ptr,ptr],C.c_int);getmodel=fn('solver_get_model',[ptr,ptr],ptr)
modelstr=fn('model_to_string',[ptr,ptr],cs);reason=fn('solver_get_reason_unknown',[ptr,ptr],cs)

def bv(n,w=12):return f'(_ bv{n%(1<<w)} {w})'
def conj(a):return 'true' if not a else a[0] if len(a)==1 else '(and '+' '.join(a)+')'
def disj(a):return 'false' if not a else a[0] if len(a)==1 else '(or '+' '.join(a)+')'
def eq(a,b):return f'(= {a} {b})'
def ite(c,a,b):return f'(ite {c} {a} {b})'
def choice(i,a):
 r=a[-1]
 for k in reversed(range(4)):r=ite(eq(f'k{i}',bv(k,3)),a[k],r)
 return r

def make(n,timeout,mode='raw'):
 assert 2<=n<250
 max_step=max(abs(v) for a in D.values() for v in a["end_pose"][:2])
 max_read=max(abs(v) for a in D.values() for z in a["trace"] for v in z["p"])
 assert (n-1)*max_step+max_read < (1<<11), "coordinate wrap risk"
 out=['(set-logic QF_AUFBV)',f'(set-option :timeout {timeout})','(set-option :produce-models true)']
 add=lambda s:out.append('(assert '+s+')')
 for i in range(n+1):
  for v,w in [('x',12),('y',12),('h',2)]:out.append(f'(declare-fun {v}{i} () (_ BitVec {w}))')
  out.append(f'(declare-fun b{i} () (Array (_ BitVec 24) Bool))')
 for i in range(n):out.append(f'(declare-fun k{i} () (_ BitVec 3))');add(f'(bvult k{i} {bv(5,3)})')
 for v in 'xyh':add(eq(f'{v}{n-1}',bv(0,2 if v=='h' else 12)))
 add(eq(f'k{n-1}',bv(2,3)))
 names='CUVQB'; touched=[]
 def local(i,x,y):
  xx=ite(eq(f'h{i}',bv(0,2)),bv(x),ite(eq(f'h{i}',bv(1,2)),bv(y),ite(eq(f'h{i}',bv(2,2)),bv(-x),bv(-y))))
  yy=ite(eq(f'h{i}',bv(0,2)),bv(y),ite(eq(f'h{i}',bv(1,2)),bv(-x),ite(eq(f'h{i}',bv(2,2)),bv(-y),bv(x))))
  return f'(bvadd x{i} {xx})',f'(bvadd y{i} {yy})'
 for i in range(n):
  bs=[];xs=[];ys=[];hs=[]
  for k,name in enumerate(names):
   d=D[name];first={};odd=set()
   for z in d['trace']:
    p=tuple(z['p']);first.setdefault(p,z['c']);odd.symmetric_difference_update([p])
   guard=[];hits=[];pnames={}
   for j,(p,c) in enumerate(first.items()):
    xx,yy=local(i,*p);v=f'p{i}_{k}_{j}';out.append(f'(define-fun {v} () (_ BitVec 24) (concat {xx} {yy}))');pnames[p]=v
    guard.append(eq(f'(select b{i} {v})','true' if c=='L' else 'false'))
    hits.append(eq(v,f'(concat {bv(1)} {bv(2)})'))
   add(f'(=> (= k{i} {bv(k,3)}) {conj(guard)})')
   if i<n-1:touched.append(conj([eq(f'k{i}',bv(k,3)),disj(hits)]))
   b=f'b{i}'
   for p in sorted(odd):
    v=pnames[p];b=f'(store {b} {v} (not (select b{i} {v})))'
   bs.append(b);xx,yy=local(i,*d['end_pose'][:2]);xs.append(xx);ys.append(yy);hs.append(f'(bvadd h{i} {bv(d["end_pose"][2],2)})')
  for v,a in [('b',bs),('x',xs),('y',ys),('h',hs)]:add(eq(f'{v}{i+1}',choice(i,a)))
 add(disj(touched))
 # All exact short grammar restrictions. They are redundant with physical arrays.
 allowed={'UU':[0],'UV':[0,1,2],'UQ':[0],'UB':[0],'VU':[0],'VV':[0,1,2],'VQ':[0],'VB':[],
          'QU':[0],'QV':[0,1,2],'QQ':[],'QB':[],'BU':[0],'BV':[0,1,2],'BQ':[0],'BB':[]}
 forbidden=['CCCCC']
 for a in 'UVQB':
  for b in 'UVQB':
   for k in range(4):
    if k not in allowed[a+b]:forbidden.append(a+'C'*k+b)
 for a in 'UVQB':forbidden.append('CCCC'+a)
 for w in forbidden:
  for i in range(n-len(w)+1):add('(not '+conj([eq(f'k{i+j}',bv(names.index(c),3)) for j,c in enumerate(w)])+')')
 if mode=='ports':
  ports=json.load(open(Path(__file__).with_name('minimized_actual_ports.json')))
  for i in range(n+1):out.append(f'(declare-fun s{i} () (_ BitVec 7))')
  edges=ports['transitions'] if 'transitions' in ports else ports['edges']
  for i in range(n):
   terms=[]
   for edge in edges:
    if isinstance(edge,dict):a,c,b=edge['source'],edge['label'],edge['target']
    else:a,c,b=edge
    terms.append(conj([eq(f's{i}',bv(a,7)),eq(f'k{i}',bv(names.index(c),3)),eq(f's{i+1}',bv(b,7))]))
   add(disj(terms))
 return '\n'.join(out)+'\n'

def main():
 n=int(sys.argv[1]);timeout=int(sys.argv[2]) if len(sys.argv)>2 else 30000;mode=sys.argv[3] if len(sys.argv)>3 else 'raw'
 code=make(n,timeout,mode);stem=Path(__file__).with_name(f'smt_v_reuse_{n}_{mode}');stem.with_suffix('.smt2').write_text(code)
 cfg=mkconfig();ctx=mkcontext(cfg);solver=mksolver(ctx);inc(ctx,solver);parse(ctx,solver,code.encode());start=time.time();ans=solve(ctx,solver)
 print('RESULT',n,mode,ans,'elapsed',time.time()-start,flush=True)
 if ans==0:print('UNKNOWN',reason(ctx,solver).decode(),flush=True)
 if ans==1:
  m=modelstr(ctx,getmodel(ctx,solver)).decode();stem.with_suffix('.model').write_text(m)
  found={int(i):int(v,2) for i,v in re.findall(r'k(\d+) -> #b([01]+)',m)}
  if len(found)!=n:
   print('MODEL PARSE NEEDED',m[:1000]);return
  w=''.join('CUVQB'[found[i]] for i in range(n));r=check(w)
  assert r['blocks'][-1]['target_previous'] is not None
  stem.with_suffix('.json').write_text(json.dumps(r,indent=2));print('PHYSICALLY VERIFIED',w,r['fuel'],r['blocks'][-1]['target_previous'],flush=True)
if __name__=='__main__':main()
