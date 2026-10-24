from check_cycle_birth import *

def check_erasure_run(B0,p,h,T):
    B=set(B0);m=len(B);which=wwhich(p,h)
    A=DH=DG=E=ordinary=0;Rbirth_bridge_blocks=0
    r=0;prefix_births=0;entryC=component(B,which,cursors(p,h)[1]);em=m
    epochM=m;epochN=0
    for t in range(1,T+1):
        if p not in B:
            prefix_births+=connected(B,which,*endpoints(p,which))
            r+=1;assert r<=4
            if r==4:A+=1
            p,h=step(B,p,h)
        else:
            q=p;rem=B-{q}
            dH=connected(rem,which,*endpoints(q,which));dG=connected(rem,1-which,*endpoints(q,1-which))
            DH+=dH;DG+=dG
            ex=(r==4 or dH)
            p,h=step(B,p,h)
            assert len(B)-em==r-1
            if ex:
                E+=1;assert len(B)<=3*epochM+3
                epochM=len(B);epochN=0
            else:
                ordinary+=1;epochN+=1
                actual=component(B,which,cursors(p,h)[1]);expected=component(entryC-{q},which,cursors(p,h)[1])
                assert actual==expected and len(actual)<=len(entryC)-1
                assert epochN<=epochM
                if prefix_births:Rbirth_bridge_blocks+=1
            entryC=component(B,which,cursors(p,h)[1]);em=len(B);r=0;prefix_births=0
        assert E<=A+DH
        assert A<=DG+1
        assert t<=4*ordinary+5*E+4
        assert t<=6*(m+2)*3**E<=6*(m+2)*3**(A+DH)<=18*(m+2)*3**(DG+DH)
    return {'m':m,'T':T,'A':A,'DH':DH,'DG':DG,'ordinary':ordinary,'exceptional':E,'w_birth_but_bridge_L_blocks':Rbirth_bridge_blocks}

def first_erasure(B0,p,h,limit=10000):
    B=set(B0);m=len(B)
    for t in range(1,min(limit,4*m+5)+1):
        if p in B and any(connected(B-{p},k,*endpoints(p,k)) for k in (0,1)):
            return t
        p,h=step(B,p,h)
    raise AssertionError(('erasure bound failed',m,p,h))

if __name__=='__main__':
    rng=random.Random(2217);counts={'runs':0,'prefixes':0,'w_birth_but_bridge_L_blocks':0,'first_erasure_cases':0,'max_erasure_wait':0}
    for i in range(200):
        B={(x,y) for x in range(-3,4) for y in range(-3,4) if rng.randrange(3)==0}
        p=(rng.randrange(-3,4),rng.randrange(-3,4));h=rng.randrange(4)
        c=check_erasure_run(B,p,h,180)
        counts['runs']+=1;counts['prefixes']+=c['T'];counts['w_birth_but_bridge_L_blocks']+=c['w_birth_but_bridge_L_blocks']
        t=first_erasure(B,p,h);counts['first_erasure_cases']+=1;counts['max_erasure_wait']=max(counts['max_erasure_wait'],t)
    blank=check_erasure_run(set(),(0,0),0,2000);counts['w_birth_but_bridge_L_blocks']+=blank['w_birth_but_bridge_L_blocks'];counts['prefixes']+=blank['T'];counts['runs']+=1
    rod=[]
    for r in (1,2,10,30,100):
        t=first_erasure({(x,0) for x in range(2*r)},(0,0),1)
        assert t==4*r+5
        rod.append({'r':r,'m':2*r,'first_erasure':t,'bound':8*r+5})
    out={'status':'literal exact inheritance remains valid with R-cycle births; global erasure forcing/renewal controls passed','counts':counts,'blank':blank,'rods':rod}
    (OUT/'cycle_erasure_controls.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
