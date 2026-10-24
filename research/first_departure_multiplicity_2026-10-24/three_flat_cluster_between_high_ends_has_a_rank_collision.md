# Three-flat cluster between high ends has a rank collision

24 October 2026. Complete WHITE cap-four front, actual FULL P,d.
The boundary is critical GLOBAL-M with no one-use edge. Author finite
composition result pending review. This is an EXACT THREE-FLAT cluster,
not a bound on arbitrary flat-cluster length or a general front theorem.

Take a maximal cluster of exactly three consecutive flat RIGHT contacts
in the nearest-RIGHT order, with high macros on both outside ends. The
signed root-island and mixed-LL results force one outside V at each end,
with a high3/high4 sink before the first and source after the last.
This is the same physical end interface as the signed two-flat gate.

Write g0,g1 for the numbers of LEFT contacts in the two internal gaps.
Each lies in {0,1,2}; (0,0) would give RRR and close a physical square.
Use ALL flat choices X/Y, while retaining precisely the following signed
necessary local rules, not additional guessed constraints:

- At a two-LEFT gap the second is V; its preceding flat is Y; its next
  flat is X for first O/U and Y for first V (signed LL table).
- At a zero-LEFT RR gap, its neighboring LEFT endpoints are V (general
  signed RR closure).
- A one-LEFT gap touching RR is V by that same closure. Otherwise it is
  a singleton O, preceded by Y and flanked by immediate V contacts, by
  the signed GLOBAL-M critical local-island theorem c9574fb8. This
  retains odd O and the LL-first even U; it does not discard old L3s.

These complete finite primary rules give 120 physical stencils after the
four independent high3/high4 endpoint choices. Draw every actual edge,
then add only the count-forced corner closure and all complete 0..4-read
WHITE histories at those corners. Keep all zero ports and physical
ordinal matchings, exactly as in the signed earlier local covers.

The independent-gap breakdown of the author exhaustive result is

    gaps01: 32 primaries, 18,432 literal rank collisions;
    gaps02:  8 primaries,    128 literal rank collisions;
    gaps10: 32 primaries, 18,432 literal rank collisions;
    gaps12:  4 primaries, no count-compatible corner completion;
    gaps20: 24 primaries,    352 literal rank collisions;
    gaps21:  8 primaries, no count-compatible corner completion;
    gaps22: 12 primaries, no count-compatible corner completion.

The (1,1) primary word is already excluded by its signed local rules:
its two singleton O gaps would each require the other to be V. Thus
there is no omitted primary mode. In total, 24 primaries have no count
completion and all 37,344 completed patches have a physical next-rank
collision. No additional clock, height or critical-side filtering is
needed after these finite primary rules.

This excludes that finite end-to-end cluster only. Longer flat strips
are NOT automatically excluded: the separate arbitrary-length
RR(LLRR)* necessary control has exact open internal readers and injective
rank chronology. Nor can this three-flat result simply be applied to a
three-flat subwindow whose outside RIGHTs are OTHER FLATS rather than
the specified high endpoints. That missing substitution would be an
invalid induction. The all-length endpoint/curvature problem remains.

Files: check_three_flat_cluster_between_high_ends.py/json. No period,
drift, front-support or arbitrary-radius scan was performed.
