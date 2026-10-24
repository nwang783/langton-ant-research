# Reconstruction of the missing canonical one-bit certificate

Date: 21 October 2026.

## Scope and provenance

Hao Ke's public source note states a uniform one-bit recovery theorem along a
specific complete standard highway. The public core README says that the
separate draft's original 739-record artifact is not in that release. This
continuation reconstructs a sufficient certificate from the literal dynamics,
using the published source family and published phase thresholds. It is a new
reconstruction of that evidence, not a claim to have recovered the exact lost
file and not a new general highway theorem.

Source inspected at commit:
`22e0c9edcc566a4c2f7a9bf92f5cd05c19199617`.

https://github.com/kehao95/langtons-ant-core/blob/22e0c9edcc566a4c2f7a9bf92f5cd05c19199617/highway_stability/proof/canonical-highway-one-bit-stability.md

## Complete input family

Use the thirteen-cell set P, the twelve-cell deposit D, the 104-letter word W,
and drift d=(2,-2) defined literally in `ant_exact.py`. The initial pose is
(0,0),S. After n standard periods, recentering by -n*d gives the full black set

    C_n=P disjoint_union union_(k=1..n)(D-k*d).

At phase r, execute exactly the first r letters of W, then toggle the current
cell. Both additions and removals of black cells are covered. Every older
black cell stays in the state; the checker does not discard the old wake.

The phase thresholds N_r are the 104 integers in the published source and in
`restore_one_bit_certificate.py`. They satisfy max N_r=25 and
sum_r(N_r+1)=739. We verify every pair (n,r) with 0<=n<=N_r, including all 104
boundary bases n=N_r. Equality of the checked index set is enforced.

## Why 739 finite leaves cover every age

For n>N_r the normalized source differs from the base source only on

    E subset A_(N_r)=union_(k>N_r)(D-k*d).

A first-difference coupling gives the required quantifier bridge. If the base
trajectory never reads this exclusion set, the two fields give the same color
at every actual read. Both flip the same cell, so their difference stays E.
Induction proves equal read and pose traces forever.

For each of the 104 bases, the checker verifies that every finite recovery read
and every entire future phase ray misses A_(N_r). A finite read gives a single
integer collinearity test against each point of D. Two nonparallel rays give
one determinant solution, checked for integrality and nonnegative parameters.
Parallel rays give an integer interval test. Thus the guard covers every tail
cell and every future epoch, not a finite sampling of either.

It also checks the nine actual inverse reads of the perturbed state against
A_(N_r). This ensures that the intrinsic ten-turn event count has the same
history for all greater ages. The unperturbed inverse history is not substituted.

## A finite test for an infinite supplied word

Fix a proposed period w of length P, with initial pose (p,h), returning to the
same heading and having nonzero drift d. Let q_i be its phase-i read position.
At epoch k>=0 the proposed read is q_i+k*d. A phase j in a previous epoch l
writes this same cell exactly when

    q_j-q_i=(k-l)*d.

Put a=k-l. The write precedes the current read exactly when a>0, or a=0 and
j<i. It exists from epoch k=a onward. Therefore its contribution is a parity
step function 1_(k>=a). Each black cell in the complete initial field can meet
a fixed phase ray at only one integer epoch and contributes one isolated hit.

The prescribed read bit is thus

    1_B(q_i+k*d) XOR parity{valid a : 0<=a<=k}.

Check k=0, all valid overlap thresholds a, all initial black hit epochs, and
one epoch after every initial hit. Between those finitely many points the bit
is constant. Beyond the final point it is constant forever. If every required
bit agrees with w_i, induction on literal updates proves w repeated forever.

The input field must be the COMPLETE field. An omitted remote black cell can
become a late ray hit and invalidate the certificate. Controls reject a wrong
current bit, an altered word, and a blocker placed 10^30 periods ahead. A
remote cell outside every future ray is correctly accepted as inert.

## Reconstruction results

| Quantity | Reconstructed certificate |
| --- | ---: |
| Finite cases | 739 |
| Infinite age guard bases | 104 |
| Literal recovery updates | 6,177,080 |
| Exact future parity breakpoints | 128,303 |
| Largest certified post-impact recovery time | 64,584 |
| Largest pre-recovery read radius | 76 |
| Largest intrinsic future forbidden-ten-window count | 33,586 |

The old draft reported 6,221,280 recovery updates and radius 78. Our stopping
rule chooses an earlier valid inspection boundary in 425 cases, each earlier
by 104 updates; this explains the difference of 44,200 updates. We do not claim
the two record files are identical. Both are sufficient bounds for the same
restricted theorem. These are certified boundaries, not necessarily first
entrance times or optimal radii.

A separate endpoint check confirms that final recovery head positions also lie
within the reported radius. The longest case is n=22,r=51. The largest defect
count is attained at n=7,r=72. The nine final turns match the outgoing cyclic
history because the selected final 104-turn block is the same phase word that
is then certified for the future; no untested seam remains.

## Independent audits

1. `verify_one_bit_independent.cpp` rebuilds every source by literal unperturbed
   time 104n+r, then recenters it. This differs from the Python construction by
   the affine field formula. It replays 6,177,080 recovery updates, reconstructs
   the inverse history, and checks all 739 records and all 104 age guards.
   Its infinite-tail proof uses a conservative finite interaction bound. It
   checks 7,190,456 further updates through that bound; after the bound all
   original field hits have ended and all phase overlap contributions have
   stabilized. It therefore proves the remaining infinite interval.
2. `factor_language/audit_parent_one_bit.py` uses vector rotations and an
   independent ordered translation-class criterion. It checks the entire
   required initial black set on every phase-ray class and every actual
   black-cell intersection. It matches all recorded complete-field hashes.
   It checks 16,258 translation classes and 12,010 required black entries.

These are independent implementations of the finite mathematics. They are
not a formal proof-assistant verification or external mathematical review.

## Arbitrary perturbation positions

At an arbitrary time of the unperturbed canonical trajectory, toggle any cell
q. Before its first future unperturbed read, coupling makes the trajectories
identical. If there is no such read, the entire future remains unchanged.
Otherwise the impact state is exactly a current-cell perturbation of a later
canonical phase, so the certificate above applies.

For a remote perturbation, only the first nine intrinsic ten-windows can have
noncanonical inverse-history boundary effects before impact. The safe total
bound is therefore 33,595 events, as in the source theorem. The current-cell
maximum 33,586 is not silently applied to arbitrary negative-time histories.

## Why this does not iterate to solve the full problem

After recovery, the COMPLETE state may include a scar from the disturbance.
Its future can be standard while that complete state is outside the canonical
family C_n. A second disturbance can turn the ant toward the scar. The theorem
supplies neither closure under such later disturbances nor a proof that every
finite seed reaches one of these inputs. Those are separate missing arguments.

## Reproduction

From the parent directory:

    python3 restore_one_bit_certificate.py
    g++ -O3 -std=c++17 verify_one_bit_independent.cpp -o /tmp/ant_one_bit_verify
    /tmp/ant_one_bit_verify one_bit_records.tsv
    python3 factor_language/audit_parent_one_bit.py

The JSON contains every leaf. The TSV is a compact independently parsed copy
used by C++; the code and final manifest make the inputs auditable. No original
739-record file was represented as found or retrieved.
