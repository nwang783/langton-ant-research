# C/V/B cut components have at most 36 vertices, including boundary buds

## Status and scope

This is an analytic corollary of the independently audited C/V/B fresh-V theorem, literal macro seams, and audited short-word exclusions. The component-size bound passed independent analytic audit and literal controls; see `../audits/audit_cvb_component_controls.py` and `../audits/cvb_component_controls.json`. It concerns arbitrary physically feasible finite C/V/B intervals, with the cut-forest convention from `cvb_bounded_ancestry.md`; it does not concern all five macros or arbitrary ant trajectories.

Every component has at most 36 ordinary cursor nodes plus boundary buds in total. The bound is sharp, attained by initial CCCC. Initial black-token virtual vertices are not counted: consuming one begins a cut root at depth zero.

## Positive-node structure

Call a cursor node positive if it writes at least one R-token. In C the positive nodes are 4,6,11, with output counts 1,4,4. In V they are 4,6,11,14, with counts 1,4,2,4.

The literal seam identity gives the parent of every noninitial node4 and node6: both are children of the immediately preceding terminal star. In either C or V, node11 is an internal child of node6. The audited fresh-tip theorem makes every V14 a cut root. These are all positive-node types in a C/V suffix. Hence there are no additional old-token positive branches to classify: an old token not used by one of these specified inputs can only produce a zero-output node.

Thus each positive component in a C/V suffix consists of a terminal-star chain through one consecutive C-run, with one node4 side branch per following macro, followed possibly by the nonterminal part of a V. The new terminal V14 starts a different component. This also simplifies the proof of height eight: the determinant-ten exclusion for other positive parent types is unnecessary once both forced seam inputs are used.

## Counting complete components

Each R-token of a component contributes exactly one edge and one child: either its eventual consuming cursor node within the interval, or an artificial boundary bud if it remains black at the end. Therefore component size is exactly one plus the sum of R-output counts of its positive nodes. Later consumption of an outstanding token by a zero-output node replaces one bud by one ordinary leaf and does not increase this count.

The audited short-word exclusions say:

- B occurs only as an initial B or initial CB, at most once.
- An initial C-run has length at most four if terminal, or three if followed by V.
- After a V or B, a C-run has length at most three if terminal, or two if followed by V.

For an initial C-run of length k, the component rooted at its first node6 has output sum 8+9(k-1). It therefore has size 9k, at most 36. If this run is followed by V, the V contributes another 1+4+2=7 outputs, so the component size is 9k+7, at most 34.

An initial V's common node6 component has size 1+4+2=7. An initial node4 component has size 2.

A V14 or B70 root contributes four outputs. After k subsequent C macros, its component size is 5+9k, at most 32 if the C-run is terminal. If a V follows, add seven outputs, giving 12+9k, at most 30.

The exceptional prefix B has largest component output sum 11, so largest size 12. The prefix CB has largest sum 18, so largest size 19. These are finite literal calculations: for B the maximum positive chain is B52,B57,B62,B67, with output counts 4,1,4,2. For CB the maximum is C6,C11,B4,B6,B11,B24, with counts 4,4,1,4,1,4. The B70 root is separate and is covered by the previous paragraph. No other prefix component can gain a positive descendant in the later C/V suffix, because all later positive inputs are already fixed by the seam, the internal node6-to-node11 edge, or a fresh V14 root.

This exhausts the possibilities and proves the bound 36.

## Sharpness and controls

CCCC is physically feasible and terminal. Its first node6 component has 35 R-outputs, hence 36 vertices when terminal buds are included. Its maximum node/bud depth is eight, consistently with the audited height theorem.

`cvb_component_size_controls.json` independently enumerates all feasible words through eight macros, using literal color and token-owner replay. It finds 36 at CCCC. This finite enumeration is a control, not the unbounded proof above.

## Consequence

If the interval enters with m black cells, there are at most m+1 cut roots, so at most 36(m+1) ordinary cursor nodes and boundary buds. Since each cursor node has at most four R updates and one L update, the number of physical updates is at most 180(m+1). This is much weaker numerically than the separately audited direct macro-fuel bound, but it gives a precise bounded-bush interpretation rather than merely a duration bound.
