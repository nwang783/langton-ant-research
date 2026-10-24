# A finite prepared plateau is above the exterior or touches a black input corner

23 October 2026. Complete cap-four translating front with arbitrary prepared first colors, actual full P,d. Let B be the number of initially BLACK physical cell classes in the actual full quotient. B is finite, but the input board need not have finite black support in the plane. Original WHITE fronts have B=0; their time reversals have B=N_odd. No original-fuel conclusion is made.

## 1. Prepared local-maximum theorem

Let Q be a finite full-quotient corner-connected component of C faces of one height lambda. Assume it is locally maximal: every C face touching a Q face at a primal corner has height<=lambda. Then at least one of the following holds:

    lambda>c_right;
    some initially BLACK physical cell touches a face of Q.

More precisely, if no initially black cell touches Q, Q has an embedded WHITE-selected first-L birth cycle with actual cursor retreat K_Q=lambda-c_right>=1. Black initial cells elsewhere are retained.

## 2. Positivity when the whole plateau collar is WHITE

Assume Q has no initially black incident corner. For a face F in Q and an edge-neighboring L face J, nonnegative flow gives h(J)<=lambda. If h(J)=lambda, local maximality and nonnegative flow force all four C neighbors of J to height lambda, in Q, and all four J boundary flows to zero.

Each corner of J touches Q and is initially WHITE. Either possible first R turn at that cell would use at least one zero J edge, so the cell cannot be visited. All its physical port flows vanish; the opposite diagonal L face therefore also has height lambda, and its adjacent opposite C faces also have height lambda in Q.

Repeat along the connected diagonal L contact lattice. Every newly encountered corner still touches Q and hence is WHITE by the hypothesis. There is no concealed black corner at which this propagation may stop. It would force every C and L height in the plane to lambda, contradicting c_right-c_left=1. Thus equality is impossible:

    every L neighbor of Q has height<=lambda-1,
    all four physical boundary ports of every Q face are positive.

This reconstructs the signed WHITE plateau positivity proof with the exact smaller hypothesis it uses: WHITE on the whole incident Q collar, not WHITE everywhere.

## 3. Birth and cursor closure need WHITE only on Q's selected contacts

Every Q face has a well-defined earliest first boundary departure. At its minimizing corner the complete history begins R, because that corner touches Q. The cap-four negative first-port argument and local C maximality give a flat incoming canonical contact from another Q face, with birth descent at least5 in predecessor orientation.

Finite quotient closure gives an embedded essential parent-to-child cycle inside Q, full winding+1 in actual drift orientation. Strict birth inequalities exclude a contractible cycle. At its selected contacts the complete WHITE crossing inventory is R0 LEFT->RIGHT, R2 RIGHT->LEFT, with optional L3 on one side. No other visited cell, black or white, lies on that embedded cut.

The actual cursor pairing and disjoint side-current argument therefore give a positive retreat K_Q, while the stream split gives its right-current homology c_right-lambda. Consequently

    K_Q=lambda-c_right>=1.

Prepared black histories OFF the cut remain part of its physical currents. They do not affect the selected-contact pairing or justify dropping a side component. This proves section1.

## 4. A same-height component capacity

Fix a height lambda<=c_right and any family of distinct finite locally maximal components Q at that height in the actual full quotient. Each must touch a black input class. One black cell can touch only its two incident C faces; if both are at lambda they are corner-adjacent and belong to the SAME component. Therefore a black class cannot be assigned to two distinct such components, and

    number of these same-height components <= B.

This counts whole plateau components, not faces, branches, or selected roots. It does not say that all their birth chains are acyclic, that every black corner is selected, or that an arbitrary zero-port plateau has a canonical birth at every face.

## 5. Exact reverse output interpretation

For an original complete WHITE front, reverse time and reverse the heading. Reverse drift is -d; reverse C faces are original L faces; h_rev=-h and c_right_rev=-c_left. Original odd classes end BLACK and are exactly the reversed initially-black classes. Thus B_rev=N_odd.

An original L-face component at height m, finite in the full quotient and locally MINIMAL, becomes a reverse C maximum component at lambda=-m. If m>=c_left, section4 yields

    number of these same-height L-minimum components <= N_odd.

In particular each touches an original odd-output cell. If such a component has NO odd-output incident corner, section3 instead forces m<c_left and supplies an essential reverse selected birth curve with K_Q=c_left-m>=1.

This is an output-root OR essential lower-counterflow alternative. The lower essential option is retained, and a zero-total-homology sheet is not declared empty. No bound on original seed roots, forest branch count, global genus or all-cap fronts follows.

Dependencies reconstructed locally: signed finite local-maximum plateau criterion fb1c92ce, canonical first-L birth c9171009, cursor counterflow30b6aab0 and stream sign2e940091. The prepared boundary cases are handled by the explicit black-corner alternative rather than silently importing a WHITE reverse theorem.
