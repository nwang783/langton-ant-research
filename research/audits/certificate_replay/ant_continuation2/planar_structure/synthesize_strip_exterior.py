"""Synthesize finite physical exterior connectors for a strip reset witness."""
from pathlib import Path
import json,time,sys

DIR=((0,1),(1,0),(0,-1),(-1,0))
HERE=Path(__file__).resolve().parent


def synthesize(side,connections,cap=16,node_limit=5000000):
    xs=range(-7,0) if side==0 else range(2,9)
    ys=range(-4,11)
    positions=[(x,y) for x in xs for y in ys]
    index={p:i for i,p in enumerate(positions)}
    calls=0
    began=time.time()

    def dfs(stage,p,h,known,current,seed,remaining,trace,finished):
        nonlocal calls
        calls+=1
        if calls>node_limit:raise RuntimeError('node budget')
        target=connections[stage][1]
        if p==target[:2] and h==target[2]:
            if stage+1==len(connections):
                return seed,known,current,finished+[trace]
            s=connections[stage+1][0]
            return dfs(stage+1,s[:2],s[2],known,current,seed,cap,[],finished+[trace])
        if p not in index or remaining==0:return None
        dist=abs(p[0]-target[0])+abs(p[1]-target[1])
        if dist>remaining:return None
        bit=1<<index[p]
        new=not known&bit
        options=[0,1] if new else [int(bool(current&bit))]
        successors=[]
        for c in options:
            hh=(h+(-1 if c else 1))%4
            dx,dy=DIR[hh];q=(p[0]+dx,p[1]+dy)
            dd=abs(q[0]-target[0])+abs(q[1]-target[1])
            successors.append((dd,c,hh,q))
        successors.sort()
        for dd,c,hh,q in successors:
            cc=(current&~bit) if c else (current|bit)
            ss=seed | bit if new and c else seed
            ans=dfs(stage,q,hh,known|bit,cc,ss,remaining-1,trace+[(p,h,c)],finished)
            if ans is not None:return ans
        return None

    s=connections[0][0]
    answer=dfs(0,s[:2],s[2],0,0,0,cap,[],[])
    if answer is None:return {'status':'not_found','calls':calls,'seconds':time.time()-began}
    seed,known,current,traces=answer
    return {'status':'found','calls':calls,'seconds':time.time()-began,
            'seed':[p for p in positions if seed>>index[p]&1],
            'traces':traces,'steps':[len(t) for t in traces]}


def main():
    r=json.loads((HERE/'white_strip_w2_h8.json').read_text())
    connections={0:[],1:[]}
    order=[]
    for i,s in enumerate(r['word'][:-1]):
        x,y,h,c=s['trace'][-1]
        hh=(h+(-1 if c else 1))%4
        dx,dy=DIR[hh]
        start=(x+dx,y+dy,hh)
        x,y,h,c=r['word'][i+1]['trace'][0]
        target=(x,y,h)
        side=int(start[0]>0)
        connections[side].append((start,target))
        order.append((side,len(connections[side])-1))
    cap=int(sys.argv[1]) if len(sys.argv)>1 else 16
    answers={}
    for side in (0,1):
        answers[side]=synthesize(side,connections[side],cap)
        print('side',side,{k:v for k,v in answers[side].items() if k!='traces'},flush=True)
    out={'cap':cap,'connections':connections,'order':order,'answers':answers}
    (HERE/'strip_exterior_synthesis.json').write_text(json.dumps(out,indent=2)+'\n')


if __name__=='__main__':main()
