"""Exact symbolic replay of a fresh diagonal record. Standard library only."""
import json
from pathlib import Path

DIRECTIONS=((0,1),(1,0),(0,-1),(-1,0))
N,E,S,W=range(4)

def replay(black, position, heading, updates):
    black=set(black)
    events=[]
    for i in range(updates):
        before=position in black
        outgoing=(heading+(-1 if before else 1))%4
        events.append({'time':i,'cell':position,'incoming':heading,'black':before,'outgoing':outgoing})
        black.symmetric_difference_update({position})
        dx,dy=DIRECTIONS[outgoing]
        position=(position[0]+dx,position[1]+dy)
        heading=outgoing
    return black,position,heading,events

def main():
    p=(0,0)
    b,pos,h,ev=replay({p},p,E,6)
    assert b=={p,(1,0),(1,1)} and pos==(-1,1) and h==W
    assert ''.join('L' if e['black'] else 'R' for e in ev)=='LRRRRL'
    assert all(sum(e['cell'])>=0 for e in ev)
    six={'events':ev,'end':{'black':sorted(b),'position':pos,'heading':h}}
    cases=[]
    q=(-1,0); z=(-1,1)
    for qc in (False,True):
        for zc in (False,True):
            seed={p}
            if qc: seed.add(q)
            if zc: seed.add(z)
            steps=8 if zc else 12
            b,pos,h,ev=replay(seed,q,S if qc else N,steps)
            assert pos==q and h==S
            assert all(e['cell']!=q for e in ev[1:])
            assert ((q in b) != qc)
            assert p in b
            assert max(sum(e['cell']) for e in ev)==2
            assert sum(1 for e in ev if sum(e['cell'])==2)==(1 if zc else 2)
            assert all(sum(e['cell'])>=0 for e in ev[1:])
            # Every read outside {p,q,z} lies in the initially white upper half-plane.
            assert all(e['cell'] in {p,q,z} or sum(e['cell'])>0 for e in ev)
            if zc:
                expected=seed.symmetric_difference({q,z,(1,0),(1,1)})
            else:
                expected=seed.symmetric_difference({q,(1,0),(1,1),(-1,2),(0,2),(0,1)})
            assert b==expected
            cases.append({'initial_q_black':qc,'initial_z_black':zc,'steps':steps,
                          'word':''.join('L' if e['black'] else 'R' for e in ev),
                          'events':ev,'end':{'black':sorted(b),'position':pos,'heading':h}})
    result={'status':'all_exact_cases_passed','six_step_macro':six,'first_returns':cases}
    target=Path(__file__).with_suffix('.json')
    target.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'first_return_cases':len(cases),'output':str(target)}))

if __name__=='__main__': main()
