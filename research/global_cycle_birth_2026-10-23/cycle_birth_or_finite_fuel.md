# Actual topology-free stretches have finite fuel

23 October 2026, 22:12 UTC. Author derivation; independent audit requested.
This is an arbitrary-word physical theorem, not a defect-count budget or a
proof of universal standard104 capture.

## 1. Statement

Use the two exact diagonal BLACK graphs of the paired-cursor model. A black
cell is an edge in each graph. The R update inserts both edges, with z crossing
and w staying; L deletes both, with w crossing and z staying. Call an R update
a **cycle birth** if its new edge closes a cycle in AT LEAST ONE of these two
finite black graphs. Equivalently the relevant graph's cycle rank rises by one.

At an arbitrary actual entry cut let m be the complete black mass and let
beta be the total cycle rank of the black graph containing the L-moving
cursor w. All initial components, not just the active component, count in beta.

**Theorem.** Every actual interval containing no cycle birth has length at most

    2*(m+1)*(3^(beta+1)-1)-1.                         (1)

Consequently a cycle birth occurs within the next

    2*(m+1)*(3^(beta+1)-1) <= 2*(m+1)*(3^(m+1)-1)    (2)

physical updates. Every finite-support ant has infinitely many cycle births
in the two graphs combined.

By the independently signed hull-growth lemma, EVERY such birth is an R on a
white physical cell INSIDE an existing current black rectangle hull. Thus a
long topology-free stretch cannot avoid an actual finite-hull reconnection
indefinitely. The reconnection is to an actually connected pair of endpoints
in one black graph, not a final-XOR connection or an invented causal wire.

If the w black graph is initially a forest, beta=0, so a no-birth stretch has
length at most4m+3. Other-graph initial cycles may be present; the beta=0
conclusion still holds. Constants are conservative.

## 2. Exact compressed block and the causal bridge law

Partition a no-birth interval into complete blocks R^r L and a terminal run
of R's. There can be at most three R's in ANY run: four consecutive R's insert
a black four-edge unit cycle in the z graph, on their fourth update.
Hence every complete block has r<=3 and at most four physical updates.

Throughout its R prefix, w stays at one vertex. The addressed edges are
distinct consecutive ports, so the departing L edge was already black at
BLOCK ENTRY, not created during that prefix. Every R edge is a bridge on
insertion, since a cycle birth was excluded. Thus each attaches a previously
separate complete black component to the stationary vertex w. No component
or passive field is discarded in this statement.

Let C be the actual active w-black component at block entry. Suppose the L
edge e is a bridge when removed. It was then already a bridge of C. The new
active component, after w crosses e, is EXACTLY the component on the far side
of C minus e. All components attached by the R prefix remain on the OLD w
side and are left behind. In particular

    E(active after) <= E(active at block entry)-1.    (3)

This is a chronological active-component assertion, not monotonicity of
total mass or total component count. The new R-written edges remain physically
present; they may be reimported later, but not by this bridge-departure block.

If the departing L edge is NONBRIDGE, it may retain the newly attached field.
However that deletion lowers the GLOBAL w-black cycle rank by exactly one.
R bridge insertions and L bridge deletions leave that rank unchanged. There
are therefore at most beta such nonbridge L blocks in the entire interval.
These are the only renewal events that can interrupt a sequence of the strict
active-component losses (3).

## 3. Quantitative accounting retaining the complete board

Let h<=beta be the number of nonbridge L blocks. They partition the bridge
blocks into h+1 chronological epochs. Let M_j be the COMPLETE actual black
mass at epoch j entry, and n_j its number of bridge L blocks, j=0,...,h.

Repeated use of (3) gives n_j<=M_j. A complete block has mass change r-1<=2,
so the bridge epoch raises total mass by at most2n_j<=2M_j. A following
nonbridge block raises it by at most two more. Therefore

    M_0=m,
    M_(j+1)<=3M_j+2,
    M_j<=(m+1)*3^j-1.                              (4)

This pays for ALL stored new edges, including those abandoned by earlier
bridge crossings and later reimported at a nonbridge renewal. No reset of
external components or their ancestry is used.

The total number N_L of complete blocks obeys

    N_L = h+sum_j n_j
        <= (m+1)*(3^(h+1)-1)/2-1
        <= (m+1)*(3^(beta+1)-1)/2-1.

Each has at most four updates and the final R run has at most three. Thus
T<=4N_L+3, proving (1). Applying (1) at any state after a hypothetical last
cycle birth contradicts an infinite remaining trajectory. This establishes
the global infinitude assertion without any eventual periodicity premise.

## 4. A long NONSTANDARD control: retained rod transport has no cycle births

The transport word itself is retained, not newly invented here: see
causal_reduction/unit_scale/axial_domino_transport.md, stage1. The new use is
the complete paired-forest/topology-free control.

For every integer r>=1 prepare exactly

    B_r = {(x,0):0<=x<2r},   head(0,0,E).

Then the exact physical word T^r, T=LRRL, executes for4r updates, finishing
at(2r,0,E) with COMPLETE board

    {(x,1):0<=x<2r}.

Every copied T reads (2i,0)L,(2i,1)R,(2i+1,1)R,(2i+1,0)L.
No supplied black cells are added during execution, and all old cells are
accounted for.

At every fine cut the black board is a union of two row intervals:

    upper row y=1: 0<=x<=a,
    lower row y=0: b<=x<2r,

where a<=b; either interval may be empty. Each single row is a simple zigzag
path in either diagonal black graph. Their possible common vertices lie on
y=1/2. In one graph these vertices pair the physical columns{2k,2k+1}; in
the other they pair{2k-1,2k}. Because a<=b, the two row paths have AT MOST ONE
common vertex in each graph. Their union is a forest. Thus there are no cycle
births in EITHER graph at ANY fine cut, and every cut is bi-exterior.

The four cyclic length-ten words of T-infinity are

    LRRLLRRLLR, RRLLRRLLRR, RLLRRLLRRL, LLRRLLRRLL.

All four lie outside the standard104 ten-factor set. Thus every wholly
contained ten-window of this arbitrarily long topology-free transport is
nonstandard; for4r>=11 it has exactly4r-10 wholly contained adjacent-bad-ten
windows. Topology-free evolution does NOT force a standard local pattern.
The entire finite prepared rod is consumed as input and shifted, with mass
m=2r; this is not a fixed-mass construction or an infinite finite-seed orbit.

In fact the next four turns are RRRR and their fourth update is the FIRST
cycle birth, at time4r+4. The new four-square is below the just-shifted rod.
It has no earlier black-edge connection capable of closing either graph;
the fourth edge closes its z unit cycle. Hence a mass term is essential in
any waiting-time bound even on paired forests. The linear order of the
beta=0 theorem cannot be replaced by a constant independent of mass.

## 5. Relation to the global capture gap

The result does NOT bound cycle births by original mass. Standard104 itself
can create and erase cycles repeatedly, and the signed184-cell construction
has unbounded nonstandard complexity across spatially growing finite seeds.
Equation(1) only bounds ONE actual interval during which no new cycle forms.

Nor is an inside-hull cycle birth proved to be a defect, a standard motif,
a fresh-root merger, or a decrease of any capture rank. A long nonstandard
forest transport can use old fuel without any internal episode, as above.
The new global causal restriction is that pure bridge growth and bridge
crossing cannot renew their own active supply forever: either an actual
stored cycle is spent, or a new cycle must be written within the explicit
bound. Classifying the sequence of genuine renewals remains open.
