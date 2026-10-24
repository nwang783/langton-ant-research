#!/usr/bin/env python3
"""Finite local certificate, not a complete cap-five front exclusion.
Full(+4,0), every period P>=16: non-singleton lowest profiles fail using
proper-path necessities or an explicit affine-in-P negative clock cycle.
"""
from collections import defaultdict,Counter
from pathlib import Path
import json,time
from probe_axis4_fast_zone import rows
from axis4_first_return_window import bad_window
D=((0,1),(1,0),(0,-1),(-1,0))
def constraints(hs):
 edges=[];events=[];ins=defaultdict(list);outs=defaultdict(list)
 for y,row in enumerate(hs):
  for x,h in enumerate(row):
   for j,a in enumerate(h):
    e=y,x,j;events.append(e);ins[y,x,a].append(e);outs[y,x,(a+(1 if j%2==0 else -1))%4].append(e)
    if j:edges.append(((y,x,j),(y,x,j-1),0,-4,'rank'))
 for (y,x,g),es in outs.items():
  dx,dy=D[g];xx=x+dx;yy=y+dy
  if not 0<=yy<len(hs):continue
  ts=ins[yy,xx%4,g];assert len(es)==len(ts)
  for a,b in zip(es,ts):
   k=xx//4;edges.append((a,b,-k,1,'physical'));edges.append((b,a,k,-1,'physical_reverse'))
 return events,edges

def negative_cycle(events,edges,P=16):
 ds={e:0 for e in events};prev={}
 for it in range(len(events)):
  z=None
  for a,b,k,c,kind in edges:
   if ds[b]>ds[a]+k*P+c:ds[b]=ds[a]+k*P+c;prev[b]=(a,b,k,c,kind);z=b
  if z is None:return None
 for _ in events:z=prev[z][0]
 v=z;cycle=[]
 while True:
  edge=prev[v];cycle.append(edge);v=edge[0]
  if v==z:break
 k=sum(e[2] for e in cycle);c=sum(e[3] for e in cycle)
 if k>0 or k*P+c>=0:return None
 return dict(slope=k,intercept=c,edges=cycle)

def run():
 st=time.time();ss=rows(1,5,4);ix=defaultdict(list)
 for row in ss:ix[tuple(row[c]['ins'][0] if c%2==0 else row[c]['outs'][2] for c in range(4))].append(row)
 forbidden=[(m,)*4 for m in range(2,6)]+[(2,2,3,3),(4,4,5,5),(1,2,2,1),(3,4,4,3)]
 cert=[];summaries=[]
 for ns in forbidden:
  bottom=[tuple((3 if j%2==0 else 1) if c%2==0 else 2 for j in range(m)) for c,m in enumerate(ns)];counts=Counter();cases=[]
  for row in ix[ns]:
   upper=[r['h'] for r in row];reason=bad_window([bottom,upper])
   if reason:item=dict(upper=upper,kind='proper_path',reason=reason);counts[reason]+=1
   else:
    ev,edges=constraints([bottom,upper]);cycle=negative_cycle(ev,edges);assert cycle is not None,(ns,upper)
    item=dict(upper=upper,kind='affine_negative_cycle',**cycle);counts['affine_negative_cycle']+=1
   cases.append(item)
  cert.append(dict(bottom=ns,cases=cases));summaries.append(dict(bottom=ns,raw_upper_rows=len(cases),rejections=dict(counts)))
 result=dict(status='AUTHOR_LOCAL_BOUNDARY_CERTIFICATE_PASS',full_drift=[4,0],cap=5,minimum_period=16,scope='LOWEST_ROW_REDUCTION_ONLY_ALL_PERIODS_ALL_WIDTHS',remaining_bottom_profiles=[[0,0,1,1],[1,1,1,1]],profiles=summaries,seconds=time.time()-st)
 root=Path(__file__).parent;root.joinpath('axis4_cap5_bottom_reduction.certificate.json').write_text(json.dumps(dict(parameters={k:result[k] for k in ('full_drift','cap','minimum_period','scope')},profiles=cert))+'\n');root.joinpath('axis4_cap5_bottom_reduction.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True)
if __name__=='__main__':run()
