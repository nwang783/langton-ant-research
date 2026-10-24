# Nonuniform finite-order direction substitutions are impossible

23 October 2026, 05:29 UTC. Independently signed analytic review at 05:35 UTC.
The active-pair lumping and terminal-component arguments were checked separately.

## Statement

Let phi be a fixed nonerasing substitution on the four absolute movement
letters E,N,W,S, with arbitrary unequal finite image lengths. Suppose
net(phi(v))=A v for one integer matrix A of finite order. No growing rooted
power-limit of phi can be the movement word of a Langton ant, on any initial
coloring.

No symmetry or preservation of coarse final headings is assumed. This extends
the signed uniform direction theorem, but still has only four UNDECORATED
movement letters and a fixed controller. Hidden states, changing directives
and occurrence-specific image choices are not included.

## 1. Work only in the genuine unit-spatial fixed phase

Take a power divisible by both the root cycle and the order of A. Denote the
resulting substitution by psi and its actual growing fixed word by P. Then
psi(P)=P and net(psi(v))=v. Every refined image of an appearing direction is
an actual factor of P. Thus all these words alternate movement axes and have
internally consistent ant reads when provided their actual incoming headings.

For direction v, net displacement v implies

    count_v(psi(v)) = 1 + count_(-v)(psi(v)).

Therefore every direction image contains its own letter. The ordinary direction
incidence matrix is entrywise at least I. An inactive direction means precisely
psi(v)=v. Because the root grows, some reachable direction is active.

## 2. A terminal active direction component must branch

Choose a terminal strongly connected component T in the graph induced by the
reachable ACTIVE directions. Every child outside T is then inactive, hence an
identity letter. The restricted unweighted matrix B(1,1) is irreducible and
at least I. It has Perron value greater than one unless T is a singleton {v}
with exactly one occurrence of v in its image.

That exception is geometrically impossible. Unique v means no -v. Axis
alternation then permits at most two perpendicular letters, so a nonidentity
image must be exactly

    psi(v) = q v (-q),       q perpendicular to v.

Both q and -q are outside the singleton active component and are therefore
identities. Consequently psi^2(v)=q q v (-q) (-q), containing consecutive equal
directions. It cannot be a quarter-turn path, contrary to its being a factor
of P. Thus B(1,1) has Perron value greater than one.

Let Q consist of T and the inactive directions reachable from T. Its weighted
direction matrix has block form

    D(X,Y) = [[B(X,Y),C(X,Y)],[0,I]].

All offsets are read offsets in psi(v), and their addition under refinement
is exact because the spatial matrix is I.

## 3. Every branching weighted block has a strict clock region

B has a fixed irreducible zero pattern. Its Perron value lambda(X,Y) is positive,
simple and real-analytic on the positive quadrant, with lambda(1,1)>1.

Regard each individual child occurrence as a directed edge, weighted by its
integer read offset. If some directed cycle has nonzero total offset q, choose
a real z with both coordinates nonzero and z dot q>0. At characters
(X,Y)=(exp(t z_x),exp(t z_y)), its cycle weight tends to infinity. The spectral
radius is at least that cycle weight to the reciprocal cycle length, so
lambda>1 for sufficiently large t. A quarter rotation puts these characters
in a strict positive-clock cone, also for sufficiently large t.

If every directed cycle has zero total offset, the weights are a vertex
potential difference: p_e=a_target-a_source. This follows by comparing paths
with a fixed return path in the strongly connected graph. In particular all
parallel edges have the same offset. A diagonal monomial conjugation then
identifies B(X,Y) with B(1,1), so lambda is the constant lambda(1,1)>1.

In either case there is one rotated clock and a nonempty open positive-character
domain U on which its literal increment vector is positive and lambda>1.

## 4. Pair lifting and a strictly positive lifted Perron vector

Each direction in T occurs arbitrarily many times in refined T blocks, by
irreducibility and Perron growth greater than one. Thus each has a genuine
positive-position occurrence in P, not only a possible initial root occurrence.
The same holds for inactive directions reached from T. Let S consist of the
genuine occurring pairs (u,v) in P with v in Q. It has at least one pair over
every direction of Q, and every pair is perpendicular. Put F(v)=first(psi(v)), G(v)=last(psi(v)). Lift a pair
(u,v), with psi(v)=w_0 ... w_(l-1), to

    (G(u),w_0), (w_0,w_1), ..., (w_(l-2),w_(l-1)).

This is exactly the read-state block psi(v) after psi(u) in the actual word.
It is closed on S because child outgoing directions remain in Q. Its weighted
incidence M iterates the actual block psi^r(v) following psi^r(u), with incoming/
final headings G^r(u),G^r(v), displacement v, and additive read offsets.

Partition S into active pairs with outgoing direction in T and inactive pairs
with outgoing direction in Q minus T. Inactive outgoing directions are fixed
identity letters. Their pair image has exactly one zero-offset child,
(G(u),v). Thus the inactive pair matrix D0 is a deterministic zero-offset
map, with spectral radius1 whenever the inactive set is nonempty. It need NOT
be the identity map, since the incoming heading can change. Write

    M = [[C,E],[0,D0]].

Let L lift a vector on T to the active pairs by its outgoing direction.
Summing weighted children by their outgoing direction gives the EXACT lumping

    C L = L B.

The positive Perron eigenvector r of B therefore lifts to a strictly positive
vector v=Lr satisfying C v=lambda v. This alone proves rho(C)=lambda, without
assuming that the pair graph is irreducible. For example the weighted maximum
norm defined by v gives operator norm lambda, and lambda is an eigenvalue.

For any strictly positive clock vector g, the active resolvent is

    [(I-tM)^(-1)g]_active
      = (I-tC)^(-1) h(t),
    h(t)=g_active+t E(I-tD0)^(-1)g_inactive.

On the chosen clock domain lambda>1, so t0=1/lambda<1. The inactive resolvent
is analytic and nonnegative at t0. In particular h(t) is strictly positive
near t0 from below, with h(t)>=epsilon v for some epsilon>0. Therefore

    [(I-tC)^(-1)h(t)]_s >= epsilon v_s/(1-t lambda)

for every active pair s and positive t approaching t0 from below. The rational
resolvent has a genuine positive-real pole there. No claim about a nondominant
component pole or cancellation between arbitrary SCCs is used. If there are
no inactive states, omit that block and take h=g_active.

## 5. The clock and semilinear denominator finish the contradiction

For each physical pair s=(u,v), use the chosen rotated clock head difference
H_s=gamma_v*w(v)-gamma_u and checker turn vector d. Then g=H-d is strictly
positive on U. At depth r, exact telescoping gives

    (M^r g)_(u,v) = H_(u,v)(r)-(M^r d)_(u,v),
    H_(u,v)(r)=gamma_(G^r(v))*w(v)-gamma_(G^r(u)).

The map G is finite, so the boundary sequence is eventually periodic and has
no generating-function pole inside the unit disk. Every refined block is
internally ant-legal. At fixed depth and position its incoming axis is fixed,
so every coefficient of the signed checker occupation M^r d is in{-1,0,1}.
Read offsets have norm O(r).

The already signed finite-valued rational-series argument supplies, for any
fixed s with outgoing direction in T, a denominator

    P_s(t;X,Y)=product_j (1-t^(a_j) X^(b_j) Y^(c_j)), a_j>0.

The genuine clock Perron pole cannot be cancelled by the boundary sequence,
so P_s(1/lambda(X,Y);X,Y)=0 throughout U. Its left side is real-analytic on
the connected positive quadrant. At(1,1) this contradicts lambda(1,1)>1,
because the denominator specializes to a product of1-t^a and has no positive
zero below one. This proves the statement.

## Scope warning

The lumping relies on the EXACT four-direction pair lift: the complete
weighted outgoing-letter inventory is independent of the incoming context.
Additional hidden states may change internal images and invalidate it. The zero-cycle gauge
argument is used only on one irreducible terminal ACTIVE direction block.
No claim is made about arbitrary nonuniform decorated presentations, varying
controllers, or general ant paths.

Independent finite controls: `audits/check_nonuniform_pair_clock_independent.py/json`
checks24 mixed-length geometric maps, including axis-swapping images and periodic
boundary headings. These controls supplement, rather than replace, the analytic proof.
