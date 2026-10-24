# Phase28: a second central return and a protected complete future

## Complete finite-seed theorem

Let u=x-y and z=x+y. For every independent pair of integers m,k>=100, start the usual north-facing blank-board ant with exactly these three black cells:

    s=(-2m-19,-2m+8),
    Q=(-2m-2k-26,-2m-2k-5),
    C=(-2m+2k+27,-2m-2k-5).

The exact bivariate checker, retaining every initial cell and every later write, proves first contacts with s,Q,C at respectively

    104m+10005,
    104m+104k+16491,
    312m+312k+110526.

It proves standard SE phase-zero capture by

    416m+416k+173038,
    pose (25,-61), heading south.

More strongly, every read from time zero through the entire infinite future satisfies

    u >= -84, z <= 35.

The proof checks86,550,721 exact bivariate incidence exclusions and the infinite tail. The four discovery runs only supplied a candidate word decomposition; they do not prove any parameter claim. No earliest-capture claim is made.

## Why the full history matters

The previously audited two-cell phase28 family already has a nested return. Its first distant Q reversal runs NE into the original central history, whose output runs SW into a black cell written during the first retained-core recovery. That second interaction gives the SE tail at time312m+208k+111801, pose(45-2m,-26-2m), west, phase99.

The new C impact reverses this SE flight. Its comparison-model output runs NE back toward the central history a second time. Blindly continuing that clean model would be wrong. The new certificate starts at the ORIGINAL time-zero three-cell field and follows the entire return into that history. After its final NE flight, it reaches the fixed pose(28,-41), east, and undergoes a further6631-turn central interaction before the certified SE tail above.

Every parameter-length piece in the resulting word is a power of a cyclic standard104 word. Their repetition counts are

    m, k+1, m+k+2, m-8, k-13, k-9, m-29.

All other pieces are fixed words. This is a finite hierarchy of consumed old interactions, not a self-renewing controller or an unbounded defect-count construction.

## Exact archive interface

The small checker binds the old two-cell template to the new proof's first nine segments and to its audited complete color certificate. Including the actual initial cells, every finite write, and the canonical phase99 output core, the old two-cell fixed archive is supported in

    -84 <= u <= 80.

Its whole infinite future also satisfies u>=-84,z<=35. The SE tail's infinite incoming canonical wake is not silently placed in that fixed archive; it is handled by the established all-age ordinary-scatterer rule.

The first ordinary-core recovery ends at core-frame(-21,6), west, phase102. Its phase72 ray has base(-24,-3). Taking epoch k+1 gives the displayed Q. The old two-cell phase99 tail has phase72 base(53,-31), in the same core frame obtained by adding(2m,2m). A further exceptional SE hit sharing Q's row therefore forces epoch k-13 and exactly the displayed C. Its time agrees with the all-parameter first-contact check.

## Recurrent mass-five exclusion

Assume the previously audited critical-clock exposure, favorable-ten sector, and four-edge/four-cycle incidence lemmas. Fix m>=100 first, then let the four other cells escape every fixed finite set. The singleton phase28 parent has an outgoing SW front. An ordinary first remote hit escapes by the established58-unit guard, so the only remaining case is the exceptional Q above, with k tending to infinity.

In a four-cycle, write the other corners A=(Q.x,t), C=(r,Q.y), D=(r,t). The exposed vertical and horizontal gaps diverge positively. The z-clock implies z(D)->+infinity, since Q,D are the only positive-z-sign remote cells and Q has z->-infinity. Also u(A)=u(Q)-(t-Q.y)=-21-(t-Q.y)->-infinity. Thus A,D are outside the entire two-cell future. Only C can be read on its final SE tail; if it is not read, capture is already permanent.

An ordinary favorable C impact has u(C)->+infinity. Its entire recovery lies in u>=u(C)-58, avoiding the fixed archive u<=80 and the other corners, which lie behind it by the diverging axial gaps. The all-age incoming standard wake is covered by that ordinary-channel rule. The only exceptional possibility is the displayed C, so the complete three-cell theorem applies.

Now use only justified axial gaps, not an assumption about the absolute sign of t. Put g=t-Q.y->+infinity. Exactly,

    u(A)=-21-g -> -infinity,
    z(D)=-4m+22+g -> +infinity.

Consequently neither unused corner is ever read in the entire certified three-cell future, including its earlier prefix. This remains valid when t itself tends to negative infinity. The threshold may depend on fixed m.

For the four-edge orientation with a potentially SE partner C, the other two remote cells have the same forms A=(Q.x,t1),D=(C.x,t2), where t1,t2 are bounded. Their gaps above Q.y diverge; the same exact bounds exclude them. In the transposed orientation the prospective C has bounded x and y=Q.y tending to negative infinity, so it misses the old two-cell SE tail's bounded-z strip. The NW partner has u tending to negative infinity; the remaining bounded-column remote corner has z tending to positive infinity. Both miss the entire old two-cell parent, and capture is already permanent.

Therefore no recurrent mass-five fixed-pose subsequence can retain the phase28 core s_m for any fixed m>=100, under the stated incidence hypotheses. This is not a theorem about all arbitrary three-cell seeds, all retained cores, or arbitrary finite seeds.

## Reproduction

Run certify.py and certify_interface.py. The manifest pins all proof inputs and outputs; discovery data are deliberately outside it. The old complete two-cell certificate is blank_return_cap/r28_complete_certificate.json, SHA25697ed7332cd4d1883d0bf168baa6946a37429fb49fa8e5e59f4d7376995f9ed0f, in the independently reviewed blank_return_cap package.
