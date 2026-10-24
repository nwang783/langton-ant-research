# A white-input H/LR/Q ownership relaxation, not a continuous ant front

Status: author-checked positive complete color histories. The three physical connectors are missing. No renewal, nonstandard highway, finite-seed construction, or counterexample follows.

Use headings N,E,S,W = 0,1,2,3 and drift D=(2,2). The exact H and Q words are frozen in short_refinement_scaffold_inputs.json and forward108_prepared_control.json. Q is the separately normalized forward time reverse of the prepared108 word, at heading E, not the old reversed pose.

## 1. The derived two-cell repair

The mature standard H rail translated by (0,10) supplies two of Q's three required-black classes. On Q's read footprint it has precisely these two mismatches:

- A=(-1,6), class (x-y,x mod2)=(-7,1), is black but must be white.
- B=(0,6), class (-6,0), is white but must be black.

Starting at A with heading S, the literal word LR reads A then B, toggles exactly those two cells, and ends at (0,5,S). This is an adjacent black transfer, not a closed-pose operation. Its actual pose change is essential.

## 2. Complete chronological positive relaxation

In each period, prescribe these three disconnected pieces in the listed order:

1. H at (0,10,E), ending (2,12,E).
2. LR at (1,8,S), ending (2,7,S).
3. Q at (0,0,E), ending (2,2,E).

Translate all pieces by nD in period n. For each cell orbit a=(x-y,x mod2), sort the event from phase position p and piece/local index (b,j) by ( -floor(p_x/2), b, j ). This is the actual temporal order on a fixed representative cell across all translated periods. Every one of the 42 orbit histories starts R and alternates. Their total contains 214 reads, signed charge20, and20 final-black orbits. The full histories are in forward108_domino_repair.json.

More generally, place H at (2l,10+2l,E), repair at (-1+2t,6+2t,S), and Q at (0,0,E). The corresponding whole-piece ordering conditions are l>=-1, l-t>=-2, t>=1. The displayed choice is l=0,t=1; it is one compatible phase, not a completeness claim over all choices.

This gives correct bulk color ownership only. Its displacement sum is (5,3), not D, and the endpoints do not join. It is not even a continuous path before the missing reads are supplied.

## 3. Shortest connector obstruction

The missing pose-to-pose connectors in this displayed phase are:

- (2,12,E) to (1,8,S), shortest length7, exactly3 direction words.
- (2,7,S) to (0,0,E), shortest length15, exactly21 direction words.
- (2,2,E) to (2,12,E), shortest length20, exactly126 direction words.

The corresponding continuous full word would have length256 and driftD. All7,938 shortest triples fail full white-input orbit chronology; check_pipeline_shortest_connectors.py/json preserves one exact witness per triple. This finite result has an elementary stronger reason within its scope: every shortest first connector starts south, hence R from E. But H reads its endpoint (2,12) at its own index40 with R, and does not read it again before ending there. Thus this cell is black at the connector entry on every realizing board, forcing L/north. The contradiction occurs before the other two connectors execute. Likewise a shortest final connector approaches its penultimate cell (1,12) northward and demands R there, although H's final read103 left it black and the assumed other pieces do not repair it. The first argument alone suffices.

No longer connector is excluded by this observation. No shortest-length parameter was increased.

## 4. Separate discovery relaxations

The complete all-count incidence system on normals -17 through3 is feasible with all H/LR/Q physical read-type counts as lower bounds, white input, free binary output, and total displacementD. A floating MILP proposes a232-read integer flow; its integer equalities and nonnegativity are checked exactly in probe_pipeline_integer_flow.py/json. It has24 output-black classes. This is not a chronological path, nor is the optimizer's minimality used as a theorem.

The ONE supplied232-read flow has no ordinal/clock chronology in check_pipeline_fixed_flow_chronology.py/json (solver-only UNSAT). The same encoder reconstructs literal standard104 from its full physical counts as a nonvacuous positive. No statement about other flows, arbitrary reorderings, or wider support is inferred.

A deterministic finite continuation from the disconnected schedule's H-end cut merely follows standard H in the exploratory control pipeline_cut_continuation.json. Its entry field contains a semi-infinite prepared past; no capture or finite-support theorem is asserted from the finite trace.

## 5. Remaining construction obligation

A genuine construction must connect the pieces with all its own read histories, or replace the whole-piece schedule by an explicitly continuous phase splice. Matching profiles, pose endpoints, aggregate circulation, or the positive disconnected history table alone is insufficient. Both present fixed-controller exclusions and the standard-producer funding bounds must keep this potentially nonstandard interleaved producer outside their scope.
