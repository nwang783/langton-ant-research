# Exact reverse-rail periodic-front criterion

Status: exact reduction and bounded enumeration, not independently audited.
The rail is an infinite periodic input medium, not a finite black seed. The
purpose is to test a proposed reusable transfer primitive, not to claim a
counterexample to finite-seed attraction.

## Interface problem

Let D(x,y) be black on all of rows y=0 and y=-2 and on odd x in row y=-1,
and white elsewhere. Let S(x,y) be black only on odd x in row y=-1.
A westgoing front has a heading-returning turn word w and displacement (-p,0),
with p>0. It reads D before arrival and leaves S after departure, allowing a
finite moving interface defect. We ask separately in the two conserved pose
sectors sigma=x+y+h modulo two.

Every such front has even p. The ant's heading-returning period has even
length and hence even position displacement parity. Its net black-mass
change over one advancing interface period is -2p: two solid rows of length
p are removed, the odd middle row is unchanged, and the translated finite
interface defect has no net change in cardinality. Therefore

    count_R(w)-count_L(w)=-2p.

This is a necessary pruning condition, not the full criterion.

## Necessary and sufficient chronology test

Trace the finite word w at its proposed heading and vertical placement.
Group read events by the physical cell classes modulo (-p,0). The class key
is (x mod p,y); write each read coordinate as its chosen representative plus
an integer multiple r of (-p,0). Sort events in each class by descending r,
then by phase in w. These are the chronological reads of a fixed physical
cell by all translated periods.

For every class touched, its sorted turn letters must be the alternating
sequence beginning with that class's D color. Its final color must be its S
color. In addition, every class where D differs from S must be touched. Since
D and S are p-periodic, this is exact and finite. Equivalently, the odd-visit
classes must be exactly all p residues in rows 0 and -2, and every class's
read sequence must begin with D and alternate.

Necessity follows from the chronology of any front arbitrarily far from its
finite startup defect. For sufficiency, install the interface state at a cut
of the bi-infinite translated event schedule: untouched-ahead cells have D,
finished-behind cells have S, and the finitely many cells with reads on both
sides of the cut have their parity-determined intermediate colors. All reads
then occur with the specified colors, and the cut state translates after w.
No simulated finite horizon is being extrapolated.

## Exhaustive bounded-period implementation

`search_reverse_rail_fronts.py` enumerates every binary necklace for each even
period. Cyclic rotation merely changes the front's phase, so no distinct
periodic geometry is discarded. It keeps axial nonzero displacements, rotates
the initial heading to make the drift west, and tests all vertical placements
whose footprint reaches both required solid rows. There is one such heading
for each nonzero axial drift. For each sector, the initial horizontal parity
is forced by x+y+h=sigma. Even horizontal translations preserve the input and
output rails, so no further horizontal placement is needed. The check above
is then applied literally to all read classes.

Through period28 the only front words found are the first three powers of
RLLRLLLL, which is a cyclic phase of the known D=RLLLLRLL reverse sweep.
They all have sector1. Thus the complete tested class has no sector0 front.
This does not exclude longer-period fronts or aperiodic reverse transfer.

The sector1 D front is a positive control. No assumption about the five-macro
language, low mass, module lifts, bounded retreats, or standard highways is
used in this enumeration.
