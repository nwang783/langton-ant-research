from analyze_language import *
from isolated_defect import state

def main(pre=150):
    h=highway_word();fs,edges=graph(h,10)
    p=Path(__file__).with_name('words150.txt')
    if p.exists():prefixes=p.read_text().splitlines()
    else:
        _,prefixes=extend_consistent_language(h,10,150)
        p.write_text('\n'.join(prefixes)+'\n')
    pred=defaultdict(set)
    for w in prefixes:pred[w[1:]].add(w[:-1])
    reach=set(cyclic_factors(h,149));front=list(reach)
    while front:
        a=front.pop()
        for v in pred[a]:
            if v not in reach:reach.add(v);front.append(v)
    print('W ancestors',len(reach),flush=True)
    starts=prefixes if pre==150 else extend_consistent_language(h,10,pre)[1]
    candidates=[]
    for w in starts:
        seen,x,y,d=state(w)
        for c in 'LR':
            if w[-9:]+c not in fs and seen.get((x,y))!=c:
                candidates.append(w+c)
    successes=[];count=0;levels=Counter()
    def rec(w,seen,x,y,d,k):
        nonlocal count
        levels[k]+=1
        if k==149:
            count+=1
            if w[-149:] in reach:successes.append(w)
            return
        for c,dest in edges.get(w[-9:],[]):
            if seen.get((x,y))==c:continue
            old=seen.get((x,y));seen[x,y]=c
            nd=(d+(1 if c=='R' else -1))%4
            dx,dy=DIRS[nd]
            rec(w+c,seen,x+dx,y+dy,nd,k+1)
            if old is None:del seen[x,y]
            else:seen[x,y]=old
    for w in candidates:
        seen,x,y,d=state(w);rec(w,seen,x,y,d,0)
    print('candidate centers',len(candidates),'full survivors',count,'successes',len(successes))
    print('success examples',successes[:3])
    Path(__file__).with_name(f'one_defect_exit_{pre}.json').write_text(json.dumps({'pre':pre,'centers':len(candidates),'survivors':count,'reach_count':len(reach),'successes':successes,'levels':dict(levels)},indent=2))
    return len(successes)

if __name__=='__main__':
    import sys
    main(int(sys.argv[1]) if len(sys.argv)>1 else 150)
