"""All-even-n sixteen-cell moving old module with an exact protected future."""
from pathlib import Path
import json,hashlib
from check_return_permanent_output_debt import DXY,rot,future,case
P=Path(__file__).parent;G={(0,-1),(1,1),(1,3),(2,2)}
B=set(G);p=(0,0);h=1;AP=[];Q=[];Qh=[];s=''
for t in range(286):
    if t<182:AP.append(p)
    else:Q.append(p);Qh.append(h)
    old=p in B
    if old:B.remove(p);h=(h-1)%4
    else:B.add(p);h=(h+1)%4
    s+='L' if old else 'R';p=(p[0]+DXY[h][0],p[1]+DXY[h][1])
A,U=s[:182],s[182:]
add=lambda a,b:(a[0]+b[0],a[1]+b[1]);neg=lambda a:(-a[0],-a[1]);mul=lambda a,c:(a[0]*c,a[1]*c);cn=lambda c:(0,c)
poses=[(cn(0),cn(0)),((14,-1),(14,0)),((10,0),(18,-4)),((2,5),(10,0))]
heads=[1,0,3,2];rs=[(7,-4),(2,-5),(4,-6),(2,-6)];parts=[61,71,61,56];target=((6,0),(6,3))
def point(i,q,j=(0,0)):
    r=rot(q,heads[i]-1);d=rot((2,2),heads[i]-1)
    return tuple(add(add(poses[i][a],cn(r[a])),mul(j,d[a])) for a in range(2))
def dot(q,n):return add(mul(q[0],n[0]),mul(q[1],n[1]))
def relative(q):return tuple(add(q[a],neg(target[a])) for a in range(2))
ineq=[]
def nonneg(f,label):
    a,b=f;assert a>=0 and 10*a+b>=0,(label,f)
    ineq.append(dict(label=label,affine=f,at_k10=10*a+b,slope=a))
V=[]
for i in range(4):
    nonneg(add(rs[i],cn(-1)),f'positive_R{i}')
    v=[point(i,q) for q in AP]
    for q in Q:v += [point(i,q),point(i,q,add(rs[i],cn(-1)))]
    v += [point(i,Q[t],rs[i]) for t in range(parts[i])];V.append(v)
    assert point(i,Q[parts[i]],rs[i])==(poses[i+1] if i<3 else target)
    assert (Qh[parts[i]]+heads[i]-1)%4==(heads[i+1] if i<3 else 2)
seps=[(0,1,(0,1),(14,0)),(2,0,(1,-1),cn(-3)),(3,0,(1,-1),cn(-3)),
      (2,1,(1,0),(10,1)),(3,1,(0,1),(14,0)),(3,2,(0,1),(10,1))]
for a,b,n,beta in seps:
    for j,q in enumerate(V[a]):nonneg(add(add(beta,neg(dot(q,n))),cn(-1)),f'sep{a}{b}_a{j}')
    for j,q in enumerate(V[b]):nonneg(add(dot(q,n),neg(beta)),f'sep{a}{b}_b{j}')
source=json.loads((P/'TRANSVERSE_FAR_MODULE_SOURCE.json').read_text());bounds=source['protected_bounds'];assert bounds==dict(Smin=-73,Smax=17,Tmin=-20)
inside=lambda q:-73<=q[0]+q[1]<=17 and q[0]-q[1]>=-20
for q in V[1]:nonneg(add(dot(relative(q),(1,1)),cn(-18)),'stage1_above')
for q in V[2]:nonneg(add(neg(dot(relative(q),(1,-1))),cn(-21)),'stage2_left')
for q in AP+list(G):
    nonneg(add(neg(dot(relative(point(0,q)),(1,1))),cn(-74)),'source_launch_below')
    nonneg(add(neg(dot(relative(point(3,q)),(1,-1))),cn(-21)),'return_launch_left')
for t in range(parts[0]):nonneg(add(dot(relative(point(0,Q[t],rs[0])),(1,1)),cn(-18)),'outgoing_partial_above')
# Fixed restricted XOR from both complete genuine read histories.
C=set()
def toggle(q):
    if q in C:C.remove(q)
    else:C.add(q)
for v in range(-30,36):
    for x,y in Q:toggle((x+2*v,y-3+2*v))
for v in range(-20,-6):
    for q in Q:
        x,y=rot(q,1);toggle((x+5+2*v,y-3-2*v))
for q in Q[:56]:
    x,y=rot(q,1);toggle((x+5-12,y-3+12))
C={q for q in C if inside(q)};assert len(C)==330 and C==set(map(tuple,source['protected_black']))
assert max(x+y-3+4*(-31) for x,y in Q)<-73
assert min(x+y-3+4*36 for x,y in Q)>17
assert max(8+x+y+4*(-21) for x,y in Q)<-20
# Every complete marked-lifetime pose escapes fixed physical bands as n grows.
suffix=[point(0,Q[t],(3,-3)) for t in range(72,104)]
for q in Q:suffix += [point(0,q,(3,-2)),point(0,q,add(rs[0],cn(-1)))]
suffix += [point(0,Q[t],rs[0]) for t in range(parts[0])]
suffix += V[1]+V[2]+V[3]+[target]
for q in suffix:
    nonneg(add(q[0],neg((2,3))),'marked_x_ge_n_plus3')
    nonneg(add(q[1],neg((6,-5))),'marked_y_ge_3n_minus5')
assert Q[71]==(6,9) and U[71]=='R'
align=[]
for i,q in enumerate(Q):
    dx,dy=6-q[0],9-q[1]
    if dx==dy and dx%2==0 and dx>=0:align.append([dx//2,i]);assert 104*(dx//2)+i<=71
# Full fixed protected dynamics, not a finite repeat observation.
F,Z=source['post_contact_word'],source['tail_word'];assert len(F)==8986 and len(Z)==104 and F[-1]!=Z[-1]
BB={q:-i-1 for i,q in enumerate(sorted(C))};pp=(0,0);hh=2
for t,ch in enumerate(F):
    assert inside(pp);old=BB.pop(pp,None);assert (old is None)==(ch=='R')
    if old is None:BB[pp]=t;hh=(hh+1)%4
    else:hh=(hh-1)%4
    pp=(pp[0]+DXY[hh][0],pp[1]+DXY[hh][1])
tw,dr,tail,tests=future(BB,pp,hh);assert tw==Z and dr==(2,-2) and (pp,hh)==((17,-13),2)
qq=pp;h2=hh
for ch in Z:
    assert inside(qq);h2=(h2+(1 if ch=='R' else -1))%4;qq=(qq[0]+DXY[h2][0],qq[1]+DXY[h2][1])
assert any(Z==U[i:]+U[:i] for i in range(104))
rc=case('protected_transverse330',C,2,8986+208)
assert rc['relevant_mass_max']==432 and sum(z['death'] is not None for z in rc['initial_read_fates'])==285
# Pruned field and all-future relevance profile close after one further period.
B0={tuple(z['cell']):z['lifetime'] for z in rc['terminal_black']};p0=tuple(rc['terminal_pose'][0]);h0=rc['terminal_pose'][1];N=rc['physical_updates']
w0,d0,t0,_=future(B0,p0,h0);C0={q for q,i in B0.items() if i in t0};DD={};ev=[];BB=dict(B0);pp=p0;hh=h0
for i in range(104):
    old=BB.pop(pp,None);ev.append(old)
    if old is None:BB[pp]=N+i;hh=(hh+1)%4
    else:DD[old]=i;hh=(hh-1)%4
    pp=(pp[0]+DXY[hh][0],pp[1]+DXY[hh][1])
w1,d1,t1,_=future(BB,pp,hh);DD.update({i:104+t for i,t in t1.items()});C1={q for q,i in BB.items() if i in t1}
assert w1==w0 and d1==d0 and C1=={(x+2,y-2) for x,y in C0}
L=len(C0);profile=[L]
for i,old in enumerate(ev):L+=int(N+i in DD) if old is None else -1;profile.append(L)
assert max(profile)<=432
controls=[]
for n in (20,40,80):
    k=n//2;ev=lambda a:a[0]*k+a[1];seed={tuple(ev(a) for a in point(i,q)) for i in range(4) for q in G};assert len(seed)==16
    expected=''.join(A+U*ev(rs[i])+U[:parts[i]] for i in range(4));c=780*n-1207;b=156*n-59;q0=(3*n,3*n+3);assert len(expected)==c
    BB={q:-i-1 for i,q in enumerate(sorted(seed))};pp=(0,0);hh=1
    for t,ch in enumerate(expected+F+Z*2):
        if t==b:assert pp==q0 and pp not in BB
        if t==c:
            assert pp==q0 and hh==2 and BB[pp]==b
            actualC={(x-q0[0],y-q0[1]) for x,y in BB if inside((x-q0[0],y-q0[1]))};assert actualC==C
        old=BB.pop(pp,None);assert (old is None)==(ch=='R')
        if old is None:BB[pp]=t;hh=(hh+1)%4
        else:hh=(hh-1)%4
        pp=(pp[0]+DXY[hh][0],pp[1]+DXY[hh][1])
    zw,dw,tt,ct=future(BB,pp,hh);assert zw==Z and dw==(2,-2)
    controls.append(dict(n=n,initial_black=sorted(seed),physical_updates=len(expected+F+Z*2),
        marked_lifetime=dict(cell=q0,birth=b,death=c,age=c-b),exact_first_canonical_start=c+8986,
        full_terminal_black_count=len(BB),full_terminal_pose=[pp,hh],parity_tests=ct,
        full_terminal_sha256=hashlib.sha256(json.dumps(sorted((q[0],q[1],i) for q,i in BB.items())).encode()).hexdigest()))
out=dict(status='AUTHOR all-even-n>=20 theorem; independent audit pending',parameter_domain='n=2k, integer k>=10',
    complete_read_separators=seps,integer_affine_inequality_count=len(ineq),affine_inequalities=ineq,
    protected_bounds=bounds,protected_black=sorted(C),protected_initial_relevant=285,
    protected_all_future_relevant_max=432,protected_reference=rc,pruned_period_relevance_profile=profile,
    source_word_tail_ray_tests=tests,marked_source_phase71_alignments=align,
    entire_relevant_cap=max(16+22+330,432),marked_position='(3n,3n+3)',marked_birth='156n-59',marked_death='780n-1207',
    marked_age='624n-1148',marked_excursion_lower_bounds=['x>=n+3','y>=3n-5'],
    exact_first_canonical_start='780n+7779',controls=controls,
    scope='One complete finite capturing orbit per parameter, with a genuinely moving old module and fixed relevant cap432. No single orbit with infinitely many unbounded-age returns or failure of eventual orbit-dependent boundedness.')
(P/'TRANSVERSE_FAR_MODULE_CHECKED.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['affine_inequalities','protected_black','protected_reference','pruned_period_relevance_profile','controls']},indent=2))
print(json.dumps(controls,indent=2))
