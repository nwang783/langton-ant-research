# Primitive translating spines and a bounded last-parent clock that does not bound drought

24 October 2026. Separate addendum to CHRONOLOGICAL_SPINE_ORIENTATION_MANIFEST.json (65a4b907). The main result is independently signed; the two additional statements here require their own audit. The main immutable files are unchanged.

## 1. The positive quotient-cycle shift is exactly one

Use the general last-exit quotient of the main note, for an actual unit-grid translating read path with nonzero integer drift d. Its quotient cycles have positive integer layer shift m. In fact

       m=1,

and each cycle has zero total effective turning. Thus the component-count formula simplifies to the number of quotient cycles.

### Why the quotient cycle is embedded

Take one directed quotient cycle. Its vertices are distinct classes modulo Z d. A translated horizontal unit grid edge and a vertical unit grid edge can intersect only at an integer grid point, hence at an endpoint. An interior crossing in the quotient would therefore repeat a vertex class. Coincident parallel edges would likewise repeat endpoint classes. The degenerate two-edge backtrack has zero displacement and is already excluded by positive shift. A one-edge essential loop can occur only when the unit edge itself is one deck translation; it is embedded as well.

The selected cycle is therefore a simple embedded polygonal closed curve in the cylinder R^2/Z d. This is an assertion about the actual chronological LAST-PARENT edges. It does not identify them with black Tait-graph edges, an active-component graph, or the controller lane's other last-L maps.

### Primitive shift by ordering the lifts

Suppose m>1. A lift of the cycle, joined to all its translates by m d, gives a proper embedded periodic line. Translating this line by0,d,...,(m-1)d gives m disjoint proper lines, all contained in strips of bounded transverse width. They are disjoint because an intersection would identify two points of the embedded quotient cycle.

Each line separates the far positive and negative transverse half-planes. The Jordan separation property therefore linearly orders these disjoint lines from one transverse side to the other. Translation by d preserves that order, since it preserves both far transverse half-planes. But it cyclically permutes the m lines. A finite linearly ordered set admits no nontrivial order-preserving cyclic permutation. This contradicts m>1. Positivity excludes m<=0, proving m=1.

### Zero turning by a finite polygonal angle identity

Choose a straight essential curve parallel to d, sufficiently far on one transverse side that it misses the selected cycle. The two embedded essential curves bound a compact annulus in the flat cylinder. Triangulate this annulus into finitely many Euclidean triangles, adding vertices on the two boundaries as necessary.

If V_i and V_b are the interior and boundary vertex counts, the triangle-edge and Euler identities for an annulus give F=2V_i+V_b. The sum of all triangle angles is pi F. Interior vertices contribute2pi V_i, so the sum of the interior boundary angles is pi V_b. Hence the total exterior turning of the two oriented boundary curves is zero. The straight curve has zero turning, and therefore so does the selected cycle.

This is only the angle identity of an explicitly embedded annulus. No temporal-forest Euler characteristic is equated to the instantaneous black-graph Euler characteristic. For the ant, every cycle vertex turns by90 degrees by the sector constraint, so its total signed quarter-turn sum is exactly zero.

The result does not bound the number of cycles. In particular it supplies no universal two-spine theorem for an unknown finite-seed future. Standard104 has two because its separate exact quotient computation gives two cycles.

## 2. Exact last-read time jumps on every MT tree edge

The signed MT tree layering also gives a second, distinct temporal potential. Its selected last-parent edges have uniformly bounded chronological time jumps, even while the completed pristine drought grows without bound.

Let ell_n(v) be v's last read in the completed drought, measured relative to its starting cut s_n. Give the final, fresh root the time label D_n. Write K=n-100. With the same disjoint upper/lower/middle decomposition as the main note,

       ell_K(q)=ell_0(q),                         q in translated upper cap;
       ell_K(q)=ell_0(q)+104K,                    q in fixed lower cap;
       ell_K(r+2k(1,1))=tau_r+104(K-k),           1<=k<=K.

In the first line, q denotes the baseline vertex before translation by(2K,2K). The constants tau_r are the exact latest SW phase times already listed in the signed22-row table.

These formulas follow from the actual source hit indices, not a predicted timing fit: upper hit indices are independent of K; every lower SW/F hit shifts by104K; all phases of every middle class occur and their final phase is fixed. At a boundary the formulas agree because

       ell_0(r)=tau_r,
       ell_0(r+2(1,1))=tau_r-104.

For a middle edge(r,k)->(r',k+delta), its time jump is exactly

       tau_r' - tau_r -104 delta,

independent of K and k. The22 positive jumps range from1 to125. Every upper or lower edge has precisely its baseline jump, including both cap interfaces and the final edge into the root.

The maximum over the ENTIRE tree is therefore exactly

       max_edges [ ell_n(parent(v))-ell_n(v) ] =29865

for every n>=100. It is attained on the fixed lower edge

       (210,186) -> (210,187),

whose baseline last-read labels are29029 and58894. Both labels acquire the same104K shift.

The four inserted maximum-spine edges have jumps1,1,5,97, summing to104 while adding only four units of tree height. This gives the exact relation D_n=26H_n+34335 already signed in the main note.

### This is NOT a bounded lifetime-age statement

The actual old-M BLACK lifetime R20165 at(206,229) is still present at the starting record cut and is consumed at update31805+208n. Its age is

       11640+208n,

which is unbounded across the same family. Its source and consumption are the signed complete-field archive transfer, not a hypothetical revived permanent cell.

Thus a bounded time jump on EVERY selected last-exit edge is not a substitute for bounding the ages of actually consumed R lifetimes. The forest records the latest departures from cells and can forget when the specific input identity was born.

Together, initial mass22, tree depth-layer width<=39, maximum-spine turning range[0,5], and last-parent jump bound29865 still permit arbitrarily long completed pristine record droughts in this actual finite family.

The quantifier remains UNIFORM ACROSS FAMILY MEMBERS. Every member captures. This does not construct one orbit with unbounded late ages, and it does not refute an eventual orbit-dependent bound or a stronger invariant retaining the full lifetime genealogy.
