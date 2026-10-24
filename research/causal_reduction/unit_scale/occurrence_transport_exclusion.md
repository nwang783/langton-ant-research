# Controller-free identity/nine unit transport obstruction

23 October 2026, 02:42 UTC. The charge-preserving chronological tree has passed independent
fine-step reconstruction. The charge-free addendum below is separately
submitted for independent replay. This extends the fixed-root heading-controller
result, but does not absorb its separate first-letter two-cycle computation.

## Statement

Let p(n),h(n),c(n) be one actual infinite ant trajectory on any initial
coloring. There is no increasing integer map T with T(0)=0 such that:

- p(T(n))=p(n) and h(T(n))=h(n) for all n;
- every increment T(n+1)-T(n) is1 or9, and at least one increment is9;
- the signed turn charge of each macro interval[T(n),T(n+1)) equals the
  coarse turn sign at n.

No fixed image, controller state, computability, periodicity or finite-support
assumption is made. Occurrence choices are completely independent.

Every length-one macro must be the literal coarse turn. Every nine-step
macro must belong to the six legal charge-preserving unit-transport images
for that turn, rotated to its incoming heading. These palettes are exactly
those in heading_dependent_transport_exclusion.md.

## Normalization at the first insertion

Let N be the first coarse index whose increment is9. All preceding increments
are1, so T(N)=N. Shift the time origin to N and rotate its incoming heading
to north. The coarse and fine suffixes now start at the SAME actual state,
not merely the same physical pose on unrelated boards. Thus the first macro
must start with the coarse root turn. There are four possible nine-step
root images for each of the two initial turn signs.

Generate the common suffix word chronologically. The first expansion makes
its next eight coarse letters known. At every subsequent coarse cursor i,
choose independently from the seven-image palette for its known turn.
The net displacement and final-heading conditions align the next macro
boundary automatically. Every emitted letter is checked against the most
recent prior turn at its cell. Same-turn consecutive reads are impossible
on every initial coloring.

This is an exact finitely branching tree. Identity images never shrink the
known-letter queue, so no missing coarse future is guessed. The only global
information used is literal same-cell chronological alternation.

## Frozen finite certificate

Each root sign has53 accepted macro-boundary nodes and316 terminal conflicting
branches. The latest zero-based conflict is43. At most seven full macro images
complete; the longest accepted boundary is at read39. The2000-read and
1,000,000-node safety caps are not reached. Therefore the entire tree is
exhausted, not merely a bounded search with unexplored leaves.

Artifacts: probe_occurrence_transport.py/.json/.records.json.
Record digest900039e3e38c7afebeb574338ebce95d57f476d9847235e0f55a3b8bcd6791aa.
The script shares the author's palette generator; independent reconstruction
must regenerate that palette rather than count that import as a second check.

## Limits

A positive initial time offset T(0)>0 is not normalized away by the first-
insertion argument. Macros of other lengths, different unit rotations,
changes of boundary heading, non-charge-preserving macros, and general
stationary-memory architectures remain outside this statement. A two-cycle
substitution squares to macros of lengths up to81, so its separate certificate
is still needed. No universal nonexpanding-renormalization theorem follows.

## Charge-free strengthening: every unit transport of length at most nine

The same conclusion holds with the charge hypothesis removed, provided all
increments are at most9. A macro with the same incoming-to-final heading
relation as one coarse quarter turn has odd length. Its moves alternate
axes, and its net displacement is one unit in the final-heading direction.
The number of moves on that axis is odd and on the other axis even, so
its length is1 mod4. Consequently the complete bound<=9 consists exactly
of lengths1,5,9.

There are ten internally legal images per coarse turn:

R: R; RLLLL; LLLLR; RRRRLLLLR; RLRRRRLLL; RLLRRRRLL;
   RLLLLRRRR; LLRRRRLLR; LLLRRRRLR; LLLLRLLLL.
L: L; RRRRL; LRRRR; RRRRLRRRR; RRRLLLLRL; RRLLLLRRL;
   LRRRRLLLL; LRRLLLLRR; LRLLLLRRR; LLLLRRRRL.

The five-step images have charges-3/+3, and the final extra nine-step
right/left images have charges-7/+7. They are included rather than being
silently discarded by the earlier charge-conservation assumption.

With all ten choices available independently at every occurrence, the
complete tree has238 accepted macro-boundary nodes and2,138 terminal
conflicts per root turn. Its latest conflict is again43; maximum accepted
boundary39, coarse depth7. No cap is hit. The author's frozen generator
and output are probe_occurrence_short_transport.py/.json/.records.json,
with record digesta3a89812be848066b9f71118b37160c21eb80f18e1bfbf5ccd825e6214827089.
Independent direct fine-step reconstruction is signed: the separate checker
audits/check_occurrence_short_transport_independent.py uses no image palette
or controller sharing and reproduces 238 accepted macro nodes, 19,806 fine-
search nodes per root, maximum coarse index7 and last complete boundary39.

This is a controller-free bounded-delay obstruction. It does not exclude
an embedding with a macro of length13 or more, or an initially offset
embedding. No longer-image sweep is proposed as the next step.
