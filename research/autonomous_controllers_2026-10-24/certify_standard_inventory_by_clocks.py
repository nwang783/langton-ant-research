#!/usr/bin/env python3
"""Transparent finite-domain clock-cycle certificate, no SMT status premise."""
import json,time
from pathlib import Path
from check_standard_fixed_inventory import setup,P
OUT=Path(__file__).resolve().parent

def constraints():
 ev,d,H,points,ix,opts,original=setup();var={};varmeta=[]
 for i,p in enumerate(points):
  hs=opts[i][0]
  for heading in range(4):
   m=sum((hi+(1 if j%2==0 else-1))%4==heading for j,hi in enumerate(hs))
   for k in range(m):var[i,heading,k]=len(varmeta);varmeta.append([i,heading,k])
 assert len(var)==P
 allopts=[]
 for i,p in enumerate(points):
  oo=[]
  for hs in opts[i]:
   cin={h:0 for h in range(4)};cout={h:0 for h in range(4)};incoming=[];outgoing=[];const=[]
   for j,hi in enumerate(hs):
    ho=(hi+(1 if j%2==0 else-1))%4
    q=(p[0]-__import__('check_extremal_read_coupling').D[hi][0],p[1]-__import__('check_extremal_read_coupling').D[hi][1]);r,k=__import__('check_extremal_read_coupling').quotient(q,d);ii=ix[r]
    ei=var[ii,hi,cin[hi]];cin[hi]+=1;eo=var[i,ho,cout[ho]];cout[ho]+=1
    incoming.append(ei);outgoing.append(eo);const.append(1+k*P)
   ee={}
   def add(u,v,w):ee[u,v]=max(ee.get((u,v),-10**9),w)
   for ei,eo,c in zip(incoming,outgoing,const):add(ei,eo,c);add(eo,ei,-c)
   for j in range(1,len(hs)):add(incoming[j-1],incoming[j],4+const[j-1]-const[j])
   oo.append(ee)
  allopts.append(oo)
 return allopts,original,varmeta

def common(allopts,domains):
 out={}
 for i,dom in enumerate(domains):
  keys=set(allopts[i][dom[0]])
  for o in dom[1:]:keys.intersection_update(allopts[i][o])
  for e in keys:
   w=min(allopts[i][o][e]for o in dom);out[e]=max(out.get(e,-10**9),w)
 return out

def cycle(edges,N=P):
 dist=[0]*N;prev=[None]*N;last=None
 for _ in range(N):
  last=None
  for (u,v),w in edges.items():
   if dist[v]<dist[u]+w:dist[v]=dist[u]+w;prev[v]=(u,v,w);last=v
  if last is None:return None
 x=last
 for _ in range(N):x=prev[x][0]
 start=x;back=[]
 while True:
  edge=prev[x];back.append(edge);x=edge[0]
  if x==start:break
 out=list(reversed(back));assert sum(e[2]for e in out)>0;assert all(out[j][1]==out[(j+1)%len(out)][0]for j in range(len(out)))
 return out

def propagate(allopts,domains,original):
 rounds=[];t=time.time()
 for rnd in range(100):
  base=common(allopts,domains);assert cycle(base)is None
  removed=[]
  for i,dom in enumerate(domains):
   if len(dom)==1:continue
   for o in dom:
    ee=dict(base)
    for e,w in allopts[i][o].items():ee[e]=max(ee.get(e,-10**9),w)
    cc=cycle(ee)
    if cc:
     assert o!=original[i],('removed genuine standard',i,o)
     removed.append({'cell':i,'option':o,'positive_cycle':cc})
  rounds.append({'domains_before':domains,'common_edge_count':len(base),'removed':removed})
  print('ROUND',rnd,'domain_sizes',[len(d)for d in domains],'removed',len(removed),'seconds',time.time()-t,flush=True)
  if not removed:break
  remove={(z['cell'],z['option'])for z in removed};domains=[[o for o in dom if(i,o)not in remove]for i,dom in enumerate(domains)]
  assert all(dom for dom in domains)
 return domains,rounds

def main():
 oo,original,varmeta=constraints();domains=[list(range(len(o)))for o in oo];final,rounds=propagate(oo,domains,original)
 result={'scope':__doc__,'variables':varmeta,'initial_domain_sizes':list(map(len,oo)),'rounds':rounds,'final_domains':final,'standard_options':original,'all_forced_to_standard':all(d==[o]for d,o in zip(final,original)),'unresolved_product':__import__('math').prod(map(len,final))}
 (OUT/'standard_inventory_clock_propagation.json').write_text(json.dumps(result,separators=(',',':'))+'\n');print('DONE',result['all_forced_to_standard'],'remaining',result['unresolved_product'],flush=True)
if __name__=='__main__':main()
