# C-free macro start centers are pairwise distinct

Status: all-length deduction from the audited29-site freshness theorem;
independent analytic and literal-word review passed. The finite ingredient checker is
verify_cfree_center_self_avoidance.py.

For a physical pose(p,h), define the doubled coarse center

    K(p,h) = 2p + rot((-1,1),h).

In every physically feasible C-free word over U,V,Q,B, the values K at
its macro STARTS are pairwise distinct. The final endpoint is not claimed
here. The proof applies to every finite factor and does not use finite support.

## Previously proved input

Every site in the29-site marked family is unread before its own macro,
within a C-free factor. We use these particular consequences:

- U,Q,B each mark local(-1,0).
- V marks local(1,2).
- Each macro marks its terminal-star input: U(0,3), V(1,2), Q(-4,-3),
  B(-3,-4).
- A few further Q/B marked sites, recorded explicitly in the checker.

Every macro reads local(-1,0),(0,1),(1,2). Q and B also read(-2,-1).
U reads(-1,2).

## Choose a minimum-span repeated pair

Suppose macro starts i<j have equal centers, with j-i minimal. Rotate and
translate so macro i starts at(0,0,N). Since C is absent, headings are N/S.

If macro j also faces N, it starts at(0,0). A later U/Q/B repeats its marked
(-1,0); a later V repeats its marked(1,2). Each was read by macro i. Thus
macro j must face S and start at(-1,1).

If macro j is U/Q/B, its marked(-1,0) is physical(0,1), already read by i.
So macro j is V. If macro i is Q/B, the later V's marked tip is(-2,-1),
already read by i. Thus macro i is U or V.

A single macro never preserves its coarse center, so j>=i+2. Consequently
P, the macro immediately preceding j, occurs strictly after macro i.
Regardless of P's type, its terminal-star input is physical(-1,2).
If macro i is U, that site was read by i, violating P's marked freshness.
Hence macro i is V too.

The span cannot be2: the four possible two-macro center displacements
starting V are(1,7),(2,6),(-2,-2),(-1,-3), none zero. Thus j>=i+3.
Let A be the macro immediately following i. It starts at(1,3,N), strictly
before P. Every A reads physical(0,3) and(1,4).

The predecessor P of the later V has one of the following entries:

    U: (-1,5,S)    V: (0,4,S)
    Q: (3,5,N)     B: (2,6,N).

If P is U or B, its marked set contains physical(0,3).
If P is Q, its marked set contains physical(1,4).
Those sites were read by A, so P must be V.

P's marked tip is physical(-1,2). If A were Q or B, A would have read that
site, since its local(-2,-1) maps there. Thus A is U or V.

The entries of A and P are respectively(1,3,N) and(0,4,S), which have the
same doubled center(1,7). They occur at i+1<j-1 and have strictly smaller
span, contradicting the choice of i,j.

Therefore no repeated macro-start center exists.

## Scope

This is stronger than the earlier one-fold center-disjointness result for
C-free factors. It does not apply across C blocks: known C-containing
examples revisit centers. It is not a full completed-C marker-freshness
proof, but it rules out the hidden center return in the current finite-patch
terminal-C abstract witnesses.
