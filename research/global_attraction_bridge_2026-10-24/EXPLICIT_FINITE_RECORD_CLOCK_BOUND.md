# An explicit finite record-clock bound, with no compact-cover search

24 October 2026. Author proof; independent audit pending. This strengthens the signed effective existence theorem09b1ee22. It does not classify the translating word as canonical104 and does not prove a forcing window occurs on every finite orbit.

## 1. Explicit theorem

For each integer H>=1, define

    G = H(H+1)^4,
    S = 4*2^G,
    F_star(H) = G+1+2S^2+(H+3)S.              (1)

Take any complete finite black field at a pristine augmented-hull record cut. The augmented hull includes the ENTIRE original seed and all earlier head positions. Suppose every H-step block through the next F_star(H) updates contains a new strict hull-expansion record in some direction. Then an exact translating periodic turn/pose future has already begun within that window.

A sufficient tail begins at a cut s<=G+1+S and has a period P<=S. All old archive is retained. The drift is nonzero, but the word need not be assumed or proved canonical104.

The formula is deliberately loose and enormous. It gives an explicit computable forcing window, rather than merely a computable search whose termination is proved by compactness. No F_star-scale simulation is attempted. The earlier compact proof remains a separate, signed argument and is not edited or replaced.

## 2. A finite truncated-memory state is exact during the clock window

Use relative time0 at the starting record and let R_t be the full augmented rectangle. The signed last-normal theorem gives

    p_d in R_b  implies  d-b<=G,

whenever the interval lies within the H-clock window. This applies to initial BLACK input at b=0 and to a returning R lifetime at its birth cut b.

At each update t>=G+1 in the window, the next read is determined by just:

    current heading, and the last G turns.

To see this, reconstruct the last G head positions relative to p_t by reversing those turns and unit moves. If the current cell was read during that history, its most recent turn determines its current color: the cell is BLACK exactly when that turn was R. If there was no such read, the cell must be WHITE. Otherwise its BLACK identity is either original, which would be a forbidden visit to R_0 after G, or R-born at b<t-G, which would be a forbidden return of age>G.

An older most recent L causes no problem: it left WHITE and the truncated rule also returns WHITE. The only possible failure of the truncated rule on an arbitrary history is a WHITE prediction against an actual old BLACK input. Such a failure is excluded inside the stated clock window.

Given the heading and G turns, relative head coincidences are exactly recoverable. The resulting truncated-state update is deterministic. It does NOT assert that the whole physical black board is a finite state, nor delete older output.

There are at most S=4*2^G truncated states. Among the S+1 cuts

    G+1,...,G+1+S

two states repeat. Write the earlier cut as s and their gap as P, so

    1<=P<=S,
    s+P<=G+1+S.

The same deterministic transition rule applies throughout the remainder of the observed clock window. Hence the actual turn word from s repeats a length-P word w for as long as observed. The repeated state includes the heading, so w restores the heading. Its head displacement is some integer vector d, and observed copies have read points Q_i+kd,0<=i<P.

## 3. A genuine later record certifies an outward direction

Set

    K=2P+H+2.

Formula(1) leaves at least K complete copies observable after s, since

    s+PK <= G+1+S+S(2S+H+2) = F_star(H).

The clock supplies an actual union record r in(s+P,s+P+H]. This lies within those observed copies. Let a be its normal. The previous same-phase point r-P is already part of the observed repeated word, so

    a·d = a·p_r-a·p_(r-P) > 0.

Therefore d is nonzero and a·d>=1. In particular, an apparent zero-drift loop cannot survive the next H-clock block.

Let B_s be the COMPLETE physical black field at s, and M_a(s) the corresponding old hull maximum. It satisfies

    a·q <= M_a(s) <= a·p_s+P+H     for every q in B_s,

because r is a new record and unit speed bounds p_r-p_s. Every phase point obeys a·Q_i>=a·p_s-P. Thus any hit of B_s by a future phase ray has

    Q_i+kd in B_s  implies  k<=2P+H.          (2)

This is the essential full-field transport step. It uses every initial or written black cell via the actual old hull, not only a cropped recent kernel. A remote extra original BLACK could enlarge that hull and remove the claimed record r even while preserving a long turn prefix.

## 4. The observed copies certify all future read parities

For each phase i, the read at Q_i+kd has color determined by:

- its initial membership in the COMPLETE B_s;
- earlier same-period phases;
- earlier-period phase coincidences Q_j-Q_i=md.

Every nonnegative initial-field hit index is bounded by(2). Each positive self-overlap threshold m is at most P: choose a nonzero integer coordinate of d, and use the diameter bound |Q_j-Q_i|_infinity<=P. An earlier phase with m=0 is already active at period0.

The parity at a fixed phase is constant between its finite thresholds and initial-hit changes. It is enough to test period0, every self-overlap threshold, every initial-hit index and its successor. All these indices are at most

    2P+H+1 = K-1.

The actual observed K copies test every one of them. They therefore certify the repeated word for ALL future periods, by the exact phase-ray parity induction. No unobserved old BLACK hit or delayed self-overlap can remain beyond the tested range.

Consequently the complete original physical board has the translating future w forever from s. This proves(1) without retrospective pruning, an unknown-future oracle, a general controller classification, or a compact-cover enumeration.

## 5. Consequences and scope

The earlier nontranslation drought consequence can now use the explicit function F_star. For every H, EVERY interval of length F_star(H)+H on a nontranslating finite orbit contains an H-step subinterval with no pristine union record.

This does not prove that a finite seed ever maintains one of these fast clocks long enough. It also does not rule out a noncanonical translating controller. Both the occurrence problem and unrestricted canonical104 uniqueness remain separate.

The finite-input/global-whiteness promise matters. The augmented initial hull is supplied by the ENTIRE initial seed. A merely observed finite word with undisclosed remote BLACK input does not establish the required record clock. The retained pre-funded and exterior-completion controls are therefore not bypassed.

## 6. Bounded independent-check interfaces

The checker does not construct S or F_star for large H, and never runs an F_star-length experiment. It evaluates the formula only at H=1 and2 as arithmetic regressions.

Four tiny complete initial fields are replayed for4800 total updates to test the truncated predictor at memory lengths1,4,16,64. Every discrepancy is exactly an actual BLACK input older than the retained memory; no false BLACK prediction occurs.

Three complete MT archive states are taken at their signed first WEST record, n100/137/500. After208 literal preparation reads, the last208-turn-plus-heading state repeats after104 reads. For each complete field, the checker observes314 full104-turn blocks, verifies the actual union-record clock H=104, identifies its positive record normal, computes ALL complete-field phase-ray hits and self-overlap thresholds, and independently checks the resulting infinite read parity. It retains every old cell and hashes both complete fields. These controls use98592 physical reads in total.

The memory208 and period104 in these regressions are named interfaces, not substitutes for the universal G and S. The general bound is proved analytically in Sections2–4. No arbitrary-period exhaustion, practical universal runtime or global capture claim is inferred from the controls.
