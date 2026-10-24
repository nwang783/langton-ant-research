# Independently signed all-cap period bounds

23 October 2026, 10:32 UTC. Current status index, audit LC and addendum.
All statements concern the ACTUAL full event period and full drift.
No primitive quotient, period scan or formal-proof-assistant claim is made.

Every nonzero complete initially-white translating front satisfies

    P >= 28.

More finely, for D=||d||infinity>=3 and complete multiplicity n>=4 in any
one full-drift class,

    P >= 4n+2D.

The signed unrestricted cap3 exclusion guarantees some n>=4. Thus
P>=2D+16 for D>=3. D1 is already all-cap excluded. D2 is either the excluded
unit axis or full(±2,±2), whose signed cap6 exclusion givesP>=28. D3 cap4
exclusions force n>=5, givingP>=26; D4 cap4 exclusions (axis4 through cap5)
giveP>=28; D5 givesP>=26; D>=6 givesP>=28. This first gives universal26. The signed backbone/equality refinement
below excludes26 and proves the current universal28.

## Proof layers and exact scopes

1. Arbitrary quarter-turn walk, D>=2:
   P>=4(n-1)+2D, from cyclic class gaps of displacement k_i*d with sumk_i=1.
   Source quotient_visit_drift_packing.md, synchronized phase note;
   frozenSHAaecd51bd92e318274606a72e6caf734eaeb96f37a56d831bb849e3a6dfc10bdf.
2. Actual Langton trajectory on ANY coloring:
   Four consecutive four-step physical returns are impossible. The complete
   32-case certificate four_unit_returns.certificate.json, SHAe38b61d81d5e8c11a4018643aff3099487fc68040e837f7e7fd7505915d391bb,
   has an explicit consecutive same-cell same-turn contradiction for every
   possible loop-orientation word. Exactly four three-loop prepared words
   remain legal; none was improperly discarded.
3. Hence arbitrary-color actual ant withD>=3,n>=5:
   P>=4n+2D, by excluding equality and usingP mod4. Frozen proof note
   four_unit_return_factor_obstruction.md, SHA01ebdb9dd44b00699e0d48cbfd08a6cc8a38468f2c2641faadc7021024640dfb.
4. Complete WHITE front at n4,D>=3:
   Equality would use one of two legal R-initial three-loop clusters plus
   an extremal monotone winding passage. Its required near-cell black input
   would be an unprepared first L, including the exceptional west-approach
   case. Frozen white_four_visit_packing_equality.md,
   SHA760259f33049e36baa81087b15d19b39d81f901dc1fb940a3bdf76171bd74900.

The frozen proof documents may retain their original pre-audit headers;
the independent analytic signoffs are audit LC and its white-input addendum.
The index here records their current SIGNED status without changing hashes.

## Uniform density refinement

For arbitrary input, call a class gap cheap if it is a zero-displacement
four-step return. Cheap runs have at most three gaps, so at leastceil(n/4)
gaps are noncheap. The signed unit_return_density_refinement.md gives

    D>=4: P>=4n+4ceil(n/4)+2D-8;
    D=3:  P>=4n+2ceil(n/4), rounded toP=2mod4.

## Supplied-drift all-cap consequences

- Fullaxis4: signed cap5 exclusion forces n>=6; the signed four/eight
  first-return/equality refinement below givesP>=40, superseding32/36.
- Full(2,2): signed cap6 exclusion forces n>=7, henceP>=28 by layer1.
- Full(3,±1),(3,3): cap4 exclusions plus the global equality refinement
  giveP>=30 after the compulsory odd-odd residue (former26/28 superseded).
- Full(4,±2),(4,4): the all-cap first-read speed bound givesP>=32.
- Full(5,±1),(5,±3): the all-cap coupled-run speed bound givesP>=42.
Genuine rotations apply. The last two chiral geometries were checked
separately. These are lower period bounds at ALL multiplicities, not
all-cap exclusions for those drifts.

The universal bound does not assert existence atP28,104minimality,
eventual periodicity or eventualstandard104 capture. No exhaustive external
literature-priority claim is made. The finite-black-seed conjecture remains
OPEN; the stable-white suffix bridge only transfers these necessary bounds
to an eventual periodic endpoint word if such a suffix exists.

## Signed four/eight-step chronological refinement (09:21 UTC)

Five consecutive FIRST physical returns at one cell cannot all cost4/8;
four such returns cost at least20. This is arbitrary-input chronology,
independently reconstructed through all12/42/48/16/0 guarded prefixes and
192 fifth-step conflict cells (LC addendum). Frozen note
four_eight_return_density.md, SHA8569bbfc40b96d53888f8c7a377811082d4e539497709064d8eac12d40116b1b;
certificate four_eight_unit_returns.certificate.json,
SHA0c95fe72142a0cc41a68f1e7461c04e6da0b19fef804393b3684017d79da4e89.

For arbitrary input and D>=2 this gives P>=min(6,3+D/2)*n; forD>=6,
P>=6n+2D-12. For WHITE fullaxis4, split the n6 cyclic gaps by their
nonzero winding count; all possibilities giveP>=36. For n>=7 the earlier
4n+2D bound already gives36. This is all-cap necessary period36, not an
all-cap front exclusion. The separately signed twelve-step/equality
refinement below strengthens this to40.

## Signed twelve-step factor and axis-four equality (09:31 UTC)

The frozen four_eight_twelve_return_density.md,
SHAb9d2adab9acde72091c926539151dbca88bee33334d261391b2542e4a0d58b3c,
and certificate four_eight_twelve_unit_returns.certificate.json,
SHA04a8a95449bce8c467e6350d525de860b60765988c995cbf9c6c0d11709c428b,
are independently signed. Eleven physical first returns of lengths4/8/12
are impossible; ten positive programs are retained. ANY five physical
first returns cost>=32. Block packing yields arbitrary-input
P>=min(7,3+D/2)n, or7n+2D-16 forD>=8.

The frozen axis_four_period36_equality_exclusion.md,
SHA84149eef56f38b18dc976cf43f08b10bde6f476d6672af8d1fcfc442b6982302,
reduces a putative axis4P36 to n6, three4-step zero returns and
three8-step winding gaps{+1,+1,-1}. All552,960 exact geometric compositions
were independently rebuilt;4,320 pass the complete central chronology and
NONE passes every complete white history. Thus all-cap fullaxis4P>=40.
This is an equality-case necessary period theorem, not an all-cap drift
exclusion. No stronger endpoint or finite-seed conclusion is inferred.

## Signed cap-four global stream/backbone coupling (09:55 UTC)

The first-R predecessor weakly climbs max incident unshifted C-face height
at every active cell under WHITE cap4. Its full-quotient functional cycles
are simple essential circles with negative winding; reversing them gives
actual-edge backbones of winding+1. Every active C-superlevel component
contains one, ruling out finite active height islands but not essential
strips. Frozen cap_four_first_read_stream_backbone.md,
SHA723e469574ffd3362a511f2d37a9347fdedc31b8be75c1e5d82b49949dbba115.

The separate time-debt addendum is signed: exact lifted first-time
increments around a maximal-height backbone give P>=3ell; every L-run
start additionally costs four in it or its predecessor. Since the simple
unit-edge essential circle has equalR/L and R runs<=3, this yields

    WHITE cap4, ANY full drift: P>=6D+4ceil(D/3).

Frozen cap_four_backbone_time_debt.md,
SHA72ff752e865d13ac4e230c0d636fee11e20d8acd7055d7fc0c9bc8c292aa22cc.
This supersedes that note's weaker4D+2 multiplicity argument without
changing its validity. The cap restriction is essential: at cap5 a first
R can turn around the lower of two unequal C heights. No all-cap or capture
claim follows from this relation.

## Signed universal white-front period28 (09:56 UTC)

Global_period26_equality_exclusion.md,
SHA45c563ae2ac0b58a73fd4c08bab510e5203950ae84ec2cb9e4c48e5793aae0bf,
has independently passed its reduction and complete equality replay.
P26 would force D<=5. D2 is excluded by signedcap6; D4 by signedcap4;
D5 would be cap4 and contradicts the new backboneP38 bound. D3 remains,
with exactlyfive visits in a class, and the winding sum gives only two
precise gap layouts. Full(3,+1),(3,-1),(3,3) are checked separately.

Check_global_period26_equality.py/json independently regenerates all
164,480 geometric compositions and all complete unfolded physical
histories, including translated negative-period predecessors. There are
2,591 central-white survivors and NONE white at every complete class.
ThusP26 is impossible; every nonzero complete WHITE front hasP>=28.
The frozen resultSHA67da2e8bc5449f9f98d6f43e3fd686af5ff836928866d569a372a5a46472ed47.
This is not104minimality, a general bounded-period search, or capture.
No chain of nearby equality scans is being launched.

## Signed ALL-CAP first-read speed theorem (10:06 UTC, LL)

The cap restriction is REMOVED from the time-debt theorem, not from height
localization. ANY complete bi-infinite WHITE front has a generic first-read
predecessor functional cycle on its finite FULL-drift quotient. Actual first
times force winding-1; embedded simplicity makes it a genuine essential
circle. Reversing gives incoming-first-R at each backbone vertex. At every
RIGHT corner its successor is immediately first-read, so q=j=0 exactly;
at every LEFT-run start q>=2, and other LEFT corners q>=1. Hence

    ALL-CAP WHITE: P>=6D+4ceil(D/3).

Frozen white_front_first_read_speed_bound.md,
SHA6f4126d41803fc9501f4d151a5271660eb4eabdad70f789428f7d6df25fa46e3.
There is no visit, period, width or drift bound. Prepared input or a finite
initial head is NOT included. Stream-height superlevel localization alone
remains restricted to cap4. Numerical all-cap consequences are now
D4P>=32(axis4separately40),D5P>=38,D6P>=44,D7P>=54.
The universal28 plusP=2Dmod4 also gives odd-odd full driftP>=30.
This is not an all-cap drift exclusion,104minimality or capture.

## Signed coupled-run ALL-CAP speed bound (10:28 UTC, LP)

The frozen white_front_coupled_run_speed.md,
SHA8237331f8e40b3ee4a29f94d711e2d0bf6de0836781fad9794c95d7032e8165d,
couples each R run to the following L run using only the already signed
eight-step first-return table. If both runs have length>=2, the L run
pays another q unit. With m=ell/2 and s runs,t such long-long pairs,
Q>=m+s+t and2m<=4s+2t giveP>=4ell>=8D.

Thus ANY complete bi-infinite WHITE front satisfies P>=8D, rounded upward
to8D+2 for oddD. Tiny independent enumeration of all256 eight-step words
checks the two possible return words and their literal earlier-p/u firstR
conflicts. The positive-input scope is not expanded: prepared input and
initial-head exceptions remain excluded. Current numerical ALL-CAP bounds:
D3P>=30(global28plusresidue),D4P>=32(axis4separately40),D5P>=42,
D6P>=48,D7P>=58. Earlier6D+4ceil(D/3) remains valid but is superseded
where weaker. Fullaxis4cap6 has a complete AUTHOR candidate now, but no
new cap-six exclusion is used before independent complete replay.

## Signed additive first-departure counterflow (10:58 UTC, LQ)

white_first_departure_counterflow.md,
SHA44302c05565a1320b3793e3f279a6355ce099387f1b2f853bca2046895446c7a,
proves that EVERY complete WHITE front's first-R departure map has only
essential winding-minus-one cycles. For any k distinct cycles of lengths
ell_i, P>=sum ell_i+2D*(1+k)>=2D*(1+2k). This is an ADDITIVE bound
across these vertex-disjoint cycles, obtained by subtracting their unit
negative flows and bounding the remaining nonnegative flow of homology1+k.
Do not add separate rank/time debts to it; combine those by maximum.
No minimum k beyond one is proved. Both first-arrival and first-departure
graphs may have multiple essential components (standard104 has two each).
No published uniform numerical bound above changes merely from this theorem.
The optional new departure monitor is separately pending code audit.

## Signed simultaneous two-family subtraction (11:09 UTC)

dual_first_backbone_edge_separation.md,
SHA0929ac725f878787a042a24f8b072301d0e687eea97bf12394c2de00121984b2,
proves that any forward first-arrival and backward first-departure essential
cycles are edge-disjoint. L/L vertex contacts are allowed. For selected
a forward and b backward cycles,

    P>=sum ell_A+sum ell_B+2D*abs(1-a+b).

It is now safe to remove BOTH families at once from integer flow. The two
register forms start at2D and-2D and have nonnegative increments ell±2D.
Do not clip the negative register upward before additions. Rank/time debt
bounds still combine by maximum. No new uniform numerical lower bound or
exclusion follows without additional information about the cycle families.
