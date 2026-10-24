# A connected constant-original-mass producer of long 1564-wave episodes

23 October 2026, 16:46 UTC. Author proof/certificates, undergoing independent
component-gluing review. The finite R=100,N=3 instance is already independently
signed. No assertion of an infinite wave on one finite board is made.

## Proposed all-parameter statement

For every integer N>=1, put R=100+28N. The 184 black cells in
`prepared1564_uniform_support_manifest.json`, at their listed affine-in-N
coordinates, form one finite initial input. Start at

    (33+14N, 70+14N), heading W.

The actual ant executes the complete supplied 16-stage word. It consists of
seven ordinary standard104 flights, six finite two-corner routers, a 55-turn
standard prefix, the signed 24-turn fresh launch, and then N complete periods
of the signed1564 wave. No cell is added, removed or edited after time zero.
The initial set is exactly184 distinct cells, independent of N.

The N-wave episode starts at time858R+5947, pose(-6,-6,N), and ends at

    time858R+5947+1564N = 91747+25588N,
    pose(14N-6,14N-6,N),
    current black mass99R+905+104N = 10805+2876N.

The N in a pose means north; in formulas N is the positive integer parameter.

Each wave period has614 cyclic adjacent defects, so the actual trajectory's
adjacent-defect count is unbounded as N increases while its ORIGINAL black
mass stays184. A separate exact seam count may sharpen this to614N+92, but the
weaker614N-O(1) consequence already suffices. This disproves a mass-only bound
on total future defects if the all-parameter gluing is confirmed. It does NOT
disprove eventual104 capture: every supplied run is only a finite long episode,
and its later evolution is not specified here.

## Geometry and exact word

Let u=x+y and t=x-y. The seven canonical H phase0 lanes, in chronological
order, have (t,x mod2,heading):

    (-37,1,W), (-65,0,E), (-25,1,W), (49,0,E),
    (-13,0,W), (21,0,E), (1,1,W).

Their complete straight read bands are respectively

    [-40,-30],[-72,-62],[-28,-18],[42,52],[-16,-6],[14,24],[-2,8].

They are pairwise disjoint. The two exterior bands are helper flights and miss
the wave's entire read-normal hull[-54,30]. The other five are exactly the
independently signed useful writer cover, with the stated phases.

The six router input u coordinates are

    -2R+3, 2R+1, -4R+3, 4R+3, -2R+1, 2R+3.

Their literal words and complete finite caps are in
`prepared1564_noncrossing_router_plan.json`. They use ONLY retained short
corners. No new image/cap palette was searched. The router specifications are:

    1: (46,R,102) H^5  (46,R,102)
    2: (46,R,102) H^8  (46,R,102)
    3: (69,L,1)   H^14 (65,L,101)
    4: (69,L,1)   H^11 (68,R,102)
    5: (69,L,1)   H^4  (68,R,102)
    6: (89,L,1)   H^0  (65,L,101).

Here (a,c,b)=H[:a] c H[b:], omitting the suffix when b=0. All physical
rotations are proper; no reflection or global color complementation is used.
The full seven flight counts are

    3R/4, R+1, 3R/2+1, 2R+1, 3R/2+1, R+1, R/2-2.

The last flight ends at(7,6,W); H[:55] reaches(4,0,S), the exact signed launch
entry. The initial phase0 is at u=R+3, INSIDE the first right-side outer cap.
Starting farther NE would cross that cap's later route and is invalid.

Initial black mass is13 canonical source cells, plus the six router additions
of sizes24,24,20,23,23,23, plus34 signed launch additions: total184. The
manifest checks all pairwise affine seed equalities and excludes every
collision for every integer N>=1.

## 1. Isolated router contracts

`prepared1564_six_local_router_certificates.json` gives exact complete-board
H^30/router/H^infinity tests for all six words, using the retained arithmetic
periodic-tail checker rather than sampled repetitions. Each initial field is
the canonical13-cell standard input plus its listed fresh local cap.

These contracts extend to any incoming length m>=30. Relative to the router,
all router reads and extra cap cells have |u|<=14. Any additional incoming
period before the last30 has u>=114 for a SW approach or u<=-114 for a NE
approach. Such older history cannot affect the router. The complete incoming
and opposite outgoing H read-normal strips are disjoint, so the additional
older wake cannot affect any later outgoing period either. Thus the retained
local chronology is unchanged at every read.

All seven global flights have at least60 periods for N>=1. This leaves the
local incoming/outgoing buffers at adjacent routers compatible with one
continuous standard phase, rather than imposing disconnected initial states.

## 2. Mutual ownership and chronology

`check1564_uniform_support_guards.py` reconstructs each finite router's FULL
read support together with its preloaded black cap, and every entire standard
flight read rectangle. It verifies85 exact affine separation statements for
ALL N>=1, not merely at selected values:

* every router/cap misses every nonincident flight;
* all distinct router/cap components miss each other;
* all router/cap components miss the canonical initial seed;
* all seven flight bands are disjoint;
* the initial seed misses every other flight;
* every router/cap and the initial seed miss the central launch/wave window.

Each statement is witnessed by one u- or t-interval strict inequality whose
coefficient and value at N=1 have the required sign. The full coefficients are
retained. Incident incoming/outgoing intersections are not discarded: they
are precisely the complete isolated-router contracts from section1.

The34 launch additions lie only in the last writer strip and miss its ENTIRE
strict past, by the separately signed launch theorem. They therefore miss
all earlier straight flights, while the support inequalities put them away
from every router. Induction through the chronological components now gives
one actual trajectory on the single preloaded184-cell board.

## 3. Complete field supplied to the wave

The four completed useful writer flights have a conservative32-unit buffer
from both endpoints. Their central fully settled u intervals are

    [-2R+35,R-29], [-4R+35,2R-25],
    [-2R+33,4R-27], [-2R+31,2R-29].

Every interval contains[-21,28N] for R=100+28N. A single H period has u offset
range[0,10] for NE and[-10,0] for SW; the32 buffer exceeds both that range and
all entering-router debris. Hence all complete local cell histories have
finished in this central window. The manifest separately reconstructs their
odd-read black profiles and matches the EXACT48 classes of the four other
bands in the signed launch contract, including longitudinal parity.

The last SW writer starts beyond the central window by more than32 units.
Its finite start/router fringe cannot be read by the launch or the N-wave
prefix. Therefore its field on every relevant cell equals the causal SW
standard front required at phase55. The helper-band wakes are transversely
outside all those reads; all router/source debris is longitudinally outside.
No black subset or incomplete boundary field is substituted for the board.

The signed fresh34-cell launch now applies to the complete relevant field.
Its prelude and the first N wave periods read only the central window:
min u=-21, max u=28N. Thus every one of their colors agrees with the signed
infinite prepared model. This completes the finite, connected all-N claim
subject to independent review of the component-gluing implementation.

## Evidence and scope

Independent finite sample: R100,N3, all96439 reads, exact minimal184-cell seed,
full final11117-cell field hash, actual K1934. Author additional complete-field
controls R380,N10 and R2900,N100 pass347627 and2650547 reads respectively.
Those samples are controls, not the reason for the all-N quantifier.

The proof dependencies are the six all-future local contracts, the85 exact
uniform support guards, exact mature-profile identities, and the independently
signed fresh launch/wave. The supplied affine manifest binds every seed cell,
word, count, pose and time needed for a separate implementation.

No subsequent capture, renewable circuit, infinite finite-seed nonstandard
wave, or universal-conjecture conclusion is claimed.
