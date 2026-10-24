# No prepared104 return in the central four-row cylinder

Independently signed, 2026-10-23 09:43 UTC. The separate checker reconstructs
the wake from literal104 and enumerates all histories without a period-parity
shortcut. See audits/check_wake_fourrow_chronology_independent.py/json.

This is a fixed read-strip obstruction, not a varying-width return theorem.
It does not assume a supplied visit or period cutoff, and it prescribes no output.

Use compass headings N,E,S,W=0,1,2,3, the mature NE standard104 wake's
periodic black profile, and pose-sector bit x+y+h=1 modulo2. The proposed
return has full displacement D=(-2,-2). Require every read cell to be a
translate by ZD of one of

    (0,-2),(1,-1),(0,-1),(1,0),(0,0),(1,1),(0,1),(1,2).

Their input bits are 0,1,1,0,1,0,0,1. Signed audit LK gives, without a
chronology assumption, total period at most12 and site multiplicity caps
0,1,2,3,3,2,1,0. The source is `wake_return_flow_bounds_h4_off-2.json`.

At site i, enumerate every incoming-heading string of each length from0
to its cap, using the two headings allowed by the checker sector. The
outgoing headings are fixed by alternating turns starting from the
prescribed input bit. This is exactly99,225 history assignments. Discard
zero length and lengths not divisible by4, because displacement(-2,-2)
has equal even coordinate counts and the endpoint heading must match.

Matching each directed edge's incoming and outgoing occurrences in
chronological rank gives a permutation on the event set. There are only
two assignments with matching ports. In the displayed site order their
incoming-heading strings are:

    (), (E), (S), (S,N), (W,W), (E), (N), ();
    (), (E), (S,S), (S,N,S), (W,W,W), (E,W), (N), ().

The first is one eight-event component of total seam winding0. The
second is that same eight-event zero-winding component together with a
four-event component of winding1. In neither case can all events be one
actual translating ant orbit. Indeed chronological edge equations around
any nonempty component give its positive length equal to its winding
times the full period, so a zero-winding component is already impossible.

`check_wake_return_fourrow_finite.py` performs this entire finite
enumeration without a SAT/SMT solver and preserves both exact port-cycle
witnesses in `wake_return_fourrow_finite.json`. A separate shared-epsilon
SMT formulation agrees, but its solver response is not needed for the
finite replay proof.

The prepared infinite wake is merely the local input contract. This
result does not claim that a finite seed prepares such an interface, nor
exclude a return using other cell orbits, a different displacement, a
nonperiodic return, or another sector.
