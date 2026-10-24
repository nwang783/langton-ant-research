from pathlib import Path
import json,random,sys
sys.path.insert(0,str(Path(__file__).parent.parent/'global_biexterior_2026-10-23'))
from check_biexterior_return import step,cursors,exterior
from check_backward_section import endpoints
OUT=Path(__file__).parent

def graph(B,which):
    g={}
    for q in B:
        u,v=endpoints(q,which)
        g.setdefault(u,[]).append((v,q));g.setdefault(v,[]).append((u,q))
    return g

def connected(B,which,u,v):
    if u==v:return True
    g=graph(B,which);todo=[u];seen={u}
    while todo:
        a=todo.pop()
        for b,q in g.get(a,()):
            if b==v:return True
            if b not in seen:seen.add(b);todo.append(b)
    return False

def component(B,which,u):
    g=graph(B,which);todo=[u];seen={u};edges=set()
    while todo:
        a=todo.pop()
        for b,q in g.get(a,()):
            edges.add(q)
            if b not in seen:seen.add(b);todo.append(b)
    return edges

def rank(B,which):
    g=graph(B,which);seen=set();n=0
    for u in g:
        if u in seen:continue
        n+=1;seen.add(u);todo=[u]
        while todo:
            a=todo.pop()
            for b,q in g.get(a,()):
                if b not in seen:seen.add(b);todo.append(b)
    return len(B)-len(g)+n

def wwhich(p,h):
    w=cursors(p,h)[1]
    ks=[k for k in (0,1) if w in endpoints(p,k)]
    assert len(ks)==1
    return ks[0]

def cyclebirth(B,p):
    assert p not in B
    return any(connected(B,k,*endpoints(p,k)) for k in (0,1))

def trace_until_birth(B0,p0,h0,limit=10000):
    B=set(B0);p=p0;h=h0;m=len(B);which=wwhich(p,h);beta=rank(B,which)
    bound=2*(m+1)*(3**(beta+1)-1)
    blocks=bridge_blocks=nonbridge_blocks=0
    r=0;entryC=component(B,which,cursors(p,h)[1]);entrymass=m
    epoch_entry_mass=m;epoch_bridge_count=0;epochs=[]
    for t in range(1,min(limit,bound)+1):
        assert which==wwhich(p,h)
        if p not in B and cyclebirth(B,p):
            epochs.append((epoch_entry_mass,epoch_bridge_count))
            assert t<=bound
            assert nonbridge_blocks<=beta
            return {'time':t,'m':m,'beta':beta,'bound':bound,'blocks':blocks,'bridge_blocks':bridge_blocks,'nonbridge_blocks':nonbridge_blocks,'epochs':epochs}
        if p not in B:
            r+=1;assert r<=3
            assert not connected(B,which,*endpoints(p,which))
            p,h=step(B,p,h)
        else:
            q=p;pre=set(B);rem=pre-{q}
            nonbridge=connected(rem,which,*endpoints(q,which))
            p,h=step(B,p,h);blocks+=1
            assert len(B)-entrymass==r-1
            if not nonbridge:
                bridge_blocks+=1;epoch_bridge_count+=1
                actual=component(B,which,cursors(p,h)[1])
                expected=component(entryC-{q},which,cursors(p,h)[1])
                assert q in entryC
                assert actual==expected and len(actual)<=len(entryC)-1
                assert epoch_bridge_count<=epoch_entry_mass
            else:
                nonbridge_blocks+=1
                epochs.append((epoch_entry_mass,epoch_bridge_count))
                assert len(B)<=3*epoch_entry_mass+2
                epoch_entry_mass=len(B);epoch_bridge_count=0
            assert rank(B,which)==beta-nonbridge_blocks
            entrymass=len(B);entryC=component(B,which,cursors(p,h)[1]);r=0
    raise AssertionError(('no birth within theoretical/check limit',m,beta,bound,limit))

def main():
    rng=random.Random(202610232212)
    counts={'cases':0,'bridge_blocks':0,'nonbridge_blocks':0,'max_wait':0,'rod_all_fine_states':0}
    for _ in range(400):
        B={(x,y) for x in range(-3,4) for y in range(-3,4) if rng.randrange(3)==0}
        # Passive separated field must stay in the complete global mass/rank.
        B|={(100+x,100+y) for x,y in ((0,0),(1,0),(0,1),(1,1))} if _%7==0 else set()
        p=(rng.randrange(-3,4),rng.randrange(-3,4));h=rng.randrange(4)
        c=trace_until_birth(B,p,h)
        counts['cases']+=1;counts['bridge_blocks']+=c['bridge_blocks'];counts['nonbridge_blocks']+=c['nonbridge_blocks'];counts['max_wait']=max(counts['max_wait'],c['time'])
    rods=[]
    for r in (1,2,3,10,30,100):
        B={(x,0) for x in range(2*r)};p=(0,0);h=1
        for t in range(4*r):
            assert all(exterior(B,p,h))
            assert rank(B,0)==rank(B,1)==0
            ch='LRRL'[t%4]
            assert (p in B)==(ch=='L')
            if ch=='R':assert not cyclebirth(B,p)
            p,h=step(B,p,h);counts['rod_all_fine_states']+=1
        assert B=={(x,1) for x in range(2*r)} and (p,h)==((2*r,0),1)
        cc=trace_until_birth({(x,0) for x in range(2*r)},(0,0),1)
        assert cc['time']==4*r+4
        rods.append(cc)
    std=json.loads((OUT.parent/'recovered_bundle/ant_global/root/standard.json').read_text())['word']
    ten={(std*2)[i:i+10] for i in range(104)}
    bad=[('LRRL'*4)[i:i+10] for i in range(4)]
    assert all(w not in ten for w in bad)
    result={'status':'literal active-component, full-field mass and first-birth controls passed; all-size proof separate','counts':counts,'rods':rods,'all_four_transport_ten_windows_bad':bad}
    (OUT/'cycle_birth_controls.json').write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2))

if __name__=='__main__':main()
