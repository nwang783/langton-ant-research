# Finite-root mass growth and collision-free square-root packing coexist

23 October 2026. Explicit countermodel to a specified GLOBAL residual-resource
relaxation. This is not an ant orbit, not a literal DCUV packet ledger, and
not the physical cursor-token forest of audit LE.

## 1. The exact limitation

For recurrent-eight physical factors the signed theory supplies, among other
facts, residual mass at least r0+3k and an entry-root box radius
floor((2k+13)/3). It is tempting to expect that a finite spatial arrangement
of roots, simultaneous branching and eventual overlap of root boxes forces
collisions that a single-lineage bound misses.

Those numerical/resource premises alone do not force collision. The model
below starts with FIVE fixed roots, has EXACT current mass 5+3k after k
updates, positive produced-parent age at least five, parent/output distance
at most two, plain ancestry speed at most 2/5, and distinct current identities
at all times. Its entire support is within O(sqrt(k)) of its finite roots.
All ancestry displacements are coordinatewise nonnegative, different root
colours never merge, and no collision resolution is used.

The model intentionally omits literal simultaneous multi-input demands,
packet output masks, full 272-role potential inequalities, forced white
contexts and the single head's chronological path. Therefore it does NOT
refute any theorem retaining those stronger physical requirements. The new
point is that adding GLOBAL finite-root packing to the mass/age/box relaxation
still does not close it. The missing coupling is not merely root-box overlap.

## 2. Cells, active identities and immutable buds

More generally fix any integer q>=5. A macro-cell (i,j), i,j>=0, has anchor

    a(i,j)=(2i,2j).

Initially the q anchors a(0,0),...,a(q-1,0) carry active root identities.
They are put in a FIFO queue in increasing i order. All other cells are empty.
There are two reproduction rules. Each consumes the first active identity
at its anchor and installs FOUR NEW identities, after retiring the input.

Vertical rule, used whenever j>=1 or i<q-1:

    active output: a(i,j+1),
    immutable buds: a(i,j)+(0,0),(1,0),(1,1).

Bottom-spine rule, used when j=0 and i>=q-1:

    active outputs: a(i+1,0), a(i,1),
    immutable buds: a(i,0)+(0,0),(1,1).

Append active outputs to the queue in the displayed order. Buds are never
consumed. In particular, the same-position bud is a FRESH output identity;
it does not retain the retired input's birth or ancestry label. Every output
has the consumed identity as its parent and inherits that root colour.
An abstract integer clock increments once per reproduction. A produced
identity's birth clock is the clock at its producer's start.

This is a resource rewrite system. Its four outputs are not asserted to be
a legal r=4 Tait star or a literal DCUV packet's four residual outputs.
The abstract clock is not asserted to be an actual ant C-count.

## 3. All current cells stay distinct, globally

Every macro-anchor is processed at most once. The first q-1 bottom columns
are separate infinite northward chains. The last root supports an eastward
bottom spine; every spine vertex emits one separate northward chain.
These active edges cover the macro-grid with unique parents. No active
output is another root: the only eastward parents begin at i=q-1.

All buds lie inside their producer's own half-open 2-by-2 block. Different
producer blocks are disjoint. Nonzero-offset buds are not macro-anchors.
A zero-offset bud uses exactly the just-retired input cell, which no later
active path revisits. Thus every output avoids every surviving identity.
All intermediate states are ordinary finite binary sets, with exact
ordered remove-then-install identity semantics.

There are finitely many cells at every finite clock, and every update removes
one identity and inserts four distinct ones. Hence

    r(k)=q+3k                                               (1)

exactly. Distinct root colours occupy disjoint producer blocks and do not
need to interact. The active ancestry paths are straight northward rays
attached to a straight eastward spine; no crossing of two distinct active
paths is required. Zero-length input/output recycling occurs only after
retirement, and is explicitly retained.

## 4. Positive age and even stronger plain speed

A vertical update replaces one active identity by one active identity; a
spine update replaces one by two. Therefore active queue length is never
smaller than q. At birth, a child is appended behind at least q-1 other
active identities. Its eventual consuming update is at least q ticks after
its producing update. All produced-input ages are consequently at least
q>=5. Every active child is eventually consumed because it has finitely many
queue entries ahead of it and each update retires the first entry.

Each parent-to-output L-infinity displacement is at most two. For every
produced parent born at b and output born at c,

    ||output-parent||_infinity <= 2 <= (2/5)*(c-b).          (2)

The first edge from an initial identity is handled separately and costs at
most two. Telescoping (2) gives, for a descendant born at B,

    ||descendant-initial_root||_infinity <= 2+(2/5)*B.      (3)

At clock k, every output was born at B<=k-1; surviving roots have distance
zero. In particular every current identity lies within

    floor(2+2k/5) <= floor((2k+13)/3)                       (4)

of its own root. Thus the EXACT numerical signed LB root-box ceiling is
satisfied, not just an unspecified O(k) estimate.

If desired, attach a formal birth-heading h(B)=h0-B modulo four. Then every
parent/child clock gap automatically obeys n=h(parent)-h(child) modulo four,
including the initial-boundary heading relation. This merely supplies the
marginal heading congruence; no physical heading sequence, role-dependent
potential inequality or allowed literal output mask is inferred.

## 5. A stronger square-root spatial bound

Give each initial active root generation depth zero. An active child adds
one. For roots i<q-1, depth d contains the single node (i,d). The last root's
comb contains exactly the d+1 macro-nodes

    (q-1+a,d-a), 0<=a<=d.

Hence generation d has exactly q+d active reproduction sites. FIFO processes
whole generations in order. Before generation d begins, exactly

    q*d+d*(d-1)/2

updates have occurred. The largest processed generation at clock k is at
most floor(sqrt(2k)). Every currently active child has depth at most one
higher, and every bud is within one coordinate unit of its producer.
Measured from its OWN initial root, every current identity is therefore
within

    2*floor(sqrt(2k))+2                                  (5)

in L-infinity distance. This is compatible with (1): the model deliberately
uses two-dimensional area rather than confining all new mass to one ray.
All five initial roots in the q=5 case lie in one fixed horizontal segment
of length eight. Finite initial root geometry does not force new pairwise
root interactions in this relaxation, even at the critical square-root
spatial scale.

## 6. Physical trust boundary and useful consequence

Equations (1)--(5) show that none of the following, even taken together,
forces termination of a residual-resource model:

- fixed finitely many roots in a fixed initial bounded set;
- exactly three net new identities per clock;
- binary current support with no collisions;
- positive produced-parent age at least five;
- plain coordinate speed bounded by a positive constant below 2/3;
- the signed numerical root-box radius floor((2k+13)/3);
- monotone ancestry and no merger of different root colours.

Any proof based only on these conditions would also exclude this explicit
model and is therefore invalid. A valid physical bridge must exploit an
additional premise, such as actual simultaneous inputs, role/output masks,
chronological head transport, or forced white regions. A bounded new-pair
interaction budget could still be useful IF a separate physical theorem
shows regeneration requires such interactions. The present model has none,
so that requirement cannot be deduced from mass, ages and packing alone.

The O(sqrt(k)) bound is not o(sqrt(k)); no collision contradiction at the
strictly sub-square-root scale is defeated. Nor is this a new ant, a physical
counterexample, or a claim that the abstract rewrites are executable by one
head. Independent review requested.
