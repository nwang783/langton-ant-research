"""Target a possible uniform footprint overshoot beyond the first-L box.

This is a finite falsification tool, not a proof of a uniform bound.
"""
from pathlib import Path
import json
import sys
from collections import Counter

ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/'ant_continuation/factor_language/five_macro_footprints.json').read_text())

def rot(x,y,h):return ((x,y),(y,-x),(-x,-y),(-y,x))[h]

def main(depth):
    last={};path=[];records=[];maxgap=-1;nodes=0
    # Bounds order: minimum x, minimum y, maximum x, maximum y.
    def extend(box,p):return (min(box[0],p[0]),min(box[1],p[1]),max(box[2],p[0]),max(box[3],p[1]))
    def dfs(x,y,h,blackbox,readbox):
        nonlocal nodes,maxgap
        nodes+=1
        if path:
            gaps=[blackbox[0]-readbox[0],blackbox[1]-readbox[1],readbox[2]-blackbox[2],readbox[3]-blackbox[3]]
            gap=max(gaps)
            if gap>maxgap:
                maxgap=gap;rec={'gap':gap,'word':''.join(path),'firstL_box':blackbox,'read_box':readbox,'direction_gaps':gaps};records.append(rec);print(rec,flush=True)
        if len(path)==depth:return
        for k in 'UV C QB'.replace(' ',''):
            changes=[];ok=True;bb=blackbox;rb=readbox
            for z in D[k]['trace']:
                dx,dy=rot(*z['p'],h);p=x+dx,y+dy;c=z['c'];old=last.get(p)
                if old==c:ok=False;break
                changes.append((p,old));last[p]=c
                rb=extend(rb,p)
                if old is None and c=='L':bb=extend(bb,p)
            if ok:
                dx,dy=rot(*D[k]['end_pose'][:2],h);path.append(k)
                dfs(x+dx,y+dy,(h+D[k]['end_pose'][2])%4,bb,rb);path.pop()
            for p,old in reversed(changes):
                if old is None:del last[p]
                else:last[p]=old
    dfs(0,0,0,(10**9,10**9,-10**9,-10**9),(10**9,10**9,-10**9,-10**9))
    out={'depth':depth,'nodes':nodes,'maximum_box_excess':maxgap,'records':records}
    Path(__file__).with_name('fuel_hull_probe.json').write_text(json.dumps(out,indent=2)+'\n');print('complete',{'nodes':nodes,'maximum_box_excess':maxgap})

if __name__=='__main__':main(int(sys.argv[1]) if len(sys.argv)>1 else 10)
