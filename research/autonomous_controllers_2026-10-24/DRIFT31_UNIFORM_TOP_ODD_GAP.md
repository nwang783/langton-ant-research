# A uniform six-level odd-read boundary obligation at full drift(3,1)

24 October 2026. Author proof, submitted for independent review. This is a
complete-read boundary theorem, not a classification or a physical controller.

## Statement

Let a complete WHITE front have actual full drift(3,1). Use T=3y-x and choose
the translation sector so incoming headings are vertical at even T. Let M be
the maximum of its COMPLETE READ footprint. Then at least one of the six
classes M-1,...,M-6 has ODD read multiplicity.

No growth value, global visit cap, period bound, lower support bound or single-
used F-circle hypothesis is needed for this boundary statement. The signed
read-maximum lemma2d5bb1e6 applies in this sector: M is even and its complete
history is the singleton N/R. It concerns the actual read footprint, not the
black field, odd-output maximum alone, or a scalar face potential.

## Literal finite proof

Translate the even normal maximum to20. This preserves the incoming-axis
sector and full drift voltages. Above20 there are no reads, so T21,T22,T23
may be named empty. All lower omitted classes remain UNKNOWN.

Assume T19,...,T14 have even multiplicity. Starting with T20=N, exact physical
port multiplicities and WHITE alternation give the following complete cover:

T19=EW and T18=NN.
T17 is EWWW or WWEW.
The three complete T16 extensions are NNNNSS, NNSSNN, NNSNNS, coupled to those
T17 modes exactly as recorded in the certificate.
Their five T15 extensions have three skipped-rank returns, one positive-clock
cycle and one survivor. Thus T15=EWWEEW,T16=NNSNNS,T17=WWEW.
At T14 the five complete histories have three skipped-rank returns and two
survivors: NNSSNSNN or NNSSNNNS.

Now T13 has five E arrivals and four N departures. Counting alternating turn
ranks yields the DERIVED bound n13<=2(5+4)+1=19. Its parity is unrestricted.
For each T14 mode, all actual same-physical-cell return paths through the named
upper region impose consecutive-read ordinal equations. There are respectively
seven and three complete T13 words satisfying every such equation. Every word
begins W,E. In every case the actual eight-step event path is

T14.rank0 -> T13.rank1 -> T16.rank1+d -> T17.rank0+d
-> T20.rank0+2d -> T19.rank0+2d -> T16.rank2+d
-> T17.rank1+d -> T14.rank2.

The initial and final events occur at the SAME physical point. There is no
intermediate T14 read on the path. It skips rank1 and therefore cannot occur
in any complete chronology. The full path is recorded with all lattice lifts,
not merely quotient adjacency. Thus both T14 modes fail at every multiplicity
and either parity of T13. This proves the statement.

All finite bounds here come from the two already fixed perpendicular ports:
for I uses of one incoming heading and J uses of one outgoing heading, splitting
those counts between R and L gives n<=2(I+J)+1. The greatest bound used is19.
The certificate enumerates all words through that derived bound, not an
arbitrary cap. Its one positive-clock rejection records an explicit closed
inequality cycle valid at every possible period. The other rejections are
literal skipped-rank paths.

## Consequence for the LIVE two-quadruple family

Signed prior proofs reduce that branch to full odd inventory

O={0,1,2,5,6,6a+1,6b+2,6c+2}, a>=2, c>=3, 1<=b<a<=c.

If a<c, its largest odd level is M=6c+2. Every other odd level is at most
6c-5=M-7: indeed 6a+1<=6c-5 and b<a implies6b+2<=6c-10; the fixed0,1,2,5,6
are also belowM-6 for c>=3. Since the read maximum is itself odd, it is this
same M. This contradicts the six-level boundary theorem. Hence

                     a=c

is a necessary condition in the live two-quadruple family. This is not the
already excluded cyclic-E family and does not assert an incompatible ordering
without proof. The remaining c>=3 and1<=b<c are OPEN. No completed front,
finite seed, physical wake or controller is supplied.

This uniform theorem subsumes the separately frozen O20 two-ended exclusion
442642ea, where a=2<c=3, but that independent proof artifact is preserved.

## Artifacts

`certify_drift31_top_odd_gap.py` regenerates the full local case cover.
`drift31_top_odd_gap_certificate.json` retains every parent/domain, full-lift
return and rejection witness. No solver or historical width-ten computation
is used. Every unlisted level<=12 is UNKNOWN, not empty.
