#!/usr/bin/env python3
"""Discovery only: derived first upper-pair domains over155 current cases."""
import json,time
from itertools import product
from collections import Counter
import certify_diagonal_read_minimum as base
import probe_boundary_extension as paths
from probe_consecutive_port_generator import generate
TARGETS=[v for v in product(range(9),repeat=4)if sum(v)==8 and all(x%4==2 for x in[v[0]-v[1],v[3]-v[2],v[0]-v[2],v[3]-v[1]])]
def fits(H):
 v=[0]*4
 for i,h in enumerate(H):
  if len(h)%2:
   t=i//2-1;r=i%2;v[2*r+(t-r)%2]+=1
 return [q for q in TARGETS if all(a<=b for a,b in zip(v,q))]
def main():
 cert=json.load(open('certify_diagonal_read_minimum.json'));ids={(a,tuple(b))for a,b in json.load(open('first_N_return_rules_certificate.json'))['explicit_set_difference']['exact_final155_ids']};S=Counter();rows=[];survivors=[];start=time.time()
 for c in cert['cases']:
  for z in c.get('survivors',[]):
   key=c['case'],tuple(z['A_indices'])
   if key not in ids:continue
   H=[tuple(h)for h in c['lower_headings']+z['A_headings']];_,G=paths.graph(H);rel=paths.relations(H,G);a,b=H[-2:];oc=lambda hs,d:sum((x+(1 if j%2==0 else-1))%4==d for j,x in enumerate(hs));ports=[(oc(a,0),b.count(3)),(oc(b,0),a.count(3))];q=generate(*ports[0],False,rel[0]);r=generate(*ports[1],False,rel[1]);cc=Counter();sample=[]
   for qi,ri in product(range(len(q)),range(len(r))):
    HH=H+[q[qi],r[ri]]
    if not fits(HH):kind='residue_budget'
    else:
     kind,w=base.graph(HH)
     if kind=='closed_component':assert w['other_local_events']>0
    cc[kind]+=1;S[kind]+=1
    if kind=='open':survivors.append({'case':key,'Q_indices':[qi,ri],'histories':HH});sample.append([qi,ri])
   rows.append({'case':key,'histories':H,'counts':dict(cc),'helper_domain_sizes':[len(q),len(r)],'surviving_Q_indices':sample})
 result={'scope':__doc__,'aggregate':dict(S),'coarse_survivors':sum(bool(r['surviving_Q_indices'])for r in rows),'coarse_removed':[r['case']for r in rows if not r['surviving_Q_indices']],'by_case':rows,'survivors':survivors,'seconds':time.time()-start};json.dump(result,open('/tmp/diagonal_paired_helpers.json','w'),indent=2);print({k:v for k,v in result.items()if k not in('by_case','survivors')})
if __name__=='__main__':main()
