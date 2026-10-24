# Three actual cap-six resource witnesses have no immediate physical pair

24 October 2026. Exact supplied-candidate composition test. Each candidate is
physically executable from a finite board; none of their nine ordered pairs
is executable with its prescribed COMPLETE active-component profiles. This
is not a general cap-six exclusion. A separate application of the complete-
field import-budget lemma below also traps P and T individually; Q remains
open to different intervening profiles.

## 1. Exact individually physical candidates

The compact source is
`../reframe_finite_seed_2026-10-24/physical_cap6_resource_obstructions.json`.
Use its three distinct profile indices, normalized to head(0,0),N and fixed
w sector1. All controls keep the complete field and active fine-cut mass<=6.

P=2818:

    seed {(-1,1),(0,1)}, initial mass2;
    word RRRRLRL;
    exit(-2,1),W, active w empty;
    output straight dimer {(-1,0),(0,1)} plus star S.

Q=33389:

    seed {(0,1),(1,2)}, initial mass2;
    word RRRRLRRLRL;
    exit(1,3),N, active w empty;
    output corner {(-1,0),(-1,1)}, singleton {(0,2)}, plus S.

T=33390:

    seed {(-1,3),(0,1),(1,2)}, initial mass3;
    same word and exit as Q;
    output corner {(-1,0),(-1,1)}, straight dimer {(-1,3),(0,2)}, plus S.

Here S={(0,-1),(1,-1),(1,0)} is a complete three-edge star. Every listed
output module is a COMPLETE w component in the corresponding literal control.
The source's abstract type circulation P+Q preserves its two-edge resource
and creates a singleton and two stars. P+Q+T supplies a further resource
relaxation. Those arithmetic statements alone do not give a physical circuit.

## 2. All nine immediate pairs fail with arbitrary unread exterior

**Theorem.** No ordered pair in {P,Q,T}^2 has a complete finite-board lift
with the ordered source transition profiles and the physically dictated
translation/rotation at the seam. Passive components stay at their actual
positions. Adding an arbitrary pre-funded unread exterior cannot repair it.

**Proof.** Use the exact complete-port/read-parity lift criterion independently
signed in TWO_CLEAN_RETURNS_OBSTRUCTION.md Section3. At every cut require the
proposed complete active edges black and every other port incident to their
vertices OR the cursor white. Pull each requirement back to the initial bit
using the parity of all earlier actual reads of that physical cell.

For every pair starting with P, cell(-1,0) is forced initially WHITE by P's
complete active field at cut1. P actually writes it at update5, and never
deletes it before the seam. At cut11, four R updates into ANY of the proposed
second profiles, that second complete field requires the same cell to be
WHITE again. The supplied physical plan has read it exactly once, so this
requires it initially BLACK. Contradiction.

For every pair starting with Q or T, cell(0,2) is forced initially WHITE by
the first profile's complete field at cut1. It is R-born at update8. At cut14,
four R updates into ANY proposed second profile, that second complete field
requires it WHITE, again after exactly one physical read. It would have to
be initially BLACK. Contradiction.

All nine pairs are covered by these two explicit same-cell constraints.
Unread external bits cannot change a bit already forced at the earlier cut.
This is an output-lifetime/port conflict, not merely a rotation or heading
closure objection, and need not be visible from the R/L word alone. QED.

The bad old cells are genuinely current R-born outputs. P's bad edge belongs
to its surviving dimer; Q's is a singleton, and T's belongs to the surviving
dimer made with its pre-funded extra edge. They are not never-read passive
cycle labels. The full component identity, not just its mass/type, detects
the compulsory later contact.

## 3. Exact finite-profile realization helper

`finite_component_profile_lift.py` is a pure reusable implementation of the
already signed finite supplied-profile criterion. It accepts ordered kernel
transitions, rotates/translates them using the CONTINUOUS physical pose,
and constrains all complete-component incident ports at all fine cuts,
including the final isolated cursor. A consistent requirement system constructs
the finite seed of all forced initially black cells, then directly replays
the COMPLETE board and every component. A contradiction returns its two
opposite initial-bit requirements. Positive cases also retain actual R-birth
and L-consumption identities and whole-component import provenance.

`check_three_cap6_profiles.py` reproduces all three literal seeds and all
nine pair contradictions. `three_cap6_profiles_certificate.json` contains
the complete single-profile traces, output fields, actual import/consumption
records and the nine exact witnesses, binding the compact source hash.
No large return enumeration, unrestricted board scan, virtual recolouring,
mid-run added cells or translated archive is used.

## 4. Remaining transport obligation

The source profiles are individually valid and the type accounting fails to
exclude them, but their proposed immediate resource circulation is not a real
execution. The pair theorem alone does not exclude a different intermediate
profile or routing phase.

A SEPARATE stronger application of EMPTY_CURSOR_IMPORT_BUDGET_TRAPS.md uses
the entire mandatory output of each supplied full profile, not only cells
whose last physical read was R. The minimal finite seed contains every
initial cell forced black by the complete-profile guards. All additional
initial cells are outside every guard/read and remain unread, so the minimal
seed's final black field is a subset of EVERY realizing board's final field.

For P, its forced surviving old cell(0,1), together with the R-born cell
(-1,0), forms a two-edge component at a nonfirst port of the next empty root.
For T, its forced surviving old cell(-1,3) joins the R-born cell(0,2) in the
same budget-saturating way. Their other next-root neighbor ports have no
additional forced field. Thus the general budget lemma traps P and T
individually on a sustained-cap6 orbit, regardless intervening routing.
This does not deny their one-shot realizability. Q has only a mandatory
singleton at that nonfirst port and remains unresolved by that lemma.

The old cells here are mandatory FULL-PROFILE members, not claimed necessary
for the turn word alone. Their unconsumed presence strengthens the physical
component obstruction, while the explicit pair-conflict cells themselves
are actually R-born. No complete cap-six impossibility or global attraction
is claimed.
