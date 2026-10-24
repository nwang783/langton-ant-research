# The lifted lamp input is not a pointwise static gauge

An attractive simplification would be a universal function f on lifted cosets such that the first-read lamp of any reached coset C is

    lambda(C) = B0(project(C)) XOR f(C).

This is false, even comparing two finite square seeds with the same starting pose. The obstruction does not rule out a more complicated dependence on other seed cells or prior history.

Start at (0,0), heading north. Consider these two feasible prefixes:

    w = RRRRLRRRRLRRRRLLLLRLRRRRLRRRRLLLLRLRRRRLRRRRLLLLRL
    v = LLRLLRLLRL.

The first has length50 and is realized from the all-white board. The second has length10 and is realized with black seed

    {(-2,-2),(-2,-1),(-1,-3),(-1,0),(0,-3),(0,0),(1,-2)}.

Both words reduce in C4*C4 to v, and both end at physical pose (1,-1,north). Their terminal right coset C=vH has not been read earlier in either prefix. Its physical point (1,-1) is initially white in both seeds.

However w has previously read that physical point once, while v has not read it. Thus the next read, which is the first read of the SAME coset C in each trajectory, is L after w and R after v. A fixed f(C) cannot give both values from the same projected initial bit0.

The short word visits ten distinct physical cells and its finite seed is obtained simply by setting its seven L-read cells black. The long word is verified directly by successive-read alternation with every first physical read R. No probabilistic inference or long simulation is used.

Exact replay: `check_static_lift_gauge_obstruction.py`; output: `static_lift_gauge_obstruction.json`.

This isolates another reason finite support cannot be pushed through the covering map as a local finite defect of a universal lifted background. The surviving exact formulation is the chronological physical parity chain, or the equivalent spine/corner consistency equation. Dependence on the rest of the finite seed is essential.
