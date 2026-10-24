"""Nonnegative additive exponential bounding potentials; exploratory LP only."""
import json,sys
import numpy as np
from scipy.optimize import linprog
from pathlib import Path
P=Path(__file__).parent;compound=len(sys.argv)>1 and sys.argv[1]=='compound'
if compound:
 J=json.load(open(P/'dcv_compound_resources.json'));G=J['compounds'];K=list(range(len(G)));T=J['transfer_edges']
else:
 J=json.load(open(P/'dcv_residual_core_resources.json'));G=J['geometry'];K=J['kept_packet_types'];T=[];H={tuple(map(int,l.split()[:7]))for l in open(P/'dcv_protected_patch2_kernel.tsv')}
 for e in J['transfer_edges']:
  a,k=e['producer'];b,j=e['consumer']
  for x,y,h in e['poses']:
   if (a,b,x,y,h,*G[a]['outputs'][k]) not in H:T.append([a,k,b,j,x,y,h])
R=lambda p,h:complex(*p[:2])*(-1j)**h
U={(a,k,h):4+n for n,(a,k,h) in enumerate((a,k,h)for a in K for k in range(len(G[a]['inputs']))for h in range(4))};W={(a,k,h):4+len(U)+n for n,(a,k,h) in enumerate((a,k,h)for a in K for k in range(len(G[a]['outputs']))for h in range(4))};N=4+len(U)+len(W)
base_rows=[]
for a,k,b,j,x,y,hr in T:
 for h in range(4):
  r=np.zeros(N);r[U[b,j,(h+hr)%4]]=1;r[W[a,k,h]]=-1;base_rows.append(r)
results=[]
for b in [1,1.0625,1.125,1.25,1.5,2,3,4,8]:
 rows=base_rows.copy()
 for a in K:
  g=G[a];e=g['endpoint'];dh=e[2]
  for h in range(4):
   r=np.zeros(N);r[h]-=1;r[(h+dh)%4]+=b**int(R(e,h).imag)
   for k,p in enumerate(g['inputs']):r[U[a,k,h]]-=b**int(R(p,h).imag)
   for k,p in enumerate(g['outputs']):r[W[a,k,h]]+=b**int(R(p,h).imag)
   rows.append(r)
 r=linprog(np.ones(N),A_ub=rows,b_ub=np.zeros(len(rows)),bounds=[(1,None)]*4+[(0,None)]*(N-4),method='highs')
 print('compound',compound,'base',b,'status',r.message,flush=True);z={'base':b,'status':r.message}
 if r.success:z['core']=list(r.x[:4]);z['inputs']=[[*key,float(r.x[v])]for key,v in U.items()];z['outputs']=[[*key,float(r.x[v])]for key,v in W.items()]
 results.append(z)
(P/('dcv_compound_exponential_fuel.json' if compound else 'dcv_exponential_fuel.json')).write_text(json.dumps(results,indent=2))
