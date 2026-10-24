# Direct odd-output reservations close the early ancestor capacity

23 October 2026. Complete WHITE cap-four K1 front, actual full P,d.
No zero-output hypothesis. Count the surviving actual EARLY main-source
classes n_A from the signed ancestor injection 427658fb. The signed
source-L3 cleanup and two-ancestor inventory a7f57d46 apply to every one,
after f614a375 excludes all early zero-L3 suppliers.

Partition this family into S ancestors (count n_Sanc), RIGHT ancestors
with x=EWW (count n_R3), and RIGHT ancestors with x=EWWW (count n_R4).
These counts satisfy n_A=n_Sanc+n_R3+n_R4. We prove

    Nodd >= n_Sanc + n_R3 + 2 n_R4 = n_A + n_R4,
    N_O >= n_R4.

This is physical/full-quotient OUTPUT capacity, not initial fuel. It
strengthens the separately signed neighborhood bound n_A<=14 Nodd.
The older capacities remain valid and are not added to this bound.

## 1. Exact RIGHT-ancestor alternatives, without evenness

Use the original main source at (0,0). Its actual chain contains

    Q1=(-3,1) -> P0=(-2,0) -> I=(-1,1).

For RIGHT Q1 the signed complete histories are j=(-3,1)=EEWE and
k=(-3,2)=NNNS, with p(Q1)=Q2=(-4,0), both Q1,Q2 at M. The signed 72-row
ancestor table has 36 RIGHT rows and exactly these lower interfaces:

    x=(-2,0)   r=(-1,-1)   e=(-1,0)
    EWW         WEEW        SNN
    EWWW        WEW         SNNN
    EWWW        WEWW        SNNN.

All three have 12 necessary completions. No global zero-output filter
has been applied. In particular the two EWWW rows have the same physical
r.E input count ONE, despite r's optional L3.

## 2. x=EWW is itself an injected odd class

A complete WHITE EWW history has three reads and ends black. It is a
flat contact with opposite R headings, and L1 has the heading of R2,
not R0. Thus it is a POSITIVE flat three-read contact, never a canonical
negative first-L entry.

The actual right-C face of its L1 INCOMING edge is P0: its W arrival
comes from the E neighbor, and the right-hand C face on that directed
edge is the NE face P0. This identifies P0 uniquely from the complete
physical three-read history, in every rotated pose. The signed early
assignment makes all P0 classes distinct. Therefore the n_R3 cells x
are distinct physical/full-drift odd classes. No ancestry degree bound
or arbitrary new maximum component is being substituted for this
specific geometric recovery.

## 3. x=EWWW forces a unique complete lower square

Let F=(-3,-1) be the opposite C face across x. Since x has opposite R
headings and P0=M, also F=M. Put its NW corner d=(-3,0), SE corner
t=(-2,-1), SW corner a0=(-3,-1).

The complete j=EEWE sends exactly one S arrival into d. The complete
x=EWWW accepts exactly one E arrival from d. Thus d has one S input and
one E output. The complete r=WEW or WEWW accepts exactly one E arrival,
so t has one E output. Complete canonical birth at global maximum F
still holds. Test ALL 110 canonical profiles in ALL four rotations,
with these exact physical conditions and x=EWWW. Exactly ONE completion
survives, without any evenness condition:

    SW a0=EEWW, NW d=NNS, NE x=EWWW, SE t=SSS.

The canonical birth of F is at a0; its only possible canonical child
contact is d. The two new cells d and t are genuine odd-output classes.
This is not a zero-output-only obstruction: it reconstructs the literal
output required in every such RIGHT-ancestor mode.

## 4. d is the canonical entry of a distinct actual O producer

The actual Q2 has SE d=NNS and NE j=EEWE. Complete canonical completion
at Q2, using all 110 profiles and rotations, gives exactly FOUR rows:

    SE d   SW       NW      NE j
    NNS    WW       NSSS    EEWE
    NNS    WWE      NSSS    EEWE
    NNS    WWEE     NSN     EEWE
    NNS    EWW      SSNS    EEWE.

All four have canonical birth at d. They are precisely the signed odd
producer O profiles: incoming flag0, at most ONE flag1 child contact,
namely j. That child is ACTUAL Q1, by the already retained p(Q1)=Q2.
Hence every such Q2 has q=+1 and is an actual O producer, and p(Q2)=F.

The assigned Q1 classes of different early sources are distinct by
427658fb. An O face has at most one actual flag1 child, so these Q2
classes are distinct. Their canonical entry d classes are distinct.
Thus N_O>=n_R4, with n_R4 distinct negative-flat three-read outputs.

## 5. The additional t outputs are distinct too

The unique F profile in section3 has only one POSSIBLE canonical child,
d. Section4 makes that child Q2 actual. Different Q2 therefore have
different F faces. A complete t=SSS has both R headings S and chooses
the unique incident higher C face F; the other incident C height is
M-2. Thus a fixed physical t, in any rotated pose, identifies that F
uniquely. The n_R4 classes t are consequently distinct as well.

Physical uniqueness transfers to the actual full quotient by translating
one witnessing package by an integer multiple of full d before aligning
the selected cell or canonical face. Repeated quotient periods cannot
increase an injection or replace a complete history with another one.

## 6. Disjointness and the safe output union

The three-read x reservations of section2 have opposite R headings and
L1=R2. The three-read d reservations have opposite R headings but
L1=R0. They cannot coincide after rotation or full translation. The
three-read t reservations have SAME R headings, so cannot coincide with
either family. The signed S-ancestor reservation uses ONE-read cells,
so is disjoint from all three. Its own injection was already proved in
427658fb.

We therefore have n_Sanc+n_R3+2n_R4 distinct odd physical classes, giving
the displayed bound. The d reservation can overlap existing O/rise
reservations, and t can overlap existing same-R stock/helper outputs.
No additive union with those older families is asserted here. Output
still has no upper bound in terms of an original finite seed, and no
general K1, cap-four or finite-seed exclusion follows.

Control `early_R_ancestor_direct_odd_reservations.py/json` checks the
36 RIGHT rows and all three interfaces, the unique full lower-square
completion, and all four exact Q2 O profiles. It performs no front,
period, drift, radius or multiplicity scan. Dependencies: canonical
inventory/flag balance d1f7304b; actual early ancestor injection 427658fb;
complete two-ancestor classification a7f57d46; all-early zero-L3
exclusion f614a375. This new result does not require 72a895af as a
premise; the all-even obstruction follows from the same stronger local
completion.
