"""Counterexample-guided exploratory max-plus height potential.

This file does not certify any invariant. A sampled transition test can only
falsify a candidate; an exact all-field oracle is needed for a theorem.
"""
from pathlib import Path
import json
import random
import sys
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
MACROS = json.loads((ROOT / 'ant_continuation/factor_language/five_macro_footprints.json').read_text())
RADIUS = 1
PATTERNS = 1 << 9
NVAR = PATTERNS + 4

def rot(p, h):
    x,y = p
    return ((x,y),(y,-x),(-x,-y),(-y,x))[h]

def representation(black, p, h):
    origins = {(x-dx,y-dy) for x,y in black for dx in range(-1,2) for dy in range(-1,2)}
    high = {PATTERNS+h:p[1]}
    for x,y in origins:
        mask = sum(1 << ((dy+1)*3+dx+1) for dy in range(-1,2) for dx in range(-1,2) if (x+dx,y+dy) in black)
        assert mask
        high[mask] = max(high.get(mask,-10**9),y)
    return high

def make_context(name, h, extra):
    d = MACROS[name]
    black = {rot(p,h) for p in d['first_L']} | set(extra)
    white = {rot(p,h) for p in d['first_R']}
    assert not black & white
    toggled = {rot(p,h) for p in d['odd_visits']}
    end = rot(d['end_pose'][:2],h)
    eh = (h+d['end_pose'][2])%4
    pre = representation(black,(0,0),h)
    post = representation(black ^ toggled,end,eh)
    return {'macro':name,'heading':h,'extra':sorted(extra),'pre':pre,'post':post}

def sample_contexts(count, seed=12345):
    rng = random.Random(seed)
    out = []
    for name,d in MACROS.items():
        for h in range(4):
            black = {rot(p,h) for p in d['first_L']}
            white = {rot(p,h) for p in d['first_R']}
            fixed = black | white
            xs,ys = zip(*fixed)
            unknown = [(x,y) for x in range(min(xs)-2,max(xs)+3) for y in range(min(ys)-2,max(ys)+3) if (x,y) not in fixed]
            out.append(make_context(name,h,[]))
            for _ in range(count):
                density = rng.choice([.1,.25,.5,.75,.9])
                extra = [p for p in unknown if rng.random()<density]
                out.append(make_context(name,h,extra))
    return out

def relax(contexts, passes=2000):
    w = np.zeros(NVAR,dtype=np.int64)
    arrays = [(np.array(list(c['pre']),dtype=np.int64),np.array(list(c['pre'].values()),dtype=np.int64),
               np.array(list(c['post']),dtype=np.int64),np.array(list(c['post'].values()),dtype=np.int64)) for c in contexts]
    log=[]
    for i in range(passes):
        old = w.copy()
        for pi,py,qi,qy in arrays:
            top = np.max(w[pi]+py)
            w[qi] = np.minimum(w[qi],top-qy)
        if i<10 or i%100==99:
            print({'pass':i+1,'minimum':int(w.min()),'head_weights':w[PATTERNS:].tolist(),'changed':int(np.sum(w!=old))},flush=True)
            log.append({'pass':i+1,'minimum':int(w.min()),'head_weights':w[PATTERNS:].tolist(),'changed':int(np.sum(w!=old))})
        if np.array_equal(w,old):
            return w,True,i+1,log
    return w,False,passes,log

def main():
    n = int(sys.argv[1]) if len(sys.argv)>1 else 20
    steps = int(sys.argv[2]) if len(sys.argv)>2 else 2000
    contexts = sample_contexts(n)
    print('contexts',len(contexts),flush=True)
    w,stable,passes,log = relax(contexts,steps)
    out={'sample_only':True,'contexts':len(contexts),'stable':stable,'passes':passes,'weights':w.tolist(),'log':log}
    Path(__file__).with_name('sample_potential.json').write_text(json.dumps(out,indent=2)+'\n')
    print({k:v for k,v in out.items() if k not in ('weights','log')},flush=True)

if __name__=='__main__':main()
