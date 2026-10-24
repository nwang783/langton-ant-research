"""Exact16-edge second-S to first-W collision at a three-read LRL portal entry.
The shared outer reader may start either color, with no imposed read cap.
"""
from pathlib import Path
from itertools import product
import json
H = 'NESW'
VEC = {'N':(0,1), 'E':(1,0), 'S':(0,-1), 'W':(-1,0)}
D = (0,3)
rows = []

def out(word, rank, black=False):
    return H[(H.index(word[rank]) + (1 if (rank % 2 == 0) != black else -1)) % 4]

for root, reader in [('EWW','SSN'), ('EWWE','SSNN')]:
    fixed = {(1,1):'SN', (0,1):root, (0,0):'NNSS', (1,0):'EE',
             (1,2):'EEW', (0,2):reader, (1,3):'NNSS', (2,3):'EEW', (2,2):'S'}
    for black in [False, True]:
        for n in range(1, 10 if black else 9):
            for letters in product('EW', repeat=n):
                word = ''.join(letters)
                if word.count('W') != 2 or sum(out(word,r,black) == 'S' for r in range(n)) != 2:
                    continue
                hs = fixed | {D:word}
                successor = {}
                for p, h in hs.items():
                    for direction, vector in VEC.items():
                        q = p[0]+vector[0], p[1]+vector[1]
                        if q not in hs:
                            continue
                        sources = [r for r in range(len(h)) if out(h,r,black and p == D) == direction]
                        targets = [r for r,z in enumerate(hs[q]) if z == direction]
                        assert len(sources) == len(targets)
                        successor.update({(p,r):(q,s) for r,s in zip(sources,targets)})
                second_s = [r for r in range(n) if out(word,r,black) == 'S'][1]
                first_w = word.index('W')
                path = [(D,second_s), ((0,2),1), ((1,2),0), ((1,1),0), ((0,1),1),
                        ((0,0),3), ((1,0),1), ((1,1),1), ((0,1),2), ((0,2),2),
                        ((1,2),1), ((1,3),0), ((2,3),0), ((2,2),0), ((1,2),2),
                        ((1,3),1), (D,first_w)]
                assert all(successor[e] == f for e,f in zip(path,path[1:]))
                assert first_w != second_s+1
                rows.append(dict(portal_root=root, reader_starts_BLACK=black, D=word,
                                 second_S_rank=second_s, first_W_rank=first_w, actual16_channel=path))
assert len(rows) == 80
assert all(sum(r['reader_starts_BLACK'] == black and r['portal_root'] == root for r in rows) == (22 if black else 18)
           for root in ['EWW','EWWE'] for black in [False,True])
Path(__file__).with_suffix('.json').write_text(json.dumps(dict(scope=__doc__,rows=rows,
    proof='Second R_E leaves BLACK; next first-W read is L_W and would emit forbidden S third.',
    warning='Exact specified entry only; arbitrary later/spaced one-use transfers and other portal words remain open.'),indent=2)+'\n')
print('PASS both portal roots,all18WHITE/22BLACK exact reader words each,80 actual16 return collisions')
