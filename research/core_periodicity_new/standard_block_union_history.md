# Complete-history union approximation and reverse-front fuel

Status: independently reviewed on2026-10-22 at20:00 UTC. The auditor independently recomputed all104 phase guards, all39 helpful rail profiles and1024 white-error subsets, first-L bound22, endpoint-mask bound44, and the geometric width bounds, and approved the endpoint/crossing-band argument. See ../audits/check_reverse_union_independent.py/json. This document does not assert global capture, bounded standard-block count, or bounded nonstandard time.

## 1. Standard blocks erase only bounded entry supply

A standard block is any positive integer power of a cyclic phase of W, executed with its actual entry pose. For the canonical phase, an exact finite seed of13 cells realizes W forever. For any phase, evolving that seed fewer than104 updates gives a sufficient seed of mass at most117. Consequently every legal finite standard block touches at most117 cells that were black at its entry: each such cell must have first requested letter L, and all first-L requirements lie in that sufficient phase seed.

The exact phase data sharpen117 to22. In each drift orbit, all but finitely many first reads are the first read in the bilateral period order, and that letter is R. The coordinate spread within every drift orbit is at most3 periods. Hence every exceptional first-L cell occurs within the first four periods. Literal first-read enumeration for all104 phases gives maximum22. This does not assume that the arbitrary actual entry field is the canonical seed; the first-read colors are forced by the prescribed word.

## 2. UNION, not an unverified XOR background

Let B be the actual field and U an auxiliary union. For a legal standard block with odd write set O, update

    B' = B xor O,             U' = U union O.

Outside O the discrepancies are unchanged. On O, U' is black, and B' is white exactly where B was black. Thus the new discrepancies on O number at most22, by Section1. It follows that

    |B' symmetric_difference U'| <= |B symmetric_difference U| +22.

A single other physical update increases the discrepancy by at most one if U is left unchanged.

Start U at the initial black set. After a complete physical history partitioned into r legal standard-power blocks and D other individual updates, the actual field differs from the union of the initial field and all block odd masks by at most22r+D. Removing the initial set from that auxiliary union costs at most its cardinality m. Therefore

    |B symmetric_difference union_i O_i| <= m+22r+D.

This is an exact complete-history estimate. It does not assume disjoint block footprints, clean crossings, permanent detachment, or physical realizability of arbitrary XOR-superposed rails.

## 3. Uniform endpoint coboundaries

For each cyclic phase let O be its one-period odd write set. Partition O into drift orbits. Choose one representative q in each of its twelve odd orbits, all with global x-coordinate0 or1, to obtain a12-cell tile Q. The orbitwise even set O xor Q has a finite one-dimensional antiderivative P, giving

    O = Q xor P xor(P+d).

The exact construction is recorded for all104 phases in standard_block_union_data.json. It gives |P|<=44, and both coordinate widths of Q are at most11. Spatial rotations preserve these bounds. The coordinate widths of every cyclic standard period's read footprint, and hence every reverse period's read footprint, are at most9.

For a block of n periods, telescoping yields

    O_n = (union_{0<=j<n}(Q+j d)) xor P xor(P+n d).

The Q translates are disjoint because Q has exactly one representative per drift orbit. Each full block odd mask therefore differs from its finite12-cell-per-period rail by at most88 cells.

Replacing all O_i in the auxiliary union by their finite rails changes at most88r cells, even if rails overlap. Combining with Section2 gives a finite-rail union U satisfying

    e := |B symmetric_difference U| <= m+D+110r.       (1)

Every rail's writer has the actual ant's invariant sector, since it was a real standard block in that history.

## 4. Finite endpoints and perpendicular rails cannot be discarded for free

Suppose the current state executes N full reverse-complement104 periods V, in the same sector as all prior standard writers. In each of the22 drift orbits of V, choose the phase of maximal longitudinal coordinate and earliest tie. Its read in each period is a first visit within this factor. These22N witness cells are all distinct.

For one prior finite rail parallel to the reverse drift, membership of these witnesses in that rail is described, for each matching orbit, by an interval of period indices. All interval starts differ by at most10, and all ends differ by at most10: the relevant coordinate widths are at most11 for the old tile and9 for the reverse witness set, and the drift changes that coordinate by2. Outside at most20 index positions in the two endpoint transition bands, this rail contributes either its entire bilateral orbit profile or nothing to the22 witnesses.

For a perpendicular prior rail, use the linear coordinate x+y after rotating the reverse drift to(2,2). That coordinate changes by4 per reverse period but is constant along the perpendicular rail's drift. The old tile has x+y width at most22 and the witness set width at most18. Hence at most11 integer period indices can have any witness on that perpendicular rail, regardless of its length or age.

Thus, conservatively, deleting at most32r period indices handles ALL endpoint transition bands and perpendicular crossings. On every remaining index, the finite union U has exactly the22-bit profile of a union of bilateral parallel same-sector standard wakes. The separately checked guard enumeration says this profile differs from V's required first-read colors on at least four classes.

Since the actual entry board B must match all first-read requirements, each such mismatch is a distinct cell of B symmetric_difference U. Hence

    4 max(0,N-32r) <= e.

Using(1), including the trivial case N<32r, gives the complete-history bound

    4N <= m+D+238r.                                  (2)

## 5. What this would and would not establish

Bound(2) prevents unbounded reverse104 defect production merely by increasing the lengths/ages of a fixed number of earlier standard flights while keeping the initial mass and number of other updates bounded. It retains all prior history through the exact discrepancy estimate and explicit endpoint bands.

It does NOT prove that D or r is bounded along arbitrary finite-seed orbits. Nonstandard activity can create new off-rail supply; a different nonstandard return word is not covered. No descent of the global K-renewal map follows from(2) alone. The result is a directed supply constraint and a possible component of a future rank, not that rank itself.
