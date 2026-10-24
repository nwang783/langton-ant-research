"""Independent complete physical replay of the two-white-column reset."""
from pathlib import Path
import json

HERE=Path(__file__).resolve().parent
DIR=((0,1),(1,0),(0,-1),(-1,0))
SEED={(-2,1),(-1,-1),(-1,0),(-1,2),(-1,3),(-1,4),
      (0,-1),(0,2),(0,3),(0,4),(3,0),(3,3),(4,1),(4,3),(5,2),(5,3)}


def main():
    B=set(SEED);p=(0,0);h=0
    assert len(B)==16 and all(x not in (1,2) for x,y in B)
    trace=[];word=[];seen={p};crossed=False
    for t in range(127):
        c=p in B
        trace.append([t,p[0],p[1],h,int(c),len(B)])
        word.append('L' if c else 'R')
        B.symmetric_difference_update({p})
        h=(h+(-1 if c else 1))%4
        dx,dy=DIR[h];p=p[0]+dx,p[1]+dy
        seen.add(p)
        crossed |= p[0]>=3
    assert p==(0,1) and h==3,(p,h)
    assert crossed
    assert all(x not in (1,2) for x,y in B),sorted(B)
    xs,ys=zip(*seen)
    assert min(xs)<1 and max(xs)>2
    result={'status':'PASS','steps':127,'initial_pose':[[0,0],0],
            'initial_black':sorted(SEED),'final_pose':[p,h],
            'final_black':sorted(B),'white_columns':[1,2],
            'visited_bounds':[min(xs),max(xs),min(ys),max(ys)],
            'turn_word':''.join(word),'trace':trace}
    (HERE/'two_white_columns_counterexample.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='trace'},indent=2))


if __name__=='__main__':main()
