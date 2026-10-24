# Supplier geometry for the remaining cap-three G-only spine

22 October 2026. Analytic proof independently reviewed by the proof-certificate auditor on 22 October 2026. This narrows the location of same-heading triples but does not exclude them.

## Setting

Use the already reviewed cap-three consequences: after a finite prefix there are no completed B decorations and no L4 runs. Consider a sufficiently late maximal G decoration of the spine, whose entire finite footprint misses the finite initial support and initial head. Its base is R4. A G_R packet therefore has even depth, and a G_L packet odd depth.

The parent sign is opposite the packet sign. Just before the packet the parent reads its root p, moves to the child root w, executes G, and after its return reads w with the parent sign before entering its other child. The packet reads p once at its last boundary and w once at entry.

## 1. Fresh and supplied sides

Each interior column of a G ladder has one cell whose in-packet reads are R,L and one whose in-packet reads are L,R. Under cap three and white initial input:

- The R,L cell has no earlier read at all. Two earlier reads would make the displayed L the fourth read.
- The L,R cell has exactly one earlier R. Its displayed R is the third read.

Call these the fresh side and supplied side. A supplier R at a supplied-side cell cannot use its vertical edge into the adjacent fresh-side cell before the packet. Thus it uses the edge away from the strip. This fixes its incoming heading.

For a normalized east-going G_R rooted at (0,0), heading north, the fresh side is the upper row y=0 and the supplied side the lower row y=-1. At odd interior columns the supplier R arrives northward from below and moves east; at even columns it arrives eastward and moves south. Consecutive odd/even suppliers are therefore consecutive R reads of the earlier trace.

For a normalized west-going G_L rooted at (0,0), heading north, the fresh side is the lower row y=-1 and the supplied side the upper row y=0. At odd distances from the root, the supplier R arrives westward and moves north; at even distances it arrives southward and moves west. Consecutive even/next-odd suppliers are consecutive earlier R reads.

In either case, the supplier's incoming heading is opposite that of the in-packet third R. Every interior third-R event is consequently an opposite-heading triple.

## 2. Near-boundary cells

For a G_R decoration, the parent reads L at p immediately before entry and L at w immediately after return. The entry R at w is therefore its first read. The packet's last R at p is its third read. The middle L at p and final R enter p in opposite directions. If p's first R shared its final incoming heading, that first R would move into w, contradicting w's freshness. Thus this boundary third R is opposite-heading.

For a G_L decoration, the parent reads R at p before entry and R at w after return. The packet's final L at p forces the preceding parent R there to be its first read. The entry L at w is its second read, and the parent R after return its third. If w's first R shared that third R's heading, it would arrive from p before p's first read. Thus this boundary third R is also opposite-heading. It occurs immediately after the packet, rather than inside it.

## 3. Far endpoints

The two far endpoints are read once each, consecutively, with turns R,R. Their immediately preceding R in the central R4 block lies on the fresh side (or is the fresh root for depth zero); their immediately following R lies on the supplied side, or is the already treated predecessor p in depth zero.

Suppose one endpoint's displayed R were a same-heading third R. By the reviewed triple-edge pairing theorem it belongs to a consecutive RR pair of same-heading third reads. Neither exterior neighbor can be its mate: the preceding R is first, and the following R is opposite-heading third. Therefore its mate would be the other far endpoint.

The first endpoint of that pair has the same incoming heading on its first and third R. Its first R would thus have to arrive from the fresh-side predecessor before that predecessor's first read, impossible. Hence any far-endpoint third R is opposite-heading as well.

## Consequence

Every third-R event inside a late G decoration, and every boundary third R caused by returning from it, is opposite-heading. Therefore a same-heading triple-edge pair can have its final RR passage only on the undecorated core, in an R^2 syllable with no intervening G decoration.

This does not show that such core pairs are impossible. The core may revisit physical points through different lifted cosets. Nor does it allow deletion of the G packets: their supplied-side cells can obtain their earlier R reads through arbitrarily remote portions of the past trace.

## 4. Earlier passages of a same-heading pair

Added 22 October 2026 at 21:59 UTC; independently analytically reviewed,
including the column/heading correction recorded below.

The same pair's middle passage is also localized to an undecorated core
L^2 syllable. Its first passage is localized to an undecorated core R^2
syllable or the two far endpoints of a G decoration.

To see this, rotate coordinates so the directed triple edge runs east from
u to v. The ordered incoming headings are

    u: N, S, N;       v: E, E, E.

The three passages are consecutive RR, LL, RR. On the middle LL passage,
the source's first and middle headings must be opposite, and the target's
must be equal.

Any LL wholly within a G ladder is on its supplied or fresh side. A
supplied-side cell has its third R inside the packet, already proved
opposite-heading, so cannot belong to this pair. On the fresh side, the
LL source has equal first-R and second-L headings, while the target has
opposite headings. The source alone contradicts the required pair type.
This includes the near endpoint: for G_L, the last LL consists of the
fresh-side cell and its predecessor p, whose first R was the preceding
parent read. The same source-heading obstruction still applies.

An LL cannot straddle a G packet boundary: the adjacent parent read has
the opposite sign from the packet's boundary sign. Therefore the pair's
middle LL is wholly on the core. Its two consecutive letters cannot
have a decoration between them, so it is an undecorated L^2 syllable.

For the first RR passage, an RR on the supplied side cannot qualify,
since those are already third reads. An outward RR on the fresh side
has source first-R and later second-L headings equal, again incompatible
with the same-pair source. At the near end of G_R the root's R and its
parent-return L have equal headings, so this argument includes the
root. At a G_L boundary, the parent R after return is a third R, not a
first R. Consequently the only remaining in-packet location for the
first passage is the central pair of far endpoints. Outside packets,
the first RR passage is an undecorated core R^2 syllable.

This statement does not assert that any of these remaining locations is
realizable, nor that the locations contradict one another. Different
lifted core vertices may project to the same physical pair of cells.

### General heading table for the passage localization

Normalize G_R to travel east from its north-facing root. For every fresh
upper-row LL pair directed west, the source is an even column with
first-R/second-L headings N,N, and the target is the preceding odd column
with headings E,W. Normalize G_L to travel west. For every fresh lower-row
LL pair directed east, the source is an odd distance from the root with
headings S,S, and the target is the preceding even distance with headings
W,E. The distance-zero target is the parent predecessor and has those same
headings. In both cases the source is equal and target opposite, whereas
a same-heading triple-edge pair requires source opposite and target equal.
The outward fresh-side RR pairs use the same parity class of source,
not the same physical pair reversed: G_R goes from even x to odd x+1,
while the fresh LL goes from even x to odd x-1. G_L likewise has an
odd-distance source for both fresh RR and fresh LL. Thus each outward
RR source again has equal first/middle headings.
