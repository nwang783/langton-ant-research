"""Exact frozen-circuit probes for the classical ant. Exploratory only."""
from pathlib import Path
from collections import Counter
import json,sys,random,time
DIR=((0,1),(1,0),(0,-1),(-1,0))
HERE=Path(__file__).resolve().parent

def frozen(B,p,h):
    start=(p,h);cycle=[];turn=0
    while True:
        c=-1 if p in B else 1
        cycle.append((p,h));turn+=c
        h=(h+c)%4;d=DIR[h];p=(p[0]+d[0],p[1]+d[1])
        if (p,h)==start:break
        assert len(cycle)<=8*len(B)+16
    assert turn in (-4,4),(len(cycle),turn)
    return cycle,turn//4

def run(B,p=(0,0),h=0,steps=20000):
    B=set(B);records=[];stats=Counter();examples={};lastsign=1
    for t in range(steps):
        cyc,s=frozen(B,p,h);color=int(p in B)
        other=(p,(h+2)%4)
        if other in cyc:
            kind='split';other_index=cyc.index(other);other_len=len(cyc)-other_index
            os=0
        else:
            kind='merge';other_index=0;c2,os=frozen(B,*other);other_len=len(c2)
        before=p,h
        h=(h+(-1 if color else 1))%4
        B.symmetric_difference_update({p});d=DIR[h];p=(p[0]+d[0],p[1]+d[1])
        after,ss=frozen(B,p,h)
        assert len(after)==(other_index if kind=='split' else len(cyc)+other_len)
        key=(color,kind,s,os,ss)
        stats[str(key)]+=1
        examples.setdefault(str(key),{'time':t,'pose':before,'mass':len(B),'active_before':len(cyc),'active_after':len(after),'other_length':other_len})
        records.append([t,color,0 if kind=='merge' else 1,s,ss,len(cyc),len(after),other_len,len(B),p[0],p[1]])
    return {'steps':steps,'stats':dict(stats),'examples':examples,'records':records}

def main():
    steps=int(sys.argv[1]) if len(sys.argv)>1 else 15000
    out=run(set(),steps=steps)
    (HERE/'blank_circuits.json').write_text(json.dumps(out,separators=(',',':'))+'\n')
    for k,v in out['stats'].items():print(k,v,out['examples'][k])
    for a,b in [(0,9977),(9977,steps)]:
        rows=out['records'][a:b]
        print('range',a,b,'signs',dict(Counter(r[3] for r in rows)),'length_minmax',min(r[5] for r in rows),max(r[5] for r in rows))
if __name__=='__main__':main()
