# An all-cap white-front speed bound from first-read chronology

23 October 2026, 10:05 UTC. Independently analytically approved; frozen
standalone formulation supplied for final signoff. No novelty claim.

Let an ordinary Langton ant have a COMPLETE BI-INFINITE initially-WHITE
translating front, with actual full event period P and nonzero actual full
drift d. Every physical cell has a finite complete chronology starting R,
and there are finitely many active classes modulo Z*d. Put
D=norm_infinity(d). With NO visit, strip-width, period or drift cutoff,

    P>=6D+4*ceil(D/3).                                  (1)

This is a necessary period/speed relation, not a front exclusion,
104minimality, eventual periodicity or finite-seed capture theorem. An
initial head or arbitrary prepared input would break the argument's first-R
premise and is explicitly outside its scope.

## 1. Every complete white front has an essential first-read backbone

Let T(v) be the actual FIRST read time of a physical active cell v, and
let a(v) be the physical cell read immediately before that first read.
There is no initial-head exception in the complete two-sided front. Thus

    T(a(v))<T(v).

Periodicity gives T(v+d)=T(v)+P and a(v+d)=a(v)+d. On the FINITE quotient
by the full d, a is a functional map on active cell classes, so it has a
cycle. Its cell classes are distinct before closure. Its unit checker edges
form a simple embedded circle in the physical cylinder: distinct unit grid
edge interiors cannot intersect, and a repeated vertex would repeat a
class. There are no opposite directions on the same checker edge.

Lift this cycle. Its endpoint is v+k*d and summing first-time decrease
gives kP<0. A simple embedded cylinder circle has winding0,+1 or-1,
therefore k=-1. Reversing it gives a simple directed ACTUAL-EDGE circle
with winding+1. It need not be an uninterrupted ant time interval.

Write its successive vertices v_i, i=0,...,ell, with v_ell=v_0+d, and
first times T_i, so T_ell=T_0+P. The incoming backbone edge at EVERY v_i
is literally the incoming edge of v_i's FIRST R read. A simple essential
circle in the flat cylinder has zero total turning (the turning/Euler
formula on the annulus to a parallel geodesic), so it has equally many
right and left corners. Its checker edges alternate horizontal/vertical;
consequently ell>=2D.

This existence proof uses NO stream-height or cap-four maximum rule.
Cap four is required only for the separate localization of such cycles
inside stream-height superlevels.

## 2. Exact first-time debts

Let j_i be the complete read rank at v_i immediately preceding the first
read of v_(i+1). Then

    T_(i+1)=T(v_i,rank j_i)+1.

Each physical zero-displacement return has length divisible by four and
at least four. Therefore

    T_(i+1)-T_i=1+4q_i,       q_i>=j_i>=0.              (2)

At a RIGHT backbone corner, its outgoing edge is its first R departure.
That departure immediately enters v_(i+1). Since the predecessor relation
also gives T_(i+1)>T_i, this immediate entry MUST be v_(i+1)'s first read:

    j_i=q_i=0 at every R corner.                        (3)

At a LEFT corner, the outgoing edge is not that first R departure, so
j_i>=1 and q_i>=1. With m=ell/2 L corners, already P>=ell+4m=3ell.

## 3. A left-run start cannot have debt only one

Let an L-run start v be preceded along the backbone by R corner u. Suppose
q_v=1. Then j_v=1: its selected second read L occurs exactly four steps
after its first R. To leave along the backbone's LEFT edge, that second L
must arrive with the SAME incoming heading as the first read. The unique
four-step first-return word with initial R and that final heading is RRRR.

The final intermediate read of this unit-face loop is at u, the very same
physical predecessor of v's first read. The u read immediately beforev
and this later u read are consecutive physical reads at u. The later one
is R, so the earlier one was L. It is exactly the selected read at u which
precedes v's first read, forcing j_u>=1. This contradicts (3).

Thus q_v>=2 at every L-run start. If there are s such runs, summing (2)
yields

    P=ell+4*sum q_i>=ell+4(m+s)=3ell+4s.               (4)

The equivalent disjoint-debt argument in the previously signed cap-four
note allowed the extra unit to be paid at u; (3) shows here that it must
in fact be paid at the L-run start. Neither argument uses a visit cap.

Four consecutive right turns on a simple unit-edge circle close a physical
unit face and cannot lie on an essential circle. R runs therefore have
length at most three. There are s R runs as well as s L runs, so m<=3s and
s>=ceil(ell/6). Since ell>=2D, (4) gives (1).

The bound has the compulsory residue P=2D modulo4 automatically. It gives
all-cap D4 period>=32 (axis4 separately>=40), D5>=38, D6>=44, D7>=54.
Together with the separately signed universalP>=28, odd-odd drift requires
P>=30 by the period residue. These numerical examples are necessities,
not existence assertions or a catalogue of all translating fronts.
