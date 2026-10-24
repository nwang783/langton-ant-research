# Next enlarged language: adjacent bad pairs spaced by at least140 turns

Status: exact exploratory computations, not yet independently audited; no new
finite-support exclusion theorem is claimed.

## Event convention and coverage

J(t) is bad10 ending at t and K(t)=J(t-1)J(t). A150-turn factor contains140
wholly visible K positions. Requiring at most one K in each such factor is
equivalent, on a two-sided stream, to distinct K events having distance>=140.

First enumerate the broader100-turn/spacing90 language. Its368709 exact
words give321392 histories and one cyclic SCC with115603 vertices/123133
internal edges. Any infinite physical path eventually stays there.

Then extend every one of its123133 recurrent100-words to150 turns, retaining
physical consistency, at most one K, and membership of every intervening
100-window in that recurrent subgraph. This complete enumeration visits
38384372 nodes and yields2199766 words. It is NOT the incomplete earlier
unrestricted150 enumeration, which hit its resource cap.

The resulting149-history graph has2084239 vertices and one cyclic SCC with
1471752 vertices and1555545 internal edges. Any infinite spacing140 physical
tail eventually follows this SCC. Removing the old marker M leaves one
937-vertex953-edge cyclic SCC, so the old marker alone is insufficient.

## Two-marker return language

The two equal-length markers are

    M = LLLLRLRRRRLR,
    N = RRRLLRLLRRRR.

Removing all40462 marker-history vertices from the recurrent graph is acyclic.
The longest nonmarker height is105; there are231452 actual marker returns,
with gaps at most106. Conjugating the common12-letter cut gives88 distinct
before-marker words. Thirteen contain no K and75 contain exactly one K, when
the target marker is included to detect boundary-crossing eleven-windows.
There are ten distinct eleven-letter adjacent-defect patterns among these.

The deterministic actual-port return graph minimizes to1682 forward-language
classes with9095 labelled quotient edges after7 strict refinements. This is
an exact finite necessary language, not a claim that every quotient path is
physically feasible at arbitrary lengths.

Files: enumerate_adjacent_pair_spacing.cpp; analyze_bounded_bad_graph.py;
extend_recurrent_spacing.cpp; recurrent_spaced_words150.txt and associated
logs; extract_spaced_two_marker_macros.py; spaced_two_marker_macros.json;
extract_spaced_two_marker_ports.py; spaced_two_marker_actual_ports.json;
spaced_two_marker_port_quotient.json.

## Open next target

Prove that every infinite finite-support physical path in this larger language
has only finitely many K, perhaps by charging the75 K-bearing macros to fresh
entry-black cells through a relational kernel. The old five-macro theorem does
not supply this: the larger language includes standard104 renewal cycles and
additional finite scattering excursions. A literal no-new-fuel search is in
progress to challenge that proposed charging target before attempting a large
certificate. Bounded search is evidence only, never a proof.
