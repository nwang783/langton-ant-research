"""Symbolic affine-field proof of the circuit's first divergence, for L>=128.

No extra family members are simulated. The exact fixed recovery word is
replayed once. Complete fields are then represented by affine finite points
and XOR sums of truncated diagonal rays. All inequalities are verified for
every integer L>=128, and periodic read constraints are checked by exact
cancellation of affine interval boundaries.
"""
import json
from pathlib import Path
from fractions import Fraction as Q
from single_blocks import REFERENCE,block
from ant_exact import step,plan,W

LOW=128
STATS={'finite_read_constraints':0,'periodic_read_constraints':0,
       'affine_guards':0,'excluded_isolated_equalities':0}
READ_POINTS=[]
READ_RAYS=[]

# An affine scalar is (coefficient of L, constant).
def add(a,b):return a[0]+b[0],a[1]+b[1]
def neg(a):return -a[0],-a[1]
def sub(a,b):return add(a,neg(b))
def val(a):return a[0]*LOW+a[1]
def scale(a,k):return a[0]*k,a[1]*k
ZERO=(0,0);ONE=(0,1)

def nonneg(a):return a[0]>=0 and val(a)>=0
def negative(a):return a[0]<=0 and val(a)<0

def maximum(a,b):
    STATS['affine_guards']+=1
    if nonneg(sub(a,b)):return a
    if nonneg(sub(b,a)):return b
    raise AssertionError(('affine order changes above threshold',a,b))

def minimum(a,b):return neg(maximum(neg(a),neg(b)))

def in_range(k,N):
    low=k;high=sub(sub(N,ONE),k)
    STATS['affine_guards']+=2
    if negative(low) or negative(high):return False
    assert nonneg(low) and nonneg(high),('range membership changes',k,N)
    return True

def clip(lo,hi,N):
    # First discard intervals known disjoint without imposing irrelevant
    # ordering comparisons between their remote endpoints.
    if negative(hi) or negative(sub(sub(N,ONE),lo)):return None
    lo=maximum(lo,ZERO);hi=minimum(hi,sub(N,ONE))
    STATS['affine_guards']+=1
    if negative(sub(hi,lo)):return None
    assert nonneg(sub(hi,lo)),('interval opens above threshold',lo,hi)
    return lo,hi

# A point is a pair of affine scalars.
def point(x,y):return (0,x),(0,y)
def padd(p,q):return add(p[0],q[0]),add(p[1],q[1])
def psub(p,q):return sub(p[0],q[0]),sub(p[1],q[1])
def rotate(q,j):
    x,y=q
    for _ in range(j%4):x,y=y,-x
    return x,y
def translate_local(q,base,j):
    x,y=rotate(q,j)
    return add(base[0],(0,x)),add(base[1],(0,y))

def cross(delta,d):return sub(scale(delta[0],d[1]),scale(delta[1],d[0]))

def isolated_root(a):
    if a==(0,0):return 'all'
    if a[0]==0:return None
    r=Q(-a[1],a[0])
    return int(r) if r.denominator==1 and r>=LOW else None

def no_point_collision(p,q):
    delta=psub(p,q)
    if delta==(ZERO,ZERO):return False
    root=isolated_root(delta[0] if delta[0]!=ZERO else delta[1])
    if isinstance(root,int):
        assert any(a*root+b!=0 for a,b in delta),('isolated point collision',p,q,root)
    STATS['excluded_isolated_equalities']+=1
    return True

def integer_affine(a,k):
    v=Q(a[0],k),Q(a[1],k)
    assert v[0].denominator==1,('parameter residue needed',a,k)
    if v[1].denominator!=1:return None
    return int(v[0]),int(v[1])

def line_coordinate(delta,d):
    cr=cross(delta,d);root=isolated_root(cr)
    if root!='all':
        assert root is None,('isolated line incidence above threshold',delta,d,root)
        return None
    return integer_affine(delta[0],d[0])

def ray_membership(p,base,d,N):
    k=line_coordinate(psub(p,base),d)
    return k is not None and in_range(k,N)

class Field:
    def __init__(self,points):
        self.points=set(points)
        self.rays=[]
    def point_color(self,p):
        color=p in self.points
        for q in self.points:
            if q!=p:no_point_collision(p,q)
        for base,d,N,label in self.rays:
            color^=ray_membership(p,base,d,N)
        return color
    def add_points(self,points):
        for p in points:self.points.symmetric_difference_update({p})
    def add_rays(self,bases,d,N,label):
        self.rays.extend((b,d,N,label) for b in bases)

def word_data(word,h):
    qs,hs,end,eh=plan(word,(0,0),h)
    required={};odd=set()
    for q,c in zip(qs,word):
        bit=(c=='L')^(q in odd)
        assert q not in required or required[q]==bit
        required[q]=bit;odd.symmetric_difference_update({q})
    return required,odd,end,eh

def apply_finite(field,data,base,j,label):
    required,odd,end,eh=data
    for q,bit in required.items():
        p=translate_local(q,base,j)
        got=field.point_color(p)
        assert got==bit,('finite word mismatch',label,q,got,bit)
        STATS['finite_read_constraints']+=1
        READ_POINTS.append(p)
    field.add_points(translate_local(q,base,j) for q in odd)
    return translate_local(end,base,j)

def toggle_boundary(boundaries,interval):
    if interval is None:return
    lo,hi=interval
    for e in (lo,add(hi,ONE)):
        boundaries.symmetric_difference_update({e})

def previous_ray_interval(q,d,base,e,M,N):
    delta=psub(base,q)
    det=d[0]*e[1]-d[1]*e[0]
    if det==0:
        m=line_coordinate(delta,d)
        if m is None:return None
        if e==d:lo,hi=m,add(m,sub(M,ONE))
        else:
            assert e==(-d[0],-d[1])
            lo,hi=sub(m,sub(M,ONE)),m
        return clip(lo,hi,N)
    k=integer_affine(cross(delta,e),det)
    ell=integer_affine(cross(delta,d),det)
    if k is None or ell is None:return None
    if not in_range(ell,M):return None
    return clip(k,k,N)

def apply_periods(field,data,base,j,N,label):
    required,odd,end,eh=data
    d=rotate(end,j)
    local_flips=[translate_local(q,base,j) for q in odd]
    for q0,bit in required.items():
        q=translate_local(q0,base,j)
        boundaries=set()
        if bit:toggle_boundary(boundaries,(ZERO,sub(N,ONE)))
        for b in field.points:
            k=line_coordinate(psub(b,q),d)
            if k is not None:toggle_boundary(boundaries,clip(k,k,N))
        for b,e,M,_ in field.rays:
            toggle_boundary(boundaries,previous_ray_interval(q,d,b,e,M,N))
        # Net flips from earlier copies of THIS period are present exactly
        # from epoch m onward when b-q=m*d with a positive integer m.
        for b in local_flips:
            m=line_coordinate(psub(b,q),d)
            if m is not None:
                assert m[0]==0
                if m[1]>0:toggle_boundary(boundaries,clip(m,sub(N,ONE),N))
        assert not boundaries,('uncancelled affine color boundaries',label,q0,sorted(boundaries))
        STATS['periodic_read_constraints']+=1
        READ_RAYS.append((q,d,N))
    field.add_rays(local_flips,d,N,label)
    return padd(base,(scale(N,d[0]),scale(N,d[1])))

def main():
    source,p,h,_=REFERENCE
    source=source|block((-127,-108))
    prefix_reads=[]
    # Include the blank prefix too when guarding the three remote input blocks.
    blank=set();bp=(0,0);bh=0
    for _ in range(9977):
        prefix_reads.append(bp);bp,bh,c=step(blank,bp,bh)
    assert not (set(prefix_reads)&block((-127,-108)))
    for _ in range(5781):
        assert p not in block((-127,-108))
        prefix_reads.append(p);p,h,c=step(source,p,h)
    assert p==(-127,-107) and h==2
    recovery_source=set(source);rp=p;rh=h;F=''
    for _ in range(7183):rp,rh,c=step(recovery_source,rp,rh);F+=c
    P=W[61:]+W[:61]
    fdata=word_data(F,2);pdata=word_data(P,3)
    assert fdata[2:]==((-24,25),3)
    assert pdata[2:]==((-2,2),3)
    starts=[point(-127,-107),((-2,-151),(2,-82)),point(-126,0),((2,-102),(2,-83))]
    starts[2]=((0,-126),(4,-58))
    G={(0,-1),(0,0),(1,-1),(1,0)}
    remote=[translate_local(g,starts[j],j) for j in range(1,4) for g in G]
    initial_points=[translate_local(g,starts[j],j) for j in range(4) for g in G]
    assert len(initial_points)==16
    for i,a in enumerate(initial_points):
        for b in initial_points[i+1:]:assert no_point_collision(a,b)
    for q in prefix_reads:
        for b in remote:assert no_point_collision(point(*q),b)
    assert len({point(*q) for q in source}|set(remote))==len(source)+12
    field=Field({point(*q) for q in source}|set(remote))
    for j in range(4):
        end=apply_finite(field,fdata,starts[j],j,'F'+str(j))
        N=(1,0) if j<3 else (1,-65)
        end=apply_periods(field,pdata,end,j,N,'P'+str(j))
        if j<3:assert end==starts[j+1]
    prefix_data=word_data(P[:10],3)
    assert (prefix_data[3]+3)%4==2
    end=apply_finite(field,prefix_data,end,3,'last ten reads')
    assert end==point(4,22)
    assert P[10]=='R'
    assert field.point_color(end) is True
    # Source provenance at the obstructing cell; the additional fields do
    # not alter its value at any L>=128.
    assert (4,22) in source
    point_terms=[q for q in field.points if q==end]
    ray_terms=[label for b,d,N,label in field.rays if ray_membership(end,b,d,N)]
    assert len(point_terms)==1 and not ray_terms
    # The blocker has not been read by any part of the new four-corner path.
    for q in READ_POINTS:assert q!=end and no_point_collision(end,q)
    for base,d,N in READ_RAYS:assert not ray_membership(end,base,d,N)
    old_reads=[t for t,q in enumerate(prefix_reads) if q==(4,22)]
    assert old_reads==[9500]
    out={'status':'symbolic affine guard passed for every integer L>=128',
         'parameter_minimum':LOW,'first_difference_time':{'L_coefficient':416,'constant':37740},
         'first_difference_position':[4,22],'heading':'S','expected_turn':'R','actual_turn':'L',
         'previous_reads_at_obstruction':old_reads,
         'fixed_recovery_length':len(F),'fixed_recovery_word':F,
         'period_word':P,'fourth_tail_complete_periods':{'L_coefficient':1,'constant':-65},
         'fourth_tail_partial_reads':10,'first_hit_time':15758,
         'fixed_first_hit_field_size':len(source),'statistics':STATS}
    Path(__file__).with_name('four_scatterer_affine_prefix_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ('fixed_recovery_word','period_word')},indent=2))

if __name__=='__main__':main()
