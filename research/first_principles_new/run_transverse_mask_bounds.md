# Transverse net-mask bounds for homogeneous spine runs

22 October 2026. Independently analytically audited geometric lemmas about the already proved permanent-spine decomposition, including the sharper four-bit transverse bound. These are not a highway-attraction argument.

Use cuts immediately before permanent entry, after any B at that root, as in `quantitative_boundary_mixing.md`. For a finite interval I let M(I) be the symmetric difference of its two endpoint black sets. A line count means the cardinality of the intersection of M(I) with that entire lattice row or column, not the number of reads on that line.

## 1. Every completed packet has at most two net changes on any row or column

A G packet toggles the four corners of an axis-parallel rectangle, so the assertion is immediate.

For a north-facing B_R based at (0,0), its mandatory north G has depth n>=0. With no second finger, the net mask is the four corners

    (0,-1), (1,-1), (0,n+1), (1,n+1).

With the second, east G of depth m>=0, the net mask is

    (0,-1), (0,n+1), (1,n+1), (1,0), (m+2,-1), (m+2,0).

The three x coordinates and the three y coordinates displayed are distinct. Thus each row and column contains exactly zero or two mask points. Rotation, translation, and the reflected L case preserve the bound. This claim concerns the NET mask, not the much larger read footprint.

## 2. A horizontal exponent-two block changes at most four cells per column

For an R-start eastward block, put its core on rows y=0,-1:

    w_k=(2k,0), u_k=(2k+1,0), l_k=(2k+1,-1), v_k=(2k+2,-1).

All core reads, parent B-face masks, and east G masks lie in these two central rows. Outside those rows, the only net changes are far corners of north and south G fingers.

At north column pair {2k,2k+1}, the two apparent finger sources are the mandatory north G inside an optional B_R at w_k, and the optional G_L at u_k during the R stage. They are mutually exclusive by `b_packet_spine_constraint.md`: a preceding B at this exponent-two parent has two fingers and forbids the ensuing optional child1 G. If the B is the last post-core packet and the ensuing stage lies outside the block, the latter optional G also lies outside. The first pre-cut B is excluded by the cut convention. The same reasoning applies to the mandatory G_R in B_L at l_k versus the optional G_R at v_k on south pair {2k+1,2k+2}.

Every fixed column belongs to exactly one north pair and one south pair. There is at most one included finger of each type, each with at most one noncentral far-corner bit on that column. Consequently M(I) has at most one upper bit, one lower bit, and the two central bits:

    |M(I) intersect {x=c}| <= 4.                           (1)

Partial first or last pairs only omit possibilities. Thus the same bound holds for an L-start block and for an odd number of stages. Its rigidly rotated version says that a vertical exponent-two block changes at most four cells on any fixed row.

## 3. An exponent-one block changes at most eight cells per row or column

Except for the final two root neighborhoods, all B packets in a consecutive exponent-one block are the forced depth-zero, one-finger packets. In the northeast R-start coordinates, their entire read footprints and the core lie in the diagonal band

    -1 <= x-y <= 2.

For example the R packet at (k,k) has word RLLLLRRR, and the L packet at (k+1,k) has word LRRRRLLL. Their literal footprints were checked in `check_alternating_spine_local.py`. Hence the union of the ordinary part's net changes meets any row or column in at most four points.

Keep the last two possibly unrestricted B packets separate. Each adds at most two net-mask points per line by Section1. There are no G packets at exponent-one stages. Therefore

    |M(I) intersect any fixed row or column| <= 8.         (2)

If the block has fewer than two stages, simply put every B into the exceptional set. The core is still in the same four-wide diagonal band. For an L-start block, a rotated diagonal band gives the same row/column bound. Pre-cut B packets are already absorbed into the initial field.

## 4. A limited but useful fuel-transfer corollary

The charging proof for an R-start exponent-two run uses only the two parallel lines containing q_k and l_k. In the eastward coordinates these are rows y=1 and y=-1; for a vertical run they become two columns.

Thus a completed perpendicular exponent-two block can add at most eight black bits on the entire charge-line union of a later run. A completed exponent-one block can add at most sixteen. These bounds are independent of both blocks' lengths and every finger depth, and do not require the later run to occur immediately. They bound direct net-toggle/addition effects only, not indirect causal influence mediated by intervening runs.

This is only a bound on additions from the specified block. Other intervening blocks can add, remove, and reuse fuel. In particular, a parallel exponent-two block can have unboundedly many net changes on one of the later charge lines. No global well-founded fuel quantity, bounded run length, or attraction theorem follows from (1)-(2) alone.
