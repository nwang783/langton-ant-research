"""Exact scattering of favorable 2x2 blocks in the blank ant's future highway."""
import sys,json,time
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from ant_exact import step,certify_period,PHASES,W,DIRS

def blank_reference():
    B=set();p=(0,0);h=0;reads=set()
    for _ in range(9977):
        reads.add(p);p,h,c=step(B,p,h)
    assert certify_period(B,p,h,W)
    return B,p,h,reads

def block(q):
    return {(q[0]+i,q[1]+j) for i in (0,1) for j in (0,1)}

def run(a,u,n,cap=300000,extra=()):
    base,p,h,reads=REFERENCE
    q=(a-2*n,a-u-2*n)
    added=block(q)
    for v in extra:added|=block(v)
    assert not added&reads
    B=base|added
    initial=sorted(added)
    first=None;head_at_first=None;last='';check_after=0
    low=len(B);high=len(B);j10=0
    for j in range(cap):
        if first is None and p in added:
            first=j;head_at_first=(p,h)
            check_after=j+312
        p,h,c=step(B,p,h)
        last=(last+c)[-312:]
        low=min(low,len(B));high=max(high,len(B))
        if first is not None and j+1>=check_after and len(last)==312:
            w=last[-104:]
            if w in PHASES and last[:104]==w and last[104:208]==w:
                cert=certify_period(B,p,h,w)
                if cert:
                    return {'a':a,'u':u,'n':n,'initial':initial,'first_hit_offset':first,
                            'first_hit_pose':head_at_first,'certified_offset':j+1,
                            'recovery_bound':j+1-first,'final_pose':(p,h),
                            'final_mass':len(B),'low_mass':low,'high_mass':high,
                            'certificate':cert,'word_phase':PHASES[w]}
                check_after=j+1+104
    return {'a':a,'u':u,'n':n,'initial':initial,'first_hit_offset':first,'status':'cap',
            'last_pose':(p,h),'mass':len(B),'low_mass':low,'high_mass':high}

REFERENCE=blank_reference()
if __name__=='__main__':
    cases=[]
    for a in (0,1):
        for u in range(-29,-16,2):
            for n in (64,96):
                r=run(a,u,n)
                cases.append(r)
                print(json.dumps({k:v for k,v in r.items() if k not in ('initial',)}),flush=True)
    Path(__file__).with_name('single_blocks_results.json').write_text(json.dumps(cases,indent=2)+'\n')
