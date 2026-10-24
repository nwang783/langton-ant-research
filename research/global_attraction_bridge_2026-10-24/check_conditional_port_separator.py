"""Two exact physical branches with a finite old-side exposure cut."""
import json
from pathlib import Path
P=Path(__file__).parent
j=json.loads((P/'MINIMAL_COHORT_RESTART_CHECKED.json').read_text())
catalog=json.loads((P/'OUTWARD_RECORD_GUARDS_CHECKED.json').read_text())
g=next(r for c in catalog['normal_catalog'] for r in c['records'] if r['phase']==45)
hole=(-3,-2);black=set(map(tuple,g['required_black']));white=set(map(tuple,g['required_white']))
G=black|white;seed=black-{hole};assert len(black)==15 and len(white)==4 and seed==set(map(tuple,j['initial_seed']))
D=((0,1),(1,0),(0,-1),(-1,0));n=lambda p:p[0]-p[1]
def sim(initial,T):
    B=set(initial);p=(0,0);h=1;events=[];states=[]
    for t in range(T):
        states.append((set(B),p,h));q=p;old=q in B
        if old:B.remove(q);h=(h-1)%4
        else:B.add(q);h=(h+1)%4
        events.append(dict(time=t,cell=q,black=old,incoming=states[-1][2]))
        p=(q[0]+D[h][0],q[1]+D[h][1])
    states.append((B,p,h));return events,states
ev,states=sim(seed,262)
assert ''.join('L' if e['black'] else 'R' for e in ev)==''.join(e['turn'] for e in j['events'][:262])
B,p,h=states[262];assert p==(-1,-1) and h==1
word=j['terminal_word'][58:]+j['terminal_word'][:58]
Q=[];q=p;hh=h
for c in word:
    Q.append(q);hh=(hh+(1 if c=='R' else -1))%4;q=(q[0]+D[hh][0],q[1]+D[hh][1])
assert q==(p[0]+2,p[1]-2) and hh==h and min(map(n,Q))==0
def multiple(v):
    if v[0]%2:return None
    k=v[0]//2
    return k if v[1]==-2*k else None
parity=[]
for i,q in enumerate(Q):
    thresholds=[];hits=[];critical={0}
    for z,r in enumerate(Q):
        m=multiple((r[0]-q[0],r[1]-q[1]))
        if m is not None and (m>0 or (m==0 and z<i)):thresholds.append(m);critical.add(m)
    for r in B:
        k=multiple((r[0]-q[0],r[1]-q[1]))
        if k is not None and k>=0:hits.append(k);critical|={k,k+1}
    for k in critical:assert (sum(k==a for a in hits)+sum(k>=a for a in thresholds))%2==(word[i]=='L')
    parity.append(dict(phase=i,point=q,initial_hits=hits,prior_thresholds=thresholds,tests=sorted(critical)))
first={}
for e in ev:first.setdefault(tuple(e['cell']),e['time'])
E={q for q in first if n(q)<0};ports=E-G
assert G<=E and len(E)==38 and len(ports)==19 and max(e['time'] for e in ev if n(e['cell'])<0)==261
assert not ports&seed
# The BLACK branch's whole old-side footprint is already exactly G.
baseword=j['terminal_word'];q=(0,0);hh=1;baseQ=[]
for c in baseword:
    baseQ.append(q);hh=(hh+(1 if c=='R' else -1))%4;q=(q[0]+D[hh][0],q[1]+D[hh][1])
assert q==(2,-2) and hh==1
baseold=set();baselast=-1
for i,q in enumerate(baseQ):
    k=0
    while n(q)+4*k<0:
        baseold.add((q[0]+2*k,q[1]-2*k));baselast=max(baselast,104*k+i);k+=1
assert baseold==G and baselast<262

port_controls=[]
for q in sorted(ports):
    T=first[q];pe,ps=sim(seed|{q},T+1)
    assert all(pe[i]==ev[i] for i in range(T))
    assert pe[T]['cell']==q and pe[T]['black'] and not ev[T]['black']
    port_controls.append(dict(initial_black=sorted(seed|{q}),port=q,first_disagreement=T,pose_before=[ps[T][1],ps[T][2]],source_turn='R',perturbed_turn='L'))

# Arbitrarily distant old-side material is retained, not clipped from a box.
archive={(-1000000,-999999),(999999999,1000000000),(-1000000000,5),(-7,0)}
assert all(n(q)<0 for q in archive) and not archive&E
archive_controls=[]
for isblack in (False,True):
    initial=(black if isblack else seed)|archive
    ae,ast=sim(initial,262)
    expected,_=sim(black if isblack else seed,262)
    assert ae==expected and archive<=ast[-1][0]
    assert not any(tuple(e['cell']) in archive for e in ae)
    archive_controls.append(dict(hole_black=isblack,initial_black=sorted(initial),full_final_black=sorted(ast[-1][0]),final_pose=[ast[-1][1],ast[-1][2]],archive_never_read=True))

components=[];remaining=set(ports)
while remaining:
    todo=[remaining.pop()];c=set(todo)
    while todo:
        x,y=todo.pop()
        for dx,dy in D:
            q=(x+dx,y+dy)
            if q in remaining:remaining.remove(q);c.add(q);todo.append(q)
    components.append(sorted(c))
assert sorted(map(len,components))==[9,10]
report=dict(status='AUTHOR two-branch finite separator; independent audit pending',head=[[0,0],1],pristine_normal=[1,-1],common_required_black=sorted(seed),common_required_white=sorted(white),released_bit=hole,conditional_required_white=sorted(ports),condition='common18 bits AND pristine half-plane AND (hole BLACK OR all19 additional ports WHITE)',old_side_exposure_white_branch=sorted(E),port_first_reads=sorted([first[q],q] for q in ports),port_components=components,white_branch_prefix=''.join('L' if e['black'] else 'R' for e in ev),white_branch_last_old_side_read=261,white_branch_terminal_time=262,white_branch_full_terminal_black=sorted(B),white_branch_terminal_pose=[p,h],white_branch_terminal_word=word,white_branch_terminal_drift=[2,-2],white_branch_terminal_ray_parity=parity,white_branch_tail_minimum_initial_normal=0,black_branch_old_side_exposure=sorted(baseold),black_branch_last_old_side_read=baselast,port_single_flip_controls=port_controls,huge_archive_controls=archive_controls,scope='A strict logical weakening of the complete phase45 guard, using a conditional finite port cut. Not an unconditional18-bit guard, not a universal record cover, not a necessity statement for eventual capture.')
(P/'CONDITIONAL_PORT_SEPARATOR_CHECKED.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(dict(common_bits=len(seed)+len(white),extra_ports=len(ports),port_components=list(map(len,components)),terminal_black_mass=len(B),tail_parity_tests=sum(len(r['tests']) for r in parity),black_last_old_read=baselast,white_last_old_read=261,old_side_exposure=len(E))))
