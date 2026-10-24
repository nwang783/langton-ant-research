from check_cycle_birth import *

def check_global(B0,p,h,T):
    B=set(B0);m=len(B);Hgraph=wwhich(p,h)
    D=E=ordinary=0;r=0;birthsinprefix=0;birth_bridge=0
    ec=component(B,Hgraph,cursors(p,h)[1]);em=m;epochM=m;epochN=0
    for t in range(1,T+1):
        if p not in B:
            birthsinprefix+=connected(B,Hgraph,*endpoints(p,Hgraph))
            r+=1;assert r<=4;p,h=step(B,p,h)
        else:
            q=p;Hnb=connected(B-{q},Hgraph,*endpoints(q,Hgraph));Gnb=connected(B-{q},1-Hgraph,*endpoints(q,1-Hgraph))
            D+=bool(Hnb or Gnb)
            if r>=3:assert Gnb
            ex=(r>=3 or Hnb)
            p,h=step(B,p,h)
            assert len(B)-em==r-1
            if ex:
                E+=1;assert len(B)<=2*epochM+3;epochM=len(B);epochN=0
            else:
                ordinary+=1;epochN+=1
                ac=component(B,Hgraph,cursors(p,h)[1]);expected=component(ec-{q},Hgraph,cursors(p,h)[1])
                assert ac==expected and len(ac)<=len(ec)-1
                assert epochN<=epochM
                birth_bridge+=bool(birthsinprefix)
            ec=component(B,Hgraph,cursors(p,h)[1]);em=len(B);r=0;birthsinprefix=0
        assert E<=D
        assert t<=3*ordinary+5*E+4
        assert t<=6*(m+3)*2**E<=6*(m+3)*2**D
    return {'T':T,'m':m,'cycle_erasing_updates':D,'exceptional':E,'ordinary':ordinary,'ordinary_with_w_birth':birth_bridge}

def first_erasure_classification(B0,p0,h0):
    B=set(B0);p=p0;h=h0;m=len(B);which=wwhich(p,h)
    originalC=component(B,which,cursors(p,h)[1]);oldB=set(B)
    ws={cursors(p,h)[1]};spent=set();born=set();nL=0;nR=0;word=''
    for t in range(1,3*m+6):
        if p in B:
            if any(connected(B-{p},k,*endpoints(p,k)) for k in (0,1)):
                assert t<=3*m+5
                assert t-1<=3*m+4 and len(B)<=2*m+4
                return t
            assert p in oldB and p in originalC and p not in spent and p not in born
            assert not connected(oldB-{p},which,*endpoints(p,which))
            spent.add(p);nL+=1
            p,h=step(B,p,h)
            w=cursors(p,h)[1];assert w not in ws;ws.add(w)
        else:
            nR+=1;born.add(p);p,h=step(B,p,h)
        assert nL<=m and nR<=2*nL+4
        assert born<=B
        assert len(B)<=2*m+4
    raise AssertionError('linear erasure bound')

if __name__=='__main__':
    rng=random.Random(2221);runs=[];maxwait=0
    for i in range(200):
        B={(x,y) for x in range(-3,4) for y in range(-3,4) if rng.randrange(3)==0}
        p=(rng.randrange(-3,4),rng.randrange(-3,4));h=rng.randrange(4)
        runs.append(check_global(B,p,h,160))
        maxwait=max(maxwait,first_erasure_classification(B,p,h))
    runs.append(check_global(set(),(0,0),0,2000))
    maxwait=max(maxwait,first_erasure_classification(set(),(0,0),0))
    rod=[]
    for r in (1,2,10,30,100):
        t=first_erasure_classification({(x,0) for x in range(2*r)},(0,0),1)
        assert t==4*r+5
        rod.append({'r':r,'m':2*r,'first_erasure':t,'linear_bound':6*r+5})
    out={'status':'exact original-bridge/simple-cursor/current-born-token/global-renewal controls passed; all-size theorem analytic','runs':len(runs),'prefixes':sum(d['T'] for d in runs),'ordinary_blocks':sum(d['ordinary'] for d in runs),'ordinary_blocks_with_w_cycle_birth':sum(d['ordinary_with_w_birth'] for d in runs),'max_random_first_erasure_wait':maxwait,'blank':runs[-1],'rod':rod}
    (OUT/'old_bridge_zipper_controls.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
