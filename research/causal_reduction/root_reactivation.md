# A dormant input-root lineage can return and supply both infinite spines

## Status and exact scope

This is a colored-token extension of the already proved twenty-cell one-shot feedback family in `sources/kehao95-core/memory_feedback/proof/scalable-feedback-circuit.md`. Its all-parameter stage separation and protected-region geometry are inherited dependencies, not newly proved here. The new exact finite checker is `certify_root_reactivation.py`.

The result rules out abandoning an ancestral root because it has been inactive for a long time or because several newer highway cores have replaced it. It does not construct infinite nonstandard renewal. Every input in the family ultimately has the standard highway.

Root colors below are exact passive ancestry labels, not a claim of independent information bits or unique counterfactual causation.

## 1. Root-color dynamics

Label every initial black edge by its virtual root and the initial cursor by X. Maintain an active root label. On R, the new edge token gets that active label. On L, the consumed token's root becomes the active label for the next cursor node. This is exactly the root projection of the forest in `forest_theorem.md`.

For the four-cell port

`G={(0,-1),(1,1),(2,2),(1,3)}`

started at (0,0), heading E, label these four cells A,B,C,D in the displayed order. Their first black reads occur at times 1,22,32,58. An arbitrary incoming active label X occurs for the last time at update 13. Labels other than A occur for the last time at update 170. At every update from 171 onwards the active root is A.

This last assertion is all-future: at the certified standard entry t=182, every black token not labeled A lies outside the entire future standard read set. Every future insertion therefore has label A, and every later consumption has label A. The checker verifies the infinite read-set exclusions by exact integer ray equations.

The reference writes (0,2) with root D at time 60, and (2,5) with root A at time 53. Neither cell is subsequently read on the reference's certified standard future.

## 2. The twenty-cell family

Let rho be clockwise quarter rotation and G[p,h]=p+rho^(h-1)G, with headings N,E,S,W=0,1,2,3. For each even n>=20 use the complete seed

`B_n = union_(i=0..4) G[p_i,h_i]`,

where the five poses are

- (0,0), E;
- (n-1,n), N;
- (-n,3n-4), W;
- (-5n+5,-n), S;
- (-3n,-3n+8), E.

All twenty cells are initially present. Start the ant at (0,0),E. Give the four roots of port i labels A_i,B_i,C_i,D_i.

The inherited all-parameter theorem proves five guarded standard stages, their disjoint read sets before the final return, and the return time

`e=624n-1516`

to (0,2),E. Its first return consumes the D_0 token born at time 60. The complete full-field future is standard from e+774; no wakes are erased.

## 3. The ancestral reactivation theorem

For every even n>=20:

1. The last update before e whose active root is A_0 is at `52n-160`.
2. The next update with active root A_0 is at `e+234=624n-1282`.
3. At update `e+233`, the ant consumes the token at (2,5), born at time 53 with root A_0. Its lifetime age is `624n-1336`.
4. At every update from `e+770` onwards, the active root is A_0. Consequently both infinite standard ancestry spines descend from this first port's root A_0.

The two successive A_0-active times in items 1-2 differ by `572n-1122`, which is unbounded at fixed initial black mass twenty. There are `572n-1123` intervening updates with no active A_0 root. This is a whole-lineage dormancy and reactivation statement, not just an old token's age.

### Proof of the long inactive interval

The second port starts at t_1=52n-173 with incoming active label A_0. The isolated port calculation makes its last use of that incoming label occur thirteen updates later, at t_1+13. The remaining stable stages have active roots A_1,A_2,A_3,A_4. The inherited disjoint read-set guards prevent reading earlier archives before e. Thus A_0 cannot reactivate during these later stages.

### Exact colored protected field

The inherited proof uses

`Omega={ (x,y): x>=-16 and -14<=x+y<=12 }`

and proves that the complete black field at e restricts to one fixed 90-cell field there for every n. The color extension is also constant:

- 24 black tokens have root A_0;
- 9 have root D_0;
- 57 have root A_4.

To verify the extension, stage 0's fixed prelude and first six standard epochs give its entire contribution in Omega. Stages 1,2,3 miss Omega. The part of stage 4 in Omega consists only of standard-tail writes, all labeled A_4 by the four-cell port calculation. Its relative epoch indices are -26,...,-1 and a fixed fourteen-letter prefix at epoch zero, exactly as in the inherited endpoint equation. Additional earlier epochs and the stage-4 prelude miss Omega. The checker performs this fixed colored construction and retains the full 90-cell labeled field.

At e the active label is A_4. The fixed protected continuation consumes (2,5) at relative time 233 and has no earlier A_0-active update. That cell is born at time 53, never read later in stage 0, and is excluded from stages 1-4 by the inherited guards. The finite protected continuation does not read it before offset 233. These facts prove items 2-3.

Every read in the 774-step protected recovery lies in Omega. The last update with a label other than A_0 is at relative time 769. At the certified standard state after 774 updates, every remaining black token with root other than A_0 lies outside the entire future read set. Exact ray equations verify this exclusion. Every later insertion and consumption thus has label A_0. The known two-spine standard-forest theorem gives item 4. QED.

## Limits

This does NOT show an infinite cycle of highway directions, infinite defects, or a reusable controller. It also does not prove that A_0 represents a necessary counterfactual input bit. The labels record a precise physical token genealogy.

The useful negative conclusion is that any genealogical proof must keep dormant token branches: an old root can disappear from the active cursor for an arbitrarily long interval, then regain both infinite standard channels. Finite initial roots do not imply an irreversible chronological ordering of which root can become active later.

## Reproduction and dependency boundary

Run `python certify_root_reactivation.py` from this directory. It independently checks both supplied-word infinite futures by epoch breakpoints, reconstructs the fixed protected colored field, checks the root reactivation and exclusions, and compares five literal full-field family controls (n=20,22,40,80,160).

Those five controls do not establish the all-parameter geometry. That geometry is explicitly inherited from the source's Sections 3-4. The finite color extension and its exact arithmetic are the present work. No external review or priority claim is asserted.
