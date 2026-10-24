# Exact inverse synthesis from automatic visit equivalence

22 October 2026. Status: analytic construction independently audited; working finite-automaton controls have not received a complete independent implementation audit. No finite-seed nonperiodic ant has been found. This extends the earlier full automatic pose-graph framework rather than asserting that all integrated automatic walks have automatic graphs.

## 1. Less than a position graph is enough

Let c(t) be a computable infinite R/L word, and let p(t),h(t) be its uniquely integrated geometric pose path from a specified initial pose. Suppose c's L-time set and the relation

    Q(s,t) iff p(s)=p(t)

have supplied, verified synchronous automata in one ordinary integer time base. Q must be proved to be the ACTUAL cell-equality relation of the integrated path; an arbitrary claimed equivalence relation is not sufficient.

Define

    First(t) iff not exists s<t: Q(s,t),
    FirstL(t) iff First(t) and c(t)=L,
    Consecutive(s,t) iff s<t and Q(s,t)
                         and not exists r: s<r<t and Q(s,r).

The path is realized by some finite black seed exactly when:

1. Every Consecutive pair has opposite turns.
2. The set FirstL of times is finite.

All these conditions are decidable by finite-automaton first-order closure, since time addition and order are automatic. Finiteness is the assertion that FirstL is bounded in time. When finite, enumerate the finite set and integrate the path to recover its cells. Those cells form the unique minimal initial black seed. First visits are one-to-one with visited cells, so using finite first-L TIMES is equivalent to the earlier finite first-L CELL condition.

The proof is the same per-cell flip induction as the pose-graph inverse theorem. The geometry is now supplied by exact integration and a certified automatic equality relation, rather than an automatic position graph. Eventual standard104 or general turn periodicity can still be decided from the automatic turn predicate.

This is a useful extension to some k-regular integrated position sequences. It does not claim that arbitrary k-regular equality/zero sets are automatic.

## 2. An effective geometrically self-similar family

Take a uniform substitution phi(R)=u, phi(L)=v, both of length k>1, with u starting R. Starting at (0,0,N), assume:

- u ends with heading E and displacement a in Z[i];
- v ends with heading W and displacement -a;
- |a|>1.

The resulting fixed point c=phi^infinity(R) exists. Letter expansion preserves the old heading change modulo4, and multiplies every coarse displacement by the same complex scalar a. Hence

    p(kn)=a p(n),
    h(kn)=h(n).

Let q_(c,j) and e_(c,j) be the displacement and heading change of the first j letters of the macro phi(c). If h(n) is encoded clockwise from N and Rot_h is that clockwise physical rotation, then

    p(kn+j)=a p(n)+Rot_(h(n)) q_(c(n),j),
    h(kn+j)=h(n)+e_(c(n),j) mod4,
    c(kn+j)=phi(c(n))[j].

The finite state (h(n),c(n)) therefore has an explicit k-DFAO update on MOST-significant-digit prefixes. The integrated position has a common expanding scalar recurrence. Its ordinary time/position graph need not be automatic.

## 3. Bounded-difference automaton for Q

Read the base-k digits of s and t from most significant to least, padded with leading zeros. Track the two finite (heading,letter) states and the exact Gaussian difference D of their current prefix positions. On the next pair of digits,

    D' = a D + delta,

where delta is the difference of two macro offsets from a fixed finite set. Let M bound every |delta|, and choose R with (|a|-1)R>=M.

If |D|>R, every following update satisfies

    |D'| >= |a||D|-M > |D|.

Therefore such a state can never end with D=0. Send it to a rejecting sink. There are only finitely many Gaussian D with |D|<=R, so the resulting automaton is finite. Accept exactly D=0 at the end. This is precisely Q: tracked differences are literal position differences, and the sink cannot discard an accepting continuation.

All arithmetic needed to select R and build the automaton is exact. One may take an integer M and find an integer R satisfying

    |a|^2 R^2 >= (R+M)^2.

Both sides are integers. Reverse the regular language and determinize to obtain the least-significant-digit convention used by the implementation. Leading-zero stability becomes trailing-zero padding stability.

Thus finite-seed realizability is DECIDABLE for each supplied substitution satisfying these geometric conditions. This is a genuine all-time certificate procedure, not a bounded trace acceptance test. It does not decide whether any substitution in the infinite family succeeds.

## 4. Any successful expanding example would be nonperiodic

The prefix phi^n(R) ends at time k^n and at position a^n. Every step is a quarter-turn followed by one unit move, so for k>1 the displacement of a k-step macro satisfies |a|<k: equality in the triangle inequality would require every unit move in the same direction, contrary to successive quarter-turns.

Consequently p(k^n)/k^n tends to zero. An eventual periodic finite-seed ant has a nonzero linear drift and hence a nonzero limit p(t)/t. These are incompatible. Any finite-seed realization in this family would therefore be a genuinely aperiodic counterexample to the standard-highway conjecture. No example is known.

## 5. An all-length signed-mass obstruction

Write e(w)=#R(w)-#L(w). If the macro words satisfy the stronger INTEGER identities

    e(u)=1 and e(v)=-1,

then e(phi(w))=e(w) for every finite word w. In particular e(phi^n(R))=1. A finite ant following the fixed point would consequently have exactly |B_0|+1 black cells at time k^n, because each R adds a black cell and each L removes one.

But its position at those times is a^n, which is unbounded. The audited axial midpoint inequality implies

    |B_0|+|B_(k^n)| >= 2 ||(p_(k^n)-d_h/2)-(p_0-d_(h0)/2)||_infinity,

a contradiction. This excludes the entire charge-preserving self-similar family at EVERY macro length, not only a bounded search. Uniformity is unnecessary for this obstruction: it applies to any prolongable substitution with the same geometric scaling and exact signed-charge preservation.

More generally, if e(u)=q and e(v)=-q, then e(phi^n(R))=q^n. An allowed negative q satisfies q<=-3, because q is1 modulo4. It is impossible for finite support, since negative odd powers would eventually force negative black mass. For positive q<=|a|, the midpoint inequality again rules out the model: its right side is at least sqrt(2)|a|^n-O(1), whereas its left side is 2|B_0|+q^n. Thus a symmetric signed-charge candidate must have q>|a|. This is only a necessary condition.

## 6. Implemented controls and bounded family exclusion

- automatic_radix.py implements first-order closure over arbitrary fixed natural-number radix, with exact hidden-witness padding; 28,800 arithmetic comparisons pass in bases2,3,5,7.
- selfsimilar_visit_relations.py constructs the bounded-difference automaton and inverse tests directly from u,v.
- R->RRL, L->LRL, scale2-i: the raw729-state difference automaton minimizes to the TWO-state identity relation. Thus the entire infinite walk is self-avoiding. Its first-L set is infinite, so it requires infinitely many initial black cells.
- R->RLR, L->LLR, scale2+i: the same exact conclusion holds. Neither is an ant counterexample.
- The overlapping controls R->RRRLL, L->LRRLL and R->RLRLLLLRL, L->LRLRRRRLR have automatic cell-equality relations and exact opposite-read failures.

The separate finite exhaustive search search_turtle_substitutions.py covers uniform odd lengths5,9,13,17 with |a|^2=k, opposite quarter-turn endpoints, u prolongable on R, and both macros internally alternating-valid. All4,45,2488,92919 candidate pairs respectively fail by explicit finite alternating-read contradictions; the latest failures occur at times8,56,297,662. This restricted enumeration is not an all-length theorem. The signed-mass obstruction above, in contrast, is all-length but only for the stated signed-charge subfamily.

## 7. Common expanding affine recurrences, beyond two-letter morphisms

The same difference argument applies to any finite-state position recurrence

    state(kn+j)=delta(state(n),j),
    p(kn+j)=a p(n)+b(state(n),j),

with a Gaussian integer a, |a|>1, integer k>1, p(0)=0, and a leading-zero-stable initial state with zero initial digit0 offset. All offsets are fixed Gaussian integers. Track the two finite states and the position difference, exactly as above. This makes every fixed-difference relation p(s)-p(t)=v automatic; enlarge the carry radius to include the finitely many target v. No canonical complex numeral system is needed.

In particular, the four unit-step relations give the outgoing directions at each ordinary time, using t+1. One can decide whether every move is unit and every consecutive pair of moves is perpendicular, with the first move perpendicular to the specified initial heading. The prescribed R/L word is then automatic. Apply the same alternating-visit and finite-first-L-time tests. This is an effective finite-seed realizability test from the recurrence alone, not from a separately asserted geometric path. For a specified finite input B, equality to any fixed cell q is also automatic by comparing p(t) with p(0)=0 using target difference q, so input compatibility is checkable.

If |a|<k, every such path has |p(t)|=O(t^(log_k|a|)), hence sublinear displacement. A validated finite-seed ant in this subclass would therefore be genuinely aperiodic. No such model has been found.

expanding_recurrence_visits.py implements this route. The ordinary dragon needs only four accessible states among the eight parity/direction states in its unreduced presentation. Its cell-equality automaton has14 states. Full all-time geometry passes, but the exact inverse test finds repeated R reads at times7 and11 and infinitely many first-L cells. This agrees with the earlier complex-base check while making no position-numeral assumption.

## 8. A finite recurrence-state exclusion

A ONE-state expanding recurrence cannot even be a unit quarter-turn walk. Write d(n)=p(n+1)-p(n), and b_last=b(k-1). At a digit-carry boundary,

    d(kn+k-1)=a d(n)-b_last.

Iterating these boundaries gives an expanding affine map on d(n). If every d is a unit vector, boundedness forces every d(n) to equal its unique fixed point b_last/(a-1). The walk is straight, contradicting quarter-turn geometry.

For binary time, a in {1+i,1-i,-1+i,-1-i}, and at most FOUR accessible recurrence states, a finite exhaustive search finds no ant path on ANY initial coloring. This finite computer-assisted exclusion has an independent complete replay, with no imported recurrence or automaton code; it is not an all-state theorem.

Completeness of the finite parameterization: an accessible m-state DFA has a shortest word reaching each state of length at most m-1. Hence each state is reached at some index n<2^(m-1). The recurrence's two offsets for that state are determined by p(n),p(2n),p(2n+1), all within the first2^m-1 MOVES. Enumerate all legal quarter-turn prefixes of that length, all canonical accessible binary state graphs with the zero digit fixing the start state, and all four scalar choices. Repeated-state offset consistency rejects incompatible combinations. No arbitrary Gaussian offset is omitted.

- m=2:128 consistent recurrences;124 nonunit failures and4 alternating-read failures.
- m=3:1512 consistent recurrences;1422 nonunit failures and90 alternating-read failures.
- m=4:816 canonical state graphs,6192 legal15-turn prefixes,3924 consistent recurrences;3136 nonunit failures and788 alternating-read failures. All fail by time19.

The four-state implementation uses equality partitions of the eight observed offset pairs to avoid a wasteful graph-by-prefix Cartesian product; it includes indistinguishable output pairs at distinct hidden states. No prefix is accepted as a positive infinite model. Scripts and controls: search_small_recurrences.py, search_four_state_recurrences.py, small_recurrence_controls.json, four_state_recurrence_controls.json.

A separate exact finite scan exclude_short_selfsimilar.py combines the signed-mass theorem with explicit alternating-read failures to exclude all805,145 prolongable-on-R geometric substitution pairs of odd lengths3 through17 with expanding a (not only |a|^2=k). Of these283,467 fail the mass theorem, and521,678 have finite alternating-read contradictions. All of these counts and finite failures passed independent full replay using feasible-word DFS and literal repeated substitution, without importing the original candidate generator or base-k letter oracle. They do not exclude longer substitutions or more-state recurrences.

Independent recurrence replay: audits/check_small_affine_recurrences_independent.py and its JSON. It matches1/2/3/4-state counts8/128/1512/3924, with latest rejection times3/11/18/19. The one-state direct finite enumeration supplements the general analytic one-state obstruction. The separate large turn-substitution enumeration is independently replayed in audits/check_short_substitutions_independent.py, .json, and .log; the latest finite conflict is at time8379.

## 9. Fixed recurrence parameters give a genuine decision problem

Status: independent analytic review passed on 22 October 2026.

For FIXED natural m,k with k>1 and fixed Gaussian a with |a|>1, the following existence question is decidable:

    Does some finite-seed ant, normalized to position0 and headingN,
    admit a leading-zero-stable common-a affine recurrence in base k
    with at most m accessible states?

There are finitely many state graphs. Every accessible state has a shortest input word of at most m-1 digits, hence has a representative n<k^(m-1). Its k offset vectors are determined by the actual positions p(n) and p(kn+j), all among p(0),...,p(k^m-1). Enumerate the finitely many unit quarter-turn words of length k^m-1, discard finite alternating-read failures, and derive every graph's offsets from those positions. Reject inconsistent repeated-state offsets. The all-time automatic inverse test decides every remaining recurrence and extracts its minimal finite seed when successful. This finite search terminates.

This also decides membership of a GIVEN finite seed in the bounded-parameter class: additionally test that its initial black bits agree with the first prescribed read at every visited cell, using the automatic fixed-position relations. Never-visited initial black cells are irrelevant and need not equal the minimal seed. Standard104 capture can then be decided for each matching recurrence.

Thus a halting reduction confined to fixed m,k,a cannot hide arbitrary computation in unbounded integer offsets or distant initial black cells. Arbitrary offsets are already covered by the finite geometry prefix, and unread cells cannot affect the orbit. This is a parameter-restricted decidability statement, not a claim about unbounded recurrence size or arbitrary ant seeds.

If |a|>k, a unit-step path of such a recurrence is in fact bounded. To see this, let f(s)=delta(s,0), b_s=b(s,0). Iterating the zero digit gives

    p(k^r n)/a^r = p(n) + sum_(i=0)^(r-1) b_(f^i(state(n)))/a^(i+1).

The left side tends to zero because |p(k^r n)|<=k^r n and k/|a|<1. Therefore p(n) equals a fixed convergent sum depending only on the finite state state(n). It takes finitely many values. Such a path cannot be an infinite classical-ant trajectory on any background: a bounded trajectory could be reproduced from finite support by copying the initial bits of its finitely many visited cells, contrary to finite-seed escape. This gives an all-state scale obstruction for |a|>k. For |a|<k, any successful finite-seed model would instead be genuinely aperiodic by the sublinear upper bound. The critical case |a|=k is not classified here.

## 10. A critical-scale rotation obstruction

Status: independent analytic review passed on 22 October 2026. This excludes unbounded unit walks in the stated class before imposing any ant-color legality.

Assume |a|=k. Let f(s)=delta(s,0), let b_s=b(s,0), and define the convergent finite-state correction

    F(s)=-sum_(j>=0) b_(f^j(s))/a^(j+1).

The eventually periodic state sequence makes each F(s) a Gaussian rational. It satisfies F(f(s))=a F(s)+b_s. Hence y(n)=p(n)-F(state(n)) obeys y(kn)=a y(n) exactly.

If p has unit steps, v(n)=y(n+1)-y(n) takes finitely many values and is k-automatic. The unit-step direction is automatic by the fixed-difference construction; states at n and n+1 are automatic as well. Choose a common most-significant-digit DFAO for this finite-valued sequence. At every reachable state q, telescoping gives

    sum_(j=0)^(k-1) v(delta(q,j)) = a v(q).

If some value is nonzero, take q of maximum magnitude M>0. Since |a|=k, equality holds in the triangle inequality for the displayed sum. Every child therefore has magnitude M and value (a/k)v(q). This remains true along every descendant path. A finite-state cycle then gives (a/k)^ell=1 for some positive ell.

Consequently, if a/k is not a root of unity, v is identically zero. Since the leading-zero-stable start has F(start)=0 and p(0)=0, y is zero and p(n)=F(state(n)) takes only finitely many positions. It cannot be an ant path on any background.

For Gaussian a and integer k, a/k has rational real and imaginary parts. A root of unity with both parts rational must be one of1,-1,i,-i. One elementary proof puts x=2*Re(a/k): the recurrence for2cos(n theta) makes x a rational root of a monic integer polynomial, hence an integer in{-2,-1,0,1,2}; x=±1 would give irrational imaginary part±sqrt(3)/2. Thus the only still-possible critical scalars are a=±k or±ik. No classification of those four cases is claimed.

Combined with Section9, an unbounded unit-step path in the common-scalar finite-state class must have either |a|<k or a in{±k,±ik}. This is a restriction on the certificate class, not on arbitrary ant trajectories.


## 11. Signed-charge spectrum versus visited area

Status: independent analytic review passed on 22 October 2026.

For the uniform two-letter family of Section2 put

    alpha=(e(u)+e(v))/2, lambda=(e(u)-e(v))/2.

The signed excess E_r of phi^r(R) obeys

    E_0=1,
    E_(r+1)=alpha*k^r+lambda*E_r,
    E_r=c*k^r+(1-c)*lambda^r, c=alpha/(k-lambda).

Here |lambda|<k. Equality would force the two macros to be monochromatic with opposite signs, whose odd-length quarter-turn endpoint has |a|=1, excluded by expansion. Thus alpha<0 forces E_r eventually negative with unbounded magnitude and is incompatible with finite black support.

There is a separate geometric bound that needs no finite-support hypothesis. The common expanding recurrence bounds EVERY read in the length k^r prefix inside a disk of radius C|a|^r: the prefix radius satisfies R_(r+1)<=|a|R_r+Q for a fixed maximum macro offset Q. Thus there are only O(|a|^(2r)) distinct visited lattice cells. If consecutive visits to every cell alternate R,L, its total signed contribution lies in {-1,0,1}. Therefore

    |E_r| <= number of distinct visited cells = O(|a|^(2r)).

Consequences:

- If alpha is nonzero and k>|a|^2, the substitution cannot be a legal ant path on ANY initial coloring, because its leading signed excess has size proportional to k^r.
- If alpha=0 and |lambda|>|a|^2, the same any-background exclusion holds.
- In the symmetric case alpha=0, a finite-support candidate must satisfy the combined necessary inequalities |a|<lambda<=|a|^2. The lower bound and positive sign are from the midpoint/mass argument; the upper bound is from visited area.

Equality k=|a|^2 or lambda=|a|^2 is not excluded by this exponent comparison. These are necessary filters, not a complete classification.

## 12. A coarse-vertex first-visit obstruction

Status: independent analytic review passed on 22 October 2026.

Again use the uniform geometric substitution, now with u beginning R and v beginning L. Suppose every internal macro read offset satisfies

    q_(c,j) not in a Z[i] for c in {R,L}, 0<j<k.

Since quarter rotations preserve a Z[i], the full path reads the sublattice a Z[i] exactly at macro boundaries kn. At these times

    p(kn)=a p(n), c(kn)=c(n).

Consequently n is a first visit to its cell if and only if kn is a first visit to its scaled cell. Any first-L cell q therefore gives first-L cells a*q,a^2*q,... . The cell0 is first read R at time0, so no first-L cell is0. Since |a|>1, every such sequence contains infinitely many distinct cells.

Thus finite black support would force NO first-L cells at all. The orbit would equal the empty-seed ant, regardless of unread initial black cells. But that independently certified standard104 trajectory has nonzero linear drift, whereas the self-similar endpoints p(k^r)=a^r have p(k^r)/k^r tending to0. Here |a|<k follows because equality in the k unit-step length bound would require every movement direction to be identical, contradicting genuine quarter-turn geometry. This is impossible.

This excludes a family by preservation of FIRST visits, not by net signed mass. For example u=RRRLRRLRLRLRR and v=LRRLRRLRLRLRR have length13, scale a=-3+2i, signed excesses5 and3, and satisfy the internal-sublattice condition. Their positive leading excess and k=|a|^2 evade the preceding sign/area filters, but they are ruled out by this first-visit obstruction. The example is only a negative control, not a claim that its infinite word otherwise passes cell alternation.

The finite hypothesis checker check_selfsimilar_obstructions.py records the three exact negative controls in selfsimilar_obstruction_controls.json. The proofs above do not depend on a bounded simulation acceptance criterion.

## 13. Uniform subballisticity on every time interval

Status: independently audited analytic deduction. This strengthens the earlier origin-based growth bound and clarifies which geometric counterexample architectures the common-scale automatic class can represent.

Assume the general recurrence of Section 8, with unit moves and 1<|a|<k. Let M=max_(s,j)|b(s,j)| and alpha=log_k|a|<1. After r digits, for 0<=j<k^r,

    p(k^r n+j)=a^r p(n)+B_r(S(n),j),
    |B_r(s,j)| <= M (|a|^r-1)/(|a|-1).

Thus the diameter of the positions in any aligned k^r-time block is at most

    D_r=2M (|a|^r-1)/(|a|-1).

Any interval of t moves with 1<=t<=k^r meets at most two adjacent such blocks. Their last and first poses are joined by one unit move. Therefore its endpoint displacement is at most 2D_r+1. Choosing the smallest r with t<=k^r gives the uniform bound

    |p(n+t)-p(n)| <= C t^alpha for EVERY n>=0,t>=1,
    C=4M|a|/(|a|-1)+1.

No ant-color hypothesis is used. This is a finite-state geometrically scaling unit-walk obstruction.

### 13.1. A computable bound on every translating periodic episode

Suppose a heading-restoring turn word w of length P and nonzero drift d occurs consecutively N times, starting at any time, not necessarily at zero. Then its displacement is Nd, so the uniform bound gives

    N^(1-alpha) <= C P^alpha / |d|.

Hence the number of repetitions is bounded by a constant determined by the recurrence and w. In particular, no such common-scale path contains arbitrarily long standard104 episodes, even if those episodes are separated by scattering events that make the total origin-based displacement sublinear.

An entirely rational effective bound avoids logarithmic comparisons. Choose rational q with |a|<q<k, a rational Mbar>=M, and integer ell with P<=k^ell. Find R with

    k^R |d| > 4 Mbar (q^(R+ell)-1)/(q-1)+1.

Such an R exists because k/q>1. It is enough to replace |d| on the left by the rational lower bound1. Then k^R consecutive copies are impossible. All comparisons and the search for R use rational arithmetic.

For at most m accessible controls, normalize p(0)=0 by translation (renormalizing the offsets too). The shortest representative argument then bounds M uniformly by

    M <= (k^m-1)+|a|(k^(m-1)-1),

since every offset is determined by positions before k^m and unit speed bounds |p(n)| by n. Thus a uniform episode bound is computable from m,k,a,P alone, without an arbitrary geometric-offset restriction.

### 13.2. Architectural limitation, not a universal ant theorem

An expanding rectangular circuit with longer and longer straight rail sweeps cannot belong to this subcritical common-scale class: each rail sweep supplies arbitrarily many copies of a fixed translating bulk word. The same applies to increasingly separated long104 free flights. An ordered-event certificate can still describe such architectures, because its affine event coordinates need not provide a common expanding recurrence in ordinary physical time.

This does not assert that arbitrary finite-seed ants have long highway episodes. It only specifies a necessary property of any counterexample found inside this automatic recurrence class: its geometric subballistic bound is uniform over all time windows, not merely from the initial pose.
