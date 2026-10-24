"""Relaxed exact white-strip reset search.

The exterior is a nondeterministic connector: after leaving one side, any
sector-compatible entrance on the SAME side may be selected. Thus failure to
reset is rigorous for the tested finite-height strip, while a reset witness
still needs a physically realizable exterior.
"""
from collections import deque
import json,sys,time
from pathlib import Path

DIR=((0,1),(1,0),(0,-1),(-1,0))
HERE=Path(__file__).resolve().parent


def crossing(mask,w,H,side,y):
    p=(0 if side==0 else w-1,y)
    h=1 if side==0 else 3
    trace=[]
    while 0<=p[0]<w:
        x,y=p
        if not 0<=y<H:
            return None
        j=x*H+y
        c=(mask>>j)&1
        trace.append((x,y,h,c))
        mask ^= 1<<j
        h=(h+(-1 if c else 1))%4
        dx,dy=DIR[h]
        p=x+dx,y+dy
        assert len(trace)<10000
    return mask,int(p[0]>=w),p,h,trace


def search(w,H):
    entrances={s:[y for y in range(H) if ((0 if s==0 else w-1)+y)%2] for s in (0,1)}
    start=(0,0,False)
    prev={start:None}
    q=deque([start])
    count=0
    while q:
        state=q.popleft()
        mask,side,visited_right=state
        for y in entrances[side]:
            c=crossing(mask,w,H,side,y)
            if c is None:continue
            mask2,side2,p,h,trace=c
            flag=visited_right or side2==1
            nxt=(mask2,side2,flag)
            if nxt in prev:continue
            prev[nxt]=(state,y,trace)
            if mask2==0 and flag:
                words=[]
                at=nxt
                while prev[at] is not None:
                    st,y,tr=prev[at]
                    words.append({'from':st,'entry_y':y,'trace':tr,'to':at})
                    at=st
                words.reverse()
                return {'width':w,'height':H,'status':'relaxed_reset',
                        'states':len(prev),'macro_steps':len(words),'word':words}
            q.append(nxt)
        count+=1
    return {'width':w,'height':H,'status':'no_relaxed_reset','states':len(prev)}


if __name__=='__main__':
    w=int(sys.argv[1]) if len(sys.argv)>1 else 2
    H=int(sys.argv[2]) if len(sys.argv)>2 else 8
    t=time.time();r=search(w,H);r['seconds']=time.time()-t
    (HERE/f'white_strip_w{w}_h{H}.json').write_text(json.dumps(r,indent=2)+'\n')
    print(json.dumps({k:v for k,v in r.items() if k!='word'},indent=2))
    if 'word' in r:
        for step in r['word']:
            print(step['from'],step['entry_y'],''.join('L' if z[3] else 'R' for z in step['trace']),step['to'])
