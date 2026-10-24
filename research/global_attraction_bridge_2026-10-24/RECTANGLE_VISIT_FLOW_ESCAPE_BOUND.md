# A directed visit-flow hierarchy gives perimeter-exponential confinement

24 October 2026. Author proof; independent audit pending. This is an explicit quantitative consequence of the fixed ant sector and visit alternation. No literature-priority, capture, or universal fast-record-window claim is made.

## 1. Exact finite-interval local inequality

Consider ANY actual ant interval [s,t], retaining the complete board. Put D=t-s. Let M(v) count head CUTS at v among s,s+1,...,t, including BOTH endpoint cuts. Fix west and south as the two predecessor neighbors of each cell. Then

    M(v) <= 2 M(v-(1,0)) + 2 M(v-(0,1))
            + 1 + 2 [v=p_s] + [v=p_t].                 (1)

The same inequality holds for any choice of one horizontal and one vertical predecessor direction. These choices need not be the actual incoming directions.

Proof. The fixed checkerboard sector assigns one incoming axis and the perpendicular outgoing axis at every cell, hence fixes the direction of each physical edge. Among reads at v that use NEITHER its west nor south edge, there is only one possible incoming/outgoing pair: the east and north pair, in its sector-permitted order. Such reads all have the same turn letter. Actual successive reads at a cell alternate R and L. Consequently the total read count n(v) is at most twice the number of reads that DO use a west or south edge, plus one.

Charge each such edge incidence to a neighboring head cut. An incoming edge from a neighbor charges the preceding cut; an outgoing edge to a neighbor charges the following cut. Since each physical edge has ONE direction in this sector, each head cut at that neighbor is charged at most once for this edge. The two neighbors are distinct. The only possible missing incoming cut is the initial read at p_s, giving at most one extra incidence. All outgoing edges have their following head cut included, even the final update. Thus the number of exceptional reads is at most M(v-(1,0))+M(v-(0,1))+[v=p_s]. Finally M(v)=n(v)+[v=p_t], proving (1).

This argument uses the actual chronological alternation, not merely net turn imbalance, a lifetime stack, or hypothetical routing. A read using both predecessor edges may be charged twice, which only weakens the upper bound. Arbitrary unvisited outside BLACK cells remain present.

## 2. Exact Green-function confinement bound

Suppose every head cut in [s,t] lies in a W-by-H rectangle, W,H>=1, indexed 0<=i<W and 0<=j<H. Counts outside this rectangle are zero. Define

    K(i,j) = 2^(i+j) binomial(i+j,i)  for i,j>=0,
             0 otherwise;
    A(i,j) = sum_(a=0)^i sum_(b=0)^j K(a,b);
    S(W,H) = sum_(a=0)^(W-1) sum_(b=0)^(H-1)
                 (W-a)(H-b) K(a,b).

The zero-boundary recurrence A(i,j)=1+2A(i-1,j)+2A(i,j-1) solves the constant part of (1). Coordinate induction gives

    M(i,j) <= A(i,j)
              + 2 K(i-s_x,j-s_y) + K(i-t_x,j-t_y).

Summing over the rectangle yields the endpoint-sensitive bound

    D+1 <= S(W,H)
           + 2 A(W-1-s_x,H-1-s_y)
           + A(W-1-t_x,H-1-t_y).                       (2)

In particular

    D+1 <= S(W,H)+3 A(W-1,H-1)
         <= (WH+3)(4^(W+H-1)-1)/3.                   (3)

The last estimate follows by grouping K(a,b) by a+b: the unrestricted diagonal sum is 4^(a+b). Formula (2), not the loose final bound, is the primary certificate. One may minimize it over the four predecessor corner choices.

This proof includes width-one and width-two rectangles, arbitrary endpoint headings, both sectors, and intervals that start or end on the boundary. It supplies a constructive finite escape bound without first invoking no-bounded-orbit or counting all full-board configurations. It is exponential in W+H rather than WH. It is not asserted to be optimal.

## 3. What the hierarchy means

At a cell away from the two endpoint exceptions, a large cut count forces a correspondingly large cut count at a west or south predecessor. Repeating this implication produces a monotone spatial chain towards the selected corner. The exact weighted recurrence quantifies all such chains simultaneously.

This is a hierarchy of actual directed visit counts in ONE continuous interval. It does not order the lifetimes that generated those visits. It neither says that the complete BLACK field shrinks nor prevents a later return after leaving the rectangle. Outside visits break the interval hypothesis and must be accounted for separately.

## 4. Global head-record and local-drought consequences

Start at an arbitrary finite cut with one head position. Let N(D) count strict expansions of the historical HEAD rectangle during the next D updates, allowing all four directions. Each unit step expands at most one side by one, so the final dimensions satisfy W+H=N(D)+2. By (3) and WH<=floor((W+H)^2/4),

    D+1 <= (floor((N(D)+2)^2/4)+3)
               (4^(N(D)+1)-1)/3.                      (4)

Thus head-record count is at least logarithmic in elapsed time, up to the displayed polynomial correction. This is independent of the initial black mass, spacing, or full field. It is NOT a bound on pristine record gaps: early head records can occur inside an already prepared seed rectangle.

For a genuine pristine union-record drought confined to an old augmented W-by-H rectangle, (2)-(3) directly bound its length. Equivalently, a very long drought must have sufficient actual spatial extent. This complements the signed boundary peeling theorem, but does NOT force a fast clock window afterward. The signed MT family has growing rectangle dimensions and therefore does not contradict this bound, despite its fixed seed cardinality and permanently pinned full BLACK hull.

The finite forcing-window theorem says a nontranslator must have recurring long simultaneous droughts. The present bound adds a quantitative spatial cost for each confined episode. It does not prohibit those rectangles from growing, renew a fixed cohort budget, or prove standard104 uniqueness.

## 5. Verification scope

The accompanying checker exhausts all complete boards, head positions, and headings in selected fixed small rectangles, including width one and two. It verifies (1) at every confined prefix and (2) for every complete confined prefix. Separate literal MT histories retain all BLACK cells and verify the local counts, exact endpoint-sensitive recurrence, and head-record count. Their full terminal fields are compared with the retained signed fields.

These tests challenge the endpoints and both sectors. The universal theorem is the elementary directed-edge/alternating-read argument, not an extrapolation from the finite controls.
