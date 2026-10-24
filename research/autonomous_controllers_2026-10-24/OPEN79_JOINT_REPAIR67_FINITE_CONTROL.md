# A genuine joint 67-read repair-and-consume control

24 October 2026. Positive finite control for independent replay. This is
separate from the all-length conditional proof 5f8af474, which is unchanged.

The entire newly forced local mechanism is physically realizable as ONE
finite factor, not merely a collection of separate port examples.

Start at (2,1), incoming S, with exactly these 18 BLACK cells:

    (-5,2), (-5,3), (-4,1), (-4,4), (-3,0), (-3,5),
    (-2,1), (-2,2), (-2,4), (-2,5), (-1,1), (-1,2),
    (-1,5), (0,1), (0,5), (1,1), (1,3), (1,4).

Every other cell is WHITE. The literal word is

    RLRRLLRRLRRLRRLRRRRLRLLRLLRLLLLRLLRLRLLRLLLLRRRRLRLLRLLRRRRLLRLLLLR

It has exactly 67 reads. The salient complete physical read histories are:

    U=(0,1):  4 N/L, 16 S/R, 64 N/L.
    V=(-1,1): 5 W/L, 17 W/R, 53 E/L, 61 E/R, 65 W/L.
    C=(-1,0): 6 S/R, 62 S/L, 66 S/R.
    B=(0,0):  3 W/R, 63 E/L.

Thus both guides are genuinely restored at16/17. V's two higher first
returns cost36 and8 steps. The next C return occurs at62, followed by the
four-step C,B,U,V square and C's R at66. Every intervening read from7
through61 has normal level 3y-x+11 at least13. X and A are not revisited.
The displayed named anchors match ranks X0, A2, B8/9 and C8/9/10.

The COMPLETE final BLACK support is

    (-5,1), (-5,2), (-4,2), (-4,3), (-3,1), (-3,4),
    (-2,3), (-2,4), (-1,0), (-1,2), (-1,3), (0,3),
    (0,4), (1,0), (2,1).

The final head is at(-2,0), incoming W. Mass is18 ->15. The checker records
all67 actual reads and every L read's actual previous R owner or its
explicit initial BLACK input. All18 initial BLACK lifetimes are consumed;
none is ignored as unread auxiliary stock. In particular B's L at63
consumes its R-born lifetime from3, U's L64 consumes restoration R16, and
V's L65 consumes R61. V's intermediate L53 consumes restoration R17.

## Scope

This control proves that mandatory guide repair plus the forced consumption
square is not an empty local interface. It does NOT complete all79 named
events, their earlier/later history, the full drift-orbit ordering of the
higher classes, or the full eight-cell odd output inventory. Its18 prepared
BLACK inputs are not erased from the resource accounting. The endpoint
pose differs from the start, and no translation-repeat or regeneration
relation is asserted.

The positive word came from a bounded beam search extending the already
frozen U-restoration factor. That search's width/depth limits are discovery
metadata only; no absence or shortestness conclusion is used here. The
independent replay certificate needs only the literal word and complete
fields printed above.
