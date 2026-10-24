# Ordered last exits, and an actual empty-seed circulation component

24 October 2026. Author proof and literal full-field control; independent audit pending. This is a chronological follow-up to the signed summable-flow relaxation, not another stationary balance assertion.

## 1. Exact ordered constraint missing from a flow table

Let Q be any finite set of cells. Take one actual finite ant interval whose final head is outside Q. For every Q cell read in the interval, record its LAST read time ell(v) and its outgoing neighbor z(v) at that read. Whenever z(v) belongs to Q, it is actually read at the next update before the ant can finally finish outside Q. Therefore

    ell(z(v)) > ell(v).

The internal last-exit arrows form a directed acyclic forest. Every component ends at a read whose outgoing edge exits Q. This is the familiar finite-walk last-exit ordering, now coupled to ant colors. It is not an assumed global lifetime stack.

If the Q colors are the SAME at both endpoint cuts, each visited Q cell has been read a positive even number of times. Consequently its last turn is L if it was WHITE at the initial cut, and R if it was BLACK. These are actual chronological last turns, not merely equal marginal R/L counts.

For a unit-square patch whose directed internal cycle consists of L turns, consider a restored-color packet in which NO L turn takes the external-corner route. Every L read then continues inside Q. Each last-exit root must therefore be an R read, and hence must be a cell that was BLACK at the initial cut. In particular:

    A nonempty such packet requires at least one current BLACK input in Q.

More precisely, each last-exit-tree component has a distinct initially BLACK root. This is a fixed-cut current-input requirement. The bits may have been written earlier by the ant; it is not an initial-seed-mass charge.

If all Q cells were initially WHITE, the final Q read would have to be L while its outgoing edge remains in Q, contradicting that it is the final Q read. Equivalently the internal last-exit times would force a directed temporal cycle. This proves the exclusion without any simulation.

The opposite orientation exchanges R/L and colors. It is important to retain the actual sector rather than reflecting a physical route without changing the rule.

## 2. The one-BLACK requirement is sharp in a literal empty-seed orbit

Start the classical ant with EMPTY black field, head(0,0), heading E. Let

    Q = {(9,4),(10,4),(10,5),(9,5)}.

At cut5710, only(10,5) is BLACK in Q. Its actual lifetime was born R5693, at that cell's first-ever read. The ant is at(9,5), heading E. The following complete Q passages occur:

- updates5710,5711: RR, entering at(9,5), then(9,4), exiting to(8,4), heading W;
- updates5712 through6035:324 actual reads, ALL outside Q;
- updates6036 through6041: RLLLLR, entering at(10,4), then following(10,5),(9,5),(9,4),(10,4),(10,5), exiting to(11,5), heading E.

At cut6042, the Q black set is AGAIN exactly{(10,5)}. Each of its four cells has had exactly one R and one L during this332-update interval. Every L turn is on the internal four-cell directed cycle; no external-corner L occurred.

The actual last-exit chain is

    (9,5) at6038 -> (9,4) at6039 -> (10,4) at6040
                 -> (10,5) at6041 -> outside Q.

The first three last turns are L. The last is R at the unique initially BLACK root, exactly as Section1 requires.

All four cells had WHITE first-ever arrivals: times1595,1596,5693,5710 respectively for(9,4),(10,4),(10,5),(9,5). Thus virgin first-arrival color alone does NOT exclude this locally balanced circulation after causal preparation. Indeed one cell is being visited for the very first time at the packet's entry cut.

## 3. True lifetime replacement, not a closed full state

The original current Q input is R5693 at(10,5), consumed at6037 with age344. The final R at6041 creates a DIFFERENT lifetime at that same cell; that replacement is consumed later at6313. The input bit has been replaced, not resurrected. Thus the sharp fixed-cut input obligation does not produce a decreasing seed resource.

The complete outside field matters:

- whole black mass is420 at5710 and440 at6042;
- the complete fields differ at92 cells;
- the324 outside reads contain172 R and152 L;
- the entire future-relevant current populations are296 and310 at those two cuts;
- the actual cursor changes from(9,5),E to(11,5),E.

Every field is retained in the certificate. There is no repeated full state, no autonomous local controller, and no claim that the exterior can be reset for free. The full empty-seed continuation has its exact canonical104 certificate at9977, with715 current BLACK cells and drift(-2,2). The first9977 reads and all infinite ray-parity tests are included.

## 4. Relation to the summable radial flow witness

For the central unit-square cell patch of the radial r=1/2 flow, scaling the unnormalized flow by16 assigns at EACH cell:

    internal L:15;
    external-corner L:3;
    each of the two crossing R routes:9.

The literal packet above supplies one internal L and one crossing R at each cell, with no external L. Its routing counts are therefore a nonnegative finite component of that local flow inventory. It does NOT realize the complete15/3/9/9 table, its infinite surrounding flow, or a stationary limit. The remaining external L turns in the full witness could be placed last and remove the particular all-WHITE last-exit obstruction, so this component exclusion must not be promoted to exclusion of the full witness.

The exact16-color-state/four-entry-port patch automaton confirms the local cycle: in cyclic vertex order(0,0),(1,0),(1,1),(0,1), one-BLACK mask4 enters at vertex3 and undergoes RR to mask13; entry at vertex1 then undergoes RLLLLR back to mask4. This automaton alone is only an arbitrary-port model. The separate empty-seed replay supplies the actual external route and finite causal reachability.

## 5. What this adds to recurrent-drought research

The genuine new interface is the ordered last-exit forest, together with a sharp BLACK-root condition for this circulation packet. A static flow inventory omits it. The actual control shows why replacing that condition by a charge to original BLACK seed cells fails: the required root can be self-written, and the balanced packet produces a replacement at the same location while its full exterior grows.

What remains unproved is whether the full radial flow, or suitably many compatible local circulation packets, can occur on arbitrarily large boxes from a uniformly bounded finite seed. No such family is constructed here. Nor is a finite capturing control being used to assert infinite recurrence, unbounded late ages, or failure of compact returns in one orbit.
