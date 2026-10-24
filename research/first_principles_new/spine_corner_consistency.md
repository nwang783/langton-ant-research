# Finite square support as a spine-and-corner consistency problem

Status: exact reformulation following the audited module/inclusion theorem, with independent analytic review of the spine grammar, packet patterns, and consistency criterion. No attraction or finite-state reduction is claimed.

## 1. A finite-prefix-free infinite spine

After discarding finitely many updates, the autonomous module execution enters a root call that never returns. Inside any nonreturning call, one of its two child calls must eventually be nonreturning: each child has at most two completed returns, and otherwise the finite parent face would finish. This gives a unique nested chain of nonreturning calls.

Let a be a parent's sign and b its opposite. Its nonreturning child is either child1 or child2. Before entering that child permanently, the output has exactly one of the following forms:

    child1: a [optional B_b]
    child2: a [optional G_b] a [optional B_b].

A completed B at the chosen child leaves that child's root still requesting b, forcing immediate re-entry, which cannot return. A completed G at child1 instead leaves its root requesting a and permits advancement to child2. These are the only completed calls possible in the nonreturning parent's initial portion.

Every G/B word reduces to the identity in G. Thus the successive spine increments are a or a^2, with alternating a. This is exactly the stabilized boundary syllable sequence. Each syllable is decorated by at most one G packet and one B packet. Since a B is a unit-face circuit with one or two G packets inserted, there are at most three G fingers per spine syllable.

This is stronger than merely saying that arbitrary finite side bushes exist: each completed decoration is a straight ladder or a pair of perpendicular ladders. It does not bound their integer lengths.

## 2. Exact G packet data

For an R packet starting at (0,0), heading north, let its recursive depth be n>=0. Its duration is4(n+1), its final pose is unchanged, and its read support is columns0..n+1 in rows0,-1.

Its required initial colors, with R=0 and L=1, are:

- column0: both0;
- upper row, columns1..n: all0;
- lower row, columns1..n: all1;
- column n+1: both n modulo2.

Its net lamp-toggle mask is exactly the four rectangle corners. The L case is the reflected pattern with all colors complemented. Rotate and translate with the incoming pose.

For a B_a packet, the net mask is the XOR of the four corners of the unit a-face and the corner masks of its one or two inserted G_b fingers. Required colors can be checked sequentially by its exact grammar a G_b a^3 or a G_b a G'_b a^2. This requires no simulation of the doubled interior reads.

## 3. Corner-parity equation

Flatten the spine code into elementary events of two types:

1. one spine turn, with one required read and a one-cell toggle;
2. one completed G or B packet, with its finite required initial-color map and its finite corner-toggle mask.

For event i, let S_i be its required-read set, r_i:S_i->{0,1} its required initial colors, and M_i its net toggle mask. Let

    P_i(p) = XOR of 1[p belongs to M_j] over j<i.

A square initial coloring B_0 realizes this annotated code if and only if, at every event and every required point,

    B_0(p) = r_i(p) XOR P_i(p).

Necessity is direct lamp accounting. For sufficiency, induct on events. The equation ensures that the next event sees exactly its required pattern; the proven packet grammar then executes it and applies precisely M_i, establishing the next inductive state.

Therefore an infinite code is realizable from finite square support if and only if:

- all constraints on the same physical point assign the same bit; and
- the set of points assigned bit1 is finite.

Unconstrained points may be set to0. This is an exact constructive consistency test on every finite code prefix, and an exact mathematical criterion for the infinite code. It is not claimed to decide infinite consistency or finiteness algorithmically.

## 4. Equivalent chronological coset-block equation

The no-A-B-A theorem gives each physical point p a sequence of distinct coset blocks C_(p,0),C_(p,1),... . Let m_(p,j)<=6 be a block's number of reads, and b_(p,j) its first-read color. Square compatibility is precisely

    b_(p,j+1) = b_(p,j) XOR (m_(p,j) modulo2).

Finite square support means b_(p,0)=0 for all but finitely many p. Thus the infinite lift input is not arbitrary: it is the output of one persistent parity bit per physical point, passed from one nonrepeating coset block to the next.

The standard104 code demonstrates why this input cannot be replaced by a finite list of nonzero lift lamps: it requires nineteen fresh black cosets per period. Their colors are inherited through these physical-point parity chains. The exact all-epoch source is `standard_lift_infinite_seed_obstruction.md`, with executable certificate `certify_standard_lift_seed.py` and output `certify_standard_lift_seed.json`.

## 5. The exact remaining obstruction to a finite automaton

No-A-B-A bounds the reads of one lifted block, not the number of physical-point chains that remain relevant or the distance/time between linked blocks. Similarly, the packet grammar bounds the number of fingers per syllable, not their lengths. In the corner equation, a packet can demand an arbitrarily long white/black corridor and can create corner information arbitrarily far from its root.

All finite G depths occur from finite initial square seeds: the explicit pattern in Section2 has only n or n+2 black cells and executes G_R(n). Thus there is no seed-independent bound on transient packet size. An eventual bound depending on the seed remains a possible theorem, but is not established here.

A finite-state attraction proof would need an additional global result making the active corner/parity frontier finite up to translation and rotation, or otherwise proving stabilization of the packet code. Ordinary finite support does not itself provide that result. At the time of this formulation, decoration stabilization was an additional unresolved issue. The later independently audited theorem `periodic_core_decoration_stabilization.md` removes it conditionally: eventual periodicity of the undecorated boundary core DOES force eventual full translating periodicity. It does not prove that the core becomes periodic, or classify the resulting full period as standard104.

The useful new target is therefore concrete: show that every consistent spine-and-corner code with finite assigned-one set eventually has the standard104 decorations and syllables, or establish an independently classifiable finite frontier for such codes. This is exactly where the full conjecture remains open in this approach.

A separate exact witness in `static_lift_gauge_obstruction.md` rules out replacing these chronological chains by a universal pointwise gauge lambda(C)=B0(project(C)) XOR f(C). The same first-visited coset can have opposite first-read colors under two finite seeds whose projected initial bit is the same.
