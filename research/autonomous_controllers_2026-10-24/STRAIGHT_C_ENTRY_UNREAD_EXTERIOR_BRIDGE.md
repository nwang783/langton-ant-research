# Conditional unread-exterior bridge from C entries to a single-used F circle

24 October 2026. Author proof and exact controls; independent audit pending.
No visit cap is assumed. An ACTUALLY UNVISITED C row is assumed, and is not
inferred from any stream-height maximum.

## Precise conditional setting

Normalize by a proper rotation/translation. Suppose an actual stable full
translating history has a WHITE-owned straight C-entry cycle with full drift
 d=m(-1,1), m>=1. Lift its faces as

    u_i=(-i,i-1),     p_i=(-i,i),     i in Z,

so the selected first L at p_i crosses from u_i to u_(i+1). Its first R and
first L both have incoming N, by the signed C-entry ownership lemma. The
normalization may add a common constant to all coordinates; checker sector
changes do not affect the proof.

Assume the C row immediately on the positive x+y side of these u_i is NEVER
active anywhere in the complete history. Since active C faces form one
connected physical walk, this separates the whole active component from the
farther exterior as well. The proof only needs the immediate row. Other cells
may have arbitrary visit multiplicity or prepared BLACK-first histories.

## Exterior first-return argument

Let q_i=p_i+(1,0). The first R_N at p_i moves to q_i with incoming E. At q_i,
incoming W would itself put the active C face in the forbidden exterior row.
Incoming E followed by L would move the active C face into that row. Therefore
every possible read of q_i is E/R. Actual alternation allows only ONE such
read. Thus q_i is a genuine WHITE singleton, not an assumed fresh rail.

Every R_N at p_i goes to q_i, so there is exactly one R_N. An L_S there would
also go to q_i. It cannot occur before the first R_N, because that R is the
first read of p_i; afterward it would force a second read of q_i. Thus L_S
never occurs.

The unique E/R update at q_(i+1) moves south into p_i with incoming S. Since
L_S is impossible, this is an R_S. Moreover ALL incoming S visits to p_i have
that SAME physical predecessor q_(i+1), whose sole update was already fixed.
Hence p_i has exactly one R_S, not an arbitrary number of opposite-heading R
reads. Together with its first R_N/L_N and complete alternation, this forces
exactly

    p_i : NNS  or  NNSN,
    q_i : E (singleton R).

Thus the local cap3/4 is DERIVED from physical exterior ownership, not imposed.
It says nothing about multiplicities farther inside the visited C region.

## First-R circle and height consequence

The actual first-R departure map uses

    p_i -> q_i -> p_(i-1).

There are2m distinct full-drift classes in this embedded circle, with winding
−1. Each physical edge is used exactly once in the whole history: p_i→q_i
has its unique R_N source and no L_S substitute, and q_i→p_(i-1) has the
singleton q_i source. This is a single-used FIRST-R MAP circle, not a claim
that these first-read events occur consecutively as one literal ant excursion.
At the target p_(i-1), the arriving read is its later R2, not its first R0.

The unrestricted C-stream formula also gives equal heights along the C-entry
cycle, since R_N=R_S=1 at each p_i. Every q_i singleton makes its active C face
one level higher than the unvisited exterior C face. Hence the boundary level
is exterior+1. The converse is NOT proved: a height difference of one does not
by itself establish that the exterior C faces were never active.

## Exact controls and preserved escape

In standard104 the outer C-entry cycle satisfies the unread-row hypothesis.
Its selected read histories are NNS and NNSN and its outer corners are E/R
singletons; the resulting four-class first-R circle is truly single-used.
It is the C cycle supporting the14/90 excursion decomposition.

The other standard C-entry cycle has NNSNSSN and NNSNNSSN, and its outer row
IS active. Its7/8-read histories and10/94 excursion decomposition therefore
remain valid and are explicitly retained outside the hypothesis. The lemma
must not be applied to both cycles by simply choosing an extremal height.

Prepared10 also satisfies this geometric exterior condition after rotation.
Its selected cell is NNSN and its resulting two-class first-R circle is
single-used, while its genuine BLACK fuel input remains. Consequently this
bridge alone does not establish complete WHITE, exclude prepared waves, or
force standard104.

The executable checks both complete controls and full powers1,2,3,5. Each
power retains every full-drift class rather than replacing d by its primitive
direction. All selected cell/corner histories and exact circle voltages are
stored. No cap on the unbounded interior is imported.

## The exact missing global premise

An extremal-height discovery cycle has NOT been shown to have this unvisited
outer row. Even the global active-C maximum need not occur on a discovery
cycle, as the separate standard height countercheck shows. Nor does this local
boundary lemma force a finite alphabet of the closed interior excursions.
The theorem is a conditional physical bridge, not a global one-use existence
theorem, controller classification, or finite-seed attraction result.

## Artifacts

certify_straight_outer_C_cycle_bridge.py
straight_outer_C_cycle_bridge_certificate.json
