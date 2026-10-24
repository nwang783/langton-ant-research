"""Exploratory max-plus bounding-box potential from exact residual token rules.
An UNSAT result only rejects this finite abstraction, not the trajectory theorem.
Uses installed system libz3 via ctypes, with no solver installation.
"""
import json,ctypes as C
from pathlib import Path
G=[{'endpoint':[1,1,0],'inputs':[[0,1]],'outputs':[[2,0]]},{'endpoint':[0,1,3],'inputs':[],'outputs':[[1,2],[2,0],[2,1]]},{'endpoint':[1,3,0],'inputs':[[0,3],[1,2]],'outputs':[[0,0],[0,1],[1,0],[2,0],[2,1],[2,2]]}];K=[0,1,2];T=[]
for line in open('dcv_resource_transfers_fuel20.log'):
 if line.startswith('EDGE '):
  a,x,y,b,u,v,h=map(int,line.split()[1:]);T.append({'producer':[a,G[a]['outputs'].index([x,y])],'consumer':[b,G[b]['inputs'].index([u,v])],'poses':[[0,0,h]]})
R=lambda p,h:complex(*p)*(-1j)**h
center=lambda h:complex(-1,1)*(-1j)**h
CC=['c%d'%h for h in range(4)]
U={(a,k,h):'u_%d_%d_%d'%(a,k,h)for a in K for k in range(len(G[a]['inputs']))for h in range(4)}
W={(a,k,h):'w_%d_%d_%d'%(a,k,h)for a in K for k in range(len(G[a]['outputs']))for h in range(4)}
S=['(set-logic QF_LIA)','(set-option :timeout 120000)','(set-option :produce-models true)','(set-option :produce-unsat-cores true)']
for v in CC+list(U.values())+list(W.values()):S.append('(declare-fun '+v+' () Int)')
assertions=[]
def add(s):
 name='A'+str(len(assertions));assertions.append(s);S.append('(assert (! '+s+' :named '+name+'))')
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
text='\n'.join(S)+'\n';Path('dcv_maxplus_observed.smt2').write_text(text)
LIB=C.CDLL('/usr/lib/x86_64-linux-gnu/libz3.so.4');ptr=C.c_void_p;cs=C.c_char_p
def fn(n,args,ret):
 f=getattr(LIB,'Z3_'+n);f.argtypes=args;f.restype=ret;return f
cfg=fn('mk_config',[],ptr)();ctx=fn('mk_context',[ptr],ptr)(cfg);sol=fn('mk_solver',[ptr],ptr)(ctx);fn('solver_inc_ref',[ptr,ptr],None)(ctx,sol);fn('solver_from_string',[ptr,ptr,cs],None)(ctx,sol,text.encode());r=fn('solver_check',[ptr,ptr],C.c_int)(ctx,sol)
out={'status':{1:'sat',0:'unknown',-1:'unsat'}[r],'scope':'CONDITIONAL ONLY: transfer alphabet observed in exhaustive mass<=20 controls, not proved complete.'}
if r==-1:
 core=fn('solver_get_unsat_core',[ptr,ptr],ptr)(ctx,sol);out['unsat_core']=fn('ast_vector_to_string',[ptr,ptr],cs)(ctx,core).decode();out['assertions']=assertions
if r==1:out['model']=fn('model_to_string',[ptr,ptr],cs)(ctx,fn('solver_get_model',[ptr,ptr],ptr)(ctx,sol)).decode()
if r==0:out['reason']=fn('solver_get_reason_unknown',[ptr,ptr],cs)(ctx,sol).decode()
Path('dcv_maxplus_observed.json').write_text(json.dumps(out,indent=2));print(out)
