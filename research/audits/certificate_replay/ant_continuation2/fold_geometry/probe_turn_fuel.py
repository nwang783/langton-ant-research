"""Targeted finite probes for candidate all-parameter turn-fuel lemmas.

This is discovery only. A finite result does not establish a universal bound.
All strings consist of before-marker blocks; physical consistency is exact.
"""
import json
from pathlib import Path
from collections import Counter
import sys

ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/'ant_continuation/factor_language/five_macro_footprints.json').read_text())

def rot(p,h):
    x,y=p
    return ((x,y),(y,-x),(-x,-y),(-y,x))[h]

def main(depth):
    last={};seq=[];stats=Counter();witnesses=[];maxturn=0
    def dfs(x,y,h,mass,turns):
        nonlocal maxturn
        stats['nodes']+=1;maxturn=max(maxturn,turns)
        if len(seq)==depth:return
        for k in 'UV C QB'.replace(' ',''):
            info=D[k];changes=[];newL=[];ok=True
            for z in info['trace']:
                dx,dy=rot(z['p'],h);p=x+dx,y+dy;c=z['c'];old=last.get(p)
                if old==c:ok=False;break
                changes.append((p,old));last[p]=c
                if old is None and c=='L':newL.append(p)
            if ok:
                seq.append(k)
                if k in 'CQB' and not newL and len(witnesses)<20:
                    witnesses.append({'word':''.join(seq),'new_black_on_last_turn':newL,'mass':mass,'turns':turns+1})
                    print('ZERO FUEL TURN',witnesses[-1],flush=True)
                dx,dy=rot(info['end_pose'][:2],h)
                dfs(x+dx,y+dy,(h+info['end_pose'][2])%4,mass+len(newL),turns+(k in 'CQB'))
                seq.pop()
            else:stats['infeasible']+=1
            for p,old in reversed(changes):
                if old is None:del last[p]
                else:last[p]=old
    dfs(0,0,0,0,0)
    out={'depth':depth,'statistics':dict(stats),'maximum_turns':maxturn,'zero_fuel_turn_witnesses':witnesses}
    Path(__file__).with_name('turn_fuel_probe.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':main(int(sys.argv[1]) if len(sys.argv)>1 else 8)
