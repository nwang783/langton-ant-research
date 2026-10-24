"""Exact two-macro spatial composition controls, not an unrestricted scan.
The proof uses persistent complete star components; every literal test retains B.
"""
from pathlib import Path
from itertools import product
import sys,json,hashlib
ROOT=Path('/workspace/shared/langton');OUT=Path(__file__).parent
sys.path.insert(0,str(ROOT/'reframe_finite_seed_2026-10-24'))
from active_flight import rot,cursor,ends,sector,vertices,comp,step
SRC=ROOT/'reframe_finite_seed_2026-10-24/kernel_M5_scc.json'
J=json.loads(SRC.read_text());A=J['first_return_cycles'][0];C=J['first_return_cycles'][11]
assert A['word']=='RRRRL' and C['word']=='RRRRLRL'
MAC={'A':A,'C':C}

def add(p,q):return p[0]+q[0],p[1]+q[1]
def trans(S,p,h):return {add(p,rot(tuple(q),h))for q in S}
def ports(C,p,h,k):
    V=vertices(C,k)|{cursor(p,h)};P=set()
    for x,y in V:
        for sx,sy in product((-1,1),repeat=2):
            q=((x+sx)//2,(y+sy)//2)
            assert (x,y)in ends(q,k)
            P.add(q)
    return P

def plan(letters):
    p=(0,0);h=0;records=[];k=sector(p,h)
    for letter in letters:
        macro=MAC[letter]
        for local in macro['transitions']:
            B=trans(local['input_component'],p,h)
            assert comp(B,k,cursor(p,h))==B
            records.append(dict(p=p,h=h,C=B,turn=local['turn']))
            pn=add(p,rot(tuple(local['output_pose'][0]),h));hn=(h+local['output_pose'][1])%4
            N=trans(local['output_active'],p,h)
            expected=trans(J['first_return_cycles'][0]['transitions'][0]['input_component'],pn,hn) if False else None
            p,h=pn,hn
        assert not N
    records.append(dict(p=p,h=h,C=set(),turn=None))
    return records,k

def finite_lift(letters):
    R,k=plan(letters);constraints={};readparity={}
    for t,a in enumerate(R):
        for q in sorted(ports(a['C'],a['p'],a['h'],k)):
            initial=int(q in a['C'])^readparity.get(q,0)
            if q in constraints and constraints[q]['black']!=initial:
                return dict(status='NO_COMPLETE_BOARD_LIFT',letters=letters,conflict_cell=q,first=constraints[q],second=dict(cut=t,black=initial,required_current_black=q in a['C'],read_parity=readparity.get(q,0)))
            constraints.setdefault(q,dict(cut=t,black=initial,required_current_black=q in a['C'],read_parity=readparity.get(q,0)))
        if a['turn'] is not None:readparity[a['p']]=readparity.get(a['p'],0)^1
    B={q for q,a in constraints.items()if a['black']};seed=set(B);p=(0,0);h=0;maxC=0
    for t,a in enumerate(R):
        assert (p,h)==(a['p'],a['h'])
        F=comp(B,k,cursor(p,h));assert F==a['C'],(letters,t,F,a['C'])
        maxC=max(maxC,len(F))
        if a['turn'] is not None:
            assert a['turn']==('L'if p in B else'R')
            p,h=step(B,p,h)
    return dict(status='ACTUAL_FINITE_BOARD_LIFT',letters=letters,initial_black=sorted(seed),word=''.join(MAC[x]['word']for x in letters),final_pose=[p,h],final_black=sorted(B),maximum_complete_active_mass=maxC)

# Exact persistent-star obstruction, in square w coordinates.
DIR=((1,0),(0,1),(-1,0),(0,-1))
def star_obstruction(letters):
    v=(0,0);blocked={};history=[]
    for i,ch in enumerate(letters):
        d=DIR[i%4];left=DIR[(i+1)%4];u=add(v,d)
        for role,p in [('empty_root',v),('first_R_tip',u)]:
            if p in blocked:
                return dict(letters=letters,first_blocked_macro=i,role=role,vertex=p,earlier_star=blocked[p],history=history)
        S={v,add(v,(-d[0],-d[1])),add(v,left),add(v,(-left[0],-left[1]))}
        for p in S:blocked.setdefault(p,i)
        history.append(dict(macro=i,letter=ch,root=v,direction=d,stride=1 if ch=='A'else 2,occupied_star_vertices=sorted(S)))
        v=add(v,(d[0]*(1 if ch=='A'else 2),d[1]*(1 if ch=='A'else 2)))
    return None

def wcoord(v):
    dx=v[0]-1;dy=v[1]+1
    assert (dy-dx)%4==0 and(dx+dy)%4==0
    return (dy-dx)//4,-(dx+dy)//4

controls=[]
for name,seed in [('A',set()),('C',{(-1,1)})]:
    x=finite_lift(name);assert x['status']=='ACTUAL_FINITE_BOARD_LIFT' and set(map(tuple,x['initial_black']))==seed
    B=set(seed);p=(0,0);h=0;k=sector(p,h)
    for c in MAC[name]['word']:
        assert c==('L'if p in B else'R');p,h=step(B,p,h)
    star={(1,0),(1,-1),(0,-1)}
    assert B==star|(set()if name=='A'else{(-1,0)})
    assert comp(B,k,(1,-1))==star
    assert sorted(wcoord(v)for v in vertices(star,k))==[(-1,0),(0,-1),(0,0),(0,1)]
    assert wcoord(cursor(p,h))==((1,0)if name=='A'else(2,0)) and h==3
    if name=='C':
        assert comp(B,k,(-1,1))=={(-1,0)}
        assert sorted(wcoord(v)for v in ends((-1,1),k))==[(1,0),(2,0)]
        assert sorted(wcoord(v)for v in ends((-1,0),k))==[(1,0),(1,1)]
    controls.append(x)

prefix_counts=[];five=[]
for n in range(1,6):
    words=[''.join(x)for x in product('AC',repeat=n)]
    lifts=[finite_lift(x)for x in words]
    prefix_counts.append(dict(length=n,actual_lifts=sum(x['status']=='ACTUAL_FINITE_BOARD_LIFT'for x in lifts),geometrically_unblocked=sum(star_obstruction(x)is None for x in words)))
    if n==5:
        for x,lift in zip(words,lifts):
            z=star_obstruction(x);assert z is not None and lift['status']=='NO_COMPLETE_BOARD_LIFT'
            five.append(dict(star_collision=z,full_component_boundary_conflict=lift))

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
out=dict(status='PASS exact five-clean-return spatial obstruction and full-board controls',source_sha256={str(SRC.relative_to(ROOT)):sha(SRC)},actual_one_block_controls=controls,prefix_counts=prefix_counts,all_32_five_return_obstructions=five,scope='A/C are exact zero-singleton-drop cap5 return paths. No unrestricted board or trajectory scan; full-component port/read-parity constraints are necessary and sufficient for each supplied finite path. General cap5 conclusion additionally needs independent exact-kernel/SCC/singleton proof.')
(OUT/'five_clean_returns_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':out['status'],'prefix_counts':prefix_counts,'one_block_controls':controls},indent=2))
