"""Literal all-multiplicity two-port return collision on a one-use L0 R L0 R L0 body.
Named seven WHITE cells have complete fixed histories. Outer reader Z may start
WHITE or BLACK; its exact Ein2/Nout2 domain bounds length by8 or9 algebraically.
"""
from pathlib import Path
from itertools import product
from collections import Counter
import json
H = 'NESW'
VEC = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}
A, R, B, S, C, U, V, Z = (0,-1), (0,0), (1,0), (1,1), (2,1), (1,-1), (2,0), (2,-1)
fixed = {A: 'WWE', R: 'N', B: 'WWE', S: 'N', C: 'WWE', U: 'SSNN', V: 'SSNN'}

def out(word, rank, black=False):
    turn_right = (rank % 2 == 0) != black
    return H[(H.index(word[rank]) + (1 if turn_right else -1)) % 4]

rows = []
counts = Counter()
for black in [False, True]:
    for n in range(1, 10 if black else 9):
        for letters in product('EW', repeat=n):
            word = ''.join(letters)
            if word.count('E') != 2 or sum(out(word, r, black) == 'N' for r in range(n)) != 2:
                continue
            r_e = sum(word[r] == 'E' for r in range(n) if (r % 2 == 0) != black)
            r_w = sum(word[r] == 'W' for r in range(n) if (r % 2 == 0) != black)
            assert r_e == r_w <= 2
            histories = fixed | {Z: word}
            successor = {}
            for p, h in histories.items():
                for direction, vector in VEC.items():
                    q = p[0] + vector[0], p[1] + vector[1]
                    if q not in histories:
                        continue
                    sources = [r for r in range(len(h)) if out(h, r, black and p == Z) == direction]
                    targets = [r for r, x in enumerate(histories[q]) if x == direction]
                    assert len(sources) == len(targets)
                    successor.update({(p, r): (q, t) for r, t in zip(sources, targets)})
            second_n = [r for r in range(n) if out(word, r, black) == 'N'][1]
            first_e = word.index('E')
            path = [(Z, second_n), (V,3), (B,1), (U,0), (A,0), (R,0), (B,2), (U,1), (Z, first_e)]
            assert all(successor[e] == f for e, f in zip(path, path[1:]))
            # A returned first-E rank before/equal to second-N is an ordinal reversal;
            # later than next rank skips reads; exactly next rank would emit N third.
            if first_e <= second_n:
                result = 'backward_rank'
            elif first_e != second_n + 1:
                result = 'skipped_rank'
            else:
                assert out(word, first_e, black) == 'N'
                raise AssertionError('would be a forbidden third N departure')
            counts[(black, result)] += 1
            rows.append(dict(reader_starts_BLACK=black, reader_word=word, second_N_rank=second_n,
                             first_E_rank=first_e, result=result, actual8_channel=path))
assert len(rows) == 40 and sum(not r['reader_starts_BLACK'] for r in rows) == 18
assert sum(r['reader_starts_BLACK'] for r in rows) == 22
Path(__file__).with_suffix('.json').write_text(json.dumps(dict(scope=__doc__,fixed_histories={str(p):h for p,h in fixed.items()},
    rows=rows,summary={str(k):v for k,v in counts.items()},
    conclusion='No initial color or multiplicity of the outer reader can complete this exact physical eight-step return.',
    warning='The all-size proof is the first-port/next-turn argument. The finite domains follow exact counts, not a chosen read cap.'),indent=2)+'\n')
print('PASS all18 WHITE/all22 BLACK exact count-domain histories; same actual8 return collides in every case')
