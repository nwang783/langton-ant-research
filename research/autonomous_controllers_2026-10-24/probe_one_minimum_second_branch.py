#!/usr/bin/env python3
"""Discovery of a specified three-row completion family; no completion claims."""
import json,time
from collections import Counter
from itertools import product
import certify_diagonal_read_minimum as base
from probe_consecutive_port_generator import generate
from probe_one_singleton_extension import fits
from check_extremal_read_coupling import D,quotient

def rels(H,G):
 result=[[],[]]
 for chain in G['chains']:
  (i,j),k=chain[0];assert k==0;p=G['points'][i];h=H[i][j];source=(p[0]-D[h][0],p[1]-D[h][1]);r,v=quotient(source,(2,-2))
  (ii,jj),kk=chain[-1];p=G['points'][ii];ho=(H[ii][jj]+(1 if jj%2==0 else-1))%4;target=(p[0]+2*kk+D[ho][0],p[1]-2*kk+D[ho][1]);assert sum(source)==sum(target)==len(H)//2-1
  if source==target:
   a=[z for z,x in enumerate(H[i])if x==h].index(j);b=[z for z,x in enumerate(H[ii])if(x+(1 if z%2==0 else-1))%4==ho].index(jj);result[r[0]].append((a,b,len(chain)+1))
 return result

def domain(H,G):
 nextT=len(H)//2-1;isC=bool(nextT%2);a,b=H[-2:];oc=lambda hs,d:sum((x+(1 if j%2==0 else-1))%4==d for j,x in enumerate(hs))
 ports=[(oc(b,1),a.count(2)),(oc(a,1),b.count(2))]if isC else[(oc(a,0),b.count(3)),(oc(b,0),a.count(3))]
 re=rels(H,G);return[generate(*ports[r],isC,re[r])for r in(0,1)],ports,re

def main():
 start=time.time();frontier=[[(3,),(),(0,),(2,2),(3,1,3),(3,3,1)]];rounds=[]
 for row in range(3):
  stats=Counter();nxt=[];details=[]
  for idx,H in enumerate(frontier):
   k,G=base.graph(H);assert k=='open';(AA,BB),ports,rr=domain(H,G);counts=Counter()
   for a,b in product(AA,BB):
    HH=H+[a,b]
    if not fits(HH):kind='residue_budget'
    else:kind,w=base.graph(HH)
    stats[kind]+=1;counts[kind]+=1
    if kind=='open':nxt.append(HH)
   details.append({'histories':H,'ports':ports,'relations':rr,'domain_sizes':[len(AA),len(BB)],'counts':dict(counts)})
  print('ROW',row,'parents',len(frontier),'counts',dict(stats),'seconds',time.time()-start,flush=True)
  rounds.append({'parent_details':details,'stats':dict(stats),'survivors':nxt});frontier=nxt
 result={'scope':__doc__,'rounds':rounds,'seconds':time.time()-start};json.dump(result,open('one_minimum_second_branch_discovery.json','w'),indent=2)
if __name__=='__main__':main()
