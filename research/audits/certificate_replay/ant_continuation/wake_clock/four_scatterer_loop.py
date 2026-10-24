"""Finite exact tests of a geometrically closed four-block scattering loop.

These are tested finite seeds, not an all-scale theorem.
"""
import sys,json,hashlib
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from ant_exact import step,plan,certify_period,PHASES,W
from single_blocks import REFERENCE,block

def rot(v,j):
    x,y=v
    for _ in range(j%4):x,y=y,-x
    return x,y

def build(L):
    a,u,n=1,-19,64
    initial,p,h,_=REFERENCE;B=initial|block((a-2*n,a-u-2*n))
    hit=104*n-875
    for _ in range(hit):p,h,c=step(B,p,h)
    first=p;firsth=h
    G={(x-first[0],y-first[1]) for x,y in block((a-2*n,a-u-2*n))}
    for _ in range(7117):p,h,c=step(B,p,h)
    word=W[99:]+W[:99]
    assert certify_period(B,p,h,word)
    phase_gap=(61-99)%104
    for _ in range(phase_gap):p,h,c=step(B,p,h)
    assert h==(firsth+1)%4
    v=(p[0]-first[0]-2*L,p[1]-first[1]+2*L)
    starts=[];groups=[];q=first
    for j in range(4):
        starts.append((q,(firsth+j)%4))
        groups.append({(q[0]+rot(g,j)[0],q[1]+rot(g,j)[1]) for g in G})
        r=rot(v,j);q=(q[0]+r[0],q[1]+r[1])
    assert q==first
    seed=set().union(*groups)
    assert len(seed)==16
    return seed,groups,starts,9977+hit,7117+phase_gap+104*L

def run(L,cap=1000000):
    seed,groups,starts,t0,macro=build(L)
    B=set(seed);p=(0,0);h=0;last='';after=312
    visits=[[] for _ in range(4)];stage_matches=[]
    for t in range(cap):
        for j,g in enumerate(groups):
            if p in g and (not visits[j] or t-visits[j][-1]>104):visits[j].append(t)
        for j in range(5):
            if t==t0+j*macro:
                target=starts[j%4]
                stage_matches.append({'stage':j,'time':t,'actual':(p,h),'target':target,'match':(p,h)==target})
        p,h,c=step(B,p,h);last=(last+c)[-312:]
        if t+1<after:continue
        w=last[-104:]
        if w not in PHASES or last[:104]!=w or last[104:208]!=w:continue
        cert=certify_period(B,p,h,w)
        if cert:
            return {'L':L,'initial':sorted(seed),'block_groups':[sorted(g) for g in groups],
                    'planned_first_hit_time':t0,'planned_macro_duration':macro,
                    'planned_stages':starts,'stage_matches':stage_matches,
                    'block_read_clusters':visits,'certified_time':t+1,
                    'final_pose':(p,h),'final_mass':len(B),'phase':PHASES[w],
                    'certificate':cert,
                    'field_sha256':hashlib.sha256(repr(sorted(B)).encode()).hexdigest()}
        after=t+1+104
    return {'L':L,'initial':sorted(seed),'status':'cap','last_pose':(p,h),
            'stage_matches':stage_matches,'block_read_clusters':visits,'mass':len(B)}

if __name__=='__main__':
    rows=[]
    for L in (128,192,256):
        r=run(L);rows.append(r)
        Path(__file__).with_name('four_scatterer_loop_results.json').write_text(json.dumps(rows,indent=2)+'\n')
        print(json.dumps({k:v for k,v in r.items() if k not in ('initial','block_groups','block_read_clusters')}),flush=True)
