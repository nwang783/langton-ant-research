# Mixed LL zero-chord bridges and the critical last-LEFT gate

24 October 2026. Complete WHITE cap-four translating front, actual full
P,d. An actual b-circle has constant selected C height c. For the critical
chronology conclusions assume c=c_right+1. The 144-row inventory assumes
no incident cycle edge is single-used; the critical last-LEFT gate itself
does not need that hypothesis. Author proof pending independent review.
Older stock and all odd-output alternatives remain.

## 1. Complete mixed LL junction, not the constant-two shortcut

Take the physical b subpath

    B=(1,1) -> Y=(0,1) -> Z=(0,0) -> A=(1,0).

Both LEFT contacts have physical flow two. The preceding/following RIGHT
may enter from or exit to a 3/4 macro. The full no-one-use endpoint alphabet
for this stencil is

    Z: NSS, NNSS, NSSN; Y: EWW, EEWW, EWWE;
    A: EEWW, EWWE, EWE, EWEW;
    B: SSNN, SNNS, SSS, SSSS.

All 144 complete choices retain physical/zero ports, all ordinal edges,
exact next-read returns, all rank clocks and dual heights. There are 72
port failures, 21 skipped-rank failures, 12 clock contradictions and 39
necessary OPEN rows. They split exactly into

    the THREE old flat-end rows c3f16bb3; and
    all 36 rows A in{EWE,EWEW}, B in{SSS,SSSS},
              with BOTH LEFT choices independently O/U/V.

The latter four parent endpoint pairs are source/sink3/4 gates, not
constant-flow-two RIGHT contacts. Their missing A->B N edge has total
flow ZERO at both ends. The intervening L face has h=c-2, and the C face
on that chord's right has h=c-2 too: a genuine height-two C notch. At the
old flat ends that C height is c, so the same chord has flow two instead.
Thus the older forced four-L square/second-LEFT-V argument cannot simply
be carried into a mixed bridge.

The 39 rows are local necessary port/clock/stream models, not a filled
one-event orbit or completed WHITE front. The executable control exposes
all physical channels and all remaining incoming/outgoing exterior ports.

## 2. Actual critical chronology restores second LEFT V

Suppose a crossing contact v is SECOND in an LL pair. Multiplicity is
preserved at LEFT contacts, so its predecessor u has the same flow.
Crossing profiles are WEE/WEEW at flow two, or WEEE at flow three, by the
signed mixed first-track table d5acded4.

If u is also a crossing, first ordinal matching gives

    T1(v)=T0(u)+1 <= T1(u)-3,

while second ordinal matching gives

    T2(v)=T1(u)+1 < T2(u).

Thus v's actual LEFT interval starts before u's L1 and contains that
crossing event. This contradicts the critical same-contact disjoint
interval pipeline. No exterior reader can fit into the exact one-edge
ordinal transitions.

The only noncrossing predecessor with the same flow is LEFT V at flow
two; flow-one LEFT histories cannot be adjacent to a flow-two/three
crossing because their shared edge would have inconsistent multiplicity.
For u=V, first/second outgoing ordinals are R0 and L3, so

    T1(v)=T0(u)+1, T2(v)=T3(u)+1.

Both u.L1 and u.R2 are strictly inside that interval, but both are RIGHT
side events in the exact first-track table. The actual cursor must stay
LEFT throughout v's return interval. Contradiction.

Hence at the critical level NO crossing LEFT can be second in an LL pair.
For the flow-two mixed stencil Z must therefore be V=NNSS. This removes
all other locally feasible second-LEFT O/U rows, leaving FIFTEEN necessary
open junctions: the old three plus twelve zero-chord rows. It does not
force the first LEFT to V or close its longer return.

## 3. The surviving mixed LL root feeds the actual persistent lane

If Y is first-LL O/U and Z=V, its actual LEFT return begins

    Y.L1 -> Z.L3 -> A.(second incoming cycle rank).

At the old flat reset this is A.L1 and closes the signed four-L cleanup.
At a zero-chord mixed bridge it is A.R2, a genuine source3/4 endpoint.
Thus the return immediately feeds the persistent second lane of
signed a37a9d33. Its first three turns are L,L,R, not the four-L square.
The same-heading return must consequently have length at least eight.

Even Y=U is retained here. For example the local choices

    Y=EWWE, Z=NNSS, A=EWEW, B=SSSS

are all four-read and satisfy the necessary local port/clock/stream
conditions. This is NOT a zero-output full front and does not undo the
positive-output scope correction. It demonstrates exactly why the
constant-flow-two singleton-U nesting theorem must not be imported into
mixed LL source/sink geometry.

No claim of exterior completion, arbitrary repetition, finite fuel or
reader-independent exclusion of this surviving long mixed return is
made.
