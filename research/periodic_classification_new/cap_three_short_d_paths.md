# Short doubled paths after the same-type exclusion

22 October 2026. Sections 1–4 and the same-type exclusion are independently analytically reviewed.
They do not yet prove cap-three nonexistence.

Use A=AAB and B=ABB for the opposite first/third heading types, and D for
edges traversed twice. Its path source is a white RL cell with opposite
incoming headings; its sink is a white RL cell with equal incoming headings.
Both endpoint reads traverse their unique D edge.

## 1. Geometric length bound

All interior D turns are left, by `cap_three_same_type_exclusion.md`.
Four consecutive edges turning left at the three intermediate vertices
return to the source lattice point. That would give the degree-one source
an incoming D edge, impossible. Thus a D path has one, two, or three edges.
D circles remain the previously classified unit squares with adjacent
A,A,B,B. This reasoning takes place in the physical lift and also excludes
a longer essential path. A path's two quotient endpoints cannot be the
same class, since one is an RL source and the other an RL sink.

## 2. A three-edge path is BA

Normalize the path to

    p=(0,0) -> u=(0,1) -> v=(-1,1) -> q=(-1,0).

Both intermediate turns are left. The last read at q is L with incoming
south, and exits east into p. At p the resulting incoming east is its last
L, since its first R has incoming west. Let q's L time be T. Therefore
p's L occurs at T+1 and u's second D arrival at T+2.

If u=A, that arrival is u's middle L and it immediately feeds the first
D arrival at v. If v=A, this would be v's first R at T+3, but its third R
already fed q's last L at T-1. If v=B, this would repeat v's middle L,
which already fed q's last L at T-1. Both are impossible.

Thus u=B. If v=B too, q's last L is preceded by v's middle L at T-1,
which is in turn preceded by u's first R at T-2. But u's second D arrival
at T+2 is its third R. The intervening three reads are v,q,p, so there is
no middle L at u. Contradiction. Only u=B,v=A remains.

The two interior Whitney contributions therefore cancel.

## 3. The remaining curvature carrier

One-edge paths contribute zero. A two-edge path has exactly one A or B
corner and contributes respectively +1 or -1. Unit-square circles and
three-edge BA paths contribute zero. Hence, writing p_A,p_B for the counts
of these two-edge path types in the full-drift quotient,

    g/4 = p_A - p_B.

An exclusion or an injection p_A<=p_B would now exclude all white-input
cap-three translating fronts, without any period bound. That step has
NOT been proved here.

## 4. A one-A path forces a neighboring A

Normalize a one-A path as p=(0,0) -> u=(0,1) -> q=(-1,1), and put
r=(-1,0). Then u has D incoming north and outgoing west. The last L at p
has incoming east and is preceded by a read at r exiting east. The last
L at q exits south into r. These two r reads occur in that order, since
p's last L feeds u's middle L, which feeds q's first R.

The earlier r read cannot be L: such a turn exiting east would have
incoming south and require q's last L already to have occurred. Thus it
is R. It cannot be third R because r is read again later, so it is first R,
with incoming north. The later r read, reached after q's last L, cannot
be L: it would exit east into p for an impossible third read of the
complete double cell p. It is therefore r's third R, with incoming south.
Its middle L cannot have incoming south, because q has no other southward
exit. Hence its middle heading is north and r is AAB as claimed.

All three ordered read times at r exceed the corresponding read times at
u: r's first R directly precedes p's last L (after u's first R); its middle
L occurs after the consecutive rR,pL,uL,qR segment; and its third R occurs
two steps after u's third R.

This is not a contradiction: r may lie on another one-A path, on the A end
of a BA path, or on an AABB square. A drift-parallel propagation cannot be
excluded by treating stable times as a bounded function on the quotient.

## 5. Finite controls, not an exclusion theorem

`probe_double_path_imbalance.py/.json` exhausts the inverse first-L-fuel
trees through initial mass 6, and records only empty, B, and BA clean
complete D paths. The mass-7 run stopped at its node cap and is UNKNOWN.
The absence of A in these finite trees is motivation only, not a proof.
