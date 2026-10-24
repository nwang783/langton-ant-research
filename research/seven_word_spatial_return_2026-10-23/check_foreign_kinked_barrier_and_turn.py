"""Exact edge intersections, physical missed-edge controls, repaired proxy turns."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json
ROOT=Path('/workspace/shared/langton');HERE=Path(__file__).resolve().parent
P=HERE/'foreign_return_resource_locality.json';J=json.loads(P.read_text());rows=J['rows'];M='LLLLRLRRRRL'
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[0],a[1]-b[1]
def cross(a,b):return a[0]*b[1]-a[1]*b[0]
def dot(a,b):return a[0]*b[0]+a[1]*b[1]
def on(p,a,b):return cross(sub(p,a),sub(b,a))==0 and dot(sub(p,a),sub(p,b))<=0
def contact(a,b,c,d):
    u=sub(b,a);v=sub(d,c);r=sub(c,a);z=cross(u,v)
    if z:
        s=F(cross(r,v),z);t=F(cross(r,u),z)
        if 0<=s<=1 and 0<=t<=1:
            p=[F(a[k])+s*u[k]for k in range(2)]
            return dict(points=[[str(x)for x in p]],source_parameter=str(s),edge_parameter=str(t),proper=0<s<1 and 0<t<1)
        return None
    points=[p for p in sorted({a,b,c,d})if on(p,a,b)and on(p,c,d)]
    return dict(points=[list(p)for p in points],collinear=True)if points else None

def edge(q):
    x,y=q;d=(1,1)if sum(q)%2==0 else(1,-1)
    return((2*x-d[0],2*y-d[1]),(2*x+d[0],2*y+d[1]))
def rotate(q,h):
    x,y=q
    return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def center(p,h):return add((2*p[0],2*p[1]),rotate((-1,-1),h))
def cdiv(a,b):return-((-a)//b)
def inventory(a,b,ctx):
    # Necessary midpoint box from an intersecting edge2q+-d, |d_j|=1.
    lo=[cdiv(min(a[k],b[k])-1,2)for k in range(2)]
    hi=[(max(a[k],b[k])+1)//2 for k in range(2)]
    hits=[]
    for x in range(lo[0],hi[0]+1):
        for y in range(lo[1],hi[1]+1):
            q=(x,y);v=contact(a,b,*edge(q))
            if v:hits.append(dict(cell=q,in_full_context=q in ctx,intersection=v))
    return dict(start=a,end=b,candidate_box=[lo,hi],contacts=hits,missing=[r for r in hits if not r['in_full_context']])
barriers=[];controls=[]
for r in rows[4:]:
    ctx={(x,y)for x,y,b in r['requirements']};end=center(tuple(r['endpoint'][:2]),r['endpoint'][2]);old=inventory((-1,-1),end,ctx)
    points=[(-1,-1),(-7,-3)]+([]if r['name']=='F'else[end])
    pieces=[inventory(a,b,ctx)for a,b in zip(points,points[1:])]
    assert all(not p['missing']for p in pieces)
    barriers.append(dict(name=r['name'],whole_chord=old,repaired_points=points,pieces=pieces))
    if r['name']in('Q','B'):
        q=(-2,-2)if r['name']=='Q'else(-1,-2)
        hit=next(v for v in old['missing']if tuple(v['cell'])==q)
        seed=set(map(tuple,r['minimal_entry_black']))|{q};assert q not in ctx
        p=(0,0);h=0;board=set(seed);nread=0;exit_board=None
        for t,c in enumerate(r['word']+M):
            if t==len(r['word']):exit_board=sorted(board)
            assert(p in board)==(c=='L')
            nread+=int(p==q);board.symmetric_difference_update({p})
            h=(h+(-1 if c=='L'else 1))%4;p=add(p,rotate((0,1),h))
        assert nread==0 and q in board and q in set(map(tuple,exit_board))
        assert len(seed)==(21 if r['name']=='Q'else 24)
        assert len(exit_board)==len(seed)+r['mass_gain']
        controls.append(dict(name=r['name'],persistent_cell=q,seed=sorted(seed),entry_mass=len(seed),raw_exit_black=exit_board,raw_exit_mass=len(exit_board),reads_of_persistent_cell=nread,whole_chord_intersection=hit['intersection'],scope='Prepared raw foreign+actualM11 control only; no214incoming-history claim.'))
assert [len(r['whole_chord']['contacts'])for r in barriers]==[9,13,10]
assert [len(r['whole_chord']['missing'])for r in barriers]==[0,3,1]
assert [len(r['pieces'][-1]['contacts'])for r in barriers]==[9,8,9]
# Exact turn algebra uses alpha=a*pi/4+b*beta, beta=atan(1/3), 0<beta<pi/4.
alpha={'D':(1,0),'C':(1,0),'V':(2,-1),'U':(2,0),'F':(4,1),'TQ':(2,0),'TB':(2,1)}
expand={'D':['D'],'C':['C'],'V':['V'],'U':['U'],'F':['F'],'Q':['F','TQ'],'B':['F','TB']}
omega={'D':0,'C':2,'V':0,'U':0,'F':4,'TQ':0,'TB':0}
def interval_strict_inside(a,b):
    # t=beta/(pi/4) in(0,1). Endpoint equality is permitted only if variation
    # immediately enters the open interval; a constant boundary is not.
    lo=min(a,a+b);hi=max(a,a+b)
    return lo>=-4 and hi<=4 and not(b==0 and abs(a)==4)
turnrows=[]
for x in expand:
    for y in expand:
        s=expand[x][-1];t=expand[y][0]
        aa=omega[s]+alpha[t][0]-alpha[s][0];bb=alpha[t][1]-alpha[s][1]
        wrap=1 if(s,t)==('C','F')else 0
        aa-=8*wrap
        if(s,t)==('F','F'):
            assert aa==4 and bb==0
            status='excluded_by_raw_FF_infeasibility'
        else:
            assert interval_strict_inside(aa,bb)
            status='strict_principal_turn'
        turnrows.append(dict(before_macro=x,after_macro=y,before_atom=s,after_atom=t,turn_pi_over_4_coefficient=aa,turn_beta_coefficient=bb,subtract_full_turn=wrap,status=status))
for t in('TQ','TB'):
    aa=omega['F']+alpha[t][0]-alpha['F'][0];bb=alpha[t][1]-alpha['F'][1]
    assert interval_strict_inside(aa,bb)
# Physical finite CF+M11 control and exact RAW FF conflict.
def requirement(word):
    p=(0,0);h=0;odd=set();req={};first={}
    for t,c in enumerate(word):
        b=(c=='L')^(p in odd)
        if p in req and req[p]!=b:return dict(feasible=False,conflict=dict(read=t,cell=p,previous=first[p]))
        req[p]=b;first.setdefault(p,t);odd.symmetric_difference_update({p});h=(h+(-1 if c=='L'else 1))%4;p=add(p,rotate((0,1),h))
    return dict(feasible=True,seed=sorted(q for q,b in req.items()if b),endpoint=[*p,h])
word={r['name']:r['word']for r in rows};cf=requirement(word['C']+word['F']+M);ff=requirement(word['F']*2)
assert cf['feasible']and not ff['feasible']and ff['conflict']['read']==107
# The literal prefix split is a true fine cut, NOT a new marked packet.
assert word['Q'].startswith(word['F'])and word['B'].startswith(word['F'])
assert word['Q'][56:]=='LRRLRRRR'
assert word['B'][56:]=='LRLLLLRRRRLRRLRRRR'
deps=[P,ROOT/'word_stabilization/shifted1_llrlrrrrlll_fold_coalesced_port_quotient.json',ROOT/'seven_word_return_bridge_2026-10-23/manifest.json']
out=dict(status='AUTHOR_FOREIGN_KINKED_CURRENT_EDGE_BARRIER_AND_TURN_PENDING_INDEPENDENT_AUDIT',scope='Universal literal foreign-word survivor proxy, with actual full foreign RAW+M11 context. No intermediateFcore, global center simplicity, all-age U permanence or new Jordan inference.',barriers=barriers,physical_straight_chord_controls=controls,tail_words=dict(TQ=word['Q'][56:],TB=word['B'][56:]),alpha_coefficients=alpha,macro_expansions=expand,boundary_turn_rows=turnrows,CF_control=cf,FF_raw_conflict=ff,
    open_turn_formula='pi/2*[n_C-e_C_last+2(n_foreign-e_Fatom_last)-4*n_adjacent_C_foreign]+alpha_last-alpha_first',
    dependencies={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()for p in deps})
(HERE/'foreign_kinked_barrier_and_turn.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(dict(status=out['status'],whole_misses=[len(r['whole_chord']['missing'])for r in barriers],piece_contacts=[[len(p['contacts'])for p in r['pieces']]for r in barriers],CF_control_mass=len(cf['seed']),FF=ff),indent=2))
