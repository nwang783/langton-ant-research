"""Complete exact finite leaves for the corner-block family, 1<=n<34."""
import sys,json,hashlib
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from ant_exact import step,certify_period,PHASES

def seed(a,u,n):
    return {(a+sx*2*n+i,a-u+sy*2*n+j)
            for sx in (-1,1) for sy in (-1,1) for i in (0,1) for j in (0,1)}

def run(a,u,n,cap=1000000):
    B=seed(a,u,n);initial=sorted(B);p=(0,0);h=0
    assert len(B)==16
    last='';after=312;checks=0
    for t in range(cap):
        p,h,c=step(B,p,h)
        last=(last+c)[-312:]
        if t+1<after:continue
        w=last[-104:]
        if w not in PHASES or last[:104]!=w or last[104:208]!=w:continue
        checks+=1
        cert=certify_period(B,p,h,w)
        if cert:
            return {'a':a,'u':u,'n':n,'initial':initial,
                    'certified_time':t+1,'pose':(p,h),'mass':len(B),
                    'phase':PHASES[w],'certificate':cert,'tail_checks':checks,
                    'field_sha256':hashlib.sha256(repr(sorted(B)).encode()).hexdigest()}
        after=t+1+104
    return {'a':a,'u':u,'n':n,'initial':initial,'status':'cap','time':cap,
            'pose':(p,h),'mass':len(B),'tail_checks':checks}

def main():
    results=[]
    for a in (0,1):
        for u in range(-29,-16,2):
            batch=[run(a,u,n) for n in range(1,34)]
            results+=batch
            Path(__file__).with_name('small_corner_blocks_results.json').write_text(json.dumps(results,indent=2)+'\n')
            print(json.dumps({'a':a,'u':u,'cases':len(batch),
                              'unresolved':[r['n'] for r in batch if 'status' in r],
                              'max_certified_time':max(r.get('certified_time',0) for r in batch)}),flush=True)
    assert len(results)==462
    assert not [r for r in results if 'status' in r]
    print(json.dumps({'total_cases':len(results),
                      'total_literal_steps':sum(r['certified_time'] for r in results),
                      'largest_certified_time':max(r['certified_time'] for r in results)}),flush=True)

if __name__=='__main__':main()
