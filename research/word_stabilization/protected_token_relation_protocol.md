# Protected residual-token relations

Status: the induction protocol has received a preliminary analytic review. The new generated closures are not independently replayed and do not prove D/C/V exclusion.

Fix the literal seven packets D, DC, DCC, DCCC, V, VC, VCC with actual M11 right markers. Define a protected pair by packet types A,B, their relative pose, and a physical cell q. Its premise is that q is black immediately after RAW A, and no strict intermediate packet's RAW plus its actual M11 marker reads q. The outer source and target are not subject to this avoidance condition. The target's first read, if it has one in its actual context, must consequently be L.

The finite candidate universe uses overlapping source-RAW/target-context pairs, and q in the union of those two footprints. Missing candidate types are not inferred forbidden. A previously justified ordinary forbidden-pair relation may always be used without the protected premise.

Base controls remove every physically feasible adjacent pair with q black at the seam, and every feasible gap-two triple whose middle packet's complete context avoids q. A source RAW last L or target-context first R contradicts the black-cell premise directly.

For gap at least three, let C and D be the actual successor of A and predecessor of B. Their contexts must avoid q. Every proper subpair inherits the protected premise: a shifted subsource is an intermediate packet, which neither reads nor changes q, so q remains black after it. All cells and relative poses are normalized into that subsource's frame. If q falls outside a chosen finite candidate universe, only an ordinary relation may discharge that subpair.

An equal-read barrier uses the first odd-multiplicity intervening reader, whose first and last letters are opposite the equal source/target letter. That reader must also avoid q. Two-cell transition rules similarly retain only readers whose complete context avoids q, and omit a reader only when an ordinary or protected strict subpair excludes it. The four-state color path remains an overapproximation of every physical intervening sequence.

Minimum actual packet-index gap justifies same-family cyclic dependencies. Right-marker overlaps are part of the premise and remain present in every proper subpair; they must not be silently replaced by RAW-only avoidance.

## Residual-token application

The audited residual-core model has disjoint input and output sets. A surviving residual black cell cannot silently enter the moving five-cell core: that is precisely an input consumption. At a packet boundary, a surviving residual cell is outside both cores. If its full packet context read it, its first read would require black and would put it in the input set. Therefore every strict intermediate packet between its producer and consumer avoids it in the full context, not just in RAW.

The query at a source output and a target input thus has the protected premise. Initial residual tokens need no producer relation and receive a uniform finite initial weight in any resource potential.

## Current finite experiments

- `generic_protected_token_kernel.cpp`: neighbor and odd-reader rules.
- `generic_protected_patch2_kernel.cpp`: adds exact two-cell transitions.
- `dcv_protected_patch2_kernel.tsv`: 102,122 stable protected clauses after 14 pruning rounds, based on the existing ordinary relation. No independent implementation audit yet.
- The proposed same-heading upper/right C-deposit transfers into D remain unexcluded.
- Of 324 directed resource-transfer poses admitted by the ordinary relation, the protected two-cell closure excludes 103 and leaves 221. This does not establish the much smaller observed transfer alphabet.
