# Stronger chronological rules for least-gap spatial certificates

Status: the inference arguments below were independently reviewed by the audit analysis on 2026-10-22. New engines are exploratory implementations, not independently replayed theorem certificates. The existing signed certificates and their engines were not modified.

## Scope and common induction

A pair type specifies an earlier owned RAW macro A and a later macro B at an exact relative pose. B's target footprint may include its actual right context. Every source-to-target interval is indexed by the actual owned macros, not by overlapping context objects. All smaller-gap uses must refer to this same family and inherited right-context scope. Physically feasible gaps one and two are removed before closing any rule. A proposed family is sound if every remaining type has a rule whose hypothetical realization implies a strictly smaller-gap realization in the same family. A minimum-gap counterexample then proves the family empty of realizations.

Every reader below is an exact translated/rotated RAW macro pose. Enumerating poses from each literal read offset of a marked cell is exhaustive without any spatial cutoff. A reader can be removed only if its source-to-reader or reader-to-target strict subpair belongs to the proposed forbidden family. Macros missing the marked cells entirely may be ignored when they act as identity on the retained colors.

## Odd-reader rule

Suppose the source's LAST read of q and the target context's FIRST read of q both have letter c. After the source, q has color opposite(c), while before the target it must have color c. Thus the number of intervening reads of q is odd. Choose the first intervening RAW macro whose q multiplicity is odd. Every earlier intervening macro has even multiplicity and restores q's color. Literal within-macro alternation therefore gives FIRST(q)=LAST(q)=opposite(c) for that selected macro.

Consequently it suffices to block all exact RAW reader poses with odd q multiplicity and FIRST(q)=LAST(q)=opposite(c). Even-multiplicity readers and odd readers with the other input color need not be blocked. This strictly strengthens the older rule that blocked every touching pose.

## Two-cell transition rule

Choose distinct cells q1 and q2 with defined source RAW LAST and target-context FIRST reads. The source fixes the two post-bits to opposite(LAST), and the target fixes the required pre-bits to FIRST. These target pre-bits are valid even when the two first reads occur at different positions in the actual right context: before each first read the target prefix has not changed that cell.

For every exact intervening RAW macro pose touching either cell, record its partial color transition. On a touched cell, the input must equal RAW FIRST and the output is opposite(RAW LAST). An untouched bit is preserved. Delete a pose only by one of the strict forbidden subpairs above. Allow all remaining transitions in arbitrary order, including spatial teleports and repeated poses. This four-state graph is an overapproximation of every actual intervening macro sequence. If the required target bit pair is unreachable from the source post-bit pair, the outer pair is impossible.

The same reasoning works for any finite set of cells, with 2^k color states. A three-cell exploratory implementation currently tests triples of diameter at most two. That restriction merely omits possible certificates; it does not change soundness of any certificate found.

## Implementations and negative outcomes

- generic_odd_reader_spatial_kernel.cpp
- generic_patch2_spatial_kernel.cpp
- generic_patch3_spatial_kernel.cpp

For the seven-word D/C/V/U/F/Q/B language, both the raw seven-type abstraction and the 32 two-word-context abstraction still have empty stable forbidden kernels under these rules. The three-cell tests also end empty. This is failure of these abstractions, not a physical counterexample and not evidence that the language admits an infinite finite-support trajectory.

The 14 maximal-C-run packet abstraction is also empty under the two-cell rule. Its 75 two-packet-context refinement is being tested separately. No claim is made from an unfinished closure.
