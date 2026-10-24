# Two physical returns demand incompatible incoming ordinals

24 October 2026. Author analytic proof, submitted for independent review.
This is an all-cap obstruction to one specific open prefix, not a further
reduction in the216 coarse diagonal interfaces.

## Abstract all-cap return lemma

At a cell whose incoming axis is vertical, a W departure occurs exactly at
S/R or N/L. Write w_i for the complete read rank of its i-th W departure,
and n_i for that of its i-th N arrival, with ordinals starting at zero.
Read turns alternate; the first color is irrelevant to this lemma.
It is impossible that BOTH

    n_0 = w_1+1,           n_2 = w_2+1.                 (1)

Indeed, if the first N arrival n_0 were R, its previous read w_1 would be L.
An L departing W arrives N, contradicting that n_0 is the first N.
Therefore n_0 is L and departs W. As it is the very next read after the
second W departure, it is exactly the THIRD W departure: n_0=w_2.
The other relation in(1) now asserts n_2=n_0+1. But the second N arrival
n_1 must occur at a strictly intermediate read rank. Contradiction.

There is no multiplicity, period, support width, or initial-color bound in
this abstract argument. Rotating all ports gives the corresponding literal
versions. These are read identities, not conserved mass estimates.

## Concrete complete-history interface

Use full d=(2,-2), representatives (r,t-r), r=0,1, and the named histories

    t=-1: W, empty
    t= 0: N, SS
    t= 1: WE, WWE
    t= 2: SNN, SSNS
    t= 3: EEWE, WWEW.

This is precisely the24-event OPEN cap-four interface08185afc. Its internal
ordinal matches and distinct P200 phases are consistent. That fact does
not supply any unknown upper complete histories.

At the actual next cell Q=(2,2), equivalent to representative(0,4), incoming
N occurs three times and outgoing W occurs three times. More importantly,
the complete LOWER histories force two uninterrupted returns to this SAME
physical Q:

1. Its second W departure, through19 named reads, returns to its FIRST N
   arrival after20 steps.
2. Its third W departure, through three named L reads, returns to its THIRD
   N arrival after four steps.

Q is not among the intermediate positions in either path. Thus these are
exactly the two consecutive-read identities(1), and the abstract lemma
forbids every upper completion, regardless of how many visits are allowed.

The20-step path's named events, as (physical cell, complete rank), are:

    ((1,2),1), ((1,1),0), ((0,1),0), ((0,2),1),
    ((-1,2),1), ((-1,1),0), ((-2,1),0), ((-2,2),0),
    ((-1,2),2), ((-1,1),1), ((0,1),1), ((0,2),2),
    ((1,2),2), ((1,1),1), ((2,1),0), ((2,0),0),
    ((1,0),0), ((1,1),2), ((2,1),1).

The four-step path is

    Q -> ((1,2),3) -> ((1,1),3) -> ((2,1),3) -> Q.

All physical occurrence ordinals, full-drift lifts, headings and turns are
retained and checked in check_two_return_ordinal_collision.py and
its output two_return_ordinal_collision.json. No lower-field read was
removed and no outside port was supplied an arbitrary color.

## Interpretation and exact scope

The positive OPEN interface remains a correct local countercheck against
inferring one-use F edges from internal cap-four clock/port constraints.
It is NOT a possible complete front: this first genuinely missing upper
cell cannot have an alternating history at all. Global completion matters.
The obstruction is stronger than a cap-four-only completion failure and
stronger than merely forcing seven visits at Q. It uses the20-step return
as well as the short four-step return, not only the third-port closure.

The whole-controller height13/cap12/g8 search fixing this prefix returned
UNKNOWN after60s. That solver outcome is not a premise. The analytic two-
return identity proves this particular prefix impossible at EVERY height,
cap and period, at any growth. It does not remove the larger coarse
boundary case, whose other upper histories still remain open. The signed
coarse g8 diagonal remainder is still216, not215.

No controller construction, full g8 exclusion, general cap-four F-edge
multiplicity theorem, or arbitrary finite-seed capture statement follows.
