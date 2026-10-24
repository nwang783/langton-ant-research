# No nonempty reverse-phase lower-bounce system

23 October 2026, 04:28 UTC. Independently signed analytic lemma, including
the carefully scoped parity-padding extension.

Use an adjacent horizontal pair C=(0,y), D=(1,y) modulo full drift (+2,0).
They have equal finite complete histories, starting R and alternating R,L;
C incoming headings are N/S and D outgoing headings are S/N. All horizontal
occurrences match by ordinal, with clock increments 1 for E and P+1 for W.
Assume P>8 and all paths used below are proper. Let p_j be the ordered N
arrivals to C and q_j the ordered S departures from D. Suppose there are
m>=1 of each, and the lower strip supplies the ordered three-step paths

    D_(q_j) -> C_(p_j),
    compass S,E,N for even j; S,W,N for odd j.

Their voltages are 1,0,1,0,... . We show these hypotheses are inconsistent.
This is the opposite phase from the singleton-boundary bounce system.

If q0 is odd, its W source C_k followed by lower input0 makes a four-step
first physical return to C_(p0). Hence p0=k+1. The unmarked k before the
first N arrival is even, so p0 is odd. W ordinals give k=q0+1 and
p0=q0+2. The first downward mark q0 is then odd and precedes every C
mark, violating the prefix ballot. Thus q0 is even.

Its E source C_k followed by input0 has voltage1, so
c_(p0)=c_k+4-P<c_k and k>p0. If p0 were even, ballot would give q0<=p0.
If q0<p0 the matched source would be k=q0+1<=p0; if equal it would be
k=p0. Both contradict k>p0. Thus p0 is odd.

Input0 followed by C_(p0)'s W edge first-returns to D at rank q0+1,
which is odd with W input and hence departs S. Therefore q1=q0+1.
W ordinals yield (p0+1)/2=q0/2, or p0=q0-1. If m=1, the forced q1 is
already impossible.

The E source C_k of D_(q0), input0, C_(p0)'s W edge and input1 form an
eight-step first physical return to C_(p1). The intermediate C is translated
by+d; thus p1=k+1. Since k>p0 and p1 is the next N mark, k is unmarked odd.
Its E ordinal is (k-1)/2-1, while D_(q0)'s is q0/2. Thus

    k=q0+3,       p1=q0+4 (even).

Input1 followed by C_(p1)'s E edge first-returns to D at q1+1=q0+2,
an even E arrival and hence another S departure. Thus q2=q0+2. If m=2
this is already impossible. The E ordinal at D_(q2) is q0/2+1, exactly
that of C_(p1), since their preceding marked signs cancel appropriately.
Consequently C_(p1) is the E source of D_(q2), and input2 gives

    c_(p2)=c_(p1)+4-P<c_(p1),

contradicting p2>p1. No nonempty reverse-phase system exists.

## Optional parity-padding extension, proposed separately

The same contradiction applies if the two finite suffix histories start
with L rather than R, provided their horizontal E/W counts match and their
known lower paths have the stated form. Prepend one fictitious unmarked
R event to each local history: C arrives S and goes W to D, and D arrives
W and goes N. This adds one W occurrence to both port lists and shifts
every existing rank by one, giving the original L parity at its new rank1.
Choose the two new clocks sufficiently early with d_new=c_new+P+1; all
existing local clock orders and matched edges remain unchanged. Every
known lower-path first return remains between the same actual events with
both endpoint ranks shifted equally. The dummy edge ends at the unmarked
new D event, so it cannot enter one of the lower-path arguments.

The proof above is purely a contradiction among these local clocks,
parities, matched ports and actual first-return rank equations; it does
not require the padded pair to be an actual ant trajectory or assign new
phase slots in the full period. Thus the padding is only a logical local
model extension, not a claimed modification of the physical front.
