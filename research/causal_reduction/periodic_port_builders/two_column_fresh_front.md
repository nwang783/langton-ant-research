# A white frontier cannot remain in a two-column moving window

Status: independently audited elementary lemma,22October2026.
This is a small local obstruction, not a general highway or axial-front theorem.
It is a direct use of the two-column ladder geometry, not a new global resource.

Let column x=0 be entirely unread and white, with the ant entering at(0,y,E).
Until it first reaches x=1, require every read and pose to remain in columns
-1 and0. Column-1 is arbitrary. If the ant does reach x=1 under this rule,
then for some integer d>=0 its exact turn word is

    (RRLL)^d RRRR (LLRR)^d LR,

and its endpoint is(1,y+1,E). The now-completed column0 has exactly two black
cells, at heights y+1 and y-2d-1. No assumption on the rest of column-1 is
needed beyond feasibility of this displayed finite word.

Proof: the fresh-column entry gives RR and returns west to column-1 at y-1.
To avoid escaping west of column-1, the old column must reflect using either
LL or RR. An LL pair moves the next fresh-column entry two levels downward,
where both new cells are still white. This repeats the RRLL descent. A mixed
old pair escapes west and is forbidden. The first feasible RR reflection
ends the descent. It restores the head to the lowest fresh-column entry.
Every subsequent ascent is forced: LL erases one intervening new-column pair,
and RR restores one old-column pair previously erased during descent. At the
last old-column reflection, a black top neighbor would instead cause a forbidden
west exit; conditional on advancing, this final pair must also be RR. At the
original entry height, L at the original black site and R at the fresh site
above it transmit east. Tracking the new-column pairs leaves precisely the
two stated endpoint black cells. If descent never stops, there is no advance;
on a finite-support board it cannot continue forever through old black pairs.

Now suppose column1 is also unread and white. From the displayed endpoint,
the next four turns are forced RRRL:

- RR on column1 reaches column0 at height y, heading W;
- that site is white, so R reaches its black upper neighbor at height y+1;
- L moves west to column-1.

The rightmost visited column is now1, but the ant has reached column-1, two
columns behind it. It has not entered column2. Consequently no finite-support
orbit escaping to the right can eventually stay within just the current
rightmost column and its predecessor. This holds at arbitrary vertical height
and with an arbitrary finite initial field. Rotating gives all four directions.

The calculation also checks the crossed-column mod4 charge: the two deposited
black sites have the same vertical parity, so their alternating sum is2 mod4.
This differs from a complete right excursion returning left, whose change is0.

Independent analytic review and literal depths0..150: audits/check_two_column_and_dcv_controls.py/json.
