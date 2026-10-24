# Selecting any occurrence: an automatic forced-seed construction

Date: 2026-10-23. Status: independent analytic review passed for the A=I theorem
and the elementary genuine-path-cover lemma (2026-10-23 04:52 UTC). No integrated implementation or new growing ant model is claimed.

## 1. The precise class and conclusion

Fix a finite typed alphabet (in particular the eight incoming-heading/turn
states), a nonerasing substitution phi, and a root a for which phi(a) begins
with a and |phi^r(a)| tends to infinity. Every image must preserve its coarse
unit displacement and final heading: spatial A=I. Let P=lim phi^r(a) be the
resulting prescribed geometric/read word. This is syntactic data; ant legality
is NOT assumed. Initial pose is fixed, and white corresponds to R.

**Theorem.** One can effectively construct a 2-automatic coloring
b_*(x,y), white outside the set visited by P, such that every initial coloring
realizing P agrees with b_* on all visited cells. Consequently it is decidable
whether P is realizable from SOME finite-support board, with no supplied seed,
coordinate bound, or mass bound. On a yes-instance one can return its unique
minimal finite seed. The proof uses no finite-valued signed-occupation assumption.

This is a theorem about a fixed highly structured prescribed path. It says
nothing about whether an arbitrary finite-seed ant enters such a presentation,
and it does not decide the global finite-support highway conjecture.

## 2. Exact all-depth parity is automatic

Let Q_s(r,z) in F2 be the number of reads at z in phi^r(s), modulo two. If child
j of image s is state t_sj at offset p_sj, then

    Q_s(0,z) = 1[z=0],
    Q_s(r+1,z) = XOR_j Q_t_sj(r,z-p_sj).

The signed-coordinate relation Q_s=1 is effectively 2-automatic by the rational
Laurent transfer and Cartier construction already proved in `theorem.md`.
This holds without any legality assumption: Q is simply read-count parity.
All affine integer substitutions and Boolean operations on its arguments are
effective automatic constructions. Signed coordinates may be represented by
sign plus magnitude, or by a finite orthant split.

## 3. A bounded family of genuine occurrences covers every visited site

Form the finite directed occurrence graph with vertices s and DISTINCT edge
letters e=(s,j,t_sj), weighted by p_sj. Let L be the regular language of all
finite edge paths from a, with every endpoint accepting. The empty path is
included. A path e_1...e_r picks one actual leaf/read in phi^r(a); its position
is the sum of its edge weights and its turn is the final state's turn.
Thus the weight image of L is exactly the visited set R of P.

One route uses the following primary, constructive language theorem: for a regular
language L there is an effective bounded expression B=w_1*...w_m* with
Parikh(L intersect B)=Parikh(L). The intersection is genuinely a subset of L,
not merely a different language with the same abstract Parikh image.
Source: Ganty, Majumdar, Monmege, *Bounded Underapproximations*, Section4.1,
Lemma5 (and Problem1),
https://people.mpi-sws.org/~rupak/Papers/BoundedUnderapproximationsFMSD.pdf .
An alternative effective construction enumerates bounded expressions B and
checks the displayed equality by effective Presburger Parikh images; the
published existence theorem guarantees termination.

**Lemma (effective genuine bounded path cover).** In a finite directed graph,
every path has the same edge-count vector as a path in one of finitely many
effectively constructible linear path schemes. Every scheme instance is genuine.

Proof: use the following support-preserving reduction.
From any graph walk, repeatedly delete a nonempty contiguous closed segment
whenever deletion preserves the set of used edges. This process terminates in
a base walk b with the same endpoints and the same positive edge support.
Between two successive occurrences of a fixed vertex in b, the closed interval
cannot be removed. Hence it contains an edge with no occurrence outside that
interval. The intervals between successive occurrences are edge-disjoint as
positions in the walk, so their witness edge types are distinct. There are at
most |E| intervals per vertex. Consequently each vertex appears at most |E|+1
times, and the base length is at most |V|(|E|+1)-1.

The difference between the original and base edge counts is a nonnegative
integer circulation, because every removed segment was closed. Decompose it
into simple directed cycles. There are finitely many simple cycle types in the
finite graph; choose a fixed basepoint and order for each type. The base walk
visits every used edge, and therefore every chosen cycle basepoint. At the
first occurrence of each such basepoint insert, in the chosen fixed order, the
required powers of its cycle types. This is a genuine graph walk with EXACTLY
the original edge counts. In particular it has the same output position.

Enumerate every graph base walk of the displayed bounded length, and equip it
with stars for all simple cycles whose edges are in its support, inserted at
those fixed first occurrences. This directly constructs a finite family of
linear path schemes covering all possible edge-count vectors. Empty paths are
included separately. Thus the bounded-language theorem is a cross-check, not
an indispensable unproved lifting step.

The resulting schemes have the form

    pi(n) = u_0 v_1^(n_1) u_1 ... v_l^(n_l) u_l,  n_i>=0,

where each v_i is an actual closed edge path and every exponent choice is a
valid path from a. Their weight images cover R. Their final states are constant
per scheme. Both total length R_pi(n) and total weight W_pi(n) are affine integer
functions of n. The construction intentionally preserves genuine word order
within the chosen schemes, while changing the representative occurrence.

For each z in R choose the least scheme index having a representation of z,
then the lexicographically least exponent tuple n in N^l with W_pi(n)=z.
Every nonempty subset of N^l has a lexicographic minimum. The selected graph
Sel_pi(z,n) is Presburger: impose W_pi(n)=z, no earlier scheme representation,
and no lexicographically earlier tuple in this scheme. It is single-valued
on R. This chooses SOME occurrence, not the first chronological occurrence.

## 4. Exact parity before the selected occurrence

For an edge path e_1...e_r, put V_(d-1)=sum_(h<d) weight(e_h), and write
 e_d=(s_d,j_d,t_d). The part of phi^r(a) strictly before the selected leaf is
the disjoint ordered concatenation of the earlier sibling blocks at each level.
Consequently its read parity at z is exactly

    C(e_1...e_r,z) = XOR_(d=1..r) XOR_(i<j_d)
      Q_t_(s_d,i)(r-d, z-V_(d-1)-p_(s_d,i)).                 (1)

No earliest-visit operation occurs in this formula. It counts all previous
reads, even when the selected occurrence is very late and the cell was read
many times before.

For a fixed path scheme, a fixed connecting-word edge gives one Q evaluation
with affine arguments in (z,n). For edge h within repetition q of cycle v_i,
where 0<=q<n_i, both the current depth and accumulated weight are affine in
(z,n,q): earlier block lengths and displacements are affine in n, and the q
completed copies contribute q|v_i| and q weight(v_i). Formula(1) therefore
becomes a fixed finite XOR of terms of two forms:

    Q_s(affine(z,n)),
    XOR_(0<=q<n_i) Q_s(affine(z,n,q)).                     (2)

Each unbounded repetition is accounted for; there is no cutoff on n or depth.

## 5. Finite-fiber parity projection is effectively automatic

If A(u,q) is a synchronous automatic predicate and 0<=q<n_i is among its guards,
then the predicate "an odd number of q satisfy A(u,q)" is automatic.
Here u includes the nonnegative integer n_i. To see this constructively, use
canonical padded binary encodings of common input length L. Every q<n_i fits
in those L digits, and each q has exactly one such padded representation.
Take a deterministic automaton for A. For each visible input digit, sum over
the two possible q digits in F2. Track the vector of parities of paths reaching
each automaton state. There are only finitely many such vectors, so this is a
deterministic finite automaton with an output bit. The acceptance bit is the
sum of accepting-state coordinates.

Extra leading zero padding cannot introduce multiplicity: q<n_i excludes all
representations with a nonzero extra leading digit, and each old q has one
zero-padded extension. Thus this is a well-defined automatic relation on numbers,
not parity of infinitely many word encodings. The n_i=0 fiber is empty.
Affine-argument tests are first compiled into A, so their potentially larger
intermediate values introduce no extra counted encodings.

Applying this construction to every term in(2), then intersecting with the
unique Sel_pi and existentially eliminating n, constructs the exact automatic
value C_*(z) of the prior-read parity for the selected occurrence. The turn bit
ell_pi is fixed by the scheme's terminal state.

Define

    b_*(z) = ell_pi XOR C_*(z)  for z in R,
    b_*(z) = 0                 for z not in R.             (3)

Selection is unique, so the existential elimination here is ordinary projection,
not a parity sum over possible representative tuples. Equation(3) is automatic.

## 6. Necessity and the unbounded-mass finite-seed decision

If an initial board b realizes P, the color immediately before the selected
read at z is b(z) XOR C_*(z). It must equal that read's turn bit ell_pi. Thus
b(z)=b_*(z) for every visited z. Colors outside R never affect P and can be
removed. This proves uniqueness of the only possible minimal initial board;
it does not assert that the selected requirements are globally consistent.

An automatic subset of Z² is effectively testable for finiteness. For example,
decide the automatic first-order sentence

    exists M>=0 forall x,y: b_*(x,y)=1 implies -M<=x,y<=M.

If false, no finite seed realizes P. If true, find such M by effective witness
search and enumerate the finite set B_* in that box. Feed this explicit board
into the independently signed exact given-seed validator (`theorem.md`, IJ).
If it accepts, return B_*. If it rejects, no initial board can repair P, because
all boards realizing P must have exactly B_* on R and outside R is never read.
Every step terminates. The radius M is derived from the constructed automatic
coloring, not hypothesized as a search cutoff.

## 7. Scope of the improvement and unresolved implementation

This removes the unknown-mass barrier for the fixed A=I
presentation class, bypassing generic XOR-component reachability by exploiting
its specific origin in an ordered substitution. It does not decide arbitrary
bounded-displacement automatic XOR graphs; the general graph hardness result
remains intact, and no graph-to-ant compiler is furnished.

The existing implementation covers supplied parity and the one-ray automatic
parity extractor. The bounded occurrence-cover compiler, canonical tuple
selector, parity-projection automata, and final composed coloring have NOT been
implemented as an integrated solver. The result here is an effective mathematical
algorithm, not an executed discovery of a growing ant model.

## 8. Exact finite component controls

`check_forced_seed_components.py` / `forced_seed_components.json` execute 3,273
genuine support-preserving base/cycle reconstructions, 12,856 full prior-parity
fiber comparisons against literal refined words, and 11,264 bounded-hidden-
coordinate F2 projection checks including extra binary padding. The two projected
control machines have11 and37 determinized vector states. These independently
exercise the elementary constructions; they are not an integrated forced-seed
compiler and do not replace the analytic proof.
