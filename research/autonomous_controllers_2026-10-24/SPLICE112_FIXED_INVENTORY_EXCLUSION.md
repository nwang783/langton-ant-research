# A failed 112-event constructive splice, including all local orders

24 October 2026. Author exact finite-domain certificate, not yet independently
reviewed. This is one explicit constructive target, not a growth-eight theorem.

## Complete target and its scope

The candidate has actual full drift (2,-2), 25 occupied quotient classes, 112
reads and growth 12. Representatives have x=0 or 1, and t=x+y ranges from -1
through 11: its complete read height is 13. The two lanes of its proposed lower
five rows have incoming-heading histories

    (W, empty), (N, SS), (WE, WWE), (SNNS, SSNS), (EEE, WWEEWW).

All higher histories are the supplied standard104 complete histories with
original t>=2, translated physically by (1,1) and reduced by the FULL drift.
The exact 26-class list, including the one empty class, is in
`probe_standard_upper_splice112.json`. WHITE gives R,L,R,L,... at each nonempty
history. Every directed incoming/outgoing physical port total matches.

The proposed ordering nevertheless splits its exact ordinal event permutation
into a 104-event component of winding +1 and an eight-event component of winding
zero. The latter is already impossible, since summing actual successor clock
identities would force 8=0. Its complete lifted path is retained in the JSON.
Neither this consistent-port list nor its 104-event component is a physical
front, finite factor, or finite-seed controller.

The stronger question was whether a coordinated change of chronological order
at ALL 25 classes could repair the splice, preserving only the exact count of
each (incoming heading, R/L) event type at every physical drift class. It cannot.

## Exhaustive all-order certificate

At each cell distribute its fixed positive-heading R and L counts independently
over the even and odd read ranks. This enumerates every complete WHITE history
with the supplied inventory. The local option counts, in (t,x) order, are

    1,1,1,1,2,4,2,1,9,3,1,24,6,24,18,12,100,3,1,9,1,2,2,1,1.

Their product is 3,482,851,737,600. No arbitrary visit cap is imposed: the counts
are those of this one finite proposed inventory. The 112 actual physical
outgoing-port ordinals are the clock variables.

For a selected local history, the kth incoming crossing is matched to the kth
outgoing crossing at the physical predecessor, with full drift time offset.
If that predecessor is r+a*d and P=112, its read clock at the target is
X_in+1+a*112=X_out. Adjacent complete reads at a physical cell have gap at least
four. Both equality directions and these rank inequalities are retained.
This is exactly the already signed fixed-inventory clock encoding, with this
new inventory and P=112; the prior standard uniqueness conclusion is not used.

The certificate takes sound common inequality bounds over the current domain
at each cell, then tests each candidate option by adjoining its own bounds.
Each deletion has an explicit positive closed difference-constraint cycle.
Six propagation rounds delete 1,3,4,5,22,6 options, respectively. All nine options
at class (1,2) are thereby eliminated. There is one proof-tree node, 41 explicit
option deletions, no branch, no feasible leaf, no solver UNSAT premise and no
unfinished timeout. An independent checker need only rebuild the finite options
and verify the supplied cycle edges and positive sums; it need not run a search.

Therefore no complete WHITE translating front has this exact full directed
event inventory. Unread fields cannot repair an impossible clock identity.
No conclusion follows for another inventory, added events, or omitted classes.

## Comparison with the retained short-detour theorem

A direct count comparison shows that this full inventory is precisely the
standard inventory translated by (1,1), plus eight extra event occurrences.
Thus it is closely related to the retained eight-step pose-return detour family
in `../causal_reduction/front_surgery/eight_step_detour_finite_fuel.md`.
That theorem fixes the actual standard backbone order and inserts short
pose-return words. The present check did NOT impose that order, a deletable
backbone, or an actual eight-step insertion. We do not claim a general extension
of the old theorem, nor novelty relative to published literature.

## Files

- `probe_standard_upper_splice112.py/json`: exact proposed inventory and both
  event components, including the eight-event zero-winding obstruction.
- `search_splice112_inventory_clock_tree.py`: complete local-order domains and
  proof-producing clock propagation.
- `splice112_inventory_clock_tree.json`: one-node explicit rejection certificate.
- `SPLICE112_SHA256SUMS`: frozen direct and transitive dependency hashes.
