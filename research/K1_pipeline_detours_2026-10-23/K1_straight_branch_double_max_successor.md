# A straight LEFT max branch forces a double-max RIGHT successor

23 October 2026, 19:08 UTC. Exact branchful corner extension, submitted
for independent review. This is not a front scan or a new exclusion.

## 1. Complete-front scope and exact geometry

Use a complete WHITE cap-four translator, actual full P,d, canonical
first-L maximum-face curve Gamma and K=1. No leftmostness, global branch
absence, leaf hypothesis or original-input fuel is assumed.

Let a STRAIGHT face F have lower-left (0,0) and an immediate LEFT max
neighbor J with lower-left (-1,-1). The signed straight-flat theorem
forces the complete helper history z=(0,0) to be W,W,E,E. Both adjacent
selected contacts have no LEFT L3; optional RIGHT L3 is retained.
The signed successor theorem forces the next curve face G to turn RIGHT.

Normalize this successor by

    G lower-left (-1,1), entry A=(0,1), exit B=(0,2),
    first LEFT helper w=(-1,1), second LEFT helper y=(-1,2),
    first other C face H lower-left (-2,0),
    second other C face I lower-left (-2,2),
    e=(-1,0).

Here A has N,N,S and either no L3 or RIGHT L3 incoming S; B has E,E,W
and an optional L3. H and I are not assumed strict or equal-M in advance.
The C faces at e are J(SE) and H(NW). Put alpha=T1(A).

## 2. Exact necessary complete histories

The following is the entire necessary port/clock table on these six
physical cells. Each row retains both e=N,S,S and e=N,S,S,N.
All listed H and I heights equal M.

    A       w       y       B
    NNS     EWW     SSN     EEW
    NNS     EWW     SSNS    EEWE
    NNS     EWWE    SSNN    EEW
    NNSS    EWW     SSN     EEWW
    NNSS    EWWE    SSNN    EEWW

Consequently BOTH unused LEFT neighbors H,I of the forced RIGHT
successor are maximum. In particular the first helper cannot merely
have a strict-lower neighbor while a branch appears somewhere else.
The state0-to-state1 rise is only the second row; the other rows retain
constant-zero/no-L3 or optional RIGHT-L3 alternatives.

This is a necessary whole-history inventory, not a claim that any row
has an exterior connector or extends to a complete white front.

## 3. Reconstructing the finite table without period assumptions

Every vertex has its complete white history of at most four reads.
At an equal-height C corner the two R headings are opposite. At a
strict corner both R headings, if two occur, choose the higher face.
Thus at w the strict alternatives have R heading W, and the equal
alternatives have opposite W/E headings. At y strict R heading is N,
and equal R headings are N/S. At e strict R heading is N, and equal
R headings are N/S. In the strict H case its R-count height difference
is the SAME at e and w. This shared height constraint is retained.

Match, in actual chronological ordinal order, every occurrence on

    A --W--> w --N--> y --E--> B --S--> A,
    e --E--> z --N--> A, and w --S--> e.

The complete z history is W,W,E,E. Impose consecutive same-cell returns
at least four reads apart and the actual K1 inequality T2(A)<T1(B).
No time is replaced by a residue class. These are finite exact local
constraints, with exterior suppliers left unconstrained, so deleting
an inconsistent row is safe but retaining a row does not prove it.

The saved table control straight_branch_right_corner_extension.py/json
constructs the complete length-1 through length-4 histories afresh,
retains every L heading and either R-count at strict corners, matches
these actual port ordinals, and tests only their finite difference
constraints. It finds exactly the ten rows above (five times two e
histories), without importing the earlier right-turn profile table.
No drift, period, radius or bounded-front search occurs.

There is also a short diagnostic for the first forced equality. Since
z.R2,z.L3 are its two E inputs,

    time(second E output at e)=T3(z)-1=alpha-2.

If H is strict, the exact RIGHT entry-state0 inventory forces w=WW.
Then its first S output is L1, supplied by A.R2, so e's first S input
would occur at T2(A)+2>alpha. But e has one R choosing J, hence can have
at most one E output before its first S input, a contradiction. The
W-first equal-H rows fail the same deadline. The remaining E-first rows
force equality at I; exact matching of e's TWO E outputs removes EEWW
and leaves EWW or EWWE, as retained in the full table.

## 4. Actual old-stock four-L loop and early max birth

More than geometry is forced. In every retained row the exact ordinals
are

    T0(w)=alpha-3,
    T1(e)=alpha-2,
    T3(z)=alpha-1,
    T1(A)=alpha,
    T1(w)=alpha+1,
    T2(e)=alpha+2.

They follow from actual consecutive physical events

    w.R0 -> e.L1 -> z.L3 -> A.L1 -> w.L1 -> e.R2.

Thus the middle four departures are an ACTUAL uninterrupted L,L,L,L
square. It returns to e with the same incoming S heading, but it is not
a deletable state identity: its four cell colors have changed. It is
old stock and is not charged as a new root or permanent fuel.

Since w.R0 chooses H, the first-boundary definition gives

    B(H)<=T0(w)-1=alpha-4=B(G)-4.

This is an actual earlier birth of the specific first LEFT max neighbor,
not a new max component or a step in a proved infinite LEFT regress.
For completeness e's R0 chooses J, its R2 chooses H, and its L1-to-R2
span is exactly four. Optional e.L3 incoming N is retained; it does not
alter any displayed event or justify deleting a future source.

## 5. Scope and dependencies

The new conclusion is a local branchful propagation and chronology:
straight+LEFT max branch forces RIGHT+TWO LEFT max branches, and a
specific old-stock four-L cleanup with an earlier H birth. The branches
can be in the SAME maximum component. No general K1 exclusion, branch
payment, output-to-original-fuel identification or iterative regress
follows.

Signed dependencies:
K1_branches_force_bends.md SHA
57c354298337f3aa7e3b98ac44a0887729e473dc8c42264d737019ad5a631611;
K1_straight_max_branch_forces_right.md SHA
0d058388dbe1608810b7fdbc04b4bbe4a3bb1a5216396b18e3b207b8f374300a.
Control source SHA
d41292e3a6df68e3d917f005dce278c9b560a5867f6a6041e66b868c5faa4ef4;
control data SHA
096c4bc966ff688c5df49ff25079f8cd66a227111bd797103957cc9aee0baedd.
