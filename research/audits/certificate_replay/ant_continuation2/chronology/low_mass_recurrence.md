# A sharp clock-forcing lemma and eventual black mass at least four

Status: analytic results for every finite black seed of the ordinary Langton
ant. The finite audits described below pass. This does not prove eventual
highway formation, does not prove capture from every three-black seed, and does
not prove that the black mass tends to infinity.

Use the conventions of **axial_separator_proof.md**: headings \(N,E,S,W\), white
turns right, black turns left, flip before moving. The complete state is
\(X_t=(B_t,p_t,h_t)\), its mass is \(M_t=|B_t|\), and its invariant sector is
\(\sigma=(-1)^{p_t^x+p_t^y}\) for a vertical heading and the negative of this for
a horizontal heading.

## 1. Four established critical clock components

Put \(z(x,y)=x+y\), \(u(x,y)=x-y\), and \(\chi(x,y)=(-1)^{x+y}\). Set

\[
e_z(N)=e_z(E)=1,\quad e_z(S)=e_z(W)=-1,
\]

\[
e_u(E)=e_u(S)=1,\quad e_u(W)=e_u(N)=-1,
\qquad
a(1)=\tfrac12,\quad a(-1)=-\tfrac32.
\]

The four rational-valued potentials are

\[
\begin{aligned}
\Psi_{z,+}(X)&=-\sigma\sum_{q\in B}\chi(q)3^{z(q)}
                  +a(e_z(h))3^{z(p)},\\
\Psi_{z,-}(X)&=-\sigma\sum_{q\in B}\chi(q)3^{-z(q)}
                  +a(-e_z(h))3^{-z(p)},\\
\Psi_{u,+}(X)&=\sigma\sum_{q\in B}\chi(q)3^{u(q)}
                  +a(e_u(h))3^{u(p)},\\
\Psi_{u,-}(X)&=\sigma\sum_{q\in B}\chi(q)3^{-u(q)}
                  +a(-e_u(h))3^{-u(p)}.
\end{aligned}
\tag{1}
\]

These are the one-sided critical components of Hao Ke's clock construction,
already recorded with source links and exact checks in
**../../ant_continuation/wake_clock/proof_notes.md**, Section 3. They are not new
clock definitions in this continuation. Direct substitution in the local
heading/color cases gives

\[
\Delta\Psi_{v,+}=
\begin{cases}
4\,3^{v(p)},&e_v(h)=-1,\ e_v(h')=1,\\
0,&\text{otherwise},
\end{cases}
\tag{2}
\]

\[
\Delta\Psi_{v,-}=
\begin{cases}
4\,3^{-v(p)},&e_v(h)=1,\ e_v(h')=-1,\\
0,&\text{otherwise},
\end{cases}
\qquad v=z,u.
\tag{3}
\]

Exactly one of the four increments is positive on each update. Each component
is nondecreasing, but it can be negative and need not diverge on a general
escaping orbit. The sign reversal between the \(z\)- and \(u\)-field sums in
(1) is essential.

## 2. The sharp forcing lemma

**Theorem 1.** If a finite state has mass at most \(K\), then each of the four
clock increment types in (2)–(3) occurs among the next \(2K+4\) updates.
The constant is sharp: for every \(K\), some state of mass \(K\) avoids a
specified increment type for \(2K+3\) updates.

### Proof

It is enough, by rotation, to forbid the increment
\(e_z:-1\longrightarrow+1\). Consider an initial trajectory segment in which
this increment never occurs. Its \(e_z\)-sequence is first \(+1\) and then
\(-1\), with at most one \(+1\longrightarrow-1\) switch. Either run may be empty.
While \(e_z=+1\), the trajectory is a northeast staircase with headings
alternating \(N,E\). While \(e_z=-1\), it is a southwest staircase with headings
alternating \(S,W\).

We first show that every **read cell** in such a segment is distinct.

If there is no switch, strict monotonicity of \(z\) makes this immediate.
Otherwise, let the switch occur on update \(a\), so that there have been \(a\)
northeast updates. If \(a=0\) or \(a=1\), the southwest staircase has no cell in
common with the short northeast prefix. If \(a\ge2\), the first southwest cell
is new. Were the southwest staircase to continue for a second move, it would
arrive at

\[
p_{a+2}=p_{a-2}.
\tag{4}
\]

Indeed, the last two northeast moves and the first two southwest moves have
opposite displacement vectors in the opposite order. The incoming heading at
this return is opposite to its earlier incoming heading. Continuing on the
southwest staircase would therefore require the **same turn** as at the first
read of \(p_{a-2}\): rotating both incoming and outgoing headings by \(180^\circ\)
does not change right versus left. That cell has been read once in between
these comparisons and has flipped. The same turn is impossible. Its actual next
update is the forbidden \(-1\longrightarrow+1\) switch.

Thus a segment avoiding that switch can end at this repeated cell, but cannot
read it. All its read cells are distinct.

Every left turn in the segment consequently reads a cell that was black at
the start. Hence

\[
L\le K.
\tag{5}
\]

Within either constant-sign staircase the turns alternate right and left.
The complete turn word consists of two alternating runs and at most one
intervening switch turn. Each alternating run has \(R-L\le1\), and the switch
contributes at most one more. Therefore

\[
R-L\le3,\qquad R+L=2L+(R-L)\le2K+3.
\tag{6}
\]

An increment-avoiding segment cannot have \(2K+4\) updates. Rotation gives the
same conclusion for every clock type.

For sharpness, start at \((0,0),N\) with

\[
B_K=\{(j+1,j):0\le j<K\}.
\tag{7}
\]

The literal first \(2K+3\) turns are

\[
(\mathrm{RL})^K\mathrm{RRR}.
\tag{8}
\]

They avoid the \(z,+\) increment. The next update is the first such increment.
This construction includes \(K=0\), where the three initial right turns are
followed by \(W\longrightarrow N\). ∎

**Scope.** The theorem bounds waiting from a state of finite current mass. It
does not assume that the mass stays below \(K\) during the block. Its conclusion
is occurrence of each increment type; the numerical increment may be small
when the read cell is far from the chosen coordinate origin.

## 3. Infinite low-mass recurrence forces all four clocks to diverge

**Theorem 2.** Fix a finite orbit and an integer \(K\). If \(M_t\le K\) at
infinitely many times, all four potentials in (1) tend to \(+\infty\).

**Proof.** The sharp midpoint bound proved in **axial_separator_proof.md** says

\[
|B_s\triangle B_t|
\ge2\left\|
\left(p_t-\tfrac12d_{h_t}\right)
-\left(p_s-\tfrac12d_{h_s}\right)
\right\|_\infty.
\tag{9}
\]

At two mass-at-most-\(K\) checkpoints, this gives incoming-midpoint distance at
most \(K\). Consequently the head positions at all such checkpoints lie in a
fixed finite box.

Set \(L=2K+4\). Choose an infinite subsequence of checkpoints \(t_j\) for which
the blocks \([t_j,t_j+L)\) are disjoint. Each block starts with mass at most
\(K\), so Theorem 1 supplies a positive increment of every clock in that block.
All read cells in all these blocks lie in one fixed finite enlargement of the
checkpoint-head box: the block has only \(L\) unit steps.

There is therefore a constant \(\delta>0\), independent of \(j\), such that each
clock increases by at least \(\delta\) during every selected block. Explicitly,
if \(|z|,|u|\le R\) at all checkpoint heads, one may use

\[
\delta=4\,3^{-(R+L-1)}.
\tag{10}
\]

The monotonicity (2)–(3), including between these blocks, gives divergence of
all four components. No assumption that their initial values are positive is
needed. ∎

This is stronger than merely saying that the components remain above fixed
initial lower bounds. That distinction matters: sparse remote endpoint
families can satisfy all lower bounds while some clock components approach a
finite limit.

## 4. Every finite orbit is eventually above mass three

**Theorem 3.** For every finite black seed, only finitely many times satisfy
\(M_t\le3\). Equivalently,

\[
\boxed{\liminf_{t\to\infty}M_t\ge4.}
\tag{11}
\]

**Proof.** Suppose instead that there are infinitely many such times. The
checkpoint heads lie in a fixed finite box by (9), and Theorem 2 says that all
four clocks tend to \(+\infty\).

For a black cell \(q\), put

\[
b(q)=-\sigma\chi(q)\in\{-1,1\}.
\]

The field sums of the \(z\)-clock pair have coefficient \(b(q)\); those of the
\(u\)-clock pair have coefficient \(-b(q)\).

With at most three black cells, one of the two sign classes contains at most
one cell. Suppose first that there is at most one \(b=+1\) cell. The positive
field contribution to the \(z\)-pair is then at most \(3^{z(q)}\) and
\(3^{-z(q)}\), respectively, or zero if the class is empty. At least one of
these two numbers is at most 1. Every other field summand is nonpositive.
Hence at least one \(z\)-field sum is at most 1. If instead the class \(b=-1\)
has at most one cell, the identical argument applies to the \(u\)-pair.

The head terms are uniformly bounded above on the finite checkpoint-head box.
For instance, if \(|z(p)|,|u(p)|\le R\) there, every head term is at most
\(\tfrac12\,3^R\). Thus every mass-at-most-three checkpoint satisfies

\[
\min\{\Psi_{z,+},\Psi_{z,-},\Psi_{u,+},\Psi_{u,-}\}
\le1+\tfrac12\,3^R.
\tag{12}
\]

All four components cannot diverge while (12) holds at infinitely many times.
This contradiction proves (11). ∎

The argument is independent of any exhaustive capture calculation for
one-black, two-black, or three-black seeds. It proves eventual exclusion of
mass at most three on **every** finite-seed trajectory. It does not establish
what happens to a trajectory once its mass stays at least four.

## 5. Why four cells already evade this endpoint argument

The checkerboard counting step in Theorem 3 cannot be extended to four cells
without another dynamical restriction. Here is an exact endpoint family that
shows the issue, including the axial mod-four charges.

For \(n\ge1\), take the head \((0,0),N\) and the four rectangle corners

\[
B_n=\{-2n,\,2n+1\}\times\{-2n+1,\,2n+2\}.
\tag{13}
\]

The two selected \(x\)-coordinates have opposite parity, as do the two selected
\(y\)-coordinates. Thus each occupied row and column has signed mass zero.
The southwest corner has checkerboard sign \(-1=-\sigma\). Factoring the four
monomials shows that every one-sided critical field contribution is positive,
increases with \(n\), and tends to infinity. For example,

\[
-\sum_{q\in B_n}\chi(q)3^{x(q)+y(q)}
=(3^{2n+1}-3^{-2n})(3^{2n+2}-3^{-2n+1}).
\tag{14}
\]

The other three formulas use the analogous positive spans in the negative
\(x\)- and/or \(y\)-directions. The rectangular convex hulls are nested.

This family even passes simultaneous radial-clock increase at every center.
For \(f(v)=3^{|v|}\), put \(d_n=4n+1\). In the \(z\)-normal, its signed field
term in the integer radial clock is

\[
f(2-d_n-c)+f(2+d_n-c)-2f(2-c),
\tag{15}
\]

and in the \(u\)-normal it is

\[
f(-1-d_n-c)+f(-1+d_n-c)-2f(-1-c).
\tag{16}
\]

The head term is fixed. Strict convexity of the piecewise exponential
\(f\) makes (15) and (16) strictly increase with \(d_n\), for every fixed center
\(c\). These are complete finite endpoint states with four black cells, not
states proved reachable successively on one orbit.

No finite counterexample, renewable circuit, or actual low-mass recurrence
follows from (13). The family only shows that the current endpoint charges,
convex-hull tests, and centered clock inequalities are compatible with
unbounded four-cell memory when actual path construction is omitted.

## 6. Exact verification

**forcing_and_small_mass.py** uses integer and exact rational arithmetic. The
recorded run in **forcing_and_small_mass_audit.json** passes:

* all 32 parity/heading/read-bit local cases for the exact four clock updates;
* all feasible increment-avoiding symbolic turn plans for \(K=0,\ldots,16\),
  all four initial headings, and all four forbidden clock types: 272 cases,
  visiting 12,992 symbolic nodes;
* the sharp family (7)–(8) for \(K=0,\ldots,64\);
* 40,400 first-increment checks at 10,100 literal finite-seed interval starts.

The symbolic audit assigns initial colors on first reads and enforces every
subsequent flip; it does not treat an arbitrary turn word as a legal ant trace.
The general proofs above, rather than these finite ranges, establish the
unbounded-parameter statements.

