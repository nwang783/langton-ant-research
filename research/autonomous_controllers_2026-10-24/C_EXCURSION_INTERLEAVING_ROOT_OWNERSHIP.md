# Strict C-excursion interleaving forces an actual imported root

24 October 2026. Author proof and complete supplied controls; independent
audit pending. This is conditional on a strict interleaving. No assertion that
every WHITE front has one, or has two discovery cycles, is made.

## Exact all-cap relation

Use the actual WHITE-owned C-entry excursions from a74e13f8 and their signed
one-sided winding theorem d6407a02. Suppose two actual lifted excursions have

    r_i < r_j < l_i < l_j,

where E_i=[r_i,l_i), E_j=[r_j,l_j) are closed SAME-head-pose first-R/first-L
intervals. They cannot belong to the same C-entry cycle, whose selected
excursions are event-disjoint.

The actual lifetime R_i at r_i is consumed at l_i INSIDE E_j, while its source
is strictly BEFORE E_j. The root has no read between r_i and l_i, so l_i is
also the first E_j read of that physical cell. This is a required imported
BLACK lifetime with exact age l_i-r_i, not a hypothetical source at the same
coordinate or an input inferred from a cropped field.

There is also an exact geometric consequence. Let u_j and v_j be E_j's parent
and child C faces. The complete physical root of E_j has its first R at r_j
and its first L at l_j. Thus E_i reads that root EXACTLY ONCE, at the R event
r_j. Its clockwise stream difference at the two adjacent C faces is therefore

    f_i(u_j)-f_i(v_j)=1.

But v_j is first activated at l_j+1, after E_i ends. The entire forward ray of
its own C-discovery cycle is still unread during E_i. The same proper escape
argument as d6407a02 gives f_i(v_j)=0. Hence

    f_i(u_j)=1,  f_i(v_j)=0.

This combines actual ownership, interval order, full physical lifts and
closed-walk geometry. It does not replace a lifetime by a projected crossing,
and it does not pretend that E_i and E_j are disjoint modules. In particular
these are NOT eligible for a component-packing lemma requiring disjoint events.

## Genuine standard feedback, with exact full-period voltage

In the standard104 control, full d=(-2,2), there are exactly two such lifted
relations per period, with the older root placed in phases0..103:

1. 28 < 56 < 116 < 148.
   E88 imports its root at (-2,4) into E92: actual R28 -> L116, age88.
   E88 has clockwise winding1 at E92's parent (-6,3), and0 at child(-7,4).

2. 56 < 132 < 148 < 220.
   E92 imports its root at (-6,4) into the NEXT period's E88:
   actual R56 -> L148, age92.
   E92 has winding1 at that next parent's (-4,5), and0 at child(-5,6).

Thus the two long excursions genuinely form an interleaved root-ownership
feedback chain with full temporal winding1. Their total length180 exceeds104
because they share events. The shorter E8 and E12 are still retained in their
respective complete cycle decompositions; no incorrect sum of all four lengths
is substituted for one period.

This is compatible with the signed negative older coefficients of E92 and
with the exact A10/B94 self-feeding field. The feedback concerns selected
ROOT lifetimes; it does not account for every other imported BLACK cell.
For example the two A10 suppliers R62-P andR43 lie in the same first-entry
basin as the inner cycle, so a general claim that supplied fuel must cross
between different basins is already false on standard104.

## Controls, target, and scope

The checker reconstructs every root, physical position and event occurrence,
all strict interleavings among the selected cycles, and the independent finite
polygon winding values. All22 rotation/power/phase controls retain the full
period voltage; a q-th power has2q listed relations rather than silently
identifying its distinct full-drift classes.

Prepared10 has a WHITE-owned discovery cycle but no selected interleaving,
and its hidden BLACK input remains. Prepared80 and supplied1564/4352 have no
WHITE-owned C-entry cycles to choose. These examples make an interleaving-or-
input statement a concrete POSSIBLE next target, not an established theorem.
No such necessity has been proved from finite support, triangular winding,
positive ages, or the present source relation. Connector imports and arbitrary
higher-multiplicity tree excursions remain open channels.

There is no read/period/width cap, no broad word scan, no inferred physical
splice, no new controller and no general classification result here.

## Artifacts

certify_C_excursion_interleaving.py
C_excursion_interleaving_certificate.json

The supplied complete fields and stable histories are the signed dependencies;
the new checker never drops an unread field or claims independent realization
of either overlapping excursion.
