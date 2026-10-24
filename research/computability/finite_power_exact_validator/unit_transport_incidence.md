# Incidence monotonicity of arbitrary exact unit-pose transports

2026-10-23 05:21 UTC. Analytic lemma independently reviewed and geometrically replayed at05:25 UTC.
No local charge-preservation or ant-legality assumption is needed.

## Lemma

A physical state s consists of an incoming compass heading h and a turn R or
L. Consider any finite quarter-turn word starting with heading h, ending with
the same final heading as the single coarse action s, and having exactly the
same unit displacement as s. Let n_t be its eight physical-state counts and
put delta_t=n_t-1_(t=s).

There exist integers A,B,z such that, in N,E,S,W order,

    (delta_RN,delta_RE,delta_RS,delta_RW)=(B+z,A+z,B+z,A+z),
    (delta_LN,delta_LE,delta_LS,delta_LW)=(A,B,A,B).

Moreover all four integers A,B,A+z,B+z are nonnegative. In particular every
such image contains its own parent physical state, and its incidence vector
dominates the corresponding identity vector entrywise. Its length and charge
satisfy

    length = 1+4(A+B+z),
    charge = coarse_charge+4z.

The parameters can depend on the parent state and image. For exact charge,
z=0 and this reduces to the independently signed checker-axis identity.

## Proof

View the turn word as a directed walk on the four heading vertices. Subtract
the single parent edge. Matching initial/final headings makes the remaining
signed edge counts a circulation. Write r_h=delta_Rh and l_h=delta_Lh.
The heading balance equations imply that

    r_h-l_(h+1)=r_(h-1)-l_h=z

is constant, with clockwise indexing N,E,S,W. Hence r_h=l_(h+1)+z.

Matching spatial displacement says that total counts of outgoing N and S
are equal after subtraction, and likewise E and W. These equations become
l_N+l_E=l_S+l_W and l_E+l_S=l_W+l_N. Thus l_N=l_S=A and l_E=l_W=B,
giving the displayed formula.

Only the parent entry was subtracted, so every other delta entry is visibly
nonnegative. Each displayed class has two opposite-heading entries, at most
one of which can be the parent. The other proves that common class count
nonnegative; it then proves the parent correction nonnegative too. Summing
counts and signed counts gives the length and charge formulas.

## Consequence and strict limit

Any fixed controller on the eight UNDECORATED physical states, with exact
unit-pose geometry but arbitrary image charges, has incidence matrix M>=I
entrywise. Its strongly connected components with growth Perron greater than
one are the branching components of M-I. This is a structural constraint,
not by itself an ant obstruction.

A singleton component with one self occurrence can have weighted incidence
X^a Y^b rather than 1 unless its actual self offset is proved zero. More
generally a decorated recursive letter b->U b V can produce an out-and-back
family U^r b V^r. Therefore do not infer a bounded spatial footprint merely
from Perron value one or from this incidence lemma. General reducible,
nonuniform, non-charge-preserving controllers remain unresolved here.
