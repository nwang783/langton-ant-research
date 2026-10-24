"""Whole finite-board static mirror pairing geometry, fixed initial-E sector."""
from collections import Counter, defaultdict
DXY = ((0,1),(1,0),(0,-1),(-1,0))

def successor(z, B):
    p,h = z
    hh = (h + (-1 if p in B else 1)) % 4
    return ((p[0]+DXY[hh][0], p[1]+DXY[hh][1]), hh)

def circuit(z, B):
    q = z; out = []; seen = set()
    while q not in seen:
        seen.add(q); out.append(q); q = successor(q,B)
        assert len(out) <= 8*len(B)+4
    assert q == z
    return out

def winding(a):
    """Winding at each unit plaquette center, keyed by its lower-left corner."""
    vertical = defaultdict(Counter)
    for z,zz in zip(a,a[1:]+a[:1]):
        (x,y),_ = z; (xx,yy),_ = zz
        if y != yy:
            assert x == xx and abs(yy-y) == 1
            vertical[min(y,yy)][x] += 1 if yy>y else -1
    out = {}
    for y,row in vertical.items():
        lo,hi = min(row),max(row); s = 0
        for x in range(hi-1,lo-1,-1):
            s += row[x+1]
            if s: out[x,y] = s
        assert s + row[lo] == 0
    area2 = sum(z[0][0]*zz[0][1]-zz[0][0]*z[0][1] for z,zz in zip(a,a[1:]+a[:1]))
    assert area2%2 == 0 and sum(out.values()) == area2//2
    assert area2 != 0 and set(out.values()) == ({1} if area2>0 else {-1})
    return out, area2//2

def whole(B, pose):
    """Exactly all altered baseline circuits, plus the cursor circuit if untouched."""
    U = set()
    for p in B:
        for h in ((1,3) if sum(p)%2==0 else (0,2)):
            U.update(circuit((p,h),set()))
    if pose not in U: U.update(circuit(pose,set()))
    base = Counter(); unseen=set(U)
    while unseen:
        a=circuit(min(unseen),set()); unseen.difference_update(a)
        w,ar=winding(a); assert len(a)==4 and ar==-1
        base.update(w)
    assert all(sum(q)%2==0 and n==-1 for q,n in base.items())
    unseen=set(U); total=Counter(); pos=Counter(); rows=[]; active=None
    while unseen:
        a=circuit(min(unseen),B); assert set(a)<=U
        unseen.difference_update(a); w,ar=winding(a); total.update(w)
        if ar>0:pos.update(w)
        row=dict(representative=a[0],length=len(a),area=ar)
        rows.append(row)
        if pose in a:active=row
    assert total == base
    area=sum(max(r['area'],0) for r in rows)
    assert area == sum(pos.values())
    assert sum(abs(r['area'])for r in rows)-len(U)//4 == 2*area
    return dict(black_mass=len(B),baseline_loops=len(U)//4,affected_states=len(U),
                circuits=rows,active=active,positive_winding_area=area,
                positive_winding=[[q,n]for q,n in sorted(pos.items())],
                positive_loop_count=sum(r['area']>0 for r in rows),
                max_loop_length=max(r['length']for r in rows),
                max_absolute_area=max(abs(r['area'])for r in rows))

def local_surgery(B, pose):
    p,h=pose; other=(p,(h+2)%4)
    old_a=circuit(pose,B); old=[old_a]
    if other not in old_a:old.append(circuit(other,B))
    C=set(B);C.symmetric_difference_update({p})
    new_a=circuit(pose,C);new=[new_a]
    if other not in new_a:new.append(circuit(other,C))
    assert {z for a in old for z in a} == {z for a in new for z in a}
    assert sorted(len(v)for v in [old,new]) == [1,2]
    def data(aa):
        total=Counter();areas=[];domains=[]
        for a in aa:
            w,ar=winding(a);total.update(w);areas.append(ar);domains.append(set(w))
        return total,areas,domains
    ow,oa,od=data(old);nw,na,nd=data(new);assert ow==nw
    pair=oa if len(oa)==2 else na
    domains=od if len(oa)==2 else nd
    same=pair[0]*pair[1]>0
    if same:assert not (domains[0]&domains[1])
    else:assert domains[0]<domains[1] or domains[1]<domains[0]
    delta=sum(max(a,0)for a in na)-sum(max(a,0)for a in oa)
    predicted=0 if same else min(map(abs,pair))*(1 if len(new)==2 else -1)
    assert delta==predicted
    return dict(kind='split'if len(new)==2 else'merge',old_areas=oa,new_areas=na,
                same_orientation=same,positive_area_change=delta,
                pair_domain_sizes=list(map(len,domains)),
                old_lengths=list(map(len,old)),new_lengths=list(map(len,new)))
