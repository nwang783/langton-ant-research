# An exact full-board collision/emission operator with geometric lifetime genealogy

24 October2026. AUTHOR analytic construction and executable exact operator; independent review requested. The empty-reference coupling already appears in the retained one-black proof, Sections1--2, and underlies earlier blank-parent first-contact arguments. No priority claim is made. The extension here is a CLOSED full-board XOR-segment implementation and explicit lifetime/ordering obligation. This representation does not prove capture.

## 1. The total next-collision map

At ANY finite full board B and physical pose(p,h), compare the actual ant with the certified empty-board ant from the same pose. The next visit to ANY member of B is the first old-cohort contact. Before it every read, turn and flip is identical to the empty reference. This includes arbitrary self-generated revisits; B is not replaced by an active component.

The empty reference consists of a fixed9977-move prefix and a104-period tail. In normalized initial heading N, its complete tail-entry black field E has715 cells, its tail drift is d=(-2,-2), and its periodic read positions are q_i. For a supplied cell x, its first empty-reference visit is the minimum of:

1. its occurrences in the finite9977 prefix;
2. times9977+104k+i with x=q_i+k d and integer k>=0.

Translation and proper rotation handle arbitrary poses. Thus the first contact with an explicit finite B is decidable without searching an unknown time horizon. If there is no contact, the actual full future is the empty reference forever, with B literally unread, so standard capture is certified.

Suppose the first contact is x at elapsed t. Let E_t be the COMPLETE empty-reference black field immediately before that read. Since no old cell was read earlier, E_t is disjoint from B, and x is absent from E_t. The actual turn at x is L instead of the empty reference’s first-visit R. Therefore the exact successor is

    B_next = (B minus{x}) union E_t,
    h_next = h_incoming_at_x -1 mod4,
    p_next = x + unit(h_next).

All old cells other than x remain, and ALL newly emitted black cells remain. The elapsed macro time is t+1. No reflection, reversal of the physical rule, component cropping, or erased historical residue is involved.

## 2. Closed compact exact fields, not expanded long flights

Represent a finite board as an XOR of finitely many finite arithmetic segments

    { b+j v : 0<=j<L },

where v is one of(2,2),(2,-2),(-2,2),(-2,-2), or v=0 with L=1. L is an arbitrary positive integer. Every finite input is included by using point terms. All overlaps are interpreted by PARITY, not set union.

For t=9977+104k+r, the full emission has the exact form

    E_t = E XOR XOR_(0<=j<k)(M+j d) XOR(P_r+k d),

where M is the32-cell odd-read mask of one104 block and P_r the prefix-r odd mask. Thus one emission requires715 fixed point terms, at most32 long segment terms, and at most104 additional point terms, irrespective of k. Short t uses its exact finite prefix mask. Actual rotations preserve the four permitted diagonal segment directions. Toggling x and adjoining E_t therefore leaves this representation CLOSED under the operator.

To find the first black cell on a future read ray q+k d, intersect each existing XOR segment with it:

- parallel or antiparallel segments give an integer interval of k;
- the other diagonal direction gives at most one integer pair(k,j), by an exact2x2 determinant;
- a point term gives at most one k.

Clip to k>=0 and the segment’s finite domain. XOR all interval indicators by toggling their endpoints. The first odd-parity interval starts at the first black ray cell. This is a finite integer endpoint sweep, not a scan over geometric distance. Together with the1376 distinct finite-prefix first reads and104 tail rays, it gives a total operator on the CLOSED representation itself, not just on materialized boards.

The proof of soundness is exact first-difference induction plus these complete integer intersection cases. Random finite controls are implementation checks, not the all-input proof.

## 3. Genuine lifetime genealogy and the necessary geometric ordering

At a nonterminal macro entry a_j, its selected parent token is a black lifetime already present. It is consumed at c_j=a_j+t_j. Every cell of E_(t_j) is a new current black lifetime born at its LAST R in that blank prefix; the checker can retrieve that birth exactly. Assign each emitted lifetime as a child of this consumed parent token.

The parent was born before a_j. A child is born b' with

    birth(parent) < a_j <= b' < c_j.

If the child is later consumed, that consumption occurs after c_j, because it is not selected until a later macro. Along a parent-child edge with both deaths we therefore have

    birth(parent) < birth(child) < death(parent) < death(child).

All finite roots are the black lifetimes at the initial cut. Every parent emits finitely many children, all unconsumed old siblings remain in the full field, and the exact mass ledger is

    m_(j+1) = m_j -1 + |E_(t_j)|.

There is no LIFO or stack restriction. An infinite collision run produces an infinite finitely branching finite-root genealogy; an infinite ancestry ray is entirely possible. Both births and deaths decrease backwards on a ray, but this gives no decreasing age, distance, wait, or forward well-founded potential.

The essential additional ordering condition is SPATIAL and simultaneous: at each event, the entire live old board B_j must avoid EVERY earlier empty-reference read, while its selected parent lies at the first such read. Every child lies in the complete emitted E_(t_j), with its genuine last-R birth. Other old branches cannot be silently discarded when testing the next event. These negative read-set guards, together with emitted positions, are the exact obligation that a future reproduction/return invariant must exploit. A generic branching forest without these guards is too permissive.

## 4. A decisive scope control: standard104 itself never terminates this map

For EVERY one of the104 cyclic standard phases, compare its turn word with the empty-reference prefix. The first disagreement occurs at an empty-reference R versus an actual standard L, after one of

    0,1,2,3,5,6,7,10

matching moves. The maximum is10. Thus at EVERY restart on an already standard orbit, this operator has another old contact within11 physical moves. It does NOT terminate merely because the ant has captured, and an infinite collision genealogy is not evidence of noncapture.

A global-attraction use must stop when an independently certified capture guard is reached, including guards at intermediate physical cuts, or classify the recurrent collision process. Proving that the raw collision operator has only finite runs would be false.

## 5. Executed controls and scope

`blank_collision_operator.py` implements finite-prefix lookup, exact parity-ray intersections, full emission, L successor, exact emission birth queries and optional finite materialization. `check_blank_collision_operator.py` verifies:

-300 bounded XOR-segment/ray controls including cancellation and all direction pairs;
-35 consecutive exact collision macros on each of seven literal finite seeds, stopping only if the no-contact case is certified; each whole field and every emitted lifetime is compared with ordinary read-by-read dynamics;
-a single remote black input at parameter K=10^9: its first contact is at elapsed104000009905, yet its complete emitted board uses757 XOR terms; a further exact collision on that enormous COMPLETE board is found without materialization;
-all104 standard-phase nontermination controls above.

The giant-distance case is symbolic;104 billion moves were NOT simulated. No infinite or external supply is introduced: every segment length is finite and all cells arise from the exact empty-prefix emission.

The sharp pristine-cohort advance theorem now supplies a concrete constraint on this unrestricted event model: before its first collision at a pristine coordinate record, advance is at most22. But after a collision the emitted field can refill later record cohorts. Neither the exact event model nor finite-root genealogy controls that replenishment globally. The standard104 conjecture remains UNSOLVED.
