# Finite white components give bounded internal episodes

**Status (22 October 2026): proved.** This is a reduction for every finite-support
classical Langton ant. It does not prove eventual translation or the period-104
highway. Its unresolved part is the dynamics along the unbounded white component.

## 1. Coordinates and the dual edge walk

Write the physical ant state as `(B,p,h)`, with `N,E,S,W = 0,1,2,3`, white giving
a right turn and black a left turn. Normalize the invariant checkerboard sector
so that even physical cells receive vertical arrivals. A lattice translation or
a quarter-turn puts either sector into this convention.

The Tait representation in [Jillhewar, *Finite-Support Periodic Highways*,
Section 4](https://github.com/Atharva12456/langtons-ant-highway/blob/main/paper/main.tex)
uses the odd-parity plaquettes as primal vertices and black cells as primal
edges. We use the planar dual: even-parity plaquettes are vertices and a dual
edge is present exactly when its physical cell is white. Identify an even
plaquette with lower-left corner `(a,b)` with

\[
  (u,v)=((a+b)/2,(a-b)/2)\in\mathbb Z^2.
\]

At a physical cell `p=(x,y)`, the associated dual bond has endpoints

\[
 e_p^*=\begin{cases}
 \{((x+y)/2-1,(x-y)/2),((x+y)/2,(x-y)/2)\},&x+y\text{ even},\\
 \{((x+y-1)/2,(x-y-1)/2),((x+y-1)/2,(x-y+1)/2)\},&x+y\text{ odd}.
 \end{cases}
\]

Thus the dual graph is an ordinary square lattice. The ant's active dual vertex
`a_t` is the plaquette on the left of its incoming directed edge. In physical
plaquette coordinates it is respectively

| Incoming heading | Left plaquette lower-left corner |
| --- | --- |
| N | `(x-1,y-1)` |
| E | `(x-1,y)` |
| S | `(x,y)` |
| W | `(x,y-1)` |

The active vertex is always one endpoint of the addressed bond `e_p^*`. Direct
substitution in the ant rule proves the following exact update:

* **White / right:** cross the present dual bond to its other endpoint and delete
  that bond.
* **Black / left:** insert the absent dual bond and keep the same active dual
  vertex.

The next addressed bond is determined by the new heading. No planar drawing or
assumption about the frozen active contour is needed for these statements.

## 2. The invariant finite set during an internal episode

Let `D_t` be the dual white graph. Since only finitely many bonds are absent,
`D_t` has a unique infinite connected component. Define

\[
 S_t=\{v:v\text{ belongs to a finite component of }D_t\},
 \qquad W_t=\text{the component of }a_t\text{ in }D_t.
\]

The set `S_t` is finite. Suppose `W_s` is finite, and let

\[
 \tau=\inf\{j\ge1:W_{s+j}\text{ is infinite}\}.
\]

Initially allow `tau=infinity`. Let `K` be the connected component of `a_s` in
the **ordinary nearest-neighbor graph induced by the vertex set `S_s`**, with
all ordinary bonds restored for this definition. Several distinct white
components can therefore lie in one `K`.

**Theorem 1.** For all `0 <= j < tau`:

1. `S_{s+j}=S_s` exactly.
2. `a_{s+j}` and its white component `W_{s+j}` lie in `K`.
3. Every update before the exit update toggles a bond with both endpoints in
   `K`; every bond leaving `K` is absent/black and stays so.
4. The exit update inserts one boundary bond of `K`. More precisely, its other
   endpoint is in the infinite white component and
   `S_{s+tau}=S_s \ W_{s+tau-1}`.

**Proof.** A white update deletes a bond inside the active finite component.
It can split that component but cannot change which vertices belong to finite
components. The new active vertex is the other endpoint, still in `S_s`. A
black update adds a bond incident to the active component. Until the exit,
its other endpoint is in a finite component too; the update merges finite
components or creates an internal cycle, again leaving `S` unchanged.
Each such active-vertex move or component merger stays in the same ordinary
connected component `K` of `S_s`. If a bond incident to `K` has its other
endpoint outside `K`, that endpoint cannot belong to `S_s`, by the definition
of `K`. Such a bond is therefore absent while `S=S_s`; inserting it is exactly
an exit to the infinite white component. Only the active white component is
then absorbed into the infinite component. This proves all assertions,
including the statement about the first possible exit. ∎

The theorem includes active clockwise contours nested inside a finite white
region. A criterion based only on clockwise versus counterclockwise orientation
would not suffice.

## 3. Size and state-count bounds

Put `E=|B_s|`, `N=|K|`, and let `m` be the number of ordinary bonds with both
endpoints in `K`. Every boundary bond of `S_s` is absent, so

\[
 |\partial S_s|\le E.
\]

For every finite set `A` of square-lattice vertices, if it occupies `r` rows and
`c` columns, its edge boundary has at least `2r+2c >= 4 sqrt(|A|)` bonds.
Consequently

\[
 |S_s|\le E^2/16,\qquad N\le E^2/16,\qquad m\le2N.
\]

There are exactly four compatible directed ant edges with a specified left
dual vertex. Before exit, all exterior colors are fixed. There are at most
`4N 2^m` distinct complete states available during the episode. A repeated
complete state would be a periodic bounded orbit. The unboundedness theorem,
or the strictly increasing integer clock below, rules this out. Thus

\[
 \boxed{\tau\le4N2^m\le4N2^{2N}.}
\]

The bound includes the exit update: if the `tau` pre-exit states are distinct,
there are at most `4N2^m` of them.

## 4. A sharper bound using a one-dimensional clock

Let the bounding rectangle of `K` in dual coordinates have sides `a` and `b`
(numbers of occupied coordinate levels, including endpoints). Since `K` is
connected, each intermediate coordinate level is occupied. Its boundary has
at least `2(a+b)` bonds, hence

\[
 2(a+b)\le|\partial K|\le E,
 \qquad r:=\min(a,b)\le E/4.
\]

The [Ke integer clock](https://github.com/kehao95/langtons-ant-core/blob/main/clock_escape/PROOF.md)
for `s=x+y-c` has

\[
 f(s)=3^{|s|}-1,\qquad
 J(s,e)=\begin{cases}\tfrac12f(s),&es\ge0,\\
 -\tfrac32f(s),&es<0,\end{cases}
\]

\[
 \Theta_c(B,p,h)=-\sigma\sum_{z\in B}(-1)^{z_x+z_y}f(z_x+z_y-c)
                 +J(p_x+p_y-c,\epsilon(h)),
\]

where `epsilon(N)=epsilon(E)=1`, `epsilon(S)=epsilon(W)=-1` and `sigma` is
the invariant sector. Every update increases this integer by at least one.
Rotating the coordinates gives the same assertion for `x-y-c`.

If `K` has `u` coordinates from `u0` through `u1`, put `c=u0+u1+1`. Every
internal dual bond corresponds to a physical cell with `|x+y-c| <= a-1`;
every possible pre-exit ant pose has `|x+y-c| <= a`. The `m` mutable field
terms therefore have total range at most `m(3^(a-1)-1)`. The head term has
range at most `2(3^a-1)`. All exterior field terms are constant and cancel
when clocks at two pre-exit states are compared. There are `tau-1`
internal-to-internal updates, so

\[
 \tau\le m(3^{a-1}-1)+2(3^a-1)+1.
\]

For the `v` coordinates from `v0` through `v1`, use `c=v0+v1` in the rotated
`x-y` clock. This gives the same bound with `b`. Therefore

\[
 \boxed{\tau\le m(3^{r-1}-1)+2(3^r-1)+1,
 \quad r=\min(a,b)\le E/4.}
\]

In particular, one may replace `r` by `floor(E/4)` and `m` by
`floor(E^2/8)` to obtain a bound using entry mass alone. An internal episode
requires `E>=4`, so these exponents are nonnegative. The direct geometric
bound is preferable when the shape of `K` is known.

## 5. Consequences and the remaining obstruction

**Corollary 2.** Every finite-support orbit reaches states whose active dual
vertex lies in the infinite white component infinitely often. A finite white
region cannot trap the ant forever, even if it contains many nested frozen
contours or shares a boundary with other finite white regions.

**Proof.** If only finitely many such states existed, every sufficiently late
state would begin an infinite internal episode, contradicting either bound. ∎

**Corollary 3.** If an orbit has infinitely many states of black mass at most
`M`, it also has infinitely many external states with a bound on mass depending
only on `M`. If the low-mass heads lie in a fixed bounded set, these external
heads lie in a fixed bounded set as well.

**Proof.** Leave an already external state unchanged. Otherwise advance to the
first external state. The episode length is bounded by the formula in Section
4 with `E<=M`; each step changes mass by one. Spatial displacement is bounded
either by episode length or by the diameter of its fixed `K` and the final
exit step. An infinite set of starting times cannot map into finitely many exit
times because all such intervals have uniformly bounded length. ∎

This reduces both a possible non-highway orbit and a possible bounded-mass
subsequence to the **outer interface**. It does not prohibit repeated returns
along that interface. At external states, additions and deletions can still
split and merge primal components, create new finite white regions, or absorb
old ones. None of those operations is excluded by this theorem.

## 6. Attribution and verification

The medial/Tait correspondence and frozen-loop surgery are existing results;
the present contribution is the constancy of the entire finite-white vertex
set during an internal episode, its confinement to one ordinary component,
and the resulting entry-mass bounds. The exponential clock itself is an
existing result used as a lemma. No novelty claim is made beyond this
explicitly stated deduction, pending a broader literature check.

`audit_white_episodes.py` independently implements the physical ant and the
dual graph. It checks the coordinate update, the invariant finite set on
sampled full orbits, and every internal coloring and compatible starting pose
for small rectangular finite regions. `white_episode_audit.json` records the
exact counts and observed maxima. These finite checks audit conventions;
the proof above establishes the all-size claims.
