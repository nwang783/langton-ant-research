# The first center self-contact has a two-through-six-C entry gap

23 October 2026, 14:12 UTC. This is an all-length geometric consequence of the
independently signed atomic turning identity. It is not a no-contact theorem
or a finite word-length bound. Independent reconstruction is requested.

## Exact event and clock conventions

Consider a finite actual atomic center path inside a complete recurrent-eight
factor, with the corrected center and straight atomic chords of the signed
1400 note. Suppose this path has a self-contact. Choose the earliest later
path parameter tau at which any point has already been visited, and let sigma
be its earlier parameter. Ordinary continuity through a shared endpoint of two
consecutive chords is not a repeated visit: those endpoint parameters are the
same path parameter.

All chords are nonzero, and adjacent chord turns are strictly between -pi and
pi. Adjacent chords therefore cannot reverse or overlap. With finitely many
chords, a first repeated point exists whenever the polygonal path is not
injective. Before tau the path is injective, so the earlier parameter sigma
is unique. The subarc from sigma through tau is a simple closed polygon.

Let a be the chord leaving sigma and b the chord arriving at tau. If sigma
is an atomic vertex, take the outgoing chord. If tau is an atomic vertex,
take the incoming chord. Both partial endpoint chords have positive length.
Let n be the difference between the C clocks at the ENTRIES of atoms a and b.
Thus n counts the C atoms from a through the atom immediately before b.

This definition deliberately does not count a C atom b merely because tau
happens to be its endpoint. The claim concerns atomic ENTRY clocks. It does
not assert that every possible choice of marked endpoints around the loop
has the same C gap.

## The simple loop fixes the lifted angle

The signed 1400 turning identity gives the sum of all turns strictly inside
this loop, from its first chord direction to its last chord direction:

    L = n*pi/2 + alpha(a) - alpha(b),

where alpha(U) = 0, alpha(V) = atan(1/3), and alpha(D) = alpha(C) = pi/4.
In particular, the offset difference lies between -pi/4 and pi/4.

At the closing point, the principal turn gamma from chord b to chord a lies
strictly between -pi and pi. The endpoint cannot be an opposite-direction
cusp: the two incident segments would then overlap immediately beside the
endpoint, contradicting simplicity. A collinear forward corner is harmless.

The simple polygon's signed total turn is plus or minus 2*pi. Since n is
nonnegative, L is at least -pi/4. Adding gamma greater than -pi makes a total
of minus 2*pi impossible. Hence this particular loop has positive orientation,

    L + gamma = 2*pi,

and therefore

    pi < L < 3*pi.

If n is zero or one, L is at most 3*pi/4. If n is at least seven, L is at
least 13*pi/4. Both contradict the strict interval above. Thus

    2 <= n <= 6.

The endpoint refinements are exact:

- n = 2 requires alpha(a) > alpha(b).
- n = 3, 4 or 5 permits every ordered pair of atom types at this angle level.
- n = 6 requires alpha(a) < alpha(b).

Equality at n = 2 or n = 6 would require a forbidden opposite-direction
closing cusp. The finite checker verifies all 58 surviving atom-pair and
clock cases using the exact ordering of the three alpha values, without
floating-point angle comparisons.

## What this does and does not reduce

The signed atomic nonreturn and center-turning theorems imply that every
closed full-pose atomic excursion has a center self-contact. Its first such
contact therefore supplies a contiguous actual geometric loop with an entry
clock gap between two and six. The rest of the history is not erased, and
no claim of feasibility after loop deletion is made.

The two atoms may be far along the factor, and the loop can contain arbitrarily
many zero-C atoms. This gives neither a packet-depth cutoff nor a finite
geometric box. The contact may be a proper crossing, a vertex touch, or the
onset of a later overlap. The event definition and the simple-loop proof cover
these degeneracies, rather than assuming a transverse crossing.

For a first atom D or C, the separate finite proper-crossing inventory has
only two geometric possibilities, both with later V. Their headings are E
or W, so the first-contact gap can only be three or five, respectively. This
inventory is being checked separately and is not a premise of the horizon
proof. The existing actual ten-cell control DC, DC, DC, D, V has a proper
gap-three center crossing, so this result cannot be strengthened into a
universal no-contact statement.

The open task is to connect these bounded-C, possibly unbounded-length local
loops to exact literal history or an adequate conserved quantity. The signed
turning theorem alone does not do that. Larger full-pose returns, V1, U1 and
global capture remain open.

Dependency: atomic_center_turning_frozen_20261023_1400/manifest.json, SHA-256
8b2e2c132d6dd857e5acee596167d5ac6b169eb1795998f00ea14864d2a2ad84.

Working checker: check_first_center_contact_C_horizon.py.
Finite table: chronology_dcuv/first_center_contact_C_horizon.json.
