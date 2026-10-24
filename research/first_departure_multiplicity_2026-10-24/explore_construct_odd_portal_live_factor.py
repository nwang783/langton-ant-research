"""Constructive guide routing for one SPECIFIED odd-root mixed incoming portal interface.
Not a front, period, multiplicity or support-width scan. A failure is only a
routing failure and is not promoted as an impossibility statement.
"""
from pathlib import Path
from collections import Counter
import ast, json, random, time, os
b = Path(__file__).parent
raw = json.loads((b/'explore_odd_root_portal_upper_completion.json').read_text())
options=[r['histories'] for r in raw['open'] if r['histories']['(1, 1)']=='SSNS' and r['histories']['(1, 0)']=='W' and r['histories']['(2, 0)']=='SSN' and r['histories']['(1, 3)']=='N']
option=min(options,key=lambda h:sum(map(len,h.values())))
core={ast.literal_eval(p):h for p,h in option.items()}
L = {'__file__':str(b/'check_even_reader_rail_and_merge_reset.py')}
exec((b/'check_even_reader_rail_and_merge_reset.py').read_text().split('rows=[]')[0], L)
su,components,order,calendar = L['graph'](core)
H = 'NESW'
V = {'N':(0,1),'E':(1,0),'S':(0,-1),'W':(-1,0)}
rng = random.Random(int(os.environ.get('ROUTING_SEED','281947')))
# Rank-valid whole-component orders, not arbitrary chronological windows.
component_of = {e:i for i,c in enumerate(components) for e in c}
links = {i:set() for i in range(len(components))}
indegree = [0]*len(components)
for p,h in core.items():
    for r in range(len(h)-1):
        i,j = component_of[p,r],component_of[p,r+1]
        if i != j and j not in links[i]: links[i].add(j);indegree[j]+=1
ready = [i for i in range(len(components)) if indegree[i]==0]
order = []
while ready:
    i = ready.pop(rng.randrange(len(ready)));order.append(i)
    for j in links[i]:
        indegree[j]-=1
        if indegree[j]==0:ready.append(j)
assert len(order)==len(components)
black = set()
seen = set(core)
seed = set()
visits = Counter()
hist = {p:[] for p in core}
word = ''
pose = components[order[0]][0][0], core[components[order[0]][0][0]][0]
route_log = []

def step(pose, tr):
    p,h = pose
    nh = H[(H.index(h)+(1 if tr=='R' else -1))%4]
    dx,dy = V[nh]
    return (p[0]+dx,p[1]+dy),nh

def route(start, goal):
    # beam entries: pose,current black,seen guides,seed guides,visits,path
    frontier = [(start,frozenset(black),frozenset(seen),frozenset(seed),dict(visits),'')]
    for depth in range(121):
        new = []
        keys = set()
        for at,board,old,initial,count,path in frontier:
            if at == goal:
                return at,set(board),set(old),set(initial),Counter(count),path
            p,h = at
            if p in core:
                continue
            if count.get(p,0)>=4:
                continue
            choices = ['L' if p in board else 'R'] if p in old else ['R','L']
            for tr in choices:
                nxt = step(at,tr)
                q,nh = nxt
                if q in core and nxt != goal:
                    continue
                if not (-9 <= q[0] <= 10 and -9 <= q[1] <= 10):
                    continue
                nb = set(board)
                ni = set(initial)
                no = set(old)
                if p not in old:
                    no.add(p)
                    if tr=='L':ni.add(p);nb.add(p)
                assert (p in nb) == (tr=='L')
                nb.symmetric_difference_update({p})
                nc = dict(count);nc[p]=nc.get(p,0)+1
                key = (nxt,frozenset(nb),frozenset(no))
                if key in keys:
                    continue
                keys.add(key)
                dist = abs(q[0]-goal[0][0])+abs(q[1]-goal[0][1])
                if q==goal[0] and nh!=goal[1]: dist += 4
                reuse = sum(max(0,n-1) for n in nc.values())
                score = dist + 0.045*(depth+1) + 0.015*reuse + rng.random()*0.015
                new.append((score,nxt,frozenset(nb),frozenset(no),frozenset(ni),nc,path+tr))
        if not new:
            return None
        new.sort(key=lambda z:z[0])
        frontier = [(at,board,old,initial,count,path) for _,at,board,old,initial,count,path in new[:600]]
    return None

for number,i in enumerate(order):
    comp = components[i]
    first = comp[0]
    goal = first[0],core[first[0]][first[1]]
    if pose != goal:
        starttime = time.time()
        ans = route(pose,goal)
        if ans is None:
            print('ROUTE FAILED',number,i,pose,goal,flush=True)
            raise SystemExit(2)
        pose,black,seen,seed,visits,path = ans
        word += path
        route_log.append(dict(component=i,guide_word=path,seconds=time.time()-starttime))
        print('ROUTE',number,i,len(path),'total',len(word),flush=True)
    for p,r in comp:
        assert pose == (p,core[p][r]),(i,p,r,pose)
        assert len(hist[p])==r
        tr = 'R' if r%2==0 else 'L'
        assert ('L'if p in black else'R') == tr
        hist[p].append(dict(t=len(word),incoming=pose[1],turn=tr))
        black.symmetric_difference_update({p});visits[p]+=1
        pose=step(pose,tr);word+=tr
print('SUCCESS',len(word),'seed',len(seed),'max',max(visits.values()),'end',pose,flush=True)
obj = dict(scope=__doc__,core={str(p):h for p,h in core.items()},word=word,initial_black=sorted(seed),
    start=[components[order[0]][0][0],core[components[order[0]][0][0]][0]],end=pose,final_black=sorted(black),
    target_histories={str(p):z for p,z in hist.items()},factor_max_reads=max(visits.values()),route_log=route_log,
    warning='Author discovery only until independently replayed from the complete prelaid seed. No complete WHITE/global-M/front/controller claim.')
Path(__file__).with_name('prepared_odd_portal_live_candidate_'+os.environ.get('ROUTING_SEED','281947')+'.json').write_text(json.dumps(obj,indent=2)+'\n')
