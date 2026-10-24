# A forced late outward-record pattern at the remaining k9 scale

Status: independently audited exact finite geometry and analytic argument,
22 October 2026. Independent reconstruction: audits/check_k9_records_independent.py.
This lemma alone does not exclude the remaining scale.

Assume a finite-seed ant has the pure inflation p(9n)=3p(n),h(9n)=h(n).
Use the complete audited nine R images and nine L images from the k9 inventory.
Fix a direction in which the path has unbounded coordinate records; rotate
it to north. Let tau(Y) be the first read on row Y, where Y is larger than a
constant depending only on the finite initial black support. Write its pose
as (X,Y,N). Then

    tau(3Y) = 9*tau(Y),

and the 18 turns starting at that time are exactly

    RRLRRRRLR RLRLLLLRL.

In macro notation, the images chosen for the two coarse R turns at tau(Y)
and tau(Y)+1 are forced to be the two displayed nine-letter words. Thus this
necessary condition holds without any finite controller or periodic-choice
assumption.

## Proof

1. At the first visit to row Y all earlier coarse centers have height<Y.
   The current cell and its eastern neighbor are unvisited and initially
   white, for large Y. The next two coarse turns are therefore RR.

2. Enumerate every physically feasible pair of R images. If its combined
   read history has a first-L cell whose possible coarse owners all have
   relative height>=0, that cell is globally unread before this pair. It is
   not initially black once Y is large: every offset here is bounded and its
   absolute height is 3Y+O(1). Such a pair is impossible.

   The exact forward-ownership test leaves only five pairs:

     RRLRRRRLR / RLRLLLLRL;
     LLLRLLRLR / RLRRLRRRR;
     LLLRLLRLR / RLRLLLLRL;
     LLLLRRLLR / RLRRLRRRR;
     LLLLRRLLR / RLRLLLLRL.

3. Examine possible fine reads on row 3Y BEFORE the current macro. Every
   image in every heading has maximum northward offset at most3. Therefore
   only a previous coarse center on row Y-1 could reach row 3Y. Exactly four
   oriented images can do this:

     R image RRLLRLLLL, entering W: top reads L at offsets0,-1;
     R image RLRRLRRRR, entering W: top reads R at offsets0,1;
     L image LRLLRLLLL, entering E: top reads L at offsets0,-1;
     L image LLRRLRRRR, entering E: top reads R at offsets0,1.

   Each such macro ends with the COARSE northward step into row Y. By the
   definition of tau(Y), it can only be the immediately preceding macro.
   No earlier macro can have read this top row at all. The L-top alternatives
   require a first-L on a high initially white row, so are impossible. The
   R-top alternatives leave exactly the two black cells with horizontal
   offsets0,1 from the current scaled center. Otherwise that top row is white.

4. The first images LLLRLLRLR and LLLLRRLLR both require their local top-row
   cells at offsets0 and-1 to be black, read L first. The preceding possibilities
   give either no black cells or the pair0,1, never the required cell-1.
   Hence four of the five pairs are impossible. Only the stated pair remains.

5. Its first read at offset0 is R, which also excludes the preceding R-top
   alternatives. Thus NO fine read on row 3Y occurred before time9*tau(Y).
   At that time the head is (3X,3Y,N). Nearest-neighbor continuity then proves
   this is the first record on row3Y, establishing the claimed tau identity.

All arguments rotate covariantly to the other three coordinate directions.
The threshold Y may be chosen so the entire bounded pair footprint and top-row
checks lie beyond the initial support. No monotone retreat bound is used.

## What this does not say

The forced pair is genuinely renewable at the local level: its turn excess
is2, the same as coarse RR, and its first-L inputs lie behind the frontier.
It does not itself demand a fresh initial black bit. The lemma therefore
narrows a possible adaptive scale3 construction instead of ruling it out.
It only prescribes turns at scaled record times and should not be silently
extended to all record times, all boundary passes, or all macro occurrences.

The complete finite checks, including all five surviving pairs and all four
top-reaching oriented images, are asserted in `check_k9_record_pattern.py`
and saved in `k9_record_pattern.json`.
