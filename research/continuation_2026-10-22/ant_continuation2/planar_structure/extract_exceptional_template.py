"""Generate, but do not certify, a one-parameter word template.

The subsequent affine-field verifier must check every prescribed color for
all parameters. Matching two simulations is only a candidate generator.
"""
import json
from pathlib import Path

DIRS = ((0, 1), (1, 0), (0, -1), (-1, 0))


def literal(n, count):
    black = {(-33-2*n,-14-2*n), (-33-2*n,41+2*n),
             (8+2*n,-14-2*n), (8+2*n,41+2*n)}
    p, h = (0, 0), 0
    word = []
    for _ in range(count):
        b = p in black
        word.append('L' if b else 'R')
        if b: black.remove(p)
        else: black.add(p)
        h = (h + (-1 if b else 1)) % 4
        dx, dy = DIRS[h]
        p = p[0] + dx, p[1] + dy
    return ''.join(word), p, h


def long_runs(word, minimum=1040):
    runs = []
    a = 0
    end = len(word)-104
    while a < end:
        if word[a] != word[a+104]:
            a += 1
            continue
        b = a+1
        while b < end and word[b] == word[b+104]: b += 1
        if b-a >= minimum:
            # Select a whole-period prefix of this maximal periodic region.
            count = (b-a+104)//104
            runs.append((a, count))
        a = b+1
    return runs


def main():
    base = 200
    w0, p0, h0 = literal(base, 200304+728*base)
    w1, p1, h1 = literal(base+1, 200304+728*(base+1))
    r0, r1 = long_runs(w0), long_runs(w1)
    assert len(r0) == len(r1)
    segments = []
    last0 = last1 = 0
    for (a0,c0),(a1,c1) in zip(r0,r1):
        gap0, gap1 = w0[last0:a0], w1[last1:a1]
        assert gap0 == gap1, ('nonmatching gap',a0,a1)
        if gap0: segments.append({'type':'finite','word':gap0})
        period0,period1 = w0[a0:a0+104],w1[a1:a1+104]
        assert period0 == period1
        coefficient = c1-c0
        constant = c0-coefficient*base
        assert coefficient >= 0
        segments.append({'type':'periods','word':period0,'count':[coefficient,constant]})
        last0,last1 = a0+104*c0,a1+104*c1
    assert w0[last0:] == w1[last1:]
    if w0[last0:]: segments.append({'type':'finite','word':w0[last0:]})
    assert sum(s['count'][0] for s in segments if s['type']=='periods') == 7
    out={'status':'candidate extracted from two literal runs; requires affine verification',
         'base':base,'family':'{-33-2n,8+2n} x {-14-2n,41+2n}',
         'time':[728,200304], 'final_pose_at_base':[p0,h0],
         'final_pose_at_base_plus_one':[p1,h1], 'segments':segments,
         'infinite_tail_word':w0[-104:]}
    Path(__file__).with_name('exceptional_rectangle_template.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ('segments','infinite_tail_word')},indent=2))
    print(json.dumps([{'type':s['type'],'length':len(s['word']), 'count':s.get('count')} for s in segments],indent=2))


if __name__=='__main__':main()
