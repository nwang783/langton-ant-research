#!/usr/bin/env python3
"""Optional first-DEPARTURE CELL-graph monitor; new code pending audit.
Reverse each first-R departure to give indegree one and required winding+1.
Entries are(column,seam_mod3,nonnegative_rank_debt,capped_edge_distance).
The cumulative counterflow increment must be ADDED to a separate register
initialized at2D. Combine that register with rank debt by MAXIMUM, not sum.
"""
def transition(state,old,new,p,geometry,S=120):
    rows=(old,new)
    active=lambda rr:{c for c,a in enumerate(rr) if a['h']}
    A=active(old);B=active(new)
    covered={c for root,es in state for c,w,z,l in es}
    assert covered==A,(covered,A)
    components=[];at={};rank_bound=counterflow_increment=0
    D=max(abs(geometry.a),abs(geometry.b))
    def put(root,entries):
        obj={'root':root,'es':entries};components.append(obj)
        for v in entries:at[v]=obj
        return obj
    for root,es in state:
        entries={(0,c):(w,z,l) for c,w,z,l in es}
        rt=None if root<0 else(0,root)
        if rt is not None:assert entries[rt]==(0,0,0)
        put(rt,entries)
    for c in B:put((1,c),{(1,c):(0,0,0)})
    for ar,ac,br,bc,d,k in geometry.splice_arcs(p):
        source=rows[ar][ac]['h']
        if not source or (source[0]+1)%4!=d:continue
        target=rows[br][bc]['h']
        j=next(j for j,h in enumerate(target) if h==d)
        # Reverse the ACTUAL first-departure arc and its seam sign.
        u=(br,bc);v=(ar,ac);cu=at[u];cv=at[v]
        if cv['root']!=v:return None,0,0,'first_departure_already_exposed'
        debt=0 if j==0 else 4*j-2
        wu,zu,lu=cu['es'][u];wv,zv,lv=cv['es'][v]
        if cu is cv:
            winding=(wu-k-wv)%3
            if winding!=1:return None,0,0,'departure_cycle_wrong_winding'
            rank_bound=max(rank_bound,min(S,zu+debt))
            counterflow_increment=min(S,counterflow_increment+lu+1+2*D)
            cu['root']=None
            cu['es']={a:(w,0,0) for a,(w,z,l) in cu['es'].items()}
        else:
            shift=(wu-k-wv)%3
            rank_offset=min(S,zu+debt);length_offset=min(S,lu+1)
            for a,(w,z,l) in cv['es'].items():
                cu['es'][a]=((w+shift)%3,
                    0 if cu['root'] is None else min(S,rank_offset+z),
                    0 if cu['root'] is None else min(S,length_offset+l))
                at[a]=cu
            components.remove(cv)
    out=[]
    for comp in components:
        entries=sorted((c,w,z,l) for (r,c),(w,z,l) in comp['es'].items() if r==1)
        if not entries:
            if comp['root'] is not None:return None,0,0,'closed_departure_tree'
            continue
        if comp['root'] is None:
            base=entries[0][1]
            entries=[(c,(w-base)%3,0,0) for c,w,z,l in entries];root=-1
        else:
            rr,root=comp['root']
            if rr!=1:return None,0,0,'forgotten_departure_root'
        out.append((root,tuple(entries)))
    return tuple(sorted(out,key=lambda a:a[1][0][0])),rank_bound,counterflow_increment,None
