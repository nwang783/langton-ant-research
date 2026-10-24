# Exact exceptional return map: twenty-four persistent archive strings

23 October 2026. New analytic map and exact finite-mask calculation, submitted
for independent review. This is NOT unbounded fixed-mass defect count,
noncapture, or an independently renewed finite component.

## 1. Main conclusion

The exceptional reverse-singleton scattering on ANY fixed certified capturing
finite base has an exact constant-pose return-section normal form

    Y_n = (A_X XOR shift(K d, sum_{i=0}^{n-1} shift(i d,L)), r_K,h_R),
    elapsed = 52262 + 104K + 208n,                       (1)

after its chosen incoming standard boundary. Here n>=0, K is a computable
base-dependent nonnegative integer, A_X is one FIXED complete finite field,
and r_K,h_R are fixed. The initially added obstacle lies at canonical
phase72 depth11+K+n. The return section is chosen before ANY possible old-base
collision; every old black cell is retained in A_X.

The universal finite return layer L is explicitly reconstructed below.
It is not a finite translation coboundary. In fact it has24 nonzero full-drift
orbit parities and an exact decomposition

    L = P XOR C XOR(C+d),       |P|=24, |C|=2189,         (2)

with one P cell in each of24 DISTINCT full-drift cell orbits. Therefore

    sum_{i=0}^{n-1}(L+i d)
      = sum_{i=0}^{n-1}(P+i d) XOR C XOR(C+n d).         (3)

The middle term is exactly24 disjoint black strings of length n. In
particular the COMPLETE return-state black mass is

    |Y_n.black| = |A_X| + 24n                           (4)

for this PHYSICAL return map. Indeed each extra n adds one incoming and
one opposite-drift genuine104 period; each has curvature/black-mass gain12,
while the stable replay is fixed. Equation(3) additionally gives the purely
set-theoretic bound |A XOR train_n(L)|>=24n-|A|-4378 for any finite A.

A reduction replacing this return by an n-independent finite base or only
bounded-mass moving end caps is impossible if the COMPLETE board is to be
preserved. A compressed train representation is possible and is exactly
(3); it is not a decreasing original-fuel invariant.

## 2. Imported canonical scattering component

Normalize the incoming standard boundary to the retained pristine base S:
position(-15,10), heading W, standard drift d=(-2,-2),13 active black cells.
Let H be its genuine forward104 turn word. Let W denote its complete wake:

    F^104(S) = shift(d,S) XOR W.

The retained all-depth pristine phase72 theorem has stable depth11 and
stable literal replay length a=52262. At obstacle depth11 its complete
terminal state is R=(B_R,r,h_R), with a genuine opposite-drift standard
continuation, e=-d=(2,2). Define its COMPLETE reverse wake V by

    F^104(R) = shift(-d,R) XOR V.

These are actual forward dynamics in both cases. V includes every passive
black cell of B_R in the whole-board shift difference, not just its small
active104-read core. Its large support must not be silently discarded.

The retained pristine induction and wake guards imply that for depth11+b,
all b incoming clean periods, the translated stable replay, and any desired
number of subsequent clean opposite-drift periods are exact; accumulated
incoming wake copies are fully inert along that entire continuation.

## 3. Arbitrary capturing base and a safe return cross-section

At its supplied standard boundary, write the arbitrary complete finite base
as S XOR D_X, with the same head and heading. The discrepancy D_X is finite
and misses the ENTIRE future incoming H read set, since the two actual
standard traces agree forever and first-difference induction preserves their
board discrepancy. All original debris remains in D_X.

Choose K large enough that D_X misses:

- every translated stable-replay read A+(K+b)d, b>=0;
- every opposite-period read Q+(K+b)d, b>=0,

where A is the fixed complete stable-replay read set and Q is the complete
one-period read set from R. Also enlarge K until every proposed added obstacle
misses X's finite prelude and the true initial inverse ten-read history. This
makes initial insertion before that prelude identical to insertion at the
standard boundary, without changing earlier K counts. Such K exists and is computable: for every pair
of finite offsets solve a single nonzero-drift integer ray equation and put
K beyond all its nonnegative solutions. Incoming clean flights already miss
D_X at every depth. Thus no old-base collision occurs through the return
section constructed below, for EVERY n>=0.

Use obstacle depth11+K+n. After K+n incoming periods and the fixed stable
replay, the complete actual board is

    D_X XOR shift((K+n)d,B_R)
      XOR sum_{i=0}^{K+n-1}(W+i d).                    (5)

The head is r+(K+n)d. Follow exactly n opposite standard periods. Their
whole-board wake formula and the retained incoming-wake guards give

    D_X XOR shift(Kd,B_R)
      XOR sum_{i=0}^{K+n-1}(W+i d)
      XOR sum_{j=K+1}^{K+n}(V+j d).                   (6)

The head is now r_K=r+Kd, heading h_R, independent of n. No color requirement
was inferred only from an XOR formula: the pristine induction supplies the
legal continuous cursor, and the chosen K keeps D_X unread throughout it.
Split the W sum at K. Set

    A_X = D_X XOR shift(Kd,B_R) XOR sum_{i=0}^{K-1}(W+i d),
    L = W XOR(V+d).

Equation(6) is precisely(1). The elapsed length is
104(K+n)+52262+104n. Including X's finite prelude simply adds its fixed T.
All true inverse histories are those of this ONE actual trajectory; none
is reset at the section. For n>=1 the final104 reads are genuine opposite-
drift standard, so even the preceding-ten suffix at the cut is fixed.

## 4. Orbit-parity obstruction and canonical string form

For any finite mask M, define its full-drift orbit profile pi_d(M) as the
parity of |M intersection O| for each cell orbit O=q+Z d. It is finitely
supported. Every finite coboundary C XOR(C+d) has zero profile. Conversely,
if a finite mask has zero profile on every orbit, its one-dimensional prefix
parities along each orbit define a finite C with M=C XOR(C+d). This is just
the finite Laurent-polynomial divisibility test by1+z over GF(2), not an
assumption of physical realizability.

More generally, choose one representative P point on each odd-profile orbit.
Then M XOR P has zero profile and admits the finite-coboundary decomposition.
Summing n translates telescopes exactly to(3). Distinct P points lie on
DISTINCT full-drift orbits, so the24 strings cannot intersect one another.
Their total mass is24n; the two finite C caps and any fixed finite field change
it by a bounded amount, giving the purely set-theoretic estimate after(4).
The exact physical equality(4) is independently stronger and follows from the
actual turn curvature. All finite-gauge coboundary changes preserve the number24.

## 5. Exact exceptional masks and profile

The companion compute_exceptional_layer.py/json reconstructs the blank entry,
its exact13-cell active base, the phase72 stable replay, and one full reverse
period. It retains the COMPLETE B_R field when forming V. The exact masks
satisfy

    |W|=12, |V|=2436, |L|=2438.

The source's PhaseChecks.layer is shift(4d,L); the script uses that gauge in
its explicit coordinate lists. Translation by4d changes neither orbit profile,
cap mass, nor(3). Translate P,C back by4d for the raw L in(1).

The24 odd orbit classes, recorded as(t=x-y, a=x modulo2), are:

    incoming band:
    (-28,0),(-28,1),(-27,0),(-26,1),(-25,1),(-24,0),
    (-23,1),(-22,1),(-20,0),(-19,0),(-18,0),(-18,1);

    reverse band:
    (42,0),(42,1),(43,1),(44,1),(46,0),(47,0),
    (48,1),(49,0),(50,0),(51,1),(52,0),(52,1).

The bands are disjoint. The incoming and reversing fronts have not erased
each other's persistent wakes: they leave two separate12-class systems.
The large remaining finite portion of L is an exact coboundary with a2189-cell
cap C. Direct finite-mask identities verify(2); no extrapolation from mass
slopes is used. Several finite sums are additional error controls only.

## 6. Consequence and exact open problem

There IS an exact finite DESCRIPTION of the return map: fixed finite base,
fixed pose,24 growing strings, and a bounded remote cap. There is NOT an exact
bounded-size finite BOARD return map of the naive kind, and fresh-bit
consumption alone does not remove this newly manufactured archive.

This does not prove that the24 strings cause many K events: standard flights
themselves build long black strings with zero bulk K. Indeed, after increasing
K if necessary to protect the true initial inverse ten-read history, the
number of K events up to this return section is EXACTLY independent of n for
all n>=1. Both variable flights are then at least104 reads long; their bulk
K is zero and every remaining history join has the same fixed literal
context. The archive growth24n therefore creates no prefix defect-growth
claim. The subsequent scattering is the genuinely unknown part. It also does not prove
that a single fixed original seed undergoes arbitrarily many returns. Each n
above is a different initial obstacle location, and what happens AFTER this
safe return section is not classified for arbitrary X. A successful nonlinear
budget must bound the actual scattering of the fixed old base against this
24-string family, or prove another rank that explicitly retains those strings.
