# Identical early R births can be permanent wake or later input

24 October 2026. AUTHOR exact paired finite/infinite countercontrol; independent audit requested. This identifies the lifetime mechanism behind the minimal-cohort growth. It does not claim that a lifetime proved forever unread in an actual trajectory can later be read in that same trajectory.

## An exact balance identity

Let C*(t) be the current black lifetimes that will eventually be consumed. During [t,u), let R and L count actual white/right and black/left reads. Let P count the R-born lifetimes from this interval that are never consumed anywhere in the complete future. Then

    |C*(u)| - |C*(t)| = (R-P) - L.

Every L removes one currently relevant lifetime. An R adds one relevant lifetime exactly when that lifetime has a later L; otherwise it adds permanent unused archive. Equivalently, the number of current forever-unread black lifetimes is nondecreasing along a single actual orbit, and increases exactly by P. This is a retrospective identity, not a decision procedure or a global bound on P.

## Paired full-board controls

Compare the fourteen-cell defect seed in `MINIMAL_RELEVANT_COHORT_RESTART.md` with the fifteen-cell seed obtained by filling its missing cell (-3,-2). Both start at (0,0), E. The filled seed satisfies the exact canonical phase45 guard from the start. The defective seed agrees with it for the first 71 reads, then deviates and ultimately captures later.

The first 104 updates of BOTH histories contain exactly 58 R and 46 L moves. Their relevant-cohort balances differ:

| history | eventually consumed R births | permanently unread R births | relevant change |
|---|---:|---:|---:|
| filled canonical guard | 46 | 12 | 0 |
| fourteen-cell defect | 55 | 3 | +9 |

The canonical relevant size is 15 at both phase-aligned cuts. The defective relevant size grows 14 -> 23. Thus the +9 is exactly a deficit of nine permanent-write outputs relative to this paired standard control, not a difference in the gross R/L mass balance.

## Four identical birth events with different complete futures

These four R births occur in the COMMON prefix, at exactly the same time, position and cursor history in both controls:

| birth | cell | filled guard future | defect future L |
|---:|---|---|---:|
| 44 | (2,2) | never read again | 168 |
| 46 | (1,1) | never read again | 166 |
| 52 | (-2,2) | never read again | 200 |
| 58 | (-3,1) | never read again | 210 |

Every original fourteen-cell lifetime in the defect has already died by time 70. The four later reads therefore recover self-generated material, not an unconsumed original input. The initially missing bit changes the later routing and makes these early outputs part of the exact future-relevant cohort.

This is a countercontrol to prematurely declaring an R birth permanently retired merely because the current finite trajectory and its geometric position match a standard wake template. The full future of the correctly filled board is not transferable across the missing unread bit. In the defective history these four lifetimes were relevant all along, under the retrospective C* definition; no genuinely forever-unread lifetime is resurrected.

The nine-unit permanent-output difference is a NET balance. Only the four displayed common-prefix identities are asserted here to match birth-for-birth; no identification of all nine lifetimes is silently assumed.

## Certification and scope

The baseline fifteen-cell board is certified by an independent all-period ray-parity calculation with 154 exact change-point tests. Every black lifetime at its full 27-cell cut-104 state is classified by its first ray hit, or by an exact never-hit result. The defective field and all its lifetime deaths are supplied by the separately independently checked 308-read/full-future certificate. Both whole fields and actual cursor sectors are retained.

`check_paired_wake_return_credit.py` verifies the actual 104 baseline word, both counts, all lifetime classifications, and the four common births. Its report is `PAIRED_WAKE_RETURN_CREDIT_CHECKED.json`.

The identity may help formulate a correct spatial production/escape account, but the countercontrol supplies no universal lower bound on permanent output. It does not refute weighted or amortized charging, establish a regenerative ladder, or alter the fixed-cohort 272754 theorem. Global finite-seed attraction remains UNSOLVED.
