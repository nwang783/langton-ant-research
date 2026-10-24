# Uniform geometric and lamp support for same-coset returns

Status: independently analytically audited consequence of the module interface. The cross bound was suggested by the global analysis. This note supplies the exact refined interface and endpoint convention.

## Statement

Let s<t be two read times of the same lifted right coset A, projecting to the physical point q. For every intermediate read time s<=r<=t, its physical point lies in

    {|x-q_x|<=2} UNION {|y-q_y|<=2}.                       (1)

Let B_s and B_t denote the physical black sets immediately BEFORE reads s and t. Then

    |B_s XOR B_t| <= 34.                                  (2)

The time gap, arm lengths, and total number of temporarily read points need not be bounded. These are return-excursion structure statements, not physical transience or highway attraction.

## 1. Which abstract calls can occur before the later A read?

Use the same rebase and finite interfaces as in `completed_fingers_and_no_interleaving.md`: after at most four initial equal turns, A is root, predecessor, or one of the two interiors of one root face. The initial prefix is contained in that face. If the later return occurs before or at this rebase, it is confined to the initial unit plaquette, so both claimed bounds are immediate.

Every abstract call encountered before the later A read must complete, unless the A read is its true terminal predecessor read. This is the already audited separation/conditional-completion statement.

A completed B strictly before t is impossible. Its root still requests the same sign, so it is immediately reentered; the return ledger permits no further completed return. An A outside that module cannot then be reached. If A is its predecessor boundary, reaching it would force the forbidden additional completion. Thus all fully completed abstract calls before t are G.

At most one abstract call can be terminally incomplete at t. It may be of type G or B, and its completion differs from its executed prefix only by the single read/flip at A at time t.

Each abstract module has at most one G return in its entire execution, by the return language {empty,G,B,GB}. These statements require no bound on return duration.

## 2. Exact cross table

The following poses use the equal-edge root w=(0,0), heading north, predecessor p=(0,-1). A complete R G finger at pose (x,y,N) is its east-going two-row ladder in rows y,y-1; rotate for other headings. The L version is reflected. A terminal B uses the full two-arm Q footprint, but only when the module's predecessor is A.

### A=w or p

Keep both root faces explicit. Their four child modules are abstract. For A=w, only the first child of either face may be terminal B; its two Q arms lie within the width-one axial cross about w. Every other abstract call is G. For A=p all four abstract calls are G, since none has predecessor p. Their north-going vertical rails and east/west-going horizontal rails lie within the width-one cross about p. The explicit face points also satisfy those bounds.

### A=x=(1,0) or y=(1,-1)

Keep the R face and its two L children explicit. Their eight physical points are

    (0,0),(0,-1),(1,0),(1,-1),(1,1),(0,1),(2,-1),(2,0).

The five abstract calls are the opposite root L module and four R grandchildren:

    root word   pose          G footprint                    predecessor
    L-root      (0,0,N), L    west rows0,-1                   p
    RL          (1,1,N), R    east rows0,1                    x
    RLL         (0,1,W), R    north columns0,1                (1,1)
    RRL         (2,-1,E), R   south columns1,2                y
    RRLL        (2,0,N), R    east rows-1,0                   (2,-1)

For A=x, only RL may be terminal B. Its additional north arm has columns1,2. All five G footprints, that extra arm, and the explicit points lie within the width-one cross about x.

For A=y, only RRL may be terminal B. Its additional east arm has rows-1,-2. All G footprints except RL lie within the width-one cross about y, as does that additional arm. RL's east arm has rows0,1, whose offsets from y are1,2; hence the entire interface lies within the width-two cross about y.

The L-side interiors are the mirror image. Initial-prefix points are in the same root face and satisfy the corresponding cross bound. This proves the uniform width2 assertion. Without the G-only refinement one gets the weaker width3 bound immediately from the full Q footprints.

## 3. Exact lamp-mask count and terminal convention

For the root/predecessor interface there are at most six explicit physical sites and four abstract modules. For the interior interface there are eight explicit physical sites and five abstract modules. Use the latter, larger numbers uniformly.

Each of the at most five G returns toggles exactly four rectangle corners. A complete B toggles at most six points: its positive cancellation height is a straight strip or an L-shaped union of two strips and the root square, whose mixed boundary has respectively four or six corners. This also follows directly by XORing the parent-face and inserted-finger corner masks.

There is at most one terminal incomplete packet. If it is G, it can be included among that module's at most five G packets. If it is B, it is an additional packet after a possible earlier G in that module. Thus the net changed-site set is contained in

- the at most8 explicit skeleton sites, including the initial same-turn prefix;
- at most5 complete-G corner masks, each of size4;
- at most1 complete-B corner mask, of size at most6.

The packet that ends at t has not yet read its final predecessor A, because B_t is the state before that read. Its prefix mask equals its completed mask XOR {A}; A is one of the explicit skeleton sites already counted. No additional site is needed for this endpoint correction.

Therefore the union has size at most8+5*4+6=34, proving (2). Overlap only lowers the count. The same convention also covers an endpoint in an explicit face, where no abstract packet is partially executed.
