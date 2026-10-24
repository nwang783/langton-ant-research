# Exact inverse certificates for permutation-coupled expanding paths

22 October2026. Status: analytic extension independently audited;
finite implementation controls pass, but the full implementation is not independently certified. No finite-support ant model is supplied.
This is broader than a pure inflation of one path, and does not infer that
arbitrary integrated automatic turn words have automatic positions.

## 1. The candidate class

Fix radix k>=2, a Gaussian integer a with |a|>1, a finite state set S with

    S(kn+j)=delta(S(n),j),  S(0)=s0, delta(s0,0)=s0,

and finitely many phase curves P_c:N->Z[i], c in C. For each control state s
and digit j, specify a PERMUTATION pi_(s,j) of C and offsets b_c(s,j), requiring
b_c(s0,0)=0 for every c. Define P_c(0)=0 and, for n or j nonzero,

    P_c(kn+j)=a P_(pi_(S(n),j)(c))(n)+b_c(S(n),j).

The phase being expanded can change at each digit and can depend on the finite
control. A chosen phase c* is the proposed physical ant position path.
Every position is effectively determined by well-founded digit recursion.
The zero-offset condition makes arbitrary leading-zero padding harmless.

For example, a first-letter two-cycle may have

    P_R(kn)=a P_L(n),  P_L(kn)=a P_R(n),

rather than either individual path satisfying pure inflation. This avoids
replacing k by k squared merely to fix the root phase.

## 2. A finite equality automaton

For an MSB-first numeral, guess its initial selected phase. When a digit j
is appended at control state s, replace the old selected phase c by the UNIQUE
new phase c' satisfying pi_(s,j)(c')=c. Update the selected coordinate by

    z' = a z + b_(c')(s,j).

At the end require the selected phase to be c*. For any digit string and
final phase there is exactly one consistent initial phase, since each pi is
a permutation. Induction on prefix length proves the resulting z is exactly
P_(c*)(n). This is a finite-phase selection mechanism, not an approximation.

For two synchronized numeral tracks, allow all pairs of initial phases and
track both finite controls, both selected phases, and the difference D. Its
update is

    D' = a D + b_(c')(s,j)-b_(d')(t,l).

Let M bound the norm of every offset difference. Choose an integer R at least
the norm of the desired displacement target, with (|a|-1)R>=M. If |D|>R,
then |D'|>|D|; such a difference can never return to a target inside the disk.
Collapse all outside differences to one rejecting sink. The remaining states
are finite: two controls, two phases, and Gaussian D in the radius-R disk.
Accept exactly the prescribed final phases and desired difference.

Thus P_c(n)-P_d(m)=v is an effectively regular synchronized relation for any
fixed phases and any fixed integer displacement v. Reverse the MSB automaton
and determinize to obtain the ordinary LSB-first automatic relation used by
our arithmetic verifier. In reversal, acceptance must intersect the SET of
original start states; choosing one arbitrary initial phase would be wrong.

No positional numeral system for Gaussian grid points is required, and no
bound is imposed on the time indices being compared.

## 3. Exact ant validation and finite support

Use the displacement relations for0 and the four unit vectors, together with
ordinary arithmetic on n, to check all unit moves and quarter-turn geometry.
For a geometrically valid selected path, derive its automatic R/L predicate
from consecutive movement directions and the supplied initial heading.

The previously audited inverse theorem now applies unchanged:

- consecutive reads of every physical cell must alternate R,L;
- the set of first-L times must be finite.

These are decidable first-order/regular-language tests using the exact
same-cell relation. When both pass, the minimal initial black set consists
exactly of the cells at those finitely many first-L times, and literal induction
proves the whole infinite proposed path. A given finite seed can instead be
checked by binding each visited cell's first-read bit to that seed; unvisited
extra black cells are harmless.

If |a|<k, every phase satisfies |P_c(n)|=O(n^(log_k|a|)), by the elementary
maximum-offset recurrence. Therefore any validated finite-seed ant in this
subcritical class would have no translating periodic tail: its displacement
is globally sublinear, while zero-drift periodicity confines it to finitely
many cells. This would be an actual counterexample, not just a failed104 test.

Caution: the earlier UNIFORM ALL-WINDOW Holder bound for a single common-scale
recurrence is not claimed here. Within a digit block, different descendants
may select different coarse phases. The global-from-origin growth estimate
suffices for the stated nonperiodicity conclusion.

## 4. Rotation/reflection-controlled recurrences are included

Let a>1 be a real integer, and let G be a finite group of lattice isometries
fixing the origin, for example the eight rotations/reflections of the square.
A recurrence

    P(kn+j)=a g_(S(n),j) P(n)+b(S(n),j)

can be put in the preceding form by taking phase curves P_h=h P for h in G.
The phase permutation is right multiplication h -> h*g_(s,j), and the phase
h offset is h*b(s,j). Real scaling commutes with every h. Consequently the
inverse certificate framework includes these controlled orientation changes.
For non-real Gaussian a, reflection does not in general commute with scaling;
this corollary must not be applied without checking that algebra separately.

## 5. Implementation controls

`phase_permuted_recurrence.py` implements the finite carry and multi-start
reversal directly. Two independent recursive-coordinate controls use phase
swapping and digit-dependent phase selection. Each checks58,800 displacement
comparisons, including cross-phase equality and neighboring-cell differences.
The saved `phase_permuted_recurrence_controls.json` reports all passes.
These controls test implementation conventions; the general proof is above.
The full first-order automata library is not independently formally verified.
