# Five-C nonproper first contacts: two D gates and a sharp control

## Exact scope

Inside an actual complete recurrent-eight factor, use the actual atomic
D/V/U/C cuts, ordered residual identities, and corrected centers
head + rotation(−1/2, −1/2). A canonical first center contact uses the outgoing
earlier chord with parameter 0 <= s < 1 and incoming later chord with
0 < t <= 1. Normalize the earlier entry to (0, 0, N).

If the entry C gap is five and the contact is nonproper, all possibilities
reduce to these two gates:

- Earlier D base, later C at (0, −1, W).
- Earlier D base, later U base at (1, 0, W). In this second gate the original
  D output (2, 0) is retired by an immediate plain V predecessor at
  (4, −1, W), or an immediate plain U predecessor at (5, 0, W).

The containing full source may be D or DC. The later C can be internal to its
full packet. This note does not delete the second gate using a separately
pending helper-history result. It does not assert a generic entry-only law.

The first gate is actually attained by the sixteen-cell full word
DC, VC, V, VC, VC, VCC. Its first nonadjacent center contact is at path time 12:
the start of the initial D chord meets the endpoint of the final second C.
The later C has entry pose (0, −1, W) and entry clock five; its exit clock is
six. This is not a full-pose return or renewable control. All eight possible
full-packet prepends to this fixed word fail, but that does not prove every
realization of the gate is entry-only.

## Complete geometry and finite scope

The exact contact parallelograms yield 24 sector-compatible nonproper cases.
For every earlier atom D, C, V, U, the later possibilities are:
D or C at (0, −1, W); V at (2, −1, W); U at (1, 0, W) or (3, 0, W).
There are four additional earlier-U cases: D or C at (0, 1, W), V at
(2, 1, W), and U at (3, 2, W).

No head-radius, word-length, C-threshold extension, or extrapolated simulation
is used. There are 15 actual source/full-producer roles; internal C roles keep
their full-source birth-clock shift explicitly.

## Seventeen one-slot exclusions

For seventeen geometries, some original fresh source output is in a target
white guard or target entry core. It must retire strictly before the later
atom. The complete finite consumer table covers every full packet, every
input alignment, and every entry gap from zero through five. It checks:

- Containing full-source completion, sector, signed HB, and signed cap-five
  clauses. The table entry five is overflow >= 5, not exact five.
- A consumer base whose closed chord already touches the original earlier
  chord would give an earlier nonadjacent center contact.
- For a later base target, the strict consumer's full packet must finish first.
  For an internal C target, no unseen C tail is required to finish.
- The exact zero- or one-C endpoint cone from the consuming BASE exit,
  counting only C atoms actually before the target cut.

A source-independent last-output existence premise is never substituted for
an original identity: these tables follow the mandatory retirement of one
particular fresh identity.

The zero-C endpoint semigroup is rotation of (a+b, a+3b+4c), with nonnegative
integers a, b, c. The one-C test uses the exact decomposition into a zero-C
prefix, the C head step (0, 1), and a zero-C suffix at heading W. In normalized
N coordinates its total y minus one is nonnegative and bounds the finite
prefix enumeration. Thus no bounded D-run assumption is hidden in the test.

## Two further exclusions and the D-to-U gate

The three remaining D-to-V/U cases all require the original D output (2, 0)
to retire. Timely consumer options reduce to V/VC at (0, 1, E) and clock three,
or, in the U-at-(1,0,W) case only, plain V/U at clock five.

The clock-three V base installs its fresh exit bud at (2, −1). Signed atomic
post-exit maturation keeps it current through the later target clock five.
It lies in the V-at-(2,−1,W) or U-at-(1,0,W) entry core; at U-at-(3,0,W) it is
a lower input of produced age two, below the signed minimum three. These
options are all impossible.

The clock-five options are exactly V at (4, −1, W) or U at (5, 0, W), with
base exit equal to the U target entry (1, 0, W). They have no attached C tail
and a nonempty zero-C word cannot have zero displacement, so they must be the
immediate predecessors stated above. They remain open in this certificate.

## The two old-core D-target cases

For either earlier D or C, the later D at (0, −1, W) requires its true input
at old atomic-core cell (−1, −1). This is never an entry residual at the later
D without a genuine fresh residual birth. That cell is absent from every
possible containing full source's output mask.

No later full producer can create it at clock zero: if a source C remains,
another full producer starts at clock at least one; otherwise plain D exits
upward and all clock-zero N producers have nonnegative output y offsets.
The D-input minimum three leaves only birth clocks one or two.

Birth clock one would give exact produced age four. All 136 universal
D/DC-input queries exclude that age. At birth clock two, the complete
272-case origin table leaves only a plain D producer at (1, −1, S), after
sector, counted, HB, and earlier-contact cuts. Its BASE EXIT center equals
the final D's ENTRY center. The claimed endpoint contact would therefore not
be the first center contact. Both D-target geometries are excluded.

## The C-source to C-target case

An actual earlier C always has a previous atom in its containing full packet.
That preceding atom's fresh exit bud is r = (1, −1), already current at the
C entry. It is also a genuine output of the containing full producer, with
the correct one-clock shift in second-C cases. The later C at (0, −1, W)
requires r in its entry core, so r must retire strictly beforehand.

All 966 retirement options leave two kinds:

- V/VC at (−2, −1, E), clock three, only for a full DC source. Its base exit
  center equals the later C's entry center, already an earlier repeat.
- A V-family base at (3, −2, W) or U-family base at (4, −1, W), clock five.
  Each requires the ORIGINAL earlier C common output (2, 0) white. Two complete
  966-case tables show that this identity has no timely noncontact retirement
  before either helper base. Attached helper tails may extend after the later
  C target; the proof works before the helper base and does not finish them.

Thus this C-to-C possibility is excluded too.

## Reproducible positive control and limitations

The checker derives and executes the complete sixteen-cell seed, all 190 raw
steps plus actual M11, every full core and ordered identity transition, all
12 atomic chords, and every nonadjacent chord intersection. The seed is listed
in the machine-readable output. It also checks all eight failed prepends to
this one word.

The certificate contains 9,522 primary mandatory-retirement rows, 136 exact
age-four D-input queries, 272 old-core origin cases, 966 incoming-bud cases,
and 1,932 late-helper common-output rows. All unbounded endpoint cones are
exact semigroups, not finite-depth path searches.

No higher-C return, infinite-fuel, record-count, global capture, or generic
boundary-only theorem follows. Proper five-C crossings are separate results.
