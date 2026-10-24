"""Exact standard-positive regression against conserved normalized capacity."""
from pathlib import Path
import json
from check_return_permanent_output_debt import DXY,future
P=Path(__file__).parent
G={(0,-1),(1,1),(1,3),(2,2)};B={q:-i-1 for i,q in enumerate(sorted(G))};p=(0,0);h=1
for t in range(182):
    old=B.pop(p,None)
    if old is None:B[p]=t;h=(h+1)%4
    else:h=(h-1)%4
    p=(p[0]+DXY[h][0],p[1]+DXY[h][1])
assert p==(5,1) and h==1 and len(B)==36
source=dict(B);word,drift,tail,tests=future(B,p,h);assert drift==(2,2)
Q=[];R=[]
for i,c in enumerate(word):
    Q.append(p);old=B.pop(p,None);assert (old is None)==(c=='R')
    if old is None:B[p]=182+i;h=(h+1)%4;R.append((i,p))
    else:h=(h-1)%4
    p=(p[0]+DXY[h][0],p[1]+DXY[h][1])
permanent=[];returning=[]
for phase,q in R:
    later=[];equalities=[]
    for i,r in enumerate(Q):
        dx,dy=q[0]-r[0],q[1]-r[1]
        if dx==dy and dx%2==0 and dx>=0:
            m=dx//2;equalities.append([m,i])
            if 104*m+i>phase:later.append([m,i])
    if not later:permanent.append(dict(phase=phase,cell=q,all_nonnegative_ray_equalities=equalities))
    else:returning.append(dict(phase=phase,cell=q,death=min(104*m+i for m,i in later)))
assert len(permanent)==12
marked=next(r for r in returning if r['phase']==68);assert marked==dict(phase=68,cell=(7,7),death=184)
marked['age']=116
marked['permanent_births_in_return']=sum(68<104*k+r['phase']<184 for k in range(2) for r in permanent)
assert marked['permanent_births_in_return']==13
Sreturn={(r['cell'][0]+2*k,r['cell'][1]+2*k) for k in range(2) for r in permanent if 68<104*k+r['phase']<184}
assert len(Sreturn)==13 and len(Sreturn & {(x+2,y+2) for x,y in Sreturn})==1
for a in Sreturn:
    for b in Sreturn:
        dx,dy=a[0]-b[0],a[1]-b[1]
        assert dx!=dy or dx%2 or abs(dx//2)<=1
marked['permanent_return_support']=sorted(Sreturn)
marked['adjacent_translated_support_overlap']=1
marked['K_return_physical_support_count']='12K+1 for K>=1'
W={tuple(r['cell']) for r in permanent}
for a in W:
    for b in W:
        dx,dy=a[0]-b[0],a[1]-b[1]
        assert dx!=dy or dx%2 or a==b
# Literal rectangle union and exact translated-new-area checks.
checks=0
for w,H in [(1,1),(3,7),(150,9)]:
    S={(x,y) for x in range(w) for y in range(H)}
    for dx,dy in [(0,0),(1,0),(-1,2),(2,2),(w+1,H+1)]:
        T={(x+dx,y+dy) for x,y in S}
        new=len(T-S);formula=w*H-max(0,w-abs(dx))*max(0,H-abs(dy))
        assert new==formula<=H*abs(dx)+w*abs(dy);checks+=1
out=dict(status='AUTHOR positive regression and analytic moving-band correction; independent audit pending',
         source_black=sorted(source),source_pose=[[5,1],1],source_time=182,
         full_infinite_parity_tests=tests,word=word,drift=drift,
         actual_permanent_phase_cells=permanent,normalized_permanent_slot_count=12,
         translating_marked_return=marked,
         physical_union_counts=[dict(periods=k,count=12*k) for k in (1,2,17,10**9)],
         all_integer_translate_disjointness=True,rectangle_formula_controls=checks,
         scope='Canonical positive regression; does not satisfy unbounded-age or guard-avoiding hypotheses. Rules out treating a recurring normalized finite output pattern as conserved physical capacity.')
(P/'MOVING_CAPACITY_REGRESSION_CHECKED.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['source_black','word','actual_permanent_phase_cells']},indent=2))
