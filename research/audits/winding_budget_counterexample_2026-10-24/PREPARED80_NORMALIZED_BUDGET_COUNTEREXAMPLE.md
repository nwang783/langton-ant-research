# A literal prepared80 counterexample to the normalized winding-input budget

24 October 2026. Exact supplied-word certificate, independently reconstructed after discovery. Peer review requested. The discovery search and its coverage are not premises.

## Result

The proposed actual-front inequality

    gcd(|dx|,|dy|) * (sum of absolute boundary windings - 1)
        <= 2 * min(consumed-input roots, permanent-output roots)

is false for a complete alternating PREPARED translating front. The following word has full period80, full drift(4,4), initial heading N:

    RRRRLLLLRLRRRRLLLLRLRLRRRRLRRRRLLLLRLRRRRLRRRRLLLLRLRRRRLRLRLRRRRLRRRRLLLLRLLRRL

Its primitive turn-word period is80. There are31 complete full-drift read classes, two consumed-input roots, fourteen output roots, no internal lifetime cycles, and two boundary circuits. One circuit has winding magnitude3, one input and thirteen outputs; the other has winding0, one input and one output. Thus m=4 and S=3, and the proposed inequality would require8<=4.

The two input reads are phases15 and21. The output phases are2,38,39,44,50,53,54,55,57,62,63,68,74,77. Input21 and output77 are DISTINCT lifetime endpoints at the same physical class. They are not merged.

The certificate reconstructs every actual event, all stable-class chronological reads, every R-to-next-L matching and full voltage, the exact actual-step conjugate matching, all16 fibre paths, both boundary cycles, and every one of the eight full horizontal/vertical fibre noncrossing pairings. It is not a relabelled abstract matching.

## Full physical preparation and all-N proof

Put d=(4,4), C={(-1,-1),(-1,0)}, and A={(0,1),(3,2)}. A single word executes from the actual four-black finite board C union A. The exact final board is

    (C+d) union O,

where the following fourteen cells are actual permanent R outputs relative to this period:

    O={(-1,2),(-1,3),(0,3),(0,4),(1,-1),(1,2),(1,3),
       (1,5),(2,-1),(2,5),(3,-1),(3,1),(3,2),(4,0)}.

Every later input copy A+j*d, j>=1, is missed by this entire word. Exact104-free ray arithmetic over the80 actual read phases proves that no O lifetime is read at any later event of the infinite repeated word. Different O copies do not alias.

Therefore, for EVERY integer N>=1, the finite seed

    C union {a+j*d: a in A, 0<=j<N}

has2+2N black cells and executes exactly N full words. Its full final board, without deletion, is

    (C+N*d) union {o+j*d: o in O, 0<=j<N},

of size2+14N, at head N*d,N. This follows by exact field induction, not extrapolation from named controls. The certificate also literally replays N=1,2,3,10,100 with all fields and all input ownership.

With no further paid input, the finite seed agrees with the next word through its first15 reads and then disagrees at absolute read80N+15: the expected next input at(0,1)+N*d is WHITE, so the actual ant turns R rather than L. Thus this is NOT a finite-seed autonomous controller.

For a complete forward prepared front, use the full initial board

    C union {a+j*d: a in A, j>=0}.

For a bi-infinite translating full board, additionally retain every old output copy

    {o+j*d: o in O, j<0}.

All those old outputs are unread by the forward trace. The exact one-period field equation then translates this ENTIRE infinite board by d. No missing negative-period output archive is cropped to fabricate the counterexample.

## Full-period representation and scope

The certificate reconstructs powers1,2,3,5. They have m=4q, I=2q, O=14q and S=3, so the failure remains8q>4q. At q=3 the winding3 component splits in the genuine full-period cover, while total absolute winding stays3. No primitive-drift quotient is substituted for the physical full quotient.

This refutes the named gcd-normalized budget for arbitrary prepared fronts. It does NOT refute a complete-WHITE unit-winding statement, exclude or realize any of the four live WHITE boundary types, supply a finite-seed noncanonical controller, or refute global finite-seed attraction. The need for infinitely many prelaid inputs is explicit.
