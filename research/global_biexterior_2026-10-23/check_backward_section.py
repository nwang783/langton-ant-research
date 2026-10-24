from check_biexterior_return import *

def prev(B,p,h):
    dx,dy=DIR[h];q=p[0]-dx,p[1]-dy
    if q in B:
        B.remove(q);hh=(h-1)%4
    else:
        B.add(q);hh=(h+1)%4
    return q,hh

def backward_return(B0,p0,h0):
    B=set(B0);p=p0;h=h0;m=len(B)
    if all(exterior(B,p,h)):return 0,len(B)
    rs=closure(B);r=next(r for r in rs if inside(p,r));k=r[4]
    area=(r[1]-r[0]+1)*(r[3]-r[2]+1)
    rad=(r[1]-r[0]+r[3]-r[2]+1)//2
    bound=(area+2)*(3**rad-1)+1
    outside={q for q in B if not inside(q,r)}
    for t in range(1,bound+1):
        assert inside(p,r)
        oldB=set(B);oldp=p;oldh=h
        p,h=prev(B,p,h)
        # Actual physical forward undo checks all field and head state.
        b=set(B);pp,hh=step(b,p,h)
        assert b==oldB and pp==oldp and hh==oldh
        assert len(B)<=m-k+area+1<=m*m+1
        assert abs(p[0]-p0[0])+abs(p[1]-p0[1])<=2*k-1
        out={q for q in B if not inside(q,r)}
        assert out==outside or (out==outside|{p} and not inside(p,r))
        if all(exterior(B,p,h)):return t,len(B)
        assert inside(p,r) and out==outside
    raise AssertionError(('backward bound',B0,p0,h0,bound))

def endpoints(q,which):
    x,y=q
    s=1 if (x+y)%2==which else -1
    return (2*x-1,2*y-s),(2*x+1,2*y+s)

def no_new_cycle(B,q,which):
    graph={}
    for p in B:
        u,v=endpoints(p,which);graph.setdefault(u,set()).add(v);graph.setdefault(v,set()).add(u)
    u,v=endpoints(q,which);seen={u};todo=[u]
    while todo:
        a=todo.pop()
        for b in graph.get(a,()):
            if b not in seen:seen.add(b);todo.append(b)
    return v not in seen

if __name__=='__main__':
    cells=[(x,y) for x in range(-1,2) for y in range(-1,2)]
    counts={'backward_starts':0,'nonexterior_starts':0,'hull_writer_tests':0,'new_cycle_tests':0,'max_backward_delay':0}
    for mask in range(512):
        B={q for i,q in enumerate(cells) if mask>>i&1};rs=closure(B)
        for p in cells:
            for h in range(4):
                counts['backward_starts']+=1
                if not all(exterior(B,p,h)):
                    counts['nonexterior_starts']+=1
                    t,mm=backward_return(B,p,h)
                    counts['max_backward_delay']=max(counts['max_backward_delay'],t)
        for p in [(x,y) for x in range(-2,3) for y in range(-2,3)]:
            if any(inside(p,r) for r in rs):continue
            assert p not in B
            for which in (0,1):
                assert no_new_cycle(B,p,which)
                counts['new_cycle_tests']+=1
            for h in range(4):
                assert all(exterior(B,p,h))
                b=set(B);pp,hh=step(b,p,h)
                assert all(exterior(b,pp,hh))
                counts['hull_writer_tests']+=1
    (OUT/'backward_section_controls.json').write_text(json.dumps({'status':'literal controls passed, all-size proof separate','counts':counts},indent=2))
    print(json.dumps(counts,indent=2))
