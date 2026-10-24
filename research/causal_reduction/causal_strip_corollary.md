# A conditional global obstruction from causal bushes

## Status and dependency

This is a small new consequence of the exact token forest and the inherited complete-crossing-history theorem, not a new proof of that theorem and not highway capture. The relevant inherited proof is

`first_principles_2026-10-21/ant_rethink/constructive_alternatives/oblique_strip_pumping.md`.

That result proves: if a tail lies in a finite union of fixed-width non-axis strips, its trace is eventually nonzero translating periodic. It does not identify the standard word. Its crossing-history splice retains complete past histories, rather than substituting a first-frontier state.

## Theorem

Let an actual finite-seed ant's edge-token forest have finitely many infinite ends. Choose one root-to-infinity spine for each end, merging common prefixes. Suppose:

1. Each spine's cursor positions are eventually contained in a fixed-width strip with non-axis direction. The finitely many strips need not be parallel.
2. There is H such that every cursor node outside the union of those spines has ancestry distance at most H from its last spine ancestor. Entire finite root components can be excepted, since they contain only finitely many nodes.

Then the physical ant trace is eventually translating periodic.

In particular, the conclusion applies if there are finitely many eventually straight diagonal causal spines and uniformly bounded cursor-node bush depth. Eternal buds are not cursor positions and do not affect this hypothesis.

## Proof

Each parent-child step changes the Tait cursor by zero or one diagonal unit edge. Thus a node at ancestry distance at most H from a spine ancestor is at l_infinity distance at most H from that ancestor. The physical head is a corner of its cursor plaquette, at additional l_infinity distance at most one.

Except for finitely many early nodes, every node's last spine ancestor lies in one of the stated strips. To justify this qualification, there are only finitely many exceptional spine nodes; bounded depth and outdegree at most four give only finitely many descendants within distance H of them. Finite root components are also finite by local finiteness and König's lemma.

Therefore the actual tail is contained in the finite union of the original non-axis strips, each widened by a fixed amount accounting for H+1. The inherited strip theorem supplies a nonzero translating periodic tail. QED.

## Exact contraposition

A finite-seed orbit that is not eventually translating periodic must have at least one of:

- infinitely many infinite ancestry ends;
- a finite-end backbone with an end that is not eventually confined to any fixed-width non-axis strip;
- unbounded cursor-node depth in finite bushes off its finite-end backbone.

Here the last two bullets describe the finite-end case. The theorem does not exclude any of these alternatives. In particular, 'two straight spines' without control of all their finite side bushes is insufficient for this argument. Those bushes may carry the entire infinite sequence of bad events.

For the standard word the complete certificate establishes two straight spines and cursor-node bush depth six. Thus the desired solution fits a sharply bounded special case of the theorem. No bound of six, seven, or any other constant has been asserted for general inputs.

## A separate proof check on the crossing-history mechanism

For a fixed-width horizontal strip with a uniform visit bound, one can recover eventual translation directly. Every sufficiently far right half-strip initially starts white. View it as an interactive deterministic subsystem: each entry specifies boundary row and incoming heading; between an exit and the next entry its internal field is unchanged. A bound on complete cut-history length leaves finitely many input/output histories. Two equal histories give translated-equal right-half fields at their last entries. No subsequent exit occurs. Their future trajectories are therefore exact translates.

The existing source proves a stronger oblique-strip result, including the visit bound, and contains the complete splice proof. This paragraph is an independent way to understand the interface, not a new claim of priority.
