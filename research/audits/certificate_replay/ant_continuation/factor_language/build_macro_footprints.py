"""Rebuild and/or verify every finite geometric macro footprint.

The coverage verifier produces after-marker words. This script conjugates
their cut to BEFORE the marker and computes all footprint fields from scratch.
Without --write it checks the distributed JSON rather than changing it.
"""
from pathlib import Path
import json
import sys

HERE=Path(__file__).resolve().parent
MARKER='LLLLRLRRRRLR'
DIRS=((0,1),(1,0),(0,-1),(-1,0))

def footprint(word):
    x=y=h=0;trace=[];first={};last={};odd=set()
    for i,c in enumerate(word):
        p=x,y
        assert last.get(p)!=c
        trace.append({'i':i,'p':[x,y],'h':h,'c':c})
        first.setdefault(p,c);last[p]=c;odd.symmetric_difference_update({p})
        h=(h+(1 if c=='R' else -1))%4
        dx,dy=DIRS[h];x+=dx;y+=dy
    def points(mapping,c):return [list(p) for p in sorted(p for p,v in mapping.items() if v==c)]
    return {'word':word,'length':len(word),'end_pose':[x,y,h],'trace':trace,
            'first_L':points(first,'L'),'first_R':points(first,'R'),
            'odd_visits':[list(p) for p in sorted(odd)],
            'last_L':points(last,'L'),'last_R':points(last,'R')}

def main():
    coverage=json.loads((HERE/'five_macro_verification.json').read_text())
    data={name:footprint(MARKER+after[:-len(MARKER)]) for name,after in coverage['after_marker_words'].items()}
    target=HERE/'five_macro_footprints.json'
    if '--write' in sys.argv:target.write_text(json.dumps(data,indent=2)+'\n')
    else:assert data==json.loads(target.read_text())
    print({name:{'length':d['length'],'end_pose':d['end_pose'],'first_L':len(d['first_L'])} for name,d in data.items()})

if __name__=='__main__':main()
