# Exact finite-support certification for expansive integer-matrix paths

2026-10-22 23:54 UTC. Status: Sections 1–7 independently analytically audited on 2026-10-22 at 23:58 UTC.
This is a finite-support candidate-validation bridge, not a found counterexample,
not an undecidability theorem, and not a further infinite-background reduction.
It extends the independently audited scalar framework in
`selfsimilar_visit_certificates.md` to genuinely anisotropic integer matrices.

## 1. Candidate and exact computational question

Fix a radix k>=2, a finite state set S, a state transition delta:S x {0,...,k-1}->S,
an initial state s0 with delta(s0,0)=s0, a 2x2 integer matrix A, and integer offsets
b(s,j). Require b(s0,0)=0. Suppose every complex eigenvalue of A has modulus>1.
Define, with p(0)=0 and S(0)=s0,

    S(kn+j)=delta(S(n),j),
    p(kn+j)=A p(n)+b(S(n),j).

The leading-zero conditions make these recurrences well-defined at zero and
allow padded digit strings. No claim is made that an arbitrary automatic turn
word has a recurrence of this form. Conversely the supplied recurrence need not
already describe a geometric walk; unit moves and quarter turns are tested.

For EACH supplied candidate, the following are decidable exactly:

1. Whether p is a unit quarter-turn walk from a specified initial heading.
2. Whether all consecutive reads at the same cell have opposite R/L turns.
3. Whether only finitely many cells are first read L.
4. If all tests pass, the unique minimal finite black seed realizing the path.
5. Compatibility with any supplied finite seed, allowing unread extra blacks.
6. Eventual standard104 capture or eventual turn periodicity.

Items 1--5 supply the actual finite-support bridge missing from merely long
finite prefixes. This does NOT say any candidate passes them.

## 2. An exact rational expanding norm

Direct Euclidean expansion is too restrictive. For example
A=((2,3),(0,2)) has both eigenvalues2 but contracts some Euclidean vectors.
Let B=A^(-1). Solve the rational linear equation

    P - B^T P B = I

for a symmetric 2x2 matrix P. Since rho(B)<1, the solution exists uniquely and is

    P=sum_(i>=0) (B^i)^T B^i.

Thus P is positive definite and P>=I. Conversely a positive definite solution
to the displayed equation forces every eigenvalue of B to have modulus<1:
apply the equation to a complex eigenvector. Hence solving its three rational
linear equations and checking P11>0 and det(P)>0 is also an exact test of the
expansiveness hypothesis, after checking det(A)!=0.

Write ||v||_P=sqrt(v^T P v), T=trace(P), and

    q=1-1/(2T),                 0<q<1.

Because v^T P v<=T||v||_2^2,

    ||Bv||_P^2=||v||_P^2-||v||_2^2
               <=(1-1/T)||v||_P^2 <= q^2 ||v||_P^2.

Every constant here is rational and every norm comparison can be made by
squaring; no numerical eigenvalue tolerance enters the certificate.

An alternative is to group r digits until ||A^(-r)||_infinity<1. The Lyapunov
version avoids increasing the radix and its transition alphabet.

## 3. Finite carry automaton for every fixed displacement

Read padded base-k numerals s,t from most significant to least significant.
Track their two finite states and D=p(s_prefix)-p(t_prefix). A digit pair j,l
updates

    D'=A D + b(S(s_prefix),j)-b(S(t_prefix),l).

Let M be an integer upper bound on the P-norm of every offset difference.
For any finite desired set of target displacements, choose an integer R with

    R >= maximum target P-norm,
    R >= q M/(1-q).

From D=B(D'-difference) one has

    ||D'||_P >= ||D||_P/q-M.

Therefore if ||D||_P>R, all subsequent differences have strictly increasing
P-norm and can never reach a target. Replace all such differences by a single
rejecting sink. The remaining integer differences are finite because P is
positive definite (in fact P>=I). The resulting finite automaton accepts exactly

    p(s)-p(t)=v

by testing its final carry against v. Leading-zero stability is exact. Reversing
and determinizing gives the usual least-significant-digit synchronized relation.
This proof handles unequal eigenvalues, nondiagonalizable shears, and nonscalar
complex-eigenvalue matrices, not only Gaussian similarities.

## 4. Geometry, chronology, and finite support

The four unit-displacement relations and t=s+1 decide the outgoing direction at
every time and test that it is a unit vector. Relations at neighboring times
test perpendicularity and derive the R/L predicate, after checking the initial
heading. All are first-order operations on automatic relations in radix k.

Using Eq(s,t): p(s)=p(t), define

    First(t): not exists s<t Eq(s,t),
    FirstL(t): First(t) and turn(t)=L,
    Consecutive(s,t): s<t and Eq(s,t)
                      and not exists r (s<r<t and Eq(s,r)).

Test every Consecutive pair for opposite turns and test FirstL for finiteness.
These are decidable by the ordinary closure and finiteness algorithms for finite
automata. If both pass, enumerate the finite FirstL times and initialize exactly
their p(t) cells black. Induction on chronological reads proves the ENTIRE infinite
path, rather than only a finite approximation. A fixed-seed test instead compares
the initial bit of every first-read cell against its prescribed turn; fixed-cell
membership is automatic by comparison with p(0)=0 and fixed displacement targets.

An automatic turn word's eventual periodicity is first-order expressible using
ordinary time addition: exists a nonzero P and N such that every t>=N has the
same turn at t and t+P. A fixed standard word is still simpler. These tests do not
claim a decision procedure for arbitrary finite ant seeds, only for this supplied
recurrence class.

## 5. A constructive finite-parameter existence decision

For fixed state bound M, radix k, and expansive matrix A, existence of a compatible
finite-seed ant recurrence with at most M accessible states is decidable.

Enumerate all finite state graphs with at most M accessible states and the required
leading-zero loop. Each accessible state has a representative n<k^(M-1), using a
shortest state-reaching digit word. Its offsets are forced by

    b(s,j)=p(kn+j)-A p(n),

so they are completely determined by the finite physical prefix through position
k^M-1. Enumerate the finitely many unit quarter-turn words of that length, discard
finite chronology conflicts, derive all offsets, and reject repeated-state
inconsistencies. Apply the all-time decision above to every survivor.

Thus unbounded integer offsets or remote unread seed cells do not create hidden
infinite parameters at fixed M,k,A. This is usually an enormous finite search,
not a practical universal algorithm or a bound on M for actual ants.

## 6. A successful subcritical model would really refute capture

If rho(A)<k, choose rho(A)<lambda<k. There is a constant C such that
||A^r||<=C lambda^r. Expanding the digit recursion gives |p(n)|=O(n^alpha),
alpha=log_k(lambda)<1. Thus p(n)/n tends to0.

Every eventually periodic turn tail of a valid finite-seed ant has nonzero
translation drift; zero drift would confine its path to finitely many cells.
It therefore has a nonzero asymptotic velocity. Consequently ANY candidate
passing the finite-support tests with rho(A)<k would be genuinely aperiodic,
not merely another highway period. No such candidate is supplied here.

For a single common-A recurrence there is also a uniform all-window bound. The
positions inside each aligned k^r block have diameter O(lambda^r), because their
coarse A^r p(n) term is common and all digit offsets are bounded. An interval of
at most k^r moves intersects at most two adjacent such blocks; their boundary
positions are joined by one unit move. Hence displacement over EVERY length-t
window is O(t^alpha). The constant is independent of the window's start time.
This all-window assertion is not automatically extended to phase-permuted curves.

## 7. Pure same-path matrix parity filter

Suppose, more specifically, that a unit quarter-turn path from the same launch
obeys p(kn)=A p(n) at EVERY n, with no offsets at aligned boundaries. Then

    A mod2 = I                if k=1 mod4,
             ((0,1),(1,0))   if k=3 mod4,
             zero            if k=0 mod4,
             all-ones        if k=2 mod4.

Indeed consecutive physical move axes alternate. If k is odd, the fine k-block
at kn starts with the same move axis as coarse step n. A block starting horizontal
has (k+1)/2 horizontal and (k-1)/2 vertical moves; a vertical block interchanges
them. Signed displacement has those same coordinate parities. Both coarse axes
occur, so this fixes both columns of A modulo2. For even k every block has k/2
moves on each axis, giving the last two cases. This filter is for the pure aligned
identity, not arbitrary state-dependent offset recurrences.

## 8. Implementation and scope

`expanding_matrix_visits.py` implements the exact rational Lyapunov solution,
carry machine, and all-time geometry/inverse interface using the existing
`automatic_radix.py` operations. Controls cover diagonal unequal eigenvalues,
a nonnormal shear whose Euclidean minimum singular value is below1, a nonscalar
complex-eigenvalue matrix, and the established dragon negative control.

Implementation controls do not replace the displayed proof or independent review.
The matrix extension removes an artificial similarity restriction from the exact
finite-support search space. It neither manufactures the infinitely many required
hardware cells nor claims an ant simulates the recurrence's evaluator.

The implementation optionally sharpens q without any floating-point arithmetic.
Gershgorin gives lambda_max(P)<=U=max(P11+|P12|,P22+|P12|). Take a dyadic rational
q>=sqrt(1-1/U), with q<1, and check I-(1-q^2)P is positive semidefinite exactly.
This has the same proof and greatly reduces the carry radius for diagonal A.
The four-direction adapter `direction_substitution(A,images,root='E')` accepts
absolute movement words with net displacement A times their movement letter.
It does not require quarter-rotation covariance. Geometry and chronology remain
separate mandatory tests.

Independent audit: `../audits/check_matrix_bridge_independent.py/json` solves a separate full four-variable Lyapunov system and checks Schur expansiveness for all 2,401 integer matrices with entries -3..3 (1,408 expansive), including rational contraction PSD checks. Separate carry machines match 1,769,472 literal pair/target checks. The theorem is signed; no successful ant model is asserted.
