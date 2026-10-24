from collections import defaultdict, Counter
from itertools import product
from pathlib import Path
import json
root=Path(__file__).resolve().parent
# Headings N E S W =0 1 2 3; source departs E along a max-C face below it.
def histories(axis):
    for n in range(1,5):
        for hs in product((axis,(axis+2)%4),repeat=n):
            outs=[(h+(1 if i%2==0 else -1))%4 for i,h in enumerate(hs)]
            yield hs,outs

def cls(hs,face_heading):
    rf=sum(h==face_heading for i,h in enumerate(hs)if i%2==0)
    rg=sum(h!=face_heading for i,h in enumerate(hs)if i%2==0)
    if not rf or rf<rg:return None
    return {(1,0):'single_R_boundary',(1,1):'flat_two_R',(2,0):'same_face_defect'}[rf,rg]
compat=[]
for hs,os in histories(0):
    sc=cls(hs,0)
    if not sc:continue
    f=os.count(1)
    for ht,ot in histories(1):
        tc=cls(ht,1)
        if tc not in ('flat_two_R','same_face_defect') or ht[2]!=1 or ht.count(1)!=f:continue
        n=ht[:3].count(1)
        j=[i for i,o in enumerate(os)if o==1][n-1]
        compat.append(dict(source=list(hs),target=list(ht),source_class=sc,target_class=tc,edge_flow=f,target_second_R_input_ordinal=n,supplier_rank=j,source_pair_R_rank=j-j%2))
summary=defaultdict(set)
for x in compat:summary[x['target_class'],x['source_class']].add(x['supplier_rank'])
# Exact R2 input/output port ordinal law, all two-R cells.
ordinal_rows=[]
for hs,os in histories(1):
    if len(hs)<3:continue
    i=hs[:3].count(hs[2]);o=os[:3].count(os[2]);same=hs[0]==hs[2]
    assert sorted((i,o))==([2,3]if same else[1,2])
    ordinal_rows.append(dict(incoming=list(hs),input_ordinal=i,output_ordinal=o,kind='same_face_defect'if same else'flat_two_R'))
# Literal standard front, retaining full actual drift. R ranks may exceed2 here.
W=(root.parent/'word_stabilization/standard_word.txt').read_text().strip()
records=[]
for copies in (1,2,3):
    a=2*copies;d=complex(a,a);P=104*copies;q=-1+0j;h=1j;hist=defaultdict(list)
    def canon(z):
        k=int(z.real)//a;return z-k*d,k
    for t,c in enumerate(W*copies):
        z,k=canon(q);hist[z].append((t-k*P,h,c));h*=(-1j if c=='R'else 1j);q+=h
    hist={z:sorted(es)for z,es in hist.items()}
    assert all(c==('R'if j%2==0 else'L')for es in hist.values()for j,(t,h,c)in enumerate(es))
    nodes=[(z,j)for z,es in hist.items()for j in range(0,len(es),2)]
    # For each R target, locate the actual predecessor event and pair its source rank down.
    edges={};suppliers=Counter();flow=Counter()
    for z,es in hist.items():
        for j,(t,hh,c)in enumerate(es):flow[z,hh*(-1j if c=='R'else 1j)]+=1
    for z,r in nodes:
        t,hh,c=hist[z][r];u,k=canon(z-hh)
        j=next(j for j,(tt,_,_)in enumerate(hist[u])if tt+k*P==t-1)
        pair=j-j%2;delay=t-1-(hist[u][pair][0]+k*P)
        assert delay>=0 and delay%4==0 and (delay==0)==(j%2==0)
        assert delay//4>=j-pair
        # Store dependency target -> source and source-supplier edge orientation.
        edges[z,r]=((u,pair),k,j,delay//4,hh)
        suppliers[hist[u][j][2]]+=1
    visited=set();cycles=[]
    for start in nodes:
        if start in visited:continue
        node=start;order=[];where={}
        while node not in visited and node not in where:
            where[node]=len(order);order.append(node);node=edges[node][0]
        if node in where:
            cyc=order[where[node]:];K=-sum(edges[x][1]for x in cyc);Q=sum(edges[x][3]for x in cyc)
            assert K>0 and K*P==len(cyc)+4*Q
            # Each actual supplier occurrence unique across all selected cycles.
            for x in cyc:
                (u,pair),k,j,qq,hh=edges[x]
                flow[u,hh]-=1;assert flow[u,hh]>=0
            cycles.append(dict(length=len(cyc),actual_winding=K,qsum=Q,second_or_later_R_nodes=sum(r>=2 for z,r in cyc),L_suppliers=sum(edges[x][2]%2 for x in cyc),physical_vertex_repeats=len(cyc)-len({z for z,r in cyc})))
        visited.update(order)
    K=sum(x['actual_winding']for x in cycles);L=sum(x['length']for x in cycles)
    assert sum((n*e for (z,e),n in flow.items()),0j)==(1-K)*d
    assert P>=L+2*a*abs(1-K)
    records.append(dict(full_period=P,full_drift=[a,a],R_nodes=len(nodes),all_R_target_supplier_turns=dict(suppliers),cycles=cycles,cycle_subtraction_bound=L+2*a*abs(1-K)))
res=dict(status='PASS exact local ordinal enumeration and literal full-drift standard controls only',two_R_local_rows=len(ordinal_rows),local_compatible_pairs=len(compat),supplier_rank_summary=[dict(target_class=k[0],source_class=k[1],supplier_ranks=sorted(v))for k,v in sorted(summary.items())],ordinal_rows=ordinal_rows,compatible_pairs=compat,standard_controls=records)
(root/'paired_r_controls.json').write_text(json.dumps(res,indent=2)+'\n')
print(json.dumps({k:v for k,v in res.items()if k not in('ordinal_rows','compatible_pairs')},indent=2))
