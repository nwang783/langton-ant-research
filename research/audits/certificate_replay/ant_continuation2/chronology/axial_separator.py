"""Exact mod-4 alternating-row/column invariant and arbitrary-interval audit."""
from pathlib import Path
from collections import Counter
from math import comb
import random,json,sys
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'ant_continuation'))
from ant_exact import step,DIRS

def sign(n):return 1 if n%2==0 else -1

def sector(p,h):return sign(p[0]+p[1])*(1 if h%2==0 else -1)

def row_head(r,p,h,sigma):
    if p[1]<r:return 0
    if p[1]>r:return 2
    k=sigma*sign(r)
    return (0,k,2,-k)[h]

def col_head(c,p,h,sigma):
    if p[0]<c:return 0
    if p[0]>c:return 2
    k=sigma*sign(c)
    return (k,0,-k,2)[h]

def signed_lines(B):
    rows=Counter();cols=Counter()
    for x,y in B:
        rows[y]+=sign(x);cols[x]+=sign(y)
    return rows,cols

def delta4(n):
    r=n%4
    return min(r,4-r)

def midpoint2(p,h):return tuple(2*p[i]-DIRS[h][i] for i in range(2))

def heading_distance(h,g):return min((h-g)%4,(g-h)%4)

def rectangle_size(m,K):
    """Universal number of possible head cells while all masses are at most K."""
    assert K>=m>=0
    return (m+K+1)*(m+K+2)

def confined_state_bound(m,K):
    A=rectangle_size(m,K)
    # The invariant heading/checkerboard sector permits only 2 headings per cell.
    return 2*A*sum(comb(A,j) for j in range(min(K,A)+1))

def confined_field_bound(m,K):
    A=rectangle_size(m,K)
    return sum(comb(A,j) for j in range(min(K,A)+1))

def check_interval(X,Y):
    B,p,h=X;C,q,g=Y
    sigma=sector(p,h);assert sector(q,g)==sigma
    br,bc=signed_lines(B);cr,cc=signed_lines(C)
    rr=set(br)|set(cr)|set(range(min(p[1],q[1]),max(p[1],q[1])+1))
    xx=set(bc)|set(cc)|set(range(min(p[0],q[0]),max(p[0],q[0])+1))
    delta=B^C
    changed_rows=Counter(y for x,y in delta);changed_cols=Counter(x for x,y in delta)
    row_cost=0;col_cost=0
    for r in rr:
        assert (br[r]-row_head(r,p,h,sigma)-cr[r]+row_head(r,q,g,sigma))%4==0
        cost=delta4(row_head(r,q,g,sigma)-row_head(r,p,h,sigma))
        row_cost+=cost
        assert changed_rows[r]>=cost
        if r not in (p[1],q[1]):
            crossing=(p[1]<r<q[1]) or (q[1]<r<p[1])
            assert (cr[r]-br[r]-2*crossing)%4==0
    for c in xx:
        assert (bc[c]-col_head(c,p,h,sigma)-cc[c]+col_head(c,q,g,sigma))%4==0
        cost=delta4(col_head(c,q,g,sigma)-col_head(c,p,h,sigma))
        col_cost+=cost
        assert changed_cols[c]>=cost
        if c not in (p[0],q[0]):
            crossing=(p[0]<c<q[0]) or (q[0]<c<p[0])
            assert (cc[c]-bc[c]-2*crossing)%4==0
    mp=midpoint2(p,h);mq=midpoint2(q,g)
    exact_row_cost=abs(mq[1]-mp[1]) if p[1]!=q[1] else heading_distance(h,g)
    exact_col_cost=abs(mq[0]-mp[0]) if p[0]!=q[0] else heading_distance(h,g)
    assert row_cost==exact_row_cost
    assert col_cost==exact_col_cost
    assert len(delta)>=max(row_cost,col_cost)
    assert len(delta)>=max(abs(mq[i]-mp[i]) for i in range(2))
    return len(rr)+len(xx)

def local_cases():
    count=0
    for x in (0,1):
        for y in (0,1):
            for h in range(4):
                for color in (0,1):
                    p=(x,y);B={p} if color else set();before=(set(B),p,h)
                    q,g,letter=step(B,p,h)
                    check_interval(before,(B,q,g));count+=1
    return count

def main():
    rng=random.Random(20261022);cases=local_cases();intervals=0;line_checks=0
    for seed in range(100):
        B={(rng.randrange(-5,6),rng.randrange(-5,6)) for _ in range(rng.randrange(36))}
        # These unchanged remote cells are retained throughout.
        if seed%3==0:B|={(10**6+seed,-10**6),(-10**6,10**6+seed)}
        p=(rng.randrange(-3,4),rng.randrange(-3,4));h=rng.randrange(4)
        states=[(set(B),p,h)]
        for _ in range(300):
            p,h,_=step(B,p,h);states.append((set(B),p,h))
        for _ in range(50):
            s=rng.randrange(301);t=rng.randrange(s,301)
            line_checks+=check_interval(states[s],states[t]);intervals+=1
    B=set();p=(0,0);h=0;diagonal=[];blank_states=[]
    blank_times=set(range(251))|set(range(0,30001,137))|{30000}
    for t in range(30001):
        if t in blank_times:blank_states.append((set(B),p,h))
        if t in (18,247):
            sign,c=(1,-1) if t==18 else (-1,8)
            assert not any(x+sign*y==c for x,y in B)
            z=p[0]+sign*p[1]
            assert min(0,z)<c<max(0,z)
            diagonal.append({'time':t,'black':sorted(B),'head':p,'heading':h,
                             'diagonal_sign':sign,'empty_separator_coordinate':c})
        if t<30000:p,h,_=step(B,p,h)
    for _ in range(1000):
        s=rng.randrange(len(blank_states));t=rng.randrange(s,len(blank_states))
        line_checks+=check_interval(blank_states[s],blank_states[t])
    result={'status':'PASS','local_parity_heading_color_cases':cases,
            'arbitrary_complete_field_intervals':intervals,
            'blank_intervals':1000,'blank_time_horizon':30000,
            'signed_line_checks':line_checks,
            'checks':'Exact mod4 charges, exact heading-corrected line costs, sharp incoming-midpoint bound',
            'initial_blank_running_mass_state_bounds':{str(K):confined_state_bound(0,K) for K in range(5)},
            'initial_blank_running_mass_field_bounds':{str(K):confined_field_bound(0,K) for K in range(5)},
            'diagonal_counterexamples':diagonal}
    Path(__file__).with_name('axial_separator_audit.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='diagonal_counterexamples'},indent=2))

if __name__=='__main__':main()
