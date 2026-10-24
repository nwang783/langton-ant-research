# What known long-distance scattering families do to the proposed budget

23 October 2026. Author analytic deductions and exact count controls. Independent
review pending. Universal capture and fixed-mass budget finiteness remain open.

## 1. The bi-standard restriction does not weaken the budget premise

Let N(X) be the number of future true-history adjacent-bad-ten events, allowing
infinity. Let H be forward standard capture and S=H intersect I(H), using the
exact reversor. Put

    B(m)=sup {N(X): X finite, initial black mass<=m},
    b(m)=sup {N(X): X in S, initial black mass<=m}.

Both suprema are taken in the extended natural numbers. The signed twelve-cell
completion theorem gives the exact sandwich

    b(m) <= B(m) <= b(m+12).                               (1)

The first inequality is inclusion. For the second, take any q<=N(X). Protect
at least ten negative turns and a positive prefix through q actual events.
The completed state belongs to S, has mass at most m+12, and preserves those
events. Thus b(m+12)>=q. This applies also to every q when N(X)=infinity,
and to arbitrarily large finite N across a family.

Consequently fixed-mass budget finiteness for all bi-standard inputs is
equivalent, up to the mass shift, to uniform fixed-mass event budgets over ALL
finite inputs. It is a genuinely global premise, stronger than merely saying
every individual input captures. Restricting to already positive scattering
states makes finite diagrams available, but does not automatically simplify
the bound.

The same completion transfers any already captured X to a bi-standard Y with
mass at most |B_X|+12 and

    N(X) <= N(Y) <= N(X)+197.                              (2)

To obtain (2), protect the entire finite pre-standard prefix and ten subsequent
standard turns in a square, and protect ten negative turns. The first positive
exit then occurs after every original K event. Before it, all events are the
original ones. The inserted quadrant port has at most187 transient reads,
followed by standard104. At most ten further boundary windows remain; hence
at most197 new K events. The reverse port is disjoint from the whole positive
read set. The exact value197 is a safe bound, not an optimal event count.

No computability of a finite b(m) is inferred from (1). No uniform budget is
asserted here.

## 2. Exact standard-power compression lemma

Let F be the84 cyclic ten-factors of standard H104. Define the K predicate
on an eleven-letter word z by

    z[:10] not in F AND z[1:] not in F.

It vanishes on every cyclic standard eleven-factor. Fix arbitrary left and
right contexts A,B, and any cyclic phase U of H. For every n>=1, replacing
A U^n B by A U B leaves its TOTAL K count unchanged, provided the same
boundary history is supplied on the left.

Proof. An eleven-window entirely inside U^n is cyclic standard, hence has
zero cost. A window meeting the left boundary sees at most ten letters from
the start of U^n, independent of n; one meeting the right boundary sees the
same suffix of U. No eleven-window can meet both boundaries because even
one U has104 letters. Removing whole cycles therefore removes only zero-cost
windows and preserves all boundary windows, with multiplicity. This proof
also applies to any finite-window cost that is zero on the standard periodic
stream, with target length at most104; no ant feasibility is assumed.

Apply this separately to ANY finite number of independently variable standard
powers in a certified turn template. The total count is determined by a single
fixed compressed word, not by flight lengths. This is a finite-context count
identity; it does not bound how many nonstandard interaction blocks an arbitrary
actual trajectory can generate.

## 3. The43-cell two-parameter loop family has exactly5963 future K events

Use the independently signed all-r,s family, r,s>=50, from
`../causal_reduction/unit_scale/unequal_four_corner_loop_certificate.json` and
`unequal_four_corner_capture_certificate.json`. Its actual full turn stream is

    R H^r H[:68] R H^s H[:68] R H^r H[:68] R H^s H[:60]
    C H^(s-10) D H^infinity,

where C and D have fixed lengths4954 and9458. Its capture boundary is
208r+312s+13640, unbounded in two independent geometric parameters.

Its true preceding ten turns are always

    RLLLLRLLLL.

This assertion is not based on sampling. Thirteen initial cells are constant.
For each of the other thirty affine seed points, a coordinate with coefficients
of one sign is already outside[-12,12] at r=s=50 and only moves farther away.
Thus none can affect the ten inverse reads, all of which are within ten lattice
steps of the initial pose. The exact coordinate witnesses are serialized in
the count report. Literal inversion of the thirteen-cell local seed gives the
displayed history.

Replace the four variable H powers and H^(s-10) by one H each. Append the first
ten letters of the final tail so every possibly bad boundary window is counted;
afterward every eleven-window is wholly standard. The resulting fixed word,
including those ten tail letters, has length15210. Two independently formulated
local counters, one string-based and one packed streaming automaton, give

    N(X_(r,s)) = 5963 for every r,s>=50.                    (3)

The all-parameter physical execution is imported from the independently signed
loop/capture certificates. The new all-parameter count identity is the analytic
compression lemma plus the finite exact calculation, not finite simulation
extrapolation. Eight complete template expansions corroborate the result.

In particular these fixed43-cell long closed excursions do NOT refute b(m)<infinity.
They supply finitely many interaction blocks and arbitrarily long zero-cost
standard interiors. Their bi-standard twelve-cell completions have at most55
initial black cells and, using (2), between5963 and6160 future K events.
No claim is made that the unmodified43-cell seeds are themselves bi-standard.

## 4. The retained20-cell feedback circuit also has constant count

This section is CONDITIONAL on the retained all-parameter execution/recovery
theorem in
`../sources/kehao95-core/memory_feedback/proof/scalable-feedback-circuit.md`.
That theorem has not received a new all-n geometry reconstruction in this work.
Fresh physical controls below do not replace its universal separation/guard proof.

For even n>=20, let k=n/2. The certified turn stream consists of five fixed
182-turn port preludes A, separated by

    H^(k-4) H[:61], H^(2k-5) H[:71], H^(4k-6) H[:61],
    H^(2k-7) H[:71], H^(3k-4) H[:14],

then one fixed774-turn recovery and the cyclic phase103 standard tail. The
input has twenty black cells, the created lifetime has age624n-1576, and exact
standard entry is at624n-742.

All sixteen moving input cells lie outside the inverse-history neighborhood
for n>=20. The four fixed gate cells give the same preceding ten turns
RLLLLRLLLL. Replace every positive H power by one H, append ten final tail
turns, and count the resulting2492-letter compressed word. The exact result is

    N(X_n) = 440 for every even n>=20,                      (4)

conditional on the retained execution theorem. The source's already reported
532 J10 events from update9 onward is a DIFFERENT count and is not relabeled
as440 adjacent K events. The lifetime's unbounded age therefore does not
supply unbounded K count at fixed mass.

The fixed recovery was independently reconstructed by direct simulation of
n=20, and its SHA256 is
9f59ff6b715683c6b3950523cb47c7b3dfb0ec454e0a4470ae89e93c7e9cf667.
Fresh complete physical replays for n=20,22,24,30,50,100,202 exactly match the
retained stage template and this same recovery, and both count detectors agree.
These are controls supporting the count implementation; the conditional
all-n scope remains explicit.

## 5. Why existing trains are not fixed-mass counterexamples

The retained30-rule guarded trains preinstall one distinct marker per
interaction, giving mass13+k+|G| for k rules. Their recovery blocks have bounded
length at most32656; long standard gaps have zero K cost. At most ten windows
per recovery boundary can remain nonstandard afterward. Thus, on this EXACT
certified class,

    N <= 10 + 32666*k.

The initial ten accounts for true-history boundary windows. There is no claim
that an arbitrary finite seed admits this marker allocation.

The retained genuine-return packet trains similarly preinstall THREE distinct
markers per packet and have mass13+3k+|G0|. Their variable n flights are standard
and can be compressed, while their fixed A,C,E blocks have lengths832,51272,
23661. The two flights have104n+14 and104n-170=104(n-2)+38 turns. Keeping one full cycle of each leaves at most

    832+(104+14)+51272+(104+38)+23661+10=76035

possibly charged reads per packet, including the ten tail-boundary windows.
Thus N<=10+76035*k on this exact train class, independently of every excursion
length. The arbitrary number k is encoded in increasing input mass, not in
separation alone. Complete-history return is real, but repeated return is not free fuel.

The inward spiral is different: its long variable arms repeat S=RLLR, whose
cyclic ten-factors are bad. Its actual K count grows quadratically, but its
initial mass11n+2 grows too. The compression lemma cannot delete S periods at
zero cost. The spiral therefore rules out a LINEAR mass-only bound, not a finite
budget at every fixed mass.

## 6. Current conclusion and an unexcluded architecture

No retained fixed-mass family examined here has unbounded actual K count.
This is not evidence that a universal fixed-mass budget exists. Boundedly many
prepared components need not imply boundedly many collisions: an actual front
can return to its own growing scars and reactivate them.

One concrete possible falsifier is a fixed cap that launches a NONSTANDARD
periodic rewriter along a length-N standard wake produced by an earlier flight,
leaving a DIFFERENT bulk profile. N repetitions could give linear K growth
at fixed input mass, followed by eventual endpoint capture. The reverse104 and
ten-turn D mechanisms are excluded by retained supply guards; exact oblique
profile order excludes restoration cycles/complete erasure, not every changed-
output rewriter. No such rewriter, finite-seed launch or endpoint capture is
asserted here. Infinite prepared-background components alone do not suffice.

A separate explicitly scoped search tests small finite XOR caps on the infinite
bilateral standard wake, using a full-background infinite-tail oracle. Its result
must retain that infinite-background limitation and is not a finite-seed budget
experiment. It is a component search, not an undecidability reduction.

## 7. Artifacts

`check_fixed_mass_scattering_counts.py/json` records the exact counts, all thirty
moving-cell separation witnesses, both detectors, phase/power controls and
complete physical20-cell controls. `feedback20_recovery_word.json` preserves
the fixed freshly reconstructed recovery. Dependencies retain their original
files unchanged.
