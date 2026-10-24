"""Attempt a max-plus rank on exact two-packet residual transfers. Experimental."""
import json,ctypes as C,sys,time
from pathlib import Path
J=json.load(open('dcv_compound_resources.json'));G=J['compounds'];T=J['transfer_edges'];R=lambda p,h:complex(*p[:2])*(-1j)**h;center=lambda h:complex(-1,1)*(-1j)**h
CC=['c%d'%h for h in range(4)];U={(a,k,h):'u_%d_%d_%d'%(a,k,h) for a,g in enumerate(G) for k in range(len(g['inputs'])) for h in range(4)};W={(a,k,h):'w_%d_%d_%d'%(a,k,h) for a,g in enumerate(G) for k in range(len(g['outputs'])) for h in range(4)}
S=['(set-logic QF_LIA)','(set-option :timeout '+str(int(sys.argv[1]) if len(sys.argv)>1 else 180000)+')','(set-option :produce-models true)']
for v in CC+list(U.values())+list(W.values()):S.append('(declare-fun '+v+' () Int)')
def add(s):S.append('(assert '+s+')')
def plus(n,v):return v if n==0 else '(+ '+str(n)+' '+v+')'
add('(= c0 0)')
for a,k,b,j,x,y,hr in T:
 for h in range(4):add('(<= '+U[b,j,(h+hr)%4]+' '+W[a,k,h]+')')
for a,g in enumerate(G):
 e=g['endpoint'];dh=e[2]
 for h in range(4):
  cy=int(center(h).imag);old=[CC[h]]+[plus(2*int(R(p,h).imag)-cy,U[a,k,h]) for k,p in enumerate(g['inputs'])];end=2*R(e,h)+center((h+dh)%4)-center(h);new=[plus(int(end.imag),CC[(h+dh)%4])]+[plus(2*int(R(p,h).imag)-cy,W[a,k,h]) for k,p in enumerate(g['outputs'])]
  for q in new:add('(or '+' '.join('(<= '+q+' '+v+')' for v in old)+')')
text='\n'.join(S)+'\n';Path('dcv_compound_maxplus.smt2').write_text(text);print('START variables',len(CC)+len(U)+len(W),'assertions',sum(s.startswith('(assert') for s in S),flush=True)
LIB=C.CDLL('/usr/lib/x86_64-linux-gnu/libz3.so.4');ptr=C.c_void_p;cs=C.c_char_p
def fn(n,args,ret):
 f=getattr(LIB,'Z3_'+n);f.argtypes=args;f.restype=ret;return f
cfg=fn('mk_config',[],ptr)();ctx=fn('mk_context',[ptr],ptr)(cfg);sol=fn('mk_solver',[ptr],ptr)(ctx);fn('solver_inc_ref',[ptr,ptr],None)(ctx,sol);fn('solver_from_string',[ptr,ptr,cs],None)(ctx,sol,text.encode());r=fn('solver_check',[ptr,ptr],C.c_int)(ctx,sol)
out={'status':{1:'sat',0:'unknown',-1:'unsat'}[r],'scope':'Exploratory two-packet rank with inherited ordinary and protected transfer exclusions.'}
if r==1:
 model=fn('solver_get_model',[ptr,ptr],ptr)(ctx,sol);out['model']=fn('model_to_string',[ptr,ptr],cs)(ctx,model).decode();out['values']={};sort=fn('mk_int_sort',[ptr],ptr)(ctx)
 for name in CC+list(U.values())+list(W.values()):
  sym=fn('mk_string_symbol',[ptr,cs],ptr)(ctx,name.encode());ast=fn('mk_const',[ptr,ptr,ptr],ptr)(ctx,sym,sort);value=ptr();assert fn('model_eval',[ptr,ptr,ptr,C.c_bool,C.POINTER(ptr)],C.c_bool)(ctx,model,ast,True,C.byref(value));out['values'][name]=int(fn('get_numeral_string',[ptr,ptr],cs)(ctx,value).decode())
if r==0:out['reason']=fn('solver_get_reason_unknown',[ptr,ptr],cs)(ctx,sol).decode()
Path('dcv_compound_maxplus.json').write_text(json.dumps(out,indent=2));print(out['status'],out.get('reason',''),flush=True)
