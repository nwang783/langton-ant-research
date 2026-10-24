# A five-period inverse104 slab fails even with nonstationary short images

Author-certified 2026-10-23 11:55 UTC. Independent semantic review requested.
The local1/5/9 image palette, single-period chronology and compatible standard
rail inputs were independently signed separately. This note changes the
stationarity assumption, not the palette, coarse scaffold, or spatial cutoff.

## Model and exact entry-board contract

Let V=complement(reverse(H)) be the fixed104-letter coarse inverse scaffold,
starting at(0,0,W), net displacement d=(-2,-2), final heading W. In EACH of
five consecutive coarse periods, EACH of the104 occurrences independently
chooses any of the complete ten internally legal exact-pose images of its
coarse turn with length1,5,or9. There are520 independent image choices, not
104 choices reused five times. Output colors are unrestricted.

The untouched input region has the mature output of any compatible finite
standard NE/SW white-written rail bundle in the same conserved sector. Its
exact48 anchored profiles and pairwise full-read-band incompatibilities are
those of the independently signed multi-rail theorem. There is no explicit
cardinality bound; geometry permits only the385 compatible subsets.

EVERY cell that an earlier allowed coarse period could have read is granted
an entirely arbitrary entry color. These bits are independent of the rail
profile and of one another. No realizable previous history is imposed, so the
boundary treatment is a relaxation, not an assumption of a reset or blank
front. Only genuinely new cells have rail-supplied input.

## Exact overlap and ownership calculation

Use orbit a=(x-y,x mod2), representative (e,e-a_0), and longitudinal level
k=floor(x/2). For every possible phase read in period0, collect its level l.
For orbit a let L_a and U_a be the minimum and maximum such offsets. These
finite sets are regenerated from ALL ten images at ALL104 phases.

The global potential offset range is[-2,2], width4. A read from coarse period
r has level k=l-r. Hence two possible occurrences at the SAME physical cell
can have period indices differing by at most4. Five consecutive periods are
therefore the geometry-derived complete overlap range. This does NOT mean a
SAT five-period slab would decide infinite feasibility; it only explains the
single test horizon, and no horizon escalation is used.

For an earlier period r=-j, j>=1, the possible levels on orbit a are l+j.
The union over every earlier period and every possible image is EXACTLY

    { k in Z : k >= L_a+1 }.

The inclusion from left to right follows from l>=L_a and j>=1. Conversely,
for any k>=L_a+1 choose an actual potential read at l=L_a and j=k-L_a.
This is a geometric possibility statement; incompatible earlier choices do
not matter because allowing all these cells arbitrary only weakens the test.

Thus a current slab cell is treated as follows:
- k>=L_a+1: arbitrary inherited entry bit;
- k<=L_a: untouched rail-profile entry bit.

The five-period potential read support has214 physical cells:64 inherited
free bits and150 prescribed new cells. The complete positions and per-orbit
L_a/U_a values are frozen in nonstationary_short_slab/architecture.json.

## Equivalent finite-front interpretation

For each orbit a, past periods can read levels at least L_a+1, while future
periods can read only levels at most U_a. The entire inherited overlap is
therefore precisely the finite interval [L_a+1,U_a]. Summing these interval
lengths over30 orbits gives64 frontier color bits. Each new coarse period
introduces one untouched level L_a per orbit, hence30 new profile bits, and
shifts the frontier frame by one level. All local image occurrences remain
independent choices constrained by actual color chronology.

For each of the385 compatible standard input profiles, this defines an exact
finite64-bit front transition relation. The five-period CNF asserts a path
of length5 in that relation, with completely arbitrary initial and final
front states. Its UNSAT certificate is a symbolic proof that the fifth power
of every such transition relation is empty, not just that it has no fixed
point. This explains why no periodicity or stationary-controller assumption
is needed. It does not create a length or reach bound for other architectures.

## Finite chronological encoding

Each physical cell, not merely each drift orbit, has one current-color chain.
Potential events are ordered by (period index, coarse phase, local slot).
This is the actual chronological order for EVERY choice of image lengths.
Selected events must read their specified L/R color and toggle; unselected
events leave the bit unchanged. Each occurrence has its own exactly-one
image selector. There is no relation identifying choices in different periods.

The rail OR-input relation is applied ONLY to the150 new cells. The64
inherited initial bits have no restrictions. All known finite local geometry
and current-color constraints are retained; final colors are free.

## Result and nonvacuous controls

The single CNF has44983 variables and183663 clauses. It is UNSAT. A separate
monotone RUP certificate has787 additions, all verified by the retained
independent checker, with no RAT steps or deletions.

CNF SHA256:
4ffcc192c250541073d3a8f83285d172719419715a3e87e45ed0c4096035456a

RUP SHA256:
184f384fe8169a5e3a438233eea1be314976feb788baf998fc9df39cf6d3520f

Two positive controls use the SAME finite physical-cell chronology encoding
but allow the entire entry board to be inferred rather than demanding rail
colors on new cells:
1. Five prepared108 periods give a legal540-turn word, input68/output28.
2. A genuinely nonstationary control forces the first period's phase31 image
   to be L and the fifth period's same image to be LRRRR. The resulting532-turn
   word has different period-image assignments and passes an independent
   complex-heading complete-board replay on the solver's78-black input,
   ending with30 black cells. This is a finite positive control only.

Artifacts:
- synthesize_nonstationary_short_slab.py
- nonstationary_short_slab/architecture.json
- nonstationary_short_slab/result.json
- nonstationary_short_slab/five_period.cnf
- nonstationary_short_slab/five_period.rup
- nonstationary_short_slab/prepared108_finite_positive.json
- nonstationary_short_slab/nonstationary_finite_positive.json

## What follows, and what does not

There is no legal five-period block under this untouched-standard-bundle plus
arbitrary-inherited-front contract, even when all image occurrences change.
Therefore a nonstationary schedule cannot traverse an unbounded perfect bulk
region of that form using this exact short inverse scaffold. A hypothetical
longer traversal must encounter additional prepared defects, nonstandard bulk
input, or depart from the stated image/coarse-path architecture.

The fixed-flight preparation bound can be adapted only after explicitly
accounting for standard-flight endpoints, cap reads, initial extra blacks and
any varying active rail subset across a slab. This note does not silently
apply a single constant bundle to a window crossing such interfaces. It does
not assert a global ant obstruction, a finite-seed counterexample, or a
complete decision procedure for arbitrary nonstationary refinements.

The separately reconstructed minimal seed for the532-turn nonstationary
positive control has70 black cells and22 output black cells; eight irrelevant
black cells in the solver-provided78/30 board can be removed. Exact literal
minimal-field data are in nonstationary_short_slab/minimal_positive_controls.json.

## Independent signoff, 2026-10-23 12:01 UTC

`../../audits/check_nonstationary_short_slab_independent.py/json` independently
regenerates the palette, every physical cell, all183663 clauses, the exact64/150
inherited/new split, and every RUP addition. Both complete-field positive
controls pass, with minimal input masses68 and70. The stated five-period
contract is signed without periodic image-choice equality or final-field
constraints. Extra untouched prepared defects and arbitrary non-architecture
prior interventions remain outside this local contract.
