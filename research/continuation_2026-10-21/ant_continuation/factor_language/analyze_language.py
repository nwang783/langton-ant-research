from collections import defaultdict, Counter
from pathlib import Path
import json

DIRS=((0,1),(1,0),(0,-1),(-1,0))

def simulate(n, black=(), pose=(0,0,0)):
    b=set(black); x,y,d=pose
    word=[]
    trace=[]
    for t in range(n):
        color=int((x,y) in b)
        word.append('L' if color else 'R')
        trace.append((x,y,d,color))
        b.symmetric_difference_update({(x,y)})
        d=(d+(1 if color==0 else -1))%4
        dx,dy=DIRS[d]; x+=dx;y+=dy
    return ''.join(word),b,(x,y,d),trace

def highway_word():
    w,*_=simulate(12000)
    h=w[11000:11104]
    assert w[11000:11936]==h*9
    return min(h[i:]+h[:i] for i in range(104))

def cyclic_factors(h,k):
    return {(h*((k+len(h)-1)//len(h)+1))[i:i+k] for i in range(len(h))}

def consistent(word):
    x=y=d=0; seen={}
    for c in word:
        if seen.get((x,y))==c:return False
        seen[x,y]=c
        d=(d+(1 if c=='R' else -1))%4
        dx,dy=DIRS[d];x+=dx;y+=dy
    return True

def graph(h,k):
    fs=cyclic_factors(h,k)
    edges=defaultdict(list)
    for f in sorted(fs):edges[f[:-1]].append((f[-1],f[1:]))
    return fs,edges

def extend_consistent_language(h,k,maxn):
    fs,edges=graph(h,k)
    words=sorted(fs)
    sizes={k:len(words)}
    for n in range(k+1,maxn+1):
        words=[w+c for w in words for c,_ in edges[w[-k+1:]] if consistent(w+c)]
        sizes[n]=len(words)
        if n%10==0: print('length',n,'count',len(words),flush=True)
        if len(words)>1_000_000:break
    return sizes,words

if __name__=='__main__':
    h=highway_word()
    print('Highway',h)
    print('counts',[(k,len(cyclic_factors(h,k))) for k in range(1,25)])
    for k in [10]:
        fs,g=graph(h,k)
        print('branches',[(s,v) for s,v in g.items() if len(v)>1])
        sizes,words=extend_consistent_language(h,k,180)
        bad=[w for w in words if w not in cyclic_factors(h,len(w))]
        print('sizes',sizes)
        print('nonhighway',len(bad),bad[:10])
    Path(__file__).with_name('language_results.json').write_text(json.dumps({'highway_word':h,'sizes':sizes,'nonhighway_180':bad},indent=2))
