# A balanced CC return cannot turn and continue

Status: independently audited analytic argument with a finite footprint checker.
This is a new terminal-reuse obstruction, not a proof of completed-C freshness.

Let X,Y be nonempty words over U,V with the same number of U blocks and the
same number of V blocks. For every A in {C,U,V,Q,B}, the word

    X C C Y C A

is physically infeasible. Moreover, if X C C Y C itself is feasible, its final
C is the first C in its run and reuses its phase-1 first-L input from X.
Thus omitting the continuation condition from the proposed C-fuel theorem
would be false even for factors starting non-C.

## Exact geometry

Use north-facing entry (0,0,N), and write D=4u+3v for the vertical displacement
of each run. Their horizontal displacement is v. Since the runs are nonempty,
D>=3. Each U/V block stays north-facing or, after CC, south-facing.

After X the pose is (v,D,N). The two C blocks have combined displacement
(-1,1) and heading reversal. After X CC Y the pose is therefore (-1,1,S).
The final C ends at (-1,0,E). Every macro A reads its local cell (0,1) for
the first time at phase 11, with letter R. In this east-facing frame that is
the physical cell (0,0).

The first macro of X reads (0,0) at phases 0 and 4, with letters L,R, and
never again. The following list excludes all intervening reads of (0,0):

- Later blocks of X have entry height at least 3 and local minimum read
  height -1, so every read has physical height at least 2.
- The first middle C has minimum height D-1>=2. The second starts at
  (v,D+1,W); its minimum height is D because C's minimum local x is -1.
- Before each south-facing block of Y, let d be the remaining vertical
  displacement of Y, including that block. Its entry height is d+1. Its
  maximum local read height is its own displacement, 3 for V or 4 for U.
  Thus all its physical reads have height at least 1.
- The final C would read (0,0) only at its local cell (-1,1), absent from
  C's footprint.
- The following macro A first reads its local (0,1) at phase 11.

Hence the two reads at X phase 4 and A phase 11 are consecutive reads of
(0,0), both R, contradicting the flip rule.

## The reused C input

The final C's phase-1 input is physical (0,1). The first macro of X reads
that cell last with R, at phase 19 if it is U or phase 11 if it is V.
Later outward blocks and the
middle CC do not read it, by the same height estimates above.

A return block can reach height 1 only if it is the last block of Y. For
last U the required local cell is (-1,4), absent from U; for last V it is
(0,3), absent from V. Thus the next read of (0,1) is the final C's phase-1 L.
It is genuinely reused, but the word cannot have any following macro.

Examples VCCVC and VVCCVVC are literally feasible. They cannot be extended
by any macro. Regression checks for longer words are not needed by the
all-length geometric proof.

## Scope

The proof does not say that every reused first-C input arises from such a
balanced CC return. That classification, or another argument excluding a
reused input in a completed C-run, remains open.
