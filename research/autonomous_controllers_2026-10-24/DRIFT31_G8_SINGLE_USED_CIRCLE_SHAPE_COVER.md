# A finite conditional shape cover at full drift (3,1), growth eight

24 October 2026. Author proof-producing cover, submitted for independent review.
Its hypothesis is an ACTUAL single-used first-R circle. It neither forces such
a circle for arbitrary(3,1) fronts nor asserts that a surviving interface completes.

## Signed finite geometric reduction, not a bounded period scan

The independently signed corrected charge7774dde0/report21f678e1 gives, for a
single-used F circle, ell<=2g and g>=2D+2*tau, where tau is its number of triple
left corners. At g8 and actual d=(3,1), D=3, so ell<=16 and tau<=1. The essential
circle has full winding-1 and alternating movement axes. If m=ell/2, it has
m horizontal and m vertical steps with displacement(-3,-1). Therefore m is odd,
m>=3, and the ONLY possible lengths are6,10,14. This bounds the geometric circle,
not the unknown period, history multiplicities outside it, or support width.

For m=3,5,7, choose the horizontal-step positions in either alternating axis
phase, choose exactly(m-3)/2 of those steps to be E, and choose exactly(m-1)/2
vertical steps to be N. All other steps are W or S. This directly exhausts
6,100,1470 paths, respectively, with the required full endpoint displacement.
No reflection, reversal or primitive replacement is used.

Since T=3y-x identifies exactly the full(3,1) classes, simplicity requires that
all ell read vertices have DISTINCT T. Every length10 and14 path repeats a
full class. Each of those1,570 paths has an explicit pair of equal-T vertex
indices in the certificate. All six length6 parametrizations are cyclic cuts
of the SAME circle. Translation to its minimum-T vertex gives outgoing word

    W N W S W S,

at normal levels0,1,4,5,2,3, respectively. Its lifted vertices are
(0,0),(-1,0),(-1,1),(-2,1),(-2,0),(-3,0), ending at(-3,-1)=-d.

## Quadruple placements and exact internal physical ports

The geometric right corners are levels0,1,2 and have singleton complete
histories S,W,S. The left corners are levels3,4,5. Their histories are
EEW[ E ], SSN[ S ], EEW[ E ], with the bracketed last read present exactly at
a quadruple. The corrected charge requires at least two of these three left
corners to be quadruple. All four such subsets are retained, and all pass the
separate-fibre deficit bound. Passing that necessary arithmetic test does not
assert realizability.

Two subsets, {3,5} and {4,5}, fail EXACT internal directed port totals between
levels3 and4. Their complete source and target read ranks and full seam voltage
are stored as mismatch witnesses. No exterior cell can repair an edge whose
TWO endpoint histories are already complete.

Only two complete-circle profiles survive, in level order0 through5:

    S, W, S, EEWE, SSNS, EEW;
    S, W, S, EEWE, SSNS, EEWE.

The first has fourteen named reads, two quadruple left corners and one triple;
the second has fifteen reads and three quadruple left corners. Both have
internally consistent OPEN successor graphs. All classes not on the circle
are UNKNOWN in the checker, including lower normal levels. No outside cell
is silently set empty, WHITE, or cap-limited. The signed right-side support
lemma is available but is not needed to close any omitted port here.

## One concrete surviving exterior obligation

In either surviving profile the next vertical-axis class at T=6 has exactly
three incoming N occurrences. Its outgoing E count is2 in the first profile
and3 in the second, as required by the complete T=5 history.
The exact lower path from its FIRST E departure through levels5,2,3 returns
to its SECOND N arrival in four actual steps, at the SAME physical cell.
Thus the second N rank is immediately after the first E rank.

The mandatory count identity derives n6<=11 or13, respectively. Complete binary
heading enumeration with that exact first return gives7 and13 histories:
all20 retain open internal graphs. They are fully listed in the certificate.
No claim is made that these cells, their exterior ports, or the whole circle
can be completed consistently. The two profiles and twenty next-cell histories
are precise remaining obligations, not new finite seeds or controllers.

## Evidence and scope boundary

`certify_drift31_single_used_g8_shapes.py` regenerates all1,576 geometric paths,
each repeated-class witness, all four placements and their exact fibre arrays,
the two internal port contradictions, and both surviving successor interfaces.
`drift31_single_used_g8_shapes_certificate.json` retains every witness and all
20 complete next-cell histories. `DRIFT31_SINGLE_USED_SHAPES_SHA256SUMS` binds the
signed charge premise and direct geometric/ordinal code dependencies.

The separate unconditional25-case read-minimum theorem92b5092a/report2bf25e31
is consistent with these surviving profiles, but is NOT needed as a premise
for the finite shape cover. The present certificate does not eliminate any
front whose F circles are all multiply used. The universal finite-support
highway conjecture and eventual-periodic classification remain unsolved.
