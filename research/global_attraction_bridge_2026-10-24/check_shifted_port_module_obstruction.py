"""All-parameter guarded execution: remote ports shift, old return module does not."""
from pathlib import Path
import json,hashlib
from check_return_permanent_output_debt import DXY,rot,future
P=Path(__file__).parent;G={(0,-1),(1,1),(1,3),(2,2)}
B=set(G);p=(0,0);h=1;Apos=[];Q=[];Qh=[];word=''
for t in range(286):
    if t<182:Apos.append(p)
    else:Q.append(p);Qh.append(h)
    old=p in B
    if old:B.remove(p);h=(h-1)%4
    else:B.add(p);h=(h+1)%4
    word+='L' if old else 'R';p=(p[0]+DXY[h][0],p[1]+DXY[h][1])
A,U=word[:182],word[182:]
add=lambda a,b:tuple(x+y for x,y in zip(a,b))
scale=lambda a,c:tuple(c*x for x in a)
cn=lambda c:(0,0,c)
poses=[((0,0,0),(0,0,0)),((2,2,-1),(2,2,0)),((-2,2,0),(6,2,-4)),((-10,2,5),(-2,2,0)),((-6,2,0),(-6,2,8))]
headings=[1,0,3,2,1];counts=[(1,1,-4),(2,0,-5),(4,0,-6),(2,0,-7),(3,-1,-4)];parts=[61,71,61,71,14]
def point(i,q,j=(0,0,0)):
    r=rot(q,headings[i]-1);d=rot((2,2),headings[i]-1)
    return tuple(add(add(poses[i][a],cn(r[a])),scale(j,d[a])) for a in range(2))
def dot(p,n):return add(scale(p[0],n[0]),scale(p[1],n[1]))
checks=[]
def nonnegative(f,label):
    a,b,c=f;v=10*a+c
    assert v>=0 and a>=0 and a+3*b>=0,(label,f,[v,a,a+3*b])
    checks.append(dict(label=label,affine=f,vertex=v,ray_slopes=[a,a+3*b]))
sets=[]
for i in range(5):
    nonnegative(add(counts[i],cn(-1)),f'positive_R{i}')
    points=[point(i,q) for q in Apos]
    for q in Q:points.extend([point(i,q),point(i,q,add(counts[i],cn(-1)))])
    points += [point(i,Q[t],counts[i]) for t in range(parts[i])]
    sets.append(points)
    endpoint=point(i,Q[parts[i]],counts[i]);eh=(Qh[parts[i]]+headings[i]-1)%4
    assert endpoint==(poses[i+1] if i<4 else (cn(0),cn(2)))
    assert eh==(headings[i+1] if i<4 else 1)
separators=[(0,1,(0,1),(2,2,0)),(2,0,(1,-1),cn(-3)),(3,0,(1,0),cn(0)),(4,0,(1,0),cn(0)),
 (2,1,(1,0),(-2,2,1)),(3,1,(0,1),(2,2,0)),(4,1,(0,1),(2,2,0)),
 (3,2,(0,1),(-2,2,1)),(2,4,(1,-1),cn(-11)),(3,4,(1,0),(-6,2,0))]
for a,b,n,beta in separators:
    for j,q in enumerate(sets[a]):nonnegative(add(add(beta,scale(dot(q,n),-1)),cn(-1)),f'sep{a}{b}_left{j}')
    for j,q in enumerate(sets[b]):nonnegative(add(dot(q,n),scale(beta,-1)),f'sep{a}{b}_right{j}')
for i,n,sign,bound in [(1,(1,1),1,13),(3,(1,1),-1,15),(2,(1,-1),-1,45)]:
    for j,q in enumerate(sets[i]):nonnegative(add(scale(dot(q,n),sign),cn(-bound)),f'outside_Omega_{i}_{j}')
nonnegative(add(counts[0],cn(-6)),'six_stage0_epochs')
nonnegative(add(counts[4],cn(-26)),'twentysix_stage4_epochs')
omega=lambda q:q[0]>=-16 and -14<=q[0]+q[1]<=12
C=set(G)
def toggle(q):
    if q in C:C.remove(q)
    else:C.add(q)
for q in Apos:toggle(q)
for j in range(6):
    for x,y in Q:toggle((x+2*j,y+2*j))
for v in range(-26,0):
    for x,y in Q:toggle((x-8+2*v,y+2*v))
for x,y in Q[:14]:toggle((x-8,y))
C={q for q in C if omega(q)};assert len(C)==90
old=json.loads((P/'RETURN_PERMANENT_OUTPUT_DEBT_CHECKED.json').read_text())
rec=next(r for r in old['controls'] if r['name']=='protected_recovery90')
assert {(x,y-2) for x,y in C}==set(map(tuple,rec['initial_black']))
# Finite exclusions behind the constant protected-field identity.
assert min(x+y for x,y in Q)+4*6>12
assert max(x+y for x,y in Q)-8+4*(-27)<-14
for q in Apos:
    nonnegative(add(scale(dot(point(4,q),(1,1)),-1),cn(-15)),'stage4_prefix_below')
for q in G:
    nonnegative(add(scale(dot(point(4,q),(1,1)),-1),cn(-15)),'stage4_input_below')
# The translated nominal marker is permanent phase90 of the real first wake.
assert Q[90]==(6,8) and U[90]=='R'
marker_ray=[]
for i,q in enumerate(Q):
    dx,dy=6-q[0],8-q[1]
    if dx==dy and dx%2==0 and dx>=0:
        marker_ray.append([dx//2,i]);assert 104*(dx//2)+i<=90

controls=[]
for n,K in [(22,3),(40,10),(80,80)]:
    k=n//2;assert 3<=K<=3*k-30
    ev=lambda a:a[0]*k+a[1]*K+a[2]
    seed=set()
    for i in range(5):
        for q in G:seed.add(tuple(ev(a) for a in point(i,q)))
    assert len(seed)==20
    stages=[A+U*ev(counts[i])+U[:parts[i]] for i in range(5)]
    expected=''.join(stages);e=624*n-1516;assert len(expected)==e
    B={q:-i-1 for i,q in enumerate(sorted(seed))};p=(0,0);h=1;dead={};actual=[];target=(2*K,2*K+2);marker=104*K-40;at_e=None
    for t in range(e+983):
        if t==e:
            assert p==(0,2) and h==1 and B[p]==60
            assert len(B)==72*n-88 and {q for q in B if omega(q)}==C
            at_e=dict(pose=[p,h],black_count=len(B),returned_lifetime=B[p],protected90_sha256=hashlib.sha256(json.dumps(sorted(C)).encode()).hexdigest())
        old=B.pop(p,None);ch='R' if old is None else 'L'
        if t<e:assert ch==expected[t]
        if t==marker:assert p==target and old is None
        if old is None:B[p]=t;h=(h+1)%4
        else:dead[old]=t;h=(h-1)%4
        actual.append(ch);p=(p[0]+DXY[h][0],p[1]+DXY[h][1])
    tw,dr,tail,tests=future(B,p,h);dead.update({i:e+983+d for i,d in tail.items()})
    assert B[target]==marker and marker not in dead and dead[60]==e
    assert any(tw==U[i:]+U[:i] for i in range(104))
    L=sum(i in dead for i in range(-20,0));M=L
    for t,ch in enumerate(actual):L+=int(t in dead) if ch=='R' else -1;M=max(M,L)
    controls.append(dict(n=n,K=K,initial_black=sorted(seed),physical_updates=e+983,actual_return=at_e,
        translated_marker=dict(cell=target,last_R=marker,death=None),full_terminal_black_count=len(B),
        full_terminal_black_sha256=hashlib.sha256(json.dumps(sorted((q[0],q[1],i) for q,i in B.items())).encode()).hexdigest(),
        tail_pose=[p,h],tail_drift=dr,full_future_parity_tests=tests,observed_relevant_peak=M))
out=dict(status='AUTHOR all-parameter guarded architecture obstruction; independent audit pending',
         domain='integer k>=10, 0<=K<=3k-30; nominal-marker permanence additionally K>=3; n=2k',
         affine_domain_vertex=[10,0],affine_domain_rays=[[1,0],[1,3]],
         stage_period_counts=counts,stage_poses=poses,stage_partial_lengths=parts,
         complete_read_separators=separators,integer_affine_inequality_count=len(checks),
         affine_inequalities=checks,protected90=sorted(C),marker_phase90_ray_equalities=marker_ray,
         actual_old_marker_return='R60 at(0,2), death624n-1516 independent ofK',
         translated_nominal_marker='(2K,2K+2), last R104K-40, forever unread forK>=3',
         exact_first_canonical_start='624n-742 independent ofK',
         inherited_entire_relevant_cap=132,controls=controls,
         scope='Only the stated two-parameter20-cell architecture. Outside-domain probes remain named controls; no universal localization or wandering-module exclusion.')
(P/'SHIFTED_PORT_MODULE_OBSTRUCTION_CHECKED.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['affine_inequalities','protected90','controls']},indent=2))
print(json.dumps(controls,indent=2))
