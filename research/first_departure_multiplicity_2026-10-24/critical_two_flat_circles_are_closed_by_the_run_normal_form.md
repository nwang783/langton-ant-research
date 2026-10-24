# Critical two-flat circles are closed by the run normal form

24 October 2026. Complete WHITE cap-four front, actual FULL P,d. Gamma
is a b-circle at GLOBAL maximum M=c_right+1 with no one-use edge.
Author dependent result pending review. This is an exact two-flat
composition exclusion, not a general one-use or complete-front theorem.

Dependencies: signed local pair gate94b498ab/reportea0bd913; high-run
normal form20cb0cb1/reportcbb8b590 and zero-gap clarificatione2010748;
local Y-reader gate17e8d2fd/reportdadd4a43; the earlier mixed first/second
lane and flat-island results. No imposed clock, support or rail cutoff.

## 1. A Y must exist, and cannot be isolated among high RIGHT contacts

If a flow-two crossing exists, the signed local island theorem c9574fb8
makes its immediate predecessor Y. If none exists, the actual selected
second lane has only X positive L1->L3 jumps and Y negative jumps.
Telescoping one negative b lap gives

    -P = ell + sum_X age13 - sum_Y age13.

Thus Y exists in either case. This argument permits arbitrarily long
physical ages, not residues modulo P.

Suppose a Y has no other flat as either of its nearest preceding/following
RIGHT contacts. The RIGHT neighbors therefore are a high sink and a high
source. It cannot be in RR, since a flat RR partner must also be flat.
The intervening flow-two LEFT run cannot contain O/U: a root at the
incoming high end violates the signed flat-predecessor theorem, and a
root at the outgoing high end violates the signed global-M local island.
It cannot be VV either. The complete LL ordinal/count relation has
flat-flat or high-high ends, never one flat and one high. Hence each side
has exactly one V. The local physical gate is exactly

    high sink, V, Y, V, high source,

excluded by the signed reader theorem17e8d2fd, even allowing arbitrary
multiplicity at its auxiliary readers. Therefore every Y has another
flat as at least one of its nearest RIGHT neighbors. This does not claim
that every flat is Y or that every flat cluster has bounded length.

## 2. Consecutive flats with high outside must be RR

Assume there are exactly TWO flat RIGHT classes and some high macro.
The existence/nonisolation of Y implies that the two flats are nearest
RIGHT neighbors on one side. With exactly two, their other connecting
arc contains every high macro. Both immediate outside neighbors of the
pair are high, since there is no third flat.

At each outside flat/high interface, the same signed O/U and LL
restrictions used above force a single V. The two flats themselves are
separated by zero, one or two LEFT contacts; three would close a physical
square. The exact local pair gate94b498ab retains all O/U/V middle
histories and all high3/high4 outer types. It excludes the one-LEFT and
two-LEFT cases. Thus the pair is RR.

This uses actual physical stencils. No pair of physical providers is
identified merely because its classes agree. The finite local covers are
overapproximations even if some named physical cells are full-drift
translates: a genuine quotient still has to satisfy those complete words.

## 3. Zero turning forbids the remaining RR pair

The complementary high run starts/ends with one V next to the RR flat
pair. By the signed triangular run form it consists either entirely of
RR3/RR4 blocks, or of one initial RLR3 followed by RR3/RR4 blocks. Every
internal separator is VV. Write q for its number of RR blocks and
 epsilon=0 or1 for the presence of its initial RLR3. The run INCLUDING
its two endpoint V contacts, but excluding the two flat RIGHTs, has

    RIGHT count = 2q + 2epsilon;
    LEFT count  = 2q + 3epsilon;
    signed turning count RIGHT-LEFT = -epsilon.

The RR flat pair contributes +2. Hence the complete circle has signed
turning count 2-epsilon, which is 1 or2, not zero. The embedded essential
b-circle must have zero signed turning. Contradiction. There is no bound
on q, P, rail age or drift magnitude in this argument.

If there are no high macros, the two flats are the only two RIGHTs;
zero turning gives two LEFTs, all edges flow two. Its cyclic turn word is
RRLL or RLRL. The former is excluded by signed actual-event separator
9276befb; the latter by the signed global-M constant-two staircase
obstruction e597889e. Essential short quotients are not assumed absent.

## 4. Exact conclusion and open mechanism

At least THREE flat RIGHT classes are necessary under these hypotheses.
The structural content is that a high run cannot internally relaunch an
RLR3 crossing: a new launch needs another flat interface. This two-flat
corollary does not bound the number of flat interfaces or show that their
exterior matchings are impossible. Three/many-flat launches, odd output,
older stock, within-band transfers and K>=2 remain open. No original-
fuel resource or attained positive front is inferred.
