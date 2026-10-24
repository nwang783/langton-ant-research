# Axial mod-four charges and endpoint mass bounds

Status: proved consequences for every finite trajectory of the ordinary two-color
Langton ant. These results do not prove eventual highway formation, and the
running-maximum estimate below does not prove that the instantaneous black mass
tends to infinity.

## 1. Conventions and relation to the existing paper

A state is \(X=(B,p,h)\), where \(B\subset\mathbb Z^2\) is the complete finite set
of black cells, \(p=(x,y)\) is the head cell before the next read, and

\[
d_N=(0,1),\quad d_E=(1,0),\quad d_S=(0,-1),\quad d_W=(-1,0).
\]

At a white cell the ant turns right, at a black cell it turns left; it then flips
that cell and moves one unit in the new heading. The headings are encoded
\(N,E,S,W=0,1,2,3\). We write \(X_t=(B_t,p_t,h_t)\) and \(M_t=|B_t|\).

The checkerboard/heading sector

\[
\sigma=(-1)^{x+y}
\begin{cases}1,&h\in\{N,S\},\\-1,&h\in\{E,W\}\end{cases}
\]

is invariant: both checkerboard parity and the heading axis change on every
update.

**Attribution.** Atharva Jillhewar's *Finite-Support Periodic Highways of Langton's
Ant: Necessary Conditions, Transverse Exclusions, and Exact Search*, dated
17 August 2026, already proves a general additive-charge cocycle proposition.
The source supplied for this continuation is
`../planar_structure/source_paper_main.tex`, Proposition `prop:cocycle`.
The weight \(w_r(x,y)=(-1)^x\mathbf1_{y=r}\pmod4\) satisfies its four-corner
condition, so the invariant below is an explicit specialization of that
framework. Its Section `sec:residue` applies related charges to periodic wake
strands. We claim no priority for a new invariant. The purpose here is to give
explicit endpoint corrections and apply them to arbitrary finite intervals,
support changes, and mass bounds. The direct passage proof in Section 3 is
self-contained.

## 2. The complete line invariant, including endpoint corrections

For a horizontal row \(r\), put

\[
S_r(B)=\sum_{(x,r)\in B}(-1)^x,
\qquad \kappa_r=\sigma(-1)^r.
\]

Define \(G_r(p,h)\in\mathbb Z/4\mathbb Z\) by the following table.

| Position of the head | \(N\) | \(E\) | \(S\) | \(W\) |
| --- | ---: | ---: | ---: | ---: |
| \(p_y<r\) | 0 | 0 | 0 | 0 |
| \(p_y=r\) | 0 | \(\kappa_r\) | 2 | \(-\kappa_r\) |
| \(p_y>r\) | 2 | 2 | 2 | 2 |

Then, for each fixed row \(r\),

\[
\boxed{S_r(B_t)-G_r(p_t,h_t)\pmod4\quad\text{is independent of }t.}
\tag{1}
\]

For a vertical column \(c\), put

\[
T_c(B)=\sum_{(c,y)\in B}(-1)^y,
\qquad \kappa_c=\sigma(-1)^c.
\]

The corresponding correction is

| Position of the head | \(N\) | \(E\) | \(S\) | \(W\) |
| --- | ---: | ---: | ---: | ---: |
| \(p_x<c\) | 0 | 0 | 0 | 0 |
| \(p_x=c\) | \(\kappa_c\) | 0 | \(-\kappa_c\) | 2 |
| \(p_x>c\) | 2 | 2 | 2 | 2 |

Writing this correction as \(F_c\),

\[
\boxed{T_c(B_t)-F_c(p_t,h_t)\pmod4\quad\text{is independent of }t.}
\tag{2}
\]

### Direct verification of (1)

If the read cell is not on row \(r\), its signed row mass is unchanged. When the
step also ends off the row, the head stays on the same side and \(G_r\) is
unchanged. When it enters the row from below, its new heading is \(N\), so both
the old and new corrections are 0. Entry from above has new heading \(S\), so
both corrections are 2.

It remains to read a cell \(p=(x,r)\). Write \(w=(-1)^x\) and \(b=1_{p\in B}\).
The change of \(S_r\) is \(w(1-2b)\). If the old heading is vertical then
\(\kappa_r=w\); if it is horizontal then \(\kappa_r=-w\). Substitution into the
table gives

\[
G_r(p_{t+1},h_{t+1})-G_r(p_t,h_t)
\equiv w(1-2b)\pmod4
\]

for each of the eight choices of heading and bit. For example, \(N\) at white
changes (0) to \(\kappa_r=w\), while \(E\) at black changes
\(\kappa_r=-w\) to 2, whose difference \(2+w\) is \( -w\pmod4\).
This proves (1). A quarter-turn of coordinates proves (2); its displayed table
can also be checked in the same eight cases.

## 3. Axial separator theorem

**Theorem.** Let \(s<t\). If neither endpoint head is on horizontal row \(r\),
then

\[
S_r(B_t)-S_r(B_s)
\equiv 2\mathbf1\{p_s,p_t\text{ are on opposite sides of row }r\}\pmod4.
\tag{3}
\]

The analogous statement holds for a column, with \(T_c\) in place of \(S_r\).

This follows at once from (1), but there is a particularly short geometric
proof. Every complete passage through a horizontal row reads two adjacent cells
consecutively: it enters vertically, turns horizontally, and turns vertically
again to leave the row. Endpoint heads off the row ensure that all row reads in
the interval are partitioned into such complete passages.

Suppose the two cells are \(k,k+1\), and their bits just before the passage are
\(b_k,b_{k+1}\). The change of signed row mass is exactly

\[
(-1)^k(1-2b_k)+(-1)^{k+1}(1-2b_{k+1})
=2(-1)^k(b_{k+1}-b_k).
\tag{4}
\]

If the bits agree, the two turns agree and the passage returns to its entry
side; its signed mass change is 0. If the bits differ, the turns differ and the
passage exits on the opposite side; its change is \(2\pmod4\). The parity of the
number of transmissions is exactly the side difference of the endpoint heads.
This proves (3) for arbitrary initial row colors and arbitrary finite intervals.

**Consequences.**

* If an entire row has exactly the same colors at \(s\) and \(t\), endpoint heads
  off that row cannot be on opposite sides.
* Every row strictly between \(p_s^y\) and \(p_t^y\) contains at least two cells of
  \(B_s\triangle B_t\).
* If such a row is white at \(s\), it contains at least two black cells at \(t\).
  If it contains exactly two, their \(x\)-coordinates have the same parity.
* The same statements hold for columns.

The restriction to axial lines matters. Starting from an entirely white field
with head \((0,0),N\), at time 18 the head is \((-1,-1),S\), yet the entire
diagonal \(x+y=-1\), strictly between the endpoint heads, is white. At time 247
the head is \((4,-5),E\), yet the entire diagonal \(x-y=8\) is white. The complete
fields and literal-step checks are recorded in `axial_separator_audit.json`.

## 4. Sharp heading-corrected support-change bound

For an integer \(v\), let

\[
\delta_4(v)=\min(v\bmod4,\,4-(v\bmod4)).
\]

Each changed cell contributes \(+1\) or \(-1\) to a line's signed mass change.
Consequently, (1) gives the per-row bound

\[
|(B_s\triangle B_t)\cap(\mathbb Z\times\{r\})|
\ge\delta_4(G_r(p_t,h_t)-G_r(p_s,h_s)).
\tag{5}
\]

The analogous inequality holds for each column. Thus

\[
|B_s\triangle B_t|\ge\max\left\{
\sum_r\delta_4(G_r(t)-G_r(s)),
\sum_c\delta_4(F_c(t)-F_c(s))\right\}.
\tag{6}
\]

These two sums have simple exact formulas. Define

\[
\rho(h,g)=\min((h-g)\bmod4,(g-h)\bmod4),
\qquad m(X)=p-\tfrac12d_h.
\]

The point \(m(X)\) is the midpoint of the incoming edge. The row sum in (6) is

\[
\begin{cases}
|2(p_t^y-p_s^y)+d_{h_s}^y-d_{h_t}^y|,&p_s^y\ne p_t^y,\\
\rho(h_s,h_t),&p_s^y=p_t^y.
\end{cases}
\tag{7}
\]

The column sum is the same formula with \(x\) in place of \(y\).

To verify (7), suppose the lower endpoint row is \(y=a\), the upper endpoint row
is \(y=b>a\), with corresponding headings \(h_\ell,h_u\). Each of the \(b-a-1\)
strictly intermediate rows contributes 2. The lower row contributes

\[
\delta_4(2-G_a(h_\ell))=1+d_{h_\ell}^y,
\]

and the upper row contributes

\[
\delta_4(G_b(h_u))=1-d_{h_u}^y.
\]

Their sum is \(2(b-a)+d_{h_\ell}^y-d_{h_u}^y\), giving the first case of (7).
If the endpoint rows coincide, their common correction table is a four-cycle
in heading, giving exactly \(\rho(h_s,h_t)\).

Since \(\rho(h_s,h_t)\ge|d_{h_s}^y-d_{h_t}^y|\), and likewise in \(x\),
(6) implies

\[
\boxed{|B_s\triangle B_t|\ge
2\|m(X_t)-m(X_s)\|_\infty.}
\tag{8}
\]

There is no additive endpoint error in (8). It is sharp for every single
update: exactly one cell changes, and each coordinate of the incoming midpoint
changes by \(1/2\) in absolute value.

## 5. What low-mass recurrence would have to look like

Fix \(K\). For any two times \(s,t\) satisfying \(M_s,M_t\le K\),

\[
\|m(X_t)-m(X_s)\|_\infty
\le\tfrac12|B_s\triangle B_t|\le K.
\tag{9}
\]

Hence all incoming midpoints at mass-at-most-\(K\) checkpoints have coordinate
diameter at most \(K\), regardless of the size or diameter of the initial seed.
Their head cells have coordinate diameter at most \(K+1\), so they occupy at
most \((K+2)^2\) lattice cells. Only two headings are compatible with the fixed
sector at any one cell.

Thus an infinite sequence of mass-at-most-\(K\) checkpoints would contain an
infinite subsequence with exactly the same head position and heading. All row
and column charge residues would be the same along that subsequence. This
narrows the possible recurrence to changes in remote memory with a recurrent
head pose. It does not by itself exclude that possibility: the endpoint bounds
do not bound the positions of black cells at isolated low-mass checkpoints.

For comparison with the earlier two-black endpoint constructions: if the
current head is far from the initial head while the whole black field contains
only two cells, (8) directly rules it out once the displacement exceeds the
finite initial-mass allowance. Satisfaction of all previously tested scalar
clock inequalities was not sufficient for reachability.

## 6. Explicit first-hit bound for the running black mass

Let \(m=M_0\), and suppose

\[
M_t\le K\quad(0\le t\le T),\qquad K\ge m.
\]

Set \(u=m+K\), and write \(a_i=2p_0^i-d_{h_0}^i\) for \(i=x,y\). By (8),
every head cell lies in the fixed integer rectangle

\[
Q=\prod_{i=x,y}\left[
\left\lceil\frac{a_i-u-1}{2}\right\rceil,
\left\lfloor\frac{a_i+u+1}{2}\right\rfloor
\right]\cap\mathbb Z^2.
\tag{10}
\]

One of \(a_x,a_y\) is odd and the other is even. Accordingly the two side
lengths of \(Q\), in lattice cells, are \(u+1\) and \(u+2\), in one order.
In particular

\[
A:=|Q|=(m+K+1)(m+K+2).
\tag{11}
\]

All reads up to time \(T-1\) occur in \(Q\). Thus outside \(Q\), the complete
field remains equal to \(B_0\). If \(m_{\rm out}=|B_0\setminus Q|\), there are at
most

\[
N_{K,m_{\rm out}}=\sum_{j=0}^{K-m_{\rm out}}\binom A j
\tag{12}
\]

possible complete color fields compatible with the mass bound. Terms beyond
\(A\), if any, are interpreted as zero.

We use the already established **no-coloring-repeat theorem**: the complete
field \(B_t\) cannot be identical at two distinct times. This is Proposition 2
of the Etse source supplied in the parent research, and also follows from the
exact path-hull lemma proved in the preceding continuation. For completeness,
the short geometric argument is as follows. For an interval of length at least
two the visited positions have a noncollinear convex hull, since every move
turns through a right angle. Choose a hull vertex other than the two endpoint
heads. It can have at most two neighboring visited cells, and those neighbors
must be adjacent directions. The invariant heading/checkerboard sector fixes
which incident edge is incoming and which is outgoing. Thus every read at that
vertex would have to make the same turn. Since its color flips, it can be read
only once, so the complete field changes there. An interval of length one
changes its read cell directly.

It follows that

\[
T+1\le N_{K,m_{\rm out}}\le
N_K(m):=\sum_{j=0}^{K}\binom{(m+K+1)(m+K+2)}j.
\tag{13}
\]

Equivalently, **the black mass exceeds \(K\) by update \(N_K(m)\)**. The bound
depends on the initial mass, but not on the initial support diameter. Counting
full states instead would give the weaker \(2A N_K(m)\), since the sector allows
only two headings per head cell; the no-coloring-repeat theorem removes this
unnecessary factor.

For fixed \(m\) and \(K\to\infty\), the elementary binomial estimate gives

\[
\begin{aligned}
N_K(m)&\le(K+1)(eA/K)^K,\\
\log N_K(m)&\le K\log K+K+O_m(\log K).
\end{aligned}
\tag{14}
\]

Consequently the running maximum satisfies

\[
\boxed{\max_{0\le t\le T}M_t\ge
(1-o(1))\frac{\log T}{\log\log T}}
\qquad(T\to\infty, M_0=m\text{ fixed}).
\tag{15}
\]

This is a universal quantitative escape from every fixed mass cap. It is a
running-maximum result. It neither proves \(M_t\to\infty\) pointwise nor bounds
how often a trajectory may return to small mass after reaching large mass.
No claim is made that the rate (15) is sharp, or that this application has
publication priority over existing results.

## 7. Exact audit

Run `python ant_continuation2/chronology/axial_separator.py` from the workspace
root. The verifier uses integer arithmetic throughout. It checks:

* all 32 choices of coordinate parity, heading, and read bit; these cover every
  local transition relevant to the correction tables;
* 5,000 intervals on 100 arbitrary finite-seed trajectories, retaining remote
  initial cells rather than discarding them;
* 1,000 intervals of the blank trajectory through update 30,000;
* each complete row/column invariant, each per-line changed-support bound, the
  exact sums (7), and the sharp midpoint inequality (8).

The recorded run passes 523,982 signed-line checks. The script also stores the
two complete diagonal-separator counterexamples and sample values of the
first-hit counting bound. These are consistency audits of the analytic proof,
not a substitute for it. The two files are `axial_separator.py` and
`axial_separator_audit.json` in this directory.

