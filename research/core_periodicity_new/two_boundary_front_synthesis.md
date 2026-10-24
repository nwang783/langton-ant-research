# Non-axis inverse synthesis with prescribed incoming and outgoing profiles

Status: approved by the independent auditor on 2026-10-22 at 22:19 UTC, including the signed stable-class moments, finite-cap construction, 856 energy, and arbitrary-background midpoint extension. The original white-input source is ../sources/kehao95-core/wake_synthesis/PROOF.md, Sections2,8,9,10.

## Inputs and exact intended scope

Fix a nonzero non-axis full drift d with even checker parity, an initial pose/heading, and two finite sets I,O of full d-classes. These describe black incoming and outgoing drift-periodic profiles, respectively. This is an INFINITE-background problem: the entry board is the bilateral incoming profile I with an arbitrary finite cap modification. A repeated finite word must see I far ahead, and leave O on every completed physical class in its advancing region. Unread backward background need not change.

Define the signed profile change

    delta_v = 1_O(v)-1_I(v),

and the odd-used set A=I symmetric_difference O. We seek an exact infinite repetition, not a finite repeated prefix.

## Exact stable-color criterion

For any candidate word, order its visits in each full drift class by decreasing longitudinal coefficient, then phase index, as in the cited source. The list must alternate, beginning R if v is not in I and L if v is in I. Its length parity must equal1_A(v). In particular any changed profile class must actually be visited.

This is necessary and sufficient for a finite-cap realization on I. The finite initial boundary deletes a prefix of each stable visit list. Flip the incoming color at the finitely many boundary sites where the deleted prefix length is odd. All remaining suffixes then begin with their required color and alternate. Outside those finitely many boundary sites, the initial board agrees with I. Conversely far enough forward every phase is present and fixes the incoming color and alternating sequence.

The signed R-minus-L contribution of class v is exactly delta_v. Thus the raw signed growth g=sum delta_v is divisible by4, though it need not be positive.

## Period cutoff from reciprocal moments

Rotate coordinates to d=(a_0,-b_0), a_0,b_0>0, and transform the pose and sector accordingly. Put k=gcd(a_0,b_0), eta=(b_0/k,a_0/k), choose r=4, and let

    a=r^eta_x, b=r^eta_y,
    kappa=1-2/(a+1)-2/(b+1)>0.

The source's literal one-sided clock identities are independent of initial support. Over a full period the head correction cancels, because eta dot d=0 and the heading returns. Their increments are

    A_+ = -sigma sum_v chi(v) delta_v r^(eta dot v),
    A_- = -sigma sum_v chi(v) delta_v r^(-eta dot v).

The sums are finite and independent of representatives. Copying a finite period's read set justifies the same calculation even though the surrounding incoming board is infinite. Therefore

    kappa sum_i r^(eta dot q_i) <= A_+,
    kappa sum_i r^(-eta dot q_i) <= A_-.

Both A_+,A_- must be strictly positive, and

    P^2 <= A_+ A_- / kappa^2.

This supplies a computable integer upper bound on every possible period. Enumerate all words up to it, retaining the prescribed displacement/heading and the exact stable-color and output tests. A passing word yields a finite cap by the preceding construction; exhaustion certifies nonexistence. Optional resource limits must return INCONCLUSIVE, not 

Thus fixed incoming AND outgoing profiles admit total all-period inverse synthesis for non-axis full drift. The result does not decide whether an arbitrary cap eventually settles, and does not bound the possible outgoing profile, drift, or period if those are not prescribed.

## Sharper diagonal budget

For a diagonal drift, rotate to d=(m,-m), m>0, and put t=x+y. The source's integer clock gives, for every integer center c,

    P <= -sigma sum_v chi(v) delta_v (3^|t(v)-c|-1).

The same signed delta can also be used in the source's crossing-flow recurrence, since the local balance counts depend on signed R-minus-L counts, not on white input. These are optional stronger cutoffs; the reciprocal bound already proves decidability.

## No same-sector pure eraser of a standard wake

Use the canonical settled standard wake of core_periodicity_new: its twelve (u=x-y,e=x mod2) classes are

    (-3,0),(-3,1),(-2,1),(-1,0),(0,0),(1,1),
    (2,0),(3,0),(5,1),(6,1),(7,0),(7,1).

The canonical standard producer has sector sigma=-1. Rotate counterclockwise so the transverse clock coordinate is u and the transformed sector is+1. At center c=2, the wake's clock energy per basic (2,2) translation is

    -sum_(u,e in T) (-1)^u (3^|u-2|-1) = 856 > 0.

A proposed same-sector periodic consumer, with compatible full drift plus or minus k(2,2), k>=1, and completely white outgoing profile has delta=-1_T. Its diagonal budget is therefore -856k, which cannot be at least the positive period P. Such a pure eraser is impossible for EVERY turn word and every period, with arbitrary finite moving caps.

The actual time-reversed standard front flips the sector and is not excluded. A consumer that emits a DIFFERENT nonempty wake is also not excluded. This theorem is stronger in word scope than testing only the reverse-complement104 word, but weaker in output scope than our earlier finite-factor input-guard results.

## Zero-output-change fronts, including axis drift

A complementary all-axis observation follows from the audited midpoint separator inequality, extended to arbitrary backgrounds by finite-read-set copying:

    |B_s symmetric_difference B_t|
      >= 2 ||p_t-d(h_t)/2-p_s+d(h_s)/2||_infinity.

For a periodic-input/output front, after n periods the complete XOR has size n|A|+O(1), while the midpoint displacement is nd. Therefore

    |A| >= 2 ||d||_infinity.

This remains true with zero or negative signed mass growth. In particular I=O is impossible for ANY nonzero drift, including axis drift: a transparent moving finite cap cannot advance indefinitely on preinstalled infinite hardware while restoring that hardware exactly behind it. This density statement does not by itself give a period cutoff for arbitrary nonzero axis profiles.
