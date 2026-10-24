LANGTON'S ANT: BOUNDARY PROOFS AND GLOBAL INVESTIGATION
21 October 2026

STATUS

The full highway conjecture is NOT proved in this bundle. No finite-support
counterexample was found. The completed work consists of local analytic
theorems, one restricted computer-assisted exclusion, exact record identities,
and a precise account of the remaining global gap.

These are research notes from this session. They have internal mathematical
and computational checks. They have not been checked in a proof assistant or
reviewed by an external mathematician. No claim of novelty or priority is made.

The user supplied earlier work on growth-eight highways at displacement
(2,-2), width ten, and on fresh boundary excursions. That earlier width-ten
enumeration is not rerun or re-certified here. The new converter exclusion has
its own input inventory, enumerator, controls, and coverage audit.

THE GLOBAL TARGET

For every finite set B_0 of initially black cells on an otherwise white square
grid, and every ant pose, prove that the future turn stream is eventually a
cyclic phase of the standard 104-letter word. Translations and quarter-turn
rotations of the highway are allowed.

The ant turns right on white and left on black. It then flips the read cell
and moves one unit. All initial black cells remain part of the state. No old
writes are deleted from the actual dynamics.

Unboundedness is weaker than transience. The fact that the ant leaves every
finite containing region does not prove that it returns only finitely often
to every fixed cell. Neither property by itself establishes highway capture.

MAIN COMPLETED RESULTS

1. Arbitrary initial colors under a fixed cap

See boundary/arbitrary_cap_third_row.md. Put

  T_r=(r,-r), A_r=(r,-1-r), B_r=(r,-2-r), C_r=(r,-3-r).

Take a finite path that starts and ends at x+y<=-4, never exceeds x+y=0, and
has the heading sector in which top visits arrive east. All initial colors
are arbitrary. Let M count top visits, N_X count processed visits on row X,
and Delta_X be final minus initial black population on its visited footprint.

The proof defines four nonnegative integers D_0,H,rho,Z_0 and proves

  N_C = 12M - 8Delta_A + 4Delta_B - Delta_C
        - 8D_0 - 4H - 16rho - 4Z_0.

Here H counts black upper turns on A. Such turns join adjacent top visits.
They occur only at initially black A cells and each such cell is visited once
in a completed capped path. A maximal chain of these turns is a roof.
rho counts the bridges beyond the first bridge of each positive-length roof.
D_0 counts white upper B turns after one turn for each ordinary four-step
top loop is removed. If Q counts black lower A turns and K_C counts black
upper C turns, then Z_0=K_C+2D_0-Q.

The central step is an injective assignment from unmarked black A events to
black C corners. The proof excludes all three ways that two assigned returns
could share a corner. It does not rely on a bound on the period or seed size.

An exact family with k initially black A bridges attains equality for every
k>=1. See sources/arbitrary_cap_bridge_sharpness.md. With the other terms
held fixed, this family verifies sharpness of the coefficients on H and rho.

2. Unfinished prefixes

See boundary/capped_prefix_charge_bound.md and
global/partial_cap_port_identity.md. The endpoint can be inside the cap,
including a black top cell just before the first exit. Initial colors remain
arbitrary. The exact endpoint port terms and the unfinished charge give

  N_C <= 12M - 8Delta_A + 4Delta_B - Delta_C + 14.

The constant 14 is sharp with the other coefficients fixed. Start at
(0,-4), facing west, with black cells (1,-3) and (0,-2). After twelve updates
the ant is at (2,-2), facing east, on an unprocessed black top cell. The counts
are M=1, (N_A,N_B,N_C)=(4,4,2), and
(Delta_A,Delta_B,Delta_C)=(2,-2,0). The right side without 14 is -12, whereas
N_C=2. The event-by-event replay is global/partial_cap_sharp_witness.json.

3. A stronger inequality when A starts white

See global/fresh_a_cap_shift_inequality.md. Keep B,C and all deeper rows
arbitrary, but assume A initially white. Let L_C count black lower corners on
C. For a completed capped path,

  7Delta_A - 4Delta_B + Delta_C <= 8M - L_C.

This follows from a new charge between separate upper runs. A run consists of
C upper excursions between two white C events. If it contains P short right
excursions, D left connections, and M top visits, its exact contribution to
S=7Delta_A-4Delta_B+Delta_C-8M is

  S_run = 3 + 2M - 5P - 11D.

There is only one possible positive run type. It has D=0,P=1,M=2 and score 2.
Initial whiteness of A forces an earlier short excursion for each such run.
The assigned earlier shorts are distinct. The proof shows that each assigned
short lies in a run with sufficient negative score. Summing gives
sum S_run<=0. The remaining lower C corners each contribute -1.

The proof is independent of the exploratory finite-word checks. The old-A
counterexample in root/cap_shift_old_counterexample.json shows why A freshness
cannot simply be omitted, even if no black upper A bridge occurs. A limited
extension with an initial-A defect term is in
sources/old_a_no_bridge_shift_bound.md.

The prefix form is proved in boundary/fresh_a_prefix_shift_bound.md:

  7Delta_A - 4Delta_B + Delta_C - 8M + L_C <= 14.

The same twelve-step example attains 14. The note also gives the smaller
endpoint-specific bounds and the exact record-birth formula.

4. A restricted backward-converter exclusion

See sources/negative_converter_exclusion.md. In coordinates where the standard
highway travels by (-2,-2), its settled wake has twelve black translation
classes in -3<=x-y<=7. Consider a bi-infinite periodic path through this
periodic input, with full displacement (2,2). Require it to preserve the
standard heading sector, stay in this same band, and leave fewer than twelve
black classes behind. No such converter exists within the internally audited
computer-assisted proof.

This is a restriction on a periodic input-to-output conversion. It is not a
claim that an infinite periodic input is a finite initial configuration.

The exact reduction covers all period lengths:

  complete output inventories:                 3,061
  outputs with elementary row-port profiles:     658
  complete row profiles:                      30,431
  largest possible period in those profiles:     216
  completed chronology searches:             30,431
  solutions:                                      0
  accepted timeouts or missing records:             0

An independent dynamic program reproduces the profile counts. Three positive
controls check the ordinary highway, a complemented/reflected highway, and a
two-row staircase. Two controls require nonwhite input. A separate literal
coordinate verifier checks their full repeated words.

The theorem does not cover a wider path, a different full displacement,
nonperiodic behavior, or an output with twelve or more black classes. It does
not prove stability against arbitrary finite perturbations.

GLOBAL WORK AND THE REMAINING GAP

At a fresh record, the six turns LRRRRL preserve all old row colors and add
one black cell on each of the next two diagonals. In particular, the old black
cell that caused the record is restored. A record is not the permanent
consumption of one initial black cell.

For actual row black counts define

  E_h=12b_h-8b_(h-1)+4b_(h-2)-b_(h-3),
  R_h=8b_h-7b_(h-1)+4b_(h-2)-b_(h-3).

The six-step record birth satisfies E_(h+2)-E_h=4-R_h. The completed and prefix
theorems control changes in R_h. Their initial B,C terms must be retained.
Even a valid bound on each record does not bound the number of records.

The later adaptive-cut ledger improves the endpoint allowance and removes
the apparent positive shift cost after the first stage. It still does not
bound energy production during the intervening lower excursions. The C row
of one stage is the A row of the preceding stage, but later C visits can
extend outside that earlier visited area. Rows discarded by an earlier cut
can also be changed later. These are actual state terms, not notation errors.
See global/ for the completed ledger and its explicit scope.

There is also an exact obstruction to bounding the next energy from the
current four-row state. See boundary/delayed_record_family.md. Start at
(0,-7), facing north, with four fixed black cells

  {(1,-7),(-1,-6),(-3,-6),(-2,-5)}

and the one extra black cell (-18-2n,13+2n), for any integer n>=0. At the
genuine record cut t=83, every member has the same pose, the same entire
T,A,B,C rows, and Q=3. Its next record cut is 967+104n, with

  Q_next=59+7n.

The first exit above the cap occurs at 970+104n. A finite translation-orbit
certificate proves these formulas for all n. The 312 baseline color checks
and 61 suffix color checks cover all future translation indices by explicit
thresholds. They are not samples of parameter values.

The number of forbidden ten-turn windows wholly before that exit is exactly
96 for every n. The unbounded increase in Q comes from inserted standard
periods. This disproves a bound on Q_next from the current active four rows
alone. It is a family of finite delays, not an infinite nonstandard orbit.

The present arguments therefore do not prove that the number of nonstandard
ten-turn windows is finite. In the cited factor-language framework, that
finiteness would imply eventual standardness. The finite bound on the next
event, a small observed event density, and successful tests of many seeds do
not prove event finiteness.

Raw visit counts and writes can grow without bound during an ordinary
standard highway. A global argument must allow that standard production and
control the effect of old information on later nonstandard motion. It cannot
simply declare that every lower visit or every stored black cell is disorder.

Two other investigations are retained:

* sources/compactness_and_first_divergence.md explains why compactness of
  bounded-cardinality seed sets does not give a uniform event bound. A limit
  recentered at a distant first disturbance contains a backward-infinite
  standard wake. It is outside the finite-support hypothesis.
* root/gate_* records perturbation tests using fixed-size seeds at different
  distances. Every reported positive capture uses an exact future-ray guard.
  These tests found no unbounded nonstandard-event mechanism in the tested
  families. They are experiments, not universal exclusions.

VALIDATION

The analytic arguments were read independently within this session. The
following separate calculations support them:

* The arbitrary-color proof has a physical event-assignment checker and an
  independent checker over 451,630 completed segments.
* root/check_cap_words.cpp branches on the initial color of every first-read
  cell. It checks all physically consistent words through length 32 for
  starts W at (0,-4), E at (0,-4), and W at (0,-6). Across those starts it
  checked 8,345,289 completed prefixes with a top visit. The four refined
  correction terms and all displayed row identities passed.
* root/check_cap_shift.cpp checked the weaker fresh-A inequality on all
  physical words through length 40 for E/W starts at (0,-4), covering
  13,120,974 completed prefixes with a top visit. Its maximum S was zero.
* root/check_cap_shift_stronger.cpp checked S+L_C<=0 through length 32 for
  those two starts, covering 233,697 completed prefixes with a top visit.
* root/check_cap_shift_prefix.cpp and root/check_adaptive_cut.cpp record the
  endpoint maxima of S+L_C through length 32. They agree with the proofs.
* The converter coverage audit checks every accepted profile ID, exact input,
  completed result, independent profile count, positive control, and hash.

No finite-word depth, random test length, or timeout is used as a substitute
for a mathematical all-length argument.

REPRODUCTION

The Python programs use the standard library. C++ programs require a C++17
compiler. Run commands from the directory that contains ant_global.
Supplied compiled executables are Linux binaries. Recompile on other systems.

Quick exact witnesses:

  python3 ant_global/global/check_partial_cap_sharp.py
  python3 ant_global/global/record_birth.py
  python3 ant_global/sources/check_arbitrary_cap_bridge_sharpness.py
  python3 ant_global/boundary/certify_delayed_record_family.py

Finite-word check (choose a small depth first):

  g++ -O3 -std=c++17 ant_global/root/check_cap_words.cpp -o ant_global/root/check_cap_words_refined
  ant_global/root/check_cap_words_refined 28 3 4

Fresh-A check:

  g++ -O3 -std=c++17 ant_global/root/check_cap_shift_stronger.cpp -o ant_global/root/check_cap_shift_stronger
  ant_global/root/check_cap_shift_stronger 28 3

Converter evidence audit:

  python3 ant_global/sources/audit_negative_converter_coverage.py

For a full converter replay, follow the commands in
sources/negative_converter_exclusion.md. Replays write separate result files
so the retained accepted logs remain intact. The audit's --results option
selects the new complete log rather than combining it with retained logs.

The first accepted converter process stopped before the last profile for an
undetermined operational reason. Every missing profile was then run to
completion. The audit uses both accepted logs and requires exact, duplicate-
free coverage of all 30,431 IDs. No interrupted profile counts as an exclusion.

SOURCE RECORD

See sources/source_status.md for pinned source URLs and exact scope. The main
primary records checked were Jillhewar's highway repository, Ke's ant-core
repository, Etse's MFCS 2026 paper, and OpenAI's October 2026 mathematics
release. Source access does not constitute external review of these new notes.

The supplied earlier fresh-cap proof and scattering decomposition are retained
in foundations/. Downloaded third-party research notes are not copied into
this bundle; their URLs are supplied instead.

MANIFEST

manifest_sha256.json lists the delivered files and their SHA-256 hashes.
Excluded scratch items include early conversion screens that were superseded
by the independent complete inventory, duplicate executables, and Python cache
files. The retained records are sufficient for the completed claims above.
