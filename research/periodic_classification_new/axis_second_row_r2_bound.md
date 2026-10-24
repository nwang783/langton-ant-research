# The rank-two second-row branch has length five

23 October 2026, 04:28 UTC. Independently signed analytic lemma.
This uses the signed reverse-bounce obstruction and its parity-padding
extension, in addition to the already signed singleton and ballot results.

Use the exact top-port model in `axis_singleton_second_row_structure.md`
with r=2. The second row has length n>=5 and m=n-1>=4 ports. At the third
row call the horizontal pair C=(1,2), D=(2,2), and use marks p_j,q_j as
before. Lower inputs0,1 have identity outputs and voltages0,1; input2 goes
to output3 with length3, voltage0; input3 goes to output2 with length7,
voltage1. Inputs j>=4 go to the same output with length3 and voltages
1,0,1,0,... . The whole period is at least20, so every eight-step path
below is proper. The sole sixteen-step case has a larger explicit bound.

## 1. Four upper marked ports are forced

The first two ordered standard bounces give, by the signed ballot argument,

    q0=a even, p0=a+2,
    q1=b even, p1=b-1, q2=b+1,

where b>=a+4. Let C_k be the E source of D_b. Its first bounce has
c_(p1)=c_k+4-P, so k>p1. Following inputs1 and2 gives an eight-step first
physical return to C, hence

    p3=k+1.                                           (1)

There is exactly one marked C rank, p2, strictly between p1 and p3.

Suppose p2 is odd. Then k cannot equal p2, whose output is W. Thus k is
unmarked odd, so p3 is even. Input2 followed by C_(p3)'s E edge first-
returns to D at q2+1=b+2, an even E arrival and hence q3=b+2. Input3
followed by C_(p2)'s W edge first-returns to D at b+3, an odd W arrival
and hence q4=b+3. The W ordinal of C_(p2) is (p2+1)/2, because p0,p1
have cancelling signs. D_(q4)'s W ordinal is b/2, since the four earlier
q marks have signed sum2. Thus p2=b-1=p1, impossible. This argument also
excludes m=4 as soon as it forces a fifth port.

Therefore p2 is even. If k>p2, k is unmarked odd, and its E ordinal is
(k-1)/2+1. D_b's ordinal is b/2+1. Hence k=b+1, p3=b+2, and the even
rank p2 between p1=b-1 and p3=b+2 must be p2=b.

The only other possibility is k=p2. E ordinals then give

    p2=b+2,                  p3=b+3.                  (2)

We exclude (2). If q3 were odd, its W source followed by the seven-step
input3 first-returns to C_(p2), forcing that source rank to be p2-1=b+1.
This rank is unmarked odd and outputs E, a contradiction. Thus q3 is even.

Start at D_(q3), follow input3 and C_(p2)'s E edge to D_b, then input1
and C_(p1)'s W edge to D_(q2), then input2 and C_(p3)'s W edge. This is
a sixteen-step first physical return to its starting D cell; all its
intermediate upper D visits are translated by+d. It ends at rank q3+1,
an odd W arrival, and therefore q4=q3+1. Its W ordinal matching gives

    q3=b+4,                  q4=b+5.

(The case (2) has p3=b+3>=7, so the third-row history length is at least8;
with n>=5 and the bottom two events, P>=28>16.)

C_(p3) is now the W source of D_(q4); input4 has voltage1, so their four-
step C first return forces p4=p3+1=b+4. C_(p4)'s E ordinal is b/2+2,
matching the unmarked D rank b+3. But input2, C_(p3)'s W edge, input4
and C_(p4)'s E edge form an eight-step first return from D_(q2) to D_(b+3).
Its ranks should differ by one, whereas q2=b+1. Contradiction. If there
are only four ports, the earlier forced fifth port already contradicts it.

Thus only the first possibility remains:

    (p0,p1,p2,p3)=(a+2,b-1,b,b+2),
    (q0,q1,q2,q3)=(a,b,b+1,b+2),
    a,b even and b>=a+4.                              (3)

## 2. No remaining port can occur

Cut both histories before rank h=b+3. All four marked ranks in (3) lie
before h, and no later mark can do so. Both prefixes have signed marked
sum2, hence equal E and W counts. Horizontal matching separates exactly
across this cut.

The suffixes begin L because h is odd. Their remaining lower inputs,
indexed j'=j-4, have identity output, length3 and voltages1,0,1,0,... .
The parity-padding extension of `axis_reverse_bounce_obstruction.md`
applies to these matched suffix histories and excludes every nonempty
such port system. Therefore m=4, or equivalently n=5.

This bounds the SECOND row in the r=2 branch with no cap on any higher
row. The third row still has the free even parameters a,b and possible
unmarked prefix/suffix visits. No all-axis exclusion is claimed here.
