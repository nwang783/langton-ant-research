"""Exploratory max-plus bounding-box potential from exact residual token rules.
An UNSAT result only rejects this finite abstraction, not the trajectory theorem.
Uses installed system libz3 via ctypes, with no solver installation.
"""
import json,ctypes as C
from pathlib import Path
J=json.load(open('dcv_residual_core_resources.json'));G=J['geometry'];K=J['kept_packet_types'];T=[]
for line in open('dcv_packet_transfers_fuel20.log'):
 if line.startswith('EDGE '):
  a,x,y,b,u,v,h=map(int,line.split()[1:])
  if a in K and b in K:T.append({'producer':[a,G[a]['outputs'].index([x,y])],'consumer':[b,G[b]['inputs'].index([u,v])],'poses':[[0,0,h]]})
R=lambda p,h:complex(*p)*(-1j)**h
center=lambda h:complex(-1,1)*(-1j)**h
CC=['c%d'%h for h in range(4)]
U={(a,k,h):'u_%d_%d_%d'%(a,k,h)for a in K for k in range(len(G[a]['inputs']))for h in range(4)}
W={(a,k,h):'w_%d_%d_%d'%(a,k,h)for a in K for k in range(len(G[a]['outputs']))for h in range(4)}
S=['(set-logic QF_LIA)','(set-option :timeout 120000)','(set-option :produce-models true)','(set-option :produce-unsat-cores true)']
for v in CC+list(U.values())+list(W.values()):S.append('(declare-fun '+v+' () Int)')
assertions=[]
def add(s):
 assertions.append(s);S.append('(assert '+s+')')
def plus(n,v):return v if n==0 else '(+ '+str(n)+' '+v+')'
add('(= c0 0)')
for e in T:
 a,k=e['producer'];b,j=e['consumer']
 for hr in {p[2]for p in e['poses']}:
  for hs in range(4):add('(<= '+U[b,j,(hs+hr)%4]+' '+W[a,k,hs]+')')
for a in K:
 E=G[a]['endpoint'];dh=E[2]
 for h in range(4):
  cy=int(center(h).imag)
  old=[CC[h]]+[plus(2*int(R(p,h).imag)-cy,U[a,k,h])for k,p in enumerate(G[a]['inputs'])]
  end=2*R(E[:2],h)+center((h+dh)%4)-center(h)
  new=[plus(int(end.imag),CC[(h+dh)%4])]+[plus(2*int(R(p,h).imag)-cy,W[a,k,h])for k,p in enumerate(G[a]['outputs'])]
  for q in new:add('(or '+' '.join('(<= '+q+' '+v+')'for v in old)+')')
# Prefer admitting unclassified transfers, but never weaken observed transfers.
protected={tuple(map(int,l.split()[:7]))for l in open('dcv_protected_patch2_kernel.tsv')}
soft=0
for e in J['transfer_edges']:
 a,k=e['producer'];b,j=e['consumer'];q=G[a]['outputs'][k]
 for x,y,hr in e['poses']:
  if (a,b,x,y,hr,*q)in protected:continue
  terms=['(<= '+U[b,j,(h+hr)%4]+' '+W[a,k,h]+')'for h in range(4)]
  S.append('(assert-soft (and '+' '.join(terms)+') :weight 1 :id transfers)');soft+=1
S.append('(declare-fun bound () Int)')
for name in CC+list(U.values())+list(W.values()):add('(and (<= '+name+' bound) (<= (- '+name+') bound))')
S.append('(minimize bound)')
text='\n'.join(S)+'\n';Path('dcv_packet_maxplus_optimized.smt2').write_text(text)
LIB=C.CDLL('/usr/lib/x86_64-linux-gnu/libz3.so.4');ptr=C.c_void_p;cs=C.c_char_p
def fn(n,args,ret):
 f=getattr(LIB,'Z3_'+n);f.argtypes=args;f.restype=ret;return f
cfg=fn('mk_config',[],ptr)();ctx=fn('mk_context',[ptr],ptr)(cfg);sol=fn('mk_optimize',[ptr],ptr)(ctx);fn('optimize_inc_ref',[ptr,ptr],None)(ctx,sol);fn('optimize_from_string',[ptr,ptr,cs],None)(ctx,sol,text.encode());r=fn('optimize_check',[ptr,ptr,C.c_uint,ptr],C.c_int)(ctx,sol,0,None)
out={'status':{1:'sat',0:'unknown',-1:'unsat'}[r],'scope':'CONDITIONAL ONLY: observed marked mass<=20 transfer alphabet, not proved complete.'}
if r==1:
 model=fn('optimize_get_model',[ptr,ptr],ptr)(ctx,sol);out['model']=fn('model_to_string',[ptr,ptr],cs)(ctx,model).decode();out['values']={}
 sort=fn('mk_int_sort',[ptr],ptr)(ctx)
 for name in CC+list(U.values())+list(W.values()):
  sym=fn('mk_string_symbol',[ptr,cs],ptr)(ctx,name.encode());ast=fn('mk_const',[ptr,ptr,ptr],ptr)(ctx,sym,sort);value=ptr();assert fn('model_eval',[ptr,ptr,ptr,C.c_bool,C.POINTER(ptr)],C.c_bool)(ctx,model,ast,True,C.byref(value));out['values'][name]=int(fn('get_numeral_string',[ptr,ptr],cs)(ctx,value).decode())
if r==0:out['reason']=fn('optimize_get_reason_unknown',[ptr,ptr],cs)(ctx,sol).decode()
Path('dcv_packet_maxplus_optimized.json').write_text(json.dumps(out,indent=2));print(out)
