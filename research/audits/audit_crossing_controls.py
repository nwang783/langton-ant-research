"""Independent falsification controls; these are not substitutes for proofs."""
import json, random, sys
from pathlib import Path
ROOT=Path('/workspace/shared/langton')
sys.path.insert(0,str(ROOT/'audits/transverse_snapshot'))
import crossing as c

rng=random.Random(20261022)
directions=[(2,2),(2,-2),(-2,2),(-2,-2)]
comparisons=0
for _ in range(2000):
    q=tuple(rng.randrange(-12,13) for _ in range(2))
    b=tuple(rng.randrange(-12,13) for _ in range(2))
    d=rng.choice(directions); e=rng.choice(directions)
    lo=rng.choice([None,-7,-1,0,4])
    hi=rng.choice([None,5,9,15])
    hit=c.intersect(q,d,b,e,lo,hi)
    for k in range(71):
        x=q[0]+k*d[0]-b[0]; y=q[1]+k*d[1]-b[1]
        direct=False
        if x%e[0]==0:
            j=x//e[0]
            direct=(j*e[1]==y and (lo is None or j>=lo) and (hi is None or j<=hi))
        reported=hit is not None and k>=hit[0] and (hit[1] is None or k<=hit[1])
        assert direct==reported,(q,b,d,e,lo,hi,k,hit)
        comparisons+=1

huge=10**60
assert c.intersect((0,0),(2,2),(2*huge,2*huge),(2,-2),None,None)==(huge,huge)
assert c.intersect((0,0),(2,2),(2*huge+1,2*huge),(2,-2),None,None) is None

rows=json.loads((ROOT/'scattering/transverse/crossings_discovery.json').read_text())
rejects=[]
for row in rows:
    _,_,_,static=c.first_contact(row['rotation'],row['a'],row['s'])
    field=c.Field(c.incoming_past()+static); p=(0,0); h=c.H0
    word=[]
    for _ in range(row['capture']):
        p,h,letter=field.step(p,h); word.append(letter)
    w=''.join(word[-row['cert']['period']:])
    assert c.tail(field,p,h,w)
    qs,end,eh=c.trace(w,h,p); d=c.minus(end,p)
    marker=c.plus(qs[0],c.times(huge,d))
    field.flip(marker)
    assert c.tail(field,p,h,w) is None
    rejects.append((row['rotation'],row['a'],row['s']))

out=dict(status='PASS',finite_intersection_control_comparisons=comparisons,
         exact_far_intersection_epoch=str(huge),
         far_future_marker_rejections=rejects,
         interpretation='Falsification controls supplement the exact analytic verifier audit.')
(ROOT/'audits/crossing_controls_audit.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
