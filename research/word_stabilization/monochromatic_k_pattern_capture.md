# Capture with one eventual adjacent-defect pattern

Status: both the standalone eleven-word successor-context theorem and its complete upstream150-window bridge are independently audited. The global corollary below is signed end-to-end. The full highway conjecture remains open.

## Global statement

Let W be the standard104-turn word, with its84 cyclic ten-letter factors. Let J(t) say that the ten-turn word ending at t is outside those factors, and let K(t)=J(t-1)J(t). Consider any Langton-ant orbit starting from a finite black set. If, from some time onward, every K event has the same eleven-letter word

    p = RRRLLRLLRLR,

then the turn stream is eventually a cyclic phase of W. No lower bound on the distance between K events is assumed.

## Exact finite-language bridge

A complete current-read-consistency enumeration of150-letter words, allowing a K event only when its eleven-letter word equals p, visits17,560,058 nodes and returns863,913 words. Their149-history graph has766,480 vertices. Its only cyclic strongly connected components are:

- the known H component,34,712 vertices and36,277 edges, whose five-macro finite-support exclusion is already independently audited;
- a new component,23,759 vertices and24,691 edges.

The latter has a feedback set of1,082 histories ending in one of the equal-length markers

    M = LLLLRLRRRRLR,
    N = RRRLLRLLRRRR,
    P = RRRRLLRLLRLR.

The extra possible marker L+p never occurs at these ports. The maximum nonport distance is44; there are2,510 marker returns, with gaps at most45. Shifting both cuts back twelve letters gives eleven raw words. Their exact forward-language quotient has six states and twelve labelled edges. Literal words, endpoint markers, actual port histories and all quotient edges are stored in single_k_rrrllrllrlr_{macros,actual_ports,port_quotient}.json. The original150-word list and enumeration log are retained.

The independent bridge checker regenerates all17,560,058 current-color DFS nodes and863,913 words byte-exactly, contracts the old H set and the new component and checks the full resulting DAG, and independently extracts every marker return and the six-state quotient. It also binds the old H internal edge set exactly.

## Standalone eleven-word language

Use the eleven literal raw words and six-state graph in single_k_rrrllrllrlr_port_quotient.json. Every raw block is followed by its stated actual marker. In the finite-factor theorem, each target block also has its actual next complete raw block and that next block's marker as right context.

The charged base labels and sites are:

- 0,1,6: local cell(2,-3), first read L at raw phase7;
- 2,5,9: local cell(-1,-3), first read L at raw phase10.

The certificate consequence is that each such cell is unread in every earlier raw block of the factor. Therefore, for entry black mass m,

    n0+n1+n2+n5+n6+n9 <= m.

All charged reads lie in their own RAW block, not in the appended context. Their pairwise distinctness and initial-black charge therefore require no lookahead-overlap multiplicity argument.

After the last charged block, labels4 and7 cannot persist, because their successors are charged. The only remaining recurrent cycle is

    3 -> 10 -> 8 -> 3.

Its literal length is104 and its word is a cyclic rotation of W. This gives standalone capture for every finite-support infinite path in this literal six-state language. The separate audited exclusion handles H in the global bridge.

## Why one complete successor matters

The eleven-word raw/marker-only relational kernel collapses to empty, as does the attempted two-relation first-reuse family. This is a failure of those certificates, not a counterexample.

Instead use22 overlapping context objects(A,B), for every physically feasible adjacent base pair. An object reads only RAW A and has RAW A's endpoint, but its target footprint is FIRST(A+B+marker(B)). Its next context is(B,C). The43 context edges and85 literal-feasible short triples are retained. These are ordinary necessary language restrictions, not hypothetical freshness assumptions.

The asymmetric source/target convention is essential. Source LAST and every intermediate reader use only RAW A. The target FIRST includes its complete A, actual complete B, and B's required marker. Thus an equal-read barrier inside future context includes all intervening reads of the target suffix. Every proper subpair inherits actual right context. Macro index, not extended word length, supplies strict descent.

## Finite spatial certificate

The generic spatial-pair checker enumerates93,695 overlapping relative context pairs over all four headings and the necessary parity x+y=heading(mod2). Ninety overlap types occur in a literal-feasible index-gap1 or2 factor and are removed. The stable forbidden family contains89,502 pairs, each carrying either:

1. a successor/predecessor clause, for which every compatible pair of neighbors contains a strictly shorter forbidden subpair; or
2. an equal-last/first-read clause, for which every possible intermediate RAW reader contains a strictly shorter forbidden subpair.

No circular freshness premise is used. The usual least-index-gap argument proves the whole stable family simultaneously. Querying all earlier-read alignments proves the six stated raw marker charges, for every compatible successor context.

Artifacts: generic_spatial_kernel.cpp; prepare_marker_quotient_kernel.py; build_marker_context_quotient.py; single_k_rrrllrllrlr_context2_{port_quotient,grammar}.json; single_k_rrrllrllrlr_context2_kernel.{input,tsv,fresh.tsv,summary.json,log}.

## Scope limitations

This addresses only the specified eventual K label. It does not prove that arbitrary orbits eventually have one K label, that K is universally finite, or that the full highway conjecture holds. The larger88-word spaced-K graph and its complete coverage are separate exploratory artifacts. A long finite standard-wake consumer is not excluded merely by a factor-entry fuel bound, since its entry mass may have grown during a preceding standard flight.

## Independent context audit

`../audits/check_monochromatic_context_independent.py/json` reconstructs all literal geometry and six-state paths without importing discovery helpers. It verifies93,695 candidates,90 short types,89,502 clauses (80,667 neighbor and8,835 equal-read),302,814 neighbor options,6,202,170 arbitrary reader options, and8,424 charged-site alignments. All twelve charged context types have their marker inside RAW A. This signs the standalone theorem. The separate ../audits/check_monochromatic_graph_independent.py/json signs the entire upstream150-window coverage, actual ports, returns, and quotient. Together these prove the global statement.

## Exact filtered-event equivalence

For finite initial black support, standard104 capture is equivalent to there being only finitely many K events whose eleven-letter label differs from p. The forward direction is immediate because standard tails have no J. For the reverse direction, after the last differently labelled K, the proved sole-label theorem applies. This does not imply finiteness of those filtered events for every seed.
