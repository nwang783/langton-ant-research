#!/usr/bin/env python3
"""Exact controls for the non-ant positive-face schedule. No ant simulator."""
from collections import Counter
import json
from pathlib import Path

class Schedule:
    def __init__(self):
        self.K=set(); self.B=set(); self.maxmass=0; self.moves=0
        self.fills=0; self.erases=0; self.max_fine_mass=0
    def flip(self,x,y):
        assert (x,y) not in self.K
        corners={(x,y),(x+1,y),(x,y+1),(x+1,y+1)}
        # Each local loop is a real four-read ant loop in sector sigma=-1.
        # The head is RESET before the next loop, so this is NOT one ant run.
        positive=(x+y)%2==0
        C=set(self.B); px,py=x,y; h=3 if positive else 2  # N,E,S,W
        h0=h; word='RRRR' if positive else 'LLLL'
        assert ((-1)**(px+py))*(1 if h%2==0 else -1)==-1
        dirs=((0,1),(1,0),(0,-1),(-1,0))
        for turn in word:
            assert ((px,py) in C)==(turn=='L')
            C.symmetric_difference_update({(px,py)})
            self.max_fine_mass=max(self.max_fine_mass,len(C))
            assert len(C)<=12
            h=(h+(1 if turn=='R' else -1))%4
            dx,dy=dirs[h]; px+=dx; py+=dy
        assert (px,py,h)==(x,y,h0)
        if positive:
            assert self.B.isdisjoint(corners), (x,y,'fill',self.B&corners)
            self.B |= corners; self.fills+=1
        else:
            assert corners <= self.B, (x,y,'erase',corners-self.B)
            self.B -= corners; self.erases+=1
        assert C==self.B
        self.K.add((x,y)); self.moves+=1
        self.maxmass=max(self.maxmass,len(self.B)); assert len(self.B)<=12
        D=Counter()
        for a,b in self.K:
            D[a,b]+=1; D[a+1,b]-=1; D[a,b+1]-=1; D[a+1,b+1]+=1
        D={q:v for q,v in D.items() if v}
        assert D=={q:(-1)**sum(q) for q in self.B}
        rows=Counter(); cols=Counter()
        for (a,b),v in D.items(): rows[b]+=v; cols[a]+=v
        assert all(v==0 for v in rows.values())
        assert all(v==0 for v in cols.values())
    def strip(self,x,y,h,swap=False):
        def f(a,b): self.flip(b,a) if swap else self.flip(a,b)
        f(x,y)
        for j in range(2,h,2): f(x,y+j); f(x,y+j-1)
    def bridge(self,x,y,h,swap=False):
        def f(a,b): self.flip(b,a) if swap else self.flip(a,b)
        for j in range(1,h-1,2): f(x,y+j); f(x,y+j-1)
        f(x,y+h-1)
    def grow(self,Q,side):
        a,b,w,h=Q; assert w%2 and h%2 and (a+b)%2==0
        old=set(self.K)
        if side=='L':
            self.strip(a-2,b,h); self.bridge(a-1,b,h); a-=2; w+=2
        elif side=='R':
            self.strip(a+w+1,b,h); self.bridge(a+w,b,h); w+=2
        elif side=='D':
            self.strip(b-2,a,w,True); self.bridge(b-1,a,w,True); b-=2; h+=2
        elif side=='U':
            self.strip(b+h+1,a,w,True); self.bridge(b+h,a,w,True); h+=2
        else: raise ValueError(side)
        assert old<=self.K
        assert self.K=={(x,y) for x in range(a,a+w) for y in range(b,b+h)}
        assert self.B=={(a,b),(a+w,b),(a,b+h),(a+w,b+h)}
        return a,b,w,h

s=Schedule(); s.flip(0,0); Q=(0,0,1,1); checkpoints=[]
for n in range(1,13):
    for side in 'LRDU': Q=s.grow(Q,side)
    assert Q==(-2*n,-2*n,4*n+1,4*n+1)
    checkpoints.append({'n':n,'black_mass':len(s.B),'height_area':len(s.K)})
result={'status':'PASS','is_ant_trajectory':False,'max_black_mass':s.maxmass,
        'max_fine_read_mass':s.max_fine_mass,'face_increments':s.moves,'fills':s.fills,'erases':s.erases,
        'checkpoint_controls':checkpoints}
print(json.dumps(result,indent=2))
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
