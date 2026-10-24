#!/usr/bin/env python3
"""Exhaust binary-time common Gaussian scale recurrences with <=3 states.
Scale norm squared2, zero-padding stable start state, arbitrary finite offsets.
Offsets are exhaustively determined by the first 2^m-1 unit quarter-turn moves.
Finite probes only reject. Every survivor is sent to an all-time automaton test.
"""
from expanding_recurrence_visits import Recurrence,derive_ant_geometry,sub,mul,inverse_tests
from itertools import product
from collections import Counter
from pathlib import Path
import json,time,hashlib
D=((0,1),(1,0),(0,-1),(-1,0))

def paths(length):
    for bits in product('RL',repeat=length):
        p=(0,0);h=0;ps=[p];seen={};okay=True
        for c in bits:
            if p in seen and seen[p]==c:okay=False;break
            seen[p]=c;h=(h+(1 if c=='R'else-1))%4;p=(p[0]+D[h][0],p[1]+D[h][1]);ps.append(p)
        if okay:yield ''.join(bits),ps

def machines(m):
    if m==2:
        for x,y in product(range(2),repeat=2):yield [[0,1],[x,y]]
    if m==3:
        for x,y in product(range(3),repeat=2):
            if 2 not in[x,y]:continue
            for z,w in product(range(3),repeat=2):yield [[0,1],[x,y],[z,w]]

def state(n,nxt):
    s=0
    for d in bin(n)[2:]:s=nxt[s][int(d)]
    return s

def finite_probe(model,limit=512):
    oldh=0;seen={};black=set()
    for t in range(limit):
        p=model.point(t);q=model.point(t+1);delta=sub(q,p)
        if delta not in D:return {'reject':'nonunit','time':t,'step':delta}
        h=D.index(delta);turn=(h-oldh)%4
        if turn not in[1,3]:return {'reject':'nonquarter','time':t,'headings':[oldh,h]}
        c='R'if turn==1 else'L'
        if p in seen and seen[p][1]==c:return {'reject':'equal consecutive reads','time':t,'previous':seen[p][0],'point':p,'turn':c}
        if p not in seen and c=='L':black.add(p)
        seen[p]=(t,c);oldh=h
    return {'inconclusive_prefix':limit,'first_L_count':len(black)}

def run(m):
    start=time.monotonic();count=0;counts=Counter();survivors=[];hashes=hashlib.sha256();dedup=set();prefixes=list(paths(2**m-1))
    for nxt in machines(m):
        reps={}
        for n in range(2**(m-1)):reps.setdefault(state(n,nxt),n)
        assert len(reps)==m
        for a in product([-1,1],repeat=2):
            for word,ps in prefixes:
                off=[]
                for s in range(m):
                    n=reps[s];off.append([sub(ps[2*n+j],mul(a,ps[n]))for j in range(2)])
                model=Recurrence(2,a,nxt,off)
                if any(model.point(n)!=ps[n]for n in range(len(ps))):continue
                key=json.dumps([a,nxt,off]);
                if key in dedup:continue
                dedup.add(key);count+=1;result=finite_probe(model)
                if 'reject'in result:counts[result['reject']]+=1
                else:
                    relations,meta=model.difference_machine();left,geometry=derive_ant_geometry(model,relations)
                    if any(v is not None for k,v in geometry.items()if k.startswith('bad_')):result={'reject':'exact all-time geometry',**geometry,**meta};counts[result['reject']]+=1
                    else:
                        result={**geometry,**meta,**inverse_tests(relations((0,0)),left)}
                        result['status']='POSSIBLE FINITE ANT'if result['first_left_times_finite']and result['bad_alternation_witness']is None else'exact all-time ant rejection'
                        counts[result['status']]+=1
                    survivors.append({'scale':a,'transition':nxt,'offset':off,'prefix':word,**result})
                hashes.update(json.dumps([a,nxt,off,result],sort_keys=True).encode()+b'\n')
    return {'states':m,'legal_geometric_prefixes':len(prefixes),'consistent_distinct_recurrences':count,'outcomes':dict(counts),'finite_probe_survivors':survivors,'record_sha256':hashes.hexdigest(),'elapsed_seconds':time.monotonic()-start}

if __name__=='__main__':
    out=[]
    for m in[2,3]:
        r=run(m);out.append(r);print(json.dumps(r,indent=2),flush=True)
        (Path(__file__).resolve().parent/'small_recurrence_controls.json').write_text(json.dumps({'scope':'At most3 accessible states; binary time; common Gaussian scale of norm squared2; stable zero-padding start; unit quarter-turn geometry and ant alternation. One-state case excluded analytically. No arbitrary offsets omitted, since first seven moves determine them.','results':out},indent=2)+'\n')
