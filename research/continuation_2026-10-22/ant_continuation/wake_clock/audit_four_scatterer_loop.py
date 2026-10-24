"""Locate the exact first divergence from the planned four-turn circuit.

Only the three previously certified finite seeds are audited. This is not
an additional seed search and makes no all-scale claim.
"""
import json
from pathlib import Path
from four_scatterer_loop import build
from single_blocks import REFERENCE,block
from ant_exact import step

def planned_macro(L):
    initial,p,h,_=REFERENCE
    B=initial|block((-127,-108))
    for _ in range(104*64-875):p,h,c=step(B,p,h)
    word=[]
    for _ in range(7183+104*L):
        p,h,c=step(B,p,h);word.append(c)
    return ''.join(word)

def audit(L):
    seed,groups,starts,t0,duration=build(L)
    macro=planned_macro(L)
    assert len(macro)==duration
    B=set(seed);p=(0,0);h=0;visits={}
    for t in range(t0+4*duration):
        actual='L' if p in B else 'R'
        if t>=t0:
            expected=macro[(t-t0)%duration]
            if actual!=expected:
                return {'L':L,'first_difference_time':t,
                        'stage':(t-t0)//duration,
                        'updates_since_stage_start':(t-t0)%duration,
                        'position':p,'heading':h,
                        'expected_turn':expected,'actual_turn':actual,
                        'initially_black':p in seed,
                        'previous_reads':visits.get(p,[])}
        visits.setdefault(p,[]).append(t)
        p,h,c=step(B,p,h)
    raise AssertionError('Unexpected perfect closure')

if __name__=='__main__':
    results=[audit(L) for L in (128,192,256)]
    Path(__file__).with_name('four_scatterer_loop_first_differences.json').write_text(json.dumps(results,indent=2)+'\n')
    print(json.dumps(results,indent=2))
