"""Certify the whole exceptional rectangle family for all n >= LOW.

This reuses the independently documented affine-ray parity engine from the
previous round. The candidate word comes from a finite generator, but every
prescribed read is proved algebraically for the entire parameter range.
The final infinite tail is verified against the complete retained field.
"""
import importlib
import gzip
import json
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(ROOT / 'ant_continuation' / 'wake_clock'))
import certify_four_scatterer_prefix as A


def fast_no_point_collision(p, q):
    """Same exact predicate as the older engine, with early constant tests."""
    dx, dy = A.psub(p, q)
    if dx == A.ZERO and dy == A.ZERO:
        return False
    A.STATS['excluded_isolated_equalities'] += 1
    if (dx[0] == 0 and dx[1] != 0) or (dy[0] == 0 and dy[1] != 0):
        return True
    a = dx if dx != A.ZERO else dy
    # a*n+b=0 can hold at an admissible integer only in this case.
    if a[0] == 0 or (-a[1]) % a[0] != 0:
        return True
    r = (-a[1]) // a[0]
    if r < A.LOW:
        return True
    assert dx[0]*r+dx[1] != 0 or dy[0]*r+dy[1] != 0, (
        'isolated point collision', p, q, r)
    return True


def clip_infinite(lo, hi, unused):
    if A.negative(hi):
        return None
    lo = A.maximum(lo, A.ZERO)
    A.STATS['affine_guards'] += 1
    if A.negative(A.sub(hi, lo)):
        return None
    assert A.nonneg(A.sub(hi, lo)), ('infinite interval opens', lo, hi)
    return lo, hi


def verify_infinite_period(field, data, base):
    required, odd, drift, end_heading = data
    flips = [A.translate_local(q, base, 0) for q in odd]
    old_clip = A.clip
    A.clip = clip_infinite
    try:
        for q0, bit in required.items():
            q = A.translate_local(q0, base, 0)
            boundaries = {A.ZERO} if bit else set()
            for b in field.points:
                k = A.line_coordinate(A.psub(b, q), drift)
                if k is not None:
                    A.toggle_boundary(boundaries, A.clip(k, k, None))
            for b, e, count, _ in field.rays:
                A.toggle_boundary(boundaries,
                    A.previous_ray_interval(q, drift, b, e, count, None))
            for b in flips:
                m = A.line_coordinate(A.psub(b, q), drift)
                if m is not None:
                    assert m[0] == 0
                    if m[1] > 0:
                        boundaries.symmetric_difference_update({m})
            assert not boundaries, (
                'uncancelled infinite-tail parity', q0, sorted(boundaries))
            A.STATS['periodic_read_constraints'] += 1
    finally:
        A.clip = old_clip
    return {'distinct_required_cells':len(required),
            'odd_read_cells':len(odd), 'drift':drift,
            'heading':end_heading}


def affine_coordinate_bounds(field, coordinate, omitted=()):
    """Conservative support bounds; XOR cancellations can only improve them."""
    select = ((1, 1) if coordinate == 'z' else (1, -1))
    def project(p):
        return A.add(A.scale(p[0], select[0]), A.scale(p[1], select[1]))
    values = [project(q) for q in field.points if q not in omitted]
    for base, d, count, _ in field.rays:
        values.append(project(base))
        end = A.padd(base, (A.scale(A.sub(count,A.ONE),d[0]),
                           A.scale(A.sub(count,A.ONE),d[1])))
        values.append(project(end))
    # An affine quantity a*n+b has a uniform lower bound iff a>=0,
    # and a uniform upper bound iff a<=0.
    lower = min(A.val(x) for x in values) if all(x[0]>=0 for x in values) else None
    upper = max(A.val(x) for x in values) if all(x[0]<=0 for x in values) else None
    return {'lower':lower,'upper':upper,'affine_endpoints':len(values)}


def read_bounds():
    proxy = A.Field(set(A.READ_POINTS))
    proxy.rays = [(q,d,count,'read') for q,d,count in A.READ_RAYS]
    return {name:affine_coordinate_bounds(proxy,name) for name in ('u','z')}


def first_contacts(segment, data, base, heading, elapsed, inputs, already):
    points, _, _, _ = A.plan(segment['word'], (0,0), heading)
    candidates = {}
    if segment['type'] == 'finite':
        earliest = {}
        for i, p in enumerate(points): earliest.setdefault(p,i)
        for local, i in earliest.items():
            p = A.translate_local(local,base,0)
            for label, q in inputs.items():
                if p == q:
                    if label not in already:
                        candidates[label] = A.add(elapsed,(0,i))
                else:
                    assert A.no_point_collision(p,q)
    else:
        drift = data[2]
        count = tuple(segment['count'])
        for i, local in enumerate(points):
            p = A.translate_local(local,base,0)
            for label,q in inputs.items():
                k = A.line_coordinate(A.psub(q,p),drift)
                if k is None or not A.in_range(k,count): continue
                if label not in already:
                    time = A.add(A.add(elapsed,A.scale(k,104)),(0,i))
                    candidates[label] = A.minimum(candidates[label],time) if label in candidates else time
    already.update(candidates)
    return candidates


def main():
    template = json.loads((HERE/'exceptional_rectangle_template.json').read_text())
    A.LOW = template['base']
    A.no_point_collision = fast_no_point_collision
    for k in A.STATS: A.STATS[k] = 0
    A.READ_POINTS.clear(); A.READ_RAYS.clear()
    q = ((-2,-33),(-2,-14))
    a = ((-2,-33),(2,41))
    c = ((2,8),(-2,-14))
    d = ((2,8),(2,41))
    inputs = (q,a,c,d)
    input_labels = {'q_southwest':q,'a_northwest':a,'c_southeast':c,'d_northeast':d}
    for i, x in enumerate(inputs):
        for y in inputs[i+1:]: assert A.no_point_collision(x,y)
    field = A.Field(set(inputs))
    base, heading = A.point(0,0), 0
    elapsed = A.ZERO
    records = []
    contact_times = {}
    snapshots = []
    standard_words = {A.W[k:]+A.W[:k] for k in range(104)}
    assert len(A.W) == 104
    assert len(template['infinite_tail_word']) == 104 and template['infinite_tail_word'] in standard_words
    wall_start = time.monotonic()
    for i, segment in enumerate(template['segments']):
        data = A.word_data(segment['word'], heading)
        before = base
        hits = first_contacts(segment,data,base,heading,elapsed,input_labels,contact_times)
        if segment['type'] == 'finite':
            base = A.apply_finite(field, data, base, 0, 'finite'+str(i))
            elapsed = A.add(elapsed, (0,len(segment['word'])))
        else:
            assert len(segment['word']) == 104 and segment['word'] in standard_words
            count = tuple(segment['count'])
            assert A.nonneg(A.sub(count,A.ONE))
            assert data[3] == heading and abs(data[2][0]) == abs(data[2][1]) == 2
            base = A.apply_periods(field, data, base, 0, count, 'periods'+str(i))
            elapsed = A.add(elapsed, A.scale(count,104))
        heading = data[3]
        rec = {'segment':i, 'type':segment['type'], 'time':elapsed,
               'start':before,'end':base,'heading':heading,
               'field_point_terms':len(field.points),
               'field_ray_terms':len(field.rays),'new_input_contacts':hits}
        if i == 4:
            assert set(contact_times) == {'q_southwest'}
            rec['one_bit_archive_u'] = affine_coordinate_bounds(field,'u',{a,c,d})
            rec['prefix_read_bounds'] = read_bounds()
            parent = A.Field(field.points^{a,c,d}); parent.rays=list(field.rays)
            parent_data=A.word_data(template['segments'][5]['word'],heading)
            rec['one_bit_infinite_tail'] = verify_infinite_period(parent,parent_data,base)
        if i == 8:
            assert set(contact_times) == {'q_southwest','a_northwest'}
            rec['two_bit_archive_u'] = affine_coordinate_bounds(field,'u',{c,d})
            rec['prefix_read_bounds'] = read_bounds()
            parent = A.Field(field.points^{c,d}); parent.rays=list(field.rays)
            parent_data=A.word_data(template['segments'][9]['word'],heading)
            rec['two_bit_infinite_tail'] = verify_infinite_period(parent,parent_data,base)
        if i in (4,8,13):
            snapshots.append({'segment':i,'time':elapsed,'pose':[base,heading],
                              'point_terms':sorted(field.points),
                              'ray_terms':field.rays[:]})
        records.append(rec)
        print(json.dumps({**rec,'wall_seconds':round(time.monotonic()-wall_start,3)}),flush=True)
    assert elapsed == tuple(template['time'])
    assert contact_times == {'q_southwest':(104,10881),
                             'a_northwest':(312,71330),
                             'c_southeast':(520,144036)}
    tail = A.word_data(template['infinite_tail_word'],heading)
    assert tail[3] == heading
    assert tail[2] == (-2,2)
    infinite = verify_infinite_period(field,tail,base)
    # Verify that the northeast input corner is never read in the full
    # prescribed prefix, or in any subsequent tail period.
    for p in A.READ_POINTS:
        assert p != d and A.no_point_collision(p,d)
    for b, drift, count in A.READ_RAYS:
        assert not A.ray_membership(d,b,drift,count)
    for p in tail[0]:
        b = A.translate_local(p,base,0)
        k = A.line_coordinate(A.psub(d,b),tail[2])
        assert k is None or A.negative(k)
    out = {'status':'proved by exact affine-field read verification',
           'parameter_minimum':A.LOW,'family':template['family'],
           'time':elapsed,'tail_pose':[base,heading],
           'tail':infinite,'northeast_corner_never_read':True,
           'initial_cell_first_read_times':contact_times,
           'statistics':dict(A.STATS),'segments':records,
           'wall_seconds':round(time.monotonic()-wall_start,3)}
    (HERE/'exceptional_rectangle_affine_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
    with gzip.open(HERE/'exceptional_affine_fields.json.gz','wt') as f:
        json.dump({'parameter_minimum':A.LOW,'snapshots':snapshots},f,separators=(',',':'))
    print(json.dumps(out,indent=2),flush=True)


if __name__=='__main__':main()
