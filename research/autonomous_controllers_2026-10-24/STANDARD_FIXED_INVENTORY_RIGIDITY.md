# Complete causal-order rigidity of the standard104 quotient inventory

24 October2026. Author theorem with a transparent exhaustive clock certificate,
awaiting independent audit. An exploratory SMT run suggested uniqueness, but
its UNSAT status is NOT a proof dependency of the certificate below.

## 1. Exact classification scope

Normalize the retained104 word W to initial headingN, so its full drift is
 d=(-2,2). Quotient physical cells by the FULL vector d, choosing representatives
with x in{0,1}. Trace one W period. At each of its22 occupied quotient classes,
retain the exact count of each event type

    (incoming compass heading, R or L).

Equivalently retain the actual directed incoming/outgoing port pairing counts
at every class. No cell class is deleted or added and no event type is added,
deleted, or converted. The complete invariant data are in the companion JSON
and can also be reconstructed directly from W. Their sum is104 events; the
largest local multiplicity is10, because that is W's supplied inventory, not
an independently chosen global cap.

THEOREM: Every COMPLETE WHITE translating front with period104, full drift
(-2,2), and exactly this quotient event inventory has the SAME complete ordered
incoming-heading history at every physical cell as the standard front. Hence
its actual successor orbit is standard104, up to temporal phase. Translating
and properly rotating the WHOLE inventory transports the conclusion. Reflection
or reducing d to its primitive vector is not invoked.

This covers coordinated local reorderings at ALL22 classes, not just one-pose
excursion surgery. It does not classify a different event inventory, width,
period, drift, or arbitrary finite-seed nonperiodic behavior. Unread external
black debris does not enter these read histories and is not erased by the proof.

## 2. Finite local alternatives, with no chronological orders omitted

At a class with n reads, WHITE input fixes the turns at ranks j=0,...,n-1 to
R,L,R,L,... . Its incoming headings have one fixed axis, so two possible signs.
For each of R and L separately, distribute the inventory's fixed heading counts
over the ranks having that turn. This exhausts every possible ordered history.

In lexicographic representative order the domain sizes are

    1,2,1,1,100,18,6,1,9,2,1,1,2,9,3,12,24,24,3,1,2,1.

Their product is870712934400. These are local orders of the SAME finite given
inventory, not870 billion simulated seeds or possible arbitrary ant programs.
The known standard ordering occurs in every domain and is retained as a control.

## 3. Exact physical ordinal-port clock encoding

Use one integer variable X_(e,k) for the actual departure time of ordinal k on
physical directed edge e whose source is a chosen quotient representative.
Every directed edge's total crossing count is fixed by the supplied event
inventory, so there are exactly104 such variables. For every local history
option, order each incoming and outgoing physical port by the complete local
read rank. Match the kth outgoing occurrence on a physical edge to its kth
incoming occurrence. This is literal chronological edge matching, not a
free permutation or a modulo-P rank shift.

If a cell's representative is p, an incoming edge comes from
r+a*d=p-unit_heading, where r is the predecessor representative. Its read time
at p is X_in+1+a*104. Its outgoing edge variable X_out at that same read is
therefore constrained by

    X_out-X_in = 1+a*104.

Both directed difference inequalities for this equality are retained. Between
two consecutive reads at the SAME physical cell, require a positive return gap
of at least4. In terms of the two incoming-edge variables this is

    X_in,next-X_in,previous >=4+(a_previous-a_next)*104.

The four-divisible gap fact follows from alternating movement axes and zero
net coordinate displacement; heading restoration is not assumed. The certificate
uses only the inequality>=4, not an unproved stronger bound or a visit cap.

Every genuine complete WHITE front with this inventory supplies an option at
each class and values satisfying all these equalities and inequalities. All
full-drift time offsets and both port ordinals are explicit in the generator.

### Why the encoding does not admit several hidden ant orbits

After choosing all local options, every read has exactly one predecessor and
successor: within a class use its selected incoming/outgoing pairing, and
between classes use the fixed physical port ordinal. Thus the104 reads split
into directed cycles. Sum the exact one-step clock equations around a cycle
of length ell. One obtains ell=104*k, with integer translation winding k.
Since1<=ell<=104, necessarily ell=104 and k=1. There is only ONE event cycle,
not several ants, a finite zero-winding loop, or an incorrectly stitched set
of independent controllers. Its physical lift advances by d in104 actual steps.

The ordered local clock inequalities are precisely its complete physical
visit order. WHITE rank parity then makes the actual turn sequence legal.
The retained finite-overlap construction supplies a finite seed if needed.
A common additive clock gauge is irrelevant. The exploratory SMT variant fixed
one local first clock to0; the transparent proof has no gauge-dependent premise.

## 4. Transparent exhaustive certificate, independent of SMT

Represent every option's clock implications as directed inequalities
X_v>=X_u+w with integer w. A directed cycle with positive total w is impossible.
At a finite-domain node, take every ordered variable pair appearing in EVERY
remaining option at a given class, with the MINIMUM stated bound over those
options. Those common bounds are valid regardless of which option is chosen.
Combine all classes' common bounds, keeping the strongest available bound for
each ordered pair.

For an option under test, add all its own bounds. If a positive cycle occurs,
record its exact edges and weights and delete that option. Every edge must be
an available common bound or an implication of that tested option. A verifier
checks the closed edge chain and positive integer sum directly; it need not
trust the producer's Bellman-Ford search or any solver. Recompute common bounds
and repeat sound deletions. If no deletion is possible, branch on one remaining
finite domain and cover EVERY one of its options. An empty domain or an explicit
positive cycle closes that branch.

The supplied COMPLETE proof tree has only NINE nodes: four infeasible leaves,
one complete feasible leaf, and four branch nodes. Across its nodes it gives265
option deletions, each with its own explicit positive-clock-cycle witness.
The unique remaining complete option vector is exactly the standard one.
There is no unresolved/timeout leaf. The JSON is about39KB, not an opaque log
of the enormous raw Cartesian product.

Files:
- certify_standard_inventory_by_clocks.py reconstructs the option inequalities.
- exhaust_standard_inventory_clock_tree.py generates the finite proof tree.
- standard_inventory_clock_tree.json stores every node, propagation deletion,
  cycle witness, branch cover, and the unique leaf.

The producer's elapsed-time ceiling was never reached. Completion is certified
by the closed finite branch tree, not by elapsed time, absence of examples, or
the exploratory SMT status.

## 5. Literal positive model and all-future check

The sole SAT clock model was materialized rather than assumed equivalent to W.
Its104 clock residues are all different. They yield one literal compass path,
heading-restoring drift(-2,2), and exactly cyclic phase71 of W. The reconstructed
finite-overlap seed has19 black cells, starts at(0,-7), headingW, and passes
computability/periodic_tail_checker.first_mismatch with NO future mismatch.
Three literal periods on the full growing board are additional controls, not
the infinite proof. Complete word, seed, times, ranks, positions and headings
are in standard_inventory_positive_model_certificate.json.

Thus all surviving histories do produce the known physical standard ant. No
unreplayed alternative SAT model exists in this run. This completes classification
ONLY within the fixed supplied quotient inventory.

## 6. Remaining conceptual gap

The result says coordinated causal-order surgery cannot create another WHITE
controller while preserving this standard event inventory. A genuine alternative
must change that inventory, not merely reorder its local read types. The earlier
prepared-wave root graphs and finite mixed joins show why first/last structure
or output count alone cannot force the inventory to be standard. Establishing
that stronger premise, or constructing another inventory with a valid connected
WHITE event cycle, remains open.
