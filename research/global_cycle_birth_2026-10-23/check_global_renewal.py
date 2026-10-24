from check_cycle_birth import *

def check_run(B0,p,h,T):
    B=set(B0);m=len(B);which=wwhich(p,h);beta=rank(B,which)
    A=H=E=ordinary=nonbridge=0
    r=0;hadbirth=False;entryC=component(B,which,cursors(p,h)[1]);em=len(B)
    epochM=len(B);epochN=0;sumord=0
    for t in range(1,T+1):
        if p not in B:
            birth=connected(B,which,*endpoints(p,which))
            H+=birth;hadbirth|=birth;r+=1;assert r<=4
            if r==4:A+=1
            p,h=step(B,p,h)
        else:
            q=p
            nb=connected(B-{q},which,*endpoints(q,which))
            nonbridge+=nb
            exceptional=(r==4 or hadbirth or nb)
            p,h=step(B,p,h)
            assert len(B)-em==r-1
            if exceptional:
                E+=1
                assert len(B)<=3*epochM+3
                epochM=len(B);epochN=0
            else:
                ordinary+=1;epochN+=1
                actual=component(B,which,cursors(p,h)[1])
                expected=component(entryC-{q},which,cursors(p,h)[1])
                assert actual==expected and len(actual)<=len(entryC)-1
                assert epochN<=epochM
            entryC=component(B,which,cursors(p,h)[1]);em=len(B);r=0;hadbirth=False
        assert rank(B,which)==beta+H-nonbridge
        assert E<=beta+A+2*H
        assert t<=4*ordinary+5*E+4
        assert t<=6*(m+2)*3**E<=6*(m+2)*3**(beta+A+2*H)
    return {'T':T,'m':m,'beta':beta,'A':A,'H':H,'exceptional':E,'ordinary':ordinary,'nonbridge_L':nonbridge}

if __name__=='__main__':
    rng=random.Random(2215);results=[]
    for _ in range(160):
        B={(x,y) for x in range(-3,4) for y in range(-3,4) if rng.randrange(3)==0}
        results.append(check_run(B,(rng.randrange(-3,4),rng.randrange(-3,4)),rng.randrange(4),120))
    results.append(check_run(set(),(0,0),0,1500))
    out={'status':'all exact event/active-component/epoch/global-rank controls passed; all-time theorem analytic','runs':len(results),'physical_prefixes':sum(d['T'] for d in results),'exceptional_blocks':sum(d['exceptional'] for d in results),'ordinary_blocks':sum(d['ordinary'] for d in results),'blank':results[-1]}
    (OUT/'global_renewal_controls.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
