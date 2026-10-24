"""Literal complete-front controls for the analytic first-departure theorem."""
from pathlib import Path
from collections import defaultdict,Counter
import json,hashlib
R=Path(__file__).resolve().parents[1];W=(R/'word_stabilization/standard_word.txt').read_text().strip();dirs=(1j,1,-1j,-1)
records=[]
for copies in (1,2,3):
    for sign in (1,-1):
        a=2*copies;d=complex(a,sign*a);P=104*copies;q=-1+0j if sign==1 else 0j;h=1j if sign==1 else 1;hist=defaultdict(list)
        def canon(z):
            k=int(z.real)//a;return z-k*d,k
        for t,c in enumerate(W*copies):
            z,k=canon(q);hist[z].append((t-k*P,h,c));h*=(-1j if c=='R'else 1j);q+=h
        hist={z:sorted(es)for z,es in hist.items()}
        assert all(c==('R'if j%2==0 else'L')for es in hist.values()for j,(t,h,c)in enumerate(es))
        flow=Counter();first={};edge={}
        for z,es in hist.items():
            for t,hh,c in es:flow[z,hh*(-1j if c=='R'else 1j)]+=1
            first[z]=es[0]
            target,k=canon(z-es[0][1]*1j);direction=-1j*es[0][1]
            rank=next(j for j,(_,hh,_)in enumerate(hist[target])if hh==direction)
            arrival=hist[target][rank][0]+k*P
            assert arrival==es[0][0]+1
            delay=arrival-(hist[target][0][0]+k*P)
            assert delay%4==0 and delay//4>=rank
            if rank==0:assert delay==0
            edge[z]=(target,k,direction,rank,delay//4)
        visited=set();cycles=[]
        for start in edge:
            if start in visited:continue
            pos=start;order=[];where={}
            while pos not in visited and pos not in where:
                where[pos]=len(order);order.append(pos);pos=edge[pos][0]
            if pos in where:
                cyc=order[where[pos]:];wind=sum(edge[z][1]for z in cyc)
                Q=sum(edge[z][4]for z in cyc);left=sum(edge[z][3]>0 for z in cyc)
                assert wind==-1 and left*2==len(cyc)and -P==len(cyc)-4*Q
                debt=sum(4*edge[z][3]-2 for z in cyc if edge[z][3])
                assert 0<=debt<=P
                for z in cyc:flow[z,edge[z][2]]-=1;assert flow[z,edge[z][2]]>=0
                cycles.append({'length':len(cyc),'winding':wind,'left_corners':left,'exact_q_sum':Q,'rank_debt':debt})
            visited.update(order)
        assert len(cycles)==2
        residue=sum(flow.values());disp=sum((num*direction for (z,direction),num in flow.items()),0j)
        horizontal=sum(num for (z,direction),num in flow.items()if direction.real)
        vertical=sum(num for (z,direction),num in flow.items()if direction.imag)
        assert horizontal==vertical and disp==(1+len(cycles))*d
        bound=sum(c['length']for c in cycles)+2*a*(1+len(cycles));assert P>=bound
        records.append({'period':P,'full_drift':[a,sign*a],'cycles':cycles,'residual_edges':residue,'counterflow_period_bound':bound})
note=R/'periodic_classification_new/white_first_departure_counterflow.md'
result={'status':'PASS independent complete-history first-port, first-time and counterflow controls',
        'note_sha256':hashlib.sha256(note.read_bytes()).hexdigest(),'controls':records,
        'scope':'The cap-free all-front theorem is analytic; these actual standard controls independently check conventions, cycle signs, multiple components, ordinal times and residual-flow arithmetic. No new exclusion graph.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
