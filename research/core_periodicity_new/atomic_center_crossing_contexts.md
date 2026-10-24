# Exact proper atomic center crossings force a cohort contact

Status: author complete finite reconstruction PASS, 2026-10-23 14:14 UTC. Static geometry and complete-context survival only. No chronology, simple-loop turn bound, fuel or capture is inferred.

At an actual marked atomic cut (p,h), use the corrected center p+rot_h(-1/2,-1/2). The literal D,V,U,C atoms have corrected-center increments rot_h(1,1), rot_h(1,3), rot_h(0,4), rot_h(1,1), respectively. C here occurs only as an actual prefix/tail atom of a retained complete-eight packet. All four literal raw-plus-marker contexts and residual input/output masks are independently reconstructed by the executable.

Normalize the first atom to entry(0,0,N). Its fresh output cohort O is the residual output set at that atom's exit. Every member remains a distinct current residual identity until a later packet input retires it. Subsequent C tails have no residual inputs and preserve this cohort. For C-prefix sources, the complete-full-producer identities are retained; no unproved pseudo-packet age inequality is used.

Consider a later atom whose corrected-center chord meets the FIRST chord transversely at a point STRICTLY INTERIOR to BOTH chords. Its entry pose is(p,h), with the conserved sector p.x+p.y+h even. Collinear overlaps, endpoint contacts, and nontransverse tangencies are excluded from this statement.

## Completeness, without a guessed spatial box

Work in doubled center coordinates C0=(-1,-1). Let d,e be the doubled first/later increments. A proper crossing has

2p=C0-rot_h(C0)+t d-u e, with 0<t,u<1.

Thus every candidate integer entry pose is in the coordinate bounding box of the four explicit parallelogram vertices with t,u in{0,1}. The executable enumerates precisely those bounded integer candidates, imposes the sector, and tests both rational parameters by exact integer determinants. No empirical distance, packet-depth or C-count cutoff is involved.

## Exact catalogue

There are42 cases: firstD two, firstC two, firstV twenty, firstU eighteen. All later headings are E or W,21 each. There are no relative-N/S proper crossings in the conserved sector. This does not remove endpoint/touch cases with those headings.

Every one of the42 later complete contexts touches SOME first-atom output. In40 cases at least one such output lies in a later WHITE-required or entry-CORE cell, rather than a later residual input. That output's old identity must have retired STRICTLY BEFORE the later atom starts: a current old residual cannot silently become entry core, and a white demand cannot coexist with it. The complete-context identity-survival theorem supplies exactly this conclusion. It is an ordered residual-identity retirement, not necessarily physical black erasure.

The only two exceptions are firstD or firstC followed by a later V at(-1,0,E). Its sole touched source output is(2,0), which becomes V's lower residual input(0,3). That identity may retire AT the crossing V rather than earlier. These exceptions do not show that the complete intervening history exists.

For D/C first chords, these E cases and V at(1,0,W) are the ONLY proper crossing geometries. The latter places(2,0) in the later V's entry-core cell(0,-1), forcing strict prior retirement.

For firstV and firstU, ALL proper crossings require at least one strict prior source-cohort retirement. The exact forced slots are listed per case in the JSON.

## A stronger single-output inference is false

The common fresh output(2,0) alone is not a universal crossing detector:20 cases avoid it completely. A smallest literal pair is firstV at(0,0,N), laterD at(0,1,E), with both chord parameters1/2. The later D's complete raw-plus-marker context avoids(2,0), although it touches other V outputs and therefore still requires cohort cleanup. This is a STATIC counterpair to the proposed universal single-output implication, not a chronologically feasible ant factor.

## Exact scope and ownership

This is a geometric specialization of signed literal masks and complete-context identity survival, not a new local no-hit relation or a fresh-root theorem. Strictly earlier retirements can be performed by arbitrary supporting packets; no bound on their number, age, ancestry roots or reconvergence rank is asserted. A separate proposed first-contact turning-angle restriction is NOT used here. In particular no unbounded chronology has been discarded on the strength of a floating-point drawing or bounded word search.

Replay: check_atomic_center_crossing_contexts.py writes chronology_dcuv/atomic_center_crossing_contexts.json, including every exact bounding parallelogram, every crossing parameter, all context/input/core/white classifications, and all forced source slots.
