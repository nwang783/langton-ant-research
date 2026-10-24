# Geometry forced by hypothetical four-black recurrence

Status: the endpoint and first-collision geometry in Sections 1–3 is proved
from the axial charges and clock-forcing theorem established in this
continuation. The later scattering program is conditional on separately
verified all-parameter collision certificates. No four-black recurrence or
non-highway trajectory is constructed here.

## 1. A fixed recurrent pose and four escaping cells

Assume a finite-seed orbit has infinitely many times with exactly four black
cells. The axial separator bound puts all such heads in a fixed finite box.
Pass to an infinite subsequence with one fixed pose, and translate and rotate
that pose to `(0,0),N`. The normalized sector is then `sigma=+1`.

The sharp forcing theorem in `../chronology/low_mass_recurrence.md` says that
all four critical clocks tend to positive infinity along this sequence. The
head terms are fixed. Write `z=x+y`, `u=x-y`, and `chi=(-1)^(x+y)`.

There must eventually be exactly two cells of each checkerboard sign. The
two cells with `chi=-1` supply the positive terms of both z-clocks. One has
`z` tending to negative infinity and the other has `z` tending to positive
infinity. Indeed, the positive z-clock sum tending to infinity forces the
larger of their z-values to tend to infinity, and the negative z-clock does
the same for the negative of the smaller value. The two `chi=+1` cells have
u-values tending to opposite infinities by the identical argument for the
u-clocks.

Consequently **all four cells leave every fixed bounded set**. At these
checkpoints the ant therefore follows an arbitrarily long literal prefix
of the blank trajectory.

## 2. The first far collision

There must be a first collision with one of the four initial black cells.
Otherwise the complete future head trajectory equals the blank highway and
eventually leaves the bounded checkpoint-head box permanently, contradicting
the assumed future four-black checkpoints.

The collision times tend to infinity. The standard blank highway has drift
`(-2,-2)`, so the collision cell q has bounded u-coordinate and z tending to
negative infinity. It is therefore the `chi=-1` cell with negative-diverging
z. The other `chi=-1` cell d has z tending to positive infinity. The other
two cells have u tending to opposite infinities. In particular all three
other cells become arbitrarily far from q.

Write q=(l,b). Since u(q) stays bounded, both l and b tend to negative
infinity.

## 3. Remote line charges force an exposed southwest L-corner

Choose a fixed integer D containing the original seed, original head and
normalized checkpoint head in `[-D,D]^2`. Every row or column outside this
box has signed black sum zero modulo four at every checkpoint: it started
empty and its two endpoint heads are on the same side. This is the axial
charge theorem, and uses the fixed original initial state rather than any
unproved reachability of arbitrary endpoint configurations.

For large checkpoints, q's row b and column l are outside this box. Each
contains an even positive number of black cells. Neither can contain all
four: if all four were on q's row, q's column would contain only q, and
conversely. Hence each contains **exactly two**, with opposite alternating
signs because its signed sum is zero modulo four.

It follows that the four cells have the exact form

    q=(l,b),  a=(l,t),  c=(r,b),  d=(s,v),

where a,c have checkerboard sign +1 and q,d have sign -1. Put
`H=t-b`, `W=r-l`. Then

    u(a)=u(q)-H,   u(c)=u(q)+W.

Since u(a),u(c) tend to opposite infinities, H,W either both tend to positive
infinity or both tend to negative infinity, after passing to a subsequence
of either possible assignment.

The negative alternative is impossible. In that alternative all x- and
y-coordinates of q,a,c tend to negative infinity. Any coordinate of d greater
than D would occur in a remote row or column without another black cell,
violating its zero charge. Thus both coordinates of d would be at most D,
contradicting z(d) tending to positive infinity.

Therefore

    H -> +infinity,   W -> +infinity.

Moreover d cannot share q's column l or row b, since those already contain
two cells and a third gives an odd signed sum. Any x-coordinate of d outside
the fixed box must be r, and any y-coordinate outside the fixed box must be
t. Thus

    s in {r} union [-D,D],   v in {t} union [-D,D],

and consequently

    s-l -> +infinity,   v-b -> +infinity.

The first far collider q is therefore an exposed southwest corner. Its two
axial partners are arbitrarily far north and east of it, and the fourth cell
is arbitrarily far northeast of it. This is stronger than merely knowing
that all four cells escape.

This does **not** force a rectangle for an arbitrary initial input. If one
of r,t lies in the fixed charge box, d may have a different bounded coordinate
on that axis. Rectangular shape follows once both r and t escape the box,
because their remote line charges then force d=(r,t).

## 4. Consequence for ordinary one-black scattering

The admissible first-contact fresh phases are
`14,28,32,38,46,56,60,62,70,72`, relative to the blank entry at time 9977.
Nine are ordinary channels with a uniformly bounded recovery neighborhood
and an outgoing SW, NW or SE highway. The established canonical one-bit
certificates can exclude the other three initial cells from each of these
traces. The independent full proof and numeric guard constants are being
recorded by the chronology analysis in `mass4_first_collision*`.

The geometric reason is simple: the finite recovery cannot reach cells whose
distances from q diverge. For a SW output, the relative x,y coordinates are
bounded above along the whole future trace, whereas each remaining cell has
at least one positive-diverging relative coordinate. For NW or SE outputs,
the relative z-coordinate is bounded, while the other cells have relative
z equal to H, W, and (s-l)+(v-b), all tending to infinity.

Thus the only first collision that can survive four-black recurrence is the
exceptional phase-72 shuttle. Its far recovery reverses toward the old blank
debris; it is not covered by the preceding outgoing-ray exclusion.

## 5. A targeted exceptional chain, now with an all-parameter certificate

Primary one-black sources show that the phase-72 shuttle returns to a bounded
historical region and then leaves NW. Literal certified probes give its next
phase-72 fresh ray as `x+y=8`. The first exceptional cell lies on
`x-y=-19`. The only possible second distant collider is a=(l,t). Requiring
this second hit also to be exceptional therefore gives

    q=(-33-2n,-14-2n),  a=(-33-2n,41+2n),

up to the displayed choice of depth origin.

Exact literal simulations first suggested that this two-bit seed leaves SE,
with outgoing phase-72 ray `x+y=-6`. The subsequent affine-field verifier
proves that statement for every integer n>=200, including the entire
generated archive and infinite future.
If the third collision is also forced exceptional, it must be

    c=(8+2n,-14-2n).

Both c's column and a's row then escape the charge box, forcing the last cell
to be d=(8+2n,41+2n). Thus the proposed residual four-cell family is

    {-33-2n,8+2n} x {-14-2n,41+2n}.

Its widths are 4n+41 and 4n+55. The theorem in
`exceptional_rectangle_proof.md` now proves an exact NW highway from this
entire four-cell family for every n>=200. The fourth corner is never read.
The same affine calculation supplies exact one-bit and two-bit parent tails,
prefix read bounds and full-archive support bounds. Ordinary second- and
third-hit exclusions still have to be justified as part of the reduction,
retaining all older wake and debris; the separate chronology guard and
canonical-core audit notes establish the needed interfaces.

