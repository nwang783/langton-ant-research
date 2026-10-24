import random,json
from collections import defaultdict
from pathlib import Path
DIRECTIONS=((0,1),(1,0),(0,-1),(-1,0))
R=random.Random(13042)
summary={}
witness={}
for trial in range(40000):
    b={(x,t-x) for x in range(-8,9) for t in range(-10,1) if R.randrange(2)}
    p=(0,-4); h=R.choice((1,3)); original=sorted(b);h0=h
    N=defaultdict(int); delta=defaultdict(int)
    H=EB=KC=Q=0
    for i in range(1000):
        t=sum(p)
        if t>0: break
        M=N[0];D=EB-M+2*H;Z=KC+2*D+H-Q
        ep = 14*(t==0)-20*(t==-1 and h==2)+6*(t==-1)-8*(t==-2 and h==3)+2*(t==-2)-2*(t==-3 and h==2)
        target=12*M-8*delta[-1]+4*delta[-2]-delta[-3]-8*D-4*Z+ep
        assert N[-3]==target,(i,t,h,N,delta,H,EB,KC,Q,D,Z,ep,target)
        key=f'{t if t>=-3 else "lower"}:{h}'
        s=summary.setdefault(key,{'min_D':100,'min_Z':100,'max_charge_gap':-100,'max_inequality_gap':-100,'n':0})
        f=N[-3]-(12*M-8*delta[-1]+4*delta[-2]-delta[-3])
        for name,value,typ in [('min_D',D,'min'),('min_Z',Z,'min'),('max_charge_gap',Q-KC-2*D-H,'max'),('max_inequality_gap',f,'max')]:
            if (typ=='min' and value<s[name]) or (typ=='max' and value>s[name]):
                s[name]=value
                witness[(key,name)]={'seed':original,'heading':h0,'steps':i,'value':value,'position':p,'end_heading':h}
        s['n']+=1
        c=p in b
        out=(h+(-1 if c else 1))%4
        if t==0 and out in (0,1): break
        N[t]+=1;delta[t]+=(-1 if c else 1)
        H+=int(t==-1 and c and h==2 and out==1)
        EB+=int(t==-2 and not c and h==3 and out==0)
        KC+=int(t==-3 and c and h==2 and out==1)
        Q+=int(t==-1 and c and h==0 and out==3)
        b.symmetric_difference_update({p})
        dx,dy=DIRECTIONS[out];p=(p[0]+dx,p[1]+dy);h=out
Path(__file__).with_suffix('.json').write_text(json.dumps({'summary':summary,'witnesses':{str(k):v for k,v in witness.items()}},indent=2))
print(json.dumps(summary,indent=2))
