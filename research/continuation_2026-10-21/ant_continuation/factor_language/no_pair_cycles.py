from pathlib import Path
from collections import deque,Counter
import json
from analyze_language import DIRS,consistent

def orbit_k(q,b,d):
    dx=q[0]-b[0];dy=q[1]-b[1]
    if d[0]:
        if dx%d[0]:return None
        k=dx//d[0]
        return k if k*d[1]==dy else None
    if dx or dy%d[1]:return None
    return dy//d[1]

def periodic_check(w):
    net=(w.count('R')-w.count('L'))%4
    if net:w*=4//__import__('math').gcd(net,4)
    x=y=d=0;ph=[]
    for i,c in enumerate(w):
        ph.append(((x,y),i,c));d=(d+(1 if c=='R'else-1))%4
        dx,dy=DIRS[d];x+=dx;y+=dy
    delta=(x,y);assert d==0
    if delta==(0,0):return {'period':len(w),'drift':delta,'reason':'zero drift','consistent_2':consistent(w*2)}
    groups=[]
    for q,i,c in ph:
        for b,vis in groups:
            a=orbit_k(q,b,delta)
            if a is not None:vis.append((a,i,c));break
        else:groups.append((q,[(0,i,c)]))
    firstL=0;bad=0;seed=[]
    for b,vis in groups:
        vis.sort(key=lambda t:(-t[0],t[1]))
        for i in range(len(vis)-1):bad+=vis[i][2]==vis[i+1][2]
        firstL+=vis[0][2]=='L'
        for n in range(min(v[0]for v in vis),max(v[0]for v in vis)):
            eligible=[v for v in vis if v[0]<=n]
            if eligible[0][2]=='L':seed.append((b[0]+n*x,b[1]+n*y))
    return {'period':len(w),'drift':delta,'bad_revisits':bad,'firstL_orbits':firstL,'finite_seed':seed if firstL==0 and bad==0 else None}

def main():
    r=json.loads(Path(__file__).with_name('no_pair_quotient.json').read_text())
    q={int(k):v for k,v in r['quotient'].items()}
    words=set()
    for u,c,v in r['bad_edges']:
        dq=deque([v]);prev={v:None}
        while dq and u not in prev:
            a=dq.popleft()
            for ch,b in q[a].items():
                if b not in prev:prev[b]=(a,ch);dq.append(b)
        if u not in prev:continue
        tail=[];a=u
        while a!=v:a,ch=prev[a];tail.append(ch)
        w=c+''.join(reversed(tail))
        words.add(min(w[i:]+w[:i] for i in range(len(w))))
    checks=[{'word':w,**periodic_check(w)}for w in sorted(words,key=lambda w:(len(w),w))]
    print('bad edges',len(r['bad_edges']),'mixed',r['mixed_flags'],'cycles',len(checks))
    for row in checks:print(row)
    Path(__file__).with_name('no_pair_cycles.json').write_text(json.dumps(checks,indent=2))

if __name__=='__main__':main()
