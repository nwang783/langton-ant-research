# Exact total-renewal and ranking form of the highway conjecture

22 October 2026. Status: elementary deductions passed independent analytic audit.
Dependencies: the audited adjacent-defect theorem, exact standard-tail verifier,
and the total future-pair algorithm in adjacent_defect_quantitative_compactness.md.
No universal termination or rank construction is claimed.

## 1. A deterministic total transition system

Let X be a complete finite black field and ant pose, immediately before its
next read. Use the unique true inverse history to define its preceding ten
turns. This convention is essential: it prevents losing pairs overlapping a
renewal boundary.

Define R(X) as follows. If there is no adjacent bad-ten pair ending at a read
indexed t>=0, return the terminal symbol bottom. Otherwise let t be the FIRST
such index and return the complete physical state F^(t+1)(X).

To decide existence with the true-history convention, first check the ten events whose11-letter windows straddle the initial cut, then apply the one-sided future-pair decision theorem to wholly future windows. The decision theorem therefore makes R a total computable function. After a positive
existence decision, ordinary simulation locates the first event and its full
successor field. Its running time or output size need not be polynomial in a
binary coordinate encoding. A distant interaction can generate an enormous
wake before the event occurs.

By construction no pair is skipped and each nonterminal application consumes
exactly one pair. Consequently:

    X captures standard104 iff some finite iterate of R reaches bottom.

If R never terminates, the associated physical orbit has infinitely many
adjacent pairs and is a genuine noncapture. Conversely all noncapturing
finite inputs give infinite R trajectories. This is a new choice of exact
renewal events, not the first known renewal formulation: the recovered source
research/renewal.py already has a different total complete-history renewal.

## 2. All finite count tests are recursive

For q>=0 define E(X,q) to mean that at least q future adjacent pairs occur.
E(X,0) is true; for q>0 evaluate R up to q times. Thus E is a total recursive
predicate jointly in the finite configuration encoding and q. It is monotone
in q, and

    H(X) iff exists q not E(X,q),
    not H(X) iff forall q E(X,q).

For each finite n the set of seeds with EXACTLY n future pairs is recursive:
E(X,n) and not E(X,n+1). The highway conjecture becomes the specific statement

    forall finite X exists q not E(X,q).

This is a Pi_2 presentation, not a Pi_2-hardness or independence proof. A halting
many-one reduction to any supplied finite pair count is impossible because E
is recursive. A reduction to the unbounded iteration problem remains logically
possible, but any proof that H itself is undecidable would refute the universal
conjecture, since if H were all inputs it would be decided by constant YES.

## 3. Exact natural-number ranking equivalence

The universal conjecture is equivalent to the existence of a total computable
natural-number rank rho on all finite states and bottom, with rho(bottom)=0,
positive rho(X) whenever R(X) is nonterminal, and

    rho(R(X)) < rho(X) whenever R(X) is nonterminal.

The forward implication is constructive under the truth of the conjecture:
iterate R until terminal, count the remaining adjacent events, and set rho(X)
to that count. Since every orbit terminates, this is a total computable function.
Each nonterminal transition removes exactly one event.

For the reverse implication, an infinite R trajectory would give an infinite
strictly decreasing sequence of natural numbers. Hence every input terminates.

One may equivalently require strict descent also on the final edge to bottom
by defining rho(X)=1 plus its remaining event count for every non-bottom X.
The event-free physical states then have rank1, and bottom rank0.

This is only an existence equivalence. It does not give an independently
computable formula for rho or prove its totality without the conjecture. A
bound depending only on initial black COUNT is substantially stronger and is
not supplied. Nor does the computable-rank equivalence preclude proof-theoretic
independence: a theory may be unable to prove that the rank-computing program
halts on every input. Transfinite ordinal methods can be useful for proving
termination even when the actual deterministic remaining-length rank is an
ordinary natural number on each terminating input.

## 4. Known long singleton controls do not make this rank unbounded

The audited exceptional singleton family with q_n=(-33-2n,-14-2n), n>=200,
has unbounded actual standard-tail onset. However its certified turn decomposition
is

    fixed9977, SW^(n+8), fixed51118, NE^(n+7), fixed8078, NW forever,

where each variable block and the terminal tail is a cyclic standard104 word.
Inserting more full periods into a block already longer than104 does not change
any bad-ten or adjacent-pair count: the interior contributes none, and each
fixed seam has the same bounded window data. Thus this particular family has a
constant remaining-pair rank, despite its unbounded capture time.

This is a structural consequence of the all-parameter certificate, not an
extrapolation from finite numerical samples. It is another reason not to
confuse delay, isolated-defect count, adjacent-pair count, and permanent onset.
It neither proves nor disproves the existence of a cardinality-only rank bound
for all singleton or all finite seeds.

## 5. Event-count complexity cannot hide in long standard delays

Status: independently audited deduction, 22 October2026.
The new elementary transition theorem makes E(X,q) primitive recursive,
not merely recursive: iterate the elementary total map R at most q times.
Fix an effective finite alphabet encoding of finite states, with a decidable
validity test. Let |X| be encoding length. Define

    C(n) = max({N_K(X): |X|<=n and H(X)} union {0}),

where N_K counts true-history future adjacent pairs and H is exact standard
capture. C is a total finite-valued function even if H is not all inputs.
It ignores noncapturing inputs, which have infinitely many pairs.

Then C and the characteristic function of H have the same Turing degree.
Moreover H is decidable iff C has a total computable majorant.

Proof. An H oracle selects the finitely many positive inputs of length<=n;
for each, iterate R to terminal and count events, giving C(n). Conversely,
if g(n)>=C(n), test E(X,g(|X|)+1). This is false for a capturing X and true
for a noncapturing X, because the latter has infinitely many events. Thus
one such finite-count query decides H. Taking g=C proves the degree claim.

If H is undecidable, C exceeds EVERY total computable function infinitely
often. Otherwise only finitely many exceptions to some proposed bound could
be absorbed into a hardcoded finite maximum, giving a computable majorant.
This is infinitely-often excess, not eventual domination.

The same argument is local to a compiler family. Suppose f maps machine
inputs computably to ant seeds and is claimed to satisfy

    machine e halts iff H(f(e)).

If there is a computable g(e) such that EVERY capturing f(e) has at most g(e)
adjacent events, then the alleged halting problem is decidable by the single
query E(f(e),g(e)+1), contradiction. Thus a halting-to-capture compiler cannot
put all unbounded computational difficulty into long standard highway delays
while keeping the number of adjacent defects computably bounded on its
halting outputs. This is a genuine obstruction to that architecture, not an
obstruction to all finite-support computation. No such compiler is known.

For encoding-size complexity, a primitive-recursive bound on capturing event
counts is equivalent to a primitive-recursive bound on their actual exact-tail
checkpoint times. One direction counts at most one event per read (with a fixed
boundary allowance). For the other, iterate the elementary R transition bound
for at most the supplied event budget plus one terminal call, keeping explicit
mass/radius bounds after each step. Primitive recursion closes this operation.
This equivalence is about computable input encodings, not black cardinality
alone. At fixed mass, long physical delays and bounded event counts remain
compatible, as in Section4.


## 6. Linear one-renewal cost sharpens the majorant comparison

The independently audited update in elementary_adjacent_renewal_bound.md
uses the seven-word actual-history linear fuel bound. For explicit binary
input length<=n, its closed iteration estimate gives

    F(n) <= (n+2^(n+1)+543960)*138853063^(C(n)+1),
    C(n) <= F(n)+10.

Thus C has an elementary majorant iff F has an elementary majorant, in
addition to the earlier primitive-recursive and computable equivalences.
This is a bound conditional on the number of capturing renewal events, not
an unconditional global count bound or a capture theorem.

The same logical renewal construction may now use only K labels outside
the independently audited six-label union in
../word_stabilization/six_label_union_capture.md. It remains total by exact
tail-certificate dovetail, and its iteration terminates exactly on H.
The quantitative one-transition bound above is for ALL K events; it does
not automatically bound one transition of this more selective renewal.
