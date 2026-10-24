# Bounded-mass binary chronology does not determine the live ant

Working result, 23 October 2026. This is an exact countermodel to a specified
cancellation-height relaxation, not an ant orbit or a highway counterexample.
Independent audit has been requested. No claim of literature novelty is made.

## The stronger relaxation

Put epsilon(x,y)=(-1)^(x+y), rho=epsilon*1_B, and

    Delta K(x,y)=K(x,y)-K(x-1,y)-K(x,y-1)+K(x-1,y-1).

Consider histories satisfying ALL of the following:

1. K_0=0 and B_0 is empty; at every finite time both supports are finite.
2. At every update exactly one previously zero plaquette is changed to one.
3. At every update rho=Delta K is a signed binary field, so B is an ordinary
   finite black set, and its complete alternating row and column sums vanish.
4. Every elementary height increment is itself a locally feasible ant face
   loop: it fills an entirely white positive-parity face, or erases an entirely
   black negative-parity face. Its four flips may therefore be interpolated
   as one literal RRRR or LLLL loop in the fixed sector.

These conditions retain the precise unit height increment, all intermediate
binary colors, and even local face-loop feasibility. They OMIT continuity of
one live cursor between the face loops and the prescribed location of the
cancellation at the live reduced-word endpoint. That omission is decisive.

## Theorem

There is an explicit infinite history satisfying 1--4 with black mass at most
12 at EVERY face boundary. The four-read interpolation also has mass at most
12. Infinitely many checkpoints have mass exactly four, with black cells the
four outer corners of an expanding rectangle. The height is always a zero-one
field. Every plaquette is eventually incremented exactly once.

In particular, adding the exact unit increment condition, binary validity at
every intermediate stage, a uniform working-mass bound, and pointwise
monotonicity to the existing endpoint-height relaxation still does not force
capture or even rule out endlessly expanding four-corner checkpoints. These
are not dynamically realizable ant states on one common orbit.

## Elementary face rule

For a plaquette with lower-left corner (a,b), Delta 1_face has corner signs
+,-,-,+. If a+b is even, these match epsilon at all four corners, so adding
this plaquette is valid exactly when all four current bits are zero, and it
fills them. If a+b is odd the signs are opposite epsilon, so the increment is
valid exactly when all four bits are one, and it erases them.

A uniform white square is traversed by an R^4 loop; a uniform black square by
an L^4 loop. For a positive face, start at its lower-left corner heading west; for a
negative face, start at its lower-left corner heading south. Both choices have
the common sector sigma=-1 under rho=-sigma*chi*1_B. During either loop bits are flipped
one at a time monotonically, hence interpolation cannot exceed the larger
endpoint mass. There is no claim that the ending pose of one chosen face loop
is the starting pose of the next loop.

## Odd-strip construction

A vertical strip of h consecutive plaquettes, where h is positive and odd,
and whose bottom face has positive parity, is built as follows:

- Fill its bottom face.
- For j=2,4,...,h-1, fill face j and then erase face j-1.

After each pair, K is the full initial odd-length strip and the only black
cells are its four outer corners. A new positive face has disjoint vertices
from the current strip. Filling it temporarily gives eight black cells; the
intervening negative face is now all black and can be erased. Thus the entire
strip needs at most eight black cells. Each of its h faces is used once.

## Expand any odd rectangle by two columns

Suppose K is the indicator of

    Q=[a,a+w-1] x [b,b+h-1],

where w,h are odd and a+b is even. Its binary field has only the four corners
(a,b),(a+w,b),(a,b+h),(a+w,b+h) black.

To expand right, first build the vertical strip at x=a+w+1, y=b,...,b+h-1 by
the preceding construction. Its bottom face has positive parity. Its vertex
set is disjoint from the original four corners. The old four cells plus the
strip construction use at most 4+8=12 black cells.

Now the two width-one-boundary columns x=a+w and x=a+w+1 have black pairs
only at y=b and y=b+h. Fill the missing bridge column of plaquettes x=a+w:

- For j=1,3,...,h-2, fill its face at y=b+j and erase the face at y=b+j-1.
- Erase its last face at y=b+h-1.

The filled faces have positive parity; each is all white when used. The
subsequent negative face is all black. A black horizontal pair propagates
upward, while the top pair waits. There are eight black cells before each
fill, at most twelve immediately after it, and eight after its erasure.
The final erasure leaves four outer corners. This also covers h=1: only the
last bridge face is erased.

Every one of the new 2h plaquettes is incremented once. The final height is
exactly the larger rectangle's indicator. The same construction at x=a-2,
with bridge x=a-1, expands left. Exchanging x and y gives upper and lower
expansions. The mixed difference is symmetric under this exchange; no
reflection symmetry of the actual ant is presumed.

## Infinite sequence and exact scope

Start by filling the face (0,0). For n=0,1,2,... maintain a checkpoint

    K=1_{[-2n,2n] x [-2n,2n]}.

Expand left by two, right by two, down by two and up by two. The next
checkpoint is n+1, and every intermediate rectangle retains odd side lengths
and positive lower-left parity. The proof above gives the uniform mass bound
12. The checkpoints exhaust the plane. Each finite state has finite support;
the limiting height is one everywhere, which does not have finite support.

Each state has zero alternating row and column charges. If desired, a fixed
formal head pose can be attached at all face boundaries, with unchanged
head-correction arrays. Non-axis exponential board clocks see each positive
Delta increment with the usual positive quadrant sign, so those endpoint
clock tests are also compatible with this schedule. No actual head motion
is supplied between the remote face loops. In particular this does NOT
contradict finite-seed ant unboundedness, eventual mass at least five, or
any stronger all-time ant theorem.

The missing hypothesis is not merely positivity, binary admissibility,
working mass, integer rate, or local loop realizability. It is the spatially
continuous chronological coupling to ONE live ant and its reduced word.
A global bridge must retain that coupling or replace it by a genuinely
sufficient invariant.

## Verification

`check_unit_height_schedule.py` independently implements the displayed face
operations, checks all four input bits before every flip, checks the complete
Delta K identity and zero row/column margins, and checks the rectangle
identities and uniform mass bound through a finite expanding-square control.
The all-size argument is the construction above, not that finite control.
