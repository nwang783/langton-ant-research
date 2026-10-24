# A25-obligation directional D/C/V confinement reduction

Status: CONDITIONAL, submitted for independent audit. The102-row transfer family used here is independently signed, but all25 remaining transfers are unproved. This is a new sufficient target list, not five newly excluded members of the older69-case list.

## Directional max potential

Let R_h be clockwise quarter-turn rotation, kappa=(-1,1), and L(x,y)=x+3y. The anchor `2p+R_h kappa` is just a convenient heading-dependent reference, not a claim about the geometric center of the five-cell black core. Use the exact signed residual ledger for recurrent packets D, DC, V, VC, VCC.

At a marked pose(p,h), give the core the value L(2p+R_h kappa)+c_h. A residual black token at q has value2L(q) plus its stored producer weight w_(A,slot,producer heading), or the initial weight I=max u for a token present at the chosen initial cut. A packet consuming input j at heading h requires a lower-bound weight u_(A,j,h). Let P be the maximum of the core and all residual token values.

For each packet A at heading h, the exact model verifies that its new core and each output value are bounded by the maximum of its old core value and its input lower-bound values. After subtracting L(R_h kappa), these are precisely the148 integer inequalities checked by `check_dcv_directional_confinement.py`. If every actual produced-token transfer satisfies u<=w, then P cannot increase. Unchanged residual tokens retain their old values. Initial tokens satisfy every input lower bound by the choice of I.

The integer witness is `dcv_free_direction_family102.json`, with direction(1,3). It was discovered allowing nonnegative integer direction components at most16, not assuming those bounds as a trajectory theorem. Exact arithmetic verification, independent of the optimization engine, is in `dcv_conditional_free_direction_family102.json`. All19 known finite transfer controls also satisfy the inequalities, but they are NOT used as a complete classification of physical transfers.

## Four rotations confine the board

For r=0,1,2,3 apply the same construction to the coordinate functional L_r(z)=L(R_r z), using offsets and token weights indexed by h+r. The148 inequalities include every global heading, so they apply to all four potentials. The sufficient transfer test likewise checks all four possible producer headings.

Each initial potential is a maximum over a finite initial residual set and one core value. All stored weights belong to a finite list. Thus upper bounds on the four potentials give upper bounds on L_r(p) for the head anchor and L_r(q) for every residual black cell. Opposite r give both signs. The two independent linear forms x+3y and -3x+y have determinant10, so their bounded strips intersect in a bounded region. The entire marked board lies in a finite box; bounded packet lengths also bound every intermediate read.

In this restricted language D changes total black mass by0, C by+3, and V by+4. A finite box cannot support infinitely many C or V macros. An eventual pure-D tail has nonzero displacement(1,1) per macro and cannot remain confined. Therefore, if the25 stated remaining transfer rows are impossible, no infinite finite-support D/C/V tail exists.

## Exact remaining list and signed premises

The original ordinary3873 and protected102122 clauses are signed. The additional102-row family `dcv_companion_closed_family.tsv` has SHA2568da1a5e5fc5c1162c1938890c836602ffd7ea4fa8d91831d0510425bcc16368e and audit `../audits/mutual_source_flag_family_independent.json`.

After excluding those signed rows, exactly25 transfer tuples violate the new weight inequalities. They are frozen in `dcv_directional25_targets.tsv` and in the exact-check JSON. Relative to the previous30 sufficient targets, old indices7,12,14,21,28,33,40,62 are no longer required. Three new tuples are required:

- (0,4,4,-1,3,2,0)
- (1,4,5,0,3,3,1)
- (4,4,4,1,3,2,2)

The remaining22 are the exact older indices1,2,3,4,5,15,16,17,18,19,20,22,23,24,31,35,36,39,41,42,43,44. No claim that any newly omitted row is physically possible is made. The older69-case signed ledger remains39 excluded and30 open; the two conditional routes have different potentials and different sufficient hypotheses.

The earlier counted result directly applies only to the22 shared old targets. No four-C minimum is silently asserted for the three newly introduced tuples without a separate query.
