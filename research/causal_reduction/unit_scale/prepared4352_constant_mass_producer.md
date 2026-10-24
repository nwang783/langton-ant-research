# A connected five-flight producer of 4352-wave episodes

23 October 2026, 17:35 UTC. Author all-parameter component proof, submitted for
independent exact affine chronology. The fresh causal launch is independently
signed. This note does not assert subsequent capture or renewal.

## Exact family

For every integer N >= 1, put R = 200 + 52N. Preload the 394 distinct black
cells in `prepared4352_uniform_support_manifest.json`, and start at

    (113 + 26N, 88 + 26N), heading W.

The ant executes the twelve listed stages on this one board, with no later
edits: five standard104 flights, four supplied two-corner routers, H[:28], the
signed 6812-turn launch, and N complete periods of the signed 4352 wave.
The wave starts at time 144402 + 33800N, pose (-2,3,W), and the prefix ends at

    time 144402 + 38152N,
    pose (26N-2, 26N+3, W),
    black mass 16654 + 4084N.

The original mass is exactly 394, independent of N. The exact actual adjacent
bad-ten defect count, including genuine initial history and all seams, is
1972N + 3003. This is another fixed-original-mass unbounded-defect family, not
an infinite nonstandard trajectory on one finite seed. Its distinct feature
is three useful writer bands and only five connected standard flights; its
larger launch cap means it does not improve the original 184-cell mass bound.

The manifest SHA256 is
`e3f1940d073741ad8bf48a4a8f6b33942569c4a20bc23c2809bf885ae9f0f6d4`.
It specifies every literal word, affine count, initial cell, start pose and
global time. The construction uses only four fixed retained two-corner words,
not a new cap or word search.

## Geometry and one-time input

Write u=x+y and t=x-y. The five canonical H phase-zero lanes, in order, are

    (t, x mod 2, heading) =
    (25,1,W), (89,0,E), (9,0,W), (-57,0,E), (-5,0,W).

Their complete read-normal bands are [22,32], [82,92], [6,16], [-64,-54],
and [-8,2]. All are disjoint. The two NE bands are return helpers and miss
the ENTIRE launch and wave read-normal hull [-50,78], not merely the narrower
wave hull [-16,40]. The three SW bands are exactly the useful prepared input.

The four router entry u-coordinates are

    -2R+1, 4R+3, -4R+3, 2R+1.

The five flight lengths, in full H periods, are

    3R/4, 3R/2+1, 2R+1, 3R/2+1, R/2+10.

Their sum is 25R/4+13. The four literal router lengths are 1406,1804,1708,1292,
with total 6210. Their exact words, poses and fresh black caps are in
`prepared4352_noncrossing_router_plan.json` (SHA256
`4a51be3cec7862c301bd9057ed5b4a67424717ae08739cdb4d782e09b213cfcb`).
Each needs 23 added black cells. The initial seed consists of the canonical
13-cell standard source, those four disjoint caps, and the 289-cell signed
fresh launch cap: 13+4*23+289=394. Every pair of affine seed coordinates is
checked for coincidence at every integer N>=1; none coincides.

The final H phase-zero pose is (-20,-15,W). H[:28] reaches (-24,-17,W), the
exact causal launch entry. The launch has no erasures and misses the ENTIRE
strict past of this incoming standard front. Its cap normal hull [-48,66]
misses both other useful writer read bands. These ownership statements are
part of the independently signed launch, not inferred from a finite sample.

## Isolated complete router contracts

`certify4352_four_local_routers.py` verifies H^30, then the literal router,
then H forever, on the complete finite source-plus-cap board. The outgoing
infinite tail is checked by the exact ray/first-mismatch arithmetic, not by a
repetition horizon. All four pass. The certificates are retained in
`prepared4352_four_local_router_certificates.json`.

Each extends to arbitrary incoming m>=30. Relative to its input, the router
and cap have u in [-14,12]. Any additional incoming period before the last
30 has u>=114 for SW approach, or u<=-114 for NE approach. It misses the
router and cap, and its full incoming read-normal strip is disjoint from the
oppositely directed outgoing read strip. Thus it misses every future outgoing
read too. The older-incoming field discrepancy is confined to those incoming
read cells. This proves the exact extension, without discarding inherited
wake. All five global flights have at least 60 periods for N>=1.

## Mutual guards and the complete launch field

`check4352_uniform_support_guards.py` establishes 41 strict affine box
separations for every N>=1. Each router's box includes BOTH all of its reads
and every preloaded extra black cell. The checks include each router versus
all nonincident flights, all other routers, the initial source and the entire
central launch/wave window; all distinct flight strips; and source versus
every later flight and the central window. Incident intersections are handled
by the complete local contracts, never deleted.

The central window used here is

    -61 <= u <= 52N+19,   -50 <= t <= 78.

It contains every launch-cap cell, every prelude read, and every read of the
first N wave periods. The two completed useful SW writers have fully settled
central intervals, after a conservative 32-unit endpoint guard,

    [-2R+33, R-31],  [-4R+35, 4R-25].

Both contain the whole central u-window. The source/front fringe and router
writes lie beyond those guards. Reconstructing the complete odd-read profiles
of these two writers gives exactly the 24 mod-(2,2) black classes in the
launch's two other full bands, including their physical phases. This is a full
field identity on every relevant cell, not merely coverage of black demands.

The last writer starts at u=2R+5. Its finite-start difference from the infinite
causal front lies above u=2R-27, strictly above the entire central window.
The two helper read bands miss the central window transversely. All source
and router debris misses it longitudinally or transversely by the 41 guards.
Therefore the full field seen by the fresh launch equals its signed causal
input, and the first N wave periods equal the signed infinite prepared wave.
Induction over the components establishes the stated one-board prefix.

## Count and controls

`count4352_producer_defects.py` reconstructs the source's true previous ten
turns as LRLRRRRLLL. All 381 non-source affine seed cells miss all ten reverse
read cells for every N>=1 (3810 exact exclusions). Each repeated H body has
zero cyclic adjacent bad-ten cost; each 4352 body has cost1972. The finite
first-body and seam histories give exactly 1972N+3003. The complete per-stage
first and stationary contributions are in `prepared4352_producer_defects.json`.

The charge computation is independent: H has charge12, the four routers have
charges166,214,198,150, H[:28] has charge4, and the launch charge is372.
The wave's charge is184. Thus the final mass is 75R+1654+184N, as stated.

Complete literal controls N=1 and N=2 pass from their original 394-cell seeds,
with every initial black cell used. N=1 has182554 reads and final mass20738;
N=2 has220706 reads and final mass24822. These are implementation controls,
not a substitute for the all-parameter support/chronology proof.

No eventual capture, second consumer, regenerative interface, or infinite
finite-seed counterexample is inferred from this finite family.
