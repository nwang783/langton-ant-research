# Every finite-seed Langton ant is eventually above black mass four

**Status.** Computer-assisted theorem, using the exact finite certificates
listed in Section 9. The deductions between the certificates are given below,
including the complete-field guards at the second and third collisions.
This is a lower bound on eventual black mass. It does not prove that the mass
tends to infinity or that every finite seed eventually forms a highway.

## 1. Statement and conventions

At a white cell the ant turns right, at a black cell it turns left, then flips
the cell and moves one unit in its new heading. North is `(0,1)`. The complete
state is `(B,p,h)`, where `B` is a finite subset of the square lattice, `p` is
the cell about to be read, and `h` is its incoming heading. Write `M_t=|B_t|`.

**Theorem.** For every finite initial black set and every initial pose, there
is a time `T` such that

\[
 M_t\ge 5\qquad(t\ge T).
\tag{1}
\]

Equivalently, `liminf M_t >= 5`. The previous result in
**low_mass_recurrence.md** proves that only finitely many times have mass at
most three. We prove here that only finitely many times have mass exactly
four.

All fields in this argument are complete fields. When two fields are
compared, their difference means symmetric difference. In particular, no
old wake or scatter residue is discarded when applying a one-bit certificate.

## 2. Analytic prerequisites and the first collision

Suppose, for a contradiction, that one finite-seed trajectory has infinitely
many mass-four checkpoints. The axial separator and sharp clock-forcing
theorems proved in **axial_separator_proof.md** and
**low_mass_recurrence.md** imply the following facts.

1. The checkpoint heads lie in one fixed finite box.
2. All four one-sided critical clocks tend to positive infinity.
3. There is an infinite subsequence having exactly one fixed head position
   and heading.

Translate and rotate that fixed pose to `(0,0),N`. This is a symmetry of the
rule. The invariant checkerboard/heading sector is then `sigma=+1`. Put

\[
 z(x,y)=x+y,\qquad u(x,y)=x-y,\qquad \chi(x,y)=(-1)^{x+y}.
\tag{2}
\]

At all sufficiently late checkpoints there are two black cells of each
checkerboard sign. Among the two `chi=-1` cells, one has `z` tending to
negative infinity and the other has `z` tending to positive infinity. Among
the two `chi=+1` cells, one has `u` tending to negative infinity and the other
has `u` tending to positive infinity. These conclusions follow directly from
the positive terms of the two z-clocks and two u-clocks: both opposite
exponentials must diverge, while the head corrections are fixed. In
particular, all four input cells escape every fixed bounded set.

Starting at such a checkpoint, compare with the entirely white input at the
same pose. The futures agree until the blank orbit first reads one of the
four input cells. Such a collision must occur: otherwise the actual orbit
has the blank standard tail with four untouched extra bits, and its mass
eventually grows by twelve in every period of 104 updates.

The exact blank tail starts at update 9977 at `(-15,10),W`, with drift
`(-2,-2)`. Therefore the first collision is arbitrarily far southwest. Its
cell `q` has bounded `u` and `z(q)->-infinity`. It is the negative-z
`chi=-1` cell. The other `chi=-1` cell will be denoted by `d`.

The first-collision theorem in **mass4_first_collision.md** proves that every
sufficiently late such checkpoint has first collision at fresh phase 72.
That theorem includes the full blank historical residue, the current
canonical wake, and the nine ordinary channels. Its coordinate conclusion is

\[
 q=(-17,2)+k(-2,-2),\qquad k\longrightarrow\infty.
\]

Set `n=k-8`. Then

\[
 \boxed{q=(l,b)=(-33-2n,-14-2n)},\qquad n\longrightarrow\infty.
\tag{3}
\]

The shift by eight merely fixes the convenient origin of the parameter.
Only sufficiently large n will be used.

## 3. Remote row and column charges expose a southwest corner

Choose a fixed integer `D` containing the original finite seed, its original
head, and the normalized checkpoint head in `[-D,D]^2`. At every selected
checkpoint, every row or column outside this box has signed black sum zero
modulo four. For rows the signed sum is `sum (-1)^x`; for columns it is
`sum (-1)^y`. To justify this use of the axial invariant, the row or column
starts empty and both endpoint heads lie on the same side. The endpoint
correction is therefore the same at both ends.

This assertion concerns the selected checkpoint fields. We do **not** assume
that a remote line has zero signed sum at intermediate scattering times,
when the head may have crossed it.

For large n, both the row and the column of q are remote. Each must contain
at least two black cells. One or three cells have an odd signed sum and
cannot have residue zero. Four cells on one of these lines would leave the
perpendicular line through q with only q, which is also impossible. Thus
each of these two lines contains exactly two cells, with opposite alternating
signs. The input field has the exact form

\[
 B=\{q,\ a=(l,t),\ c=(r,b),\ d=(s,v)\},
\tag{4}
\]

where a,c have `chi=+1` and d has `chi=-1`. We already know

\[
 z(d)\longrightarrow+\infty.
\tag{5}
\]

Write `H=t-b` and `J=r-l`. Since `u(q)=-19`,

\[
 u(a)=-19-H,\qquad u(c)=-19+J.
\tag{6}
\]

The two quantities in (6) tend to opposite infinities, so H and J have the
same sign for every sufficiently late checkpoint, and their absolute values
tend to infinity. The negative alternative is impossible. Along a
subsequence with `H,J->-infinity`, all coordinates of q,a,c would tend to
negative infinity. If either coordinate of d exceeded D, it would occupy a
remote row or column alone, violating its zero charge. Hence both coordinates
of d would be at most D, contradicting (5).

Consequently

\[
 H\to+\infty,\quad J\to+\infty,\quad
 u(a)\to-\infty,\quad u(c)\to+\infty.
\tag{7}
\]

The fourth cell cannot share q's row or column: it would make that line
contain exactly three cells. Any remote x-coordinate of d must therefore be
r, and any remote y-coordinate must be t. Thus

\[
 s\in\{r\}\cup[-D,D],\qquad v\in\{t\}\cup[-D,D],
\tag{8}
\]

and in particular

\[
 s-l\to+\infty,\qquad v-b\to+\infty.
\tag{9}
\]

At this point a rectangle has **not** been assumed. It will follow after
both t and r have been forced outside the fixed charge box.

## 4. Exact scattering facts used below

### 4.1 The nine ordinary current-bit channels

Let

\[
 F=\{14,28,32,38,46,56,60,62,70,72\},\qquad
 O=F\setminus\{72\}.
\tag{10}
\]

These are the ten even fresh phases of the standard period-104 word W.
Freshness is the first read of a cell, including all earlier periods. The
geometric frontier classification stabilizes at age two. The complete
canonical one-bit certificate supplies the following lemma uniformly at
every age at least 13 and every phase in O.

For an incoming southwest canonical highway, toggle the current read cell q.
The complete perturbed field has a permanent standard future, and its entire
post-impact read set, finite recovery and infinite tail together, satisfies

\[
 z(w)\le z(q)+58.
\tag{11}
\]

The portions of that read set on q's horizontal and vertical axes satisfy

\[
 (q_x+j,q_y)\text{ read}\ \Longrightarrow |j|\le31,
\]
\[
 (q_x,q_y+j)\text{ read}\ \Longrightarrow |j|\le34.
\tag{12}
\]

These are bounds on the full infinite read trace, not on a sampled prefix.
The certificate keeps the complete accumulated wake. Its old-tail exclusion
proves the same trace for every larger canonical age. The largest of the
nine individual thresholds is 13.

Let `R(x,y)=(y,-x)` be a clockwise quarter-turn. Then
`u(Rw)=z(w)` and `u(R^{-1}w)=-z(w)`. Rotating (11)–(12) gives the two forms
needed here:

| Incoming canonical highway | Entire ordinary post-impact read set | Horizontal axis | Vertical axis |
| --- | --- | ---: | ---: |
| Northwest | `u(w) <= u(q)+58` | distance at most 34 | distance at most 31 |
| Southeast | `u(w) >= u(q)-58` | distance at most 34 | distance at most 31 |

The exchange of the axis constants is essential.

### 4.2 One-bit and two-bit exceptional parents

For every integer `n>=200`, define

\[
\begin{aligned}
 q_n&=(-33-2n,-14-2n),\\
 a_n&=(-33-2n,41+2n),\\
 c_n&=(8+2n,-14-2n),\\
 d_n&=(8+2n,41+2n).
\end{aligned}
\tag{13}
\]

All parent inputs below start at `(0,0),N` on an otherwise white field.
The exact affine-field certificates prove the following statements.

| Parent input | Certified checkpoint time | Pose at that time | Standard future from that pose |
| --- | ---: | --- | --- |
| `{q_n}` | `208n+70733` | `(-15,26),E` | phase 99 of W, drift `(-2,2)` |
| `{q_n,a_n}` | `416n+146040` | `(40,-50),S` | phase 100 of W, drift `(2,-2)` |

The **entire read prefix from input time zero** obeys these exact bounds:

| Parent prefix | u-coordinate of reads | z-coordinate of reads |
| --- | --- | --- |
| Through the first checkpoint above | `-82 <= u <= 58` | `z <= 39` |
| Through the second checkpoint above | `u <= 98` | `z <= 71` |

The first parent's entire future, including its northwest tail, has
`u<=58` and `z<=39`. The second parent's entire future has `z<=71`.

After five more updates in the first parent, the phase-zero pose is
`(-15,29),N`. After four more updates in the second, it is `(40,-52),S`.
At these phase-zero poses, compare each complete field with the placed
thirteen-black canonical core. Their XOR differences `H_{1,n}` and
`H_{2,n}` satisfy

\[
 -82\le u(w)\le58\quad(w\in H_{1,n}),
\qquad
 u(w)\le98\quad(w\in H_{2,n}).
\tag{14}
\]

The sharper checked second bound is 97, but 98 suffices. Both differences
are zero on every future ray of their respective incoming standard tail.
Therefore they remain the exact same complete-field differences when both
the parent and the canonical core are advanced to any later matched phase.
They include all earlier wakes, both distant scatter residues, and all
near-origin debris that is present at the stated stage.

The phase-72 fresh rays of these two placed standard tails are exactly

\[
 (-23,31)+m(-2,2),\qquad m\ge0,
\tag{15}
\]

and

\[
 (48,-54)+m(2,-2),\qquad m\ge0.
\tag{16}
\]

Their z-coordinates are 8 and -6 respectively. The phase-zero origins have
even checkerboard parity, and their headings are vertical. Consequently an
initial `chi=+1` cell hit on either far tail has an even fresh phase, exactly
one of the ten phases in (10). The twelve odd frontier phases do not apply.

### 4.3 Why these parent statements are genuine complete-field certificates

There are two compatible verification routes. The affine verifier checks
both parent infinite tails directly against the complete retained field.
The independent core audit XORs the phase-correct clean core with that field
and checks zero parity on all future rays.

A simpler guard also explains why no growing-history assumption is hidden
here. The prescribed four-corner template's first prefix reads have
`-82<=u<=58,z<=39`. The unused corners have

\[
 u(a_n)=-74-4n,\qquad u(c_n)=22+4n,\qquad z(d_n)=49+4n.
\tag{17}
\]

Thus those three bits are unread through the first parent checkpoint for
every n>=200. Through the second parent checkpoint, c_n and d_n are unread
by `u<=98,z<=71`. Removing these untouched initial bits gives exactly the
one-bit and two-bit parent fields; this is an XOR identity, not a replacement
of a damaged field by a clean core.

Every black cell of a parent at one of these checkpoints is either an
initial parent cell or a previously read cell. The prefix read bounds and
the fixed clean-core bounds therefore imply (14), even without using XOR
cancellations. The first parent's phase-99 tail requires only eleven whole
periods before all later reads satisfy `u<-82`. The second parent's
phase-100 tail requires only three periods before all later reads satisfy
`u>98`. The template contains these periods for every n>=200. They read only
within `[-53,53]^2` and `[-60,60]^2` respectively, so none of the omitted
corners can affect them. Finite first-difference coupling followed by the
directional exclusion proves both infinite parent tails. This argument
uses the exact all-parameter color verification of the template, not the
two numerical runs from which its candidate word was first extracted.

### 4.4 The remaining rectangle

The same exact affine-field verification proves that the full four-cell
input in (13) has a standard northwest future by time

\[
 T_n=728n+200304\qquad(n\ge200).
\tag{18}
\]

Its pose at that time is `(-2n-58,2n+98),N`. The fourth, northeast input
cell d_n is never read, either in the verified prefix or in the certified
infinite tail. No assertion about the family for n<200 is required below.

## 5. The second collision must be the exceptional northwest hit

Return to the hypothetical mass-four subsequence. Its q is q_n by (3), but
its other three cells initially have only the form and limits in (4)–(9).

Compare the actual input with the one-bit parent `{q_n}`. For all sufficiently
late checkpoints, a has `u(a)<-82`, c has `u(c)>58`, and d has `z(d)>39`.
The entire first parent prefix misses all three, so the actual orbit reaches
the first fixed northwest stage with precisely those three extra untouched
bits. The full one-bit parent future misses c and d as well, since it always
has `u<=58,z<=39`.

Therefore the next initially black collision, if one occurs, is a. It must
occur: otherwise the complete actual future has the standard northwest
word, and its mass grows by twelve per period, contradicting the infinitely
many later mass-four checkpoints.

The hit of a is arbitrarily far along the northwest tail because
`u(a)->-infinity`. Its fresh phase is in F and its canonical age tends to
infinity. Its z-coordinate belongs to the finite set of transverse
coordinates of that tail. Since `a_x=l->-infinity`, it follows that
`t=a_y->+infinity`. The original checkpoint row t is therefore remote. Its
only possible partner for a is d, so

\[
 v=t.
\tag{19}
\]

This use of the row charge is at the original four-cell checkpoint, not at
the later impact state.

Suppose a's phase is ordinary, in O. Just before the impact, the actual
complete field differs from the mature canonical northwest source with its
current bit toggled by exactly

\[
 H_{1,n}\mathbin\triangle\{c,d\}.
\tag{20}
\]

This identity follows by advancing the full canonical and parent fields
together along the incoming tail. All extra bits have remained unread.

The entire ordinary post-impact trace misses (20):

* It has `u(w)<=u(a)+58`, which is eventually less than -82, whereas every
  cell in `H_{1,n}` has `u>=-82`.
* It misses c because `u(c)->+infinity` while `u(a)->-infinity`.
* The cell d lies on a's horizontal axis by (19), with displacement
  `s-l->+infinity`. The exact horizontal-axis guard is 34, so it misses d.

Complete-field first-difference coupling therefore transfers the canonical
permanent standard future to the actual trajectory. That is again
incompatible with infinitely many later mass-four checkpoints. All nine
ordinary phases are excluded.

The second collision must consequently have phase 72. Intersect (15) with
a's already known column `x=l=-33-2n`. The period index is `m=n+5`, giving

\[
 \boxed{a=a_n=(-33-2n,41+2n)}.
\tag{21}
\]

Equation (19) also gives `d_y=41+2n`.

## 6. The third collision must be the exceptional southeast hit

Now compare the actual input with the two-bit parent `{q_n,a_n}`. Its
complete prefix through the fixed southeast stage has `u<=98,z<=71`.
The remaining initial cells satisfy `u(c)->+infinity` and
`z(d)->+infinity`, so neither is read during that prefix. The actual orbit
therefore reaches the second fixed stage with exactly c,d still added to
the complete parent field.

The entire two-bit parent future has `z<=71`, so it never reads d for late
checkpoints. It must eventually read c; otherwise the actual future is
already permanently standard southeast and cannot have infinitely many
later mass-four checkpoints.

This hit of c is arbitrarily far along the southeast tail because
`u(c)->+infinity`. It has a fresh phase in F. The tail's z-coordinates are
bounded, while `c_y=b->-infinity`; hence `r=c_x->+infinity`. At the original
checkpoint, column r is now remote. Its only possible partner for c is d,
so

\[
 s=r.
\tag{22}
\]

If c's phase is ordinary, the complete actual field just before the impact
differs from the current-bit-perturbed canonical southeast source by

\[
 H_{2,n}\mathbin\triangle\{d\}.
\tag{23}
\]

The full ordinary read trace has `u(w)>=u(c)-58`, which is eventually greater
than 98. It therefore misses every cell of `H_{2,n}`. By (22), d is on c's
vertical axis, at distance

\[
 d_y-c_y=t-b=55+4n\longrightarrow\infty.
\]

The exact vertical-axis guard is 31, so that read trace misses d as well.
Coupling transfers the permanent standard future, a contradiction. Thus
the third phase must also be 72.

Intersect (16) with `c_y=b=-14-2n`. Its period index is `m=n-20`, so

\[
 \boxed{c=c_n=(8+2n,-14-2n)}.
\tag{24}
\]

The period index is nonnegative for all parameters now under consideration.
Equations (19), (21), and (22) force

\[
 \boxed{d=d_n=(8+2n,41+2n)}.
\tag{25}
\]

The entire four-cell checkpoint field is therefore the exact rectangle

\[
 \boxed{B=\{-33-2n,\,8+2n\}\times\{-14-2n,\,41+2n\}}.
\tag{26}
\]

## 7. Contradiction and conclusion

The parameter n tends to infinity along the hypothetical subsequence.
Choose a sufficiently late checkpoint so that all preceding guards hold
and `n>=200`. Its complete state is (26) with pose `(0,0),N`. The all-parameter
rectangle certificate (18) gives it a permanent standard northwest future.

The standard word contains 58 right turns and 46 left turns. Therefore the
complete black mass increases by exactly twelve in every subsequent full
period, and is eventually greater than four even during each period. It
cannot have infinitely many later mass-four checkpoints. This is the desired
contradiction.

Only finitely many times have mass four. Combined with the already proved
eventual exclusion of mass at most three, this proves (1). ∎

## 8. Quantifier and history audit

The proof does not infer an all-parameter claim from finitely many simulations.
The rectangle word was generated experimentally, but every required input
color and the infinite tail were then checked for every integer n>=200 by
exact affine arithmetic and XOR parity. Small parameter values are irrelevant
to the contradiction because its forced parameter tends to infinity.

The geometric bounds in Sections 5 and 6 concern arbitrary remaining cells
satisfying the recurrence limits. They do not assume those cells already
form the proposed rectangle. The row of a becomes remote only after the
northwest hit is established; the column of c becomes remote only after
the southeast hit is established. Those two original-checkpoint charges are
exactly what eventually force d to be the northeast corner.

Every ordinary-channel application retains an exact field difference,
(20) or (23), whose entire support is proved disjoint from the full future
read set. The canonical source contains its entire age-dependent wake.
The additional XOR archives contain all modified old material. A second
one-bit table application is never made solely from the appearance of a
local highway patch.

The fixed phase-zero origins in both later stages are even-parity cells.
The axial partners have `chi=+1`, so the allowed ten phases are unchanged
after rotating the incoming direction. This prevents accidentally applying
the nine-channel table to one of the twelve other frontier phases.

## 9. Exact dependencies and reproducibility

The analytic prerequisites are:

* **axial_separator_proof.md**: signed row/column invariants and the
  heading-corrected endpoint support bound;
* **low_mass_recurrence.md**: the sharp `2K+4` forcing lemma, divergence of
  all four clocks under low-mass recurrence, and eventual mass at least four;
* **mass4_first_collision.md**: first contact must be exceptional phase 72,
  with explicit full blank-history and ordinary-channel guards;
* **../planar_structure/mass_four_escape.md**, Sections 1–3: the exposed
  southwest-corner geometry, reproved in Section 3 above.

The finite exact data and checkers are:

| Obligation | Checker and certificate |
| --- | --- |
| Complete canonical one-bit scattering at all ages | `../../ant_continuation/restore_one_bit_certificate.py`, `one_bit_certificate_restored.json`, and independent `verify_one_bit_independent.cpp` in that directory |
| First frontier, ordinary half-plane and axis guards, retained blank history | `mass4_first_collision.py` and `mass4_first_collision_audit.json` |
| Four-corner prescribed word for every n>=200, both parent tails, and final infinite tail | `../planar_structure/certify_exceptional_rectangle.py`, `exceptional_rectangle_template.json`, `exceptional_rectangle_affine_certificate.json`, and `exceptional_affine_fields.json.gz` |
| Affine interval-parity proof engine and literal ant conventions used by that checker | `../../ant_continuation/wake_clock/certify_four_scatterer_prefix.py` and its local support module `single_blocks.py`; `../../ant_continuation/ant_exact.py` |
| Exact read-set extrema and rotated ordinary guard constants | `mass4_later_collision_guards.py` and `mass4_later_collision_guards_audit.json` |
| Literal phase-correct cores, phase-zero P13 comparison, and XOR archive vanishing on all incoming rays | `audit_exceptional_stage_cores.py` and `exceptional_stage_core_audit.json` |

The affine-field checker represents the complete board as XORs of affine
points and finite diagonal segments. A finite word is checked by its exact
first-read color constraints and flip parity. For a repeated word, each old
point or segment contributes an exact interval of epochs on each phase ray;
earlier repetitions of the same word contribute the appropriate final
intervals. Cancellation of all affine interval boundaries proves every
required read for all epochs and every n>=200. The infinite-tail check
includes the unbounded final epoch interval. Any parameter-dependent change
of affine ordering, isolated collision, or unhandled parity class aborts
the checker rather than being extrapolated past. All arithmetic in these
proof checks is integer or exact rational arithmetic.

These are computer-assisted certificates checked in this research workspace,
not a claim of a new independently rebuilt Lean formalization. The prior
canonical scattering results and clock construction are attributed in the
linked prerequisite notes; no publication-priority claim is made here.
