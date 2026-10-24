"""Independent vector dynamics and per-cell chronology audit of restored data.

The input P,D,W templates are shared mathematical data. The update code and
infinite-tail test below do not call the parent's simulator or breakpoint test.
"""
from pathlib import Path
import hashlib,json,sys,time
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from ant_exact import P,D,W

def tick(B,p,v):
    x,y=v
    if p in B:
        B.remove(p);v=(-y,x);c='L'
    else:
        B.add(p);v=(y,-x);c='R'
    return (p[0]+v[0],p[1]+v[1]),v,c

def check_tail(B,p,v,w):
    points=[]
    for i,c in enumerate(w):
        points.append((p,i,c));x,y=v
        v=(-y,x) if c=='L'else(y,-x)
        p=(p[0]+v[0],p[1]+v[1])
    dx=p[0]-points[0][0][0];dy=p[1]-points[0][0][1]
    assert abs(dx)==2 and abs(dy)==2
    groups={}
    for q,i,c in points:
        key=(dx*q[1]-dy*q[0],q[0]%2)
        if key not in groups:groups[key]=(q,[])
        b,reads=groups[key]
        a=(q[0]-b[0])//dx
        assert q==(b[0]+a*dx,b[1]+a*dy)
        reads.append((a,i,c))
    required=set();mins={}
    for key,(b,reads)in groups.items():
        reads.sort(key=lambda r:(-r[0],r[1]))
        assert reads[0][2]=='R'
        assert all(a[2]!=c[2]for a,c in zip(reads,reads[1:]))
        amin=min(r[0]for r in reads);amax=max(r[0]for r in reads)
        mins[key]=amin
        for k in range(amin,amax):
            first=next(r for r in reads if r[0]<=k)
            if first[2]=='L':required.add((b[0]+k*dx,b[1]+k*dy))
    assert required<=B
    for q in B:
        key=(dx*q[1]-dy*q[0],q[0]%2)
        if key not in groups:continue
        b,_=groups[key];k=(q[0]-b[0])//dx
        if k>=mins[key]:assert q in required
    return len(groups),len(required)

def main():
    folder=Path(__file__).resolve().parents[1]
    data=json.loads((folder/'one_bit_certificate_restored.json').read_text())
    begun=time.time();steps=0;fibers=0;required=0
    for index,row in enumerate(data['cases']):
        B=set(P)
        for k in range(1,row['n']+1):
            B.update((x-2*k,y+2*k)for x,y in D)
        p=(0,0);v=(0,-1)
        for j in range(row['r']):p,v,c=tick(B,p,v);assert c==W[j]
        B.symmetric_difference_update({p})
        for j in range(row['steps']):p,v,c=tick(B,p,v)
        steps+=row['steps']
        assert list(p)==row['position']
        assert ((0,1),(1,0),(0,-1),(-1,0))[row['heading']]==v
        assert len(B)==row['field_count']
        assert hashlib.sha256(repr(sorted(B)).encode()).hexdigest()==row['field_sha256']
        r=row['phase'];w=W[r:]+W[:r]
        f,s=check_tail(B,p,v,w);fibers+=f;required+=s
    out={'cases':len(data['cases']),'literal_steps':steps,'chronology_classes':fibers,'required_black_checks':required,'all_passed':True,'seconds':round(time.time()-begun,3)}
    print(json.dumps(out))
    Path(__file__).with_name('parent_one_bit_audit.json').write_text(json.dumps(out,indent=2)+'\n')

if __name__=='__main__':main()
