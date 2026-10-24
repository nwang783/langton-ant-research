"""Exact active frozen-loop measurements for the standard ant."""
import json
from pathlib import Path

DIRS=((1,0),(0,-1),(-1,0),(0,1))

def step(p,h,black,flip):
    h=(h+(-1 if p in black else 1))%4
    if flip:
        if p in black: black.remove(p)
        else: black.add(p)
    dx,dy=DIRS[h]
    return (p[0]+dx,p[1]+dy),h

def loop(p,h,black):
    start=(p,h); states=[]; area=0
    while True:
        states.append((p,h))
        q,k=step(p,h,black,False)
        area+=p[0]*q[1]-p[1]*q[0]
        p,h=q,k
        if (p,h)==start: return states,area
        if len(states)>4*(len(black)+2)*4:
            raise AssertionError('Frozen loop size guard')

def experiment(n=12000):
    p=(0,0); h=3; black=set(); out=[]
    prev=None
    for t in range(n+1):
        states,area=loop(p,h,black)
        record={'t':t,'position':p,'heading':h,'black_count':len(black),
                'length':len(states),'twice_area':area,
                'opposite_on_active':(p,(h+2)%4) in states}
        if prev is not None:
            record['length_change']=len(states)-prev
        out.append(record)
        prev=len(states)
        p,h=step(p,h,black,True)
    return out

if __name__=='__main__':
    out=experiment()
    here=Path(__file__).resolve().parent
    (here/'active_loop_blank_12000.json').write_text(json.dumps(out))
    print(json.dumps({'steps':len(out)-1,'max_length':max(r['length'] for r in out),
       'positive_area_times':[r['t'] for r in out if r['twice_area']>0][:30],
       'first_24':out[:24],
       'late_lengths':[r['length'] for r in out[11000:11104]],
       'late_areas':[r['twice_area'] for r in out[11000:11104]]},indent=2))
