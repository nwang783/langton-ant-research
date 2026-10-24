# Coupled quotient-visit and full-drift period packing

23 October 2026, 08:38 UTC. Independently reviewed structural consequence.
This strengthens and supersedes the earlier four-step-only numerical bound.

For ANY heading-restoring quarter-turn walk of periodP and actual full
drift d with D=||d||infinity>=2, if one full-drift quotient cell has n
occurrences in the event cycle, then

    P >= 4(n-1)+2D.                               (1)

No white-input premise or local cap is needed for (1). Cyclic EVENT phases
are used, not an assertion that the physical chronological read ranks fit
inside one period.

Arrange this class's phases cyclically and follow the actual lifted walk
from one occurrence to the next, wrapping to the first phase in the next
period. Let the gap lengths be l_i>0 and their physical displacements
k_i*d. Then

    sum l_i=P,       sum k_i=1.

Because d has even coordinate sum, each gap has even length. Half its
moves are horizontal and half vertical by compulsory axis alternation.
A nonzero k_i therefore costs

    l_i >= 2D*|k_i|.

A zero k_i is a nonempty physical return and costs at least4. If r>=1
gaps have k_i!=0, then sum|k_i|>=r, and

    P >= 4(n-r)+2D*sum|k_i|
      >= 4n+(2D-4)r >= 4n+2D-4.

This proves (1). At D2 it reduces to the previous P>=4n. At larger drift
it accounts for the compulsory winding gap that cannot be a four-step
physical return. Heading parity separately gives P=2*d_x mod4.

## Consequences from the signed white-front inventory

A supplied-drift visitcapC exclusion forces some class to have n>=C+1.
Combining it with (1) gives an ALL-CAP period lower bound

    P >= 4C+2D.

Thus signed KR gives fullaxis4P>=28, KS gives full(5,±1)P>=26, KW gives
full(4,4)P>=24, the earlier full(4,±2)cap4 result givesP>=24, and the
full(2,2)cap6 result givesP>=28. The earlier odd-odd D3 cap4 cases give
P>=22. Genuine rotations preserve these statements. These are neither
primitive quotient claims nor exclusions of arbitrary larger periods.

More generally the signed unrestricted cap3 exclusion forces n>=4, so
every hypothetical white front with D>=2 has

    P >= 2D+12.

The D1 cases are already all-cap excluded separately. This improves the
retained g>=8 plus turn-flip bound P>=2D+8 where no stronger supplied-drift
multiplicity result is available. It is not a minimal104-period theorem
or a proof of eventual periodicity/capture.
