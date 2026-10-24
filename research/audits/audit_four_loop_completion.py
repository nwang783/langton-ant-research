"""Independent cross-check of the new all-parameter completion certificate.

The final all-L tail is checked by the previously audited rectangle-tail
implementation, rather than only the newly written infinite-tail function.
"""
import importlib.util
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
SRC = HERE.parent / "continuation_2026-10-22"
NEW = HERE / "four_loop_snapshot"
sys.path[:0] = [str(NEW), str(SRC / "ant_continuation2" / "planar_structure")]
import certify_completion as N
import certify_exceptional_rectangle as C
A = N.a
A.LOW = 128
for key in A.STATS:
    A.STATS[key] = 0
A.READ_POINTS.clear()
A.READ_RAYS.clear()

template = json.loads((NEW / "completion_template.json").read_text())

# The fixed initial block really is absent from the entire blank transient.
blank, p, h, reads = N.REFERENCE
assert not (set(reads) & N.block((-127,-108)))
assert p == (-15,10) and h == 3

field, p, h = N.get_prefix_field()
assert p == A.point(4,22) and h == 2
first, period, last = (template[k] for k in
                       ("prefix_word","period_word","suffix_word"))
assert len(first) == 1766 and len(period) == 104 and len(last) == 3397
fd = A.word_data(first,h)
p = A.apply_finite(field,fd,p,0,"independent-completion-first")
h = fd[3]
assert p == A.point(-19,33) and h == 0
pd = A.word_data(period,h)
assert pd[2:] == ((-2,2),0) and period in N.PHASES
p = A.apply_periods(field,pd,p,0,(1,2),"independent-completion-flight")
h = pd[3]
ld = A.word_data(last,h)
p = A.apply_finite(field,ld,p,0,"independent-completion-last")
h = ld[3]
assert p == ((-2,-40),(2,57)) and h == 1
tail = last[-104:]
assert tail in N.PHASES
td = A.word_data(tail,h)
assert td[3] == h and td[2] == (-2,2)

new_result = N.certify_infinite(field,td,p)
old_result = C.verify_infinite_period(field,td,p)

# A one-bit discrepancy on the future ray, astronomically far ahead, must
# invalidate both certificates. The point is affine in L, so this rejection
# also concerns every parameter, not one numerical evaluation.
far = 10**60
marker = A.padd(p,(A.scale((0,far),-2),A.scale((0,far),2)))
field.add_points([marker])
rejections = []
for label,fn in [("new infinite-ray checker",N.certify_infinite),
                 ("baseline rectangle-tail checker",C.verify_infinite_period)]:
    try:
        fn(field,td,p)
    except AssertionError:
        rejections.append(label)
    else:
        raise AssertionError(("remote marker falsely accepted",label))

elapsed = A.add((416,37740),
                A.add((0,len(first)+len(last)),A.scale((1,2),len(period))))
assert elapsed == (520,43111)

out = {"status":"PASS", "domain":"every integer L >= 128",
       "capture_time":elapsed,"pose":[p,h],
       "new_infinite_tail":new_result,"baseline_infinite_tail":old_result,
       "remote_marker_rejected":rejections,
       "scope":"Exact symbolic checker audit; no full-conjecture claim."}
(HERE / "four_loop_completion_audit.json").write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps(out,indent=2))
