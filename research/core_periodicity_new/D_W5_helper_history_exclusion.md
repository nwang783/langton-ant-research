# A protected-main / second-cohort contradiction excludes the D-first W5 gate

23 October 2026 15:48 UTC. Exact finite packet-history proof; independent
reconstruction requested. No path search, cap escalation or new count closure.

## Statement and supplied first-generation gate

Let an actual D BASE at(0,0,N), belonging to full D or DC, be followed by
V BASE(1,0,W) at entry C gap FIVE, with no earlier nonadjacent CLOSED center
contact with the original D chord. This configuration is impossible.

The independently signed1437 gate says that the old original D output
M=(2,0) survives until clock5 and then first retires in a full V(4,-1,W)
or full U(5,0,W). This helper is IMMEDIATELY before the target, and its own
C tail is empty. We retain that old identity and the full helper-entry
chronology, not merely its black color or a minimum-age abstraction.

The proof below in fact excludes any such protected-main helper history
before a V- or U-base target at the same final pose(1,0,W), provided the
same first-generation gate is independently supplied. Only the proper V
application is claimed here; the separate nonproper U gate is not assumed.

## A second identity which must retire even earlier

Split into the exhaustive nine actual full-source cases:

1. Original D is plain D; its immediate next full packet is one of the six
   V/VC/VCC/U/UC/UCC types, at(1,1,N), clock0. Its fresh full output local(0,0)
   is q=(1,1). This is local(1,0), an ENTRY CORE cell, at either final V or U.
   The immediately preceding helper cannot consume q: for helper V it is
   local(2,3), and for helper U local(1,4), neither a true input. Therefore
   q MUST retire strictly BEFORE the helper entry, not between helper and
   target, where no intervening packet exists.
2. Original D is plain D; the next full packet is D or DC at(1,1,N), clock0.
   Its fresh full output local(2,0) is q=(3,1). Both possible helpers require
   q WHITE: helper V local(2,1), helper U local(1,2). Thus q must retire
   strictly before the helper.
3. Original D belongs to full DC. That full DC itself freshly outputs
   q=(3,1), with full-source birth clock0. The identical two WHITE helper
   requirements force its retirement strictly before the helper.

These cover all possible outgoing tails of the first D and all possible
next full packets after a plain D. Each source finishes before the helper.
No initial-identity age is used: q is an actual new full output in every case.

## The main must remain CURRENT through that earlier consumer

Let Q be the first full packet consuming q. It is strictly before the
helper's FULL ENTRY; consequently its ENTIRE full raw-plus-marker context
occurs while the old original M is current. If that complete context touches
M at ANY required cell, the physical configuration is impossible: a true
input would retire M too early, and any other context contact violates the
complete-context current-residual survival lemma. Hence Q's complete context
must AVOID M entirely. This is the simultaneous identity coupling missing
from an independent one-output transfer query.

The context test does not assume a bounded head box and does not extend
protection after the helper consumes M. Full temporal order supplies the
needed protection throughout Q, including any attached C tails.

## Complete finite retirement check

For each nine sources, each of two helper types, n=0..5, eight actual full
consumer types and every true input slot, align q to that input. Heading is
-n modulo four; the containing full-source birth is clock0. There are2484
raw first-consumer cases, with exact reason counts:

-368 before the q-source's full exit;
-1014 conserved-sector impossibilities;
-762 already signed KV count-five exclusions;
-78 earlier nonadjacent CLOSED contacts with the ORIGINAL D chord;
-96 contacts with protected current M in Q's COMPLETE context;
-102 full consumers whose tails would finish after helper entry;
-60 impossible remaining zero-C endpoint cones;
-4 impossible remaining one-C endpoint cones.

There is NO open case. Every Q base lies strictly after a source which is
itself after the original D base; even the full-DC case has its first C
between them. Thus its contact with the original D chord is nonadjacent.
The target of the endpoint calculation is the HELPER FULL ENTRY, not the
later crossing endpoint, so full consumer completion is necessary.

## Transparent endpoint witnesses

After the other filters, a clock5 consuming base ends at y=2, x<=3, heading W.
Both helper entries have x>=4 and y<=0. W zero-C D/V/U motion cannot increase
x or decrease y, so it cannot reach either helper.

The four remaining clock4 cases are U/UC consuming bases at(4,0,N), ending
at(4,4,N). One C remains. N zero-C motion cannot lower y; its N-to-W C
increases y by one; W zero-C motion cannot lower y either. Hence a helper
with y<=0 is unreachable. The checker independently reconstructs the exact
zero/one-C D/V/U semigroups as well as these simple inequalities. It uses
the consuming BASE exit, so an attached immediate C is conservatively
allowed to occur after arbitrary zero-C movement; failure remains sound.

## Limits

This excludes the proper D/W5 FIRST-contact gate, not all later crossings
which already have an earlier contact. The conditional protected-main lemma
can be reused only when its same late-helper history has been proved.
Other first-contact gaps, nonproper gates, boundary positive controls and
unbounded zero-C lengths remain explicit. There is no finite C budget,
fresh-root charge, beta increment, V1/U1 closure or universal capture claim.

Checker: check_D_W5_helper_history_exclusion.py.
All2484 cases: chronology_dcuv/D_W5_helper_history_exclusion.json.
