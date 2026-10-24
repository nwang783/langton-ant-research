# Finite physical macro bases under finite-power spatial refinement

2026-10-23 07:37 UTC. New analytic extension submitted for independent review.
KM signs the general additive-I macro solver and finite-order macro adapter;
this note separately treats the finite-power case, including singular matrices.
No implementation, accepted growing model or singular macro no-go is asserted.

## 1. Exact scope

For each state s supply a finite NONEMPTY physical R/L base word beta_s, its
incoming heading h_s, complete displacement v_s and final heading k_s. All
three pose data are computed literally. For every nonempty substitution image
phi(s)=t_1...t_m, require matching child boundary headings, the same initial
and final headings h_s,k_s, and

    sum_j v_(t_j) = A v_s.

A is an integer matrix. Supply mu>=0,q>=1 and verify exactly
A^(mu+q)=A^mu. No invertibility, angle preservation, nonzero v_s or unit v_s is
assumed. Let p_sj be the literal BASE-pose displacement before child j.

Choose an actual first-letter root cycle and a growing selected rooted-power
limit. Passing to a root-cycle power makes phi(a) begin with a. Physical
expansion means substitute macro labels r times, THEN replace every label by
its actual base word. Boundary-heading preservation proves inductively that
this is a physical geometric path, with net A^r v_s and child offset A^r p_sj.
Root-label growth and nonempty bases make the physical nested prefixes grow.
These hypotheses do not assert that any prefix is ant-legal.

**Claim.** For this specified infinite path, (i) legality from a supplied finite
seed is decidable, and (ii) existence of ANY finite realizing seed is decidable
and its unique minimal seed can be returned. Both are effective analytic
algorithms. Finite resources in an implementation may still yield UNKNOWN.

The proof below explicitly supplies the only changes to signed IJ/JF; it does
not replace recursive macros by unit letters or apply the unit singular no-go.

## 2. Full base parity and exact read footprints

Let q_(s,l) and ell_(s,l) be the local read position and required initial turn
bit (L=1) of physical read l of beta_s. Put

    Q_s(0;X,Y) = XOR_l X^q_(s,l).x Y^q_(s,l).y.

Every physical read is toggled separately: revisits can cancel. For all r>=0,

    Q_s(r+1,z) = XOR_j Q_(t_j)(r,z-A^r p_sj).

Thus the eventually periodic Laurent-matrix transfer in IJ is unchanged except
for its finite initial polynomial vector. Its phase generating functions are
still rational. Clearing negative exponents needs both per-depth and CONSTANT
base shifts, just as in KE/KM. The same finite Cartier construction gives
all Q_s(r,x,y) effectively as two-automatic relations. Zero initial polynomials
are permitted and do not certify legality.

The finite descending-exponent graph in JF represents a depth-r leaf macro
occurrence: its successive offset weights are exactly
A^(r-1)p_1,...,A^0 p_r. For mu>0 use its cyclic high phases and forced low suffix;
for mu=0 use cyclic phases and a terminal exit only after phase zero. An
accepted path's length and terminal exit determine the true descending power
sequence by counting backward. Arbitrary independent phase choices are NOT
allowed. Handle r=0 separately.

At a terminal macro state t, append a terminal edge for EACH physical base read
l, of constant spatial weight q_(t,l), and macro-depth weight zero. These
terminal edges have no continuation and hence belong to no directed cycle.
A root-to-terminal path has position

    sum(phase-weighted occurrence offsets) + q_(t,l),

and macro depth equal to the number of occurrence edges. Its physical read is
a genuine read of an actual root depth block. For R_s start at s instead.
Endpoint-specific Euler degree balances, weak support connectivity and these
linear depth/position sums give an exact Presburger read-set relation, as in
II and KM. Repeated q may be deduplicated ONLY for footprint existence.
This proof uses no rank or invertibility of A.

## 3. Canonical given-seed frames

Choose one fixed representative macro prefix v_s before s in the rooted
macro limit, using the empty prefix at a. With a supplied finite board B set

    z_s(r)=A^r net(v_s),
    I_s(r)=translate(-z_s(r)) [B XOR Q_(v_s)(r)].

All A^r shifts have finite eventually periodic range. The prefix parity
Q_(v_s)(r) is the finite XOR of shifted Q_t(r), with each shift A^r times its
literal base-prefix displacement. Consequently every I_s is automatic.

At depth zero check EVERY physical read l of beta_s against I_s(0) at q_(s,l),
XOR the parity of earlier reads of beta_s at that same position. This replaces
IJ's one unit-read base check. The turn bit is ell_(s,l).

For every child j and every r>=0 compare

    I_s(r+1) XOR XOR_(i<j) [A^r p_si + Q_(t_i)(r)]

with A^r p_sj+I_(t_j)(r), but ONLY on A^r p_sj+R_(t_j)(r).
These are exact automatic equality tests: split r into its finite power
phases before applying each spatial shift. Base legality plus full-read-set
frames proves sufficiency by induction. Necessity follows because two legal
runs of one finite literal physical word have identical entry colors on its
whole read set. The canonical representative occurrence is an actual prefix
of the fixed rooted limit. This proves (i), including singular A.

## 4. Some finite seed: genuine position cover, not a selector oracle

Apply the signed support-preserving genuine walk-cover lemma to the finite
phase/terminal graph of Section2, separately at each allowed root start phase.
The terminal edges cannot enter a repeated cycle. Every read position is
covered by a genuine linear path scheme; terminal state/read index is fixed
per scheme. The base-length bound uses the finite PHASE graph, not the original
macro graph. Its degree counters retain occurrence-edge depth and terminal
read identity. There is no guessed depth or support bound.

For a scheme occurrence at z, its strictly preceding parity is the XOR of:

1. All earlier sibling blocks at every selected occurrence edge, with terms
   Q_t(r-d,z-V_(d-1)-A^h p_si), where h is that edge's fixed finite phase.
2. All earlier physical reads of its TERMINAL base word, at their literal local
   offsets. At the selected z this is the fixed within-base revisit parity.

Along each scheme cycle, remaining depth and accumulated offset are affine
in exponents and the bounded repeat counter; its phase-specific sibling
positions are fixed. Thus IJ/JF's affine automatic evaluations and bounded
F2 parity projection construct this exact preceding parity. The appended base
read offset is constant, not multiplied by an extra power of A.

Union BOTH required initial colors over all genuine scheme instances. A
conflict already refutes legality. An infinite black union already refutes
finite support. Otherwise complete position coverage forces a unique finite
candidate B_* on the whole visited set, white elsewhere. Run the complete
macro given-seed frames in Section3 on B_*; these still check ALL unselected
occurrences. Acceptance or rejection is definitive. No least-scheme selector
or first-visit color oracle is required. This proves (ii).

## 5. Singular no-go boundary: nilpotent versus rank one

If A is NILPOTENT, say A^nu=0, every read position is a sum of at most
nu elements from finite phase-offset sets, plus one of finitely many terminal
base-read offsets. All depths therefore share ONE FINITE footprint. Nonempty
base words and growing root prefixes contradict finite-domain escape. This
exclusion holds on ANY initial coloring, by copying that finite footprint.
Thus the nilpotent macro subclass really is excluded; no unit-step inference
is needed.

For the remaining singular finite-power case, take a common root/spatial power
with idempotent matrix P of rank one. Only the following distinction applies.
JP's singular unit-state exclusion first confines finite-power rank-one
footprints to an O(r)-long fixed-width strip and forces any recurrent incidence
component to have Perron value at most one. Those geometric/counting steps
still survive for fixed finite macro bases (each read set adds only a bounded
terminal offset; nonempty bases preserve exponential physical length).

But the final unit-step contradiction does NOT survive. After powering the
incidence cycles, a downstream identity macro d obeys P v_d=v_d for an
idempotent singular P. This constrains only its COMPLETE displacement, not its
internal physical movement directions. For example:

- beta=LRRL, incoming E, final E, has net(2,0), fixed by P=diag(1,0). Its four
  physical moves are N,E,S,E and obey axis alternation.
- beta=RL, incoming E, final E, has net(1,-1), fixed by the integral oblique
  projection P=[[1,0],[-1,0]]. Its two moves are S,E. An oblique fixed macro
  displacement therefore does not require an oblique compass unit step.

Both finite base words are realizable on their literal forced finite inputs.
These examples disprove only the attempted MICROSTEP inference, not the full
singular macro no-go or the existence of any growing legal presentation.
Repeating such blocks can need unbounded prepared fuel. No new macro strip
exclusion, renewable builder, noncapturing seed or capture theorem follows.

If a growing finite-power macro limit were accepted, its root endpoint poses
would lie in a finite set while physical prefix lengths diverge. A genuine
finite-seed eventually periodic orbit has nonzero drift and cannot revisit
that set infinitely often. Thus such an accepted model would be a genuine
nonperiodic counterexample. None has been obtained.
