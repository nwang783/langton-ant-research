# Linear fuel in the seven-word RRRLRRRRLRR component

Status: standalone spatial certificate, linear bound, global150-window bridge and old-H inclusion all independently audited. No full-highway claim.

## Literal language and finite-factor quantifiers

Use the seven literal raw words, actual endpoint markers, and52-state quotient in mono_rrrlrrrrlrr_port_quotient.json. Types1,3,4,5,6 are the previously defined C,V,U,Q,B. The new types are2 = LLLLRLRRRRLRLLLL, from M=LLLLRLRRRRLR to P=RRRRLRRRRLRR, and0 = RRRRLRRRRLRRRR, from P to M. Every2 has successor0 and every noninitial0 has predecessor2. In fact0's successor is V3.

Consider a finite raw-block factor of an actual path in this quotient, with at least one actual full successor block and its required marker supplied as right context after the final counted block. All source and intermediate reads belong only to their own raw blocks. Each target includes its raw block, its actual successor raw block, and that successor's required marker. The factor entry has m black cells on the complete board.

Necessary short grammar has19 pairs and59 triples. The context objects(A,B) form19 types,59 edges and174 literal-feasible short triples. The exact lists and literal words are frozen in mono_rrrlrrrrlrr_context2_{port_quotient,grammar}.json.

## Spatial certificate

The same asymmetric least-index-gap method as monochromatic_k_pattern_capture.md gives81,846 candidate overlaps,75 physically feasible short types, and76,768 stable forbidden pairs after8 pruning rounds. It uses neither an assumed freshness family nor a finite spatial cutoff: every intermediate-reader pose is enumerated from literal read incidences. Proper subpairs inherit the actual successor context.

The certificate queries show the following marked cells are unread in every earlier raw block of the factor, and are first read L inside the owning raw block:
- context(1,1):(-1,0), phase1;
- any context owning2:(-1,0), phase1;
- any context owning3:(1,2), phase13;
- any context owning4:(0,3), phase23;
- any context owning5 or6:(-3,1), phase18.

Every chosen marker is inside RAW, not the right context. Thus markers from different charged blocks are pairwise distinct and were black at factor entry. If c11 counts C blocks whose immediate successor is C,

    c11+n2+n3+n4+n5+n6 <= m.

All uncharged blocks are type0 or type1 not followed by1. The pair grammar forces0→3 and1→3 in those cases, so two uncharged counted blocks cannot be consecutive. If n is the number of counted raw blocks,

    n <= 2m+1.

Every charged raw word has length at most74, and every uncharged one has length at most15. Therefore the counted raw turn length is at most

    89m+15.

No infinite finite-support path in this seven-word quotient exists. In particular the five original H words, with this actual quotient's inherited restrictions, have this linear fuel bound. This is NOT claimed for arbitrary physically feasible finite concatenations of the five raw words without the inherited language and actual right context.

## Audited global bridge

The complete p=RRRLRRRRLRR150-window graph has364858 words and326637 histories. Its cyclic components are W104,T24 and the enlarged H42002-vertex/43912-edge component. That component has1402 marker ports, maximum nonport height73,3657 returns of gap at most74, and the seven-word52-state quotient above. Discovery files are mono_rrrlrrrrlrr_words150.txt, its graph JSON, mono_rrrlrrrrlrr_bad_component.txt, and mono_rrrlrrrrlrr_{macros,actual_ports,port_quotient}.json. Independent reconstruction binds all of these objects. The linear fuel exclusion and old T24 exclusion leave only standard W, proving the separate sole-label capture theorem.

The auditor explicitly checked inclusion of all34,712 old H vertices and36,277 internal edges in the enlarged H component. Thus its actual paths inherit the linear bound and right-context restrictions. For a finite H visit, allow100 turns at the leading cut and200 at the trailing cut: the latter may lose73 nonport turns, one74-turn successor and12 marker turns. This is why the strengthened H envelope is300+89(x+100)+15, not the earlier200-based envelope.
