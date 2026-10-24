# Drought hierarchy: current exact outcome

24 October 2026. Finite-seed standard104 attraction remains UNSOLVED.

## Useful result first

The strongest new ant-specific statement is a constructive visit-flow hierarchy. Every actual interval whose entire head trace stays in a W-by-H rectangle satisfies

    duration+1 <= S(W,H)+3A(W-1,H-1)
                <= (WH+3)(4^(W+H-1)-1)/3.

Here A and S are the exact positive Green-function sums in `RECTANGLE_VISIT_FLOW_ESCAPE_BOUND.md`. The sharper endpoint-dependent bound is also retained. It is derived directly from the fixed directed sector and alternating reads, includes thin rectangles and arbitrary endpoint headings, and does not assume the no-bounded-orbit theorem. It implies a logarithmic lower bound on ordinary head-record count. It does NOT supply fast pristine-record windows.

Manifest ae95dcdef257f2fff6768449011ed58d3bc127cc10602907652d7bfc6be9db8f is independently PASS in audit62bcf41f75f008eaf74c68ef1c0cd70a2337ce51d1c0204fab663ec23ae12b8b. Binding63ba7e511ef80bc3544f8c230c84c6eca2b9aadcbc2723877bcc8e8a3d0c4f3c.

## Other signed pieces from this assignment

1. Finite boundary current: a confined interval with strict-interior endpoints has at most B(W,H)=2W²+2H²+2W+2H−12 boundary reads. The finite side exclusion moment plus at-most-once corner reads give a genuine nested sequence of HEAD-region subintervals. General endpoints cost at most six trimmed updates. Manifestf0d24e49 requires orientation clarification9a2524e9; independent audit02f628cb. This is not lifetime nesting or BLACK-hull descent.

2. Actual all-n pinning: for every n>=100, an original22-cell MT seed has an interval of length47837+104n after all original lifetimes retire, with entire current BLACK hull exactly[0,2n+250]×[0,2n+262], no boundary reads, and three genuine permanent R lifetimes pinning all four sides. Whole relevant mass at entry is807. Thus arbitrarily many reset windows can lie within one unchanged hull, despite complete original-input retirement. Same signed package.

3. Completed-drought scope: all those MT members have exactly ONE completed pristine union-record gap above3390, of length58697+104n. Initial waiting and arbitrarily many reset subwindows are not distinct completed gaps. Manifestccf51906 independently PASS07204abd; bindinge7526825.

## A separate explicit relaxation obstruction, audit pending at this snapshot

`SUMMABLE_BALANCED_TURN_FLOW_OBSTRUCTION.md`, manifest28a356641c60aa440e20db3389928b556723eeaf77b5d5c525c6dbe65454d391, gives an infinite stationary flow, NOT AN ANT ORBIT. Face weights A(i,j)=r^(|i|+|j|), edge flow A_left+A_right, and corner turn flow(3A_self+A_adj1+A_adj2−A_opposite)/4 are nonnegative for1/3<=r<1. They conserve every edge, have exactly equal R/L flow at every site, and have finite total4((1+r)/(1-r))². At r=1/2 the normalized origin occupation is1/16.

This shows why the stationary one-site frequency relaxation of the visit-count hierarchy cannot alone prove zero local occupation or transience. The actual globally compatible chronology and finite-seed reachability remain unrepresented. Do not promote it to a recurrent ant or finite-seed counterexample. Add a separate audit binding after signoff; preserve this timestamped pending status.

## What remains live

The signed finite record-clock forcing theorem says a nontranslator must have uniformly recurring long simultaneous pristine record droughts, at every chosen drought scale. The new hierarchy imposes a quantitative spatial cost on each confined episode. It does not prevent its rectangles from growing or restarting at new places. The pinning control forbids equating interior head motion with a shrinking complete BLACK hull. The MT inventory forbids claiming that one long paid return already gives unboundedly many separate completed droughts.

No fixed-cardinality finite-seed family with arbitrarily many distinct completed large pristine droughts has been constructed here. No single finite orbit with unbounded late droughts, no universal compact-return occurrence, and no unrestricted translating-controller uniqueness is proved.

All code and full fields are local in this research directory. Frozen source packages are unchanged; corrections and audit bindings are separate. There is no running author process at this snapshot.
