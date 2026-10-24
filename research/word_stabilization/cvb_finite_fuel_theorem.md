# A finite-fuel theorem for the C/V/B macro subsystem

**Status, 22 October 2026:** proved by an explicit finite local-state certificate, independently checked with different color representations and independently reconstructed macro geometry. This is an intermediate theorem, not a solution of the highway conjecture. The U and Q macros are not covered.

## 1. Exact statement and conventions

Consider any finite word over the three turn blocks

```
C = LLLLRLRRRRLRRRR
V = LLLLRLRRRRLRRLRRRR
B = LLLLRLRRRRLRLLRRLLLLRRLLRRRRLLRRLRLLRLLRLRLLRRRRLLRLRRRRLRLLLLRRRRLRRLRRRR
```

Their lengths are 15, 18, and 74. The head initially points north. A right turn is made on white, a left turn on black; the current cell is flipped and then the ant moves. A word is *physically feasible* if consecutive reads of every physical cell have alternating colors. A finite feasible word has a canonical finite realizing board: exactly the cells whose first read is L are initially black.

Coordinates are the recovered before-marker convention. Every block starts with the common marker `LLLLRLRRRRLR`. Rotations of the whole statement are allowed.

**Fresh-tip theorem.** In every physically feasible C/V/B word, the physical cell at local coordinate (1,2) of each V has not been read earlier in that word. Its first read in that V is L, at phase 13, followed by R at phase 17 (zero-based phases).

“Earlier in that word” is essential. If the word begins in the middle of a longer ant trajectory, the theorem makes no assertion about reads before the word began. It nevertheless supplies distinct black cells in the complete board at word entry.

**Finite-fuel corollary.** Starting from any board with m black cells, a physically feasible C/V/B word has at most 8m+8 macroblocks. In particular, no infinite C/V/B word can be realized from finite black support.

## 2. An exact coarse square lattice

Let p be the physical head position, f its forward unit vector, and r its right unit vector. Define the half-integral center

z = p + (f-r)/2.

Direct evaluation of the literal blocks gives:

- C fixes z and rotates the heading left.
- V translates z by r+3f, preserving the heading.
- B translates z by -2r-6f, reversing the heading.

Consequently all centers in a C/V/B word lie in one translate of the lattice with basis d=(1,3), e=(-3,1). Normalize a target V to physical pose (0,0), north. Its center is z0=(-1/2,1/2). Write any other center as z0+a d+b e.

For heading h=0,1,2,3 (north,east,south,west), write the forward vector as f_h and the right vector as r_h. The physical macro-entry pose is

p(a,b,h)=((-1+2a-6b-f_h.x+r_h.x)/2,
          (1+6a+2b-f_h.y+r_h.y)/2).

If delta_h is (1,0),(0,-1),(-1,0),(0,1), the three coarse transitions are

- C: (a,b,h) -> (a,b,h-1).
- V: (a,b,h) -> ((a,b)+delta_h,h).
- B: (a,b,h) -> ((a,b)-2 delta_h,h+2).

All headings are taken modulo four.

## 3. Reduction of an alleged old V tip to a finite problem

Let q=(1,2) be the target V tip. Suppose it was read before the target V. Because its next read is L, its immediately preceding read must be R. Let X be the C, V, or B macro containing that preceding R. Then:

1. The last read of q within X is R.
2. All complete macros between X and the target V avoid q entirely.
3. Immediately after X, each patch cell read by X has its exact last-written color. Every other patch cell may have either color.

Thus it suffices to exclude a path from the output of any possible last-R macro X to a target V, with no intermediate q-read. No assumption on earlier history, on other cells, or on the size of the original black board is needed in this reduction.

## 4. A conservative finite patch abstraction

One independently audited patch is

P7 = {(0,0),(0,3),(1,2),(1,3),(1,4),(2,0),(2,1)}.

A smaller independently audited patch is

P5 = {(0,0),(0,2),(1,2),(2,0),(2,1)}.

The finite state consists of a macro-entry head location and the current colors of all cells in the selected patch. A head location has coarse coordinates and a heading.

A coarse center is *sensitive* when some macro at some heading from that center reads a patch cell. These centers are enumerated exactly, without a spatial cutoff. If a macro trace from center zero and heading h reads physical position (x,y), then its translated copy can read patch cell (u,v) only when

A=((u-x)+3(v-y))/10,
B=(-3(u-x)+(v-y))/10

are integers. The corresponding sensitive center is precisely (A,B). Taking this finite union over patch cells, headings, blocks, and phases enumerates every sensitive center.

All four headings at sensitive centers are retained. Every other center is collapsed to a single state OUT. By construction, a macro starting at an omitted center reads no patch cell, so excursions among omitted centers preserve the patch colors.

OUT may return nondeterministically to **every** retained head with an omitted predecessor. This forgets connectivity and therefore enlarges the actual set of excursions. For V, the predecessor center of (a,b,h) is (a,b)-delta_h. For B it is (a,b)-2 delta_h, with predecessor heading h+2. C never changes the center. Keeping every such return, regardless of whether the outside excursion can actually connect the departure and return, is conservative.

At an internal head, a macro transition is allowed exactly when its successive patch reads have the required colors; every read flips that bit. All other physical-cell constraints are ignored. Except for the target V transition, any macro reading q is forbidden, because the interval began just after the last preceding q-read.

Initial states are all possible outputs of a macro whose last q-read is R. Cells it reads have their forced output colors; cells it does not read are arbitrary. The initial states therefore include every actual alleged counterexample, even when the C/V/B word began in the middle of an earlier history.

## 5. Finite closure certificate and checks

For P7, the complete-color abstraction has 69 head locations including OUT, 104 initial color states, and 3,480 reachable states. No reachable state admits the target V. There are 55 reachable OUT color assignments.

For P5, there are 65 head locations, 43 initial complete-color states, and 907 reachable complete-color states. There are 15 reachable OUT color assignments. No reachable state admits the target V. A reduced ordered binary decision diagram implementation represents the same closure using only 118 created BDD nodes; this is a representation count, not a claim that the explicit state space has only 118 states.

The certificate check is a finite inductive-closure check:

- Every initial state belongs to the certified set.
- Every permitted non-target transition from the certified set stays in it.
- No state in the certified set permits the target V.

The direct implementations perform these checks using literal turn strings and integer coordinates. Independently reconstructed tests agree:

- `cvb_local_trap.py 2`: a larger 5x5 patch, 89 head locations and 437,158 ternary known/unknown-color states.
- `cvb_seven_cell_trap.py`: P7, 6,498 ternary states.
- `cvb_five_cell_trap.py`: P5, 2,005 ternary states.
- `bdd_local_trap.py CVB V -1`: P7, 3,480 full-color states.
- `bdd_local_trap.py CVB V -2`: P5, 907 full-color states.
- Independent audit `../audits/audit_cvb_patch.py`: last-read-letter representation, exact inverse geometry and literal-endpoint outside predecessors, reproducing the 437,158-state closure.
- Independent audit `../audits/audit_cvb_seven_cells.py`: fully specified current colors, reproducing the 3,480-state closure.
- Independent audit `../audits/audit_cvb_five_cells.py`: fully specified current colors, reproducing the 907-state closure; its complete state list is `../audits/cvb_five_cells_audit.json`.

The ternary and complete-color state counts differ because distinct partial assignments can overlap. They represent compatible conservative abstractions, not the same list of concrete states.

Therefore an old q cannot precede the target V. This proves the fresh-tip theorem.

## 6. From fresh tips to a uniform finite-fuel bound

Each V tip is a new first-read-L cell, so different V blocks require different cells black at word entry. Hence n_V <= m.

The word CCCC followed by **any** of the five recovered macros is infeasible: physical cell (2,1) is requested R at times 7 and 67 with no read in between. The common first eight letters of the next macro already create this contradiction. Thus before each non-C block there are at most three consecutive C blocks, and the terminal run has at most four.

Also B C^k B is infeasible for k=0,1,2,3. Explicit same-cell conflicts are:

| Word | Cell | Earlier time/read | Later time/read |
|---|---|---|---|
| BB | (-1,-1) | 46/R | 142/R |
| BCB | (-5,-2) | 53/R | 141/R |
| BCCB | (-2,-4) | 76/L | 116/L |
| BCCCB | (-2,-3) | 67/R | 127/R |

These conflicts are independent of the initial coloring. Longer C separators are ruled out by the CCCC observation. Thus between any two B blocks there must be a V, and n_B <= n_V+1.

It follows that

n_C <= 3(n_V+n_B)+4,

n_C+n_V+n_B <= 4(n_V+n_B)+4 <= 8n_V+8 <= 8m+8.

The claimed finite-fuel corollary follows. A direct turn-count bound is 182m+179. Both bounds are deliberately loose.

## 7. Exact limitation and next target

The other recovered blocks U and Q change the coarse lattice coset. In center coordinates, U translates by 4f; Q translates by -3r-5f and reverses. The latter displacement is U minus three V displacements. The full center lattice has index two, whereas the C/V/B center lattice has index ten, leaving five possible cosets. The proof above cannot silently identify these cosets or apply its OUT relation after a U or Q.

Consequently any infinite physically feasible five-macro word from finite support must contain infinitely many U or Q blocks. Excluding that remaining behavior, and then excluding infinitely many adjacent bad ten-windows in arbitrary ant trajectories, remain separate unsolved steps.


## Stronger short-grammar consequence (22 October 2026)

The independently checked literal gap grammar in `short_macro_grammar.md`
sharpens the preceding safe bound. In a physically feasible C/V/B word, B
appears at most once and only in a prefix B or CB; every C run preceding V
after a non-C has length at most two, and the terminal C run has length at
most three. Consequently, if v is the number of V blocks, the total number
of blocks is at most 3v+5, hence at most **3m+5** for m entry-time black cells.
The corresponding turn bound is at most 48m+134. The sharper grammar does
not alter the freshness proof or its finite-support scope.
