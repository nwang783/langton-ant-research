from analyze_language import *
import argparse

def state(word):
    x=y=d=0; seen={}
    for c in word:
        assert seen.get((x,y))!=c
        seen[x,y]=c
        d=(d+(1 if c=='R' else -1))%4
        dx,dy=DIRS[d]; x+=dx;y+=dy
    return seen,x,y,d

def run(pre=150,post=150):
    h=highway_word(); fs,edges=graph(h,10)
    sizes,prefixes=extend_consistent_language(h,10,pre)
    if pre==150:Path(__file__).with_name('words150.txt').write_text('\n'.join(prefixes)+'\n')
    candidates=[]
    for w in prefixes:
        seen,x,y,d=state(w)
        for c in 'LR':
            if w[-9:]+c not in fs and seen.get((x,y))!=c:
                candidates.append(w+c)
    print('bad centers',len(candidates),flush=True)
    levels=Counter(); examples=[]
    def rec(w,seen,x,y,d,k):
        levels[k]+=1
        if k==post:
            examples.append(w)
            return
        for c,dest in edges.get(w[-9:],[]):
            if seen.get((x,y))==c:continue
            old=seen.get((x,y)); seen[x,y]=c
            nd=(d+(1 if c=='R' else -1))%4
            dx,dy=DIRS[nd]
            rec(w+c,seen,x+dx,y+dy,nd,k+1)
            if old is None:del seen[x,y]
            else:seen[x,y]=old
    for n,w in enumerate(candidates):
        seen,x,y,d=state(w)
        rec(w,seen,x,y,d,0)
    print('levels',dict(sorted(levels.items())))
    print('survivors',len(examples))
    print('examples',examples[:5])
    Path(__file__).with_name(f'isolated_{pre}_{post}.json').write_text(json.dumps({'pre':pre,'post':post,'levels':dict(levels),'examples':examples},indent=2))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--pre',type=int,default=150);p.add_argument('--post',type=int,default=150)
    a=p.parse_args(); run(a.pre,a.post)
