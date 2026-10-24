# Continuous read support is connected; final discrepancy components are not independent returns

23 October 2026, 17:55 UTC. An exact all-step observation and an ACTUAL finite
ant countercontrol. No endpoint-only model, prefix DFS or generic local validator
extension is used. Universal finite-seed capture remains open.

## 1. The causal read-edge graph is always connected

Use the independently signed even active-dual formulation. In sector zero,
cell q=(x,y) is the edge with endpoints

    q +/- (1/2,1/2) if x+y is even,
    q +/- (1/2,-1/2) if x+y is odd.

The active vertex is z=p+rotation_h(-1/2,-1/2). A fine R adds the inspected
edge and traverses it; a fine L deletes the inspected edge and stays at z.
Every inspected edge is incident to the CURRENT active vertex.

For any nonempty actual finite interval, let H be the union of all its read
edges, irrespective of their initial/final colors or read multiplicity.
Then H is connected and contains every active vertex during the interval.

Proof: begin with the initial active vertex. Each inspected edge meets the
already reached active vertex. An L leaves that vertex in place; an R moves
to the inspected edge's other endpoint, which has just been added to H.
Induction proves connectedness and includes the final active vertex. This
proof does not assume a marked K5 core, atomic-center simplicity, finite
initial support, or eventual behavior.

Thus a decomposition using connected components of the COMPLETE causal read
support has only ONE component on a continuous interval. To obtain several
pieces, a proposed ledger must make explicit temporal cuts, boundary ports,
or a choice to forget some previously read edges. Such choices require their
own travel/boundary accounting.

## 2. An actual eight-read same-pose factor

Starting from the blank ant at (0,0,N), its exact board at tick9 is

    B9={(-1,0),(-1,1),(0,-1),(0,0),(0,1),(1,-1),(1,0)},
    p9=(-1,0), h9=W.

The next eight literal reads are

    tick offset    read cell    before color
        0           (-1, 0)          L
        1           (-1,-1)          R
        2           (-2,-1)          R
        3           (-2, 0)          R
        4           (-1, 0)          R
        5           (-1,-1)          L
        6           ( 0,-1)          L
        7           ( 0, 0)          L

The word is LRRRRLLL, and the endpoint is EXACTLY the same pose (-1,0,W).
There is one continuous physical ant and no intermediate edit or reset.
The complete endpoint XOR is

    E=Cleft UNION Cright,
    Cleft ={(-2,-1),(-2,0)},
    Cright={(0,-1),(0,0)}.

These are two DISJOINT connected components in the EVEN active-dual EDGE
graph, not merely in a pixel-connectivity convention. Doubled dual endpoints:

    (-2,-1): (-5,-1)--(-3,-3)
    (-2, 0): (-5,-1)--(-3, 1)
    ( 0,-1): (-1,-1)--( 1,-3)
    ( 0, 0): (-1,-1)--( 1, 1).

The two omitted read cells are BOTH restored, each read exactly twice:

    (-1,-1): (-3,-3)--(-1,-1),
    (-1, 0): (-3, 1)--(-1,-1).

They connect the two net-discrepancy components in the full causal read graph.
They cannot be retired from a chronological ledger merely because their
endpoint colors agree. The right component is erased and the left is added;
there is no independent same-pose physical return for either component.

## 3. Exact failure of componentwise optimized return charging

For a finite nonempty set C define the unsigned optimized clock norm

    A_z(C)=min_{c in Z} sum_{q in C}(3^|z(q)-c|-1).

The signed same-pose return theorem proves T<=A_z(E) for the COMPLETE XOR.
It does NOT prove that the center may be chosen separately per component.
Here each Cleft/Cright has two consecutive z values, for BOTH z=x+y and
z=x-y. Hence

    A_z(Cleft)=A_z(Cright)=2.

The actual duration is T=8. Therefore the proposed additive decomposition

    T <= sum over net-discrepancy components C of A_z(C)

is FALSE: its right side is four. This countercontrol works for either
oblique coordinate and uses the actual natural active-dual components.
For comparison, the full E has four consecutive z values, so A_z(E)=12;
the valid global inequality 8<=12 is retained.

There is a second exact obstruction to declaring either component a return
on its own. For z=x+y and clock center c=-3, the signed field contribution
of Cleft is -2, while Cright contributes 18. At c=0 the corresponding values
are 18 and -2. Each component can REFUND the other's clock. The full signed
clock gain is at least eight at every center and has minimum eight, as an
actual eight-read return requires. Separate field pieces have no individual
positive-time interpretation without their cursor endpoint corrections.

## 4. What remains available

This does not rule out a corrected causal decomposition. It specifies the
minimum information such a decomposition must carry:

1. The actual temporal subintervals and their physical cursor entry/exit ports.
2. Restored read edges whenever they provide travel or connect different net
   changed-support components.
3. The appropriate clock head correction at each port; it cannot be canceled
   separately unless that piece genuinely has the required endpoint section.
4. Any change of clock center between pieces, with its exact boundary debt.

For disjoint ACTUAL same-pose subintervals, their individual bounds may of
course be summed. That statement is valid but does not assert that an
arbitrary large same-pose return admits such a finer decomposition. On a
simple U-entry retained factor, full atomic entry poses do not repeat; raw
microscopic returns inside atoms still occur. A proposed global argument
must not quietly replace one notion of return by the other.

The proved result is a useful boundary: all-read causal connectedness is
automatic but gives no component budget; endpoint-XOR decomposition is more
informative but loses precisely the restored travel links. Finding an
amortized, continuously cursor-coupled way to cut the single read-support
component remains open.

Dependency: core_periodicity_new/active_center_edge_walk_frozen_20261023_1739/
manifest.json (SHA256 b7d41cc3ce9b68c68943b7d7af6fbf1a448b69e434d1b833e8f0d677093ab328).
The local return-clock deduction is same_pose_complete_discrepancy_clock.md
in this directory. No historical-incidence/component-merger claim is made.
