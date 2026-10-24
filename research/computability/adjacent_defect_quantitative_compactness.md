# Computable adjacent-defect response bounds from the new language theorem

22 October 2026. Status: Sections 1–4 passed independent analytic audit on 22 October 2026. The dependency is the independently audited theorem in ../word_stabilization/adjacent_defect_highway_theorem.md and its SHA manifest. No global finiteness of adjacent defects is asserted.

We use the unique reversible two-sided physical history, so all preceding windows exist. Equivalently, in a one-sided word restrict the same-interval statements to ending times t>=10. Write J(t) for the forbidden length10 flag ENDING at read time t, and K(t)=J(t-1)J(t). The dependency says, on every finite-support orbit:

- finitely many future K events iff eventual standard104 capture;
- if K(t)=0 for every t>=T, then J(t)=0 for every t>=T.

The bounded-first-L tree in bounded_mass_compactness.md turns these qualitative implications into total computable, mass-dependent finite response bounds.

## 1. Every isolated bad window has a uniformly bounded future adjacent pair

There exists a total computable function D(m) with this property:

    If J(u)=1, K(u)=0, and the board immediately AFTER read/move u
    has at most m black cells, then K(v)=1 for some
    u < v <= u+D(m).

This quantifies over every placement of the black cells and every head pose.

Proof and algorithm: rewind11 ordinary steps from that checkpoint. The resulting finite board has at most M=m+11 black cells. Index its forthcoming reads0,1,..., so the given event is at10, with J(9)=0,J(10)=1.

Construct the binary prefix tree of legal words with at most M first-L cells. For words of length at least11, require that initial J-pattern 01, and require K(t)=0 for every10<=t<word_length. Prefixes shorter than11 are retained when legal. This is a decidable, finitely branching, prefix-closed tree.

An infinite branch would be the exact orbit of a finite seed with at most M black cells. It would satisfy K(t)=0 for every t>=10 while J(10)=1, contradicting the stronger language corollary. Therefore the tree is finite. Exhaust breadth levels until some empty level N>=12 is reached, and set D(m)=N-11. A physical history avoiding adjacent pairs for D(m) further moves would yield a forbidden node at level N. QED.

This is an effective bound because the complete level search is proved to terminate for every m. The tree algorithm itself is not a practical numerical calculation. A separate explicit LINEAR bound D(m)=10404m+2829858755 has now been derived in ../word_stabilization/linear_isolated_defect_response_bound.md; this compactness argument does not need those constants. The mass bound is measured at the specified event, not at an arbitrary distant initialization.

## 2. Bounded adjacent-defect count forces a uniformly early standard episode

There is a total computable function T(m,r,q), for m,r>=0 and q>=1, such that every ant prefix of length T(m,r,q), starting from at most m black cells, contains EITHER

1. q consecutive copies of a cyclic phase of the standard104 word; OR
2. at least r+1 adjacent-pair events whose full11-letter windows lie inside that prefix.

Construct the tree of legal words with at most m first-L cells, at most r adjacent-pair events, and no target standard episode. It is computable and prefix closed. An infinite branch would be a finite-seed orbit with at most r adjacent pairs in its entire future, hence eventually standard by the new theorem, contradicting target avoidance. Therefore the tree is finite. Its first empty breadth level defines T.

Equivalently, ALL seeds of mass<=m whose entire future has at most r adjacent pairs exhibit the target episode by this uniform time. The finite-prefix dichotomy is stronger as an operational statement because no infinite-future promise is needed to apply it.

If a proposed orbit avoids a fixed standard power forever, its adjacent-pair count must therefore diverge with an explicit computable lower-bound schedule obtained by inverting r -> T(m,r,q). This is not a positive-density bound: T may grow very quickly. It does not prove adjacent-pair finiteness on arbitrary inputs.

## 3. Primitive geometric substitutions need positive adjacent-defect density

Consider the earlier uniform two-letter geometric substitution phi(R)=u, phi(L)=v, with common length k>1, u prolongable on R, and an expanding scalar a. Each macro restores the corresponding coarse quarter-turn heading, has opposite displacement a,-a, and |a|>1. These are the exact assumptions in selfsimilar_visit_certificates.md.

Both u and v contain both letters. A monochromatic quarter-turn macro has odd length and displacement of norm1, contradicting |a|>1. Thus the two-letter substitution is primitive in the strong one-step sense.

Any valid finite-seed fixed point in this class has at least one length11 factor z giving an adjacent bad pair. Otherwise the language theorem would make it standard eventually, contradicting its geometric endpoints p(k^n)=a^n and |a|<k. The strict inequality follows because equality in the k-step length bound would require all unit moves aligned, incompatible with successive quarter turns.

Choose s with z occurring in phi^s(R). Since phi(c) contains R for both letters c, every block phi^(s+1)(c) contains z. Let L=k^(s+1). Every aligned length-L block of the fixed point therefore contains an adjacent-pair event. The lower asymptotic density of such events is at least1/L.

This is a restricted but useful architectural constraint: a valid counterexample in this primitive self-similar class cannot consist merely of isolated increasingly rare adjacent defects separated by longer and longer standard stretches. It must sustain adjacent defects at positive lower density. No such candidate has been found. General finite-seed orbits need not have this recurrence property, so no unrestricted density conclusion follows.

## 4. Existence of a future adjacent pair is decidable on EVERY finite seed

The new theorem gives a concrete all-input decision result, without assuming HC:

    Given a finite complete state X, decide whether ANY future K event occurs.

Run literal simulation, checking the actual local K predicate with the finite inverse history when necessary. In parallel at each checkpoint, test all cyclic standard104 tails with the exact finite-field ray verifier. There are two ways to stop:

- If a K event is seen, answer YES and return its first occurrence.
- If an exact standard tail is certified, inspect the next10 updates as well to cover the finite windows straddling its onset. If these and the already simulated prefix contain no K, answer 

The second answer is sound because every subsequent ten-window lies wholly inside the certified standard tail. The procedure is total: if there is a K, finite simulation reaches it (or the exact tail check resolves the preceding finite boundary); if there is no K, the new language theorem guarantees standard capture, so eventually an exact tail certificate is found. No finite-repeat heuristic is used.

The stronger corollary also gives the set equality

    {X: some future J occurs} = {X: some future K occurs},

with the same chosen starting time and true inverse-history convention. The inclusion from right to left is immediate; a J at t has a K at or after t. Thus the existing finite-input J reachability decider can alternatively be reused. Its reported quantitative complexity is not needed for the totality proof here.

### 4.1. A total adjacent-pair renewal map

Define R_K(X) to be a designated terminal symbol when there is no future K. Otherwise, simulate to the first future K event and return the complete state immediately AFTER that read/move. The next invocation starts with the next physical read, so no event is counted twice. The preceding decision result makes R_K a TOTAL computable map, even though the first physical event can be very far away.

Iterating R_K terminates exactly when the orbit has finitely many K events, equivalently when it captures standard104. Hence HC is equivalent to termination of all iterates of this total map on finite states. This is an exact reduction to a termination problem, not a solution to that termination problem.

For every finite q, the predicate “at least q future adjacent pairs occur” is decidable by at most q iterations of R_K, stopping if the terminal symbol appears. Consequently no HALT many-one reduction can use the occurrence of one adjacent pair, or any supplied FINITE number of adjacent pairs, as its accepting condition. Infinitely many pairs remains the genuinely infinitary unresolved condition. This distinction is valid even if HC is false.


### Boundary conventions for the renewal map

The renewed state must retain its last ten true turns, or reconstruct them by the inverse ant map. Restarting a detector with an empty history could miss overlapping adjacent pairs. A physical finite state determines its entire inverse history, so no extra nonphysical input is required.

If instead “future” only counts windows wholly contained in a newly started one-sided stream, the exact equivalence is:

    future K exists from X iff future J exists from F(X).

Every such K has its right-hand J starting at index at least one. Conversely, any J starting at index at least one has its preceding window present, so the same-interval language corollary forces a subsequent K. Without this one-step shift, the first ten-letter window can be the lone final defect. The direct dovetail-plus-ten-read decision proof above remains valid with either consistently specified convention.

The inherited source factor_language/proof/ten.md contains a polynomial-bit future-J decision theorem. Its constants and complexity have not been newly independently audited here, so the independently established claim in this note is total computability, not a new polynomial complexity theorem.

## 5. An explicit elementary episode/defect dichotomy

Status: the recurrence independently passed analytic audit. The linear replacement uses the independently audited constants from ../word_stabilization/linear_isolated_defect_response_bound.md, not an unbounded tree search.

Let N=270902 and, for nonnegative integer x, define

    H(x) = 300 + 89(x+100) + 15 = 89x+9215,
    T24(x) = 12x + 400,
    F(x) = x + H(x) + T24(x) = 102x+9615.

For q>=1 put

    O(q) = N + 104q + 1000,
    S(M,q) = F(F(M+O(q))).

**Segment lemma.** A legal finite word, entered with at most M black cells, containing no adjacent-pair11 factor and no q consecutive standard104 periods has length at most S(M,q)-M.

For words shorter than149 this is immediate. Otherwise their length149 histories trace the audited no-K graph. Its condensation DAG allows at most one visit to each of H, T24, and W104. The H and T24 visits cost at most H(x) and T24(x) when entered with mass x, including their alignment fringes, by the cited response proof. Inside W104 all successive read letters follow the standard cycle. Avoidance of a104q-letter standard episode bounds this visit by104q+148 edges, a deliberately loose bound. All remaining vertices are transient and occur at most once. Initial history, connecting edges, and the W visit together cost at most O(q).

Charge all those ordinary steps at the start, raising the available mass bound from M to x=M+O(q). At most two exceptional H/T24 visits remain, in either order. Monotonicity lets the first raise the mass/time envelope from x to at most F(x), and the second to at most F(F(x)). Consequently total duration is at most

    O(q) + (F(x)-x) + (F(F(x))-F(x))
      = S(M,q)-M.

Now define M_0=m and iterate

    M_(i+1) = S(M_i,q)+1,  0<=i<=r.

Then a valid explicit choice for the Section2 dichotomy is

    T_explicit(m,r,q) = M_(r+1)-m.

Indeed, split a target-avoiding prefix at each of its at most r wholly-contained adjacent-pair right-end read positions. The removed read letters are at most r separators, and the remaining at most r+1 subwords have no wholly-contained adjacent-pair factor. Apply the segment lemma successively. Each separator adds at most one to time and black mass. Padding to r+1 blocks, the total prefix length is at most M_(r+1)-m-1. Thus a prefix of length T_explicit cannot avoid both alternatives.

The new linear F makes this a fixed-height ELEMENTARY function, not merely
primitive recursive. More explicitly, with

    a=10404,
    b(q)=10404*O(q)+990345+1,

one has M_(i+1)=a*M_i+b(q), hence

    T_explicit(m,r,q)
      = (a^(r+1)-1)*m + b(q)*(a^(r+1)-1)/(a-1).

The quotient is an integer geometric sum. Thus the bound is exponential in
r and linear in m and q at each fixed r. Neither this formula nor the
qualitative dichotomy bounds r globally or bounds permanent capture time
from initial mass.
