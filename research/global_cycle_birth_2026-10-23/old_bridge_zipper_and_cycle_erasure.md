# Between cycle erasures, the live cursor zips along old bridges

23 October 2026, 22:21 UTC. Author derivation; independent audit requested.
This strengthens the separately frozen cycle-birth and logarithmic-renewal
notes. It is an arbitrary-word physical theorem, not standard104 capture.

## 1. Complete-state definitions and strongest statements

Use the paired diagonal BLACK graphs: an R inserts both edges, moving z and
keeping w fixed; an L deletes both edges, moving w and keeping z fixed. The
two edges at one physical cell are perpendicular planar duals. A **cycle
erasure** is an actual L whose deleted edge is a NONBRIDGE in at least one
of these two full current black graphs. Count that physical update ONCE even
if it erases a cycle in both graphs. No boundary crop or final-XOR graph is
used to determine whether an edge is a bridge.

**Old-bridge zipper theorem.** On any actual interval of entry mass m with
NO cycle erasure:

1. Every L crosses an edge that was BLACK AT INTERVAL ENTRY, was a bridge
   of the initial w-black component, and has not previously been crossed.
2. The w cursor follows a vertex-simple path through bridges of that ONE
   initial component. It never walks into a component newly attached by an R
   or into a newly written edge. Newly attached complete components remain
   physically behind, not forgotten or removed.
3. Every complete R^r L block has r<=2. All R-created black lifetimes remain
   current through the interval; no newly produced black lifetime is consumed
   before the next cycle erasure.
4. There are at most m L updates and at most 2m+4 R updates. In particular

       length <= 3m+4,       final mass <= 2m+4.      (1)

   The final possible run of four R's is included. Every actual mass-m state
   consequently has a cycle-erasing L within the next3m+5 updates.

The actual read edges remain incident to the simple initial bridge path of
w. The physical read CELLS lie within L1 distance one of that path;
head displacement across the interval is at most2m+2. This is a geometric
classification of topology-free transport, not just an endpoint count.

**Global renewal theorem.** On an ARBITRARY actual interval of entry mass m,
length T, and D cycle-erasing L updates, one has

       T <= 6*(m+3)*2^D.                             (2)

Thus for T>0,

       D >= log_2(T/(6*(m+3))).                      (3)

The bound may be negative on short intervals. Every finite-seed ant must
erase black cycles infinitely often, with at least logarithmically many
such actual updates in elapsed time. This is not positive density, does
not identify any cycle erasure with a nonstandard defect, and does not
bound the number of erasures by initial mass.

## 2. Local complete blocks and the stronger bridge inheritance law

Partition an interval into complete blocks R^r L plus a terminal R run.
Any actual R run has length at most four. In the w representation its R
prefix scans distinct consecutive ports at a stationary vertex. If r<=3,
the departing L edge e was already present at BLOCK ENTRY.

Let C be the actual active w-black component at block entry. Suppose e is
a bridge just before the L deletion. It was already a bridge of C. EVERY
new R edge stays on the OLD w side of this bridge: otherwise that new edge
would supply a bypass and e would not still be a bridge. This argument does
NOT require those R insertions to be bridges themselves; they may create
cycles on the departed side. Any external component attached by them is
likewise entirely on that old side.

After the actual L crossing, the active component is therefore EXACTLY the
far component of C minus e. It is a strict edge-subset of C, with at least
e removed. All newly written edges and imported components are left behind
with their actual colors and geometry intact. This is the causal invariant.

If r=3, the three R-written ports and the departing black fourth port make
a complete four-edge unit cycle in the OPPOSITE z graph. The L deletes one
of those cycle edges, so it IS a cycle erasure. If r=4, all four R-written
ports make the same opposite unit cycle, and the immediately forced L again
erases it. Thus any complete block without a cycle erasure has r<=2 and a
bridge L in the w graph.

## 3. Exact geometry and finite fuel before the next erasure

Iterate the stronger bridge inheritance through an erasure-free interval.
Every subsequent active component is obtained from the original one by
cutting off the old side of an INITIAL bridge. Added edges never enter the
retained far component. Initially nonbridge edges cannot become bridges in
this retained component: deleting bridges elsewhere cannot destroy their
original cycles. Hence every consumed edge really is an original bridge.

The old cursor vertex is excluded at each crossing and cannot be revisited.
All w moves form a vertex-simple path in the initial component; every R
stays at its current vertex. All new R edges at a departed vertex lie outside
the later retained components and cannot be addressed later during the
interval. Thus no new lifetime can be consumed. The terminal R run has no
following L in the interval and consumes no produced lifetime either.

At most m initial black edges can be spent. Each complete block has at most
two R's, and the terminal R run at most four, proving(1). Even if the entry
component has cycles, it cannot transport the cursor through one of them
without an erasing nonbridge L. Passive cycles on other components are
retained but cannot renew this zipper until a cycle erasure occurs.

## 4. Counting renewals on arbitrary trajectories

Call a complete block exceptional if r>=3 OR its L edge is a nonbridge in
the w graph. EVERY such block ends with a cycle-erasing L: for r>=3 use the
opposite unit-cycle argument, and otherwise use the w nonbridge directly.
If E counts exceptional blocks, then E<=D. A cycle-erasing L in the z graph
with r<=2 may be ordinary; leaving it unmarked only makes E smaller.

The E exceptional blocks separate ordinary blocks into E+1 epochs. Let M_j
be the COMPLETE actual black mass at epoch entry and n_j its ordinary block
count. Exact inheritance gives n_j<=M_j. An ordinary block has r<=2 and mass
increase r-1<=1; a whole ordinary epoch raises total mass by at most M_j.
The following exceptional block has r<=4 and mass increase at most three.
Consequently

    M_(j+1)<=2M_j+3,
    M_j<=(m+3)*2^j-3,
    sum_j n_j<=(m+3)*(2^(E+1)-1)-3*(E+1).

All abandoned or later reimported state is counted in these full masses.
There is no original-root budget on descendants and no reset at a renewal.
An ordinary block costs at most three updates, an exceptional one at most
five, and the terminal R run at most four. Therefore

    T<=3*sum n_j+5E+4
     <=3*(m+3)*(2^(E+1)-1)-4E-5
     <=6*(m+3)*2^E
     <=6*(m+3)*2^D,

proving(2). Setting E=0 recovers the sharper erasure-free bound3m+4.
The exact current bridge law, rather than mass descent or a finite component
summary, is what makes this a stateful global accounting theorem.

## 5. Concrete nonstandard transport and honest scope

The retained LRRL rod transport gives the exact nonstandard control described
in cycle_birth_or_finite_fuel.md: a2r-cell horizontal black row supports
(LRRL)^r for4r updates, shifts completely up one row, and keeps BOTH black
graphs forests at every fine cut. Every length-ten window is nonstandard.
The moving w simply consumes the original rod bridges while writing the new
row behind it. Its first cycle erasure is at time4r+5, after the forced final
RRRR square and L. Thus long topology-free transport need not look standard;
it spends actual old bridge input, and that input is finite.

After a cycle erasure, newly written or previously dormant state can become
active again. Repeated erasures are not restricted here; the standard highway
itself repeatedly creates and erases such cycles. Nor does the theorem show
which erasures are nonstandard or that their nonstandard subsequence ends.
The signed184-cell family and the nonmonotone bi-exterior return examples
remain fully compatible. Universal finite-seed capture remains open.
