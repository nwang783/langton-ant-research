# Structural exclusion of period26 for complete white fronts

23 October 2026, 09:53 UTC. Analytic/computational candidate; independent
review pending. The intended conclusion is the necessary ALL-CAP bound
P>=28, not standard104 minimality, an all-front classification or capture.
This is a finite equality reconstruction AFTER unrestricted structural
bounds, not a generic bounded-period search interpreted as a full proof.

Dependencies already independently approved: universalP>=26 (LC), complete
white n>=4,D>=3 boundP>=4n+2D, signed small-drift exclusions, and the new
cap-four first-read backbone boundP>=6D+4ceil(D/3). Full period and full
supplied drift are retained; reflections and primitive quotients are not used.

## Only three supplied drift families can attain26

Assume an initially-white complete translating front hasP=26. Heading reset
makesP even and full drift have even coordinate sum. The signed cap-three
exclusion and white packing bound imply some n>=4 andP>=2D+16 forD>=3,
soD<=5. D1/unit-diagonal and fullunit-axis cases are all-cap excluded.
The remaining D2 diagonal requiresP>=28 by its signed cap-six exclusion.

EveryD4 vector is cap-four excluded by the signed inventory, hence some
n>=5 andP>=4*5+8=28. AtD5, P26 and4n+2D imply EVERY class has n<=4;
but the independently approved cap-four backbone bound then givesP>=38.
ThusD3 alone remains. Genuine quarter rotations reduce it to full(3,1),
(3,-1),(3,3); the first two chiralities must be checked separately.
Each is cap-four excluded, so some class has n>=5. Its white packing bound
4n+6<=26 gives exactlyn=5.

## Exact five-gap classification

For its cyclic class gaps, let r count nonzero windings and S their absolute
sum. Since the signed winding sum is1, S is odd andS>=r. Each zero gap costs
at least4, and each nonzero gap costs at least6 times its absolute winding.

- r1: the winding gap is at least6 and the four physical first returns at
  least16. Four consecutive four-step returns are impossible. To total26,
  the winding must cost6 and zero gaps must be three4's and one8. A winding
  gap of10 would require four forbidden four-step returns.
- r2: S>=3, costing at least18+12=30, impossible.
- r3: equality26 forces winding multiset{+1,+1,-1}, all three gaps of6,
  and two zero gaps of4.
- r>=4: S>=5, costing at least30, impossible.

No other gap structure can occur. These are two exact equality types.

## Complete physical-history replay

Producer check_global_period26_equality.py regenerates ALL geometric macro
programs with no individual white-input assumption: four physical4-return
programs, TWENTY geometric8-return programs, and either3 (drift3,±1) or1
(drift3,3) extremal6-step programs per heading per winding sign. The larger
geometric8 inventory intentionally includes color-inconsistent programs;
complete chronology later rejects them, so none is accidentally omitted.

Type1 cuts at its unique winding and has4 choices for the8-return position.
Type3 cuts at its unique negative winding and has6 layouts of the remaining
two positive windings and two zero returns. All FOUR incoming headings
are kept. The complete compositions and rejection totals are

    full(3,1):  71,808 programs;35,904 heading-restoring;1,131 central-white;
    full(3,-1): 71,808 programs;35,904 heading-restoring;1,131 central-white;
    full(3,3):  20,864 programs;10,432 heading-restoring;  329 central-white.

NONE has complete white histories at every class. For a physical event at
time t and position(x,y), write x=r+3k,0<=r<3. Its chronological time at
representative(r,y-k*b) is exactlyt-26k, where full drift is(3,b). Sorting
these complete unfolded physical times and requiring R,L,R,... includes
all negative/positive translated period histories. It is not a one-period
white-board simulation with an initial head.

The result file check_global_period26_equality.json records all macro
counts, both equality types and their rejected totals. Independent replay
must rebuild geometric macros and physical histories rather than import
the producer or trust these totals. Any surviving word would be retained;
there are none.

If all dependencies and this complete replay are independently confirmed,
period26 is excluded. SinceP is even and already>=26, every nonzero complete
WHITE translating front then hasP>=28, at all drift/width/multiplicity.
This asserts no realizability at28, no external priority or104 minimality,
and no eventual-periodicity or finite-seed capture conclusion.
