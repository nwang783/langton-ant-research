#!/usr/bin/env python3
"""Exact all-cap diagonal read-minimum local cover; higher support stays open."""
import json,hashlib
from pathlib import Path
from itertools import product,combinations
from collections import Counter
from check_extremal_read_coupling import D,quotient
DRIFT=(2,-2)

def histories(I,J,rels):
 allwords=[];valid=[]
 for n in range(2*(I+J)+2):
  z=I+J-n//2
  if z%2:continue
  a=z//2;b=I-a
  if not 0<=a<=(n+1)//2 or not 0<=b<=n//2:continue
  for rr,ll in product(combinations(range(0,n,2),a),combinations(range(1,n,2),b)):
   E=set(rr)|set(ll);h=tuple(1 if k in E else 3 for k in range(n));ee=sorted(E);ss=[k for k,x in enumerate(h)if(x+(1 if k%2==0 else-1))%4==2];assert len(ss)==J
   allwords.append(h)
   if all(ee[b]==ss[a]+1 for a,b,L in rels):valid.append(h)
 return allwords,valid

def graph(H):
 pts=[(r,t-r)for t in range(-1,len(H)//2-1)for r in(0,1)];ix={p:i for i,p in enumerate(pts)}
 nodes=[(i,j)for i,h in enumerate(H)for j in range(len(h))];out={};incoming={}
 for i,p in enumerate(pts):
  for h in range(4):
   src=[j for j,hi in enumerate(H[i])if(hi+(1 if j%2==0 else-1))%4==h]
   q,k=quotient((p[0]+D[h][0],p[1]+D[h][1]),DRIFT)
   if q not in ix:continue
   ii=ix[q];dst=[j for j,hi in enumerate(H[ii])if hi==h];assert len(src)==len(dst)
   for u,v in zip(src,dst):out[i,u]=((ii,v),k);incoming[ii,v]=((i,u),k)
 chains=[];seen=set()
 for start in nodes:
  if start in incoming:continue
  seq=[];at=start;k=0
  while True:
   assert at not in seen;seen.add(at);seq.append((at,k))
   if at not in out:break
   at,dk=out[at];k+=dk
  chains.append(seq)
 if len(seen)!=len(nodes):
  at=next(v for v in nodes if v not in seen);seq=[];ind={};k=0
  while at not in ind:
   ind[at]=len(seq);seq.append((at,k));at,dk=out[at];k+=dk
  cy=seq[ind[at]:];winding=k-cy[0][1]
  return 'closed_component',{'cycle':cy,'winding':winding,'other_local_events':len(nodes)-len(cy),'open_chains':len(chains)}
 where={}
 for c,seq in enumerate(chains):
  prev={}
  for a,((i,j),k)in enumerate(seq):
   where[i,j]=(c,a,k);p=(pts[i][0]+2*k,pts[i][1]-2*k)
   if p in prev and j!=prev[p][0]+1:return'skipped_rank',{'segment':seq[prev[p][1]:a+1],'point':p,'rank_before':prev[p][0],'rank_after':j}
   prev[p]=(j,a)
 edges=[]
 for i,hs in enumerate(H):
  for j in range(len(hs)-1):
   u,a,ka=where[i,j];v,b,kb=where[i,j+1]
   edges.append((u,v,4+a-b,kb-ka,i,j))
 N=len(nodes);P=10*N+100;n=len(chains);dist=[0]*n;prev=[None]*n;last=None
 for _ in range(n):
  last=None
  for e in edges:
   u,v,C,K,*_=e
   if dist[v]<dist[u]+C+K*P:dist[v]=dist[u]+C+K*P;prev[v]=e;last=v
  if last is None:break
 if last is not None:
  at=last
  for _ in range(n):at=prev[at][0]
  start=at;cy=[]
  while True:
   e=prev[at];cy.append(e);at=e[0]
   if at==start:break
  C=sum(e[2]for e in cy);K=sum(e[3]for e in cy)
  assert K>=0 and C+K*N>0
  return'positive_rank_clock_cycle',{'chains':chains,'inequality_cycle':cy,'constant':C,'period_coefficient':K,'local_event_count':N,'positive_at_minimum_period':C+K*N}
 return'open',{'points':pts,'chains':chains,'event_count':N}

def returns(H,G):
 pts=G['points'];rel=[[],[]];paths=[]
 for chain in G['chains']:
  (i,j),k=chain[0];assert k==0;h=H[i][j];p=pts[i];sp=(p[0]-D[h][0],p[1]-D[h][1]);sr,sk=quotient(sp,DRIFT)
  (ii,jj),kk=chain[-1];ho=(H[ii][jj]+(1 if jj%2==0 else-1))%4;q=pts[ii];tp=(q[0]+kk*2+D[ho][0],q[1]-kk*2+D[ho][1]);assert sum(sp)==sum(tp)==1
  if sp==tp:
   a=[z for z,x in enumerate(H[i])if x==h].index(j);b=[z for z,x in enumerate(H[ii])if(x+(1 if z%2==0 else-1))%4==ho].index(jj)
   rel[sr[0]].append((a,b,len(chain)+1));paths.append({'lane':sr[0],'outgoing_ordinal':a,'incoming_ordinal':b,'length':len(chain)+1,'physical_start':sp,'lower_chain':chain})
 return rel,paths

def main():
 cases=[];allstats=Counter();lowerstats=Counter()
 rows=[((3,),(),a,b)for a,b in product(((0,),(0,2)),((2,),(2,2)))]
 Q=((2,2,0),(2,2,0,2),(0,2,2),(0,2,2,2))
 rows +=[((3,),(3,),a,b)for a,b in product(Q,repeat=2)]
 for caseid,H in enumerate(rows):
  H=list(H);kind,G=graph(H);item={'case':caseid,'lower_headings':H,'lower_status':kind}
  lowerstats[kind]+=1
  if kind!='open':item['rejection']=G;cases.append(item);continue
  rel,paths=returns(H,G);a,b=H[-2:];oc=lambda hs,d:sum((h+(1 if j%2==0 else-1))%4==d for j,h in enumerate(hs))
  counts=[(oc(b,1),a.count(2)),(oc(a,1),b.count(2))]
  all0,W0=histories(*counts[0],rel[0]);all1,W1=histories(*counts[1],rel[1]);cc=Counter();reject=[];surv=[]
  for i,j in product(range(len(W0)),range(len(W1))):
   HH=H+[W0[i],W1[j]];k,g=graph(HH);cc[k]+=1;allstats[k]+=1
   if k=='open':surv.append({'A_indices':[i,j],'A_headings':[W0[i],W1[j]],'event_count':g['event_count'],'chains':g['chains']})
   else:reject.append({'A_indices':[i,j],'reason':k,'witness':g})
  item.update({'top_counts':counts,'first_returns':paths,'rank_relations':rel,'raw_single_cell_counts':[len(all0),len(all1)],'filtered_A_words':[W0,W1],'pair_outcomes':dict(cc),'survivors':surv,'rejections':reject});cases.append(item)
 result={'scope':__doc__,'full_drift':DRIFT,'lower_case_count':len(rows),'lower_outcomes':dict(lowerstats),'filtered_pair_count':sum(allstats.values()),'paired_outcomes':dict(allstats),'cases':cases,'warning':'Open means no rejection by this finite necessary cover. It is not a physical field, full event cycle, translator, or classification.'}
 Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items()if k!='cases'},indent=2))
if __name__=='__main__':main()
