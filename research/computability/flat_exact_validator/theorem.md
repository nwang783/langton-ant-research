# Executed arbitrary-mass realization decision for flat typed refinements

2026-10-23 06:17 UTC. New restricted integrated implementation. Submitted for
independent analytic and executable review; no new ant model is claimed.

## Input and exact question

Supply a finite physical typing `physical[s]=(incoming heading, turn)` and a
nonempty ordered image for each letter. A turn is +1 for R/white and -1 for
L/black. Images are checked literally: each child's incoming heading agrees
with the current heading, and the complete image has exactly its parent's
unit displacement and outgoing heading. The spatial matrix is I.

Restrict the occurrence multigraph to root-reachable states. In every SCC,
each state may have AT MOST ONE internal child OCCURRENCE. Parallel children
are distinct, not merged. A recurrent SCC is consequently a simple directed
cycle; a singleton without an internal edge is transient. This is the flat
occurrence class, allowing arbitrary decorations, unequal image lengths,
multiple cyclic SCCs along a path, zero/nonzero cycle offsets and arbitrary
charge changes. It is precisely the polynomial-growth graph architecture;
a reachable SCC with internal branching instead gives exponential growth and
is returned as UNSUPPORTED, never as nonrealizable.

The executable decides whether ONE fixed initial board B makes EVERY word
phi^r(root), r>=0, an actual ant trajectory segment from the supplied root
pose. There is no seed-mass or coordinate bound. When the root is prolongable
and growing, this is exactly realization of its infinite rooted trajectory.
A nonprolongable family is also a valid input but acceptance then means the
same-board family question, not an infinite fixed word.

## 1. Every occurrence word has a unique scheme

For a path entering a cyclic SCC at state s, write its internal segment as
n complete laps of the cycle based at s followed by j internal edges, where
0<=j<cycle length. It then terminates or takes one external child occurrence
into a strictly downstream SCC. A transient state terminates or takes an
external edge immediately. Recursing over the finite SCC DAG gives finitely
many schemes

    u_0 v_1^(n_1) u_1 ... v_k^(n_k) u_k,    n_i>=0.

Every instance is an actual root-started occurrence walk. Every actual finite
occurrence walk has a UNIQUE scheme and exponent tuple, by its actual exits,
complete-lap counts and residual partial laps. This is stronger than the
signed general genuine-path cover: no occurrence order is rearranged and no
Parikh-only representation is used. Root-to-leaf walks of length r are
exactly the individual reads of phi^r(root).

Their leaf position W(n), depth R(n) and final turn are affine or constant.
All coordinates remain integral; negative positions are handled by four
sign orthants with natural magnitudes. Repeated zero-coordinate orthant
representations do not change any union, intersection or finiteness result.

## 2. Exact read parity and full preceding parity

Let Q_s(r,x,y) be the modulo-two count of reads at (x,y) in phi^r(s). The
finite Laurent transfer recurrence is rational. A common nonnegative
per-depth shift of x,y makes all matrix exponents nonnegative. Solving
(I-zT)Q=1 over the rational function field, reducing to F2 and cancelling gcds
gives unit-denominator rational coefficient series. The existing exact
Cartier construction supplies finite machines for all Q_s.

For an occurrence path e_1...e_r, let V_(d-1) be the sum of earlier occurrence
edge offsets, and let e_d choose child j_d from state s_d. The parity of reads
BEFORE this leaf at its own position W is exactly

    C = XOR_(d=1..r) XOR_(i<j_d)
        Q_(child(s_d,i))(r-d, W-V_(d-1)-offset(s_d,i)).

This partitions the earlier leaves into ordered sibling blocks. For each
fixed connector edge in one flat scheme, each Q argument is affine in the
scheme exponents. For one edge in repetition q of its cycle, the argument is
affine in exponents and q, guarded by 0<=q<n_i.

The existing carry construction compiles each affine Q evaluation. A
finite-field subset/vector construction projects q by XOR, with the explicit
q<n_i guard. All q fit the visible bound's padded input length and have exactly
one representation there, so projection counts integers rather than infinitely
many zero-padded encodings. Ordinary Boolean XOR combines the finite terms.
This produces the exact automatic C(n) for EVERY instance of EVERY scheme.

## 3. Compile all black AND all white requirements

At a selected read, required initial color is its final turn bit XOR C(n).
For each scheme, conjoin its affine position equations W(n)=(x,y), then
existentially project its exponent variables. Union separately over schemes
to obtain automatic spatial relations

    Black = cells where SOME actual read requires initial black,
    White = cells where SOME actual read requires initial white.

No canonical tuple selection is needed. Because all actual walks, not just
one representative per cell, are covered, these are COMPLETE requirements.

If Black intersects White, no initial coloring can realize the family.
Otherwise the coloring Black, white everywhere else, realizes every word:
induction through any finite word makes its actual read color equal its
prescribed turn. The typing checks already give the exact heading and motion.

Thus finite-seed realization is equivalent to both

    Black intersects White is empty, and Black is finite.

Finiteness is decided exactly by the automatic first-order bound sentence.
On a positive instance, extract a witnessed bound and enumerate precisely its
finite Black set. This is the unique minimal realizing seed. The extracted
bound is an output, not a search cutoff; the algorithm never guesses a mass.
No separate IJ frame validator or supplied parity template is needed.

## Executed implementation and current controls

`flat_forced_seed.py` integrates the literal typing checks, SCC flatness check,
exact schemes, image-derived rational parity, Cartier machines, affine carry
pullbacks, bounded F2 projection, both complete spatial requirements, conflict
and finiteness decisions, and finite-seed extraction.

The initial complete controls in `controls.json` accept identity R with empty
seed and identity L with exactly the origin black. A genuinely rooted flat R5
controller is rejected at the origin. The independently established oblique
and axial hairpins have infinite Black requirements and also conflicting
same-board requirements across depths. These observations do NOT exclude a
wrapper that changes the block's entry board with depth. Existing canonical-
prefix fuel inequalities remain the relevant wrapper condition.

`extended_controls.py` adds two-state recursive SCCs, nested quadratic axial
and oblique recursions, and a cubic mixed hierarchy. It checks EVERY finite
root occurrence walk through depth6 is covered exactly once, and compares
compiled preceding parity against the literal complete refined word at every
sampled scheme tuple. These controls test implementation mechanics; the
all-depth conclusion rests on the finite automata/scheme construction, not on
a depth extrapolation.

No accepted growing ant model, finite universal compiler, finite-seed
undecidability reduction, or global highway theorem has resulted. The broader
JE/JF arbitrary finite-power theorem remains analytic without a completely
integrated general occurrence-cover/selector compiler. This is a complete
executed solver only for its stated flat additive-I input class.
