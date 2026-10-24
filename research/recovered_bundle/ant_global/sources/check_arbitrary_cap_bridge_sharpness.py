#!/usr/bin/env python3
import json
from pathlib import Path
from check_arbitrary_cap_independent import audit, V


def run(k):
    initial = {(1,-3),(k+1,-k-3)} | {(r,-1-r) for r in range(2,k+2)}
    assert len(initial)==k+2
    black=set(initial)
    x,y,h=0,-4,3
    events=[]
    word=[]
    for _ in range(8+2*k):
        b=(x,y) in black
        hp=(h+(-1 if b else 1))%4
        events.append((x,y,h,hp,b))
        word.append('L' if b else 'R')
        if b: black.remove((x,y))
        else: black.add((x,y))
        dx,dy=V[hp]
        x+=dx; y+=dy; h=hp
        assert x+y<=0
    assert ''.join(word)=='RRLR'+'RL'*k+'RRLR'
    assert (x,y,h)==(k,-k-4,3)
    result=audit(events)
    expected={'M':k+1,'H':k,'rho':k-1,'D0':0,'D':k-1,
              'Jplus':1,'Q':0,'KC':0,'Z':3*k-2,'collisions':0}
    assert result==expected
    for row,n,delta in ((-1,k+2,2-k),(-2,2,-2),(-3,2,2)):
        er=[e for e in events if sum(e[:2])==row]
        assert len(er)==n and sum(1-2*e[4] for e in er)==delta
    return {'k':k,'initial_black':sorted(initial),'steps':len(events),
            'word':''.join(word),'endpoint':(x,y,h),'counts':result,
            'events':events if k<=2 else None}


def main():
    results=[run(k) for k in range(1,65)]
    Path(__file__).with_name('arbitrary_cap_bridge_sharpness.json').write_text(
        json.dumps({'status':'passed','universal_argument':'written simple-path proof',
                    'finite_controls':results},indent=2)+'\n')
    print(json.dumps({'status':'passed','k_range':[1,64],
                      'total_literal_updates':sum(r['steps'] for r in results),
                      'k1':results[0]['counts'],'k2':results[1]['counts']}))


if __name__=='__main__':main()
