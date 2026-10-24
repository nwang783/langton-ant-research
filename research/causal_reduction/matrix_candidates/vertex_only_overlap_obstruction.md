# First-visit obstruction with both source and target vertex overlap

23 October2026. Independently signed as audit GN after analytic review.
It strengthens coarse-vertex separation: arbitrary returns to an image's
OWN source and target coarse vertices are allowed. The global finite-seed
highway conjecture is still open.

## Hypotheses and conclusion

Let phi be an odd-length k>1 substitution on the four absolute movement
directions. Assume:

- every image alternates axes, and its first axis is given by one common
  permutation of the two source axes (either all preserve or all swap);
- its net displacement is A d for one expansive integer matrix A;
- every internal image prefix q in A Z^2 belongs to {0,A d};
- the first-letter map F and first-endpoint-arrival map H defined below
  are permutations of the four compass directions.

Then no rooted fixed point or first-letter-cycle limit of phi is an actual
finite-support ant. No spectral inequality rho(A)<k is needed. Full half-turn covariance is
SUFFICIENT to guarantee the F/H permutation hypothesis, but is not required.
Independent opposite images satisfying that hypothesis are also covered.
In particular,
loops at the source OR target of an image are not sufficient to escape the
first-L obstruction. A survivor in this family must internally read some
OTHER coarse vertex A z, with z not in {0,d}.

The proof uses the previously certified fact that blank and origin-black
initial states eventually enter nonzero-drift standard104 highways. It does
not assume that fact for arbitrary finite seeds.

## 1. Exact ownership of a scaled first visit

First treat an actual fixed point, with p(kn)=A p(n). Suppose n>0 is a first
visit to q=p(n), and write u=d(n-1),v=d(n) for its incoming/outgoing compass
letters. Any fine read of A q occurs in a block whose coarse source or target
is q, because the only image A-lattice offsets are0 and its own endpoint.
No block with coarse index below n-1 has either endpoint q. Thus A q is first
reached inside the incoming image phi(u), or exactly at its final boundary.
This remains true with arbitrary internal visits to the source vertex.

Let j(u) in[1,k] be the FIRST arrival of phi(u) at its endpoint A u. Let H(u)
be the movement direction arriving there, G(u) its final movement direction,
and r(u) the number of INTERNAL reads at A u before time k. If j(u)=k, r=0
and H=G. The first-visit time of A q is

    tau(n)=k(n-1)+j(u).

Its incoming direction is H(u). The final boundary at time kn has incoming
G(u) and outgoing F(v), where F is the image first-letter map.

## 2. Correct endpoint-color correction

All visits to a fixed lattice cell have the same time parity, hence their
incoming headings lie on the same axis. In particular G(u)=epsilon(u) H(u)
with epsilon(u) in{+1,-1}. The r internal endpoint reads flip that cell r
times. Therefore the boundary turn equals(-1)^r times its FIRST turn,
where turns are encoded+1 for R and-1 for L.

Let J be the actual outgoing direction at the first visit to A q. Elementary
quarter-turn algebra gives

    J=sigma(u) F(v),
    sigma(u)=(-1)^r(u) epsilon(u).

Both kinds of four-step loops are included. An all-R or all-L square can
preserve the incoming heading, yielding sigma=-1. A one-opposite-three-equal
square reverses the incoming heading, yielding sigma=+1. Assuming all loops
reverse the incoming heading would be WRONG; the displayed parity formula
is what handles both.

If r=0, the first read is the boundary read itself and the same formula
reduces to J=F(v). No read of a cell other than the endpoint affects this
calculation.

## 3. The first-visit context map is a permutation

The maps F and H are permutations by hypothesis and share the fixed
source-axis permutation. The first endpoint-arrival index j has the same
odd parity as the endpoint index k, so H has the image first axis. (For half-turn-covariant images, H(-u)=-H(u) and
F(-v)=-F(v), so this permutation hypothesis follows automatically.) For each
perpendicular context(u,v), define

    T(u,v)=(H(u),sigma(u)F(v)).

This is a permutation of the eight perpendicular contexts. Indeed H uniquely
identifies u from the output incoming direction; then multiplication by the
known sign sigma(u) and inversion of F uniquely identify v. Perpendicularity
is preserved by the common axis permutation.

Section1 says that applying T carries the actual context at a coarse FIRST
visit q to the actual context at the fine FIRST visit A q. Iterate this
statement at the ACTUAL new first-arrival time tau(n), not incorrectly
at kn. Pure inflation is valid at every such integer time. Every context
lies on a finite T-cycle, so
any first-L read at a nonzero q reproduces first-L reads at A^(mr)q for all
m>=0 and some r>0. Expansiveness makes these cells distinct. Finite support
therefore forbids every nonzero first-L cell.

## 4. Blank/origin contradiction

The unique minimal initial seed is now empty or{origin}; unvisited extra
black cells can be deleted without changing the path. Both such trajectories
return to the origin at time4 (RRRR or LRRR), and both eventually have a
certified nonzero-drift highway. They therefore visit the origin only finitely
often. But p(kn)=A p(n) gives p(4k^r)=0 for every r. Contradiction.

## 5. Root cycles and preservation under powers

Vertex-only overlap survives composition. Any internal point of phi^r(d)
in A^r Z^2 lies inside an outer phi-block at an A-lattice offset. It must
therefore be that block's source or target, hence A times a vertex of
phi^(r-1)(d). Injectivity reduces the lattice condition to membership in
A^(r-1) Z^2. By induction the point is0 or A^r d.

The first-letter map F is a permutation, with every root on a finite cycle.
Taking that cycle's power produces a fixed-root substitution with matrix A^m,
length k^m, the same vertex-only property, and a common axis permutation.
Its first map is F^m. Its first-endpoint-arrival map is H^m: apply the
first-arrival ownership argument to the endpoint of each finite expanded
image, reducing its incoming heading one level at a time. Thus both maps
remain permutations, and Sections1–4 apply to this power. No single-phase
identity is incorrectly asserted for the unsquared original root cycle.

## 6. A coordinate-mixing example

For k=9 and A=[[3,2],[2,5]], the eigenvalues4+/-sqrt5 are both greater than1.
This matrix is neither Gaussian scalar nor signed monomial. An east image
has compass counts E4,W1,N3,S1; a north image N5,S0,E3,W1, with source-axis
starts. The raw inventories have20 and4 words respectively.

Every internal A-lattice hit in these inventories is either the origin or
the image endpoint. For E, the only geometrically possible additional
A-lattice points in its bounding box are(-1,3) and(4,-1). With only one west
move it cannot reach x=-1 after three north moves; reaching x=4 needs four
east moves and at least three vertical moves, whose height is at least1
with only one south move. For N, the only additional
candidate besides the origin and its own endpoint is(3,2) or(-1,3); the
alternating slots and one-west budget forbid both. Rotating180 degrees
handles W,S. Thus the half-turn subclass is excluded by the theorem without
a long-prefix search. The separate finite scan also rejects four independent
images, which this permutation theorem does NOT automatically cover.
