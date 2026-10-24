#!/usr/bin/env python3
"""Discovery: exact next-cell first-return language, no paired-row enumeration."""
import json,time
from collections import Counter
import probe_boundary_extension as p
from probe_consecutive_port_generator import generate

def main():
 cert=json.load(open('certify_diagonal_read_minimum.json'));out=[];S=Counter();start=time.time()
 for c in cert['cases']:
  for z in c.get('survivors',[]):
   H=[tuple(h)for h in c['lower_headings']+z['A_headings']];k,G=p.graph(H);assert k=='open';rel=p.relations(H,G);a,b=H[-2:]
   oc=lambda hs,d:sum((x+(1 if k%2==0 else-1))%4==d for k,x in enumerate(hs));ports=[(oc(a,0),b.count(3)),(oc(b,0),a.count(3))]
   dom=[generate(*ports[r],False,rel[r])for r in(0,1)];empty=[r for r,d in enumerate(dom)if not d];S['empty'if empty else'nonempty']+=1
   out.append({'lower_case':c['case'],'A_indices':z['A_indices'],'histories':H,'ports':ports,'return_relations':rel,'domain_sizes':list(map(len,dom)),'empty_lanes':empty})
 print(dict(S),'seconds',time.time()-start,'maxdomain',max(max(z['domain_sizes'])for z in out));json.dump(out,open('/tmp/minimum_next_cell_domains.json','w'),indent=2)
 print('empty by lower',dict(Counter(z['lower_case']for z in out if z['empty_lanes'])))
 print('nonempty by lower',dict(Counter(z['lower_case']for z in out if not z['empty_lanes'])))
if __name__=='__main__':main()
