# A critical fixed-mass budget failure exposes a spatial scattering obstruction

23 October 2026. New analytic reduction, submitted for independent review.
This is NOT a defect budget, capture theorem, or finite-seed counterexample.
It explains exactly which spatial phenomena a nonlinear budget must control.
No source document was edited.

## 1. Definitions and retained dependencies

Fix the initial pose. Let K(X) be the number, possibly infinite, of actual
adjacent-bad-ten events in the nonnegative future of finite state X, using
its true inverse history at the initial boundary. Let

    B(m) = sup { K(X) : initial black mass <= m }.

The retained finite-K/capture equivalence applies to FINITE-support states.
The bounded-mass seed space is sequentially compact in pointwise board
convergence. A finite-time physical read trace is locally constant in that
topology. These elementary facts can also be proved directly below.

A standard flight has literal period P=104, full nonzero drift d, finite
read offsets s_0,...,s_(P-1), and heading restored after each period.
All of its cyclic ten-factors are among the pinned standard factors.
Spatial rotation changes neither its turn word nor this membership.

## 2. A critical family has a lower-mass capturing local limit

Suppose m is the LEAST integer with B(m)=infinity. Retained blank capture
gives B(0)<infinity, hence m>=1. Choose finite seeds X_n
of mass <=m and K(X_n)>=n. Counts may be infinite; no existence of a finite-
budget maximum or computable bound is assumed. Pass to a subsequence whose
initial boards converge pointwise to B. This is possible by a diagonal
subsequence over lattice cells. There are at most m black cells in B:
any m+1 fixed black cells would all occur in the approximants eventually.

If |B|=m, all those m cells occur in every sufficiently late approximant,
so the approximants equal B, with no extra cells. If K(B) is infinite this
already supplies a finite-seed noncapture state. Otherwise their counts
could not diverge. Thus either a mass-m noncapture limit is already obtained,
or |B|=j<m. In the latter case B(j)<infinity by minimality, so this limit
state captures the standard highway.

Since B(m-1) is finite, discard terms with n<=B(m-1). Every remaining
approximant then has EXACT mass m. After discarding further finitely many
terms, each approximant is exactly

    B_n = B union E_n,       |E_n|=m-j,

where E_n misses every fixed finite set eventually. There are no deletions:
all finitely many black cells of B are eventually present. Hence these are
remote INITIAL black additions, not arbitrary changes to a later board.

Discard enough initial terms that the true inverse ten-read histories at
time zero also agree with B. Reversibility makes this a finite local
condition, so pointwise initial convergence guarantees it.

The first read of E_n occurs at time a_n tending to infinity. Up to that
read the physical paths and all required history windows agree with B. All extra cells are
still unread, and the COMPLETE boards differ exactly by E_n. Since B
captures, discard another finite prefix so that every a_n is in its actual
standard tail. By choosing a subsequence, a_n has one fixed standard phase
phi, and

    a_n = T + N_n P + phi,       N_n -> infinity,
    q_n = p_T + N_n d + s_phi

is the first read extra-black cell. The number of defects before a_n is
at most B(m-1). Thus an unbounded number of defects remains after a_n.
This conclusion concerns defect COUNT, not flight duration.

## 3. The exact causal standard-front contact limit

Center the entire pre-read state at q_n, without changing its heading.
For each fixed relative cell z, its color in the centered B trajectory
is eventually independent of N_n. To see this, all reads after T are

    p_T + k d + s_i,       k>=0, 0<=i<P,

ordered by kP+i. Relative to q_n, a read at z requires

    z = (k-N_n)d + s_i-s_phi.

For fixed i and z there is at most one integer k-N_n satisfying this
vector equation. Its read occurs before phase phi precisely when
(k-N_n)P+i<phi. For large N_n the condition k>=0 no longer removes any
such finite candidate. Initial B_T cells translate by -N_n d and disappear
from every fixed finite region. Parity of this finite list of prior reads
therefore stabilizes, proving the claim.

Call the limiting board C_phi. It is a single exact CAUSAL standard front:
its finite-width settled wake extends backwards, its leading field is white,
and the head is at the indicated phase. It is generally infinite support.
It must not be replaced by the settled BILATERAL wake or by a freely chosen
front coloring.

Let F_n=E_n-q_n. Again pass to a subsequence with pointwise limit F. Then

    0 in F,       1<=|F|<=m-j,
    C_phi intersection F = empty.

In fact F misses the ENTIRE strict-past standard READ set

    P^-_phi = {a d+s_i-s_phi : aP+i<phi}.             (0)

Every fixed cell in (0) is read before contact in every sufficiently deep
base flight. If it belonged to F, it would belong to E_n-q_n eventually,
contradicting the definition of the first extra contact. Thus these are
causally FRESH additions, a strictly stronger restriction than current
whiteness. In particular Y has the genuine all-standard inverse read
history before its contact cut. No arbitrary inverse suffix is selected.

The last assertion is important: every E_n cell is unread before the first
extra contact, so its base-trajectory color there is white. Thus the limiting
contact perturbation is ADDITIONS-ONLY on initially white contact cells,
not an arbitrary XOR cap. Its heading remains the actual incoming phase.
The actual complete contact states converge locally to

    Y = (C_phi union F, 0, h_phi).

Every fixed finite future physical history of Y is therefore reproduced
exactly by all sufficiently late centered actual states. No head teleport,
independent reinitialization, or omission of a nearby old token is involved.

## 4. Where the finite base and its causal front can differ

There are finite sets A,S and an integer c, depending only on the fixed base
B and chosen phase, such that the centered base board at contact differs
from C_phi only inside

    (-N_n d + A) union
    union_{k>=N_n-c} (S-k d).                         (1)

Proof: the first part includes the finite complete state at T, translated
into the contact frame, and finitely many boundary phases. The second part
includes precisely the missing negative-time standard copies: C_phi allows
all k-N_n below the current phase, whereas the actual history starts at
k=0. Each missing read lies in one of finitely many phase-offset classes.
XOR cancellation may REMOVE points from (1), which only strengthens the
containment. All old finite initial data, prelude debris, and missing wake
are retained by this containment.

The actual contact state and Y can additionally differ at members of
F_n symmetric_difference F. Any such differences escape every fixed finite
region. If |F|=m-j, there are NO such differences eventually: the full mass
allowance is exhausted by the finitely many retained F cells, so F_n=F.

## 5. Exact archive-return alternative

Suppose the limiting contact state Y actually has a standard tail, with
outgoing full drift e. Its complete future read set is contained in

    A' union union_{l>=0} (S' + l e),                 (2)

for fixed finite A',S'. If e is NOT a negative multiple of d, the set (2)
is disjoint from (1) for every sufficiently large N_n.

Here is the elementary cone argument. An unbounded intersection would give

    l_n e + k_n d = bounded,
    k_n >= N_n-c -> infinity,       l_n>=0.

If d and e are independent, applying the two inverse coordinate functionals
forces both coefficients bounded, a contradiction. If e is a positive
multiple of d, both coefficients have the same sign and cannot cancel.
Only a negative multiple permits cancellation. The translated finite set
-N_n d+A is covered by the same argument. Finite transient points A'
miss (1) for large N_n automatically.

For the four actual standard104 directions, the sole exceptional case is
therefore e=-d. This is spatially opposite STANDARD motion, not the inverse
104 turn word.

Consequently, if ALL remaining initial additions belong to the finite contact
cluster (|F|=m-j), and Y captures with e!=-d, then all sufficiently late actual
contact states follow exactly Y FOREVER. First-difference induction applies
because every complete board discrepancy misses its complete future read set.
Their post-contact K counts are then bounded by K(Y)+10. The +10 permits all
true-history windows crossing the contact cut; after ten reads, the words
are identical. Their earlier counts are <=B(m-1), contradicting divergence.

Thus a critical family, unless it already yields finite-seed noncapture,
must expose at least one of:

1. a causal-standard-front plus finite ADDITIONS-ONLY cap whose actual future
   is not standard;
2. a standard scattering response directed exactly back toward the receding
   incoming archive;
3. another ORIGINAL black-cell cluster escaping relative to the first contact.

If m-j=1, alternative 3 is impossible. No claim is made that alternative 1
has infinitely many K: the finite-K/capture equivalence was not imported to
an infinite-support prepared front. Alternative 2 is necessary in that branch,
not sufficient for unbounded defects. A reverse flight can still be clean
standard, and its later archival collision can have bounded response.

## 6. What this adds, and what is missing

This is a spatially explicit necessary shape of a minimal mass-only budget
failure, rather than another finite local graph criterion. Non-opposite
standard scattering of one bounded contact cluster is automatically safe
against an arbitrarily old incoming archive. Any successful nonlinear proof
must control reverse-archive returns and/or successive separated initial
clusters, or prove the relevant causal-front scattering statements.

It supplies no bound on the number of reverse returns, no classification of
all finite caps on a causal standard front, and no global B(m). The retained
one-black exceptional channel already shows why the reverse branch cannot
be discarded. Root count, elapsed time, local histograms, and a finite suffix
alone do not settle these alternatives.
