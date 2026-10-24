"""Conditional DCUV max-plus discovery using only the new profile and literal controls."""
from pathlib import Path
import json,ctypes as C,sys,hashlib
ROOT=Path(__file__).resolve().parents[1];P=ROOT/'core_periodicity_new/chronology_dcuv';profile=json.loads((P/'profile_recurrent8.json').read_text());G=json.loads(Path(profile['files']['geometry']['path']).read_text())['geometry'];K=profile['keep'];inventory=json.loads((P/'transfer_inventory.json').read_text());rows=[e for e in inventory['protected_survivors']if e['tuple'][0]in K and e['tuple'][1]in K];byrow={tuple(r['tuple']):r for r in inventory['ordinary_survivors']};observed=Path(sys.argv[1])if len(sys.argv)>1 else P/'observed_transfers_depth5.tsv';prefix=Path(sys.argv[2])if len(sys.argv)>2 else P/'potential_free_direction_depth5';mode=sys.argv[3]if len(sys.argv)>3 else 'optimize'
CC=[f'c{h}'for h in range(4)];U={(a,k,h):f'u_{a}_{k}_{h}'for a in K for k in range(len(G[a]['inputs']))for h in range(4)};W={(a,k,h):f'w_{a}_{k}_{h}'for a in K for k in range(len(G[a]['outputs']))for h in range(4)};names=CC+list(U.values())+list(W.values())+['ax','ay'];S=['(set-logic QF_LIA)','(set-option :timeout 120000)','(set-option :produce-models true)'];S+=['(declare-fun '+n+' () Int)'for n in names]
def add(x):S.append('(assert '+x+')')
def rot(z,h):x,y=z;return[(x,y),(y,-x),(-x,-y),(-y,x)][h%4]
def lin(z):return f'(+ (* ax {z[0]}) (* ay {z[1]}))'
def off(z,v):return f'(+ {lin(z)} {v})'
add('(= c0 0)');old=json.loads((ROOT/'word_stabilization/dcv_free_direction_family102.json').read_text())['values']
for name in names:
 if name in old:add(f'(= {name} {old[name]})')
if mode=='feasible13':add('(and (= ax 1) (= ay 3))')
add('(and (<= 0 ax) (<= ax 16) (<= 0 ay) (<= ay 16) (>= (+ ax ay) 1))')
observed_rows=[tuple(map(int,l.split()))for l in observed.read_text().splitlines()];observed_rows=[r for r in observed_rows if r[0]in K and r[1]in K]
for row in observed_rows:
 e=byrow[row];a,b,x,y,hr,*q=row;k=e['source_output_slot'];j=e['target_input_slot']
 for h in range(4):add(f'(<= {U[b,j,(h+hr)%4]} {W[a,k,h]})')
checks=0
for a in K:
 g=G[a];dh=g['endpoint'][2]
 for h in range(4):
  anchor=rot((-1,1),h);old=[CC[h]]
  for k,p in enumerate(g['inputs']):
   z=rot(p,h);old.append(off((2*z[0]-anchor[0],2*z[1]-anchor[1]),U[a,k,h]))
  e=rot(g['endpoint'][:2],h);center=rot((-1,1),h+dh);new=[off((2*e[0]+center[0]-anchor[0],2*e[1]+center[1]-anchor[1]),CC[(h+dh)%4])]
  for k,p in enumerate(g['outputs']):
   z=rot(p,h);new.append(off((2*z[0]-anchor[0],2*z[1]-anchor[1]),W[a,k,h]))
  for q in new:add('(or '+' '.join('(<= '+q+' '+v+')'for v in old)+')');checks+=1
for e in (rows if mode=='optimize'else[]):
 a,b,x,y,hr,*q=e['tuple'];k=e['source_output_slot'];j=e['target_input_slot'];terms=[f'(<= {U[b,j,(h+hr)%4]} {W[a,k,h]})'for h in range(4)];S.append('(assert-soft (and '+' '.join(terms)+') :weight 1 :id transfers)')
S.append('(declare-fun bound () Int)')
for n in names:add(f'(and (<= {n} bound) (<= (- {n}) bound))')

if mode=='optimize':S.append('(minimize bound)')
else:add('(<= bound 1000)')
text='\n'.join(S)+'\n';prefix.with_suffix('.smt2').write_text(text)
LIB=C.CDLL('/usr/lib/x86_64-linux-gnu/libz3.so.4');ptr=C.c_void_p;cs=C.c_char_p
def fn(n,args,ret):f=getattr(LIB,'Z3_'+n);f.argtypes=args;f.restype=ret;return f
cfg=fn('mk_config',[],ptr)();ctx=fn('mk_context',[ptr],ptr)(cfg);sol=fn('mk_optimize',[ptr],ptr)(ctx);fn('optimize_inc_ref',[ptr,ptr],None)(ctx,sol);params=fn('mk_params',[ptr],ptr)(ctx);fn('params_inc_ref',[ptr,ptr],None)(ctx,params);symbol=fn('mk_string_symbol',[ptr,cs],ptr)(ctx,b'timeout');fn('params_set_uint',[ptr,ptr,ptr,C.c_uint],None)(ctx,params,symbol,120000);fn('optimize_set_params',[ptr,ptr,ptr],None)(ctx,sol,params);fn('optimize_from_string',[ptr,ptr,cs],None)(ctx,sol,text.encode());r=fn('optimize_check',[ptr,ptr,C.c_uint,ptr],C.c_int)(ctx,sol,0,None)
out={'kept_packet_types':K,'fixed_dcv_parameters':True,'status':{1:'sat',0:'unknown',-1:'unsat'}[r],'scope':'CONDITIONAL DISCOVERY ONLY; DCUV profile relations need their own signoff, all unproved transfer inequalities remain obligations. No DCV clauses imported.','variables':len(names),'local_inequalities':checks,'soft_transfer_rows':len(rows),'observed_controls':len(observed_rows),'observed_file':str(observed),'observed_sha256':hashlib.sha256(observed.read_bytes()).hexdigest(),'profile_sha256':hashlib.sha256((P/'profile_recurrent8.json').read_bytes()).hexdigest()}
if r==1:
 model=fn('optimize_get_model',[ptr,ptr],ptr)(ctx,sol);out['model']=fn('model_to_string',[ptr,ptr],cs)(ctx,model).decode();out['values']={};sort=fn('mk_int_sort',[ptr],ptr)(ctx)
 for n in names:
  sym=fn('mk_string_symbol',[ptr,cs],ptr)(ctx,n.encode());ast=fn('mk_const',[ptr,ptr,ptr],ptr)(ctx,sym,sort);value=ptr();assert fn('model_eval',[ptr,ptr,ptr,C.c_bool,C.POINTER(ptr)],C.c_bool)(ctx,model,ast,True,C.byref(value));out['values'][n]=int(fn('get_numeral_string',[ptr,ptr],cs)(ctx,value).decode())
 out['direction']=[out['values']['ax'],out['values']['ay']]
if r==0:out['reason']=fn('optimize_get_reason_unknown',[ptr,ptr],cs)(ctx,sol).decode()
prefix.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items()if k not in['model','values']},indent=2))
