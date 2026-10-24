"""Falsify the proposed three-CC obstruction with arbitrary U/V rails.

F=CC, and all geometry uses the before-marker cut. This bounded search is
only for discovering a counterexample or a plausible all-parameter lemma.
"""
from pathlib import Path
import json
import sys

ROOT=Path(__file__).resolve().parents[2]
D=json.loads((ROOT/'ant_continuation/factor_language/five_macro_footprints.json').read_text())
DIR=((0,1),(1,0),(0,-1),(-1,0))
WORDS={k:D[k]['word'] for k in 'UV'};WORDS['F']=D['C']['word']*2

def main(bound):
    last={};stats={'calls':0,'failed':0};answer=None
    def apply(k,pose):
        x,y,h=pose;changes=[]
        for c in WORDS[k]:
            p=x,y;old=last.get(p)
            if old==c:
                for q,v in reversed(changes):
                    if v is None:del last[q]
                    else:last[q]=v
                stats['failed']+=1;return None
            changes.append((p,old));last[p]=c
            h=(h+(1 if c=='R' else -1))%4;dx,dy=DIR[h];x+=dx;y+=dy
        return (x,y,h),changes
    def undo(changes):
        for q,v in reversed(changes):
            if v is None:del last[q]
            else:last[q]=v
    def rail(pose,which,s,t):
        nonlocal answer
        if answer:return
        stats['calls']+=1
        test=apply('F',pose)
        if test:
            q,ch=test
            if which==2:
                answer={'rail1':s,'rail2':t,'word':'CC'+s+'CC'+t+'CC'}
            else:rail(q,2,s,'')
            undo(ch)
        if answer or len(s if which==1 else t)==bound:return
        for k in 'VU':
            test=apply(k,pose)
            if test:
                q,ch=test
                rail(q,which,s+k if which==1 else s,t+k if which==2 else t)
                undo(ch)
                if answer:return
    p,ch=apply('F',(0,0,0));rail(p,1,'','');undo(ch)
    out={'maximum_rail_blocks':bound,'statistics':stats,'counterexample':answer,
         'status':'bounded probe only'}
    Path(__file__).with_name('three_cc_probe.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))

if __name__=='__main__':main(int(sys.argv[1]) if len(sys.argv)>1 else 12)
