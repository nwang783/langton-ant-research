# Exact aperiodic ants on computable infinite backgrounds

Status, 22 October 2026 at21:33 UTC: complete finite-carry certificates for both displayed substitutions passed a full independent no-import replay. The checker rebuilt the joint controls, compared 8,192 literal poses per pair, and independently exhausted both carry closures. See audits/check_cyclic_root_alternation_independent.py/json. The general phase-permuted equality construction has passed analytic audit. This is a positive inverse-certificate control on **infinite initial black sets**, not a finite-support counterexample, a universality construction, or a reduction from halting.

## 1. Two explicit root-cycling substitutions

For each row define phi(R)=u and phi(L)=v:

| u | v | Gaussian scale a |
|---|---|---|
| LRLRLRRLRLRLRLRRL | RLRRLRRLRLRLRLRLR | 3+6i |
| LRLRLRLRLRLRRLRRL | RLRRLRLRLRLRRLRLR | -3+6i |

Both words have length17. Starting north, u ends east at a, while v ends west at -a. Their first letters swap R and L. Thus psi=phi squared is prolongable on each letter; write w_R and w_L for its two fixed infinite words. The substitution phi swaps these two words.

Let P_c(n) and h_c(n) be the read position and entering heading at index n of w_c, starting at the origin facing north. Quarter-turn headings are0=N,1=E,2=S,3=W. Exact word concatenation gives

    P_R(17n+j) = a P_L(n) + rot_(h_L(n)) p_(w_L(n))(j),
    P_L(17n+j) = a P_R(n) + rot_(h_R(n)) p_(w_R(n))(j),

where p_b(j) is the jth read offset in phi(b) from a north-facing origin. The simultaneous heading/letter control

    S(n)=(h_R(n),w_R(n),h_L(n),w_L(n))

has20 reachable states for each displayed pair. Its digit transition follows directly from the literal image words. The zero state is stable under a leading zero; both phase offsets at digit zero vanish there. The helper cyclic_root_geometry.py constructs this recurrence and independently compares it with1,200 literal position/turn values per pair.

## 2. Finite certificate for all-time alternation

Compare two equally padded base17 numerals s<t. Track the two control states, a selected curve phase c, their position difference D, and a flag saying whether strict numeric order has already occurred. The selected phase toggles on every digit because the phase permutation is the fixed swap. The two tracks use the same selected phase: equal-length numerals ending in the same root necessarily have the same starting phase. Start both possible phases at D=0.

At digits d,e the update is

    c' = 1-c,
    D' = a D + offset(S_s,d,c') - offset(S_t,e,c').

Before strict order occurs reject d>e. After it occurs, every digit pair is allowed. A bad state would have strict order, D=0, and equal turn outputs in the selected final phase.

For a bound M on the norm of any offset difference, choose integer R with

    (|a|-1) R >= M.

If |D|>R, every later update has strictly greater norm, so it cannot reach zero. Discarding these transitions is sound. The implementation uses twice the ceiling of the maximum individual offset norm for M, and checks the displayed radius inequality with integer squares. All surviving states lie in a finite Gaussian disk.

The complete reachable closures contain no bad state:

| scale | radius | states | checked edges | discarded expanding edges |
|---|---:|---:|---:|---:|
| 3+6i |3|6488|1869592|1834672|
| -3+6i |4|11308|3262572|3207044|

The state lists and hashes are stored in cyclic_root_alternation_certificate.json. Replaying a closure requires only checking the two starts, all in-radius successors, and absence of a bad state; no first-order automata package or solver is needed.

Consequently, for either root of either substitution, **any two reads of the same cell have opposite turns**. In particular, a cell is read at most twice, since three binary turns would contain an equal pair. Consecutive visits therefore alternate.

Define B_c to consist of exactly those cells whose first read in w_c is L. Induction on time now proves that the ordinary R-white/L-black flip-and-move ant on B_c follows w_c forever. Cells never visited may be set white.

## 3. The background is computable, but necessarily infinite

For a given lattice cell z, its hit language is decidable by the same finite-carry construction, now comparing P_c(n) with P_c(0)+z and accepting difference z. Choose a radius containing z as well as satisfying the expanding bound. Overflow can never return to z. Finite-state reachability decides whether z is visited; if so, a finite accepted numeral gives a witness time. Simulate through that time to find its first visit and initial color. Thus membership in B_c is a total computable predicate.

The earlier independently checked squared-image sublattice argument proves that B_c is infinite. Set A=a squared=-27+36i or -27-36i. Every internal read offset of both length289 psi images avoids the sublattice A Z[i]. Therefore a nonzero first-L coarse cell scales to another first-L cell at every refinement:

- For the R root, index1 is first-L at cell1, yielding times289^j and cells A^j.
- For the L root, index2 is first-L at cell -1+i, yielding times2*289^j and cells A^j(-1+i).

These cells are all distinct because |A|=45>1. See complementary_survivor_independent_checks.json and the causal analysis's complementary_root_exclusion.md. This is an exact obstruction to finite support, not an inference from a large observed black count.

## 4. These are genuinely aperiodic turn streams

Bounded digit offsets imply an origin growth bound

    |P_c(n)| = O(n^alpha), alpha=log(sqrt(45))/log(17)<1.

On the other hand, P_c(289^j)=A^j P_c(1), so each path is unbounded. An eventually periodic relative turn stream produces either a bounded path or nonzero linear drift: non-restoring heading periods cancel after finitely many repetitions, while heading-restoring periods have fixed displacement. Hence these unbounded sublinear paths cannot have any eventually periodic turn tail.

This supplies actual aperiodic behavior for the classical rule on computable infinite backgrounds. It does not resolve whether any finite background can behave aperiodically, and it does not manufacture a reusable circuit or undecidable finite-input problem.

## Artifacts

- phase_permuted_certificates.md: analytically audited general multi-phase carry theorem.
- cyclic_root_geometry.py and cyclic_root_geometry_controls.json: the exact20-state adapters and literal controls.
- check_cyclic_root_alternation.py and cyclic_root_alternation_certificate.json: complete finite closures with hashes and every state.
- complementary_survivor_independent_checks.json: earlier independent1152-offset sublattice checks and nonzero first-L seeds.
