# Forward-chord barrier for a charged staircase output gate

2026-10-24. This is an exact local graph restriction, not a universal no-regeneration theorem. It supplements the literal staircase control without promoting its all-q paired-forest geometry.

## Graph hypotheses and proof

Use the w square coordinates in which positive mass-gain turn is CCW. Suppose the current w cursor has just arrived at u in direction E. An intended next old edge is u--a, a=u+N. Let v=u+E and b=v+N. The complete current black w graph contains a path

    u -- a -- Q -- b -- v,

where Q is any black path from a to b and none of its internal vertices is u or v. The edge u--v is white. The previous ordinary suffix has not deleted any edge of this displayed path. All other passive edges are retained; they may add connectivity, never remove this path.

Following the intended old edge u--a requires the proper r=2 block. The two R arms at u have directions S, then E. If the S arm is not white, that intended block does not execute at all. If it is white, its insertion leaves the displayed path intact. The following R inserts u--v. This closes a cycle containing u--a. Consequently the next L on u--a is NONBRIDGE in w. If the first arm already created an additional cycle, this conclusion is unchanged. Thus the proposed r2L cannot be ordinary.

The same conclusion holds under any lattice translation/rotation. The length, shape and funding of Q are irrelevant. Rerouting Q far outside the corner does not make this port ordinarily traversable. Cutting Q, entering from another port, changing which path is intended, or accepting an exceptional block are genuine changes not excluded by this lemma.

This is the ordinary old-bridge forward-chord restriction, applied to a concrete output gate. It does not assert that u--v was initial seed or newly born; only its current white status and the surviving path matter.

## Literal q=3 gate

In `staircase_backbone_witness_q3.json`, after RRRRL and the following (LRRL)^7L ordinary suffix, translate u=(-1,8), v=(0,8), a=(-1,9), b=(0,9) in w coordinates. The old stitch Q is the single edge a--b, physical cell (9,-9). The u--a and b--v edges are surviving first-epoch R lifetimes. The E arm u--v is the deleted first-epoch input edge, currently white. The current physical pose is (7,-8), N. The next two white updates are at physical cells (7,-8) and (8,-8), followed by L at (8,-9). That L is a w-cycle erasure, exactly as the gate proof requires.

The graph proof excludes repairing this particular gate merely by replacing the charged old stitch by a longer connecting detour. It says nothing about changing the first epoch so that the two R stars are no longer joined, or about eventual recycling after exceptional updates. The whole first output is a single simple path, so its static marked-path load is large even though the next ordinary cursor cannot traverse this local corner.
