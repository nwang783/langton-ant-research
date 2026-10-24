# Exact timestamp, ordinal and voltage identities at an even spatial cut

24 October 2026. Author derivation for independent review. These are exact
necessary identities and bounds, not a completed monotonicity exclusion.

## Setting and definitions

Use a complete WHITE full drift (3,1) front and a prefix of COMPLETE histories
T<=t, where t is even and strictly below the actual read maximum. Below the
actual read minimum there are no omitted read classes. Its event graph has no
proper closed component; every named event lies on an open chain.

At the cut, let w,n,s,u count the physical W_t,N_(t-1),S_(t+1),S_(t+3) ports.
The first two depart the prefix; the last two enter it. Thus C=w+n=s+u is the
number of open chains. Let N be the total number of named read events. Let K
be the sum of the full-drift voltages of all INTERNAL directed event edges;
for this coordinate system each internal N edge contributes +1, each S edge
-1, and horizontal edges zero. Define Z=C-K.

For each crossing port use its source read clock at the canonical representative
(-T,0), not its clock at an arbitrarily shifted physical copy. Let W,Nc,S,U be
the sums of these clocks over the four ports. Nc is a timestamp sum, distinct
from the total read count N. Incoming source clocks are unknown future-cell
variables, but their chronological port ordinals are fixed by the named prefix.

## Exact weighted current identity

The complete identity is

                 W + Nc - S - U = N + P Z,

where P is the unknown full period. It keeps every voltage correction.

Proof: each open chain with ell named events and internal voltage k satisfies
T_last - T_first = ell-1-kP. Every incoming boundary edge is an S move from a
future odd class into the prefix, so at representatives its clocks obey
T_first = T_outside_source + 1 + P. Sum over all C chains. The left side becomes
the four source-port timestamp sums, while the right side is
sum ell + P(C-sum k) = N + P(C-K). No chronological event or unread field is
discarded. The equality uses source clocks on both incoming and outgoing edges;
changing to arrival clocks without correcting the constants would be wrong.

At the final whole-footprint closure the open-chain formulation is replaced by
the single actual event cycle: C=0, K=1, and the corresponding sum is zero,
giving P=N as required. The proper-prefix identity must not itself be used to
assert that its open interface already closes.

## Ordinal inequalities

For any one of the four source ports with q ordered occurrences, let f and l
be its first and last source read clocks. Consecutive port occurrences are
reads of the SAME physical source class in chronological order. Their gaps are
positive multiples of four, so

q*f + 2q(q-1) <= sum of port clocks <= q*l - 2q(q-1).

When actual source ranks r_0<...<r_(q-1) are known, replace 2q(q-1) in the
lower bound by 4*sum(r_j-r_0), and in the upper bound by
4*sum(r_(q-1)-r_j). Empty ports contribute zero, with no first/last variable.

Consequently, putting Q=2*sum q(q-1) over all four ports,

w*f_W+n*f_N-s*l_S-u*l_U+Q <= N+PZ
<= w*l_W+n*l_N-s*f_S-u*f_U-Q.

These bounds directly connect accumulated reads, boundary ordinal spans and
full-drift voltage. They are invariant under translating every clock by a
common constant because w+n=s+u. Known complete source ranks give the sharper
variants above.

## What is and is not obtained

These formulas do not currently contradict the two fixed end interfaces of
the middle-short family. The unknown source ranks and canonical clock offsets
can span several full periods; assuming every canonical clock lies in [0,P)
would incorrectly erase physical-history lifts. Also Z is an integer voltage
counter, not proved bounded by 0 or1 on proper prefixes.

The identity gives a sound weighted/counter transfer invariant, but no
sign-definite inequality across every even gap has yet been derived from it.
Its growth can be absorbed in clock spans, integer voltage and period growth.
The signed arbitrary-k three-cell OPEN family d3db81f8 demonstrates a local
relaxation with unbounded traffic, not a physically realized finite factor.
It therefore cannot refute stronger inequalities using complete outside-field
realizability. No such physical counterfamily is claimed here.

A promising exact next target is to bound the centered ordinal spans or Z for
interfaces actually REACHABLE from the signed lower prefix, while preserving
all chain pairings and the two possible upper odd geometries. Until such a
bound is proved, finite residue cycling remains insufficient.
