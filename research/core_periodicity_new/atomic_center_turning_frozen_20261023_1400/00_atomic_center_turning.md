# Any closed atomic excursion has a self-intersecting center polygon

23 October 2026, 14:00 UTC. This is a finite geometric identity plus a separately
dependency-bound consequence of the signed atomic four-C nonreturn theorem.
Independent reconstruction is requested. It is not a global capture claim.

## Exact setting

Work only at actual atomic marked cuts arising when a complete recurrent-eight
factor is split into its D, V or U base and its attached C atoms. The earlier
atomic four-C theorem applies in this exact setting, including internal C cuts
and the factor's first cut. No arbitrary enlarged atomic language is licensed.

The headings N, E, S and W have indices 0, 1, 2 and 3. Rotation by one heading
index is clockwise. A C atom changes the heading index by minus one. Associate
to a marked pose with head p and heading h its corrected core center

    z = p + rot_h(-1/2, -1/2).

Join successive centers by straight segments. These are auxiliary chords, not
the microscopic path of the ant or the motion of an occupied material object.

The raw literal endpoints give the following center increments, in the entry
heading frame:

- D: (1, 1).
- V: (1, 3).
- U: (0, 4).
- C: (1, 1), with the next heading rotated left by 90 degrees.

All segments are nonzero. A C atom's raw head increment is (0, 1), but the
rotation of the center correction changes its center increment to (1, 1).
Confusing these two increments would invalidate the turning calculation.

## The exact signed turning identity

Lift the forward heading angle to a real angle theta, increasing it by pi/2
at every C atom and leaving it fixed at D, V and U. The direction of an atom's
center chord has the lifted angle

    phi = theta - alpha(atom),

where alpha(D) = alpha(C) = pi/4, alpha(V) = atan(1/3), and alpha(U) = 0.
Thus all alpha values lie in the interval from 0 through pi/4.

For consecutive atoms a and b, the signed principal turn from chord a to
chord b is exactly:

- alpha(a) - alpha(b), if a is not C. This lies between -pi/4 and pi/4.
- 3*pi/4 - alpha(b), if a is C. This lies between pi/2 and 3*pi/4.

Both intervals lie strictly inside (-pi, pi), so these are genuinely the
principal turns. There is no hidden whole-turn adjustment or reversal corner.
The finite checker reconstructs all sixteen cross products and dot products
directly from the literal raw words.

Now suppose a finite excursion returns to its full marked pose. Its number
of C atoms is a multiple of four. Sum the principal turns cyclically, including
the corner between the last chord and the first chord. The alpha terms cancel,
so the exact total is

    (pi/2) * number_of_C_atoms.

Consequently the turning number of the closed center polygon is exactly its
C count divided by four. This identity holds whether or not the polygon is
simple. In particular, the turning number is positive for every such excursion:
with no C, all D, V and U increments lie in one fixed forward cone and their
positive forward components prevent a return.

## Consequence of atomic four-C nonreturn

A simple closed polygon has signed turning number either plus one or minus
one. The usual statement allows collinear forward corners: merge them, which
does not change either simplicity or the turn sum. Adjacent reversal corners
are already absent by the strict principal-turn bounds above.

Thus a simple closed full-pose center excursion here would have exactly four
C atoms. But the independently signed atomic four-C nonreturn theorem excludes
that actual excursion, with no factor-first exception. Therefore every closed
atomic full-pose excursion in the stated language has a center polygon that is
not simple. Equivalently, its closed polygon map is not injective away from
the identification of its two endpoint parameters. A nonadjacent intersection,
touch or overlap must occur. Degeneracies count as intersections, not escapes
from the conclusion.

This reduces any possible return with eight or more C atoms to a genuine
spatial self-contact of the auxiliary center polygon. It does not prove that
such a contact is impossible.

## The indispensable limitation and next exact question

A crossing of straight center chords is not automatically a repeated ant cell,
a repeated marked pose, a collision of residual identities, or an incompatible
literal read. The ant may cross older traces and the chords skip a whole raw
atom. No claim of planar self-avoidance is made.

The open bridge is therefore concrete: can every possible center-chord
self-contact in an actual complete-eight history be associated with a literal
ordered-identity or marker conflict, or is there a finite literal control
showing that a crossing is harmless? Until that bridge is proved, larger-C
cycles, V1, U1 and global capture remain open. Funding coverage remains 11 of 13.

## Reproducibility

Working checker: check_atomic_center_turning.py.
Working finite table: chronology_dcuv/atomic_center_turning.json.
Dependency: atomic_common_4C_frozen_20261023_1344/manifest.json, with SHA-256
dd9c3ad2c7c7dd2e2383e43e05710ea4621f2d6fd25e07a3f8860fc7c458492f.

The checker reconstructs every full packet as its literal base plus C tails,
all four atomic center increments, and all sixteen adjacent angle cases. The
all-length conclusion is the explicit telescoping argument and the elementary
simple-polygon turning theorem, not a finite path search or a numerical cap.
