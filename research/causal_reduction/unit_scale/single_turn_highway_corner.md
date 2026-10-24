# Prepared ten-cell orthogonal standard104 interface

23 October2026,08:20UTC. Independently signed KZ all-parameter/all-future certificate. A positive ONE-SHOT corner, not renewable memory.

Let H be the retained standard104 word. Use compass headings N,E,S,W=0,1,2,3.
Rotate the canonical thirteen-cell W-heading seed counterclockwise once to
obtain the SE front with incoming S and drift(2,-2). Execute the first68
turns of H and translate its resulting head to(0,0). Its complete resulting
black set B has23 cells and its incoming heading is N. These23 coordinates
are in `single_turn_highway_corner_certificate.json`. Put F=H[68:]+H[:68].
The state(B,0,N) is a retained104 phase with drift(2,-2).

For every integer m>=3, add to B the following ten cells translated by
c_m=(2m,-2m):

    K={(1,4),(1,5),(1,6),(2,0),(2,1),(2,2),(2,5),(3,0),(3,3),(3,4)}.

The two sets are disjoint, so initial mass is exactly33, independent of m.
These are finite preloaded corner cells, not an infinite prepared background.
The exact actual word is

    F^m R H^infinity.

At time104m+1 its pose is(2m+1,-2m,E), and the subsequent canonical H has
NE drift(2,2). Thus the incoming SE front turns counterclockwise90degrees.
The invariant physical pose sector is respected. The threshold3 is sufficient,
not claimed minimal. Rotation gives the corresponding physical corner types.

## Exact whole-field proof and output ownership

`certify_single_turn_highway_corner.py` retains B and every prefix toggle.
The K relation is exactly disjoint from ALL F^m reads for every m>=3.
Thus the signed standard front supplies the approach. Its next cell c_m is
white, so the literal R is valid. The COMPLETE output immediately afterward is

    B symmetric_difference parity(F^m) symmetric_difference {c_m}
      union (c_m+K).

No approach trail or cap debris is discarded. The parametric initial,
pre-R and post-R black relations are in the frozen JSON. All104 infinite-tail
slot families are compared against this complete output, with every earlier
same-cell read toggled in. There are262 nonempty ordered prior relations and
no bad-color set. This is not a long repeated-word inference.

The complete XOR of the first outgoing104 block is also listed in the JSON,
relative to c_m. Every one of the ten prepared corner cells is read. Their
complete future turn histories, with times measured after the literal R, are:

    (1,4): 80L,84R,96L
    (1,5): 77L,85R,93L
    (1,6): 76L,88R,92L
    (2,0): 11L,19R,23L
    (2,1): 2L,10R,18L,22R,102L
    (2,2): 3L,7R,35L,103R
    (2,5): 50L,78R,86L,94R,202L
    (3,0): 12L,16R,24L
    (3,3): 33L,37R,41L,105R,113L,125R,205L
    (3,4): 44L,48R,52L,108R,112L,204R.

Consequently only(2,2) and(3,4) remain black among K after its last use.
Eight required input cells are consumed. This is not an unchanged reusable
corner. A physically supplied next corner, or a proved restoration with all
white guards, is an additional obligation.

## Discovery scope

The motivating architecture was only one literal read between orthogonal
standard104 phases, not a search over longer connector words. Its finite
phase inventory was useful for finding this witness; this theorem needs
only the explicit phase68-to-phase0 witness and its exact verifier.
No completeness or optimality claim about the171 initially retained phase
controls, ten-cell cost, or more complicated corner mechanisms is needed.

## No mass-only universal capture-time bound

The initial mass is33 for every m while the SE-to-NE change occurs at104m+1.
A perpetual104 tail cannot begin at or before104m-104: a complete early
period has drift(2,-2), whereas every sufficiently late period has drift(2,2).
Thus any universal bound on the onset of a perpetual104 highway must depend
on more than the number of initial black cells. This does not contradict a
possible bound involving seed diameter, nor assert that all seeds capture.
