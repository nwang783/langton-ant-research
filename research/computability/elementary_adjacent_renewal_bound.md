# A linear physical-time bound for the next adjacent-defect renewal

22 October 2026. Status: analytic derivation independently audited. The linear H replacement
was independently audited on22 October2026 at20:43 UTC; the closed-form
iteration consequence in Section6 passed independent analytic review at21:03 UTC.
The executable controls below are finite implementation checks, not a formal
verification of every line of the implementation.
This bounds one exact renewal, not the number of renewals or capture time.
It uses the audited no-K graph and H/T24 bounds, without relying on the
recovered source's separate polynomial future-J theorem.

## 1. A failed standard-tail test has an early exact mismatch

Let X have finite black field B and head position p. Set

    R=max({||b-p||_infinity:b in B} union {0}).

For ANY cyclic standard104 phase w, the exact ray verifier either proves w
forever or supplies its first literal mismatch. If it fails, that mismatch
has index at most104R+21943.

Proof: the104 read offsets q_i-p each have infinity norm at most104. The
period drift d has coordinate magnitudes2. The verifier changes its parity
formula only at the following nonnegative integer epochs k:

- pairwise phase-collision thresholds q_j-q_i=k*d, bounded by104 (using the
  deliberately loose bound ||q_j-q_i||_infinity<=208);
- epochs with a black seed b=q_i+k*d, and the immediately following epoch.
  These satisfy k+1<=(R+104)/2+1;
- the initial epoch0.

Between consecutive thresholds the predicted read bit is constant. Therefore
if a mismatch exists, its epoch is at most R+210. Its read index is at most
104(R+210)+103=104R+21943. This argument uses exact finite support, not a
finite-repeat heuristic.

Independent audit also gives the smaller bound104(R+105)+103: after epoch104
all possible earlier-phase writes are active, and at every epoch k>=R+105
all phase reads lie outside the radius-R initial field. Each phase then has
a stationary predicted bit forever. We retain the larger bound above to
avoid changing the subsequent generous constants.

Consequently, in a no-K history-graph path, its W104 component visit either
has an exact permanent-tail certificate or lasts at most

    W(R)=104R+22000

read transitions. The extra57 steps safely cover the endpoint conventions.
Once a W vertex is reached, its149-letter past is already standard, so a
successful exact tail cannot hide a boundary-straddling K event.

## 2. A joint mass/radius budget

Translate the initial head to the origin and let m be initial black mass and
R0 its initial relative support radius. After t ordinary ant moves,

    current mass <= m+t,
    current relative support radius <= R0+t.

The second inequality follows because each old seed cell is at most R0+t
from the current head. A newly black cell was read at some earlier time s,
and the path from that read to the current head has length t-s<=t, so its
current distance is at most t. Thus

    z=m+R0+2t+1

bounds their SUM plus one, and hence both quantities separately. Any interval
of L moves raises the corresponding mass-plus-radius-plus-one by at
most2L. Normalizing the initial heading by quarter rotation changes neither
mass nor infinity radius.

## 3. At most three exceptional component visits

Import the independently audited functions

    H(x)=300+89(x+100)+15=89x+9215,
    T24(x)=12x+400.

The new linear H bound comes from the independently checked seven-word
actual-history kernel, including its full successor and marker context.
Sources: word_stabilization/monochromatic_seven_word_fuel.md and
linear_isolated_defect_response_bound.md. Independent certificates are
check_seven_monochromatic_context_independent.py/json and
check_seven_monochromatic_graph_independent.py/json in audits/. The latter
explicitly embeds the old H component in the new kernel. The300 total trim
allowance is essential; the old100 trailing allowance alone is insufficient.
This replaces the older exponential H bound without changing the argument.

The no-K graph has N=270902 vertices and only H,T24,W104 as cyclic SCCs.
A finite path can visit each of these SCCs at most once. All other vertices
are transient; the initial149 reads and connecting edges are covered by

    O=N+1000.

This allowance also covers the initial ten true inverse-history reads and
the one-sided history boundary. The supplied implementation reconstructs
104 past reads instead; that larger fixed overhead is still covered.

Pre-budget all these ordinary steps and define

    z0=m+R0+2O+1,
    G(z)=z+2(H(z)+T24(z)+W(z))=411z+63230,
    Z=G(G(G(z0))).

During each exceptional visit the current mass and relative radius are at
most the current numerical budget z. If no permanent-tail certificate has
been obtained, that visit costs at most one of H(z),T24(z),W(z), and hence
raises the budget to at most G(z). Three iterations cover all possible
orders, including missing components and partial visits.

Therefore every K-free prefix containing no certifiable permanent tail has
length strictly less than Z. More precisely its length is at most
(Z-(m+R0+1))/2, but the weaker Z bound is simpler and sufficient.

## 4. Total next-K computation is elementary

At the input state reconstruct the true preceding ten turns. Simulate the
ant and detect K after every read, preserving overlapping windows. At every
checkpoint run all104 exact standard-tail phase tests. If a test succeeds,
inspect the next ten reads to account for the possible initial-cut boundary;
return a K if one occurs, otherwise return the terminal symbol.

By Section3 this process finishes within Z+10 further ordinary reads. This
is a physical-read bound, not a count of implementation bit operations. If a
K is found, returning its full after-step finite state implements the exact
renewal map R_K. Otherwise it correctly returns bottom.

All displayed functions are now affine, and only three G compositions occur.
In particular, Z+10 is LINEAR in m+R0, with a large absolute constant. The exact ray tests
and literal field updates have polynomial cost in the current explicit
field size and coordinate bit length, per checkpoint (the period104 is
fixed). The field has at most m+Z+10 cells and the coordinates have size
bounded by the input coordinates plus Z+10. Thus the entire algorithm has
polynomial bit cost in the numerical mass/radius budget and coordinate bit
length, without asserting that its bit cost is Z+10. Binary coordinate
encoding makes this an at-most-single-exponential algorithm in the standard
explicit encoding length.
Thus R_K is an unconditional elementary total function, not merely a total
function justified by an unbounded search. Its ITERATION may still run forever.
The highway conjecture remains exactly universal termination of this specific
explicitly bounded-step renewal system.

No mass-only bound is asserted: R0 is essential, since a single very distant
black cell can defer an interaction for arbitrarily long physical time.

## 5. Executable finite controls

`adjacent_renewal.py` reconstructs the unique true preceding104 turns,
checks every adjacent-defect event literally, and accepts a terminal tail
only through `periodic_tail_checker.first_mismatch`. It uses the recent
104 letters to select a candidate tail phase, rather than testing all
phases at every step. At every W-component vertex that phase is present,
so the proof above applies unchanged.

`adjacent_renewal_controls.json` records80 literal first-event comparisons,
416 certified terminal phase/rotation cases, and30 successive overlapping
renewals compared with an uninterrupted trajectory. All passed. These
controls do not prove termination; the analytic argument above does.


## 6. A closed exponential bound in the NUMBER of renewals

Set

    A0=411^3=69426531,
    B0=63230(411^2+411+1)=10706925590,
    O=271902,
    C0=2O+ceil((B0+10)/A0)=543959,
    Lambda=1+2A0=138853063.

For a state with mass m and relative radius R, define w=m+R+1+C0.
The bound above says one next-K-or-terminal computation takes at most A0*w
physical reads. After L reads, mass-plus-radius-plus-one increases by at
most2L, so an event successor satisfies

    w_next <= w+2A0*w = Lambda*w.

If a capturing input has exactly r true-history future K events, there are
r event renewals and one terminal renewal. Their combined time is at most

    A0*w * sum_(j=0)^r Lambda^j
      = w*(Lambda^(r+1)-1)/2.

This bounds a genuine exact standard-tail checkpoint, not an observed
repetition. It does NOT bound r or assert that every input captures.

For explicit binary encodings of length<=n, mass is at most n and relative
radius at most2^(n+1). Hence any known bound r<=g(n) gives the uniform
capture-checkpoint bound

    (n+2^(n+1)+1+C0)*Lambda^(g(n)+1).

Consequences for the positive-instance maxima C(n) (K count) and F(n)
(exact checkpoint time), defined in adjacent_renewal_normal_form.md:

- F(n) <= (n+2^(n+1)+1+C0)*Lambda^(C(n)+1).
- C(n) <= F(n)+10 by the true-history boundary allowance.
- C has an elementary majorant iff F has an elementary majorant. The
  earlier primitive-recursive and computable-majorant equivalences remain.
- A polynomial capturing-event-count bound would give a singly exponential
  capture-decision time bound for this explicit encoding. No such global
  polynomial event-count bound is known.

These are conditional bounds over the capturing inputs. Noncapturing inputs
have infinitely many renewals, so a supplied count majorant decides capture
by checking one more event, as in the earlier metatheorem. Universal
termination remains the unresolved conjecture.
