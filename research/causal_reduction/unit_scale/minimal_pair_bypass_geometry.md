# Minimal two-turn endpoint bypass

Status: author derivation and literal controls; independent review pending.
This changes the geometric architecture rather than increasing a unit-image
length bound. Only the pose after TWO coarse turns is retained; their
intermediate coarse pose must never occur in the fine word.

## Exact minimality

Normalize the incoming heading to north and the first coarse move to east
(the opposite case follows by reflection, interchanging R/L). The two-turn
endpoint has both coordinates odd, so a quarter-turn path to it has length
2 modulo 4. Its final heading is the second coarse outgoing direction.

At length two the intermediate pose is unavoidable. At length six, if the
first horizontal move is east the intermediate pose is immediate. Otherwise
it is west, and the remaining two horizontal moves must be east. The final
vertical move is fixed by the target heading; therefore the fifth move
arrives at (1,0) facing east, again the intermediate pose.

At length ten, avoiding the first and penultimate possible intermediate
pose forces the first and last horizontal moves west. Net horizontal
displacement one then forces the horizontal sequence W,E,E,E,W. The only
remaining possible intermediate-pose hit is after the middle horizontal
move. To avoid it, the first two vertical moves must agree. Net vertical
displacement and the final heading determine the remaining vertical moves.
There are exactly two geometric words. Direct tracing shows their ten read
cells are distinct, hence they are internally legal on the uniquely required
colors at those cells.

For coarse pairs RR,RL,LR,LL respectively the two words are:

- RR: LRRLRRLRRL, LLLRLLRLLL
- RL: LRRLRRLRRR, LLLRLLRLLR
- LR: RRRLRRLRRL, RLLRLLRLLL
- LL: RRRLRRLRRR, RLLRLLRLLR

Every word reads the old intermediate CELL facing the opposite heading, but
never the old intermediate POSE. Some words read the final endpoint early;
this must remain in the full chronology and cannot be discarded as a seam.
All input, output, read-support, complete-XOR and pose data are retained in
minimal_pair_bypass_geometry.json. An untouched external board may be
adjoined only outside the listed read support.

## Literal context controls, not a global exclusion

All sixteen nonidentity one/two-bypass periodic repetitions of the RL or LR
staircase fail complete same-cell read alternation. Only the two identity
staircases are legal. This does not exclude other coarse contexts.

A separate complete test replaces exactly one pair in inverse104, in either
of its two pairing alignments. Each of the 208 words has length112 and drift
(-2,-2), and each has a repeated equal turn in a complete physical drift-orbit
history. The unchanged inverse104 is a legal prepared periodic control.
This does NOT exclude simultaneous bypasses, whose intermediate visits may
repair one another's histories. No prepared-rail compatibility or finite-seed
realization follows merely from local endpoint geometry.

Sources: minimal_pair_bypass_geometry.py/json and
check_pair_bypass_scaffold.py/pair_bypass_scaffold.json.

## Simultaneous prepared-periodic context (author certificate)

The isolated-insertion failure motivates retaining ALL mutual support among
the 52 pair choices. For each pairing alignment, allow each coarse pair its
identity or either minimal ten-read bypass, independently, and require at
least one bypass. Initial colors on every drift orbit are FREE and output
colors are unconstrained. This is larger than any standard-rail input model.

For each orbit (x-y,x mod2), sort possible events by
(floor(x/2), coarse-pair index, local index). Selected event bits update the
cell color by XOR; each selected R demands white and each selected L black.
This is exact complete periodic chronology because all blocks share their
coarse endpoint and heading, and all complete words have drift (-2,-2).
The unknown total period length does not affect the lexicographic ordering.

Both CNFs are UNSAT: 2,266 variables and 7,593 clauses each. Retained monotone
RUP proofs have 30 and 26 additions, and an independent generic RUP checker
accepts both with no RAT or deletions. This excludes every nonidentity
STATIONARY assignment in this precise pair palette on ANY prepared periodic
profile. It does not exclude changing choices from one coarse period to the
next, larger endpoint blocks, or other scaffolds.

The exact unchanged inverse104 is a positive model in both alignments.
Fifty fixed-assignment controls, including those two identities and sparse
and dense nonidentity choices, compare the entire event-color recurrence
against direct literal complete orbit histories. All agree.

Source/records: synthesize_pair_bypass_scaffold.py,
pair_bypass_simultaneous/cut{0,1}_free.architecture.json,
cut{0,1}_free.cnf/rup/result.json, controls.json,
and check_pair_bypass_cnf_controls.py.
Semantic independent audit, including the minimality argument, is pending.

## Nonstationary local rigidity (author certificate)

There is no need to impose a periodic choice equality. The potential reads
on every physical drift orbit have phase-level span at most THREE, in both
pair alignments. Hence any physical cell is shared only by coarse periods
whose indices differ by at most three. This derives a seven-period central
neighborhood without guessing a search horizon.

Take seven successive coarse inverse104 periods. Give all 364 coarse pairs
independent choices from the three-word palette. Give EVERY physical cell
an arbitrary initial color, and leave the output entirely unrestricted.
Require at least one nonidentity pair in the central (index three) period.
Group possible reads by their actual physical cell and their exact order
(period,pair,local index). Active reads demand the correct color and flip it.
Both finite literal-chronology problems are UNSAT. They have 53,145 clauses,
15,918/15,917 variables and 266/265 potential cells. Independent generic RUP
checking accepts the 81/42 addition proofs, with no RAT or deletion steps.
The two unchanged inverse104^7 paths are positive controls; fifty exact
fixed-assignment checks match direct literal read chronology.

Subject to semantic independent audit, this proves a local rigidity theorem:
in EVERY legal finite word of at least seven such periods, all periods at
distance at least three from either endpoint are identity periods. In a
one-sided infinite legal schedule, every period of index at least three is
therefore the unchanged inverse104. This conclusion uses neither a prepared
standard rail nor finite-support assumptions. The choices can vary arbitrarily
with occurrence and history.

Since inverse104 has charge -12, the one-sided infinite schedule cannot run
from any finite black seed. This is a no-go only for this exact coarse path,
pairing alignment and identity/minimal-bypass palette. It does not rule out
changing the coarse pair endpoints, a different scaffold, overlapping
block placements or nonminimal bypass shapes.

Sources: check_pair_bypass_local_window.py and pair_bypass_local_window/,
with complete CNFs, monotone RUPs, hashes and literal controls. The broader
claim remains author-only until those semantics are independently replayed.

### Independent status update

The minimality and seven-period local-rigidity theorem above are independently
signed by audits/check_pair_bypass_local_independent.py/json. The reviewer
regenerated every geometry, event, CNF clause and literal control and checked
both proofs. Exact fixed-pair-alignment scope is retained.

The forward-H counterpart is also analytically signed with an eventual,
not index-three, conclusion. Keep the board unchanged and transform an ant
boundary pose (p,h) to (p-d_h,-h). This conjugates a finite forward trace to
its reverse with turn word swapRL(reverse(w)). The transformation is a
bijection on coarse and fine poses and preserves the intermediate-pose
avoidance condition. An interior forward window becomes a cyclically shifted
inverse window; absorb the harmless phase-boundary shift into a finite
prefix. Hence forward schedules in the same minimal pair palette eventually
use identity H, rather than being excluded.
