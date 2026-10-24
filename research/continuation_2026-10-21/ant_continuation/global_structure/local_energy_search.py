#!/usr/bin/env python3
"""Search a finite local nonnegative energy for the five-macro branch.

This is a candidate-discovery script, not a proof. Every constraint records a
fully specified finite neighbourhood on which the macro is physically legal.
"""
from pathlib import Path
import json
import random
from collections import Counter
import numpy as np
from scipy.optimize import linprog

BASE = Path(__file__).resolve().parent
DATA = json.loads((BASE.parent / 'factor_language/five_macro_footprints.json').read_text())


def rotate_pattern(p, k):
    return sum(((p >> (x+k*y)) & 1) << ((k-1-y)+k*x)
               for y in range(k) for x in range(k))


def pattern_orbits(k):
    canon = []
    for p in range(1 << (k*k)):
        q = p
        orbit = []
        for _ in range(4):
            orbit.append(q)
            q = rotate_pattern(q, k)
        canon.append(min(orbit))
    classes = sorted(set(canon) - {0})
    idx = {c: i for i,c in enumerate(classes)}
    return [-1 if c==0 else idx[c] for c in canon], classes


def prepare_macro(name, k):
    d = DATA[name]
    initial = set(map(tuple, d['first_L']))
    visited = initial | set(map(tuple, d['first_R']))
    toggled = set(map(tuple, d['odd_visits']))
    origins = sorted({(x-dx,y-dy) for x,y in toggled for dy in range(k) for dx in range(k)})
    unknown = sorted({(x+dx,y+dy) for x,y in origins for dy in range(k) for dx in range(k)} - visited)
    return initial, toggled, origins, unknown


def changes(initial, toggled, origins, outside, k, idx, n):
    before = initial | outside
    after = before ^ toggled
    out = np.zeros(n, dtype=np.int16)
    for x,y in origins:
        p = sum(((x+dx,y+dy) in before) << (dx+k*dy) for dy in range(k) for dx in range(k))
        q = sum(((x+dx,y+dy) in after) << (dx+k*dy) for dy in range(k) for dx in range(k))
        if idx[p]>=0: out[idx[p]] -= 1
        if idx[q]>=0: out[idx[q]] += 1
    return out


def main(k=3, samples=300):
    rng = random.Random(87234)
    idx,classes = pattern_orbits(k)
    rows=[]; contexts=[]
    for name in DATA:
        ini,tog,orig,unk=prepare_macro(name,k)
        masks=[set(),set(unk),{p for p in unk if (p[0]+p[1])%2},
               {p for p in unk if p[0]%2},{p for p in unk if p[1]%2}]
        for _ in range(samples):
            prob=rng.random()
            masks.append({p for p in unk if rng.random()<prob})
        for outside in masks:
            rows.append(changes(ini,tog,orig,outside,k,idx,len(classes)))
            contexts.append((name,sorted(outside)))
        print(name,'unknown cells',len(unk),'patches',len(orig),flush=True)
    a=np.array(rows,dtype=np.float64)
    res=linprog(np.ones(len(classes)),A_ub=a,b_ub=-np.ones(len(rows)),bounds=(0,None),method='highs')
    print('LP',res.message,'variables',len(classes),'constraints',len(rows),flush=True)
    out={'k':k,'samples_per_macro':samples+5,'status':str(res.message),'energy':None}
    if res.success:
        out['energy']={str(c):float(w) for c,w in zip(classes,res.x) if w>1e-8}
        print('weight sum',res.fun,'nonzero',len(out['energy']),flush=True)
        print(out['energy'],flush=True)
    (BASE/f'local_energy_{k}.json').write_text(json.dumps(out,indent=2))


if __name__=='__main__':
    import sys
    main(int(sys.argv[1]) if len(sys.argv)>1 else 3, int(sys.argv[2]) if len(sys.argv)>2 else 300)
