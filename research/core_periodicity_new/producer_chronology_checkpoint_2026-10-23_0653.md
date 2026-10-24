# Chronology/resource checkpoint, 2026-10-23 06:53 UTC

## Global scope

Coverage remains11/13 DCUV unfunded record cases. V1 and U1 remain open. Universal
finite-seed capture remains unresolved. No new confinement theorem is claimed.

## New signed mathematical resource layer

`height_age_multiset_lemma.md` gives exact current high residual counts split by
saturated C-age0..4, ordered by tail counts x_j=#tokens age>=j at each height.
Initial high counts are zero after signed whitening. For input demand tails I,
output count O and packet C count c, the exact minimal coverability predecessor is
p0=I0+max(0,t0-O,t[c+1]), pj=Ij+t[j+c] (out-of-range t=0). The exact simultaneous
maximum successor is yj=x0-I0+O for j<=c, and min(xl-Il:l<=j-c) otherwise.
Auditor independently approves both all-count formulas and exhaustive controls:
1,333,584 predecessor allocations and199,584 forward-optimum cases. This removes
matching disjunctions and guessed count caps from the backward relaxation.

Engines/builders:
- build_record_height_age_petri.py
- record_height_age_petri_backward.cpp / _bestfirst.cpp / _forward.cpp
- record_height_age_petri_interval.cpp (sound omega upper-join per control)
- replay_record_height_age_petri_witness.py (separate birth-C timestamp replay)
- match_record_witness_producer_roles.py (fixed-word full bipartite HB matching)

Best-first changes order only. The interval join is conservative and is not an
exact reachable set. Forward cap3 is a LOSSY UNDERAPPROXIMATION only. Caps are
UNKNOWN, never no-hit results. Symbolic results cover newer weighted/fast engines.

## Strong negative controls: this resource does not itself close either case

All paths below are abstract resource controls, not ant trajectories.

1. U1 full k6,23 high heights:224 strict packets+goal,94C,peak45tokens/height.
   Source delayed_height_probe/u1_k6_age_interval8.best.replay.json. Auditor
   independently replays all124high-input allocations; artifact
   audits/replay_height_age_resource_independent.json. It admits complete
   HB-compatible producer-role matching, but uses lossy low-height chronology
   and has20literal-impossible7factors.
2. V1 full k6,21highheights:139strict+goal,58C,peak30tokens/height; complete
   HB matching64/64. Prefix v1_k6_age_interval8.12illegal7factors.
3. V1 full k7 plus exact head-height strip down to-34:148strict+goal,58C,
   peak32tokens/height, complete HB matching66/66. Its actual head height stays
   [-20,2], so it NEVER uses the low reset. This is a robust negative control
   for age×height + pairwise lineage + all7factors.21illegal8factors remain.
   Prefix delayed_height_probe/v1_k7_deep_age_interval8, .heightdiag.json
   proves exact cumulative height on this particular control.
4. Symbolic's first fullresidue4 current-age U1 control has263packets INCLUDING
   goal (262strict), not264in the initial human report. My same-residue HB
   matcher supplies150/150inputs against360outputs. Latest weighted05 likewise
   matches183/183inputs against391outputs,311packets includinggoal.

Fullk7 necessary DFA generated once as chronology_dcuv/literal_factor_dfa_k7.json:
1,996classes,26,759suffixstates,92,359legal7factors. Not independently signed yet.
Source builder unchanged. Symbolic results cover U1 residue4 selective7/8 CEGAR and omega
antichain ideas. This section covers exact low-height excursion compilation.

## Signed exact low-excursion lemma and executed compiler prototype

`exact_low_excursion_summary_lemma.md` is signed analytically in audit KB. Choose
L below all high residual crossings and core/created record limits. Every low
packet leaves current high resources unchanged except aging. Exact low paths are
one-counter paths on heading×packet-DFA, weighted by saturated C count. Private
unit expansions and balanced Dyck saturation produce an exact finite relation;
maximum C is attained by an actual finite path and dominates younger low paths.
Only the monotone high-token resource scope is signed. Retained colors or other
nonmonotone effects need their own absence/effect proof.

Explicit port formula: reduce unmatched counter word to pop^k push^l. Entry d,
exit e give k<=d and l=e-d+k>=0. Use balanced R between all unmatched edges.
Initial arbitrary low depth is R(Pop R)^* followed by <=e Push R factors; parity
is checked at actual ports. No arbitrary low-height reset is needed.

Sources:
- build_low_height_unit_graph.py
- weighted_dyck_summary.cpp
- check_weighted_dyck_summary.py (separate finite derivation soundness AND complete
  fixed-point closure, so no finite stack cap is used for the exact certificate)
- compile_low_height_ports.cpp
- check_low_height_ports_bounded_controls.py (bounded controls, not proof)

Executed exact balanced closures:
- k3:444vertices/576edges,10,196balancedpairs,12,284finiteproofnodes.
- k5:4,300vertices/5,712edges,427,063pairs,503,641proofnodes.
Both pass separate author-side exact DAG+fixedpoint checks.
Port compiler L=-18,W=8 gives k3:208ports/22,638summaryedges/162initialports;
k5:2,048ports/1,420,787edges/1,301initialports. Direct stack24 controls exactly
match all43,264k3profiles and131,072sampledk5profiles, includinginitialports.

Frozen for independent audit: low_summary_frozen_20261023_0648/manifest.json,
29files/145.8MB. Those frozen files will not change. Auditor has the path and will
sign compiler semantics separately from literal graph reconstruction or record
integration. No record no-hit invariant exists.

## Current live process / next work

Fullk6 exact balanced closure ALREADY COMPLETED:18,332unitvertices,
5,328,190balancedpairs,5,996,300finiteproofnodes. Files
chronology_dcuv/delayed_height_probe/low_k6_dyck.sparse and .proof (~300MBtotal).
The sparse file carries endpoint,weight,finiteproof-root per reachedpair.
This k6 closure has not yet had the separate full exact checker adapted/run.

sparse relation. Command:
./compile_low_height_ports low_k6_unit.dat low_k6_dyck.sparse low_k6_dyck
2108 527 0 -18 8 200000
(all paths under chronology_dcuv/delayed_height_probe). Inspect/poll this handle
before any rerun; ps alone is not authoritative. Output low_k6_dyck.ports.txt/log.
Latest source differs from frozen k3/k5 ONLY to accept sparse I/O and avoid huge
all-matrix text. Do not mistake the frozen semantics signoff for this new I/O.

A further good implementation direction is finite transverse residue annotation
on each Dyck pair, keeping max C separately by net transverse displacementmod4;
Symbolic offered to own that extension. It need not duplicate all graph vertices.
Full dense proof-root matrices dominate memory; a sparse relation-recordID store
would reduce this if needed. Current machine has9.7GiBRAM,~7.9GiBavailable atlast
check,32GBdisk with8.6GBfree before the latest ~300MB k6 outputs.

 All artifacts local.
