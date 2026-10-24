from collections import defaultdict,Counter
from pathlib import Path
H=Path(__file__).with_name('standard_word.txt').read_text().strip()
D=((0,1),(1,0),(0,-1),(-1,0))
F10={ (H*2)[i:i+10] for i in range(104)}
succ=defaultdict(list)
for f in sorted(F10):succ[f[:-1]].append(f[-1])
def apply(p,h,known,c):
    if p in known and known[p]!=c:return
    k=known.copy();k[p]='R' if c=='L' else 'L'
    h=(h+(-1 if c=='L' else 1))%4
    return ((p[0]+D[h][0],p[1]+D[h][1]),h,k)
def interpret(w):
    p=(0,0);h=0;known={}
    for c in w:
        a=apply(p,h,known,c)
        if a is None:return
        p,h,known=a
    return (w,p,h,known)
states=[]
for w in sorted(succ):
    s=interpret(w)
    if s:states.append(s)
for n in range(9,150):
    canon={(H*((n+103)//104+1))[i:i+n] for i in range(104)}
    ws={s[0] for s in states}; extra=ws-canon;miss=canon-ws
    print(n,len(states),'extra',len(extra),'miss',len(miss),flush=True)
    if n>=21 and not extra:
        print('CERTIFIED finite local implication at length',n);break
    if len(states)>2000000:break
    new=[]
    for w,p,h,known in states:
        for c in succ[w[-9:]]:
            a=apply(p,h,known,c)
            if a is not None:new.append((w+c,*a))
    states=new
if n>=21 and not extra:
    Path(__file__).with_name('forcing_horizon.txt').write_text(str(n)+'\n')
