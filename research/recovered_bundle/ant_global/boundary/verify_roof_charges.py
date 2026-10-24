"""Independent event-level audit of the no-freshness cap proof.
All counts come from literal coordinates and turns; no count relaxation is used.
"""
from collections import defaultdict,Counter
from pathlib import Path
import json,random
DIR=((1,0),(0,-1),(-1,0),(0,1))

def trajectory(seed,steps):
    black=set(seed); x,y,d=0,-4,2; ev=[]; ends=[]
    for t in range(steps):
        if x+y>0: break
        color=int((x,y) in black); out=(d+1-2*color)%4
        ev.append(dict(t=t,x=x,y=y,level=x+y,incoming=d,color=color,outgoing=out))
        if color:black.remove((x,y))
        else:black.add((x,y))
        dx,dy=DIR[out]; x+=dx;y+=dy;d=out
        if ev[-1]['level']==-3 and x+y==-4:ends.append(t+1)
    return ev,ends

def audit(seed,ev):
    cell=defaultdict(list)
    for e in ev:cell[(e['x'],e['y'])].append(e['t'])
    roof=[]
    for i,e in enumerate(ev[:-1]):
        a=ev[i+1]
        if e['level']==-2 and e['outgoing']==3 and a['level']==-1 and a['color']==0 and a['outgoing']==0:
            j=i+2;k=0;tops=[]
            while True:
                top=ev[j];assert top['level']==0 and top['color']==0 and top['incoming']==0 and top['outgoing']==1
                tops.append(j)
                a=ev[j+1];assert a['level']==-1 and a['incoming']==1
                if a['color']==0:
                    end=j+2;assert ev[end]['level']==-2 and ev[end]['incoming']==2
                    break
                assert a['outgoing']==0 and (a['x'],a['y']) in seed and len(cell[(a['x'],a['y'])])==1
                k+=1;j+=2
            assert end-i==4+2*k
            assert ev[end]['x']-e['x']==k
            roof.append(dict(start=i,end=end,k=k,tops=tops,right_a=end-1))
    top_indices={e['t'] for e in ev if e['level']==0}
    assert {i for r in roof for i in r['tops']}==top_indices
    assert sum(len(r['tops']) for r in roof)==len(top_indices)
    for i in top_indices:assert len(cell[(ev[i]['x'],ev[i]['y'])])==1
    bridges={e['t'] for e in ev if e['level']==-1 and e['color']==1 and e['incoming']==1 and e['outgoing']==0}
    H=len(bridges);assert H==sum(r['k'] for r in roof)
    charged={};start_zero={};end_zero={}
    for r in roof:
        if r['k']==0:
            a,b=r['start'],r['end'];assert ev[a]['color']+ev[b]['color']==1
            idx=a if ev[a]['color']==0 else b
            assert ev[idx]['incoming']==2 and ev[idx]['outgoing']==3
            assert idx not in charged
            charged[idx]=r;start_zero[a]=r;end_zero[b]=r
    EB={e['t'] for e in ev if e['level']==-2 and e['color']==0 and e['incoming']==2 and e['outgoing']==3}
    extra=EB-set(charged)
    lowerA={e['t'] for e in ev if e['level']==-1 and e['color']==1 and e['incoming']==3 and e['outgoing']==2}
    marked={i for i in lowerA if i-1 in extra or i+1 in extra}
    unmarked=lowerA-marked
    assignments=defaultdict(list)
    for i in unmarked:
        if ev[i-1]['color']==0:
            assert i-1 in charged
            a=end_zero[i-1]['start']-1
        else:a=i-2
        if ev[i+1]['color']==0:
            assert i+1 in charged
            b=start_zero[i+1]['end']+1
        else:b=i+2
        assert ev[a]['level']==-3 and ev[b]['level']==-3
        assert (ev[a]['x'],ev[a]['y'])==(ev[b]['x'],ev[b]['y'])
        assert all(e['level']>-3 for e in ev[a+1:b])
        assert lowerA.intersection(range(a+1,b))=={i}
        assert ev[a]['color']+ev[b]['color']==1
        c=a if ev[a]['color']==1 else b
        assert ev[c]['incoming']==1 and ev[c]['outgoing']==0
        assignments[c].append(dict(A=i,start=a,end=b))
    positive_right={(ev[r['right_a']]['x'],ev[r['right_a']]['y']) for r in roof if r['k']>0}
    collisions=[]
    for c,arr in assignments.items():
        assert len(arr)<=2
        if len(arr)==2:
            pair=sorted(arr,key=lambda z:z['A']);one,two=pair
            p=(ev[one['A']]['x'],ev[one['A']]['y'])
            assert p==(ev[two['A']]['x'],ev[two['A']]['y'])
            assert p in positive_right
            assert one['end']==two['start']==c
            assert not ((p in seed) and one['A']==cell[p][0])
            collisions.append(dict(C=c,A_cell=p,returns=pair))
    M=len(top_indices);J0=sum(r['k']==0 for r in roof);JP=len(roof)-J0;rho=H-JP
    D0=len(extra);D=len(EB)-M+2*H
    Q=len(lowerA);KC=sum(e['level']==-3 and e['color']==1 and e['incoming']==1 and e['outgoing']==0 for e in ev)
    Z=KC+2*D+H-Q;Z0=KC+2*D0-Q
    assert len(marked)<=2*D0
    assert len(collisions)<=JP
    assert len(assignments)>=len(unmarked)-JP
    assert KC>=Q-2*D0
    assert all(len(a)==1 for a in assignments.values())
    assert D==D0+rho and D>=0 and Z0>=0 and Z==Z0+H+2*rho
    N={s:sum(e['level']==s for e in ev) for s in (0,-1,-2,-3)}
    delta={s:sum(1-2*e['color'] for e in ev if e['level']==s) for s in N}
    assert N[-1]==4*M-delta[-1]-4*H
    assert N[-2]==8*M-4*delta[-1]+delta[-2]-8*H-4*D
    assert N[-3]==12*M-8*delta[-1]+4*delta[-2]-delta[-3]-8*D-4*Z
    return dict(steps=len(ev),M=M,H=H,J0=J0,JP=JP,rho=rho,D0=D0,D=D,Q=Q,KC=KC,Z=Z,Z0=Z0,N=N,delta=delta,collision_count=len(collisions),collisions=collisions,roofs=roof)

def main():
    rng=random.Random(20261021)
    cells=[(r,s-r) for s in (-1,-2,-3) for r in range(-1,3)]
    seeds=[{p for i,p in enumerate(cells) if mask>>i&1} for mask in range(1<<len(cells))]
    cells2=[(r,s-r) for s in range(-1,-8,-1) for r in range(-6,7)]
    seeds.extend({p for p in cells2 if rng.random()<.27} for _ in range(10000))
    counts=Counter();witnesses={}
    for num,seed in enumerate(seeds):
        ev,ends=trajectory(seed,400 if num<4096 else 2000)
        for end in ends:
            a=audit(seed,ev[:end]);counts['prefixes']+=1
            counts['with_bridge']+=a['H']>0
            counts['with_surplus']+=a['rho']>0
            counts['with_collision']+=a['collision_count']>0
            for key,test in [('bridge',a['H']>0),('surplus',a['rho']>0),('collision',a['collision_count']>0)]:
                if test and (key not in witnesses or end<witnesses[key]['audit']['steps']):
                    witnesses[key]=dict(seed=sorted(seed),audit=a,events=ev[:end])
    out=dict(exhaustive_seeds=4096,random_seeds=10000,counts=dict(counts),witnesses=witnesses)
    Path('ant_global/boundary/roof_charge_verification.json').write_text(json.dumps(out,indent=2))
    print(json.dumps({k:v for k,v in out.items() if k!='witnesses'},indent=2))
    for name,w in witnesses.items():print(name,dict(seed=w['seed'],audit={k:v for k,v in w['audit'].items() if k not in ('roofs','collisions')}))
if __name__=='__main__':main()
