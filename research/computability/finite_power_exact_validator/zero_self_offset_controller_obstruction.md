# A conditional closure criterion for reducible unit controllers

2026-10-23 05:23 UTC. Analytic sufficient criterion independently reviewed at05:27 UTC.
The condition on unique self occurrences is explicit, NOT asserted universally.

## Statement

Consider a fixed finite typed, nonerasing, exact unit-pose substitution: every
image has the same unit displacement and incoming/final headings as its parent.
Assume for every reachable state s:

1. its image contains s at least once;
2. if it contains s exactly once, that occurrence has read offset zero.

Then no growing rooted power-limit satisfying these hypotheses can be an ant
trajectory on any coloring. It is enough that the hypotheses hold for the
actual fixed-root power; intermediate root phases are not assumed legal.

For undecorated eight-state unit controllers, condition1 follows from the new
charge-free incidence lemma. Condition2 is now independently proved by the physical unique-parent origin lemma.
For decorated types neither condition should be silently inferred from physical
incidence counts. For decorated types this remains a sufficient conditional criterion; the physical eight-state application now supplies both conditions.

## 1. Incidence and nongrowing components

Restrict to states reachable from the actual fixed root. Each iterated image
of such a state is a factor of a root power and hence internally ant-legal if
the proposed word is legal. Let M(X,Y) be the Laurent weighted incidence matrix.
Condition1 gives M(1,1)>=I. Consequently a strongly connected component has
Perron value one at(1,1) precisely when it is a singleton with exactly one
self child. By condition2 its corresponding Laurent diagonal is exactly1.
Call all other SCCs branching components. Each is irreducible and has Perron
value greater than one at(1,1).

If no branching component is reachable, every edge which changes state follows
a strict order in the SCC DAG. There are at most |S|-1 such edges on a leaf
path; all self edges have offset zero. Thus all depth-r read positions belong
to one fixed finite set, independent of r. A growing actual root prefix would
remain in this set forever, contradicting finite-domain escape on any coloring.

## 2. A terminal branching block

Otherwise choose a branching SCC T with no other branching component reachable
strictly below it. Its downstream matrix D has SCC diagonal blocks [1], hence
spectral radius exactly1 at every positive character. It may have nonzero
upper-triangular off-diagonal entries, so polynomial depth growth is allowed.
The subsystem reachable from T has block form

    M = [[B,C],[0,D]],

where B is irreducible and lambda(1,1)>1. The exact clock identity is still
M^r g=H-M^r d, with H independent of r. Both B and D may depend on X,Y.

## 3. A nonempty strict clock domain with lambda>1

If every state of T has exactly one self occurrence, condition2 gives B>=I
at every positive character. Since T is branching it contains an off-diagonal
cycle, and irreducibility implies lambda>1 everywhere.

Otherwise some diagonal B_ss contains at least two monomial occurrences.
If all those offsets are zero, B_ss>=2 everywhere. If one self offset q is
nonzero, choose a vector z with both coordinates nonzero and z dot q>0.
At (X,Y)=(exp(t z_x),exp(t z_y)), that monomial tends to infinity. Thus lambda
is greater than one for sufficiently large t. A physical quarter rotation
makes both transformed log coordinates positive; sufficiently large t then
lies in the rotated strict clock cone. The inequalities persist on a nonempty
open neighborhood U.

In all cases choose one rotated clock with its one-read increment vector g>0
on a nonempty open set U where lambda>1. Its checker vector d changes at most
by the corresponding physical permutation and global sign, preserving the
coefficient bound supplied by ant legality.

## 4. The downstream polynomial modes cannot cancel the pole

At t0=1/lambda in(0,1), the downstream resolvent (I-t0 D)^(-1) is a convergent
sum of nonnegative matrices. Therefore

    h(t0)=g_T+t0 C(I-t0 D)^(-1)g_D

is strictly positive. The active resolvent (I-tB)^(-1)h(t) has a genuine Perron
pole at t0 in every T coordinate. Its endpoint correction H/(1-t) is analytic
there, so the signed checker-occupation generating series has the same pole.

Exact unit geometry gives read offsets O(r). Internal ant legality gives each
checker-occupation coefficient in {-1,0,1}. The signed finite-valued rational-
series theorem therefore supplies a fixed semilinear denominator, a product
of factors 1-t^a X^b Y^c with a>0. It vanishes at1/lambda throughout U. Real-
analytic continuation over the positive quadrant then makes it vanish at
(X,Y)=(1,1), impossible because lambda(1,1)>1 and such a denominator there
has no positive zero strictly below one.

This closes both the polynomial and exponential incidence alternatives under
the two explicit hypotheses. It does not assert those hypotheses for arbitrary
unit transports, hidden state types, finite-order geometric changes, or changing
directive sequences.
