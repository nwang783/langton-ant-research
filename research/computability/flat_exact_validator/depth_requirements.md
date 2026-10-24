# Depth-preserving legality and exact input-fuel certificates

2026-10-23 06:24 UTC. New implementation; submitted for separate review.
The signed JX same-board compiler is unchanged. This layer allows a DIFFERENT
entry board for each refinement depth and does not certify renewal or a wrapper.

## Complete depth-dependent input requirements

Use the same exact schemes and full preceding parity as JX, but retain the
visible depth r with its affine equality r=R_scheme(n) before projecting the
scheme exponents. This gives automatic relations Black(r,x,y), White(r,x,y)
containing ALL requirements of the single finite word phi^r(root).

Use four DISJOINT orthants: a negative-sign magnitude is required to be>=1,
whereas zero belongs only to the positive sign. Thus each physical cell has
one representation. The language of bad depths is exactly

    exists x,y: Black(r,x,y) AND White(r,x,y).

For every good depth, Black(r,.,.) is its exact minimum initial black set.
Every finite word has a finite footprint, so no extra finiteness hypothesis
is needed in this per-depth question. This establishes internal legality at
all depths by a finite automaton emptiness test, not a finite-depth replay.

## Exact count as a Z-weighted binary automaton

Let A be the deterministic automatic relation for one disjoint Black orthant.
Its three digit inputs are (rbit,xbit,ybit). For b=0,1 construct the nonnegative
integer matrix M_b whose(q,t) entry counts the four possible coordinate-digit
pairs (xbit,ybit) taking q to t with rbit=b. A chosen complete coordinate pair
has exactly one deterministic automaton path.

Let C be the largest magnitude of any individual occurrence edge coordinate.
Every depth-r read position is a sum of r such edges, hence |x|,|y|<=C*r. If
the visible r encoding has length L, c=bit_length(C)+1 extra bits suffice for
all coordinates: C*r<2^(L+c). Append c forced-zero r bits, still summing their
x,y digits. The accepting column is therefore M_0^c times the ordinary
acceptance column. For ANY finite binary word representing r in LSB-first
order, including empty/all-zero words and extra zero padding, its resulting
integer weight is EXACTLY the number of black input cells in that orthant.
The finite extra padding counts each coordinate exactly once, not multiple
encodings. The relation itself rejects coordinates outside the actual support.

Direct-sum the four orthant representations. This is an exact integer-linear
representation of the full required input mass m(r) at every good depth.
On bad depths it still counts the black requirements, but should NOT be called
minimum realizable fuel.

## All-input equality with a proposed exact fuel function

An affine function alpha*r+beta has a three-dimensional LSB representation
tracking(value,place,1). The bit-b transition is

    value <- value+b*place; place <-2*place; 1<-1.

The indicator of r=0 has one-dimensional matrices M_0=1, M_1=0. Thus affine
functions with a zero-depth correction can be compared exactly by taking the
direct sum of the mass automaton and the negative proposed function.

For the resulting rational representation, compute the Q-linear span of all
reachable row vectors, starting with the initial row and closing under both
bit matrices. This terminates in at most its finite ambient dimension. The
series is zero on EVERY finite binary word iff every reached basis row is
orthogonal to the final column. This is an exact finite proof of the proposed
identity at all depths, not fitting a formula to sampled values.

## Executed controls

`depth_requirements.py/json` independently of the specialized index formulas
constructs these relations and weighted identities from the supplied images:

- Identity R: all depths legal, input mass0.
- Identity L: all depths legal, input mass1.
- Rooted flat R5: bad-depth language exactly r>=1.
- Positive oblique hairpin: bad-depth language empty; input mass exactly6r.
  The weighted proof has54 dimensions and22 reached basis rows.
- Positive axial hairpin: bad-depth language empty; input mass exactly
  4r+2-2*[r=0], namely0 at depth0 and4r+2 for r>=1. The weighted proof has
  25 dimensions and10 reached basis rows.

There are additionally25 complete literal depth replays per control. They
exercise semantics but do not supply the all-depth assertion. Both input-fuel
identities were previously established independently by physical tile tables;
this is a generic image-to-automata derivation rather than a new stronger fuel
bound. No finite-seed growing path, complete renewal device or arbitrary
wrapper theorem is claimed.
