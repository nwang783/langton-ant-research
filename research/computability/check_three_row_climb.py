#!/usr/bin/env python3
"""Complete small certificate for pristine height-three cost >= 7 south moves.
Unlike the direct probe, enumerate the individual first-row crossing catalog,
then check every feasible allocation of <=6 south moves among three crossings.
"""
import itertools,json
from pathlib import Path
D=((0,1),(1,0),(0,-1),(-1,0))
def catalog(S):
    board={}; result=[]; nodes=0
    def visit(x,y,h,s,w):
        nonlocal nodes
        nodes+=1
        if y==1:
            if s==S:result.append(w)
            return
        q=x,y; old=board.get(q)
        options=(old,) if old is not None else ((0,) if y>=0 else (0,1))
        for bit in options:
            hh=(h+(1 if bit==0 else -1))%4
            ss=s+(hh==2)
            if ss>S:continue
            board[q]=1-bit
            visit(x+D[hh][0],y+D[hh][1],hh,ss,w+'RL'[bit])
        if old is None:board.pop(q,None)
        else:board[q]=old
    visit(0,0,0,0,'')
    return dict(south=S,nodes=nodes,words=result)
def conflict(w):
    x=y=h=0;last={}
    for t,c in enumerate(w):
        q=x,y
        if q in last and last[q][1]==c:
            return dict(time=t,cell=q,kind='repeated turn',previous=last[q][0])
        if q not in last and y>=0 and c=='L':
            return dict(time=t,cell=q,kind='first upper L')
        last[q]=t,c
        h=(h+(1 if c=='R' else -1))%4;x+=D[h][0];y+=D[h][1]
    return None

def run():
    cats={s:catalog(s) for s in range(1,5)}
    assert [len(cats[s]['words']) for s in cats]==[1,1,4,16]
    rows=[]
    for ss in itertools.product(range(1,5),repeat=3):
        if sum(ss)>6:continue
        for words in itertools.product(*(cats[s]['words'] for s in ss)):
            fail=conflict(''.join(words));assert fail is not None
            rows.append(dict(south=ss,words=words,conflict=fail))
    assert len(rows)==92
    witness='RRLRRRRLRRRRLLLLRLRRRRLRRRRLLLLRLR'
    assert conflict(witness) is None
    x=y=h=s=0;heights=[]
    for c in witness:
        h=(h+(1 if c=='R' else -1))%4;x+=D[h][0];y+=D[h][1];s+=h==2;heights.append(y)
    assert y==3 and h==0 and s==7 and max(heights[:-1])<3
    return dict(status='EXACT FINITE CERTIFICATE',catalogs=cats,triples=rows,witness=dict(word=witness,end=(x,y,h),south=s),max_conflict=max(r['conflict']['time'] for r in rows))
if __name__=='__main__':
    result=run();Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(catalog_counts=[len(c['words']) for c in result['catalogs'].values()],triples=len(result['triples']),max_conflict=result['max_conflict'],witness=result['witness'])))
