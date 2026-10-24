# Mandatory south-arrival correction to the LL post-X RR gate

24 October 2026. Correction to frozen2554859e and its four-row executable
9307ff7a/cb7c747c. The geometric/role reduction and claimed contradiction
are unchanged, but one displayed ordinal edge was oriented incorrectly.

X=(1,0) EEWW departs SOUTH at ranks0,3. At B=(1,-1) NNSS these are
S arrivals ranks2,3, NOT N arrivals ranks0,1. The exact physical edges are

    X.R0 -> B.R2; X.L3 -> B.L3.

Replace section3's false T1(B)=T3(X)+1 by

    T3(B)=T3(X)+1.

B=NNSS departs E at ranks0,3, so its L3 gives C's SECOND E arrival:

    E2(C)=T3(B)+1=T3(X)+2.

The other side is unchanged: the two N outputs of C feed R.N ranks0,1,
and R.L1 immediately feeds X.R2, giving

    N2(C)=T1(R)-1=T2(X)-2<T3(X)<E2(C).

Both allowed flat C histories EEWW/EWWE have E2(C)<=N2(C), contradiction.
The corrected literal four-edge core is X.L3->B.L3->C.Esecond, and
C.Nsecond->R.L1->X.R2. All earlier B.N0/N1 and B.S2 remain present.

Only the corrected checker check_LL_post_X_RR_cap_corrected_edges.py/json
may be used as the executable ordinal certificate for this conclusion.
The immutable old executable's asserted N-arrival matching is erroneous
and must not be cited as independently verified. No physical erase,
fuel charge or broader whole-front result is introduced by this repair.
