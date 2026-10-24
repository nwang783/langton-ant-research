# Exact given-seed validation for finite-power morphic ant paths

2026-10-23 03:26 UTC. Analytic decision theorem independently signed as audit IJ.
No successful nontrivial model or practical end-to-end checker is claimed.

## 1. Scope and statement

Supply a finite typed alphabet, nonempty images phi(s), and an integer matrix
A as in unit_inductive_certificates/bridge.md: image incoming/final headings
match the parent, and its net displacement is A times the parent unit move.
Supply mu>=0,q>=1 satisfying A^(mu+q)=A^mu. Select a genuinely growing rooted
first-letter power-limit P. Finally supply a FINITE initial black list B.

**Claim.** It is decidable whether the entire infinite typed path P is
exactly the Langton-ant orbit of B at the specified initial pose.
If yes, the finite endpoint-pose argument proves that its movement tail is
not eventually periodic. If  the path is not that ant orbit.

This is a decision procedure for a specified path presentation AND a
specified finite seed. It is neither an arbitrary finite-seed capture
decider nor a decision procedure for existence of some finite realizing B.
Images need not have equal lengths, conserve signed charge, be half-turn
symmetric, or have orthogonal A. Complexity is not claimed practical.

Take a power psi=phi^m fixing the selected root s0, and replace A by A^m.
The finite-power property is preserved and an eventual period can be found
by enumerating powers. From now on write phi for this fixed-point power.
Delete letters unreachable from s0. The ordinary typed movement/heading
geometry is checked first by finite literal calculations.

## 2. Mod-two occupation is effectively base-two automatic

Let Q_s(r;X,Y) be the Laurent polynomial over F2 whose coefficient at(x,y)
is the number, modulo two, of reads of that cell in phi^r(s). At r=0 every
Q_s is1. For image occurrences t_j at proper prefix position p_j,

    Q_s(r+1)=sum_j X^((A^r p_j)_x) Y^((A^r p_j)_y) Q_(t_j)(r).

Thus the vector Q(r) satisfies Q(r+1)=T_r Q(r), where T_r is an eventually
periodic finite sequence of Laurent-polynomial matrices over F2. For one
period block M and each phase 0<=alpha<q, define the multiplication order

    M = T_(mu+q-1) ... T_(mu+1) T_mu,
    L_alpha = T_(mu+alpha-1) ... T_mu,    L_0=I.

Then

    Q(mu+qn+alpha)=L_alpha M^n Q(mu).

Choose a monomial X^C Y^D which clears all negative exponents in M, and
constant monomial shifts clearing Q(mu) and every L_alpha. Consequently
a shifted phase vector is of the form

    V_alpha(n)=L'_alpha (M')^n v,

with polynomial matrices/vectors. Each of its coordinate generating series
in Z is a rational function

    L'_alpha (I-Z M')^(-1) v

in F2(Z,X,Y), with a polynomial denominator having constant coefficient1.
The original coefficient index is recovered by an affine change
(x,y)->(x+Cn+c_alpha,y+Dn+d_alpha). Early r values are finite exceptions.

Here is a self-contained finite-automaton construction for any such rational
series P/H, where H(0,0,0)=1. For e in{0,1}^3 let Lambda_e retain monomials
whose three exponents are congruent to e modulo two, subtract e and halve.
The characteristic-two identity gives

    Lambda_e(P/H)=Lambda_e(P*H)/H.

For each variable i, put d_i=max(deg_i P,deg_i H). The numerator map
P->Lambda_e(PH) preserves coordinate degree bounds d_i. There are at most
2^((d_Z+1)(d_X+1)(d_Y+1)) polynomials over F2 within that degree box. Explore all
reachable numerator states, with these eight digit transitions and output
the numerator's constant coefficient. This is a terminating least-significant-
digit coefficient automaton. Its denominator remains H throughout.

Therefore the relation Q_s(r,x,y)=1 is effectively two-automatic, after the
phase congruence and affine coordinate substitutions. Signed spatial
coordinates may be represented by their sign and magnitude; addition,
constant multiplication, comparisons and Presburger sets are automatic in
that presentation. This does NOT assert that Q is Presburger: parity
patterns such as Pascal-triangle support are genuinely nonsemilinear.

For background on the standard Cartier construction, see Rowland,
Stipulanti and Yassawi, “Algebraic power series and their automatic
complexity I: finite fields”, https://arxiv.org/abs/2308.10977.
The rational finite-numerator argument above is the only portion needed.

## 3. Canonical templates from one representative occurrence

For every reachable letter s choose one fixed finite prefix v_s such that
v_s s is a prefix of P. These can be obtained by expanding the nested root
prefixes until every reachable letter occurs. Reachability is computed by
the finite substitution incidence graph. Every reachable letter occurs in
some finite power; nestedness and nonerasing images ensure that all have
occurred by one finite common level. Set v_s0 to the empty word.
Let z_s(r)=A^r p(v_s). This has finitely many eventually periodic values.

Let Q_(v_s)(r) be the parity-read polynomial of phi^r(v_s). It is a fixed
finite sum of translated Q_t(r), with translations A^r times ordinary
prefix positions of v_s. Hence it too is effectively two-automatic.

Define COMPLETE input/output board templates, in block-local coordinates,

    I_s(r) = translate_(−z_s(r)) [ B XOR Q_(v_s)(r) ],
    O_s(r) = I_s(r) XOR Q_s(r).

These are finite sets for each r, and effectively two-automatic relations
in(r,x,y). They are computed from B and the path presentation. There is
no guess of a board formula and no first-visit-color oracle.

The intended meaning is simply the board before/after the chosen occurrence
of phi^r(s), if that prescribed prefix has in fact been followed. Parity
flips can be computed for any prescribed geometric word, regardless of
whether it is ant-legal. This avoids circularity.

## 4. Finite automatic checks are sufficient

Use the exact read-set relation R_s(r,x,y) from the earlier bridge and its
finite-power addendum. It is Presburger, hence also two-automatic.

Check each r=0 turn against I_s(0,origin). Check the frame-agreement condition
for every parent s, image occurrence j and all r>=0:

    I_s(r+1) XOR XOR_(i<j) [A^r p_i + Q_(t_i)(r)]

must agree with A^r p_j+I_(t_j)(r) on A^r p_j+R_(t_j)(r).
All variables other than r,x,y range over supplied finite sets. XOR,
translation, intersection, equality, quantification and emptiness are
effective operations on synchronous automatic relations. Thus every check
terminates by finite automata constructions. The exact endpoint identity
follows directly from the displayed recurrence for Q_s, or may be checked.

The same read-footprint frame induction as before now proves that every
phi^r(s) is legal on I_s(r). At the root, I_s0(r)=B for EVERY r because its
representative prefix is empty. Hence all nested root prefixes run on the
one given B, so their infinite limit is its actual orbit. No accumulated
black/white-demand search or independently reset board is involved.

## 5. The checks are also necessary

Suppose P really is the ant orbit of B. Since P=phi(P), each
phi^r(v_s s) is an actual prefix of P. Therefore its chosen block begins
on exactly the canonical I_s(r), and each of its child blocks is also an
actual occurrence of the corresponding refined typed word.

Two legal executions of one finite typed word, from possibly different
complete boards, MUST agree on that word's whole read set at entry.
At a cell's first read, its prescribed turn fixes its entry color; prior
flips at that cell are zero. Equivalently, each cell's entry color is
uniquely determined by its first occurrence in the word. Consequently the
actual input of each child block agrees with its representative I-template
on the entire child read set. Every frame check therefore passes, as do
the base checks. This proves necessity and completes the decision theorem.

## 6. What is and is not established

This bypasses the still-unproved question whether earliest-read terminal
colors are semilinear. The parity boards are automatic, not necessarily
Presburger, and canonical occurrence templates convert chronology to
inductive comparisons.

The result is an analytic algorithm with explicit terminating constructions.
A practical integrated implementation of the rational matrices, automatic
relations and quantified frame checks has not yet been executed. No tested
candidate has passed all checks. A failed template check gives a finite
r/cell witness to disagreement; a literal simulation can independently find
the eventual first incorrect read.

Existence of SOME finite seed is not asserted decidable. Enumerating finite
B and applying the given-seed decider makes existence recognizable in this
specified morphic class. It does not make finite-seed noncapture generally
recognizable, nor provide a reduction from an undecidable problem.
