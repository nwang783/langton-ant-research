# The upper zero-state launch needs an outward or older-next-branch birth

23 October 2026, 16:04 UTC. Analytic addendum to the pending two-max-launch
note, not yet independently reviewed. All branch suppliers are retained.

Use exactly the zero-state LEFT/RIGHT configuration of
K1_zero_left_right_two_max_launches.md. The RIGHT face F0 has lower-left
(0,0); its selected exit is B=(1,1). The next curve face F1 has lower-left
(1,1), canonical birth B(F1)=T1(B), and arbitrary LEFT/STRAIGHT/RIGHT type.
The outward upper maximum H has lower-left (-1,1), and Y=(0,1) has R0(S)
around H. Its upper-right corner is r=(0,2). The other C face at r is

    J with lower-left (0,2).

The necessary helper profiles in the two-max-launch note show that
B.R0 is supplied either by Y.L1 or by Y.R2. In either case there is at
least one complete local return between Y.R0 and that supplier. Hence

    T0(Y)<=T0(B)-5,
    B(H)<=T0(Y)-1<=T1(B)-10=B(F1)-10.              (1)

The last inequality uses T1(B)-T0(B)>=4. These are physical first-edge
birth times, not phase classes.

H's lower-right corner Y cannot be its negative first-port birth:
Y.R0 already chooses H. If H's birth is at r, its canonical parent is
J and the signed first-L birth gap gives

    h(J)=M, B(J)<=B(H)-5<=B(F1)-15.               (2)

If F1 is LEFT, J is the next curve face F2. Its canonical birth is the
next selected L1 time, strictly larger than B(F1). This contradicts(2).
Thus in this case H's birth must use one of its LEFT corners and its
parent has lower-left (-2,0) or (-2,2).

If F1 is STRAIGHT or RIGHT, J is the first unused LEFT C-contact
neighbor of F1. In this case the right-corner birth at r is possible
only if this specific next-face LEFT neighbor is itself maximum and
has the much OLDER canonical birth in(2).

Therefore the exact alternative is:

- H is born from a further LEFT max face across one of its LEFT corners;
  or
- the next curve face is STRAIGHT or RIGHT and has the specific max
  LEFT neighbor J, whose birth precedes that curve face's birth by at
  least 15 actual reads.

The lower branch G retains its separately signed further-LEFT birth
obligation. This addendum gives a chronological condition on the upper
branch rather than discarding its upper-right supplier. It does not
force two births to move LEFT, forbid a future-face branch, order H's
launch before G's launch, or imply a fresh resource or infinite regress.

Source: K1_zero_left_right_two_max_launches.md, SHA
8cfac7cf84007c000812736c7d5fe554b10fef28430869fa4730d710521e9162.
