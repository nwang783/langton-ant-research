# The rank-zero second-row branches have zero third-row prefix offset

23 October 2026, 04:38 UTC. Independently signed analytic continuation.
The auditor separately reconstructed the literal lower-strip transducer.

Use actual full drift (+2,0) and the independently signed singleton and
second-row classification. In either rank-zero second-row branch (length
four or five), the third-row horizontal-exit class C and vertical-exit
class D have their first marked ranks

    (p0,p1,p2)=(a,a+1,a+2),
    (q0,q1,q2)=(a,a+2,a+3),              a even.

The length-four branch has no other marks. In the length-five branch,
the remaining single standard bounce after the balanced even cut a+4
forces q3=c even, p3=c+2, with c>=a+4. Thus no later mark interferes
with the rank interval [0,a+4). This follows from the signed first-port
argument applied to that matched suffix; its indices are shifted by the
even cut and its literal path has voltage zero.

The complete third-row prefixes before rank a are unmarked on both
classes and horizontally matched by identical rank. Their first a top
ports are therefore ordered literal three-step bounces, with compass
S,W,N at even indices and S,E,N at odd indices. If a>=4, the first four
are the signed singleton-boundary obstruction. Hence a is zero or two.

## The next top port is a nineteen-step voltage-two path

The marked four-rank core after that prefix is horizontally balanced, so
its matching does not depend on any later marks. Following the exact
successors through the three built rows gives input a to output a with
compass word

    S E S E S W N E N E S W N W S E N E N.

For clarity, place the new upper D input at (1,0), with upper C representative
(0,0). The successive path vertices are

    (1,0), (1,-1), (2,-1), (2,-2), (3,-2), (3,-3),
    (2,-3), (2,-2), (3,-2), (3,-1), (4,-1), (4,-2),
    (3,-2), (3,-1), (2,-1), (2,-2), (3,-2), (3,-1),
    (4,-1), (4,0).

It has length nineteen, voltage two, and no intermediate vertex on the
new upper row. Before it all top ports are the ordinary ordered bounces.
These assertions can also be reconstructed with
`probe_axis_layer_transducer.py`, but the literal path is the proof datum.

Suppose a=2. At the fourth row, relabel its incoming-N and outgoing-S
ranks as P_j and Q_j. Its first two lower excursions have length three,
identity outputs and voltages zero,one. The signed first-two-bounce
argument therefore gives

    Q0 even, P0=Q0+2,
    Q1 even, P1=Q1-1 odd, Q2=Q1+1,

and C_(P1)'s W occurrence is exactly the source of D_(Q2).
The next lower excursion is the nineteen-step path above and ends at
C_(P2). Together with that W edge its net voltage is one, so

    c_(P2) = c_(P1) + 20 - period.

The built lower strip has at least 2+8+12=22 events in the second-row
length-four branch, and at least 2+10+18=30 in the length-five branch.
Thus period>20, contradicting P2>P1. This proves a=0 in both branches,
with no cap or width bound and no restriction on higher histories.

Only the zero offset is concluded. The third-row total length and, in
the length-five branch, its remaining even parameter c are still open.
