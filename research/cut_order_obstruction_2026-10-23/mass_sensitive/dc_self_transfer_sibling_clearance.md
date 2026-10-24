# Exact sibling retirement required by a DC-to-DC transfer

23 October 2026. Finite geometric necessary conditions for actual recurrent-eight
packet factors. This retains simultaneous complete-context and core requirements;
it is not an age/speed-only relaxation. No row below is asserted feasible,
and no finite-tail or capture conclusion is inferred.

## 1. Identities and trust boundary

Use the signed ordered RESIDUAL identity ledger in
../../core_periodicity_new/chronology_dcuv/ordered_residual_identity.md.
At each packet boundary remove all input identities I, then install fresh
output identities O, including any same-cell input/output recycling.
These are not the physical cursor-token identities of audit LE. A residual
input can be absorbed into the next five-cell core before a literal L read;
its retirement need not erase the black cell. Later replacement identities
and still-black core cells are retained, not forbidden by this note.

Normalize a source DC to head(0,0),N. Its sole input is(0,1), its output
identities are

    A=(2,0), B=(2,3), C=(3,1), D=(3,2),

and its entry core is

    K={(-1,-1),(-1,0),(0,-1),(0,0),(1,0)}.

The complete RAW+M11 context's first-read requirements and complete finite
read set F are taken literally from the signed geometry. There are no
unobserved cells inside F. The target DC has one residual input only.

## 2. A general simultaneous-clearance lemma

Suppose an output identity q of a producer survives as that identity until
it is an input of a later target packet. Place the target so q matches the
specified target input. Partition every OTHER source output identity by
its cell at the target:

- Co-input: in the target residual input set I_t. It may be retired by that
  very target alongside q.
- Core: in the target entry core K_t. It MUST already have been retired as
  a source residual identity before target entry.
- White: in F_t but outside the forced entry-black set K_t union I_t. It
  MUST already have been retired before target entry, since a still-live
  source identity would leave that cell black.
- Outside: outside F_t. This local lemma places no retirement requirement.

For a core cell, the conclusion follows from the exact residual/core
partition at every packet boundary: an identity that still survives in the
residual ledger cannot simultaneously occupy the core. For a white cell,
it follows from its required entry color. In either case some strict
intermediate packet's ordered input removal must retire that old identity.
This may be followed by arbitrary replacement writes or core absorption;
only the old source identity's continued survival is excluded.

This does not merely demand a net color change. Nor does one retirement
satisfy requirements for two distinct source identities. Counts must use
the UNION of required identity IDs, not add repeated references to the
same sibling from several target edges.

## 3. Complete sector-compatible DC self-transfer table

Write target headings N,E,S,W=0,1,2,3 and let R_h be clockwise rotation.
If q is the consumed source output, the target head is uniquely

    p=q-R_h(0,1).

Source sector is1. Testing(-1)^(p_x+p_y)*(+1 for vertical h, -1 for
horizontal h)=1 leaves EXACTLY the following eight placements.
Letters in the core/white columns identify source siblings requiring
PRE-TARGET retirement. All omitted siblings lie outside the target context.
There are no co-input siblings because DC is unary.

    consumed q   target h   target p   core retire   white retire
    A            E          (1,0)      none          none
    A            W          (3,0)      C             B,D
    B            N          (2,2)      D             none
    B            S          (2,4)      none          A
    C            E          (2,1)      A             none
    C            W          (4,1)      none          B,D
    D            N          (3,1)      A,C           none
    D            S          (3,3)      B             A

The full record, including untouched siblings and exact source-coordinate
cells, is dc_sibling_clearance.json. It is regenerated directly from literal
requirements by check_dc_sibling_clearance.py, not by assuming a permitted
parent role or a feasible transition.

Thus SAME-HEADING continuation from one DC output requires retirement of
at least one sibling before the child: B requires D; D requires A and C.
A clean same-heading comb that keeps all three spare outputs dormant is
impossible, even if its numerical ages and root boxes are consistent.
The four-output-relative-input shift(3,0), sometimes tempting for an eastward
comb, is NOT in the table because it violates the physical sector.

## 4. A finite coupled-support consequence

Consider a selected DC ancestry CHAIN: every child DC's sole input is a
fresh output identity of the preceding chain producer. If N-1 of its links
are same-heading, at least N-1 DISTINCT off-chain source sibling identities
must retire before their respective children; using D continuation instead
of B adds one further required identity on that link. These are different
identities even when cells are later recycled.

No chain DC can retire one of these sibling identities: its only input is
its selected parent identity, not a spare sibling of another producer.
Consequently all required retirements occur in SUPPORT packets outside
the chain. A recurrent-eight packet has at most five residual inputs, so
at least ceil((N-1)/5) support packets are needed in the minimal same-heading
case. This is a side-clearance rate, not finite initial fuel: support
packets may themselves consume produced identities and create new branches.

The sole zero-local-clearance transfer A,E has source-normalized target
pose(1,0,E). Its generic age-three possibility is already excluded by the
signed counted relation; heading congruence then makes its actual age at
least seven. No all-age exclusion is asserted. The repeated-gate historical
clearance analysis is owned separately by the chronology investigation;
this note does not infer feasibility merely because its local clearance
column is empty.

## 5. Why this is stronger than an initial-root packing test

The five-root FIFO packing model and sector-compatible abstract output
combs can satisfy finite roots, mass growth, ages and spatial boxes while
silently retaining buds that fall into a future core or forced-white cell.
The table detects exactly those missed simultaneous obligations. Conversely
retiring a sibling does not force an infinite second lineage or a new
initial-root pair: that further implication is unproved and must not be
assumed. The repeated-root-pair counterexample also prevents replacing
these identity-sensitive obligations by a generic unused-root-name charge.

Independent analytic/literal review requested. The theorem is a necessary
retirement condition on an assumed actual packet history; it does not
construct that history or close the remaining DCUV cases.
