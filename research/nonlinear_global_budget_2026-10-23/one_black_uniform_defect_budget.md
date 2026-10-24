# An explicit distance-uniform one-black defect budget

23 October 2026. New COUNT consequence of the retained all-position one-black
capture theorem, submitted for independent review. This is not a new capture
proof, an optimal bound, or a bound for mass two or above.

## Statement

For every finite state of black mass at most one, with arbitrary placement
of that cell and arbitrary pose, the number of future actual adjacent-bad-ten
events K is at most

    B(1) <= 106268.

True inverse histories are permitted at the initial cut. The supremum of
permanent capture TIMES is nevertheless infinite. Flight length is never
charged as defect count in this argument.

## Retained theorem and exact finite data

Dependency: ../sources/kehao95-core/one_black/PROOF.md and its complete
OneBlack Lean assembly. This note uses its all-position geometric reduction,
actual/pristine same-read-trace guards, and exceptional archive-return theorem;
it does not infer a tail from a finite block match or re-run that proof.

The retained finite witness lists have these exact maxima:

- PrefixData.prefixTimes: 1376 entries, maximum 106258.
- EntryData.actualActiveTimes: 27 entries, maximum 15209.
- EntryData.actualLaneTimes: 179 entries, maximum 62345.
- EntryData.pristineLaneTimes: 152 entries, maximum 64978.

The blank flight starts after 9977 updates. PhaseChecks.postHitTime=7994.
The stable pristine replay for any lane is one entry of pristineLaneTimes,
so its length is at most 64978. These are exact supplied finite tables, not
sampled maxima over a growing coordinate region. The companion extraction
script reads and hashes them, checks the counts/maxima, and derives every
numerical upper bound below.

## Counting lemma, with joins and true history retained

If an actual turn stream is partitioned into arbitrary finite pieces of total
length L and s pieces each of which is a finite or infinite factor of the
bi-infinite cyclic standard turn word, then

    future K <= L + 10s.

Every arbitrary-piece read contributes at most one K. Inside a standard
piece, after its first ten reads every ending eleven-window is fully standard,
so both ending ten-factors are valid and K=0. At most ten reads of that piece
remain chargeable. This deliberately conservative count includes all joins,
short standard pieces, and arbitrary true inverse history before time zero.
No suffix is reset. Spatial quarter rotations preserve the standard turn word.

## Exhaustive retained decomposition

Translation/rotation normalize the initial ant to (0,0,N).

1. If the lone cell is read in the first 9977 blank updates, it belongs to the
   complete 1376-case prefix table. The actual word is one arbitrary prefix
   of length <=106258, followed by genuine standard forever. Thus

       K <= 106258+10 = 106268.

2. Otherwise the path agrees with blank through time 9977. An inert cell
   never affects the highway; K<=9977+10. The active-support finite cases
   have an arbitrary post-entry part <=15209 then standard, giving

       K <= 9977+15209+10 = 25196.

3. A future first-contact cell lies on one of the complete 22 affine frontier
   channels. Every channel's actual shallow band has the supplied direct
   witness time <=62345, followed by standard. Thus

       K <= 9977+62345+10 = 72332.

4. In any of the 21 deep ordinary channels, the actual infinite turn stream
   after entry equals the pristine stream by the retained full-history
   footprint/corridor guard. That stream is some number of clean standard
   periods, ONE translated stable pristine replay, then standard forever.
   The stable replay length is <=64978. Counting the blank prefix and anchor
   as arbitrary and the two standard pieces separately gives

       K <= 9977+64978+20 = 74975.

5. The one deep exceptional channel has the exact decomposition

       blank prefix;
       clean incoming standard periods;
       one translated stable pristine replay;
       clean spatially opposite standard periods plus a standard prefix;
       the fixed 7994-read historical-contact recovery;
       clean outgoing standard forever.

   Increasing depth adds one incoming standard period and one opposite-drift
   standard period, not extra arbitrary recovery work. The four-period lag,
   ten-period return, and final 89 phases are contained in the same clean
   opposite-drift standard piece. Phase.reverse_block_exact and the accepted
   stable terminal orientation establish a rotated GENUINE forward standard
   word there. It is not the time-reversed inverse104 word.

   There are at most three standard pieces, so

       K <= 9977+64978+7994+30 = 82979.

The maximum of these five bounds is 106268. Mass zero is covered by the blank
bound. A quarter rotation or translation changes neither the turn stream nor
its K count, completing every initial pose and singleton position.

## What this establishes and does not establish

This proves a first nontrivial distance-uniform COUNT base case for a possible
mass-sensitive global induction. It does not strengthen the retained one-black
capture theorem itself, does not bound distance-dependent capture time, and
does not justify iterating the singleton scattering rule through arbitrary old
archives. The exceptional reverse flight explains why that latter induction
requires more than locally stable forward scattering.
