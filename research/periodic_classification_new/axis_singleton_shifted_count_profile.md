# A parity-shifted second-row count profile at full axis-four drift

23 October 2026, 06:27 UTC. Independently signed analytic lemma (audit JZ).
No full-front exclusion is claimed.

Assume a complete white front has actual full drift (-4,0), and ALL four
cells in its lowest active row are singleton. Use the signed notation
C_i=(2i,1), D_i=(2i+1,1), i modulo 2. Let their complete read counts be
c_i,d_i. Their sole upward-arrival/downward-departure ranks are p_i,q_i.
The signed local branch theorem gives p_i=q_i for odd q_i and p_i=q_i+2
for even q_i. Put s_i=(-1)^q_i, so p_i has the same parity as q_i.

Define the reduced nonnegative counts

    C_i = c_i - 2 s_i,       D_i = d_i - 2 s_i.

Then

    floor(C_i/2) = floor(D_i/2),
    ceil(C_i/2) = ceil(D_(i-1)/2).                 (1)

Consequently, in physical row order (C_0,D_0,C_1,D_1), every reduced count
is m or m+1, with at most one adjacent high-count pair, exactly as in the
signed lowest-row count trichotomy after swapping the checker roles.
The all-zero case cannot occur because each reduced C_i is positive.

## Exact derivation

At C_i and D_i, the horizontal E-port bit at rank r is marked XOR odd r.
The single mark changes the total E count by s_i, so the E edge gives

    floor(c_i/2)+s_i = floor(d_i/2)+s_i.

Their W counts are respectively ceil(c_i/2)-s_i and ceil(d_i/2)-s_i.
The W edge from C_i to D_(i-1) gives

    ceil(c_i/2)-s_i = ceil(d_(i-1)/2)-s_(i-1).

Subtraction of 2s_i from an integer shifts both its floor-half and
ceil-half by -s_i. This proves (1). In the reordered variables
(a_i,b_i)=(D_i,C_(i+1)), (1) is exactly the already signed bottom-row
system ceil(a_i/2)=ceil(b_i/2), floor(a_i/2)=floor(b_(i-1)/2), so its
complete two-pair trichotomy applies without a new enumeration.

Nonnegativity is not automatic from the definition but follows from the
branch theorem. For odd q_i>=1, c_i,d_i>=q_i+1>=2, and subtraction adds 2.
For even q_i, p_i=q_i+2 forces c_i>=q_i+3. E-count equality then forces
d_i>=q_i+2. Thus C_i>=q_i+1>=1 and D_i>=q_i>=0.

## Two consequences

1. If q_0 and q_1 have different parity, the raw counts in the even-q
   column exceed the corresponding odd-q-column counts by at least THREE.
   The odd-q column has both raw counts at least two. Thus at least one
   cell in the even-q column is read at least FIVE times. This is an
   all-cap conditional local lower bound, not a global cap-four theorem.

2. Under visit cap four, the marks must have the same parity. They cannot
   both be even: the signed nonconstant-mark theorem would make the larger
   even mark at least two, so its C rank p is at least four and requires
   five reads. Hence, up to swapping columns, (q_0,q_1)=(1,3) and
   (p_0,p_1)=(1,3). The q=3 column has four reads at both cells. Applying
   (1) and the E floor equality shows the q=1 column has either three reads
   at both cells or four reads at both cells. Thus the only two second-row
   count profiles are (3,3,4,4) and (4,4,4,4), in the matching column order.

The result is conditional on a fully singleton lowest row. It does not
cover the two-singleton/two-empty family or nonsingleton bottom profiles,
classify higher rows, or exclude actual full drift (-4,0). Genuine rotations
transport it. No reflection or primitive displacement quotient is used.

Independent direct compass-port controls: `../audits/check_shifted_axis_profile_independent.py/json`. The control checks 361 column states and 5,992 matched pairs through count 20; the proof above is unrestricted algebra.
