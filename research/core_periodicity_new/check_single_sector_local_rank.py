"""Exact same-sector paired-rail controls for local-energy rank obstructions."""
import contextlib, io, json
from pathlib import Path
with contextlib.redirect_stdout(io.StringIO()):
    from check_reversal_rank_obstruction import step, event, F

def sector(s):
    return (s[2]-sum(s[1]))%2

def paired(n, padding=12):
    assert n>=1 and padding>=6
    B0=frozenset({(0,y) for y in range(-padding,0)}|{(0,2*n)}|
                 {(1,y) for y in range(2*n)}|
                 {(1,y) for y in range(2*n+1,2*n+padding+1)})
    X=(B0,(0,0),0)
    s=X; events1=[]; w1=''
    for _ in range(4*n):
        e=event(s);assert e['left_J'] and e['right_J'];events1.append(e['eleven'])
        s,a=step(s);w1+=a
    Y=s
    assert w1=='RLLR'*n and Y[1:]==((0,2*n),0)
    B1=frozenset({(0,y) for y in range(-padding,2*n+1)}|
                 {(1,y) for y in range(2*n+1,2*n+padding+1)})
    assert Y[0]==B1
    Z=(B1,Y[1],2)
    s=Z;events2=[];w2=''
    for _ in range(4*n):
        e=event(s);assert e['left_J'] and e['right_J'];events2.append(e['eleven'])
        s,a=step(s);w2+=a
    U=s
    assert w2=='LRRL'*n and U[1:]==((0,0),2)
    B2=frozenset({(0,y) for y in range(-padding,1)}|
                 {(1,y) for y in range(1,2*n+padding+1)})
    assert U[0]==B2
    assert all(sector(s)==0 for s in (X,Y,Z,U))
    assert B0^B2=={(0,0),(1,0),(0,2*n),(1,2*n)}
    return {'n':n,'path_length':4*n,'sector':0,'B0_mass':len(B0),
            'endpoint_difference':sorted(B0^B2),
            'first_forward_window':events1[0],'first_downward_window':events2[0],
            'forward_windows':sorted(set(events1)), 'downward_windows':sorted(set(events2))}

# Every cyclic ten-factor of either literal rail is bad.
assert all((word*4)[i:i+10] not in F for word in ('RLLR','LRRL') for i in range(4))
out={'status':'exact finite controls plus symbolic all-n construction',
     'cases':[paired(n) for n in (1,2,3,4,5,10,25,100,1000)]}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))
