#!/usr/bin/env python3
"""Complete four-state expanding-recurrence synthesis, using offset partitions.
All accessible states and arbitrary Gaussian offsets are covered. Finite traces
only reject; any survivor is handed to the exact visit-relation inverse test.
"""
from search_small_recurrences import paths,state,finite_probe
from expanding_recurrence_visits import Recurrence,mul,sub,derive_ant_geometry,inverse_tests
from itertools import product
from collections import defaultdict,Counter
from pathlib import Path
import json,time,hashlib

def normalize(seq):
    ids={};out=[]
    for q in seq:
        if q not in ids:ids[q]=len(ids)
        out.append(ids[q])
    return tuple(out)

def partitions(n):
    for p in product(range(n),repeat=n):
        if normalize(p)==p:yield p

def catalogue():
    groups=defaultdict(list);n=0;parts=list(partitions(4))
    for tail in product(range(4),repeat=6):
        nxt=[[0,1],[tail[0],tail[1]],[tail[2],tail[3]],[tail[4],tail[5]]]
        pattern=tuple(state(i,nxt)for i in range(8))
        if len(set(pattern))!=4 or normalize(pattern)!=pattern:continue
        reps=[pattern.index(s)for s in range(4)];n+=1
        for p in parts:
            merged=normalize(tuple(p[s]for s in pattern));groups[merged].append((nxt,reps))
    return groups,n

def main():
    start=time.monotonic();groups,graphs=catalogue();counts=Counter();count=prefixes=filtered=0;survivors=[];dedup=set();digest=hashlib.sha256();latest=(-1,None)
    for word,ps in paths(15):
        prefixes+=1
        for a in product([-1,1],repeat=2):
            offsets=[tuple(sub(ps[2*n+j],mul(a,ps[n]))for j in[0,1])for n in range(8)]
            pattern=normalize(offsets)
            if pattern not in groups:continue
            filtered+=1
            for nxt,reps in groups[pattern]:
                off=[list(offsets[n])for n in reps];key=json.dumps([a,nxt,off])
                if key in dedup:continue
                dedup.add(key);count+=1;model=Recurrence(2,a,nxt,off);result=finite_probe(model,1024)
                if 'reject'in result:
                    counts[result['reject']]+=1
                    if result['time']>latest[0]:latest=(result['time'],{'scale':a,'transition':nxt,'offset':off,'prefix':word,**result})
                else:
                    relations,meta=model.difference_machine();left,geometry=derive_ant_geometry(model,relations)
                    if any(v is not None for k,v in geometry.items()if k.startswith('bad_')):result={'reject':'exact all-time geometry',**geometry,**meta};counts[result['reject']]+=1
                    else:
                        result={**geometry,**meta,**inverse_tests(relations((0,0)),left)}
                        result['status']='POSSIBLE FINITE ANT'if result['first_left_times_finite']and result['bad_alternation_witness']is None else'exact all-time ant rejection';counts[result['status']]+=1
                    survivors.append({'scale':a,'transition':nxt,'offset':off,'prefix':word,**result})
                digest.update(json.dumps([a,nxt,off,result],sort_keys=True).encode()+b'\n')
    out={'scope':'Exactly4 accessible affine recurrence states, binary time, common Gaussian scale norm squared2, stable leading zero, arbitrary integer offsets, initial heading N and position0. Finite ant legality is necessary in the first15 moves. All survivors require exact automatic validation.','canonical_state_graphs':graphs,'offset_equality_patterns':len(groups),'legal_prefixes':prefixes,'prefix_scale_pairs_matching_some_graph':filtered,'distinct_consistent_recurrences':count,'outcomes':dict(counts),'finite_probe_survivors':survivors,'latest_finite_rejection':latest[1],'all_record_sha256':digest.hexdigest(),'elapsed_seconds':time.monotonic()-start}
    (Path(__file__).resolve().parent/'four_state_recurrence_controls.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
