# Global-constraint work, 22 October 2026

## Status

The highway conjecture is not proved here. The recovered computer-assisted theorem that every finite-seed orbit is eventually at mass at least five survives the analytic audit below. A separate analysis has replayed and audited its finite/all-parameter certificates. This note also records new analytic restrictions on any hypothetical recurrence at mass five; those restrictions do not by themselves exclude recurrence.

## 1. Audit of the recovered eventual-mass-five theorem

Primary recovered proof: `continuation_2026-10-22/ant_continuation2/chronology/eventual_mass_five.md`.

I independently checked the following logical steps.

1. The checkerboard/heading sector is invariant. The displayed axial correction tables change by exactly the signed flipped-cell contribution modulo four. Summing the per-line modular distances gives the sharp incoming-edge-midpoint inequality `|B_s XOR B_t| >= 2 ||m_t-m_s||_infinity`.
2. An interval omitting one critical-clock increment has at most one diagonal-direction sign change. Before its first repeated read it consists of two staircases. A return after the sign change has opposite incoming heading and would require the same turn as its earlier read, contradicting the intervening flip. Thus all its reads are distinct. Its number of right turns exceeds its left turns by at most three. From current mass K its length is at most `2K+3`, proving the `2K+4` forcing bound.
3. Infinitely many mass-at-most-K times have heads in one fixed box. Disjoint fixed-length forcing blocks then give uniformly positive gains to each nondecreasing critical clock, so all four diverge. The fixed-box condition is essential; it is not asserted for arbitrary fleeing orbits.
4. At recurrent mass four the two positive z-coefficient cells must tend to opposite z infinities, and the other two to opposite u infinities. All four escape every fixed finite set. The first far blank-tail collision is therefore the negative-z positive-coefficient cell.
5. Its remote row and column have zero signed charge and contain exactly two opposite-parity cells each. The two axial gaps have the same sign. A negative-gap subsequence would leave the positive-z fourth cell unable to use a positive remote coordinate without creating a singly occupied remote line. Thus both gaps tend positive. This correctly excludes U-shapes pointing southwest without prematurely assuming a rectangle.
6. At the second collision the row of the northwest collider becomes remote only after its tail interception is known. This forces the fourth cell onto that row. The ordinary-channel half-plane and horizontal-axis guards then exclude the complete XOR archive and both remaining initial cells. The exceptional phase forces the displayed northwest corner.
7. At the third collision the analogous argument makes the southeast collider's column remote, forces the northeast corner, and excludes ordinary phases using the correctly rotated vertical-axis bound. The exceptional phase fixes the full one-parameter rectangle.
8. The parameter tends to infinity, so the all-parameter certificate for n>=200 suffices. A permanent standard word has mass gain 12 per 104 turns, including any untouched debris. It contradicts infinitely many later mass-four times.

No analytic gap was found. This is not a proof-assistant formalization, nor an assertion of publication priority. The certificate audit is separately recorded in `audit.md`.

Independent executable control: `audits/global_constraints_independent.py`. It imports no recovered ant code. It passed 392 exact local cases and all legal increment-avoiding symbolic color trees for K=0,...,20, all headings, and all four increment types: 20,064 symbolic nodes. These finite checks support, but do not replace, the above unrestricted proofs.

## 2. A two-sided minimum lemma for sparse recurrent checkpoints

Let `K = liminf_{t->infinity} |B_t|` be finite. Choose times `t_j -> infinity` with mass exactly K, a fixed head pose, and locally convergent fields `B_{t_j} -> C`. The established clock/local-limit lemma gives `|C| <= K-4`.

**Lemma.** On the complete two-sided orbit through `(C,p,h)`, time zero is a global mass minimum:

`|F^r(C,p,h).black| >= |C|` for every integer r.

**Proof.** The ant update is invertible and both it and its inverse depend on finitely many cells over any fixed finite number of updates. For fixed integer r, sufficiently late checkpoint states and C therefore have identical reads and flips between offsets 0 and r, in the appropriate time direction. Their mass changes agree exactly:

`|B_{t_j+r}| - K = |C_r| - |C|`.

Since integer-valued mass has liminf K, it is at least K after some fixed time. Taking j large proves the inequality. This argument treats negative r as well because t_j+r remains positive for large j. QED.

The inverse can be written explicitly. From `(B,p,h)`, put `q=p-d_h`, read its current bit c, replace B by `B XOR {q}`, and replace the heading by `h+1` if c=0 or `h-1` if c=1, modulo four. This is the earlier incoming heading.

This lemma does not prove capture. In particular, many one-black inputs can be global mass-minimum states. It only excludes using a local limiting core whose own finite past or future reaches smaller mass.

## 3. New first-collider polarity lemma at mass at most five

This is an analytic extension of the mass-four first-contact reduction. No scattering computation is used in its proof.

### Assumptions and notation

Consider a sequence of complete checkpoints from one actual finite-seed orbit. Their head poses lie in a fixed box, their masses are at most five, and all four critical clocks diverge. Suppose a distinguished black cell q on each checkpoint satisfies

- `q_x -> -infinity`, `q_y -> -infinity`;
- `u(q)=q_x-q_y` stays bounded.

This is exactly the geometry of a first remote contact with a fixed southwest standard parent tail. The parent may be the blank orbit or any other already-certified finite-seed parent. Fix D containing the original seed and all checkpoint heads. Every row and column outside `[-D,D]` has signed black sum zero modulo four at the checkpoints.

Let `b(w)=-sigma*(-1)^(w_x+w_y)`. Positive z-clock field terms have b=+1; positive u-clock field terms have b=-1.

**Lemma.** For all sufficiently late checkpoints, `b(q)=+1`.

### Proof

Assume a subsequence has b(q)=-1. Since u(q) stays bounded, divergence of both u clocks requires two *other* b=-1 cells with u tending respectively to positive and negative infinity. Divergence of the two z clocks also requires at least two b=+1 cells. The total mass limit five forces exactly five cells: q plus two other b=-1 cells d,e and two b=+1 cells a,c. The latter have z tending to opposite infinities, while d,e have u tending to opposite infinities.

The remote row of q has even occupancy. It cannot have four cells. A zero-charge four-cell row would have two cells of each sign (four of one sign is impossible with this 3/2 population split). The sole off-row cell would then have b=-1, the same sign as q. The remote column of q would contain either q alone or q and that same-sign cell, giving nonzero charge. Thus the row contains exactly two cells, of opposite signs. The same reasoning applies to q's column.

Write q=(l,b0), a=(l,t), c=(r,b0), where a,c have b=+1. The two remaining cells d,e have b=-1. Neither can lie on q's row or column: one additional cell gives odd charge; both give a four-cell line with sign imbalance two.

Any remote y-coordinate of d or e must consequently equal t, and at most one can have that coordinate; otherwise its row is either unpaired, contains two same-sign cells, or contains three cells. Any remote x-coordinate similarly must equal r, with at most one of d,e there. Both d and e escape every bounded set by their opposite-u divergence. Therefore, after relabeling,

`d=(s,t), e=(r,v), with s,v in [-D,D]`.

The complete z,+ field sum is now

`3^(l+t) + 3^(r+b0) - 3^(l+b0) - 3^(s+t) - 3^(r+v)`

`= 3^t (3^l-3^s) + 3^r (3^b0-3^v) - 3^(l+b0)`.

Since l,b0 are eventually below -D while s,v stay in `[-D,D]`, every displayed term is strictly negative. The head correction is uniformly bounded. The z,+ clock cannot diverge to positive infinity, a contradiction. QED.

### Consequence and limitation

At a hypothetical mass-five recurrence, the local limiting core has at most one black cell. If its eventual standard tail is invoked with a valid certificate, the first distant collision still lies in the favorable parity class. After placing phase zero consistently, this restricts the first contact to the same ten even frontier phases used in the mass-four proof, rather than all twenty-two fresh phases.

This does **not** justify applying a clean one-bit scattering table to the whole actual future: an additional fifth cell can lie on an outgoing ray, and a second collision can revisit the complete old history. The favorable-polarity result is a coverage reduction, not an eventual-mass-six theorem.

## 4. Progress of the original work plan

The five-cell axial geometry and ordinary-channel exclusions requested at the first checkpoint are completed in Sections 5–9. The remaining sparse recurrence obstruction is a retained one-black local core inside the diagonal cross. Sections 10–11 explain why this method does not automatically become a global mass induction. Current next targets and pending checks are recorded at the end of this note.

## 5. Stronger five-cell southwest exposure lemma

**Status: independently reviewed analytic lemma.** Keep Section 3's hypotheses. Then eventually q is favorable (`b(q)=+1`), its remote row and column each contain exactly one other black cell,

`a=(l,t), c=(r,b0), q=(l,b0)`,

with b(a)=b(c)=-1, and

`t-b0 -> +infinity, r-l -> +infinity`.

Every other black cell w, apart from q,a,c, satisfies

`z(w)-z(q) -> +infinity`.

The proof below is by finite limiting shape classification, not a simulation.

### 5.1 Subsequence normalization and the incidence graph

To prove an eventual/asymptotic statement, suppose it fails along a subsequence. As there are at most five cells, pass to a further subsequence with constant mass, fixed cell labels, fixed b signs, fixed coordinate equality pattern, and each coordinate either constant or tending to one signed infinity. Enlarge the fixed box [-D,D] to contain every constant coordinate. This preserves the zero-charge assertion for all remote lines.

Form the bipartite incidence graph whose vertices are occupied x-coordinates and y-coordinates, with one edge for each black cell. A coordinate vertex is **anchored** if its value is constant; otherwise it is remote. At a remote vertex, the sum of the incident b signs is zero modulo four. (Multiplying a signed row/column charge by a fixed sign converts it to this sum.) Hence its degree is two or four, or zero.

Section 3 has already proved b(q)=+1. Both b classes have at least two cells because both opposite clocks of each class diverge.

No remote vertex has degree four. Indeed, if a remote row had four edges and q were not on that row, q would be the sole off-row edge, leaving q's own remote row of degree one. Thus q is on the four-edge row. Its charge must have two signs of each kind, since neither sign class has four cells. The sole off-row edge must be b=-1 and share q's column, in order to cancel q on that remote column. The only other b=+1 edge is therefore on q's row. The z,+ clock requires its x-coordinate to tend to positive infinity, since q itself has z tending negative infinity. That remote column has no partner: the off-row edge is on q's different, negative-diverging column. Contradiction. The column case is identical.

All remote vertices consequently have degree two, and their incident edges have opposite b signs. Cut the incidence graph at every anchored vertex. The resulting strands have anchored endpoints and alternating edge signs, or are cycles composed entirely of remote vertices. The strand containing q has q as an internal edge because both its coordinates are remote. With at most five total edges, it is a path of length 3, 4 or 5, or a four-cycle. Any other one-edge strand is a bounded cell. A remaining two-edge strand has one remote coordinate and two bounded endpoint coordinates. These exhaust the possibilities; a simple bipartite cycle has length at least four.

For the formulas below, use `A=3^l`, `B=3^b0`, both tending to zero. Anchor-coordinate powers are positive and uniformly bounded above and away from zero.

### 5.2 Three-edge q strand

The strand is `{(l,t),(l,b0),(r,b0)}`, with t,r anchored and signs `-,+,-`. Thus a and c have north/east gaps tending to infinity. Its z,+ contribution is

`3^(l+b0)-3^(l+t)-3^(r+b0)`,

which is bounded and tends to zero. To make the full z,+ field diverge, the at most two remaining cells must form a two-edge strand on a positive-diverging remote row or column. A negative-diverging common coordinate would make that strand's z,+ contribution tend to zero. Both of its cells therefore lie northeast of q, and their z difference from q tends to infinity. Remaining bounded cells alone cannot supply the divergent clock.

### 5.3 Four-edge q strand

Up to interchanging x and y, its cells are

`a=(l,t), q=(l,b0), c=(r,b0), d=(r,v)`,

with t,v anchored and signs `-,+,-,+`. Any fifth cell is bounded. The strand's z,+ contribution is

`3^l(3^b0-3^t) + 3^r(3^v-3^b0)`.

The first term is negative and tends to zero; the second can diverge positively only if r tends to positive infinity. Thus both axial partner gaps tend positive infinity, and d and any bounded fifth cell have z difference from q tending positive infinity. The transposed case is identical.

### 5.4 Four-cycle

The cycle is q,a,c,d=(r,t), with signs `+,-,-,+`, and any fifth cell is bounded. The only negative-sign cells are a,c (or those two plus one bounded cell). Divergence of the two u clocks forces their u-values to opposite infinities. Since u(q) is bounded, H=t-b0 and J=r-l tend to the same signed infinity. If both tended negative infinity, all four cycle coordinates would tend negative infinity and its z,+ field contribution could not diverge; the bounded fifth cell cannot repair this. Hence H,J both tend positive infinity. For d, `z(d)-z(q)=H+J` tends positive infinity.

### 5.5 Five-edge q strand, q in its middle

Write the five cells, in path order, as

`d=(s,t), a=(l,t), q=(l,b0), c=(r,b0), e=(r,v)`,

with s,v anchored and signs `+,-,+,-,+`. The only negative-sign cells are a,c, so their u-values must tend to opposite infinities. The wrong assignment `u(a)->+infinity, u(c)->-infinity` forces t,r both to negative infinity. Then all positive z terms, at q,d,e, tend to zero, contradicting z,+ divergence. The other assignment gives H,J tending positive infinity. Both d and e have one anchored coordinate strictly above the corresponding coordinate of q and the other differing by H or J, so their z differences tend to positive infinity.

### 5.6 Five-edge q strand, q next to an end

Up to transposing coordinates and reversing the path, write the cells as

`a=(l,t), q=(l,b0), c=(r,b0), d=(r,v), e=(s,v)`,

with t,s anchored and signs `-,+,-,+,-`. Its z,+ contribution has two useful forms:

`3^l(3^b0-3^t) + 3^v(3^r-3^s) - 3^(r+b0)`,

and

`3^l(3^b0-3^t) + 3^r(3^v-3^b0) - 3^(s+v)`.

The first term in each form is negative eventually, since b0 tends negative infinity and t is anchored. Positive divergence of the whole expression forces r>s and v>b0 eventually. Since r is an internal remote coordinate, r tends positive infinity; in particular J tends positive infinity. H tends positive infinity because t is anchored. The cells d,e have x-coordinate respectively r or anchored s, both differing positively without bound from l, and y-coordinate v>b0. Their z differences from q therefore tend positive infinity. The transposed case proves the other off-center position.

These exhaustive limiting shapes prove the stated exposure lemma. No conclusion is drawn about reachability of arbitrary endpoint graphs; their role is only to contain every hypothetical recurrent sequence.

## 6. Consequence for the first scattering at recurrent mass five

Assume the already-known one-black capture theorem with exact standard-word identification. A hypothetical sequence of recurrent mass-five checkpoints has, after fixing the pose and taking a local limit, a fixed core C with at most one black cell. Its future is eventually a standard highway. Rotate coordinates so its drift is southwest and retain the corresponding sigma in the clock definitions.

The actual checkpoint future must eventually read an extra initial bit; otherwise it agrees forever with the parent C and its mass grows unboundedly. The first extra-bit collision q lies arbitrarily far along the fixed parent tail, so Sections 3 and 5 apply. The favorable parity gives one of the ten even fresh phases. Its two axial partners are arbitrarily far north/east, and every other checkpoint bit has z distance above q tending to infinity.

At the parent's fixed tail-entry state, compare its complete board to the placed, phase-correct thirteen-black standard core. The finite XOR archive H is fixed and misses the entire incoming standard trace. Advancing both boards to the far collision preserves exactly that archive. For any of the nine ordinary favorable phases, the audited canonical all-future read bounds are

- `z(w) <= z(q)+58`;
- horizontal axis through q: distance at most 31;
- vertical axis through q: distance at most 34.

They miss H for sufficiently distant q, miss a,c by their diverging axial gaps, and miss all remaining extra bits by the exposure lemma. Complete-field coupling gives a permanent standard future, contradicting recurrent mass five.

**Therefore only the exceptional phase-72 first collision can occur along a sufficiently late recurrent mass-five subsequence.** This is a new necessary condition, not an exclusion of that subsequence. The exceptional return may interact with an arbitrary fixed one-black parent's complete historical field. The blank-parent two-stage templates used to exclude mass four do not automatically cover that return.

## 7. Uniform two-diagonal-strip geometry for the exceptional parents

**Exact checked consequence of the already-audited affine-word certificates.** For every n>=200, every read of each of the three blank-background parents

1. `{q_n}`;
2. `{q_n,a_n}`;
3. `{q_n,a_n,c_n}`

belongs to

`D_82 = {w: |x(w)+y(w)|<=82 or |x(w)-y(w)|<=82}`.

Here q_n,a_n,c_n are the coordinates in the recovered mass-five proof. This includes each entire finite prefix and its permanent standard tail.

The new checker `audits/check_exceptional_diagonal_strips.py` independently traces the certified words symbolically. Every finite read is an affine point in n; at least one diagonal normal has zero n coefficient and absolute constant at most 82. For every repeated or infinite period, one normal has zero coefficients in both n and the period epoch. It checks 197,496 read identities. The respective outgoing infinite-tail bounds are 17,15,45, while the common full-prefix bound is 82. It never extrapolates from parameter samples. Color validity is the separate, previously audited affine parity certificate; the three-bit parent follows because the unused northeast fourth corner is certified never read.

The scattering analysis independently checked the same all-parameter statement with a coarser single-normal-per-whole-segment bound 93. Thus either bound can be used for the asymptotic application below.

In particular, a cell with one bounded coordinate and the other tending to signed infinity is eventually outside D_82 and cannot affect any of these three parents.

## 8. Further consequence: recurrent mass five cannot have blank local limit

**Status: independently reviewed analytic derivation using Sections 3,5,7 and the recovered complete-field guards.**

Suppose a fixed-pose subsequence of mass-five checkpoints converges locally to the empty board. All five checkpoint cells then escape every fixed bounded set. The blank-parent special case of Section 6 forces the first collision to be q_n, n->infinity. This special case uses only the audited blank certificate and ordinary collision guards, not the general one-black capture theorem. The incidence-strand classification of Section 5 leaves only:

- a three-edge q strand plus a separate two-edge strand;
- a five-edge q strand, q in the middle;
- a five-edge q strand, q adjacent to one end.

A four-edge q strand or a four-cycle would leave the fifth cell bounded, contrary to the blank local limit.

### 8.1 Three-edge plus two-edge case

The four cells other than q all have one anchored coordinate and one remote coordinate: the two axial partners and both cells of the remaining two-edge strand. They are eventually outside D_82. The one-bit parent `{q_n}` therefore reads none of them, so the actual future is already standard. Contradiction.

### 8.2 Five-edge path with q in the middle

Use the coordinates from Section 5.5:

`d=(s,t), a=(l,t), q=(l,b0), c=(r,b0), e=(r,v)`,

where s,v are anchored. The extra cells d,e are outside D_82, throughout all three parent comparisons below. The one-bit parent has entire future `u<=58,z<=39`, and its prefix through its fixed northwest stage has `u>=-82`. Since u(c)->+infinity and u(a)->-infinity, the next collision must be a, far along the northwest tail; otherwise the actual future is already standard.

That hit makes z(a) bounded, so t->+infinity. In an ordinary phase its complete post-impact read set has `u<=u(a)+58`. This misses H1 because H1 has u>=-82; misses c; misses d because `u(d)-u(a)=s-l->+infinity`; and misses e because `u(e)-u(a)=(r-l)+(t-v)->+infinity`. Thus the second phase must be exceptional, forcing a=a_n.

Now the two-bit parent misses d,e by D_82 and misses c through its fixed southeast stage by the prefix bound u<=98. The next collision must be c on its southeast tail; otherwise capture is permanent. For an ordinary phase, every future read has `u>=u(c)-58`; this misses H2 (u<=98), d (u->-infinity), and e because `u(c)-u(e)=v-b0->+infinity`. Consequently c must be exceptional, forcing c=c_n.

The three-bit parent `{q_n,a_n,c_n}` is permanently standard and stays in D_82. It misses d,e, yielding the contradiction.

### 8.3 Five-edge path, first orientation next to an end

Use Section 5.6's coordinates:

`a=(l,t), q=(l,b0), c=(r,b0), d=(r,v), e=(s,v)`,

with t,s anchored, r->+infinity, and v remote. The cells a,e are outside D_82. The one-bit parent misses c because u(c)->+infinity. It misses d as well: if v->+infinity then z(d)->+infinity, while if v->-infinity then u(d)->+infinity. Its entire future has u<=58,z<=39. Thus there is no further collision and capture is permanent.

### 8.4 Transposed next-to-end orientation

This case must not be dismissed by reflection symmetry: reflection changes the right/left rule. Its actual coordinates are

`c=(r,b0), q=(l,b0), a=(l,t), d=(s,t), e=(s,v)`,

with r,v anchored, t->+infinity, s remote, and s>l eventually. The cells c,e are outside D_82. The two positive z-coefficient cells are q,d; hence z(d)->+infinity. The one-bit parent's full z<=39 bound excludes d. The only possible further collision is a on the northwest tail.

If a is read, z(a) stays bounded, whereas z(d)->+infinity. Since d and a share the row t, their horizontal separation `s-l=z(d)-z(a)` tends to positive infinity. An ordinary second-phase future has u<=u(a)+58. It misses H1, c (u->+infinity), d because `u(d)-u(a)=s-l->+infinity`, and e because `u(e)-u(a)=(s-l)+(t-v)->+infinity`. Thus a is exceptional and equals a_n.

The two-bit parent `{q_n,a_n}` now misses c,e by D_82 and misses d by its entire-future z<=71 bound. It is permanently standard, another contradiction.

All limiting shapes are excluded. Therefore an infinite mass-five checkpoint sequence cannot have empty local limit.

### Consequence and remaining gap

Combined with the earlier local-limit upper bound, a hypothetical recurrent mass-five orbit has, on some fixed-pose subsequence, **exactly one persistent local black cell and four remote cells**. More quantitatively, on each fixed-pose mass-five subsequence there is a finite neighborhood containing a black cell at all sufficiently late checkpoints; otherwise an empty local-limit subsequence could be extracted.

This does not exclude mass five. The one-black local core may be at an arbitrary fixed location, and an exceptional far collision can return to its complete, nonblank historical field. A new all-parameter two-black-parent return analysis is needed there. The result isolates that exact obstruction rather than silently replacing the parent by the blank orbit.

## 9. The retained one-black core must meet a fixed diagonal cross

**Status: independently reviewed analytic consequence.** Normalize the fixed checkpoint pose to `(0,0),N` in the same coordinates as the blank certificates. At any hypothetical recurrent mass-five subsequence with local limit `{s}`, the retained cell satisfies `s in D_82`.

Suppose instead `s outside D_82`. The entire blank trajectory lies in D_82: every finite prefix is an initial prefix of `{q_n}` for all sufficiently large n, and Section 7 includes those parents' entire futures. Hence the one-black local parent `{s}` agrees forever with the blank trajectory, with s as untouched debris. The blank first-contact reduction gives q=q_n, n tending to infinity. The four remote cells and the single bounded cell s can only have either a four-edge q strand or a four-cycle, by Section 5. Any three-edge q strand would leave either two bounded one-edge strands or one two-edge strand whose two cells both escape; neither realizes exactly one bounded and four escaping cells under the remote degree-two constraint. A five-edge strand contains no bounded edge and is also impossible.

### 9.1 Four-edge strand, first orientation

Its remote cells are `a=(l,t), q=(l,b0), c=(r,b0), d=(r,v)`, with t,v fixed and r tending to positive infinity. Both a,d lie outside D_82 eventually. The complete one-bit parent's u<=58 bound excludes c, and its D_82 confinement excludes s. Therefore the actual future equals the permanent one-bit parent, a contradiction.

### 9.2 Four-edge strand, transposed orientation

The remote cells are `c=(r,b0), q=(l,b0), a=(l,t), d=(s0,t)`, with r,s0 fixed and t tending to positive infinity. Both c,d lie outside D_82 eventually. The retained cell s also lies outside D_82. Thus the only possible extra hit for the one-bit parent is a, far along its northwest tail. If it never occurs, capture is permanent.

At an ordinary hit at a, the complete post-impact future obeys `u<=u(a)+58`. This misses H1, the fixed s, c, and d because `u(d)-u(a)=s0-l` tends to positive infinity. Therefore a=a_n is exceptional. The complete two-bit parent then misses c,d,s by D_82 confinement, and again capture is permanent.

### 9.3 Four-cycle

Its remote cells are q,a,c,d=(r,t), with signs +,-,-,+ and with both positive axial gaps diverging. Because q,d are the only positive z-coefficient cells outside the bounded core, the z,+ clock implies z(d) tends to positive infinity. The one-bit parent's bounds u<=58 and z<=39 exclude c and d, respectively. It misses s by D_82. Thus a must be read on the northwest tail. An ordinary a-hit misses H1 and s by its increasingly negative u half-plane, misses c, and misses d because `u(d)-u(a)=r-l` tends to positive infinity. Hence a=a_n.

The two-bit parent's z<=71 bound excludes d, and D_82 excludes s. Its finite prefix misses c by u<=98. Thus c must be read on the southeast tail. An ordinary c-hit misses H2 and s by its increasingly positive u half-plane, and misses d because `u(c)-u(d)=t-b0` tends to positive infinity. Hence c=c_n and d=d_n.

The complete three-bit parent never reads d_n and remains inside D_82, so it also misses s. It is permanent, the final contradiction. This proves the asserted retained-core restriction.

This restricts the persistent core to a fixed-width diagonal cross, not a finite set. It does not justify enumerating finitely many one-black cores, nor does it control a core located arbitrarily far along one arm of that cross.

## 10. What the two-sided minimum does and does not buy globally

The two-sided minimum condition is useful for rejecting particular small local cores, but it does not alone propagate an eventual mass bound or force a turn-language conclusion.

### 10.1 Explicit time reversal without complementing the field

Let `d_h` be the unit heading vector and define

`R(B,p,h) = (B, p-d_h, h+2)`.

Then R is an involution and `F R F = R`, equivalently `R F R = F^(-1)`. Indeed, if one forward update turns from h to h' at p, the reversed state at p has heading h'+2 and reads the flipped color. Its turn is the opposite turn, giving heading h+2 and a move to p-d_h. The color field returns to its earlier value. No infinite color complement is used.

### 10.2 Arbitrarily large global-minimum cores exist

Let T be the union of all read sites on the complete two-sided orbit of the empty field at a fixed pose. Its forward half is the certified blank trajectory. By the reversal formula, its backward half is a translated half-turn of another blank forward trajectory. Consequently T is contained in a finite union of fixed-width diagonal strips and a finite set; its complement is infinite.

Choose any finite set E in that complement. The complete two-sided orbit starting from E has exactly the same read positions, headings and read colors as the empty orbit, for every integer time: on each finite forward or backward interval, first-difference coupling applies, and none of the added cells is ever read. Its field is the empty orbit's field together with the untouched E. Hence its mass at any integer time r is

`|E| + |B_r^(empty)| >= |E|`.

Thus E is a global mass-minimum core, and |E| can be arbitrarily large. Its geometry can also be arbitrary within the infinite complement. This construction does not make a counterexample to highway capture; it shows that two-sided minimum by itself does not eliminate retained inert information.

### 10.3 Classifying all global-minimum cores is already equivalent to the full target

Every complete two-sided finite-field orbit has a minimum black mass: its set of attained masses is a nonempty subset of the nonnegative integers. That minimum is attained at some integer time. Eventual standard capture is unchanged by moving the initial state a finite number of steps forward or backward.

Therefore the statement “every finite-field global mass-minimum state eventually has the standard highway” is equivalent to the full finite-seed conjecture. The minimum property is not a standalone simplifying assumption that may be applied without proof to close the main theorem. What makes Section 2 useful is the additional strict loss of at least four cells in a recurrent sparse local limit.

A general induction would still need a complete-history interaction theorem: capture of the lower-mass local parent must survive all collisions with the escaping cells. The existing exact exceptional-parent calculations prove this for specific geometries, not for arbitrary parent archives. Even proving mass tends to infinity would leave the turn-language stabilization problem open.

## 11. A general incidence parity rule and a boundary of the endpoint method

**Status: independently audited.**

At a remote degree-two coordinate vertex, its two incident b signs are opposite. In addition, `b(x,y)=-sigma*(-1)^x*(-1)^y` factorizes through the two coordinate vertices. Consequently every alternating all-remote cycle in the incidence graph has length divisible by four. To see this, a cycle of length 2k has k distinct x-coordinate vertices in cyclic order; each shared y vertex forces the two adjoining x coordinates to have opposite parity. Returning to the initial x parity requires k even. In particular, an apparent alternating six-cycle cannot be realized by actual lattice cells. The same restriction applies to any alternating cycle even when other edges are present.

This extra parity does not make the low-mass first-collider polarity theorem extend to arbitrary mass. Here is an explicit eight-cell endpoint obstruction.

Take the union of two disjoint rectangles, for integer n sufficiently large:

`I_n = {-2n-17, 2n-16} x {-2n+9, 2n+10}`,

`O_n = {-6n-17, 6n-16} x {-6n+10, 6n+11}`.

Use the fixed head `(0,0),N`, so sigma=+1. The inner southwest and northeast corners have b=-1; its other corners have b=+1. The outer southwest and northeast corners have b=+1; its other corners have b=-1. Every occupied row and column has exactly two opposite signs, so all remote axial residues vanish. All eight cells escape, giving blank local limit and its valid two-sided mass-minimum property.

All four critical field sums tend to positive infinity. For the z clocks, the favorable outer corners have |z|=12n+O(1), while the adverse inner corners have |z|=4n+O(1) and the outer adverse corners have bounded z. For the u clocks, the favorable outer cross-corners have |u|=12n+O(1), while the adverse inner cross-corners have |u|=4n+O(1) and the outer adverse corners have bounded u. Bounded head corrections do not change this conclusion.

Nevertheless the first blank-tail collision is the inner southwest cell

`q=(-17,9)+n(-2,-2)`.

It is exactly the phase-13 fresh ray in the audited blank frontier table, and b(q)=-1. Every other inner corner is either northeast or has unbounded transverse u; the outer southwest corner lies exactly on the phase-28 fresh ray at depth 3n-1, later than phase 13 at depth n. Finite blank-prefix reads are irrelevant for sufficiently large n.

These are static endpoint states, not claimed checkpoints of one actual trajectory. Their role is precise: remote axial charges, four divergent clocks, bounded heads, blank local convergence, and the two-sided minimum of that local limit do not by themselves force favorable first-collider polarity once eight cells are permitted. A global proof must use additional chronological information or a different structural invariant.

## 12. Audited retained-core ray exclusion from the two-parameter certificate

**Status: independently audited on m>=15, n>=m+100.** The auditor has replayed the complete field, all prefix/archive interfaces, the canonical-core coupling, and the final phase-72 parity exclusion. The earlier m>=100 certificate is retained separately.

The scattering analysis has supplied an exact certificate on `m>=15, n>=m+100`, with

`s_m=(-23-2m,31+2m)`.

The source is `scattering/fixed_core_rectangle/`, particularly `bivariate_certificate.json` and `interface_geometry.json`. The audited complete-field interfaces are:

- The parent `{q_n,s_m}` has a permanent southeast tail from time `208n+208m+145000`, at `(40,-50),S`, phase 100. Its entire prefix and archive have `-4m-130<=u<=98` and `z<=71`; its whole future has `z<=71`, lies in D82, and has u bounded below by `-4m-130`.
- The parent `{q_n,s_m,c_n}` has a permanent northwest tail from time `416n+312m+197704`, at `(-2m-28,2m+68),N`, phase 100. Its complete prefix and XOR archive have `u>=-4m-130` and `z<=75`. Its whole future lies in D82. The phase-72 fresh ray is `(-2m-36,2m+72)+j(-2,2)`, whose x-coordinate is even.
- In the full five-bit certificate with the original a_n,d_n, those two cells are never read. Hence removing them supplies the stated two-/three-bit parents, not merely a truncated local comparison.

A recurrent mass-five local core cannot equal any fixed s_m with m>=15, even with arbitrary allowed remote axial partners rather than the exact original rectangle.

The entire blank trace has `-34<=u<=48`, so s_m is inert on the blank parent. The first remote collision is q_n. The one-bit q_n parent reaches s_m on its northwest tail before any remote northwest partner a: m is fixed while u(a) tends to negative infinity. The other remote cells miss that preliminary prefix by the same u/z guards as in Sections 8–9.

There are three remaining incidence shapes:

1. **Four-edge strand, first orientation.** Its a,d each have one bounded coordinate and one remote coordinate, so they miss D82. The two-bit q+s southeast parent can therefore only meet c. Any ordinary c-hit misses its archive (u<=98), a, and d, the latter because `u(c)-u(d)=v-b0` tends to infinity. Thus c is exceptional and equals c_n. The three-bit parent misses a,d by D82 and captures.
2. **Transposed four-edge strand.** Its c,d lie outside D82. Its a has u tending to negative infinity, so it misses the entire q+s southeast parent, whose u is bounded below for fixed m. Capture is permanent.
3. **Four-cycle.** Its d has z tending to positive infinity. The q+s parent misses d by z<=71 and a by its lower u bound. Thus only c can interrupt its southeast tail. An ordinary c-hit misses the archive, a, and d because `u(c)-u(d)=t-b0` tends to infinity. Therefore c=c_n. The three-bit prefix misses d by z<=75 and a by its lower u bound. On the final northwest tail, an a-hit cannot be exceptional: a lies on q_n's column x=-33-2n, which is odd, whereas the exceptional ray has even x. Every ordinary a-hit has complete future `u<=u(a)+58`; this misses the complete archive (u>=-4m-130), the fixed core, and d because `u(d)-u(a)=r-l` tends to infinity. Thus it also captures.

Each case contradicts recurrent mass five. The restriction m fixed is exactly appropriate to a retained local core; the bivariate all-domain certificate supplies the required eventual n threshold. This removes one full far northwest phase-72 core ray, not every cell of D82 and not arbitrary one-black parent histories.

## 13. Checkpoint and exact continuation targets (12:49 UTC)

### Audited deliverables

- Analytic audit of the recovered eventual-mass-five theorem: Section 1.
- Two-sided local-core minimum and five-cell first-collider polarity: Sections 2–3.
- Five-cell southwest exposure, exceptional first-contact reduction, exact two-strip geometry, and exclusion of blank mass-five local limits: Sections 5–8.
- Retained one-black core forced into D82: Section 9.
- Exact reversal and the limitations/equivalence of general mass-minimum classification: Section 10.

The independent auditor has explicitly passed Sections 2–3 and 5–10. Section 11's endpoint obstruction has now passed review. Section 12's analytic argument also passed review conditional on its stated interfaces; the main m>=100 complete-field replay passed, while interface and enlarged-domain verification are being completed.

### Symbolic work handed to the word analysis

The C/V local last-writer proof was independently inspected here: all patch-intersecting coarse poses are covered, the outside reentry is conservative, and the four physical patch cells form one dual star. The word analysis has since extended the proof to C/V/B and is independently auditing that result.

My general index-two-lattice extension is `word_stabilization/cuv_local_trap_global.py`. For C/U/V and U/V noses, radius-1 and radius-2 patches admit abstract OUT-teleport witnesses. Radius-3 plain BFS reached two million states without a witness or exhaustion. An antichain version was stopped for excessive cost, with no conclusion. These are abstraction limitations, not physical counterexamples.

A new 16-million-node exploratory metric intersects globally fresh first-L sites across feasible macro occurrences. The exact surviving candidate sets and counterexample words for removed sites are in `word_stabilization/fresh_intersection_summary.json`. V retains `(1,2)`; U retains `(0,2),(0,3)`; Q and B retain several other sites despite their reused `(0,2)` noses. This remains bounded-search evidence only.

Eight surviving Q sites were tested with the full-five-macro local last-writer abstraction. Radius 1 permits abstract witnesses for all; at radius 2, `(-2,2)` and `(-3,2)` still permit OUT witnesses, while the other six reached 1.5 million states without a decision. The word analysis is building a Boolean-diagram reachability implementation which may resolve these finite abstractions more efficiently. Logs: `q_fresh_site_local_radius1.log` and `q_fresh_site_local_radius2.log`.

### Open next targets

1. Audit Section 11 and the new bivariate certificate, then audit and publish the precisely scoped Section 12 ray exclusion.
2. Test other retained-core northwest fresh phases, retaining full archives. The successful phase-72 ray suggests finite channel types with exact two-parameter certificates, but no finite all-core coverage has been established.
3. Continue the symbolic analysis's BDD last-writer analysis for U/V or a surviving Q marked site. The immediate goal is a rigorous positive-fuel lemma for all five macros, not another uncapped simulation.
4. For the full conjecture, supply a chronological mechanism beyond low-mass endpoint constraints. Even complete elimination of recurrent bounded mass would not itself force the standard turn word.

No computation owned by this analysis remains running at this checkpoint. All code, logs, proofs and explicitly failed approaches have been preserved in the shared workspace.


## 14. Continuation checkpoint: chronological fuel and exact port colors (13:20 UTC)

The Section 12 retained-core ray theorem is now independently audited on the enlarged cone `m>=15, n>=m+100`. Further low-index retained cores are being treated by the scattering analysis with separate exact certificates. These are low-mass structural restrictions, not a route by themselves to the full highway theorem.

### 14.1 A uniform exit-fuel candidate, still unproved

The exploratory fresh-site intersections have a common surviving site: every non-C macro's last physical read cell. In its north-oriented entry frame these are V `(1,2)`, U `(0,3)`, Q `(-4,-3)`, and B `(-3,-4)`. Each is read L on its first visit within that macro and R on its last visit, which is the final phase. In contrast C's final cell is first read R within C. A possible uniform chronological statement is that each non-C exit cell was unread before the whole macro segment. This would imply positive first-L fuel for each non-C macro, but it is only a candidate supported by bounded exploration.

Current attempts must retain chronology. A static black-graph bridge/2-core explanation fails: `black_core_probe_global.py` finds that black 2-core edge inclusion is not monotone even through CCCC, and the verified feasible word `UBVCVUVVVVUVCVUCVVVVUUQ` has U exits which are already nonbridges in the black 2-core although their first L is globally fresh. Thus “every non-C exit consumes a current black bridge” is false. The failure does not refute a historical or labeled-edge invariant.

A simple larger-pattern count also fails. `marker_count_probe_global.py/json` gives exact feasible local fields in which each individual macro type increases the count of oriented 12-letter marker embeddings by two. This rules out that particular raw-count potential; it does not rule out every weighted 4-by-3 pattern potential. The prior exact nonnegative 3-by-3 energy obstruction remains the broader established no-go in its own stated class.

### 14.2 Finite abstraction refinements and their present limits

The full-five local last-writer closure now tracks the actual recovered H-port graph, with 994 ports and 2,702 physically feasible edges, minimized by future macro language to 77 classes. The source's other 45 edges fail literal physical parity consistency. This restricts the analysis to actual H tails, which is the relevant global word-stabilization goal; it is not a theorem about arbitrary five-macro words.

The word analysis further intersected each inside local state with colors forced by its port's preceding history. Each 149-letter port ends in the common 12-letter marker. Remove this final marker, replay the preceding 137 turns, and transport the resulting last-read colors into the current before-marker frame. For a minimized class, take the union, not the intersection, of the exact-port color cubes. OUT states remain unconstrained. These are necessary conditions for every real H-tail state, so such intersections are conservative.

I independently checked this color refinement without importing the analysis's template or BDD code. `audits/check_port_color_frames_global.py/json` reconstructs every template backwards from the fixed terminal head `(0,0,N)` and compares it with the forward-normalized construction. All 994 templates pass. Across all 2,702 feasible port edges, the checker verifies the exact before-marker suffix identity, source read consistency, class transition agreement, and 200,653 destination-color equalities. The 45 discarded edges are independently confirmed inconsistent. This is a proof of the color/frame alignment and a finite check of its exact input graph, not an audit of the BDD fixed-point implementation or of the original graph's language-exhaustiveness derivation.

Five variable-order experiments for the simpler short-grammar Q-exit radius-two BDD all remained inconclusive at the allocated resource cap: radial, Chebyshev, checkerboard, diagonal, and reverse orders. No physical counterexample or finite exclusion resulted. Their logs are `bdd_Qexit_*.log`; the more meaningful ongoing computation is the actual-port and port-color refined closure owned by the word analysis.

### 14.3 The global gap remains explicit

Even an all-five positive-fuel theorem would exclude the non-highway H macro component only after the orbit's adjacent ten-turn windows are all in the standard factor language. Proving that only finitely many bad ten-turn windows occur is a separate missing global step. Likewise, excluding all recurrent bounded masses would not classify unbounded-mass dynamics. Neither progress line is represented here as a proof of the full conjecture.

## 15. Entire retained phase-72 core ray and the new covering bridge (13:46 UTC)

### 15.1 Full half-ray exclusion

The independent auditor has completed all separate fixed-index certificates for m=0,...,14. Together with Section 12, this excludes every retained local core

`s_m=(-23-2m,31+2m), m>=0`

under the established recurrent-mass-five incidence hypotheses. The low-index proofs use their own exact output channels and complete archive interfaces, not an unsupported extrapolation of the m>=15 formula. Audit records include `audits/near_core_snapshot/`, `near_core_replay.log`, and `near_core_analytic_review.md`. This still leaves other retained cores in D82 and does not prove eventual mass six.

### 15.2 Exact covering geometry

`first_principles_new/punctured_plane_cover_global.md` identifies the free-product model geometrically. The fixed-sector physical head graph is the square medial graph. Fill its directed R^4 and L^4 plaquette faces and leave its physical-cell diamond faces unfilled. Its universal cover is the tree of R/L squares for G=C4*C4. A lifted physical-cell boundary has incoming corners exactly the right coset gH, H=<RL^3>. Distinct lifts of one physical cell are disjoint boundary lines. The auditor has independently reviewed this covering construction and its conditional first-violation transfer.

The new dynamical idea uses the audited module return ledger. Every completed G call has grammar `a^4` or `a^2 G_b a^2`, and every completed B call has grammar `a G_b a^3` or `a G_b a G'_b a^2`, where b is opposite a. These are one or two axial fingers, not arbitrary nested trees. For a north-facing R module at the origin, every completed read lies in

`Q_R={x>=0, y in {-1,0}} union {x in {0,1}, y>=0}`,

and Q_L is its reflection. Hits of either module boundary point belong to its actual boundary coset.

The first-principles analysis has written the completed-finger / no-interleaving theorem at `first_principles_new/completed_fingers_and_no_interleaving.md`. It passed full independent analytic audit at 13:46 UTC, including the noncircular square-to-coset transfer. I independently checked the crucial finite geometry and the initial-prefix / unfinished-call logic. The checker `audits/check_module_projection_neighborhood_global.py/json` keeps both root faces and their four children explicit, verifies all 16 explicit representatives above the six tracked physical cells, all eight grandchild packet-region intersections, and all eight first-turn-change rebases. These are exact finite group and affine-region checks, not bounded trajectory exploration.

The interval argument is important. After rebasing at the first turn change following an initial visit A, A is root, predecessor, or one of the first two interiors of a root face. An abstract grandchild call contains none of these cosets in its interior. If it contains a physical visit B above the same point and is followed by a later A visit, it must return, or reach A at its final boundary and complete one step later. Thus its COMPLETE-call Q bound applies retrospectively. The exact table says that its only possible hit of the tracked physical point is its true predecessor coset, not B. This proves autonomous no-A-B-A without presuming physical lift legality.

A first-violation argument transfers it to every square-ant trace: before an alleged first interleaving, assigning each coset its actual first-read color makes the lifted prefix autonomous-legal. The autonomous path already reaches the forbidden final A before its next lamp read, giving a contradiction. This closes the square-to-coset legality gap. The audited five-visits-per-group-state, six-visits-per-coset, proper symbolic lift, and unique limiting reduced boundary ray therefore transfer to every square-ant trace. It does not close the finite physical seed / infinite lifted seed gap, imply physical transience, or select the highway.

## 16. A smaller sufficient symbolic target: V fuel only

I independently audited the all-parameter proof in `word_stabilization/triple_u_fold_lemma.md` and freshly replayed `verify_triple_u_fold_lemma.py`. For every A,F,D in {Q,B} and every n,m>=0,

`A U^n F U^m D`

is physically unrealizable. The proof explicitly exhibits two consecutive equal reads of one physical cell. I rederived its transformed coordinates, occurrence indices, and intervening-footprint exclusions in all five cases, including n=0 and m=n. The 5,000 finite regression checks corroborate the literal footprint identities but are not the reason the unbounded parameter claim holds.

Combined with the exact short-gap grammar, every infinite physically feasible five-macro tail with finitely many V blocks would eventually be U-only: C cannot persist without another V, and at most two Q/B folds can occur in the remaining U/Q/B suffix. A U-only tail requires an unbounded number of globally first-read-L cells and hence cannot run from a finite black field.

Therefore every infinite finite-support five-macro tail must contain infinitely many V blocks. Proving that V's tip `(1,2)` is globally fresh in all actual H tails is now a sufficient fuel target by itself; freshness for U, Q, and B is unnecessary for this route. This does not yet prove V freshness, and it does not prove eventual admission to the standard ten-factor language.

### 16.1 Quantitative V-free bound

The same proof gives a finite bound, independently checked here. A V-free interval starting from m black cells has at most `floor(151m/125+10) <= 2m+10` macros. It has at most one leading C, three trailing C, two Q/B folds, and three U runs. A positive U run of length r needs `5r+4` black cells at its own entry; C,U,Q,B change mass by 3,4,6,6. The resulting safe bounds are `r0<=m/5`, `5r1<=m+5+4r0`, and `5r2<=m+11+4(r0+r1)`. This is a finite-fuel theorem for the complete V-free alphabet, not a bound for words containing V.

### 16.2 Symbolic exit freshness is exact but not physical freshness

The now-audited covering bridge permits a clean distinction. Every macro has a reduced endpoint S-word F_A with syllable exponents1 or2, starting R and ending L. Macro concatenation therefore causes no cancellation at endpoints. The exact reductions are C=`RLL`, V=`RLLRRL`, U=`RLLRLRRL`, with longer analogous Q/B words.

For each non-C macro T, the exit cell's first-L coset has a canonical S representative E_T starting R and containing at least three syllables. A finite exact calculation shows every read coset inside an earlier macro A has canonical syllable length at most `len(F_A)+1` relative to that macro's entry. But a future exit, after A and any number of intervening macros, has representative `F_A F_between E_T`, already an S-word, of length at least `len(F_A)+3`. Left-canceling the earlier macro entry therefore proves that the future exit coset cannot have been read in A.

The verifier is `word_stabilization/check_exit_coset_fresh_global.py/json`. Its finite bounds cover arbitrarily many intervening macros, because every extra endpoint word only increases the already-too-large canonical length. Thus every non-C exit is globally new as a SYMBOLIC coset within a macro concatenation. This does not make its physical cell new: another, older coset can project to the same square cell. That remaining projection collision is exactly what the V-fuel proof must exclude or charge.

## 17. An all-history monotone cancellation height

The new theorem in `first_principles_new/monotone_cancellation_height.md` passed independent analytic review. It applies to every positive turn word, not merely an eventual macro language or a low-mass checkpoint. Write rho_t=-sigma*(-1)^(x+y)*1_{B_t}. Online free-product reduction of the turn word removes R^4 or L^4 face loops. Every such deletion deposits one positive unit on its physical plaquette, regardless of heading or sector. The resulting integer height K_t is pointwise nonnegative and nondecreasing, and

`rho_t = rho_0 + D(reduced_word_t) + partial_xy K_t`.

Finite-support injectivity of the mixed difference makes the physical height independent of deletion order. Concatenating two words adds their separately placed heights plus a nonnegative joining defect. Exact weighted mixed-difference identities recover the four exponential clocks, while the mass identity contains alternating plaquette signs. Thus height positivity is not a positive finite fuel and the mixed derivative has no maximum principle. `audits/check_cancellation_height_global.py/json` independently checks 32 local face identities, 1,000 arbitrary words and splits, and 240 literal field/mass identities.

A useful obstruction is already visible: the nested eight-cell rectangles of Section 11 have signed field equal to the mixed difference of the outer rectangle indicator minus the inner rectangle indicator. Their containing rectangles make that height nonnegative. Therefore final height positivity alone cannot exclude those adverse-collider static states. Any successful use of the new height must retain chronological deposition or reduced-spine information, not only its endpoint value.

## 18. Protected new-route exploration checkpoint

At the coordinator's request I am preserving the audited framework above and switching one exploration slot to a genuinely different question: the exact dual white-edge process and the evolution of its active component. No eventual factor language, low-mass hypothesis, bounded retreat, or legal symbolic lift is assumed. The complementary explorer is investigating exact inverse design of nonstandard traveling fronts, actively testing the conjecture rather than assuming the standard period.

## 19. A distinct frontier route: exact exclusion hops and pristine strip barriers

The protected exploration slot produced an unrestricted column mechanism, independent of the macro language, symbolic cover, and low-mass hypotheses. Details are in `frontier_exploration/column_exclusion_rank.md`.

At a fixed physical column, a horizontal entry is followed by one vertical read and then a horizontal exit. Complement the black bit on V rows but not H rows. Every reflection back to the left is exactly one exclusion-particle hop upward; every reflection back to the right is one hop downward. With H rows and N particles, the particle-height rank has range N(H-N), so at most floor(H^2/4) reflections from one side occur without an opposite entry or transmission. Transmissions instead create or destroy two particles and cannot be silently included in the same rank sum.

This rank itself gives a self-contained proof of finite-domain escape: a bounded infinite orbit would have a rightmost recurrent column, eventually entered only from the left and never transmitted right, contradicting its finite reflection budget.

More substantially, an exact finite overapproximation permits arbitrary sector-compatible left reentries into a pristine 11-column by 9-row block. The complete inductive mask set contains 275,057 states. Every one of its 1,100,228 entry cases was replayed independently with literal one-update dynamics: 686,294 return left to the invariant set, 413,934 exit vertically, and none exits right. Maximum excursion length is 171 updates. Files are `frontier_exploration/certify_blank_strip_barrier.py`, `barrier_h9_w11.hex`, and `barrier_h9_w11.json`; the mask-set SHA256 is `04ec386f8d519687306a073b3ead9cb859109f133c62ae2ff34f132a3c4058c4`.

The abstraction is sound because before the first right crossing all real safe block entries are from the left and external excursions cannot alter block cells. Place a copy beyond the finite field on the right and a 180-degree rotated copy on the left, choosing horizontal parity separately. Any tail confined to the nine physical rows would be trapped between those barriers, contradicting the rank-based finite-domain escape proof. Thus no finite-support orbit has a tail in nine or fewer consecutive horizontal rows; rotation gives the vertical version. Smaller strips embed in nine rows. This is not a diagonal-strip theorem and does not conflict with the standard highway.

The independent auditor has approved the abstraction and placement logic and received the stable certificate for independent replay. Full novelty relative to primary literature remains unconfirmed; MFCS finite-domain escape and diagonal periodic-width exclusions have different stated scope. The former literature analysis was sent the comparison request but is not currently active; a comprehensive primary-source priority check remains open.

No owned computation remains running. The next genuine question is analytic all-height pristine barriers versus a countermodel using arbitrary left reentry. Larger state-cap hits are inconclusive. Such a driven barrier theorem is stronger than finite-support strip escape, so its failure would not by itself refute the highway conjecture. The complete next-target list and stopped-run status are preserved in the frontier note.
