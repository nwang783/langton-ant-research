# Simultaneous four-side record droughts: an exact excursion bound

24 October 2026. Author proof and exact finite/all-parameter controls; independent audit pending. Finite-seed canonical104 attraction remains UNSOLVED.

## 1. Full-field record convention

Let B_0 be the ENTIRE finite initial black field and p_t the head at cut t, before its update. Let R_t be the smallest axis-aligned closed rectangle containing B_0 and every p_s for0<=s<=t. Write its four signed normal maxima as

    M_a(t)=max {a·q:q in B_0 or q=p_s for some s<=t},
    a in {N,E,S,W}.

A strict record event is a cut t>0 at which one M_a increases. A unit lattice move increases at most one maximum, by exactly one. At an ant record, the incoming heading is that normal, and the ENTIRE current half-plane a·q>=a·p_t is WHITE. All initial black cells lie in the previous rectangle, and every R-born cell is a previously read site. Thus these are genuinely pristine events, even on boards with prepared remote ports.

These records differ from ordinary head-only strict records by only finitely many events for a fixed finite seed. In each normal, the omitted events are the finitely many levels between the initial head and the initial seed extent. Some can occur very late, so no uniform transfer time is asserted. The eventual event streams coincide after all omitted events that actually occur.

## 2. Finite geometric theorem, stronger than a closed return

Consider ANY speed-one unit lattice walk with a finite initial rectangle, not necessarily an ant. Fix s<t with endpoint q=p_t lying in R_s. List all strict rectangle-expansion times in(s,t) as

    s=r_0<r_1<...<r_N<r_(N+1)=t.

Let H=max_j(r_(j+1)-r_j). If N=0, H=t-s. Let m<=4 be the number of distinct record normals appearing in this interval. Then

    N <= (H+1)^m-1,
    t-s <= H(H+1)^m <= H(H+1)^4.             (1)

For s=t the conclusion is trivial with H=0. The endpoint t cannot be a new record because q lies in R_s. The start may be a record; it is excluded from the interior event list.

Proof. For each occurring normal a let n_a be its number of records in(s,t), and ell_a its LAST such record. Order the normals by increasing ell_a. At its last record,

    a·p_(ell_a)=M_a(s)+n_a.

Since q lies in R_s, M_a(s)>=a·q. The remaining walk therefore gives

    n_a <= a·(p_(ell_a)-q) <= t-ell_a.

After ell_a, all remaining records belong to normals with later last occurrences. Every gap in this suffix is at most H, so

    t-ell_a <= H*(1+sum_(later b) n_b).       (2)

If S is the sum of counts for an already processed suffix of normals, adjoining the next normal gives S_new<=H+(H+1)S. Starting from0, induction yields S<= (H+1)^m-1. There are N+1 gaps, proving (1).

Only unit speed and monotone integer record levels are used. There is no assumption of nested lifetimes, bounded black mass, bounded active components, a common record direction, or a restricted turn language. In particular, the head may alternate record directions many times. Their LAST occurrences are ordered only for this finite proof; this is not a global stack discipline.

## 3. Global conditional consequence: any-direction record clock suffices

Suppose the finite ant has infinitely many union-record events, and from some such event T onward every pair of consecutive union-record events is separated by at most H updates. Let

    G(H)=H(H+1)^4.

For every s>=T and every later cut t with p_t in R_s, the local endpoint-list gaps in Section2 are at most H. Therefore

    p_t not in R_s whenever t>s+G(H).        (3)

This supplies an explicit no-return-to-old-rectangle time, independent of the rectangle's dimensions, UNDER the global event-gap premise.

Every currently BLACK cell at T lies in R_T by the augmented-hull definition. Hence every such lifetime that is ever consumed dies by T+G(H). After cut T+G(H)+1 the whole future-relevant black set contains only R-born identities born at or after T. For each such lifetime born at b and consumed at d, p_d=p_b belongs to R_b, and (1) gives

    d-b <= G(H).

Unit speed then bounds the whole future-relevant radius by G(H). Exact one-time pruning and finite normalized-state recurrence give an eventual translating periodic future. Its drift is nonzero because union records continue indefinitely. Translation here means periodic future turns and periodically translated head poses, retaining all output archive; it is not equality of the complete finite black boards. This is not canonical104 uniqueness.

Conversely, an eventual translating future of period P and nonzero drift has bounded union-record gaps eventually, at most P: choose a signed axis of positive drift; after overcoming all earlier extrema, p_(r+P)=p_r+d forces another record within P. Therefore bounded eventual gaps between ANY strict rectangle expansions characterize eventual translation for finite ant orbits.

The contrapositive is genuinely simultaneous: a nontranslating finite orbit must have arbitrarily late intervals of arbitrarily large length with NO new record in ANY of the four normals. Separate unbounded waits in different directions are weaker and do not by themselves imply this. No universal bound on these simultaneous droughts is proved here.

## 4. Universal age-to-drought lower bound

For any actual completed R lifetime of age A, let H be its largest local union-record gap, including the birth-to-first and last-to-death gaps. The same physical cell is its birth and death endpoint, so

    A <= H(H+1)^m <= H(H+1)^4.

Thus H must grow if A grows. A rough explicit consequence for H>=1 is H>=(A/16)^(1/5). The exact polynomial inequality is preferable; no optimal exponent is claimed.

The signed20-cell family has a marked age624n-1576, and the signed16-cell moving-module family has marked age624n-1148, for all their retained even n>=20 domains. Accordingly both have unbounded local pristine union-record droughts across the family. Their finite initial masses and respective entire relevant-population caps132/432 do not yield a UNIFORM all-lifetime drought bound. Every member captures; neither family refutes an eventual bound depending on the individual orbit.

These statements use the augmented full-seed hull. They do not incorrectly treat head records inside pre-funded rails as pristine. The finite checker separately retains ordinary head records for comparison.

## 5. Stronger literal countercontrol after all original input has retired

The signed22-cell M-to-T family supplies an exact completed union-record gap with no original BLACK lifetimes remaining. For every integer n>=100:

- All original inputs have been consumed by update27201+104n.
- At cut s=29671+104n, the head is(233+2n,262+2n),N. This is a pristine NORTH record. The complete historical/seed rectangle is

      R_s=[-1,2n+250] x [0,2n+262].

  Its whole future-relevant population is1082, as already independently signed.
- There is NO strict record of any normal in(s,t), where

      t=88368+208n,
      p_t=(-2,372), heading W.

  This is the next union record, and it is a pristine WEST record.
- The exact completed simultaneous drought is

      t-s=58697+104n.

Both the augmented support-hull records and the ordinary head records have this same gap. The start is2470 updates after the final original lifetime's death. The old input driving the subsequent return is self-written, not an unconsumed original port.

The all-n proof retains the complete signed source trajectories. The initial standard/M history has minima(-1,0). The finite T trace reaches relative maxima x=20 and y=33, with the last new north record at relative8470. Every remaining T read, every affine endpoint of its SW flight, and the complete fixed postcollision recovery lie within R_s. The postcollision recovery reads x in[153,240], y in[158,250], and ends at(155,215),E. Its canonical NW future first reaches x=-2 at period77, phase90, after8098 updates, at(-2,372). Every earlier tail read is in R_s for n>=100. These are exact affine endpoint and104-phase calculations, not a sampled linear fit.

This refutes a proposed uniform union-record escape clock based only on initial mass, no remaining original input, fixed time since original retirement, and the current whole relevant population. It does NOT refute the orbit-dependent eventual record-clock criterion in Section3. Each member has a canonical tail and eventually bounded gaps.

## 6. Complete verification and scope

The checker replays nine entire finite histories with all current BLACK cells retained:20-cell n20/80/400,16-cell n20/40/80, and22-cell MT n100/137/500. It verifies921933 physical updates,416187 completed R lifetimes, all four last-normal inequalities, the refined m-normal count and duration bounds, and additional open intervals ending at original input cells in the initial rectangle. Every full terminal field has an exact all-future canonical104 parity certificate.

The full MT drought endpoints are preserved as complete field snapshots. The all-n geometry is separately checked by affine inequalities at n>=100 and exact finite phase rays. The inherited all-n source and lifetime results remain the upstream dependencies; no new all-position theorem or universal simulation claim is made.

The new useful constraint is simultaneous record drought, plus explicit old-rectangle evacuation under a bounded union clock. The unresolved global premise is precisely whether a single finite orbit can sustain arbitrarily late, increasingly long simultaneous droughts. The finite controls show why a seed-mass-only or original-input-retirement argument cannot supply that premise.
