# Exact low-height excursion elimination

Status: proposed all-length mathematical lemma, pending independent review and
implementation. It is not a DCUV exclusion.

Fix a packet language DFA, the global record phase, and a cutoff L low enough
that every packet begun at head height q<=L has all its residual input and output
heights <=F, and obeys the old-record core/created-peak height constraints. Such
an L exists, because packet offsets are a fixed finite set. High residual
resources therefore remain unchanged during a segment whose every packet START
and END head height is <=L, except that every current identity ages by the total
number of C macros, saturated at4. Packet headings and DFA states remain exact.

Let W be the largest absolute packet head-height displacement. Every entrance
from the finite high zone into the low zone lands at depth d=L-q in0..W-1; every
last low packet before an exit also begins at one of these finite depths. Thus
low excursions have finitely many entry/exit ports: heading, DFA state and depth.

Introduce a one-counter graph whose counter is d>=0. An original packet edge has
fixed counter change -delta_q and fixed age weight c in0..2. Replace it by a
private chain of unit pushes or pops, or a zero edge. Put the weight c on one
chain edge and0 on the others. Original endpoint nonnegativity is equivalent to
nonnegativity along this monotone chain. Private intermediate vertices prohibit
switching between packets. The graph has finitely many vertices and its only
unbounded component is the stack of one repeated symbol.

For a fixed entry/exit port pair, the set of finite counter-nonnegative paths
between their exact finite depths is computed by balanced-path saturation. Add
fixed private initial pushes to the entry depth and final pops from the exit
depth, so the query has depth0 at both ends. A balanced relation R is the least
relation containing identity and zero edges, closed under concatenation, and
under a push edge followed by R followed by a pop edge. Every nonnegative
balanced walk is generated: split at its first return if it has one before its
end; otherwise its first push matches its last pop and the interior is balanced.
Conversely every grammar production preserves balance and nonnegativity.

Annotate R with the maximum saturated age weight in {-infinity,0,1,2,3,4}.
Concatenation uses saturated addition, alternatives use maximum. This finite
lattice saturation terminates, and its least fixed point equals the maximum
weight of genuine finite walks by the same induction. A maximum value4 is
attained by some finite walk with at least4 C macros, not by a fictitious limit.

Consequently each feasible port pair may be replaced by ONE summary edge with
its maximum saturated C count. This is exact for coverability in the high-token
height/age relaxation. All low paths leave the high token multiplicities alone;
more aging dominates less aging simultaneously at every height and threshold.
The maximum edge is itself realized by a finite legal-DFA low walk, so the
replacement introduces no spurious high-resource coverability. It also preserves
full cumulative height chronology, unlike an arbitrary unbounded-low-bin reset.

Initial low prefixes are a separate regular-stack-language query, because the
initial head height may be any q<=L with the prescribed heading parity and DFA
initial class. One explicit reduction adds a fresh source which pushes an
arbitrary number of counter symbols with age weight0, subject to the required
parity, then enters the chosen actual heading/DFA initial state. Querying any
finite exit port with the same balanced grammar gives exactly the feasible low
prefixes and their maximum saturated age effect. There are initially no high
identities, so this prefix age effect can equivalently be ignored once only its
reachable exit controls are retained. Initial high-zone poses are retained
explicitly. No assumption of a bounded initial low excursion is used.

This gives a finite and effective exact low-zone compiler. It does not by itself
bound the compiler cost, sign a model implementation, restore transverse
geometry, or settle either remaining record case.

## Explicit finite port formulas

Let R be the exact weighted balanced relation, P a single unit pop, and U a
single unit push. Products mean finite weighted path concatenation, with R
between successive unmatched edges. Every push/pop word reduces, by deleting
balanced subwords, to pop^k push^l. For entry depth d and exit depth e, exactly
k<=d and l=e-d+k are required. Hence the port relation is the finite maximum of
R (P R)^k (U R)^l over0<=k<=d and l=e-d+k>=0. For boundary depths0..W-1 one
also has l<=W-1. Conversely these products all give nonnegative counter paths.
This proves that the finite port query needs no extra graph vertices per port.

For an arbitrary initial depth, the reduced unmatched word has any number of
pops and at most e pushes, where e is its fixed exit depth. Thus initial-low
reachability is the finite-state weighted regular closure R (P R)^* followed by
at most e factors U R. Its maximum weights are found by a finite-lattice vector
fixed point. The original packet endpoint parity ensures that a path into a
physical exit port automatically selects an initial depth of the correct
heading parity; equivalently that parity can be imposed explicitly.

## Executed prototype, 2026-10-23

`build_low_height_unit_graph.py` expands each packet-DFA transition into a private
monotone unit chain. `weighted_dyck_summary.cpp` exports both the exact weighted
balanced matrix and a finite derivation DAG. The separate
`check_weighted_dyck_summary.py` checks every derivation node and every identity,
zero, concatenation and push/interior/pop fixed-point obligation. Derivations
prove the attained lower inclusion; full closure proves the upper inclusion.
No explicit stack-depth cutoff occurs in this certificate.

- k3:444 unit vertices,576 edges,10,196 balanced pairs,12,284 proof nodes.
- k5:4,300 unit vertices,5,712 edges,427,063 balanced pairs,503,641 proof nodes.

Both pass the separate author-side checker. `compile_low_height_ports.cpp`
implements the explicit unmatched-normal-form formulas and interns repeated
vectors. At L=-18,W=8 it reports:

- k3:208 ports,22,638 summary edges,162 initial-low reachable ports.
- k5:2,048 ports,1,420,787 summary edges,1,301 initial-low reachable ports.

These are compiler controls. No record model has yet been replaced by these
summaries, and there is no new no-hit invariant or independent implementation
signoff. The matrix/port files live under chronology_dcuv/delayed_height_probe
with prefixes low_k3_dyck and low_k5_dyck.
