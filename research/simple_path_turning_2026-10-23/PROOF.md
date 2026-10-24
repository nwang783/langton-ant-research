# Sharp order of signed turning for a simple square-lattice path

Frozen mathematical note, 2026-10-23. This is a self-contained proof from first principles, not a literature claim. No ant-dynamics assumptions enter the geometry theorem.

## Result and conventions

Let P=(v_0,...,v_n) be a square-lattice path with n unit edges and all n+1 vertices distinct. For each internal vertex, count a left quarter-turn as +1, a right quarter-turn as -1, and a straight passage as 0. Let T=L-R. (For the opposite convention S=R-L, take S=-T.) Immediate reversals are excluded automatically by vertex simplicity.

For n>=2,

    |T| < 8 sqrt(n-1) + 2.

For n=0 or n=1, T=0. In particular, the largest possible absolute signed imbalance is Theta(sqrt(n)), not Theta(n). The numerical constant 8 is safe and is not asserted optimal.

Standard outward square spirals have n=floor((q+1)^2/4) unit edges and T=q-1 when they have q straight runs of lengths 1,1,2,2,3,3,..., turning left between runs. Thus |T|/sqrt(n) tends to 2. One may extend the final outward run by any number of straight edges without losing simplicity or changing T, giving the same lower order bound for every sufficiently large exact n.

## Step 1: replace the polygonal arc by an embedded regular C1 arc

Assume n>=2. Truncate the first and last edges at their midpoints q and r, discarding a total length 1. The remaining polygonal arc has length n-1, distinct endpoints, and exactly the original internal signed turns.

At every nonstraight lattice corner, round it by a circular quarter-arc tangent to the two incident edges, using radius epsilon<1/4. Use disjoint disks around the lattice vertices and epsilon small enough that neither endpoint is affected. Each rounding replaces length 2 epsilon by (pi/2) epsilon, so length cannot increase. Square-lattice vertex simplicity implies that nonincident unit edges do not intersect, so this rounding preserves embeddedness. Call the resulting regular C1 arc gamma:[0,1]->R^2, parametrized by arclength rescaled to [0,1], with length ell<=n-1.

The lifted tangent-angle increment of gamma is exactly (pi/2) T. All rounding disks have centers at lattice vertices and radius<1/4. This placement will preserve the precise half-integer ray intersections used below.

## Step 2: tangent rotation is the difference of two endpoint polar increments

For 0<=s<t<=1 define the secant direction

    F(s,t) = (gamma(t)-gamma(s))/|gamma(t)-gamma(s)|.

Because gamma is embedded, this is well-defined off the diagonal. Because gamma is regular C1, it extends continuously to the closed triangular domain 0<=s<=t<=1 by

    F(s,s) = gamma'(s)/|gamma'(s)|.

The closed triangle is contractible, so the map F into the unit circle has a continuous real argument lift theta(s,t). In particular, theta(s,s) is a lifted tangent angle.

Let A be the polar-angle increment along gamma about its initial endpoint q, starting from the forward initial tangent. The nonzero chord gamma(t)-q has this continuous limiting initial direction, so

    A = theta(0,1)-theta(0,0).

Let A_rev be the same polar-angle increment for the reverse arc, about r, starting from the reverse initial tangent at r. Reversing the secant direction multiplies it by -1, which adds a constant pi and does not affect increments. Consequently,

    A_rev = theta(0,1)-theta(1,1).

Therefore the exact identity is

    (pi/2) T = theta(1,1)-theta(0,0) = A-A_rev.

There is no uncontrolled multiple of 2 pi: all increments are read from the single continuous lift on the triangle. This is precisely why embeddedness matters.

## Step 3: bound either endpoint polar increment by counting ray crossings

Consider the initial endpoint q. Translate and rotate the original lattice path so its initial directed edge goes from (0,0) to (1,0), and therefore q=(1/2,0). The initial tangent angle is 0. The perpendicular upward ray is

    R_plus = {(1/2,y): y>0}.

Every intersection of the rounded arc with this ray occurs at the midpoint (1/2,j) of an original horizontal unit edge, with j a positive integer. Indeed, the ray misses every lattice vertex rounding disk (its horizontal distance from every lattice vertex is at least 1/2), and no vertical lattice edge lies on it. Since the original path has no repeated edges and the rounded arc is embedded, all such intersections have distinct positive integer heights. An intersection at the terminal endpoint r is allowed. The original starting edge cannot meet this ray again after q.

First suppose A>=0. Let k be the number of nonnegative integers j for which

    pi/2 + 2 pi j <= A.

If k=0 then A<pi/2. If k>=1, take the successive first hitting times of the lifted polar-angle levels

    alpha_i = pi/2 + 2 pi (i-1),    i=1,...,k.

These times increase strictly. Their ray intersections have distinct positive integer heights h_1,...,h_k. Between first hits of alpha_i and alpha_(i+1), the intermediate value theorem forces a hit of angle 3 pi/2 + 2 pi (i-1), on the downward perpendicular ray. Such a point has y-coordinate a negative integer and hence y<=-1.

The arc length is at least the total vertical variation from q through the kth selected intersection. Hence

    ell >= h_1 + sum_(i=1)^(k-1) [(h_i+1)+(h_(i+1)+1)]
         = 2 sum_(i=1)^k h_i - h_k + 2(k-1)
         >= k^2 + 2(k-1)
         >= k^2.

For clarity, the weighted-integer inequality in the penultimate line does not assume the h_i are ordered. If a_1<...<a_k are their order statistics, then

    2 sum h_i - h_k >= 2 sum a_i - a_k
                          >= 2(1+...+(k-1))+k = k^2.

Therefore k<=sqrt(ell), and by the definition of k,

    A < 2 pi k + pi/2 <= 2 pi sqrt(ell) + pi/2.

If A<0, reflect the picture across the initial edge and repeat with the downward ray. Thus in all cases

    |A| < 2 pi sqrt(ell) + pi/2.

Exactly the same proof applies to the reverse arc from r, after its own lattice translation and rotation, giving the same bound for |A_rev|. The reversal starts at the midpoint of the last original unit edge; endpoint truncation and all ray-intersection assertions remain valid.

## Step 4: combine the two endpoints

Using the exact identity and the triangle inequality,

    (pi/2)|T| <= |A|+|A_rev| < 4 pi sqrt(ell)+pi.

Consequently

    |T| < 8 sqrt(ell)+2 <= 8 sqrt(n-1)+2.

This completes the proof.

## Distinctions and limits of the conclusion

- Signed versus unsigned turns: a monotone staircase E,N,E,N,... has a turn at every internal vertex, so unsigned turns equal n-1, while signed turns alternate and have magnitude at most 1. The theorem does not bound unsigned curvature by O(sqrt(n)).
- Lifted tangent versus endpoint compass headings: endpoint headings determine T only modulo 4. The theorem concerns the full lifted tangent rotation, which is unbounded on square spirals. Replacing it by a principal angle would be a mistake.
- Open versus closed paths: a simple closed square-lattice polygon has signed quarter-turn total +4 or -4, including the closing corner. If one writes it as an open list with repeated terminal/start vertex but omits the closing-corner turn, the internal total differs by at most 1. It is not the n+1-distinct-vertices convention above.
- Vertex-simple square-lattice paths are geometrically embedded: any intersection of unit horizontal/vertical lattice edges occurs at a lattice vertex, so distinct vertices prevent both crossings and self-contacts.
- Crossings invalidate the result, even without edge repetition. Explicit construction: from base (3i,i), traverse a clockwise unit square with steps E,S,W,N, returning to its base; unless it is the final square, then take steps N,E,E,E to the next base. For m squares, n=8m-4 and R-L=4m-1. All undirected edges are distinct and there are no immediate reversals. Each intermediate base is visited on two transverse passes, one horizontal and one vertical. Thus edge simplicity alone does NOT suffice.
- Noncrossing repeated-vertex contacts require a stated convention. The theorem as stated does not silently admit them. There is a useful extension: if edges are not repeated and every degree-four repeated vertex is paired into two adjacent-edge passages (rather than two transverse straight passages), those contacts can be rounded into disjoint tiny arcs preserving every signed turn. The same embedded-arc/ray proof then applies. General repeated-edge, overlapping, or crossing walks need not satisfy any O(sqrt(n)) bound.

## Verification controls

verify_examples.py deterministically generates the spiral and crossing-chain families, checks edge lengths, no immediate reversals, vertex or edge uniqueness as appropriate, exact lengths and signed turns. It is a check of the explicit constructions, not a substitute for the proof.

enumerate.cpp is a small independent exhaustive checker for short vertex-simple walks. It found maximum positive CCW imbalances 4,6,7,9 at n=8,12,16,20 respectively. These finite data are not used in the proof or in any asymptotic claim.

## Ant interface (conditional, supplied separately by the global analysis)

If a separate exact zipper theorem supplies an n-edge vertex-simple bridge path, n<=M, whose signed turning controls a phase mass increment by Delta M<=S+4 up to a stated O(1) endpoint convention, this geometric result supplies Delta M<=8 sqrt(M)+6 plus that explicitly stated endpoint correction. This note proves only the geometric bound. It does not certify the zipper theorem, the bridge-path simplicity, or a downstream global-time recurrence.
