#!/usr/bin/env python3
"""Discovery only: first climb through a pristine upper half-plane.
Start (0,0,N), all y>=0 white, lower colors arbitrary. Stop at first y=H.
Limit total south moves; exact first-hit length is 2H+4S.
"""
import json,sys,time
D=((0,1),(1,0),(0,-1),(-1,0))
def trial(H,S,cap=2000000):
    cells={}; nodes=0; answer=None
    def dfs(x,y,h,s,w):
        nonlocal nodes,answer
        nodes+=1
        if nodes>cap:raise OverflowError
        if y==H:
            answer=w;return True
        # all remaining north displacement must fit remaining vertical budget
        if s>S:return False
        q=x,y
        old=cells.get(q)
        options=(old,) if old is not None else ((0,) if y>=0 else (0,1))
        for c in options:
            hh=(h+(1 if c==0 else -1))%4
            ss=s+(hh==2)
            if ss>S:continue
            cells[q]=1-c
            xx,yy=x+D[hh][0],y+D[hh][1]
            if dfs(xx,yy,hh,ss,w+('R' if c==0 else 'L')):return True
        if old is None:cells.pop(q,None)
        else:cells[q]=old
        return False
    try: ok=dfs(0,0,0,0,'');status='SAT' if ok else 'UNSAT'
    except OverflowError:status='UNKNOWN'
    return dict(H=H,S=S,status=status,nodes=nodes,word=answer)
if __name__=='__main__':
    out=[]
    for H in range(1,int(sys.argv[1])+1):
        for S in range(H+H//2,3*H+1):
            r=trial(H,S);out.append(r);print(json.dumps(r),flush=True)
            if r['status']!='UNSAT':break
    open(sys.argv[2],'w').write(json.dumps(out,indent=2)+'\n')
