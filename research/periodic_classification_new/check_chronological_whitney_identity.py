#!/usr/bin/env python3
"""Exact controls for the analytic chronological Whitney identity.
No negative finite check is a classification proof.
"""
from pathlib import Path
import json, math, random
D = ((0,1),(1,0),(0,-1),(-1,0))
def egcd(a,b):
    if b == 0: return abs(a), (1 if a > 0 else -1), 0
    g,x,y = egcd(b,a % b)
    return g,y,x-(a//b)*y

def certificate(word):
    x=y=h=0; events=[]
    for i,c in enumerate(word):
        assert c in 'RL'
        events.append((x,y,i,c,h))
        h=(h+(1 if c=='R' else -1))%4
        dx,dy=D[h]; x+=dx; y+=dy
    if h != 0 or (x,y)==(0,0): return None
    a,b=x,y; g=math.gcd(a,b); ux,uy=a//g,b//g
    _,s,t=egcd(ux,uy); classes={}
    for x,y,i,c,h in events:
        z=s*x+t*y; residue=z%g; shift=(z-residue)//g
        key=(uy*x-ux*y,residue)
        classes.setdefault(key,[]).append((-shift,i,c,h))
    K=0; contributions=[]
    for key,visits in sorted(classes.items()):
        visits.sort(); value=0
        for i,(_,_,c,h) in enumerate(visits):
            for _,_,later,hh in visits[i+1:]:
                assert (hh-h)%2 == 0
                if c=='L' and later=='R':
                    value += -1 if hh==h else 1
        K += value
        contributions.append(dict(key=key,contribution=value,visits=visits))
    excess=word.count('R')-word.count('L')
    return dict(period=len(word),drift=[a,b],excess=excess,K=K,
                verified=excess==4*K,classes=contributions)

def main():
    root=Path(__file__).resolve().parent
    standard=(root.parent/'word_stabilization/standard_word.txt').read_text().strip()
    controls={'existing_A8':certificate('RRLRRRRL'),
              'standard104':certificate(standard)}
    rng=random.Random(31); tested=0
    for _ in range(10000):
        word=''.join(rng.choice('RL') for _ in range(rng.randrange(2,51)*2))
        result=certificate(word)
        if result is not None:
            tested+=1
            assert result['verified'], (word,result)
    assert all(v['verified'] for v in controls.values())
    result={'scope':'Finite exact controls only; the theorem is analytic.',
            'random_attempts':10000,'nonzero_heading_reset_controls':tested,
            'controls':controls}
    root.joinpath('check_chronological_whitney_identity.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='controls'}))
    for name,v in controls.items():
        print(name, {k:v[k] for k in ('period','drift','excess','K','verified')})
if __name__=='__main__': main()
