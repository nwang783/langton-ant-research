# The six-transition cap-seven nonempty core cannot import its own deleted cells

24 October 2026. Exact physical semantics of the supplied new nonempty kernel
cycle. One loop has a complete five-cell realization. Two consecutive full
profile loops have NO realization, even with arbitrary unread exterior.
The literal double R/L word DOES execute from the five-cell control, so this
is not being presented as a turn-word contradiction or generic rotation fact.

## 1. Supplied core and exact one-loop control

The compact source is
`../reframe_finite_seed_2026-10-24/cap7_structure_probe.json`, cycle_witness.
It supplies six ordered normalized transitions, word

    W=RRLLLL,
    initial head(0,0),N, fixed w sector1,
    active C={(1,-1),(2,-1),(2,0)},
    imported D={(-1,-1),(-1,0)} at the FIRST R.

Use the COMPLETE finite initial board C union D, of mass5. Every physical
fine cut matches the proposed complete active component, with maximum mass7.
There is no emitted passive component. Its six updates are:

    0  R at(0,0):   import the complete old D and write(0,0);
    1  R at(1,0):   write(1,0), closing a w cycle through old C;
    2  L at(1,-1):  delete the first old C edge, a cycle erasure;
    3  L at(2,-1):  delete the next old C edge;
    4  L at(2,0):   delete the last old C edge;
    5  L at(1,0):   delete the new edge born at1.

At cut6 the actual pose is(1,-1),S and the complete board is

    C'={(-1,-1),(-1,0),(0,0)},

all of which is active. The imported old dimer D survives, together with
the fresh R0 edge; the old active three-edge path and fresh R1 edge have
actually been consumed. This is a real first-port import/cycle-erasure
exchange, not an endlessly renewable normalized state.

## 2. Exact double-loop obstruction with the continuous pose retained

**Theorem.** No complete initial board can realize two consecutive copies
of the supplied six-transition full-component loop.

**Proof.** The next normalized input C is indeed C' at pose(1,-1),S, so
the active-shape seam alone passes. But the required second imported D,
rotated by the ACTUAL heading S and translated by the ACTUAL head(1,-1), is

    D'={(2,-1),(2,0)}.

Those physical cells were read L and deleted at first-loop updates3 and4.
Neither is read again before the second loop's first R, at global update6.
They are therefore WHITE, regardless of every unread exterior cell. The
second loop cannot import the required old black dimer D'. No alternative
placement is allowed by the prescribed continuous pose and full profile.

The exact complete-port/read-parity witness is at cell(2,-1). At cut0 it
is required initially BLACK as a member of C. At cut7, after the proposed
second first-R import, it is again required currently BLACK, but the supplied
chronology has toggled it exactly once, at L3. That requires its initial bit
WHITE. These two immutable requirements contradict. QED.

This conclusion is stronger and more local than applying generic rotation
closure after enough copies. It identifies the exact unavailable lifetimes
and the wrong physical import port. Initial exterior black cells cannot
recreate a deleted cell without an actual intervening R at that same cell.

## 3. Adversarial literal double-word control

From the five-cell board, the physical ant DOES execute RRLLLLRRLLLL for
twelve updates. After the second first R its complete active component has
only4 edges, rather than the prescribed6: the old dimer is absent. After
twelve updates the full board is the singleton{(1,-1)}, not the normalized
three-edge source field. Thus turn-word repetition is not kernel-state
recurrence. All historical cells have been kept until their actual toggles.

The checker records both actual cursors and both active graph fields, in
fixed sectors w=1,z=0. No inverse trajectory, graph-role swap, pose reset,
mid-run cell supply or unrecorded passive-module motion is used.

## 4. Scope and artifacts

`finite_general_component_profile_lift.py` is a separate extension of the
already signed finite-profile guard helper, allowing NONEMPTY active seams.
The old frozen empty-return helper and cap-six certificates are unchanged.
It constrains the final actual component rather than substituting an empty
one, and checks every transformed active-component seam.

`check_cap7_nonempty_cycle.py` reconstructs the source six transitions,
constructs the five-cell one-loop board, checks the double-loop initial-bit
contradiction and records the contrasting literal double-word execution.
`cap7_nonempty_cycle_certificate.json` binds the source, full traces and
exact deleted-cell identities.

Structural uniqueness of this six-state recurrent SCC in the cap-seven
kernel is a SEPARATE author enumeration claim. This note proves only the
supplied cycle's physical nonrepeatability. If that SCC coverage passes,
the physical witness can refine/unfold this apparent nonempty recurrence;
it does not by itself prove cap-seven exit, finite return grammar, universal
attraction or standard104 classification. A path may leave this core for a
different actual transport mechanism.
