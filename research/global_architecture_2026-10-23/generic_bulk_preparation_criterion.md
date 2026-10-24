# A decidable supplied-consumer bulk criterion and linear preparation bounds

23 October 2026. Generic structural extension of the independently signed
P108 finite-flight lemma. The new generic implementation and common-period
extension are submitted separately for audit. No consumer/period scan occurs.

## 1. Effective hypothesis and exact exceptions

Supply a nonempty literal R/L word P and an incoming heading. Geometry and
the complete full-drift read histories are computable exactly. A genuine
periodic translating consumer must restore heading and have nonzero drift.

Other fixed words admit finite preprocessing. If P changes heading, take its
geometric heading-order r<=4; P^r has zero displacement. If P itself restores
heading with zero drift, take r=1. The finite word P^(2r) cannot be legal:
otherwise its full field and pose recur exactly, contrary to the retained
strict integer clock (not a new result here). A direct finite-history check
returns the actual consecutive-same-turn witness. No infinite search is used.

For a nonzero translating P, group literal reads modulo its FULL drift, and
order a slot at u_i=rep+k_i*d by i-|P|*k_i. If one complete history does not
alternate, n>max k_i-min k_i forces that impossible history inside P^n. Hence
only internally alternating profiles need a preparation criterion. Their
first turns prescribe the exact mature input colors.

The effective hypothesis for the theorem below is:

    NO conserved-sector finite compatible bundle of mature white-written
    standard104 rails matches P's complete first-read input profile.

The empty bundle is included. MATCH means only a necessary bulk interface;
it is not a finite-cap launch, joint chronology proof, or compiler.
INCOMPATIBLE gives an explicit quantitative consequence, not universal capture.

The strict-clock source is retained `../computability/rigid_reachability.md`,
Section1. Complete orbit histories, first-read colors, sector conservation and
integer lattice intersections are retained tools. This note's new content is
the generic finite rail-selector test and its common-period preparation lift.

## 2. Non-diagonal drift: only the empty bundle can matter remotely

If P's drift is not parallel to either standard diagonal, every standard read
strip intersects any ONE P drift orbit in at most22 physical cells. If all
P complete histories start R, the empty white profile matches and this test
has no obstruction. Otherwise select one first-L orbit with offset width w.
At least n-w cells have its complete P history. Standard flights touch at most
22F of them; cap words touch at most L. Every remaining one is initially black.
Thus for any legal prefix with F standard flights, L other reads, then P^n,

    |B| >= n-w-L-22F.

Flight lengths and placements are arbitrary. This case needs no rail-selector
solver. It explicitly does NOT exclude a supplied internally legal WHITE-input
translator; such a candidate is an exception requiring its own analysis.

## 3. Diagonal drift: finite common-period input comparison

Rotate the supplied geometry so P has drift(-a,-a), a>0, and incoming heading h.
Let

    l=lcm(a,2), q=l/a in {1,2}, r=l/2,
    Q=P^q, D=(l,l), S=H^r.

Q drifts -D and standard superword S drifts +/-D. Group Q reads by the exact
joint classes

    (t,e)=(x-y,x mod l), 0<=e<l.

For each class record the complete first color. This includes BOTH longitudinal
phases when a is odd; checking only one would be unsound. Standard output is
periodic modulo2, so its color at (t,e) uses e mod2.

Each canonical standard rail has an eleven-normal read band, all l residues
at every normal, with black at every residue on both extreme normals. Any two
complete white-input rails that overlap would make the later first R read an
earlier black endpoint. Thus compatible bands are pairwise disjoint.

Only rails contributing to a required-black Q class need be selected. All
others can be removed without damaging a match: they supply no needed black
and can only pollute a required white. Every contributor has a finite anchor

    input black class = translated standard black class.

Canonical NE/SW writer headings are odd, so their relative translation normal
must satisfy t_translation=h-1 modulo2. Both x parities are allowed. These
anchors generate EVERY candidate rail, not just a spatial box. There are
finitely many candidates for the given P.

Use one Boolean variable per candidate. The exact finite criterion has:

* A covering clause for every required-black Q class.
* A negative unit clause for every rail polluting a required-white class.
* A pairwise exclusion clause for every overlapping pair of read bands.

Satisfiability is exactly bulk-profile compatibility. 
The procedure analyzes ONE supplied P, not existence of some P.

`bulk_standard_compatibility.py` implements this construction and a complete
finite selector search. It can emit the CNF and use the retained monotone RUP
producer/checker to certify an incompatible instance. Backend failures are
not interpreted as an UNSAT certificate. Its geometric normalization, orbit
histories, and CNF semantics are proof obligations distinct from RUP checking.

## 4. Computable fuel-or-routing constants

Let W_Q be the range of the phase offsets floor(x/l) over Q. Let W_H be the
maximum phase-offset range of S=H^r over both parallel headings and all l
relative x residues. Let [t_min,t_max] be Q's full read-normal range. All these
are exact finite computations. Define

    C_parallel = 2*W_H + 104*(r-1),
    C_nonparallel = 22*l*(t_max-t_min+21).

If the finite criterion is INCOMPATIBLE, ANY legal prefix

    C0 H^N1 C1 ... H^NF CF P^n

on the entire initial board B satisfies

    |B| >= floor(n/q) - W_Q - L
           - C_parallel*r_parallel - C_nonparallel*r_nonparallel.

All Nj are arbitrary nonnegative integers; every H flight may use any diagonal
direction. L is the total number of non-H reads in C0,...,CF. Constants do not
depend on flight lengths, offsets, cap shapes, n, or B. A coarse equivalent
form is n<=q*(|B|+L+C(P)F+W_Q)+q-1 with C(P)=max of the two coefficients.
Arbitrary cyclic standard phases add at most104 reads per flight to L.

### Exact reductions behind this inequality

Use the legal prefix ending at Q^floor(n/q); ignore at most one final P copy.
Split each PARALLEL standard flight H^N into S^floor(N/r) followed by fewer
than r H periods. Charge these residual reads to caps, at most104*(r-1) per
parallel flight. Nonparallel flights retain their original22 full-drift lines.

Every physical cell has a unique common gauge relative to the actual Q start:

    cell = origin + (e,e-t) + k*D, 0<=e<l.

There are at least floor(n/q)-W_Q levels with every consumer phase present.
For a parallel S flight, the level of each phase is a_i+sigma*j. Outside two
endpoint windows of W_H levels each, it is complete or absent. This remains
true for flights shorter than the fringe width.

Every relevant parallel writer band lies inside

    U=[t_min-10,t_max+10].

U has l*(t_max-t_min+21) full-D classes. Each of a nonparallel flight's22
affine lattice lines intersects each U class in at most one cell, regardless
of offsets or lengths. Discard those common levels and every cap-read level.

At a retained level no cap or nonparallel writer touches U. Every parallel
writer is complete or absent. Its first read at each visited class is R.
Therefore a black endpoint left by an earlier relevant writer cannot be
erased by ANY intermediate parallel writer: that writer's first R there would
already be illegal. This includes intermediate writers not themselves meeting
the consumer. Hence relevant active writer bands are disjoint, and their final
colors are exactly one of the bundles rejected by the finite criterion.

A required-white mismatch or a required-black cell left white by any active
writer contradicts legality. The only remaining possible mismatch is a required
black outside all writer reads; with all interventions discarded it belongs
to the ORIGINAL B. Different retained k give different physical cells. Counting
them proves the inequality with no hidden multiplicity factor or lost debris.

## 5. Executed controls and architecture-level use

The supplied P108 instance gives q=1, W_Q=2, C_parallel=6 and
C_nonparallel=1408, exactly recovering the independently signed theorem.
The standard104 word returns MATCH_EMPTY_WHITE_PROFILE, preventing a spurious
claim that all periodic continuation costs growing fuel. Reverse104, D10 and
LR reject with separately checked one-addition RUP proofs; D10 and LR exercise
the odd-drift two-copy joint period. Axis RLLR exercises the non-diagonal
22F bound. R and RRRR return explicit finite-power chronological conflicts.
These are supplied-word controls, not a consumer scan or a general code audit.

For a finite supplied architecture of P words, a uniform lower bound follows
if its joint selector encoding excludes all compatible bundles and the offset
and normal-range constants have effective uniform bounds. The word may vary
between family parameters n, but each P^n run must repeat ONE selected word;
occurrence-dependent directives are not included.

The construction analysis's exact1/5/9 reverse scaffold has such uniform
data: every selected word drifts(-2,-2), every possible phase x//2 lies in
[-2,2], and its potential read-normal range is[-8,6] in the new origin convention.
Consequently q=r=1, W_Q<=4 and U=[-18,16] has70 classes. The new multi-rail
selector encoding and its all-bundle RUP exclusion have now been independently
reconstructed, including all input-OR and disjoint-band semantics. They yield

    |B| >= n-4-L-6*r_parallel-1540*r_nonparallel.

No enumeration of10^104 words is required for this lift. This
application is narrower than arbitrary refinements, longer images, changing
periods, general finite-seed ant dynamics, or a uniform defect budget.
The concise signed-premise corollary is frozen separately in
`multirail_refinement_preparation_corollary.md`.
