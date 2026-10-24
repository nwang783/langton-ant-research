# Inductive finite-seed certificates for unit-scale refinements

2026-10-23 03:04 UTC. Analytic certificate theorem independently signed as audit IB.
No nontrivial candidate has passed it. This is not a general finite-seed
decider and does not assume weighted chronological equality is automatic.

## 1. Typed geometric data

Supply a finite alphabet S. Each letter has an incoming compass heading,
a prescribed R/L turn, and the resulting outgoing heading and unit move d_s.
Supply a nonempty image phi(s), with compatible adjacent heading types.
Its first incoming heading equals that of s; its final outgoing heading
also equals that of s. Its net displacement is a*d_s for one common
Gaussian unit a in {1,i,-1,-i}. These are finite checks.

Each r-fold refined block has its parent's incoming/final headings and
endpoint a^r*d_s. Its proper read positions form a finite set R_s(r).
Image lengths may vary and image signed charge need not be conserved.

Select a letter s0 on a first-letter cycle of length m. Check that
phi^m(s0) begins s0 and has length at least two. Because images are nonempty,
the words phi^(mn)(s0) form strictly growing nested prefixes and define an
infinite typed turn path. Nongrowing roots do not define such a certificate.

## 2. Exact level-read sets are effectively Presburger

Let q be the order of a. For each ordinary image letter occurrence j of
phi(s), let p_(s,j) be its proper read position and t_(s,j) its child letter.
Construct a finite directed multigraph with vertices (s,l), l modulo q,
and an edge for each occurrence

    (s,l) -> (t_(s,j),l-1),    weight a^l*p_(s,j).

A read cell in phi^r(s) is EXACTLY a weight sum along an r-edge walk starting
at (s,r-1 mod q), ending at any letter state. This follows by selecting one
child occurrence at each refining level. For r=0 the read set is {origin}.
The unit assumption is essential: it makes the phase graph finite and the
edge weights constant.

Here is an explicit Presburger description of weighted walks, without
appealing to automatic chronological equality. For fixed start and end
vertices introduce a nonnegative integer multiplicity n_e for every edge.
Require

- sum n_e=r;
- x=sum n_e*w_(e,x), y=sum n_e*w_(e,y);
- at every vertex, outflow-inflow equals the start indicator minus the end
  indicator;
- every vertex incident to a positive-multiplicity edge is connected to the
  start in the undirected graph of positive-multiplicity edges.

The last condition is a finite Boolean formula: disjoin simple undirected
paths of length at most the number of vertices minus one, using n_e>0 as
edge predicates. With the flow equations it is exactly the directed Euler
trail criterion. For an open trail, add an end-to-start edge; a weakly
connected balanced directed multigraph admits an Euler circuit. Removing
that edge gives the desired walk. The zero-edge case is handled separately.

All formulas are Presburger. Disjoin the finitely many end vertices and
starting rotation phases, tying the latter to r modulo q. Thus the complete
relation R_s(r,x,y) is effectively Presburger, uniformly from the substitution.
This statement concerns read SETS, not first or consecutive read chronology.

## 3. Supplied parametric board families

Supply Presburger formulas I_s(r,x,y) and O_s(r,x,y), intended as the complete
input and output black boards for the finite block phi^r(s). Require each
board to be finite for each r. This is itself Presburger:
for every r there exists a coordinate bound containing every member.

At r=0 check that I_s(0,origin) matches the prescribed turn and

    O_s(0) = I_s(0) symmetric_difference {origin}.

For the inductive step write

    Delta_t(r)=I_t(r) symmetric_difference O_t(r),
    z_j(r)=a^r*p_(s,j).

The shifts z_j are periodic in r, so they are Presburger after a finite
phase split. Let the proposed current complete board before child j be

    G_(s,j)(r) = I_s(r+1)
        symmetric_difference XOR_(i<j) [z_i(r)+Delta_(t_i)(r)].

For every r>=0, every parent s and every child occurrence j, check

    G_(s,j)(r) agrees with z_j(r)+I_(t_j)(r)
    on the footprint z_j(r)+R_(t_j)(r).                 (A)

Also check the exact complete-board endpoint identity

    I_s(r+1) XOR XOR_j [z_j(r)+Delta_(t_j)(r)]
       = O_s(r+1).                                    (B)

These are finite first-order Presburger sentences after substitution.
Fixed finite XORs are Boolean formulas. No count-parity quantifier is needed.

Induction proves the intended finite-block semantics. By the induction
hypothesis each child word is legal on its I-template. Agreement on its
ENTIRE exact read set ensures it follows the identical literal trajectory
on the actual current board, regardless of different cells outside that
footprint. Its complete change is the translated Delta. Condition(A) permits
the next child; condition(B) closes the parent. This is a frame argument on
read sets, not a claim that an unordered read set alone proves legality.
All chronology is inherited from the already proved child blocks.

The base and endpoint checks also imply Delta_s(r) is contained in R_s(r).
A validator may check that redundant property explicitly.

## 4. Extracting one genuine finite initial seed

The root's refining powers must all use ONE initial board, not independently
chosen level boards. Define Presburger demand sets

    Black = {z : exists n>=0, z in R_s0(mn) and I_s0(mn,z)},
    White = {z : exists n>=0, z in R_s0(mn) and not I_s0(mn,z)}.

Check that Black is finite and Black intersect White is empty. If so, extract
Black as an explicit finite list. On that single seed, every nested root
prefix is legal: it agrees with its I-template on the complete read set.
Induction along ordinary time therefore identifies the infinite limit as
the actual finite-seed ant trajectory. Black is its minimal initial support.
Extra supplied initial cells are allowed only where no white demand occurs;
given-seed compatibility is another Presburger check.

No silent board reset occurs between levels. Disjointness of the accumulated
demands is precisely what prevents that invalid inference.

Every accepted growing unit-scale root model is nonperiodic. Its refining
prefix lengths tend to infinity, while its endpoint poses belong to the
finite set {a^(mn)*d_s0, final-heading(s0)}. A further subsequence returns
to one physical pose infinitely often. An eventually periodic movement tail
with nonzero drift cannot do that; a zero-drift periodic tail would stay in
a finite domain, contrary to finite-domain escape. Thus a successful finite
certificate would be a genuine counterexample to standard capture.

## 5. Scope and implementation status

This gives a terminating mathematical validator for SUPPLIED finite
Presburger I/O families, using Presburger decision procedures. It is not a
claim that all genuine unit models admit such families, or an algorithm to
find the families. There is no accepted nontrivial model. Finite-particle
families and finite periodic-rail/cap families are natural expressible targets.

It differs from the existing ordered-event framework: the complete weighted
chronology need not have a Presburger presentation here. Only level read
sets are computed; chronology is discharged inductively by finitely many
local board-composition identities. It also differs from the expansive
bounded-carry verifier, whose contraction premise fails at unit scale.

The present artifact supplies the formula construction and exact small
controls for the read-set claim. A practical end-to-end Presburger solver
wrapper has not been implemented. Do not report the mathematical validator
as an executed or accepted certificate.
