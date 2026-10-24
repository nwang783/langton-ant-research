# Perpendicular zero-C epochs have a uniformly bounded transfer interface

23 October2026,19:54 UTC. Analytic consequence for review, not a periodic-profile
claim or a DCUV exclusion. No assumption bounds an epoch's length or total young
ledger size. This isolates the parallel part of a possibly unbounded frontier.

## 1. A geometric lemma for two orthogonal monotone paths

Let P be a finite head-start path whose successive vectors belong to

    {(1,1),(1,3),(0,4)}.

Let Q be a finite head-start path whose successive vectors are rotations of
these by E or W, independently of the direction in which Q is indexed. Add
piecewise-linear interpolation between consecutive starts.

P is a graph x=f(y), with f nondecreasing and1-Lipschitz, because its y increments
are strictly positive and0<=dx<=dy. Q is a graph y=g(x), with g nonincreasing
and1-Lipschitz: its x increments are strictly positive or strictly negative,
and |dy|<=|dx|, with x and y progressing in opposite senses. Extend these
functions constantly past their endpoint domains, preserving both properties.

For every near pair P(y)=(f(y),y), Q(x)=(x,g(x)) with L-infinity distance<=R,

    |f(y)-x|<=R, |y-g(x)|<=R.

Hence |y-g(f(y))|<=2R and |x-f(g(x))|<=2R. The functions

    H(y)=y-g(f(y)),   J(x)=x-f(g(x))

increase by at least their argument increments, since g composed with f and
f composed with g are nonincreasing. Thus all matched source y coordinates
lie in an interval of length at most4R, and all matched consumer x coordinates
lie in an interval of length at most4R. Distinct packet starts of P have
integer y with increments at least one; distinct starts of Q have integer x
with absolute increments at least one. Therefore at most floor(4R)+1 starts
on EACH path can have a near partner on the other.

This remains true when one path has a single start, using constant extension.
No temporal ordering or physical color assumption is needed for this lemma.

## 2. Application to actual produced residual transfers

Work in one complete recurrent-eight history. An epoch consists of all full
packet starts with one fixed full-entry C clock a. All those starts have the
same heading. Consecutive starts within the epoch are separated by a zero-C
D/V/U packet, with exactly the vectors in Section1 after heading normalization.
The epoch's final positive-C packet may change heading only after its own
start, so it does not affect this start-path description.

Consider produced input transfers from one source epoch a to a consumer epoch
j, with perpendicular entry headings. Normalize source heading toN. If the
source output slot is o and consumer input slot is i at relative heading h,

    p_consumer-p_source=o-rot_h(i).

Exact literal retained geometry over all perpendicular h=E,W and the conserved
sector gives

    max ||o-rot_h(i)||_infinity =8.

One maximizing role is UCC output(-1,7) to V-family input(1,2), relative headingE,
with displacement(-3,8). The maximum is a conservative role bound, not an
assertion that this role is physically attained.

Every actual producer/consumer pair therefore has head distance at most8.
Section1 says at most33 CONSUMER PACKETS in epoch j can receive any produced
input from this SINGLE perpendicular source epoch a. This counts packets,
not just a selected ancestry edge or one input slot. Multiple transferred
identities into one packet do not increase the packet count.

## 3. A finite transverse exception budget inside each consumer epoch

Now assume the same actual history begins U/UC/UCC, so signed simplicity and
produced-input lifetime294 apply. Every produced input consumed in epoch j
has source clock a with1<=j-a<=294; age zero is independently excluded by the
signed zero-C fuel theorem. Its relative heading is-(j-a) modulo4.

A perpendicular source epoch has odd j-a. Among1,...,294 there are exactly147
such ages, and at most one source heading/epoch for each source clock. Thus
at most

    33*147 =4851

consumer packets in epoch j can receive ANY input from a perpendicular source
epoch. This bound is independent of j, entry mass, zero-C run length, radius,
and the number of produced identities. Missing source clocks only improve it.

At most r0 packets can consume an untouched entry identity, even over the
ENTIRE factor, because each such identity is consumed only once. Consequently
all but at most4851+r0 packets in any one epoch have every input produced in
an in-factor source epoch whose heading is PARALLEL or ANTIPARALLEL to the
consumer heading. After the input entry-funding horizon20R+211, the r0 term
vanishes for every later epoch.

If an epoch has N packets and E is this exception bound, it contains a
contiguous all-parallel-funded subrun of length at least

    max(0,ceil((N-E)/(E+1))).

Delete the at most E exceptional positions; their complement has at most E+1
runs. No claim is made that the surviving long run has a periodic turn word,
a bounded normal strip, a fixed profile, or a bounded number of output cells.
It may still draw on up to147 even-age parallel/antiparallel source epochs.

## 4. Relevance and limitations

This gives an exact direction-sensitive refinement of the growing frontier:
long zero-C epochs cannot be supported by arbitrarily many transverse contacts.
After a bounded number of such exceptions, their possible unbounded portion
is parallel recent-history transport. The actual age-two V rail family in
this directory is consistent with, and exemplifies, that remaining direction.

The separately signed complete periodic-profile clock must NOT be applied to
these arbitrary strings without an additional theorem proving a full periodic
bulk interface with the same actual axis, sector, anchor and passive output.
This note establishes no such profile contract, no U or C budget, no bound on
independent archive births, and no stabilization result.

Dependencies: signed literal residual geometry; signed epoch zero-C fuel /
fixed-heading projection theorem; signed294-C produced-input lifetime. The
near-pair lemma itself is the elementary monotone-function proof in Section1.
