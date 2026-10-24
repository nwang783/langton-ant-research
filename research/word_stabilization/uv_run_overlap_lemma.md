# At most four common entry centers across one mixed-run fold

Let X F Y be physically feasible, with X,Y arbitrary finite words over U,V
and F in {Q,B}. Count only macro-entry coarse centers, not the terminal
boundary after the last macro of a run. Then X and Y have at most four common
entry centers. More precisely, every coincidence involves either one of the
first two entry centers of X or one of the last two entry centers of Y.

This strengthens the local shared-center rule in
`uv_interior_crossing_lemma.md`. It is still only a one-fold result; it does
not compare runs separated by several folds, nor identify center coincidences
with reuse of a V-tip physical cell.

## Count identity at any common center

Normalize X northward and write u=(0,4), v=(1,3). Suppose X's entry center
before block i equals Y's entry center before block j, using zero-based
indices. Let a,b count U,V blocks in the suffix X[i:], and c,d count U,V
blocks in the prefix Y[:j]. The fold shifts the center by u-3v for Q and
by -2v for B, after which Y moves in the negative u,v directions. Linear
independence of u,v gives:

- Q: c=a+1 and d=b-3.
- B: c=a and d=b-2.

In either case, j=c+d=a+b-2=|X|-i-2. In particular j>=0 forces at least two
blocks of X to remain.

## Propagation toward the fold

Suppose i>=2 and |Y|-j>=3. If j>=2, the count identity gives |X|-i=j+2>=4,
so both visits have the five-block margins required by the audited local
rule. Hence X[i]=V and Y[j-1]=Y[j]=V. Moving forward one block in X and
backward one in Y gives another common center:

    (i,j) -> (i+1,j-1).

The hypotheses i>=2 and |Y|-j>=3 remain true. Repeat until j=1, unless the
initial coincidence already had j=0.

## Finite boundary contradiction

At j=1, exactly three X blocks remain. In the Q case, nonnegativity of
c=a+1,d=b-3 forces a=0,b=3 and Y[:1]=U. Thus the trajectory contains VVVQU,
which is physically infeasible.

In the B case, either a=0,b=3 and Y[:1]=V, immediately giving a VB factor,
or a=1,b=2 and Y[:1]=U. Since VB is infeasible, the sole U in the remaining
three X blocks must be last. This forces VVUBU, also infeasible.

At j=0, the Q equations require c=a+1=0, impossible. The B equations force
the remaining X suffix to be VV, again followed by the forbidden VB.

The three finite boundary obstructions are checked by literal same-cell
read alternation in `verify_uv_run_overlap.py`, with exact witnesses saved
in `uv_run_overlap_boundary_certificate.json`.

Therefore no coincidence can have both i>=2 and |Y|-j>=3. Every common
center is among the first two entries of X or the last two entries of Y.
Each run has distinct centers because its u,v counts are monotone. The
union has size at most four, proving the bound, including short/empty runs.
