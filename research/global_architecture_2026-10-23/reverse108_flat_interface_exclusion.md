# A fixed cap cannot feed the prepared108 return rewriter from a standard wake

23 October 2026. New finite interface comparison, using the construction
analysis's retained `reverse108_prepared_control.json` as a supplied candidate.
This is not a classification of rewriters or a universal-capture proof.

## Result

Let H be the literal standard104 word. Let V be its reverse complement, and
let P be V with zero-based letter31, which is L, replaced by LRRRR. Thus P has
108 letters. Consider the entire supplied architecture

    H^n C P^n

starting at the origin heading E. The fixed finite literal cap C may be
arbitrary, but must end heading W so that P returns along the producer's
diagonal. Its initial finite board may vary with n.

There is NO such cap for which these words are legal for every sufficiently
large n with a uniformly bounded initial black mass. More precisely, writing
q for C's displacement relative to the producer endpoint:

* If q_x-q_y is in {-10,-8,...,8,10}, some sufficiently large n makes the word
  chronologically impossible, regardless of initial mass.
* At every other allowed displacement, every legal word requires

      initial black mass >= 11*n - 6 - |C|.

P itself is a genuine legal periodic prepared-input rewriter with positive
cyclic K cost49. Its input has11 black drift classes, its output3, and its
complete history uses23 classes. The result does not invalidate that positive
control. It distinguishes legal prepared input from a realizable standard-wake
producer interface.

## Exact finite certificate

Use the full-drift class label

    (t,e)=(x-y, x mod2).

Both drifts are parallel to (2,2), so this exactly labels the quotient by the
full drift lattice, not merely by its primitive direction. For each literal
phase i at q_i, write q_i=r+k_i*d with r=(e,e-t). Order its visits by
i-|word|*k_i. This is the complete temporal order at a remote physical cell.
Every order reconstructed here alternates R,L.

For H at heading E, drift is (2,2). All22 classes have first letter R, so a
remote producer cell is necessarily initially white. Its final color is black
exactly when its last letter is R;12 classes are black. For P at heading W,
drift is (-2,-2), and its first letter prescribes the required entry color.

Conservation of (x+y+heading) mod2 forces q_x-q_y even. Translation of a P
class is exactly

    (t,e) -> (t+q_x-q_y, (e+q_x) mod2).

The finite producer and consumer read strips intersect only for the eleven
even transverse translations -10,-8,...,10. For EACH of these and BOTH x
parities, the checker lists an explicit P first-read color disagreeing with
H's mature output at a class that H reads. Thus all22 cases have an actual
chronological mismatch, not just a difference between black-support lists.

The executable checker is `check_reverse108_interface.py`; its complete table
and phase histories are in `reverse108_interface_certificate.json`. It does
not search words, cap lengths, periods, spatial boxes, or time horizons.

## Why a fixed cap cannot repair an intersecting case

Choose the mismatched P class in the certificate. Let its canonical
representative be r_P, and let r_H be the representative of the translated H
class. There is an integer K with q+r_P=r_H+K*(2,2).
Use P's longitudinal coordinate l, so the physical cell is

    n*(2,2)+q+r_P+l*(-2,-2).

Let p_min,p_max be the minimum and maximum k_i in this P class, and let
h_min,h_max be those for H. All P visits at this cell occur within the n
consumer copies whenever

    p_max <= l <= n-1+p_min.

All H visits occur within the n producer copies whenever

    K-h_min+1 <= l <= n+K-h_max.

Their intersection has max(0,n-D) cells, where the explicit finite constant is

    D=max(p_max,K-h_min+1)-min(p_min-1,K-h_max)-1.

All producer reads precede the cap; all consumer reads follow it. On every
one of these cells, the output of the last producer read disagrees with the
input of the first consumer read. An execution therefore requires C to read
each such cell at least once. C reads at most |C| distinct cells. Consequently

    n > D+|C|  implies chronological impossibility.

No change of initial black cells can alter the prescribed producer output.
This argument explicitly retains the whole field and all read histories.

## Why an off-strip case has linear initial fuel

Outside the eleven transverse translations, no P drift class meets any H
read class, at any longitudinal coordinate. Each of P's11 required-black
classes supplies at least n-(p_max-p_min) cells at which all consumer visits
are present and the first read requests L. The sum of these11 width losses
is exactly6, as checked from the full histories.

These cells are disjoint across drift classes. H touches none. C can touch
at most |C| of them. Every other one must be initially black. This proves
11*n-6-|C|, even when the entire finite seed depends on n.

## Implementation scope and retained work

This profile test is a necessary interface criterion, not a sufficient
construction theorem. A profile match in another candidate would still
require the actual finite cap, startup chronology, producer boundaries, and
all-n initial-fuel proof. The accompanying `flat_collinear_validator.py`
implements those exact supplied-word tests for nonzero collinear drifts; it
does not synthesize a cap or a rewriter.

Full-history orbit grouping and sector conservation are retained tools. The
new content here is their finite all-translation comparison for the supplied
prepared108 candidate, plus the explicit fixed-cap boundary argument. No
general semilinear extractor or general pump finder is claimed.
