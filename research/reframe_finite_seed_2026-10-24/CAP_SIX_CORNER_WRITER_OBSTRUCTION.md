# A cap-six corner-preserving writer, and its forced overlap

24 October 2026. Author exact construction and proof, pending audit. This
separates a genuine one-shot resource transformation from a reusable compiler.

## Exact finite-board writer

Start at (0,0), north, with exactly D={(-1,1),(-1,2)} black. The next ten turns
are RRRRLRLRRL; the complete field and active component at every cut are in
corner_writer_controls.json. The maximum active w mass is six, and the final
head is (-1,3), north, with empty active component. The final complete field
has three components in the SAME fixed k=1 w lattice:

- corner D'= {(-2,1),(-2,2)}, exactly D translated one cell west;
- singleton {(-1,0)};
- three-edge star H={ (0,-1),(1,-1),(1,0) }.

No passive field is discarded, no extra seed cell is present, and there is no
intervention. This is therefore an actual one-shot corner-preserving writer.
It is the compact complete-path profile in cap6_resource_obstruction.json,
path index 21795 of the exploratory cap-six first-return enumeration.

## Exact limit of nonnegative component-type fuel

Consider a potential A(normalized active state) plus the sum of nonnegative
weights W(type) of complete passive components, where types identify rigid
translations and quarter rotations. The initial and final active state are
both empty, with the SAME heading. The consumed and emitted corners have the
same type, even the same absolute orientation. Thus this actual prefix changes
the potential by exactly

    W(singleton) + W(three-edge star).

If that potential is required to be nonincreasing on every complete cap-six
first return, both weights must be zero. In particular, merely charging the
consumed two-edge corner cannot restore a positive singleton fuel while
retaining this universal nonincrease requirement. This is an exact integer
identity witnessed by a physical finite prefix, not numerical LP infeasibility.
It does NOT rule out all typed potentials, geometric weights, history-dependent
ranks, or a potential that permits and later charges some increasing returns.

## A second identical copy is not free

The writer displacement is d=(-1,3). To put a fresh input corner at the next
identical normalized port, add D+d={(-2,4),(-2,5)} to the initial seed. This
extra component is completely passive throughout the first ten updates, and
the first writer remains exact. On the next block's fourth R, update13, the
PREVIOUS emitted corner D' is also imported. The active mass at cut14 is eight,
so the specified cap-six second profile cannot hold.

Geometrically, relative to the new root pose, the old corner occupies cells
(-1,-2),(-1,-1). One of its w vertices is (-1,-3) in doubled relative coordinates,
which is the fourth fresh-star leaf. Its component has two edges; the new target
corner has two edges; and the four new root edges give active mass 2+2+4=8.
Additional passive components cannot remove these known edges. They can only
cause an earlier deviation from the prescribed complete profiles. Thus this
is an exact overlap obstruction to immediate translated repetition, not merely
a failure of the chosen minimal seed.

The reusable-computation obligation remains a different physical transport
phase that feeds compatible corners to the actual cursor, consumes or avoids
all earlier outputs, and fits within one finite pre-funded initial field.
Neither the type-level resource identity nor finite-board reversibility supplies
that transport. The physical-lift analysis is testing this separate obligation.
