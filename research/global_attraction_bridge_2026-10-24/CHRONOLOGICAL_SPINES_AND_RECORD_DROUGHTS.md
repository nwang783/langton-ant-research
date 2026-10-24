# Chronological spines, exact reversal, and long record droughts with bounded turning

24 October 2026. Author proofs and complete finite controls; independent audit pending.

## Results first

1. A finite-seed orbit with a certified standard104 tail has exactly TWO components in its limiting last-exit forest. Both forward spines are four-edge translating zigzags with zero net turning. Every finite-cut tree still has one root. The connecting part of the finite tree escapes every fixed finite region; it cannot be retained as a fixed chronological cutset in the limit.
2. The actual 22-cell MT family has completed pristine union-record droughts with

       duration D_n = 58697+104n,
       entire interval-tree height H_n = 4n+937,
       D_n = 26 H_n +34335,

   for every integer n>=100. Every depth layer of the ENTIRE interval tree has at most39 vertices. Its maximum-height start-to-root spine has cumulative signed turning confined to[0,5], net turning3, and inward depth2n+80 below its starting north record.
3. Therefore fixed seed cardinality, bounded chronological depth-cutset width, and bounded maximum-spine turning do NOT give a uniform bound on completed record droughts. This is a quantified family of actual finite capturing orbits, not a nontranslating orbit or a counterexample to an eventual orbit-dependent bound.

The argument does not identify temporal forests with the instantaneous black diagonal graphs. The earlier gross leaf inequality remains open and is not used.

## 1. Three distinct objects and exact endpoint conventions

For a finite head path p_s,...,p_t, form the last-exit tree by assigning each visited vertex q other than p_t its last outgoing edge before t. Delete the old outgoing edge of p_t if that endpoint was visited earlier. The result is a tree rooted at p_t.

Its path from p_s to p_t is exactly the chronological loop erasure of the head path. One proof uses the last occurrence of p_s, then the last occurrence of its successor, and continues. The last-departure times strictly increase until the final root. This gives the same sequence as the usual stack algorithm, which deletes the suffix whenever the current head reappears on the stack.

The first-entry tree of the PLAIN reversed list p_t,...,p_s is exactly this last-exit tree, with each nonroot vertex pointing toward its reverse first-entry predecessor. Its first reverse appearance is immediately after its last forward departure. This is a graph identity, not a claim that the plain reversed head list is an ant trajectory.

The physical ant reversal has a one-cut endpoint shift. Write e(h) for the unit heading vector and define

       J(B,p,h) = (B, p-e(h), h+2 mod4).

Then J is an involution and J F J=F^(-1), where F is one physical ant update. A direct two-color check proves the conjugacy: the already flipped read cell lies at p-e(h), so the reverse physical turn is the complement of the original turn.

Consequently, reversing the factor[s,t] starts at

       (B_t, p_(t-1), h_t+2)

and reads p_(t-1),...,p_s. Its final head is p_s-e(h_s), not p_s, and its complete final field is B_s. Thus the physical reverse factor's head list is the reverse of the extended list

       p_s-e(h_s), p_s,...,p_(t-1).

The operation changes the checkerboard heading sector. It is not a free physical routing trick. The checker replays the full reverse factors for both named blank intervals and the entire MT100 drought, with their complete black fields, rather than merely reversing arrows in a drawing.

Along a loop-erased spine every surviving consecutive pair of edges still turns by90 degrees: the ant's invariant sector fixes the incoming and outgoing AXES at each physical cell. However that effective turn may join edges from different visits. It need not be the letter of the cell's final read. The actual cursor heading at the cut is retained separately.

## 2. A general finite quotient for a certified translating future

Suppose a finite history is followed by an exact translating head path of period P and nonzero displacement d. Let q_i,0<=i<P, be its within-period read positions. Work modulo the actual lattice subgroup Z d, not modulo a primitive direction vector when d is nonprimitive.

Choose one representative r_j for each of the finitely many cell classes, and write

       q_i = r_j + a_i d.

The physical cell r_j+k d is read at times

       N + P(k-a_i) + i

for phases i of its class with k-a_i>=0. Once k>=max a_i for that class, every phase is available. Its exact last read is then

       N + Pk + lambda_j,
       lambda_j = max_i(i-P a_i).

The maximizing phase is unique: different phase indices cannot agree modulo P. Its outgoing physical step determines a unique quotient edge

       j -> ell, with layer change delta_j.

The successor is read after that last departure, so

       P delta_j + lambda_ell - lambda_j >= 1.       (1)

Every quotient component has one directed cycle. Summing(1) around that cycle gives a strictly positive integer total layer shift m. The lift of the cycle therefore has exactly m forward rays, distinguished by layer modulo m. The finite trees feeding the cycle do not change this number.

This yields the exact number of components of the COMPLETE limiting last-exit forest:

       number of forward components = sum_cycles m.       (2)

Here the complete forest includes every cell actually visited in the finite prehistory as well as the translating future. Every cell is read only finitely often because d is nonzero. Its last-exit successor has a strictly later last-read time. Thus a successor chain has no finite cycle and cannot remain in the finite prehistory; it eventually enters one of the quotient rays. Conversely, two distinct quotient rays cannot be joined by an undirected finite path in an outdegree-one acyclic graph unless their forward successor chains eventually merge. Their distinct quotient cycle/residue labels forbid such a merger. Finite prehistory therefore cannot join or create extra components beyond(2).

The existence of a translating future is an EXPLICIT premise. This is not a finite-state test for an unknown nontranslating orbit and not a proof of global attraction.

## 3. Standard104 has two forward components, not one

For the retained canonical word W, starting with heading E and displacement(2,2), use representatives

       r=(x mod2, (x mod2)-(x-y)).

The104 read phases give22 classes. Computing the exact last-read phase in each class yields two quotient cycles:

       (0,0) -> (0,1) -> (1,1) -> (1,2) -> (0,0),

and, with the appropriate layer changes,

       (1,-1) -> (1,0) -> (0,-2) -> (0,-1) -> (1,-1).

Each cycle has total layer shift1 and physical step headings N,E,N,E. Each therefore translates by(2,2), uses four edges per layer, and has effective turn word RLRL with zero net turning. All other classes feed one of these cycles. Formula(2) gives exactly two components for EVERY finite history entering this certified standard tail, including rotated or translated copies.

The checker also starts from the literal retained13-cell canonical source and retains its complete fields. The two fixed mature vertices(12,12) and(13,12) lie on different limiting spines. In the actual finite trees at cuts1040,2080,4160, their paths meet at the current roots(20,20),(40,40),(80,80), respectively. These three controls are not an all-cut formula. The general escape of any connecting path from every fixed finite set follows from local stabilization of all last-exit edges and the two distinct limiting components.

Thus 'a translating ant has one chronological trunk at infinity' is already false for standard104. Finite one-root connectedness is not preserved under this local infinite limit.

## 4. A concrete orientation-forcing candidate and its quantified falsifier

Consider the candidate assertion:

> For fixed initial black cardinality m, fixed bound w on the sizes of all depth layers of the completed interval last-exit tree, and fixed bound a on the cumulative turning range of a maximum-height start-to-root spine, completed pristine union-record droughts have a uniform finite duration bound depending only on(m,w,a).

The actual MT family refutes this assertion with the fixed constants

       m=22, w=39, a=5.

No proposed bound is merely defeated by a larger numerical cap. The construction works for every n>=100 and its drought length tends to infinity.

The literal seed is the retained13-cell canonical K together with the four M inputs

       (202+2a,201+2a), a in{0,1,6,8},

and the five T inputs

       (2n+230+2a,2n+229+2a), a in{0,1,3,5,6}.

The signed full-field source theorem supplies the entire trajectory, including every earlier archive cell. At

       s_n=29671+104n

the head is(2n+233,2n+262), heading N, at a pristine north record. Its next union record is

       t_n=88368+208n,
       head=(-2,372), heading W.

There is no record of ANY of the four signed axes between these two cuts. All original black lifetimes have already retired at27201+104n,2470 updates before s_n. Every family member has its exact certified canonical future; no noncapturing trajectory is constructed.

The following all-parameter tree proof uses the signed actual word, not a supplied infinite strip or a cropped kernel.

## 5. Exact all-n last-parent and height proof

Put K=n-100. From s_n to t_n, the word is

       A V^(93+K) F,

where A is the final2762 reads of the T recovery, V is the104-read SW canonical word, and F is the fixed remaining100 SW reads, the actual old-M L collision, the48464-read recovery, and8098 NW-tail reads up to the first W record.

At K=0 the start is(433,462). The A read set has minimum x=392. The F read set has maximum x=240. Increasing K translates A by(2K,2K), inserts K additional SW periods of drift(-2,-2), and leaves the complete F geometry fixed. The signed source theorem ensures this is the actual word on the whole finite board for every K>=0.

### 5.1 Exact decomposition of EVERY read vertex

Normalize each SW class to a representative r with x=363 or364, according to parity, and write its phase positions as

       q_i = r + 2a_i(1,1).

There are22 classes and every a_i lies in[13,17]. A physical phase of SW period j,0<=j<=92+K, lies at layer

       ell = K-j+a_i

relative to r. Each class therefore occupies the entire integer interval

       min(a_i)-92 <= ell <= max(a_i)+K.

The phase intervals overlap because their offsets differ by at most4 while there are93+K periods.

Let U be all baseline read vertices with x>=365, and L all baseline read vertices with x<=364. The complete n-th interval read set is the DISJOINT union

       L,
       U+(2K,2K),
       { r+2k(1,1) : r is one of the22 representatives, 1<=k<=K }.

The baseline contains1153 upper and8249 lower read vertices. Thus the exact read-vertex count is

       9402+22K =22n+7202.

This accounts for the whole visited region, not only its spine.

### 5.2 Every last-parent edge is determined exactly

For an upper-cap vertex q+(2K,2K), the F cap is excluded by x. Every possible SW hit has period index a_i-ell independent of K and at most16, so no new late SW hit becomes available when K grows. The entire last-parent edge is its baseline edge translated by(2K,2K).

For a lower-cap vertex q, the A cap is excluded by x. Every SW hit has index K+a_i-ell, where a_i-ell>=13; its validity is exactly the same as at K=0. All SW and F hit times shift together by104K. Its last-parent edge is therefore exactly the baseline edge, without translation.

For a middle vertex r+2k(1,1),1<=k<=K, all phases of its SW class occur, since their period indices K-k+a_i lie between13 and K+16. Neither finite cap can hit it. Its final phase maximizes104a_i+i. This gives a22-row exact parent table

       (r,k) -> (r',k+delta), delta in{-1,0,1}.

No event ordering is inferred from a geometric Euler formula: these are the literal MAXIMUM actual read times among all three sources.

### 5.3 An exact depth potential, including boundary crossings

Let h_0(q) be the exact root distance in the baseline interval tree. The22 representative rows satisfy

       h_0(r)=1+h_0(r')+4 delta,
       h_0(r+2(1,1))=h_0(r)+4.

Define for the parameter-K tree

       h_K(q)=h_0(q),                         q in L;
       h_K(q+2K(1,1))=h_0(q)+4K,             q in U;
       h_K(r+2k(1,1))=h_0(r)+4k,             1<=k<=K.

Set the unchanged root depth to zero. The checked parent table and the second displayed identity handle both interfaces between middle layers and finite caps. Every exact last-parent edge decreases h_K by ONE. Hence this is the genuine tree depth, not a guessed distance proxy.

The baseline maximum is1337, attained uniquely at(433,462). Upper-cap depths range1037..1337; lower-cap depths are at most1040; representative depths range1033..1040. Consequently

       H_n=1337+4K=4n+937,

attained at the start head. This is the height of the ENTIRE interval tree.

### 5.4 Uniform chronological depth-cutsets

The baseline upper depth histogram has maximum8, the lower histogram has maximum25, and at most6 of the22 representative depths have any one residue modulo4. At any depth, a middle ray class contributes at most one vertex. Therefore every complete tree depth layer has at most

       8+25+6=39

vertices, uniformly in K. Such a layer is a vertex cutset in the selected last-exit TREE: each path from a deeper vertex to the root meets it. It is not asserted to cut the physical lattice or to block the ant's future moves, which may use non-tree edges.

The literal controls have maximum width25; only the proved conservative all-n bound39 is used.

## 6. The exact maximum-height spine and its turning

Let S_0 be the baseline start-to-root spine, of length1337. Its vertex at index300 is q=(365,394). The whole parameter-K spine is obtained by:

* translating the vertices S_0[0..300] by(2K,2K);
* inserting K copies of the four-edge SW zigzag

       (0,0),(-1,0),(-1,-1),(-2,-1),(-2,-2);

* following the unchanged suffix S_0[301..end].

The every-vertex last-parent proof above validates this path for all K, and its depth decreases by one at each step. It is therefore exactly the maximum-height spine, not merely a simple path in the visited set.

At the insertion interface the cumulative effective turning is2. Each inserted block has turn word RLRL, returning that value with intermediate values2 or3. The finite caps have cumulative range[0,5] and final sum3. Thus EVERY n has the same bounded turning range and the same net turning, even as its height and drought grow without bound.

The unchanged spine suffix reaches y=182, and neither translated prefix nor inserted middle goes lower. Its starting north record is y=2n+262, giving exact inward depth2n+80. Loop erasure does not remove this deep inward excursion.

The ACTUAL ant's net turn over the drought is different:

       actual R-L =12n+2627,
       actual turn minus spine turn =4(3n+656).

The actual and spine endpoint headings agree in this family, so no half-turn discrepancy is hidden in this formula. It is an exact comparison of two turn sums, not a claim that the difference counts disjoint Jordan loops or independently chargeable resources.

## 7. Controls and exact limitations

The checker replays432537 full original-seed reads: MT n100/137/500 through their next union records, the literal13-cell canonical source, and the blank source through its certified canonical cut. Every complete end board is checked against its infinite canonical continuation. Both named blank Hall intervals are checked for the plain-reverse/last-exit identity, stack loop erasure, effective turning, and physical inverse endpoint shift.

The blank prefix[0,1579] has spine length83, full tree height100, and cumulative spine-turn range[-6,1]. The signed blank interval[5710,6042] has spine length4 but full tree height83 and actual net turn20. These controls prevent substituting a short loop-erased path for the whole visited-region tree.

The universal statements proved here concern certified translators and the exact all-n MT family. They do not show that a hypothetical nontranslator has a well-defined limiting last-exit forest, one or two ends, unbounded turning, or any particular cutset geometry. A nontranslator might revisit cells infinitely often, so some last-exit edges might not stabilize at all.

The long-drought countercontrol refutes only a UNIFORM bound depending on fixed seed cardinality, tree-layer width, and spine turning. It does not refute eventual orbit-dependent bounded age, eventual record-clock boundedness, or compact recurrence in one orbit. All members capture. The missing global occurrence theorem and arbitrary translating-tail104 classification remain separate obligations.
