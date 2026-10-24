# Exact capped axial transport of one black domino

23 October 2026, 06:23 UTC. Independently signed complete-field induction (JZ),
including both literal caps and the growth addendum. This is a finite prepared-rail operator, NOT a renewable
builder, translating front, fixed growing root, or finite-seed counterexample.

## Literal transition

For r>=1 start at(0,0,E), with exactly the black cells

    I_r = {(x,0): 0<=x<=2r} union {(-1,1),(2r,1)}.

Every other cell is white. The literal ant word is

    G_r = (LRRL)^r LLLR (RLLR)^r RRRL.

It has length8r+8 and returns to exactly(0,0,E). Its COMPLETE output is

    O_r = {(x,0): 0<=x<=2r-1}
          union {(-2,0),(-2,1),(-1,1)}.

Thus both input/output masses are2r+3. The COMPLETE XOR is exactly

    {(-2,0),(-2,1),(2r,0),(2r,1)}.

The unchanged rod and fixed near marker supply a prepared rail. The operator
moves a vertical black domino from x=2r to x=-2, leaving all other cells
unchanged. Its read support is exactly the two-row rectangle
[-2,2r] times {0,1}, of size4r+6. There is no external reset or omitted cap.

## Four literal stages, proving every r

1. Each LRRL, entering E at(2i,0), reads

       (2i,0)L, (2i,1)R, (2i+1,1)R, (2i+1,0)L.

   It moves(2,0), preserving E. The r copies erase row0 on[0,2r-1]
   and fill row1 on[0,2r-1], leaving the far input domino intact.

2. LLLR reads

       (2r,0)L, (2r,1)L, (2r-1,1)L, (2r-1,0)R.

   The first two are the supplied far domino; the next two have exactly the
   colors left by stage1. It ends at(2r-2,0,W).

3. Each RLLR, entering W at(x,0), reads

       (x,0)R, (x,1)L, (x-1,1)L, (x-1,0)R,

   and moves(-2,0), preserving W. For x=2r-2,...,0 all required colors
   are supplied by stage1, except the last upper cell(-1,1), which is the
   fixed input marker. The r copies end at(-2,0,W), restore black row0
   on[-1,2r-2], and erase row1 on[-1,2r-2].

4. RRRL reads

       (-2,0)R, (-2,1)R, (-1,1)R, (-1,0)L.

   The first two are fresh white, and the last two have the colors just
   supplied by stage3. These moves return to(0,0,E), add the left domino,
   restore the marker(-1,1), and erase the temporary lower cell(-1,0).

This proves actual chronology, every input requirement, and the COMPLETE
output. No depth cutoff or white-input front inference is used.

## Why this is a useful positive boundary control

It realizes arbitrarily long closed-pose intervals with just FOUR net changed
cells, separated horizontally. Their convex hull is exactly the read rectangle,
consistent with the signed closed-pose hull identity. It demonstrates why the
bounded-write strip theorem excludes OBLIQUE separation but must retain axial
separation. The initial black mass grows with r and the fixed rail remains
present; no contradiction to any finite-fuel or small-total-mass result occurs.

It also supplies both finite caps for this particular opposing-drift bulk pair.
In contrast to a generic inverse-front claim, every cap bit is included in I_r
and its evolving field is checked explicitly. It does not regenerate I_(r+1),
and the resulting field cannot simply be rerun as the same input. Constructing
an autonomous repeated operation would require a separate compatible complete
field and head transition, with the invariant pose sector respected.

## A second exact cap: a four-cell growth excursion

There is a closely related literal positive-growth contract, also for all r>=1.
Remove the far upper black cell(2r,1) from the preceding input, and replace
LLLR by the eight-turn cap LRRRRLLR. Thus use

    J_r = {(x,0): 0<=x<=2r} union {(-1,1)},
    H_r = (LRRL)^r LRRRRLLR (RLLR)^r RRRL.

It starts and ends at(0,0,E), has length8r+12, and its COMPLETE output is

    J_r union {(-2,0),(-2,1),(2r+1,0),(2r+1,1)}.

Thus the input/output masses are2r+2 and2r+6. The complete XOR consists of
FOUR newly black cells: two separated vertical dominoes. All old cells restore.

The modified far cap, relative to(2r,0), reads

    (0,0)L, (0,1)R, (1,1)R, (1,0)R,
    (0,0)R, (0,1)L, (-1,1)L, (-1,0)R.

It leaves the initial lower far cell black, restores the white upper far cell,
adds the new right domino, and joins exactly the same return port(-2,0,W)
relative to the far position. The outbound/return/near-cap stages from the
main proof therefore apply unchanged. This proves every r with no reset.

This is an actual finite closed-pose growth step, not a regenerative family:
the two added dominoes modify the next near and far interfaces. In particular,
the next iteration cannot silently reuse the same RRRL near cap, whose first
read at(-2,0) is now black rather than white. Any attempted phase cycle must
carry these changed endpoint states explicitly. The rod itself is prepared
and has2r+1 black cells; this is not a bounded-total-mass example.

## Actual continuation of the simple growth seed

The separate independently signed `domino_growth_capture.md` proves that every
J_r with r>=20 actually enters a104 highway at time60r+777, with pose
(2r+2,7,N) and subsequent drift(-2,2). This is an exact all-r/all-future
chronology certificate, not an extrapolation from the closed first excursion.
Thus this precise tempting growth family is no longer a renewal candidate.
Other initial endpoint/controller patterns are not covered by that result.
