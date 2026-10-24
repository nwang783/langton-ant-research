# Verified finite-order powering adapter for the integrated unit solver

2026-10-23 07:10 UTC. New separate adapter, submitted for independent review.
The general additive-I unit implementation is independently signed KJ. No
singular finite-power matrix or changing boundary-heading extension is claimed.

## Input and checked geometry

Supply a finite heading/turn unit alphabet, nonempty ordered images, a2x2
integer matrix A, a positive integer p with A^p=I, and a root a on an ACTUAL
first-letter cycle. The input validation is strict: integer state, matrix and
heading data exclude booleans, all image indices are checked, and every image
is physically traced. Its incoming/final headings must match its parent exactly
and its net movement must equal A times the parent's physical unit movement.
The matrix-power equality is checked by exact integer arithmetic.

Follow the finite first-letter map from a. If it does not return to a, this
adapter reports an unsupported root convention, not nonrealizability. Otherwise
let q be its cycle length and take m=lcm(p,q). Compose phi^m literally. The
optional powered-image-size cap gives UNKNOWN, not a negative result.

## Why the composition is an actual exact-I presentation

Each image replaces a physical unit movement v with a word of net A v and the
same boundary headings. By induction, phi^j(s) has net A^j v_s and the same
incoming/final headings: expand each child, sum A times its coarse movement,
and telescope the already matching headings. Therefore phi^m has net v_s and
literal physical heading compatibility. The adapter REVALIDATES this result
using the signed exact-I unit validator rather than relying only on the proof.
Its first child is a because q divides m.

The selected actual power-limit of phi^q(a) equals that of phi^m(a), since m is
a multiple of q and the latter is a cofinal subsequence of the former's nested
nonerasing prefixes. This includes stabilized nongrowing controls; an infinite
model acceptance is only flagged when the resulting prolongable root grows.
No unproved claim about intermediate root-cycle phases is used.

The adapter then calls the signed KJ generated-cover finite-seed solver. As an
optional safe early shortcut, an internally inconsistent finite powered block
is already a complete negative certificate on ANY board. Its two conflicting
initial-bit requirements and physical read indices are reported. Otherwise all
unknown-seed, generated-cover and frame checks remain mandatory.

## Executed controls

`finite_order_adapter.py/json` verifies:

- A=-I, order2: composed images have length81; a literal initial-bit conflict at
  reads5 and9 certifies the negative control.
- A=[[0,-1],[1,0]], order4: composed images have length2401, with the same
  independently replayable finite conflict.
- A=[[1,2],[0,-1]], order2: a NONORTHOGONAL integral finite-order input composes
  to exact-I. Its root reaches only a stable identity and the complete solver
  correctly returns an empty seed, explicitly nongrowing. Other powered images
  have length49; they are not silently ignored during the geometry check.
- A spatial-I two-state first-letter root cycle correctly takes common power2.
- Wrong order, boolean matrix entries and wrong scaled displacement are rejected
  as invalid input, not treated as proof of nonrealizability.
- A transient noncyclic root reports unsupported, and an explicit size cap reports
  UNKNOWN. Neither creates a false negative or growing acceptance.

This extends the integrated UNIT solver to its stated finite-order geometry
by a verified cofinal power. It does not implement singular eventually periodic
powers, general macro bases, arbitrary heading-boundary maps, or unrestricted
ant trajectories. No growing model is accepted.
