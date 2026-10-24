# Structure immediately above the singleton axis boundary

23 October 2026, 04:08 UTC. Independently signed analytic continuation.
The lower singleton theorem remains independently signed separately.

Normalize full drift (+2,0), with bottom A=(0,0), B=(1,0), and C=(0,1),
D=(1,1) immediately above. The bottom classes each have one visit. C and D
have a common complete history length n. Let r be D's sole downward rank,
and s C's sole incoming-N rank. All other C arrivals are S, all other D
departures N. Thus their marks are singletons.

## Period and first rank

P is divisible by four: half the moves are horizontal, and their signed
sum is two, so P/2 is even. P=4 would have two horizontal E moves and two
opposite vertical moves, visiting four distinct classes modulo (2,0).
Each would have to be a singleton R, inconsistent with the non-square
axis translation. Hence P>=8.

The signed first-downward-rank argument from
`axis_two_read_extreme_obstruction.md` uses only P>4, not m>=2, at its first
step. It therefore applies here and gives

    r even,                 s=r+2.                    (1)

In particular n>=r+3. C's input history is S^s N S^(n-s-1); D's input
history is the baseline W,E,W,E,... with its even rank r changed W to E.

## Exact lower-strip top-port map

Use third-row representatives C'=(1,2), D'=(2,2), so horizontal E edges
C'->D' have seam zero and W edges have seam -1. There are m=n-1 arrivals
into the already built strip from D', and m outputs back to C'. Order the
input ports by C's S ranks and the output ports by D's N ranks. The exact
successor paths induce the permutation

    pi(r)=r+1, pi(r+1)=r; all other pi(j)=j.

The path from input j to output pi(j) has length three, except j=r+1,
whose length is seven. Its full-drift voltage beta_j is

    j mod 2       for j<=r+1,
    1-(j mod 2)   for j>r+1.

This follows by direct E/W ordinal matching. Away from ranks r,r+1,r+2,
C_k goes to D_k. C_r goes W to D_(r+2), while C_(r+1) goes E to D_r,
through the bottom singleton to C_(r+2), then E to D_(r+1). Removing C's
non-input rank r+2 and D's non-output rank r swaps adjacent port ordinals
r,r+1 and flips the later ordinal parity.

## The sole downward rank is at most two

If r>=4, the first four lower-strip input ports j=0,1,2,3 have pi(j)=j,
length three, and literal compass words S,W,N for even j and S,E,N for
odd j. These are precisely the four ordered lower excursions used in the
proof of `axis_singleton_extreme_theorem.md`. That proof uses no later
port and no upper multiplicity cap: its ballot and eight-step first-return
argument gives a contradiction from these four excursions alone.

Therefore r is either zero or two. This is an all-cap restriction on the
second row. It does not yet bound n: the allowed forms are

    r=0: C has its sole N at rank 2, with n>=3;
    r=2: C has its sole N at rank 4, with n>=5.

Finite symbolic tests suggest n=4 or5 may be the only extendable cases,
but that stronger statement is NOT asserted. All arbitrary-suffix and
finite-multiplicity solver results retain their actual status.
