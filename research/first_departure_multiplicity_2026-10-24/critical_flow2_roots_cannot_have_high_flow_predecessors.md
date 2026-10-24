# Critical flow-two roots cannot have high-flow predecessors

24 October 2026. Complete WHITE cap-four translating front, actual full
P,d. Gamma is a b-circle at critical selected level c=c_right+1 and has
no single-used edge. The core incoming-junction obstruction needs no
global maximum or exterior height cutoff. Author proof pending review.
It uses signed mixed first-track chronology and the general LRRL gate,
not a fresh-fuel assumption.

THEOREM. Every flow-two O/U crossing u is immediately preceded on gamma
by a FLAT flow-two RIGHT contact. A 3->2 or 4->2 predecessor cannot supply
it. In particular at GLOBAL M the surviving LL crossing rows are exactly
the old flat-end four-L cleanups; the long zero-chord LL root alternatives
are excluded by actual nested intervals, while passive V/V notches stay.

## 1. Complete predecessor possibilities

The critical last-LEFT gate dba869f4 says u cannot be second in an LL
pair. Hence its predecessor q is RIGHT and has outgoing physical flow two.
No-one-use removes incoming flow one. The full RIGHT predecessor alphabet
is flat two X/Y, a 3->2 odd sink EEE, or the 4->2 target EEEE, after rotation.
These are all possibilities, not an imposed homogeneous segment.

The4->2 target has a RIGHT 2->4 source directly before it, by the signed
isolated flow-four block. If q were this target, it would be the second
RIGHT of an RR run touching u. General mixed LRRL closure f008184d forces
that neighboring LEFT to flow one or V at flow two, never O/U. Contradiction.

The same RR argument excludes a 3->2 sink q if its predecessor is RIGHT.
Its predecessor must therefore be a LEFT flow3 contact w, uniquely WEEE
in its normalized frame. This deduction is local and does NOT require a
bound on the length of a whole nonmaximal flow3 segment.

## 2. Actual first/third strands give strict interval nesting

The actual boundary subpath is w(LEFT flow three)->q(RIGHT3->2)->u(LEFT2 O/U).
First ordinal and R0 matching give

    w.R0 -> q.R0 -> u.L1,
    T1(u)=T0(w)+2.                                  (1)

On the third/second physical copies the complete profiles give

    w.L3 -> q.R2 -> u.R2,
    T2(u)=T3(w)+2.                                  (2)

These are consecutive ACTUAL reads on the stated edges; both odd q
ranks and w's late L3 are retained. Since same-cell gaps are at least 4,

    T1(w)>=T0(w)+4=T1(u)+2,
    T2(w)<=T3(w)-4=T2(u)-6.

Thus w's own actual L1-to-R2 LEFT-return interval is strictly INSIDE
u's actual L1-to-R2 interval. The critical mixed first-track theorem
pairs every crossing with its own physical return and makes these
intervals disjoint. No hidden older reader or full-drift translate can
repair this finite strict nesting. Contradiction.

Therefore q is flat two. The conclusion applies to singleton O/U and first
LL O/U alike, and it includes arbitrarily old w.L3 supply rather than
bounding or deleting it.

## 3. Consequences for the exact mixed LL inventory

In the signed 144-row LL inventory, the only nonflat open rows use a
3/4->2 predecessor AND a 2->3/4 follower, with zero closing chord. If its
first LEFT is a crossing, the preceding result rejects it. If its second
LEFT is a crossing, the signed last-LEFT gate already rejects it.
Consequently at the critical level only V/V zero-chord rows remain.

The first-LL O/U rows that survive are the two old flat-end rows:
preceding RIGHT Y, following RIGHT X, second LEFT V, literal four-L
cleanup. Under the no-one-use inventory this leaves SEVEN necessary LL
junction rows total: three flat rows plus four passive V/V zero-chord
parent pairs. These are necessary local rows, not completed front modes.
The mixed long even-U root was a valid local countercontrol, but its
high incoming sink cannot satisfy the full critical chronology.

## 4. Sharp one-flat role, retaining its required positive transfer

Add GLOBAL M and suppose there is exactly one flat RIGHT class and some
flow-two root. The signed two-ended-provider result 6d8ef66c says there
is exactly one such root, its flat F is Y=EWWE, its entry provider is
G=F+d, and ell<age13(F)<P. The current theorem further says u=b(G) at the
physical predecessor used by that entry. Exact first/second ordinals give

    T1(u)=T0(G)+1, T2(u)=T1(G)+1.

Hence the root's LEFT span is T1(G)-T0(G). Combining the provider clock
with this identity forces

    T3(F)-T0(F)=P+ell.

This cell's full first-to-last lifespan genuinely exceeds one period;
no general span<P assumption is permitted. The actual boundary factor
from G.R0 to F.L3 follows gamma once in ell steps, displacement -d, while
the unresolved exterior factor F.L3->G.L1 has displacement +d. All physical
copies and older stock remain present. Neither direction can be erased
as a phase convention or treated as original fuel consumption.

No completed WHITE exterior is constructed here. With multiple flat
classes the nearest providers may differ, and K_c>=2 can mix root
returns. A general one-use theorem, period bound or capture statement
does not follow.
