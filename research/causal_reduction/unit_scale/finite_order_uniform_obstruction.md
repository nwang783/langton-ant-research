# Finite-order uniform direction substitutions cannot be ant paths

23 October 2026, 05:09 UTC. Independently signed analytic application at 05:11 UTC.
This uses the independently signed `primitive_perron_clock_obstruction.md`.
No general Langton-ant theorem is asserted.

## Statement

Let phi be a fixed uniform substitution of length k>1 on the four absolute
movement directions E,N,W,S. Suppose net(phi(v))=A v for an integer matrix A
of finite order. No growing rooted power-limit of phi can be the movement
word of a Langton ant, even on an arbitrary initial coloring.

There is NO half-turn, quarter-turn covariance, heading-preservation, or
primitivity hypothesis. There is no upper bound on image length. The statement
is about one fixed uniform presentation, not arbitrary directive schedules or
occurrence-dependent choices. It does not rule out nonuniform presentations.

## 1. Reduce to an actual fixed word with spatial matrix I

If the claimed rooted limit uses a first-letter cycle, take the power that
fixes that actual rooted word. Then take a further common multiple with the
finite order of A. Write psi for the resulting substitution, K>1 for its
uniform length, and P=v_0 v_1 ... for the actual movement word. Thus

    psi(P)=P,                 net(psi(v))=v.

Only this actual phase is used; intermediate powers of the original
presentation need not be ant-legal. Each appearing image of psi is an actual
factor of P and hence alternates movement axes.

## 2. The exact adjacent-pair lift

Let S be the nonempty set of all consecutive direction pairs (u,v) occurring
in P, with u and v perpendicular. These are genuine pairs at positive read
times; the virtual initial incoming heading is not included or needed.

Put F(v)=first(psi(v)) and G(v)=last(psi(v)). For s=(u,v), whose second
coordinate has image psi(v)=w_0 ... w_(K-1), define

    chi(u,v) = (G(u),w_0), (w_0,w_1), ..., (w_(K-2),w_(K-1)).

There are exactly K pair states. This is precisely the sequence of read
states of the fine block psi(v) following psi(u) inside psi(P)=P. Therefore
all displayed pairs are perpendicular and belong to S. In particular S is
closed under chi, without requiring that any unused abstract pair be legal.

Each pair (a,b) is interpreted physically as one read with incoming heading
a, outgoing movement b, and its uniquely determined R/L turn. For a child
of chi(u,v), use its read position in the outgoing word psi(v) as its offset.
The complete outgoing word of chi(u,v) is psi(v), so its net displacement is
v, the displacement of its parent pair. Its incoming and final headings are
G(u) and G(v), which need not equal u and v. This is the only pose discrepancy.

Inductively chi^r(u,v) is exactly the physical read-state word of psi^r(v)
following psi^r(u). Its incoming and final headings are G^r(u),G^r(v), and
its net displacement is always v. Every such word occurs in P: expand an
actual occurrence of (u,v) under psi^r. Thus every one is internally ant-legal
if P is an ant path, regardless of the coloring at its occurrence.

## 3. Exact Laurent iteration and periodic boundary

Define the weighted incidence matrix M(X,Y) of chi using those read offsets.
Each child displacement equals the second coordinate of its pair. Hence
refining a child leaves that displacement unchanged, and offsets add exactly.
M(X,Y)^r therefore counts the actual weighted physical read states of
chi^r(s), with no hidden phase or change of coordinate frame.

For a physical pair s=(u,v), define d_s=axis(u)*turn(u,v) and the literal
one-read clock head difference H_s=gamma_v*w(v)-gamma_u. Then g_s=H_s-d_s
is strictly positive on the clock domain from the companion proof. At depth r
head corrections telescope, giving exactly

    (M^r g)_s = H_s(r) - (M^r d)_s,
    H_(u,v)(r) = gamma_(G^r(v))*w(v) - gamma_(G^r(u)).

The finite map G on four directions has eventually periodic orbits. Thus
H_s(r) is eventually periodic in r, and its generating function has no pole
inside the unit disk. No invertibility or permutation property of G is needed.

At each depth r, all reads at a fixed spatial offset q have the same incoming
axis, namely axis(G^r(u))*(-1)^(q_x+q_y). Ant legality consequently bounds
every coefficient of (M^r d)_s by one in absolute value. The depth-r offsets
are sums of r members of a finite set, so their norm is O(r). All hypotheses
of the periodic-boundary version of the companion Perron argument hold.

## 4. A terminal component suffices

Choose any terminal strongly connected component T of the finite directed
child graph on S. It is closed. Since every image has exactly K children,
its restricted row-incidence matrix has row sums K and irreducible Perron
value K>1 at X=Y=1. Every state of T occurs in P, and every iterated T-image
is an actual factor. The restricted first-child map has a zero-offset cycle.

Apply the companion proof on T: the positive clock forces a nonzero Perron
pole in the signed checker-occupation series on an open positive-character
domain; bounded integer coefficients force a semilinear denominator; analytic
continuation to X=Y=1 is impossible. This contradicts the existence of P.

## Corollary for the previously signed half-turn matrix dichotomy

For fixed uniform half-turn direction substitutions and growing rooted cycles,
the finite-order branch of `matrix_candidates/halfturn_matrix_dichotomy.md`
is eliminated. Every finite-seed survivor would therefore require

    every eigenvalue of A has modulus >1, and rho(A)<k<=|det A|.

This corollary has independent analytic signoff for this note and its companion.
It does not enlarge the hypotheses of the previously signed expansive branch.
