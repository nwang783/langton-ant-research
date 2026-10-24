"""Exact same-sector standard-wake guards for D=LLLLRLRRRR."""
import json,hashlib
from collections import defaultdict,Counter
from pathlib import Path
from periodic_wake_fronts import D as DIR,T,W,add,orbit_key
# Bind the imported wake to the pinned canonical W104 provenance.
assert hashlib.sha256(W.encode()).hexdigest()=='9772fa0cced75fab3a1d336c6a1326e0e4be8f4e471a3807e0778fccc94c1f04'
wp=(0,0);wh=3;wc=Counter()
for letter in W:
    wc[(wp[0]-wp[1],wp[0]%2)]+=1
    wh=(wh+(1 if letter=="R" else -1))%4;wp=add(wp,DIR[wh])
assert (wp,wh)==((-2,-2),3)
assert T=={c for c,n in wc.items() if n%2}

WORD='LLLLRLRRRR'
p0=(0,-1);p=p0;h=0;reads=[];w=WORD*2
for i,c in enumerate(w):
    reads.append(p);h=(h+(1 if c=='R' else -1))%4;p=add(p,DIR[h])
assert h==0 and p==(2,1)
groups=defaultdict(list)
for i,q in enumerate(reads):
    c,k=orbit_key(q,(2,2));groups[c].append((k,i,w[i]))
guard={};witnesses=[]
for c,seq in groups.items():
    seq.sort(key=lambda z:(-z[0],z[1]))
    assert all(a[2]!=b[2] for a,b in zip(seq,seq[1:]))
    guard[(c[0]-c[1],c[0]%2)]=seq[0][2]=='L'
    witnesses.append(reads[seq[0][1]])
black=sorted(k for k,v in guard.items() if v)
white=sorted(k for k,v in guard.items() if not v)
assert black==[(0,0),(0,1)]
assert white==[(1,0),(1,1),(2,0),(2,1),(3,0),(3,1)]
rails=[]
for rot in (0,2):
    base={(t if rot==0 else -t,a) for t,a in T}
    for delta in range(min(t for t,a in black)-max(t for t,a in base),
                       max(t for t,a in black)-min(t for t,a in base)+1):
        if delta%2:continue
        for parity in (0,1):
            S={(t+delta,(a+parity)%2) for t,a in base}
            bm=sum(1<<i for i,k in enumerate(black) if k in S)
            wm=sum(1<<i for i,k in enumerate(white) if k in S)
            if bm:rails.append({'rotation':rot,'offset':delta,'parity':parity,'black':bm,'white':wm})
costs=[]
for allowed in range(1<<len(white)):
    covered=bad=0
    for row in rails:
        if row['white']&~allowed==0:
            covered|=row['black'];bad|=row['white']
    costs.append(len(black)-covered.bit_count()+bad.bit_count())
assert min(costs)==2
widths=[max(p[i] for p in witnesses)-min(p[i] for p in witnesses) for i in (0,1)]
assert max(widths)<=9
out={'canonical_W_sha256':hashlib.sha256(W.encode()).hexdigest(),'word':WORD,'two_period_drift':[2,2],'same_sector_start':[list(p0),0],
     'required_black':black,'required_white':white,'first_read_witnesses':witnesses,
     'witness_coordinate_widths':widths,'helpful_rail_profiles':rails,
     'white_subsets_checked':len(costs),'minimum_union_guard_error':min(costs),
     'costs':costs,
     'scope':'all finite caps and offsets on one rail, and all same-sector parallel rail unions; finite-rail history extension requires its separate endpoint ledger'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
print(json.dumps({k:v for k,v in out.items() if k not in ('helpful_rail_profiles','costs')},indent=2))
