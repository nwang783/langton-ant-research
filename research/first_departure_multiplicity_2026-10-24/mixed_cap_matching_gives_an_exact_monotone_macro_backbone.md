# Saturated cap matching gives an exact monotone macro backbone

24 October 2026. Author dependent geometric corollary pending review.
Use the full scope and all typed gates ofb88d71dd, including corrected
post-X gate09e98e96 and flat-ended passive qualifier12769efd. No extra
reader truncation, fuel premise or one-event-orbit realization is added.

## 1. A genuine partition of the cyclic flat-gap word

List Gamma's flat RIGHT contacts in actual cyclic spatial order, keeping
all full-drift incidences. Between neighboring flats either there is a
flat-only gap with zero, one or two LEFT contacts, or a maximal high run.
The signed complete LL table forbids a two-LEFT flat/high interface, and
high-run endpoints have a single passive V, so these cases exhaust gaps.

By the saturated matchingb88d71dd, every zero-LEFT gap (a flat RR cap)
is paired with exactly one adjacent two-LEFT gap:

- a FLAT-ended passive VV LL gap pairs with the RR immediately BEFORE it;
- a genuine LL-first O/U gap pairs with the RR immediately AFTER it.

No gap is used twice: each LL and RR has exactly one assigned partner.
Therefore these adjacent gap pairs form disjoint TWO-gap packets in the
cyclic flat-gap word. Unpaired gaps are exactly singleton-LEFT gaps and
high runs. A short quotient may make a packet cover the whole gap word;
that is not ruled out merely by drawing distinct endpoint classes.

## 2. Literal geometry of every packet

A packet begins at a flat contact and stops at its endpoint flat WITHOUT
processing that final contact. Normalize its initial incoming heading N.
The literal b-turn words, endpoint displacement and final incoming
heading are as follows:

    passive packet: RRLL,       displacement(2,0), heading N;
    genuine packet: RLLR,       displacement(0,2), heading N;
    singleton gap: RL,          displacement(1,1), heading N;
    high gap: RLRLR(LLRR)^q L, displacement(3,3+2q), heading N.

In the high gap q>=0 is the number of later RR3/RR4 macros after its
initial RLR3. Their type does not change the physical b-turn geometry.
Every packet returns to its own initial incoming heading, with EXACT
signed turn zero. This concerns the packet endpoints; individual b
steps inside a packet may move backward. No such step, actual read,
L3 supply, side-current channel or open exterior port is deleted.

Because packets partition the full cyclic word, their boundary-flat
incoming headings all agree. One quarter-turn normalization makes all
packet endpoint displacements nonnegative in both coordinates. This
is an exact monotone MACRO backbone, not a claim that the full ant path
or every physical b edge is monotone.

## 3. Exact full-drift and boundary-length identities

Let p be the number of passive packets, g the number of genuine packets,
s the number of singleton gaps, h the number of high gaps, and q the
TOTAL number of later high RR macros in all high gaps. All are full-
quotient incidence counts, not counts of distinct original stock roots.
Write D for Gamma's physical displacement in this normalized frame on
one complete negative b lap. Thus D is exactly the normalized -d, not a
primitive-divided drift. The packet words give

    D_x = 2p + s + 3h;
    D_y = 2g + s + 3h + 2q;
    ell = 4p + 4g + 2s + 6h + 4q.                    (1)

No bound on p,g,s,h,q or P follows. The formulas retain every arbitrary
rail length q and every coordinate voltage of the full quotient.

In particular, if s+h>0, BOTH drift coordinates are strictly positive.
An axis degeneration requires s=h=0 and therefore q=0. If D_x=0, only
genuine RLLR packets remain. But a cyclic concatenation of those puts
a genuine first-LL crossing immediately after an RR cap, contrary to
the signed general RR closure, whose LEFT endpoints must be V. If
D_y=0, only passive RRLL packets remain. This is exactly the constant-
flow-two RRLL b-circle excluded by signed actual-event separator9276befb.
The case both coordinates zero is incompatible with d nonzero.

Hence D_x,D_y>0: an axis drift cannot realize this critical GLOBAL-M
no-one-use cap-four boundary. This is a conditional boundary geometry
consequence, not the all-cap axis theorem or a general front exclusion.

## 4. Open chronology and ownership

The macro backbone is geometric. Its temporal channels can run in the
opposite direction and can carry positive full-period voltage. Old
archives, odd outputs and cross-curve transfers remain obligatory.
Neither the packets nor the high runs are autonomous ant controllers;
no legal prepared full-factor concatenation has been supplied.
The remaining challenge is to satisfy all original channels in ONE
actual translated cursor orbit, not merely to repeat the packet words.
