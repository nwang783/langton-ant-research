"""One finite core/unlocked-token max-potential feasibility check.
All transfer constraints are a conservative literal/HB superset; this is not
trajectory search. Locked U stars are omitted from both production tracking
and later consumption, and rigid U east-pair transfer is enforced.
"""
from pathlib import Path
import json,hashlib,ctypes as C,time
R=Path(__file__).resolve().parent;W=R.parent
GP=W/'chronology_dcuv/literal_residual_geometry.json';HP=W/'chronology_dcuv/protected_patch2.tsv'
G=json.loads(GP.read_text())['geometry'];IDS=(0,1,4,5,6,7,8,9)
HB={tuple(map(int,l.split()[:7]))for l in HP.read_text().splitlines()}
LOCK={(0,0),(0,1),(1,0),(1,1)};EAST={(2,0),(2,1)}
def rot(q,h):
 x,y=q;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def sub(a,b):return a[0]-b[0],a[1]-b[1]
def locked(a,q):return a in(7,8,9)and tuple(q)in LOCK
CC=[f'c{h}'for h in range(4)]
IN={(a,k,h):f'i_{a}_{k}_{h}'for a in IDS for k in range(len(G[a]['inputs']))for h in range(4)}
OUT={(a,k,h):f'o_{a}_{k}_{h}'for a in IDS for k,q in enumerate(G[a]['outputs'])if not locked(a,q)for h in range(4)}
names=CC+list(IN.values())+list(OUT.values())
S=['(set-logic QF_LIA)','(set-option :timeout 120000)','(set-option :produce-models true)']
S +=[f'(declare-fun {n} () Int)'for n in names]
def add(t):S.append('(assert '+t+')')
def off(q,n):return f'(+ {2*(q[0]+3*q[1])} {n})'
add('(= c0 0)')
transfers=[];excluded=dict(locked=0,sector=0,HB=0,east_port=0)
for a in IDS:
 for oi,q in enumerate(G[a]['outputs']):
  if locked(a,q):excluded['locked']+=1;continue
  q=tuple(q)
  for b in IDS:
   for ik,i in enumerate(G[b]['inputs']):
    for hr in range(4):
     p=sub(q,rot(i,hr))
     if(sum(p)+hr)%2:excluded['sector']+=1;continue
     if(a,b,*p,hr,*q)in HB:excluded['HB']+=1;continue
     if a in(7,8,9)and q in EAST:
      if not(b in(7,8)and p==(3,-1)and hr==0 and tuple(i)==((-1,1)if q==(2,0)else(-1,2))):excluded['east_port']+=1;continue
     row=(a,oi,b,ik,*p,hr);transfers.append(row)
     for h in range(4):add(f'(<= {IN[b,ik,(h+hr)%4]} {OUT[a,oi,h]})')
local=[]
for a in IDS:
 g=G[a];dx,dy,dh=g['endpoint']
 for h in range(4):
  old=[CC[h]]+[off(rot(p,h),IN[a,k,h])for k,p in enumerate(g['inputs'])]
  new=[('core',off(rot((dx,dy),h),CC[(h+dh)%4]))]
  new +=[(k,off(rot(p,h),OUT[a,k,h]))for k,p in enumerate(g['outputs'])if not locked(a,p)]
  for role,q in new:
   add('(or '+' '.join(f'(<= {q} {v})'for v in old)+')')
   local.append((a,h,role))
text='\n'.join(S)+'\n';(R/'unlocked_potential.smt2').write_text(text)
LIB=C.CDLL('/usr/lib/x86_64-linux-gnu/libz3.so.4');ptr=C.c_void_p;cs=C.c_char_p

def fn(n,args,ret):
 f=getattr(LIB,'Z3_'+n);f.argtypes=args;f.restype=ret;return f
cfg=fn('mk_config',[],ptr)();ctx=fn('mk_context',[ptr],ptr)(cfg)
sol=fn('mk_solver',[ptr],ptr)(ctx);fn('solver_inc_ref',[ptr,ptr],None)(ctx,sol)
fn('solver_from_string',[ptr,ptr,cs],None)(ctx,sol,text.encode())
t0=time.time();status=fn('solver_check',[ptr,ptr],C.c_int)(ctx,sol)
out=dict(status={1:'SAT_CONDITIONAL_LOCAL_CERTIFICATE',0:'UNKNOWN_LOCAL_ANSATZ',-1:'UNSAT_LOCAL_ANSATZ'}[status],elapsed_seconds=time.time()-t0,variables=len(names),transfer_rows=len(transfers),local_clauses=len(local),excluded=excluded,direction=(1,3),transfer_scope='Literal all-heading output/input matches, signed universal HB exclusions, signed U-star permanence and rigid east-port rule. No DCV-only relation imported across U.',not_claimed='Infeasibility is not physical nonreachability. No actual trajectory or confinement claim without independent certificate review.',dependencies={str(p.relative_to(W)):hashlib.sha256(p.read_bytes()).hexdigest()for p in(GP,HP,W/'U_left_star_permanence_frozen_20261023_1918/manifest.json',W/'causal_cycle_renewal_20261023_1841/manifest.json',Path(__file__).resolve())})
if status==1:
 model=fn('solver_get_model',[ptr,ptr],ptr)(ctx,sol);out['model']=fn('model_to_string',[ptr,ptr],cs)(ctx,model).decode();out['values']={};sort=fn('mk_int_sort',[ptr],ptr)(ctx)
 for n in names:
  sym=fn('mk_string_symbol',[ptr,cs],ptr)(ctx,n.encode());ast=fn('mk_const',[ptr,ptr,ptr],ptr)(ctx,sym,sort);val=ptr();assert fn('model_eval',[ptr,ptr,ptr,C.c_bool,C.POINTER(ptr)],C.c_bool)(ctx,model,ast,True,C.byref(val));out['values'][n]=int(fn('get_numeral_string',[ptr,ptr],cs)(ctx,val).decode())
 # Exact integer recheck of every clause, independent of solver arithmetic.
 v=out['values']
 for a,oi,b,ik,x,y,hr in transfers:
  for h in range(4):assert v[IN[b,ik,(h+hr)%4]]<=v[OUT[a,oi,h]]
 for a in IDS:
  g=G[a];dx,dy,dh=g['endpoint']
  for h in range(4):
   old=[v[CC[h]]]+[2*sum((rot(p,h)[0],3*rot(p,h)[1]))+v[IN[a,k,h]]for k,p in enumerate(g['inputs'])]
   new=[2*(rot((dx,dy),h)[0]+3*rot((dx,dy),h)[1])+v[CC[(h+dh)%4]]]
   new +=[2*(rot(p,h)[0]+3*rot(p,h)[1])+v[OUT[a,k,h]]for k,p in enumerate(g['outputs'])if not locked(a,p)]
   assert max(new)<=max(old)
 out['integer_recheck']='PASS'
if status==0:out['reason']=fn('solver_get_reason_unknown',[ptr,ptr],cs)(ctx,sol).decode()
(R/'unlocked_potential.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items()if k not in('values','model','dependencies')},indent=2))
