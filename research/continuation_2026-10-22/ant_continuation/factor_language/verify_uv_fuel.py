"""Finite geometric checks used in the all-length U/V fuel proof.

This checks the building blocks and all four interfaces, not merely long
sample words.  The proof of arbitrarily many blocks is in five_macro_status.md.
"""
from itertools import product
from pathlib import Path
import json

HERE=Path(__file__).resolve().parent
A={(0,0),(-1,-1),(0,-1),(1,0)}
F={'U':{(-1,0),(-1,1),(-1,2),(0,2),(0,3)},'V':{(-1,0),(1,2)}}
DELTA={'U':(0,4),'V':(1,3)}

def shift(points,d):return {(x+d[0],y+d[1]) for x,y in points}

def trace(word):
    x=y=h=0;last={};first={}
    for c in word:
        p=x,y
        assert last.get(p)!=c,('infeasible revisit',word,p,c)
        first.setdefault(p,c);last[p]=c
        h=(h+(1 if c=='R' else -1))%4
        dx,dy=((0,1),(1,0),(0,-1),(-1,0))[h]
        x+=dx;y+=dy
    return {'end':(x,y,h),'first':first,'last':last}

def main():
    data=json.loads((HERE/'five_macro_footprints.json').read_text())
    for k in 'UV':
        t=trace(data[k]['word']);dx,dy=DELTA[k]
        assert t['end']==(dx,dy,0)
        assert {p for p,c in t['first'].items() if c=='L'}==A|F[k]
        assert min(y for x,y in t['first'])==-1
        assert max(y for x,y in t['first'])==dy
        assert {x for x,y in t['first'] if y==dy}=={dx,dx+1}
        assert all(t['last'].get(p)=='R' for p in shift(A,DELTA[k]))
    for a,b in product('UV',repeat=2):
        t=trace(data[a]['word']+data[b]['word'])
        required={p for p,c in t['first'].items() if c=='L'}
        assert required==A|F[a]|shift(F[b],DELTA[a])
        assert len(required)==4+len(F[a])+len(F[b])
    report={
        'common_initial_four':sorted(A),
        'fresh_U':sorted(F['U']),'fresh_V':sorted(F['V']),
        'all_four_junctions_feasible':True,
        'exact_minimum_seed_mass':'4 + 5 * number_of_U + 2 * number_of_V',
        'length_bound':'28 * number_of_U + 18 * number_of_V <= 9 * (mass - 4)',
        'all_length_argument':'Each block advances y by at least 3; its reads range from start_y-1 to end_y. Nonadjacent footprints are disjoint. Four explicit junction checks and the fresh-site top-row check therefore apply inductively.'
    }
    (HERE/'uv_fuel_verification.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))

if __name__=='__main__':main()
