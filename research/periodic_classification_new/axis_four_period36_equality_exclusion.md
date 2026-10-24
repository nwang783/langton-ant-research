# The remaining axis-four packing equality is not a white front

23 October 2026, 09:27 UTC. Analytic/computational candidate; independent
review pending. This is an equality-case proof leading to a necessary
ALL-CAP period bound40, not an unrestricted axis-four front exclusion.

Dependencies: signed KR (axis-four cap-five exclusion), signed LC
P>=4n+8 and four/eight first-return theorem, and the separate pending
four/eight/twelve lemma that any FIVE physical first returns cost>=32.
No claim here is promoted until all these dependencies and the equality
replay have independent signoff.

Let a complete WHITE front have actual full drift(4,0). KR supplies a
full-drift cell class with complete multiplicity n>=6. Signed results give
P>=36, and P is divisible by four. AssumeP=36. If n>=8, LC's4n+8 already
contradicts36. For n=6 or7, let r count its nonzero cyclic phase gaps.
Their integer windings sum1, so their absolute sum S is odd and S>=r.
Each zero gap costs>=4 and each nonzero gap costs>=8 times its absolute
winding.

For n7, r1 leaves six physical zero returns; five successive4/8 returns
are impossible, so one of the six costs>=12, giving32+8>=40. At r2, S>=3
and the cost is at least24+20=44. At r3 it is at least24+16=40. At r>=4,
the weaker bound8r+4(7-r)>=44 suffices. Thus n7 is impossible atP36.

For n6, r1 leaves five physical returns costing>=32, hence total>=40.
At r2, S>=3 gives24+16>=40. At r>=4,8r+4(6-r)>=40. Only r3 remains.
EqualityP36 then forces exactly three zero gaps of length4 and three
nonzero gaps of length8, with winding multiset{+1,+1,-1}. This is an exact
classification of the putative equality, not a generic word-period scan.

## Complete finite equality replay

Cut the cyclic word just before its UNIQUE negative winding gap. The other
five gaps consist of two positive windings and three zero returns. There
are exactly10 possible arrangements. Fix the common physical cell as the
origin and retain all FOUR incoming headings; no reflection symmetry or
primitive quotient is used.

For a zero gap, enumerate every4-step turn word with first return to the
full-drift class at its endpoint: there are4 programs per incoming heading.
For a positive or negative winding gap, enumerate every8-step turn word
with endpoint(plus-or-minus4,0) and no earlier same-class return: there are
6 programs per heading per sign. No color restriction is silently imposed
at the individual macro level.

`check_axis_four_period36_equality.py` explicitly composes all

    10 *4 *4^3 *6^3 =552,960

program sequences. Their entire36-step paths are retained for each check.
Exactly276,480 restore the incoming heading. For each physical read p=(x,y)
at time t, write x=r+4k with r in{0,1,2,3}; its COMPLETE chronological time
at representative(r,y) is t-36k. Sorting these actual physical times, not
cyclic ranks or time residues, must give R,L,R,L,... from white.

Exactly4,320 heading-restoring words pass this test at the chosen common
class. NONE passes at every class. This checks all translated predecessor
histories, including negative-period events; it is not a one-word
white-input simulation with an initial-head exception.

Author result check_axis_four_period36_equality.json has all macro counts
and rejection totals. The independent replay must regenerate the macros,
layouts and complete physical histories rather than trust these totals.
A SAT word would be retained verbatim; there are none in this exact case.

ThereforeP36 is impossible, and the necessary all-cap white full-axis-four
period bound isP>=40. Genuine quarter rotations give the other axis-four
signs/directions. This does not exclude periods40 and higher, arbitrary
axis-four multiplicity, or general nonperiodic finite-seed trajectories.
