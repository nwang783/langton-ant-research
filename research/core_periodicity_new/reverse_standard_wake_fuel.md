# Directed supply obstruction for reverse-standard104 fronts

Status: independently reviewed on2026-10-22 at20:00 UTC, including all104 cyclic phases, the deficit7, and the UNION deficit4. The complete-history finite-rail extension in standard_block_union_history.md is also independently reviewed. No global renewal rank, finite-seed mass bound on arbitrary future debris, or no-counterexample theorem is claimed.

## 1. Why examine this mechanism?

A long ordinary standard flight can create an arbitrarily old wake from a fixed-size seed. A hypothetical fixed cap that launched a reverse-complement104 front along that wake could recycle its black supply and emit arbitrarily many adjacent bad-ten pairs at fixed initial mass. The reversed period V has62 bad-ten windows and52 adjacent pairs per104 turns. Exact time reversal changes the invariant parity sector, so an actual single ant would need a spatially offset recycler instead. The results below exclude that exact offset reverse-word mechanism on clean own-wake supplies.

## 2. Canonical drift-orbit data

Use N,E,S,W=0,1,2,3. The supplied canonical W starts west, has length104 and drift d=(-2,-2). Its bilateral settled wake T is the XOR of all translated read positions p_i+k d, i=0,...,103 and k in Z. Drift orbits are keyed by

    (t,a) = (x-y, x mod2).

The twelve black classes are

    (-3,0),(-3,1),(-2,1),(-1,0),(0,0),(1,1),
    (2,0),(3,0),(5,1),(6,1),(7,0),(7,1).

Put V=complement(reverse(W)). It has drift -d=(2,2) when started east. The natural exact-reversal start is q0=(-1,-2), the last W read point. The asymptotic first-L orbit classes of V, translated by q0, are exactly the twelve classes of T. Its remaining ten read-orbit classes require white on their first reads.

For an orbit of V read points, write a point as a fixed representative plus k(-d). Its earliest read at any remote cell maximizes 104k-i among the phases i in that orbit. Equivalently choose maximal k, breaking ties by earliest phase. This phase supplies the first-read color guard.

## 3. Seven off-rail black cells per full reverse period

Write an arbitrary reverse-front start as q0+s, using the corresponding eastward heading. The invariant sector is (-1)^(h-x-y). The natural reversal has the opposite sector from the writer. Therefore a reverse front in the writer's own sector requires sx+sy odd, equivalently delta=sx-sy odd.

Translating the twelve required-L classes shifts t by delta and a by sx mod2. The finite exact autocorrelation table in reverse_wake_guard.json shows that every odd delta, with either parity shift, leaves at least seven required-L classes outside T. Only offsets with |delta|<=10 can overlap the transverse support at all; outside that derived finite range all twelve are missing. The minimum seven is attained for delta=+1 or-1.

For EACH missing class, take its first-read phase as above. In N full copies of V, that phase reads N distinct cells that have no earlier visit within the factor. There is no burn-in loss: maximal longitudinal coordinate makes every competing visit occur in the same or a later period, and the tie-breaking phase is the earliest in its period. All seven classes are disjoint and lie outside T. Hence any entry field B that executes this factor must satisfy

    7 N <= |B outside T|.

More generally, if B is contained in T union E for a finite exceptional set E, then 7N<=|E|. Missing black cells inside T cannot help the lower bound. Thus the same bound applies to arbitrarily long finite pieces of the clean rail, with arbitrary holes, plus finitely many off-rail black cells.

Cyclic phases transfer by changing the entry cut and applying the corresponding phase pose. Rotations transfer both writer and reverse front together. The independent checker is verifying these phase transfers directly as a finite control.

Crucial scope: |B outside T| is measured at the reverse factor's ENTRY, not at the original initialization. Arbitrary prior nonstandard activity may have created unbounded off-rail supply. The theorem does not assume otherwise.

## 4. A stronger UNION guard obstruction

Normalize a same-sector reverse front to q0+(0,-1). Its twelve required-black and ten required-white orbit classes are listed in reverse_wake_union_guard.json. Consider any UNION of bilateral standard wake rails written in the same invariant sector, with either of the two directions parallel to d. A translated canonical rail has even transverse shift; the opposite writer orientation negates t. The finite list includes every shift whose black profile meets one of the twelve required-black classes. Rails meeting no required-black class cannot improve agreement and can be discarded for minimization.

Every listed rail that supplies any required-black class also contaminates at least one required-white class. In fact every union disagrees with the22-bit first-read guard on at least FOUR classes.

The finite exhaustion has only1024 cases, one for each possible allowed subset A of the ten white-error classes. For that A, include every rail whose white-error set is contained in A. This maximal union cannot introduce a new white error outside A and maximizes black coverage, so it dominates every union having precisely those allowed errors. Direct enumeration gives minimum four. This is a finite proof by complete guard enumeration, not a bounded spatial search: the offset range is derived exactly from the finite transverse supports.

Consequently, against any such bilateral UNION background U, a legal V^N factor requires at least4N corrections on distinct first-read cells:

    |(B symmetric_difference U) intersect first_read_witnesses| >= 4N.

This assertion is meaningful on the factor's finite read set even when U is infinite. Finite rail endpoints require separate accounting and have not been silently discarded.

UNION is essential. A formal XOR of ten oppositely oriented same-sector rails can match the reverse guard. No legal construction of that overlapping XOR background has been shown. Arbitrary physical histories are not assumed to leave either a union or an independently prescribed XOR of clean rails.

## Reproduction

- reverse_wake_guard.py/json: exact drift classes, first-read order, sector offsets, and bad-window counts.
- reverse_wake_union_guard.py/json: all finite parallel-rail guard profiles and1024 maximal-union cases.
- standard_block_union_data.py/json: separate prospective complete-history bridge, with all104 cyclic phases; its analytic use is recorded in standard_block_union_history.md.
