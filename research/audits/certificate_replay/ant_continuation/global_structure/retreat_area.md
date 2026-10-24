# A quantitative bound on retreat for a nonperiodic ant

## Scope and status

This note gives a finite-state consequence of bounded retreat. It strengthens
the sufficient condition C2 in the research handoff by giving an explicit
finite-prefix bound. It does not prove that retreat is bounded. It proves
eventual translating periodicity, not the standard period 104. No claim of
publication priority or external review is made.

The argument uses one known fact: a classical ant with a finite black field
has no periodic complete state. The integer clock in
`kehao95/langtons-ant-core/clock_escape/PROOF.md` is one proof of that fact.
The finite-state construction and its quantitative count are given below.

## Definitions

Let X_t=(B_t,p_t,h_t) be the complete state before update t. The initial black
set B_0 is finite. Fix signs eps_x,eps_y in {-1,+1}, and write

    u(q)=eps_x*q_x,       v(q)=eps_y*q_y.

All four sign pairs are allowed. Define two running frontiers, including ALL
initial black cells, not only the visited cells:

    M_u(t)=max{u(q): q in B_0 union {p_0,...,p_t}},
    M_v(t)=max{v(q): q in B_0 union {p_0,...,p_t}}.

The set in each maximum is nonempty because it contains p_0. For T>=0 put

    R_u(T)=max_{0<=t<=T} [M_u(t)-u(p_t)],
    R_v(T)=max_{0<=t<=T} [M_v(t)-v(p_t)],
    A(T)=(R_u(T)+1)*(R_v(T)+1).

Each R is a nonnegative integer. Including B_0 in the frontiers is essential.
Without it, an unseen initial black cell can lie ahead of the ant and break
the claimed autonomous transition.

Call a trajectory ETC if, from some time on, its turn word has a nonzero
translating period: there are P>=1 and d!=0 with the same heading after each
P updates, and each period is the translation by d of the preceding one.

## Theorem

For every finite seed and every choice of the two signs, either the trajectory
is ETC, or for every T>=0,

    T+1 <= 4*A(T)*2^A(T).                                  (1)

Equivalently, for a non-ETC orbit,

    A(T)+log_2 A(T) >= log_2(T+1)-2.                        (2)

In particular,

    A(T) >= log_2(T+1)-log_2 log_2(T+1)-O(1).

If one retreat bound stays at most C, the other must grow at least on the
order of log T on a non-ETC orbit. If both are at most R(T), then
R(T) must grow at least on the order of sqrt(log T).

## Proof

Fix nonnegative integers r_u,r_v. At time t consider the rectangle

    W_t={q: M_u(t)-r_u <= u(q) <= M_u(t),
              M_v(t)-r_v <= v(q) <= M_v(t)}.

It contains A=(r_u+1)(r_v+1) lattice cells. Retain only the following state:

1. The A black/white bits in W_t, indexed relative to its upper right corner.
2. The head position relative to that corner.
3. The physical heading.

The state is allowed only while the head lies in W_t. There are at most
4*A*2^A allowed states.

This is a deterministic partial automaton. The current bit gives the turn,
the bit flips, and the heading gives the next position. Each frontier either
stays fixed or advances by one. If the next head lies below a lower side of
the new rectangle, the automaton stops. Otherwise it shifts the rectangle,
discards bits below its lower sides, and fills every newly exposed front
cell with white.

The last action is exact. A cell newly entering the rectangle has u above
the old M_u or v above the old M_v. Such a cell is neither in B_0 nor among
the previously visited cells. The cell is therefore white. No cell enters
through a lower side, because both frontiers are nondecreasing.

The discarded cells cause no error before a stop: the head remains in the
current rectangle, and its lower sides only advance. A discarded cell can
never re-enter that rectangle. It would require a violation of a retreat
bound for the ant to read it.

Suppose an allowed automaton state first repeats at times s<t before a stop.
Its future abstract states repeat with period P=t-s. Every cycle advances
the two frontiers by the same nonnegative vector (d_u,d_v). The corresponding
physical translation is d=(eps_x*d_u,eps_y*d_v). The cycle never stops.

The literal ant follows these cycles forever. This follows by induction on
cycles: all retained bits match, all newly exposed front cells are white,
and all discarded cells stay behind the repeated path. Thus the same turns
and translated positions occur in every cycle.

The vector d cannot be zero. If it were zero, neither frontier would advance
inside the cycle. The head and all altered cells would remain in one fixed
rectangle. Its bits and the pose repeat; every exterior bit remains unchanged.
The complete finite state would repeat, contrary to the no-cycle theorem.
Therefore d is nonzero, and the trajectory is ETC.

Now set r_u=R_u(T), r_v=R_v(T). The first T+1 abstract states are allowed.
If T+1 exceeds their number 4*A(T)*2^A(T), a state repeats, so the trajectory
is ETC. The contrapositive proves (1). Taking logarithms proves (2). The
asymptotic consequences follow from the monotonicity of A+log_2 A. QED.

## A finite certificate

A repeated abstract state is a certificate that can be checked without a
future retreat promise. Record the two times, the fixed bounds, the state
bits, the pose offsets, and the frontier shift. Check one intervening cycle.
The proof above then establishes every future cycle. This is stronger than
observing a long periodic turn block alone.

## What this does not prove

The inequality supplies a lower bound on the needed retreat area. It supplies
no upper bound. A recurrent orbit can satisfy the inequality in all four
orthants by making larger excursions. The known endpoint convex-hull identity
also allows this: a few distant black corners can preserve a large hull.
Additional chronology is needed to rule out such states along one orbit.

The count 4*A*2^A is deliberately simple. It does not use parity constraints,
the relation between heading and mass, or geometrically unreachable bit states.
A lower count would improve constants but would not close the global gap.
