# Flat finite-base macro refinement: complete input/output certification

2026-10-23 06:34 UTC. New implementation submitted for independent review.
This extends JX to actual multi-read macro bases. It does not silently
subdivide a macro recursive symbol into a single-unit-read controller.

## Class and semantics

A state s has a finite NONEMPTY physical base word b_s and its incoming heading.
Literal execution gives its read table, outgoing heading and displacement v_s,
which may be zero or have arbitrary integer length. Its ordered nonempty
substitution image is a word of macro states. Concatenating the children's
BASE poses must match the parent base's incoming/outgoing headings and net
v_s exactly. These finite geometric checks are made before any color claim.

The physical word at depth r is obtained by applying phi r times, then
replacing EVERY resulting state by its full base word. The root need not be
prolongable. Reachable occurrence SCCs must be flat as in JX: at most one
internal child occurrence per state. No assumption is made that a base is
already internally ant-legal; inconsistent bases are detected as negative
instances, including a zero complete-parity base such as R^8.

The fixed-input-board version decides whether one finite board realizes every
depth word from the same initial pose. It returns its unique minimal seed when
one exists. The depth-preserving version lets each depth have its own board
and decides all-depth internal legality, complete input/output requirements
and proposed exact input-fuel functions. Only a separately checked prolongable,
growing root gives a growing infinite path; the transient capped-rod roots
below do NOT have that property.

## Exact extension of the signed JX machinery

The simple-cycle schemes still enumerate EVERY actual occurrence walk, because
that fact is purely about the finite ordered occurrence multigraph. An edge
is now weighted by the prefix displacement of preceding macro children.
A depth-r path ends at a macro base, not at one physical read. Split each
terminal scheme over every read j in that terminal base.

Let tau_sj be its base-relative read position, ell_sj its turn bit, and
c_sj the parity of earlier reads AT tau_sj within that base. For scheme
exponents n, its chosen physical read position is W(n)+tau_sj. Its complete
preceding parity is c_sj XOR the same earlier-sibling-block sum as in JX,
evaluated at this actual read position. This counts all earlier physical reads,
including internal base revisits, without replacing the macro by a unit label.

The parity recurrence has the same Laurent transfer matrix but its initial
vector is now the exact base-read parity polynomial B_s(X,Y), rather than1.
Choose common nonnegative coordinate shifts C,D for all occurrence edges and
constant shifts e,f for all base reads. The coefficient machine represents

    Q_s(r,x,y) at (r, x+C*r+e, y+D*r+f).

The rational series is (I-zT')^(-1)B', where T' is the edge-shifted matrix
and B' the constant-shifted base vector. Both are polynomial and the denominator
has unit constant. Zero numerator is handled explicitly. All remaining carry,
F2 bounded projection, both-color union, conflict/finiteness decisions and
finite-seed extraction are as in JX. Constant shifts are included in EVERY
sibling parity evaluation, not just the final root parity.

For depth-dependent fuel counts, the read coordinates satisfy

    |coordinate| <= C0*r+B0,

where C0 is the largest edge-coordinate magnitude and B0 the largest base-read
coordinate magnitude. A fixed extra bit count covering C0+B0+1 makes the
Z-weighted counting construction exact, including r=0 and leading-zero inputs.
The same rational reachable-row-space identity test proves proposed all-depth
fuel formulas.

## Concrete capped-rail presentation and executed complete tables

Let the prepared operators have A=LRRL, B=RLLR, D=RRRL, with the exact headings
and poses in `../../causal_reduction/unit_scale/axial_domino_transport.md`.
The central macro C is either LLLR or LRRRRLLR. A,B,D are fixed; phi(C)=A C B.
A transient root g has base C D and image A C B D. Thus its depth-r physical
word is EXACTLY A^r C B^r D for all r>=0. g is not prolongable.

The executable uses equivalent individual fixed physical labels for A,B,D;
the recursive C remains an actual multi-read base. It derives22 walk schemes,
with32 terminal base-read schemes for transport and40 for growth.

For BOTH families the bad-depth automaton is empty: every depth is internally
legal on its own prepared board. The complete input relation, output relation,
XOR and read-support relations are each compared to the supplied table by
exact automaton equality in four disjoint orthants. All16 equalities per family
hold for EVERY binary depth and spatial input, including r=0. No numeric fitting
or sampled spatial bound supplies these conclusions.

The exact minimum input masses are2r+3 (transport) and2r+2 (growth), proved by
weighted automaton equivalence. Both same-board questions are negative: the
required-black union is infinite and there are conflicting requirements across
depths. This does NOT exclude wrappers that genuinely alter the block's entry
board. The constructor's separate actual forward-orbit/capture result concerns
a different question and is not inferred from this local family compiler.

Additional generic controls accept an identity multi-read base and a two-state
cycle of identical multi-read bases, both returning the exact three-cell seed.
An identity R^8 base with complete parity zero is correctly rejected by its
internal alternating-read conflict.

No growing finite-seed trajectory, renewable builder, or general ant capture
theorem is produced. The original JX single-read and signed depth-layer sources
remain unchanged. This broader finite-base macro class is a genuine extension
of the EXECUTED compiler, not an assertion that its symbols already satisfy the
single-unit hypotheses of earlier architecture exclusions.
