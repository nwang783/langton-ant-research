# Prominent scope correction: zero-output complete WHITE fronts are already excluded

24 October 2026, 01:30 UTC. This additive clarification applies to ALL
stage15 through stage20 handoffs and their dependencies. Frozen sources
are preserved, not rewritten. Independently reviewed by
continue_ant_independent_audit.

## 1. Existing retained theorem, exact scope

Every complete bi-infinite WHITE translating front with actual full
period P and nonzero full drift d satisfies

    g=R-L=Nodd >=2||d||_infinity >0.

This is the retained signed residue theorem of
`sources/kehao95-core/wake_synthesis/proof/periodic-growth-closure.md`,
section2.3, source SHA prefix bd3e74c5. It needs no multiplicity cap,
K1 hypothesis, unit-diagonal certificate, or new stock-hole argument.
For each nonzero drift coordinate a, each residue modulo |a| has
checker-signed odd-class count congruent to2 modulo4. Thus at least
2|a| odd classes are necessary; quarter rotation gives the y bound.

## 2. The complete-WHITE to finite-input bridge is exact

At any time cut of a complete P,d front, the set of physical cells
visited both before and after the cut is finite. Indeed each of the
finitely many phase classes has only a finite interval of translation
indices for which some phases are past and others future.

Set BLACK precisely the currently black FUTURE-read cells in that
finite overlap, and WHITE elsewhere. Every genuinely fresh future cell
starts WHITE by the complete-front hypothesis, and every discarded old
wake cell is never read again. This finite seed reproduces the ENTIRE
future periodic word with its same actual full P,d. Therefore the
retained finite-support residue theorem applies directly to our scope;
there is no prepared-input or infinite-wake exception allowing Nodd=0.

## 3. What this changes in earlier progress descriptions

Every theorem whose ONLY conclusion is an exclusion or period lower
bound under the GLOBAL hypothesis Nodd=0 is COUNTERFACTUAL in the
complete WHITE-front setting. It is not a fresh live front exclusion,
not an improvement over the retained positive-output theorem, and must
not be presented as such. This includes the zero-output K1 eighteen-
current conclusion, whole-front half-turn/late-route consequences and
the zero-output stock-hole/face-loop conclusions in stages15 through20.

Their local algebraic implications, exact complete-history gates and
conditional motif identities remain valid. They may be used on an
actual locally even patch if its exact hypotheses are separately
proved; one must retain required positive odd defects elsewhere.
The immutable older proof files are not declared false. This correction
concerns significance and live scope, not their conditional logic.

## 4. Live results that remain substantive

- Every clockwise contractible canonical node is an elementary C-face
  four-edge loop, WITHOUT a zero-output assumption: signed2c2d0905.
- The simultaneous contour contact barriers ad564468 hold at every
  sheet for all outputs.
- The nonzero-output nonleaf stock-hole capacity e2161703 is live:
  h<=Nodd-Ntop+J, with actual disjoint disks and paired top roots.
- The nonleaf parallel-exchange tradeoff160ea8de is live:
  beta>=F4 and h<=J+F4<=J+beta, without an output-zero premise.
- Flow-three source-sink pairing, its essential-cycle theorem5036e7c2,
  early output capacities and all exact physical ordinal identities
  remain live at positive output.

Future essential assembly must retain Nodd>=2||d||_infinity and treat
odd defects as required parts of the actual front. A zero-output global
assembly is not an unresolved candidate front.

## 5. Independent binding

`audits/check_WHITE_front_positive_output_scope.py`
SHA d2a41ca0307f12b9f37ab09557bf834d22f31b8ae0b7022a1b72d10c6994aeac.

`audits/check_WHITE_front_positive_output_scope.json`
SHA f0e306e2c1b2f8b05f75a56b6e0d2018b017a7c5a915f76cf6a523e5f97796da.

The independent report verifies the finite-overlap construction and
4096 exact local mod-four potential checks. The section2.3 residue
monodromy is sufficient; no stronger growth-eight dependency is needed
for the zero-output scope correction.
