"""Independent exact finite-support obstruction for the T24 graph cycle."""
from pathlib import Path
import json

HERE=Path(__file__).resolve().parent
DIRS=((0,1),(1,0),(0,-1),(-1,0))

def main():
    data=json.loads((HERE/'no_pair_graph_result.json').read_text())
    word=next(c['word'] for c in data['cyclic'] if c['size']==24)
    x=y=h=0;visits=[]
    for i,c in enumerate(word):
        visits.append((x,y,i,c))
        h=(h+(1 if c=='R' else -1))%4
        dx,dy=DIRS[h];x+=dx;y+=dy
    assert (x,y,h)==(2,0,0)
    # All cells on each listed ray are first read in their corresponding
    # period at the listed phase, and that first read is L.  Later periods
    # cannot create those black bits before this first read.
    rays=[]
    for phase in (7,22):
        qx,qy,_,c=visits[phase];assert c=='L'
        same=[]
        for px,py,i,letter in visits:
            if py==qy and (px-qx)%2==0:
                shift=(px-qx)//2
                same.append((shift,i,letter))
        # Cell q+n*(2,0) is visited in period n-shift at phase i.
        # Larger shift means earlier period.  Phase breaks ties.
        first=min(same,key=lambda v:(-v[0],v[1]))
        assert first==(0,phase,'L')
        rays.append({'base':[qx,qy],'drift':[2,0],'first_read_phase':phase,
                     'same_orbit_phase_visits':same})
    assert rays[0]['base'][1]!=rays[1]['base'][1]
    out={'word':word,'length':24,'end_pose':[2,0,0],
         'required_disjoint_initial_black_rays':rays,
         'conclusion':'Every infinite T24 repetition requires infinitely many initially black cells.'}
    (HERE/'t24_verification.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
