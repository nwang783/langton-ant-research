# Exact finite-seed realization as a finite-support parity-graph problem

2026-10-23 03:40 UTC. Analytic reduction independently signed on 2026-10-23 03:50 UTC.
This is a FORWARD equivalence for a supplied finite-power path presentation.
It is not an undecidability reduction into finite Langton-ant seeds.

## 1. Eliminate the guessed initial board from the canonical checks

Keep the hypotheses and fixed-point power of theorem.md, but leave the initial
board B unknown. Write its indicator as b:Z²->{0,1}. All quantities other
than b are effectively automatic.

For each reachable letter s, its representative prefix v_s has displacement
p(v_s). Put z_s(r)=A^r p(v_s). At child j of phi(s), let

    d_j(r)=A^r p_j,   t_j=child letter.

At a local parent read cell w in d_j(r)+R_(t_j)(r), the canonical frame check
is exactly one equation

    b(w+z_s(r+1)) XOR b(w-d_j(r)+z_(t_j)(r)) = c_(s,j)(r,w),

where the explicitly computable right side is

    Q_(v_s)(r+1,w+z_s(r+1))
      XOR XOR_(i<j) Q_(t_i)(r,w-d_i(r))
      XOR Q_(v_(t_j))(r,w-d_j(r)+z_(t_j)(r)).

The two offsets have finite range because A has finitely many powers.
The right side and the footprint guard are automatic predicates. Split the
finitely many offset values and labels c, then existentially quantify r.
This constructs a labelled undirected automatic graph on the physical
lattice Z², with only finitely many possible edge displacements.
Parallel edges with different labels are retained as inconsistent equations;
zero-displacement edges are allowed, including an immediately impossible
label-one loop.

The base checks are the finitely many pins

    b(p(v_s)) = [turn(s)=L] XOR Q_(v_s)(0,p(v_s)).

By the exact given-seed theorem, a finite black list B realizes the whole
morphic ant path if and only if its indicator satisfies all graph equations
and pins. Thus UNKNOWN finite-seed realization has been reduced exactly to
finite-support XOR colouring of this concrete bounded-displacement automatic
graph. The graph is derived from the path; arbitrary such graphs are not
claimed realizable by ants.

## 2. An automatic finiteness obstruction

Let E1 be the set of label-one edges. Every such edge must have at least one
black endpoint. The finite displacement alphabet bounds every vertex degree.
Therefore a finitely supported solution is impossible when E1 is infinite.
Finiteness of E1 is decidable from its regular canonical digit language; when
finite, its endpoints can be listed effectively.

This is a genuine terminating finite-fuel necessary test, independent of
which finite seed might be used. It does not need a seed-size guess.

## 3. The remaining obstruction is component finiteness

Suppose E1 is finite. Let E0 be the zero-labelled graph. Every solution b is
constant on each E0 connected component. A component assigned black MUST be
finite. Conversely any choice of finitely many finite black components gives
a finite board, if it obeys the remaining constraints.

Only components touching endpoints of E1 or pinned vertices matter. All
other components can be white. In the finite quotient of those critical
components, impose the label-one opposite-colour constraints and the pins;
add colour zero for every infinite E0 component. A finite-support solution
exists exactly when this finite abstract constraint system is consistent.

This is an exact characterization, not a promise that the relevant component
mergers or their finiteness can be decided for the derived automatic graph.
That connectivity/finiteness issue is the remaining unknown-seed boundary.
A finite black component has a checkable finite closure certificate because
the displacement set is finite and edge membership is decidable.

## 4. Computability scope

Enumerating finite boards and using theorem.md recognizes successful finite
realization in this fixed presentation class. The graph formulation explains
what a successful finite certificate is buying: it selects only finite
zero-edge components while meeting finitely many nonzero constraints.

No reverse compiler from an arbitrary graph or machine into the permitted
ant substitutions is supplied. Therefore this reduction proves neither
finite-seed undecidability nor unrecognizability, and does not contradict the
separate hardness result for arbitrary infinite initial boards.
