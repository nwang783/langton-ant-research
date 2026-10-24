# Mass-four recurrence: only the exceptional first-collision channel survives

Status: proved reduction using the analytic low-mass results and a finite exact
full-field scattering audit. It does not exclude the exceptional channel and
does not by itself prove that mass four occurs only finitely often.

The accompanying verifier is **mass4_first_collision.py**; its output is
**mass4_first_collision_audit.json**. It replays the needed ten cases from the
previously reconstructed canonical one-bit certificate, including complete
endpoint fields, infinite standard tails, and all-age old-tail guards.

## 1. A hypothetical infinite mass-four subsequence

Assume one finite-seed trajectory has infinitely many times of black mass four.
By the results in **low_mass_recurrence.md**:

1. all four one-sided critical clocks diverge to \(+\infty\);
2. the checkpoint heads lie in a fixed finite box;
3. after passing to a subsequence, the head position and heading are fixed.

Translate and rotate this fixed pose to \((0,0),N\). This is an exact symmetry
of the ant, and its sector is then \(\sigma=+1\). Write

\[
z=x+y,\quad u=x-y,\quad b(q)=-\chi(q),\quad\chi(q)=(-1)^{x+y}.
\]

At sufficiently late checkpoints there are exactly two cells with \(b=+1\) and
two with \(b=-1\). Otherwise the checkerboard argument proving eventual mass at
least four would bound one clock component.

Moreover, after labeling within each class,

\[
z(q_+^-)\to-\infty,\qquad z(q_+^+)\to+\infty,
\]

\[
u(q_-^-)\to-\infty,\qquad u(q_-^+)\to+\infty.
\tag{1}
\]

For example, divergence of \(\Psi_{z,+}\), with bounded head correction,
forces the maximum \(z\)-coordinate among the two positive field terms to
infinity. Divergence of \(\Psi_{z,-}\) forces their minimum to minus infinity.
The \(u\)-pair gives the other two limits. Thus **all four black cells escape
every fixed compact set**, while the checkpoint pose stays fixed.

## 2. The first collision with the blank orbit

Starting at any such checkpoint, compare the actual orbit with the ant from
the entirely white plane at the same pose. They agree until the blank orbit
first reads one of the four initially black cells.

A collision must occur. If none occurs, complete-field first-difference
coupling makes the actual future equal the blank standard highway with four
untouched added cells. Its black mass tends to infinity, contradicting the
assumed infinite later mass-four checkpoints.

The blank orbit has a certified standard tail from update 9977, at pose
\((-15,10),W\), with the supplied word \(W\) and drift \((-2,-2)\). Because all
four input cells escape every compact set, the first collision occurs
arbitrarily far along this tail. Its cell \(q\) therefore satisfies

\[
z(q)\to-\infty,\qquad u(q)\text{ belongs to one fixed finite set}.
\tag{2}
\]

The \(b=-1\) cells cannot satisfy (2), by (1). Consequently \(q=q_+^-\), so

\[
\chi(q)=-1,\qquad q_x,q_y\to-\infty.
\tag{3}
\]

The invariant sector then makes the incoming heading at \(q\) horizontal.
This excludes twelve of the twenty-two first-read frontier phases.

### Exact frontier audit

The verifier reconstructs the blank field at update 9977 and checks its entire
future against \(W\). It computes first-read frontier phases by exact integer
ray comparisons: a phase cell is excluded when an earlier phase or period has
already read it, and all finite prefix hits are checked. From period depth
2 onward, the resulting first-read classification is stable.

The ten horizontal-arrival phases are

\[
\boxed{14,28,32,38,46,56,60,62,70,72.}
\tag{4}
\]

The corresponding \(u\)-coordinates lie in
\(\{-27,-25,-23,-21,-19\}\), two phases for each coordinate. In particular the
remaining exceptional phase 72 has

\[
q=(-17,2)+n(-2,-2).
\tag{5}
\]

The phase convention is the beginning of \(W\) at blank update 9977, not an
arbitrary cyclic relabeling.

## 3. Exact axial partners of the first collider

The signed row and column charges from **axial_separator_proof.md** are fixed
at the fixed checkpoint pose. Only finitely many rows or columns have nonzero
residue. Since both coordinates of \(q\) tend to minus infinity, its row and
column eventually have residue zero.

Each therefore contains at least two black cells. A row with one or three
black cells has odd signed mass and cannot have residue zero modulo four. A
row containing all four black cells would leave the column of \(q\) with only
one black cell, also impossible. Hence both the row and column of \(q\) contain
**exactly two** black cells. Their coordinate parities are opposite, since
their signed sum must be zero, rather than \(2\pmod4\).

The four-cell field therefore has the form

\[
\boxed{B=\{q,\ a=(q_x,t),\ c=(r,q_y),\ d\},}
\tag{6}
\]

where \(a,c\) have \(b=-1\), and \(d\) has \(b=+1\). By (1)–(2),

\[
|t-q_y|\to\infty,\qquad |r-q_x|\to\infty,\qquad z(d)\to+\infty.
\tag{7}
\]

No claim that all four points form a rectangle is needed. Nor is any sign
assumption on the two axial gaps needed for the ordinary-channel exclusion
below.

## 4. What the one-bit scattering certificate actually supplies

The canonical full field is the thirteen-black seed \(P\), with its entire
accumulated twelve-cell-per-period wake. At a fixed phase, its complete age-\(n\)
source differs from the checked age-\(N\) source only in older deposited wake
copies. The supplied all-age guard checks that these copies miss both the
finite recovery reads and every ray of the certified outgoing standard tail.
Thus the **complete future read trace**, in the impact frame, is identical
for every \(n\ge N\).

The verifier replays all ten relevant anchor records and rechecks these guards.
Here the directions have been rotated into the actual blank southwest frame.

| First phase | Age threshold \(N\) | Recovery updates | Outgoing drift |
| ---: | ---: | ---: | --- |
| 14 | 2 | 312 | \((-2,-2)\) |
| 28 | 13 | 6,448 | \((-2,-2)\) |
| 32 | 3 | 8,424 | \((-2,2)\) |
| 38 | 7 | 5,824 | \((-2,2)\) |
| 46 | 4 | 728 | \((2,-2)\) |
| 56 | 7 | 7,592 | \((-2,2)\) |
| 60 | 9 | 2,496 | \((-2,-2)\) |
| 62 | 12 | 7,384 | \((-2,2)\) |
| 70 | 4 | 8,528 | \((-2,-2)\) |
| 72 | 11 | 51,168 | \((2,2)\) |

These are certificate boundaries, not asserted earliest recovery times.

### Uniform guards for the nine ordinary channels

For any of the first nine rows of the table, let \(\mathcal R_q\) be the entire
post-impact read set of the canonical perturbed orbit, including its infinite
standard tail. The exact finite-footprint and ray calculations give

\[
z(v)\le z(q)+58\quad(v\in\mathcal R_q),
\tag{8}
\]

\[
(q_x+s,q_y)\in\mathcal R_q\Longrightarrow |s|\le31,
\tag{9}
\]

\[
(q_x,q_y+s)\in\mathcal R_q\Longrightarrow |s|\le34.
\tag{10}
\]

These are all-future bounds, uniformly for every canonical age above the
relevant threshold. For a tail ray \(q+\alpha+k\delta\), \(k\ge0\), an
intersection with an axial line through \(q\) fixes \(k\) by one coordinate
equation, since both coordinates of \(\delta\) are nonzero. The verifier checks
that exact solution, not a large finite sample of the tail. Bound (8) holds
because the outgoing ordinary drifts have \(z(\delta)\le0\).

## 5. Retaining and guarding the actual blank history

At the blank entry pose \((-15,10),W\), the rotated thirteen-black core is a
subset of the complete field of 715 black cells. The remaining set
\(H_E\), of size 702, is kept explicitly as a field difference. The audit finds

\[
-21\le z(v)\le35\qquad(v\in H_E).
\tag{11}
\]

The blank and canonical futures have the same standard read trace, so their
complete field difference remains \(H_E\) at every later matched age.

Just before the first collision \(q\), the actual field differs from the
current-cell-perturbed canonical source precisely by

\[
H_E\triangle\{a,c,d\}.
\tag{12}
\]

The three other original input bits have not yet been read. This is a complete
field identity; no history or scatter scar is removed.

For sufficiently late checkpoints, (7) and \(z(q)\to-\infty\) give

\[
|r-q_x|>31,\quad |t-q_y|>34,\quad
z(d)>z(q)+58,\quad z(q)+58<-21.
\tag{13}
\]

Equations (8)–(11) therefore prove that the entire canonical post-impact read
trace misses every cell in (12). First-difference coupling transfers its
complete future to the actual orbit. All scars and old wake cells remain in
the checked canonical field; the additional history is protected by the
explicit exclusion inequalities.

As a uniform depth sufficient for the history part of (13), \(n\ge18\) works
for all nine ordinary frontier phases. The other guards concern the actual
axial gaps and the fourth cell, rather than an assumed clean neighborhood.

## 6. The surviving first channel

**Theorem.** If a finite-seed orbit has infinitely many mass-four checkpoints,
then on every sufficiently late subsequence with one fixed normalized pose,
its first initially black collision with the blank orbit is on phase 72:

\[
q=(-17,2)+n(-2,-2),\qquad n\to\infty.
\tag{14}
\]

**Proof.** Sections 1–3 restrict the first collision to the ten phases (4) and
give the axial form and escaping gaps. Sections 4–5 turn any of the nine
ordinary phases into a permanent standard future. That future has unbounded
growing mass and hence cannot belong to an orbit with infinitely many later
mass-four checkpoints. Phase 72 is the only remaining case. ∎

Phase 72 has an outgoing northeast tail and may encounter the fixed historical
residue near the original head. Thus (8) fails for it, and this proof does not
discard that collision. The known one-black exceptional-channel theorem gives
a separate affine return to history, which is the next step for this
continuation. The three remaining input cells must be guarded again after
that return; a one-bit theorem is not automatically closed under further
collisions.

## 7. Verification scope and dependencies

The exact audit uses:

* the literal ant update and finite parity-breakpoint standard-tail verifier
  in **../../ant_continuation/ant_exact.py**;
* the previously reconstructed 739-record one-bit certificate in
  **../../ant_continuation/one_bit_certificate_restored.json**;
* fresh replays of all ten anchor cases used here, including their complete
  endpoint-field hashes and exact infinite old-tail exclusion tests;
* an independent reconstruction of the blank entry and all twenty-two
  first-read phase classes, with the twelve parity-incompatible classes
  explicitly removed.

The source certificate's SHA-256 and every numerical guard above are recorded
in **mass4_first_collision_audit.json**. The analytic arguments in Sections
1–3 convert hypothetical actual recurrence into the finite guarded cases;
the finite calculation alone would not establish that coverage.

