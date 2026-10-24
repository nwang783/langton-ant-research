# A43-black growing-diameter closed-pose excursion

23 October2026,08:41UTC. Independently signed LF exact all-r certificate. A positive finite excursion family, not renewal or a counterexample.

Use the signed standard104 word H. Let J(x,y)=(-y,x), the counterclockwise
quarter rotation, and let K be the ten-cell corner stencil in the separately
signed `single_turn_highway_corner.md`. Let S_NE be the canonical13-black
standard104 seed with incoming E, hence drift(2,2).

For every integer r>=3 define

    d_r=(2r+3,2r+6),
    c_0=0, c_j=sum_{i=0}^{j-1} J^i d_r,
    I_r=((1,0)+S_NE) union union_{j=1}^3(c_j+J^j K).

These four sets are disjoint. I_r has EXACTLY43 black cells, all other cells
are white, and the actual initial pose is(0,0,N). The ant executes the word

    L_r=(R H^r H[:68])^3 R H^r H[:60].

It returns exactly to(0,0,N) after416r+268 reads. Its final black mass is
48r+87, so the signed charge gain is48r+44. Of the43 initial black cells,
11 remain black and32 are erased. The COMPLETE whole-board XOR has48r+108
cells. No remote marks or written sides are discarded.

This gives arbitrarily long, growing-diameter closed-pose excursions from a
constant number43 of initially black cells. Seed positions, not seed mass,
grow with r. It does not give one fixed seed with infinitely many excursions.

## Why the word stops eight reads before the tempting full loop

The geometrically closed four-corner word(R H^r H[:68])^4 asks forR at the
origin eight reads before its final end. The original firstR has already
made that site black. Truncating precisely there produces L_r, itself a
closed-pose word. Its next ACTUAL turn is thereforeL. Repeating L_r, or
finishing the nominal extra eight reads, is not licensed by this theorem.
In particular the43 input markers have NOT been renewed:32 were consumed.

## Exact checker contract

`certify_four_corner_loop.py` constructs all684 affine read-slot families.
Each H-arm slot has a repetition variable0<=i<r; the remaining cap and partial
period reads are individual affine families. Every family is injective in its
read index. Its literal chronological time is an affine function of r and x,
so all earlier same-cell relations are Presburger sets, with no finite cutoff.

For every target family the checker starts with the COMPLETE I_r coloring,
XORs all strictly earlier same-cell families, and compares the required turn
at EVERY r>=3. It finds1604 nonempty prior relations and no wrong-color set.
The complete output is the43-cell seed XOR every read family. Exact set tests
prove the11/32 retained/erased split and origin-black postcondition. The
endpoint and total charge formulas follow by the four rotations and the exact
prefix charges charge(H[:68])=charge(H[:60])=10.

The JSON records both full parametric fields and all43 affine seed points.
The r10 andr20 later-trajectory controls are only finite observations and are
not dependencies of this all-r finite-excursion certificate.
