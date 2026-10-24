# Singleton fuel and finite-support cap-five exit

24 October 2026. Author proof pending independent audit. Uses the complete
cap-five local kernel and first-return grammar frozen in grammar_manifest.json.
No standard-highway capture, undecidability, or independent novelty claim.

## 1. Exact component-count invariant

At an empty-active cut every black w component is passive. Along an actual
first-return path, an R import removes exactly one COMPLETE passive component;
an L detachment adds exactly one COMPLETE nonempty passive component. All other
passive components stay unchanged. A passive-passive merge cannot occur silently:
only the active R insertion changes connectivity, and any attached component
is then part of the recorded complete import. The full black field, including
all earlier emitted stars, is retained throughout.

Therefore if S is the number of singleton black w components, the exact change
between empty-active cuts is

    S_after - S_before = (# singleton emissions) - (# singleton imports).

singleton_return_certificate.json lists all complete consumed/emitted type
counts for every one of the 110 first-return paths. Its exact integer checker
finds S_after<=S_before on every path, with strict decrease on 108 paths.
There are exactly two zero-drop paths:

A, index 0: RRRRL; imports nothing; emits one three-edge star.
B, index 11: RRRRLRL; imports one singleton; emits one three-edge star and one
singleton. The imported singleton need not be the same cell as the emitted
singleton. This is component-count conservation, not lifetime conservation.

For a finite black field, S is a finite nonnegative integer. Thus any infinite
cap-five orbit eventually has only A and B first returns. More quantitatively,
there are at most S strict-drop returns after a specified empty-active cut.

## 2. Exact cursor geometry of A and B

Use doubled physical coordinates and normalize the macro-entry pose to p=(0,0),
north, with w=(1,-1). Both paths start by four R updates, then an L. At that L,
the w cursor moves from (1,-1) to (-1,1), leaving exactly the three black edges
with cell midpoints (0,-1),(1,-1),(1,0), centered at the old w vertex (1,-1).

For A this is the final cut. For B the required initial singleton has midpoint
(-1,1). After the first L it is the active singleton at w=(-1,1). The extra R,L
replace that singleton by the edge at midpoint (-1,0), and move w once more
in the same direction, to (-3,3). Thus the macro w trajectory is a straight
stride of respectively one or two w-lattice edges. In both cases the physical
heading rotates by a quarter-turn counterclockwise. Hence consecutive macro
stride directions turn by the same quarter-turn. Reflection/rotation of the
integer w lattice makes the generic enumeration directions E,N,W,S equivalent.

These statements are about actual intermediate w positions. The B middle
vertex can retain a singleton. We do NOT assert that distinct macro segments
are disjoint or forbid crossings at previous B middle vertices.

## 3. Persistent stars forbid old macro starts

During a run using only A and B, every freshly emitted three-edge star remains
an unchanged complete passive component. Neither path imports any component
of size three or more. Such a component cannot be read or modified until it
is actually imported. Any attempted attachment therefore leaves the specified
two-path run. In particular each earlier macro START vertex retains its three
incident black star edges for the rest of the run.

Every vertex reached along a later macro segment is either its final empty
active cut or B's intermediate cut with active mass one. It cannot equal an
earlier macro start vertex, where the unchanged star would force active mass
at least three. Thus a necessary condition on a run of A/B macros is:

- each segment has length one or two on the square w lattice;
- successive directions turn by the same quarter-turn;
- no segment, including its interior vertex, visits an earlier segment START.

This last condition is weaker than full self-avoidance. It allows intersections
at old stride-two interior vertices and imposes no extra restriction from
other passive archives. It is therefore safe as an impossibility relaxation.

## 4. Eight-return bound for the zero-drop subsystem

The exact bounded-stride enumeration keeps only segment start/end vertices as
forbidden vertices. Starting at the origin, it enumerates all choices of stride
one or two and checks each newly traversed lattice vertex against the earlier
start vertices. Counts of surviving prefixes at lengths 1 through 9 are

    2, 4, 8, 10, 12, 10, 8, 4, 0.

The companion script is a 9-level exhaustive binary check with exact integer
coordinates; every surviving word is recorded in the JSON. There is no run of
nine A/B returns. The four geometrically surviving length-eight stride words
are 12211221, 12211222, 22211221, 22211222. They are only relaxed geometric
survivors, not assertions of physical realizability.

## 5. Finite-support cap-five exit theorem

No finite-black-seed orbit can have active w mass at most five at every cut
from some time onward. Equivalently, every such orbit has infinitely many cuts
with active w mass at least six.

Proof. Suppose the cap holds forever from a finite cut. All fields at finite
cuts have finite black support. The cap-five kernel minus the empty-active
state is a finite DAG, so the orbit must reach empty and return to empty
infinitely often. Its first returns belong to the complete list of 110 paths.
Their singleton count never increases and decreases on 108 of them. Finiteness
therefore leaves an infinite tail consisting only of A and B. Section 4 rules
out even nine consecutive returns in that tail, contradiction.

More quantitatively, beginning at an empty-active cut with S singleton
components, there can be at most 9*S+8 completed first returns before cap exit
or a final nonreturning cap-preserving suffix. This counts at most S strict
drops, with at most eight zero-drop returns in each of their S+1 gaps. A final
suffix avoiding the empty state has bounded length by the same finite DAG.
No mass-only highway bound follows; this is solely a small-active-cap exit
result. On infinite-support backgrounds S need not be finite, so the finite-
support theorem does not automatically extend to them.
