# Narrow orientation clarification for f0d24e49

24 October2026. This addendum is mandatory when reading the frozen boundary proof. It changes no formula, checker, field, or claimed scope.

In the finite-side-current paragraph of DROUGHT_BOUNDARY_PEELING_AND_PINNING.md, the phrase

    tangent direction of an R turn from the inward normal

means, and should be read as,

    tangent direction of an R turn from the OUTWARD normal, which is the incoming heading when the ant arrives on that side FROM the strict interior.

The exact side-index directions used by the code and proof are:

- top side: east;
- right side: south;
- bottom side: west;
- left side: north.

With that ordering, both straight RR and LL passages are01->10 and change Phi by-1. Using the geometric inward normal would reverse the ordering and the sign of Phi; it would not change the absolute finite budget, but that is not the convention in the frozen calculation.

Likewise, 'normal-arrival' denotes this arriving outward-normal heading, not a heading pointing geometrically into the rectangle. All corner and complete-episode claims already use the correct actual headings.
