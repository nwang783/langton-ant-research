# Horizontal full-drift frontier geometry for finite clock zones

23 October 2026, 03:33 UTC. Full drift (2,0) through cap EIGHT is independently signed.
The common clock-zone framework is independently signed. This note states
exactly the additional geometry used by the new axis producer.

Let the full displacement be d=(a,0), with a positive even integer. Row y
has representatives (i,y), 0<=i<a. Fix the checker sector with vertical
outgoing edges at i+y even and horizontal outgoing edges at i+y odd.
Every local complete white history starts R and alternates R,L. At an
even vertex its incoming headings are E/W; at an odd vertex they are N/S.
The other checker sector is obtained by translating the integer origin.

Inside each row, an odd vertex's E edge ends at column i+1 modulo a with
seam voltage floor((i+1)/a). Its W edge ends at column i-1 modulo a with
voltage floor((i-1)/a). All these horizontal edges are included as soon
as the row is exposed. Their chronological kth departure and arrival are
matched exactly; row histories with unequal counts are discarded.

Between old row y and new row y+1 there is one directed vertical edge at
each column. If i+y is even it is the old vertex's N edge to the new one;
if i+y is odd it is the new vertex's S edge to the old one. Its seam
voltage is zero. Both histories' directed traversal counts must agree,
and kth occurrences are matched. There is no intra-row vertical edge.

Compress the already exposed partial event graph into unfinished directed
paths with endpoints on row y. Appending row y+1 resolves every old missing
port, creates every new-row horizontal arc and every intervening vertical
arc, and leaves only the new row's upward ports unresolved. Thus the exact
same path-block, sole-cycle, phase-cut and finite clock-zone proof applies.
Event IDs are (column, local rank), with lexicographic canonical anchors.
No new assumption about event periods or transverse width is introduced.

For a=2 and cap eight, the independent reconstruction starts from all
522,242 unpruned row assignments and retains 35,154 internally compatible
rows. With weakening bound two and voltage modulus two, the complete zone
graph has 17,736 reachable states and 17,736 accepted edges, with no
potential whole-front outcome. It checks 1,234,166 outgoing extensions and
491,048 independent Bellman-Ford closures. Cap seven also passes with
2,688 states and edges. Thus every complete white-input front with actual
full drift (2,0), or a quarter rotation, has some physical cell visited at
least NINE times, at every width and period. This is not an all-cap axis
exclusion, and does not classify other full horizontal displacements.

Producer: `probe_axis_zone.py` and `probe_axis_zone_core.py`.
Frozen certificate: `axis_d2_0_zone_cap8_bound2_mod2.certificate.json`.
SHA256: ab6513181ca4e3ed0b8a07458f96946e5051d789af589a658f4f357a13e8c1bf.
Independent reconstruction: `../audits/check_axis_general_zones_independent.py`
and `../audits/axis_d2_0_zone_cap8_bound2_mod2_independent.json`.
Ledger IC records the mathematical and complete-graph signoff. The separate
full drift (4,0), cap-four author certificate remains pending independent
replay and is not included in this signed conclusion.
