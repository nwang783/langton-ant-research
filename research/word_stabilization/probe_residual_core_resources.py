"""Exact residual-core geometry and exploratory amortized linear ranking.
Uses a forbidden-pair relation as a sound overapproximation of possible resource transfers.
An infeasible LP is not an ant counterexample.
"""
import json,sys
from pathlib import Path
from collections import defaultdict
from scipy.optimize import linprog
import numpy as np
prefix,cert,out=sys.argv[1:4]
Q=json.load(open(prefix+'_port_quotient.json'));M=Q['macro_words'];forbid={tuple(map(int,l.split()[:5]))for l in open(cert)}
D=(1j,1,-1j,-1)
def tr(w):
 p=0j;h=0;first={};last={};odd=set()
 for t,c in enumerate(w):
  first.setdefault(p,(c,t));assert last.get(p)!=c;last[p]=c;odd.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p+=D[h]
 return p,h,first,last,odd
xy=lambda p:[int(p.real),int(p.imag)]
core={p for p,(c,t)in tr('LLLLRLRRRRL')[2].items()if c=='L'}
geom=[]
for a in M:
 p,h,first,last,odd=tr(a['word']);_,_,ff,_,_=tr(a['word']+a['end_marker']);nc={p+q*(-1j)**h for q in core};b={p for p,(c,t)in ff.items()if c=='L'};o=b^odd
 assert core<=b and nc<=o
 ei=b-core;eo=o-nc
 assert not ei&eo
 inp=sorted(ei,key=lambda q:(q.real,q.imag));output=sorted(eo,key=lambda q:(q.real,q.imag))
 assert all(last.get(q)=='R'for q in output)
 geom.append({'name':a.get('name'),'endpoint':xy(p)+[h],'inputs':[xy(q)for q in inp],'outputs':[xy(q)for q in output],'input_first_phases':[ff[q][1]for q in inp],'forced_white':[xy(q)for q,(c,t)in ff.items()if c=='R']})
keep=[i for i,a in enumerate(M)if a.get('name')not in ['DCC','DCCC']]
ins=[(a,k)for a in keep for k in range(len(geom[a]['inputs']))];outs=[(a,k)for a in keep for k in range(len(geom[a]['outputs']))];ix={v:i for i,v in enumerate(ins)};ox={v:i+len(ins)for i,v in enumerate(outs)};n=len(ins)+len(outs);rows=[];rhs=[];trans=[]
for a,k in outs:
 z=complex(*geom[a]['outputs'][k])
 for b,j in ins:
  q=complex(*geom[b]['inputs'][j]);poses=[]
  for h in range(4):
   p=z-q*(-1j)**h;x,y=xy(p)
   if (x+y-h)%2:continue
   if (a,b,x,y,h)not in forbid:poses.append([x,y,h])
  if poses:
   row=np.zeros(n);row[ix[b,j]]=1;row[ox[a,k]]=-1;rows.append(row);rhs.append(0);trans.append({'producer':[a,k],'consumer':[b,j],'poses':poses})
for a in keep:
 row=np.zeros(n)
 for b,k in ins:
  if b==a:row[ix[b,k]]=-1
 for b,k in outs:
  if b==a:row[ox[b,k]]=1
 rows.append(row);rhs.append(-1)
r=linprog(np.ones(n),A_ub=rows,b_ub=rhs,bounds=(0,None),method='highs')
res={'source':prefix,'certificate':cert,'core':[xy(q)for q in sorted(core,key=lambda q:(q.real,q.imag))],'geometry':geom,'kept_packet_types':keep,'inputs':ins,'outputs':outs,'transfer_edges':trans,'linear_rank_success':bool(r.success),'linear_rank_status':r.message}
if r.success:res['input_weights']=[[a,k,float(r.x[ix[a,k]])]for a,k in ins];res['output_weights']=[[a,k,float(r.x[ox[a,k]])]for a,k in outs]
Path(out+'.json').write_text(json.dumps(res,indent=2));print('inputs',len(ins),'outputs',len(outs),'transferedges',len(trans),'LP',r.message)
for a in keep:
 print(geom[a]['name'], 'in',geom[a]['inputs'],'out',geom[a]['outputs'],'usableout',sum(any(t['producer']==[a,k]for t in trans)for k in range(len(geom[a]['outputs']))))
if r.success:print(res['input_weights'],res['output_weights'])
