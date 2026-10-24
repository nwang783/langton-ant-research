# Exact chronological relay on one-use first-R paths

24 October 2026. Author cap-free consequence, pending independent review.
The hypotheses concern actual complete WHITE cell histories and actual total
physical edge use. No multiplicity bound is imposed on the exterior. The
boundary-local alphabet is the independently signed 61ab7596 lemma. This is
not an existence result, an unread-row claim, or a whole-front exclusion.

## 1. Finite one-use path, with physical lifts and voltages

Let v_0,...,v_m be an actual first-R departure b-path whose m selected
physical edges each have total use one. Both endpoint corners are RIGHT.
Every internal RIGHT vertex is the singleton R history; every internal
LEFT vertex is, after physical rotation, WWE or WWEW. At a RIGHT target
the selected arrival is its R0; at a LEFT target it is its R2. Optional
L3 is retained and need not be a last read of any other cell.

Write T_r(v) for the actual physical occurrence time and
Delta(v)=T_2(v)-T_0(v) at an internal LEFT. Each selected edge therefore
has the exact equation

    T_0(v_(i+1))-T_0(v_i) = 1-Delta(v_(i+1))  if the target is LEFT,
                               1              if the target is RIGHT.

Consequently

    T_0(v_m)-T_0(v_0) = m - sum_internal_LEFT Delta(v).

This is a physical-lift identity. If v_m=q+k*d in chosen full-drift
representatives, the left side is T_0(q)-T_0(v_0)+k*P. No voltage may be
dropped. It is not asserted for a path whose selected edges merely have
first-ordinal ownership rather than total physical use one.

## 2. Entire one-use circle: exact temporal covering

Now let gamma be an embedded essential full-quotient b-circle, with all
its physical edges used once. Its ell vertex classes are distinct. Use
the retained actual b-circle orientation, so the physical closed lift
ends at v_0-d and the temporal winding is -1. Every LEFT class has the
Delta above, and

    -P = ell - sum_LEFT Delta(v).

At a half-integer temporal cut t, include ALL full-period translates.
Let N(t) count translated intervals (T_0(v),T_2(v)) for LEFT classes.
Let B(t) count selected unit actual-event edges of gamma crossing t.
These unit edges are event-disjoint: their source events are the R0s of
distinct physical vertex occurrences. Hence B(t) is either zero or one.
The exact pointwise identity is

    N(t) = 1+B(t).

Indeed the selected closed temporal walk consists of its actual forward
unit edges, with every LEFT arrival R2 followed by the formal backward
interval to that same cell's R0. Its degree is -1. Equivalently, the
endpoint coboundaries of B-N cancel at every cut, and its period integral
is ell-sum Delta=-P. This does not remove those backward intervals from
the real ant orbit and does not splice any physical trajectory.

Thus the first-R-to-second-R intervals cover every time once, and cover
it twice exactly during selected boundary unit edges. Arbitrary old
copies are included, not discarded using a presumed age bound.

## 3. Reverse order and the one-LEFT exception

List successive LEFT occurrences L_i along the physical b lift. Between
them there are r_i RIGHT vertices, with r_i in {0,1,2}; three consecutive
RIGHT turns would close a physical unit square, incompatible with the
embedded essential b-circle. The selected edges between these LEFTs are
an ACTUAL contiguous successor channel

    L_i.R0 -> (r_i singleton RIGHT events) -> L_(i+1).R2.

Its length c_i=r_i+1 is in {1,2,3}, so

    T_2(L_(i+1)) = T_0(L_i)+c_i.

Two consecutive reads of one physical cell are at least four steps apart.
Therefore Delta>=8. The exact channel gives

    T_0(L_i)-T_0(L_(i+1)) = Delta(L_(i+1))-c_i >=5.

The second-R endpoints also decrease strictly:

    T_2(L_i)-T_2(L_(i+1)) = Delta(L_i)-c_i >=5.

These are actual strict chronological orders, not just stream signs.
The channel occurrences are event-disjoint components of the selected
successor subgraph; no arbitrary overlapping-window packing is used.

If n is the number of LEFT full-quotient classes, both ordered sequences
shift by -P after n indices. For n>=2, the n-1 other first-R gaps are at
least five, and consequently every LEFT satisfies

    8 <= Delta(v) <= P-5*(n-1)+3 <= P-2.

In particular Delta<P is a CONCLUSION for this wholly one-use circle,
not a general same-cell lifetime premise. For n=1 it instead satisfies
Delta=P+c_0, which may exceed P. This exception is explicitly retained;
no claim is made here that a complete front attains or excludes it.

The embedded essential circle has zero total turning, so ell=2*n.
Integrating the cover yields P>=3*ell. This is only the existing local
clock's arithmetic consequence. It is not added to overlapping flow,
output, or age budgets and is not offered as a global speed theorem.

## 4. Scope and next composition question

The finite-path identity applies to partial one-use runs with RIGHT
endpoints, independently of any whole-circle completion. The interval
cover and reverse cyclic order require an entirely one-use b-circle.
They cannot be imported unchanged across a multiplicity-changing source
or sink. All optional L3 reads and exterior physical suppliers remain.

These statements do not force an arbitrary critical cap-four circle to
be wholly one-use. Stage41 supplies only at least one one-use edge.
Mixed circles, longer one-use runs, changing source/sink modes, and
noncritical curves still require their actual exterior port chronology.
