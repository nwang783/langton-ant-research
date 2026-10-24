# Physical return debt: a port capacity and an exact open-state countercheck

24 October2026. Author proof and literal controls, submitted for independent
review. No novel-priority claim, finite-state reduction, complete gap
exclusion or autonomous controller is asserted.

## 1. A precise debt record

For a prefix of COMPLETE spatial read histories, retain each open event chain
with its outside source and target physical port ordinals, its number of
named events, and its exact full-drift voltage. If the two outside endpoints
are the SAME physical cell, the chain forces those two reads to be consecutive
in that cell's complete chronology. Store the return record

    (departure port, departure ordinal, arrival port, arrival ordinal,
     physical duration, full lift).

This is an actual rank obligation, not just an edge-current count. In a
complete continuation, the arrival rank must be the departure rank plus1.
The existing exact graph operator already retains these records. They can be
extracted from all boundary chains, but keeping ONLY the currently visible
same-cell returns loses chains that will become returns after more cells are
added. The sufficient state is the entire port-labelled, length/voltage-
weighted chain matching plus the unresolved rank/clock inequalities. This
note does not prove that representation minimal or that any finite quotient
is impossible.

## 2. All-cap four-return endpoint capacity

Fix a physical cell, a return incoming heading v, and a turn sign alpha.
Put u=turn_alpha(v). Count actual four-step consecutive physical returns
whose first departure is u and whose final incoming heading is v. Then

    number of these returns <= number of alpha reads with incoming v.   (1)

Only reads covered by the return endpoints need be counted. The board may
have arbitrary prepared input, histories may have any multiplicity, and no
translation hypothesis is required.

Proof: the four-step loop is a unit face. Its three noncentral turns are all
alpha. If its source read has sign alpha, its incoming heading is v, so
charge that source. Otherwise its source has sign -alpha and the same cell
flips, making the return read alpha with incoming v; charge that target.
Thus every return charges one alpha/v read. Two returns sharing a charged
read would be the immediately preceding and following excursions at that
cell, both around the SAME unit face. Its first helper would then be read
with sign alpha twice, with no intervening helper read. That contradicts
the flip rule. Hence the charge is injective. The argument includes both
first colors and all four genuine rotations.

For the horizontal gap cell, u=S and v=W give alpha=L. Hence if q such
four-step returns are forced, q<=lambda, where lambda counts W at L ranks.
For the vertical gap cell with u=E and v=N, alpha=R, giving q<=I-eta, where
I counts all N arrivals and eta counts N at L ranks. These are chronological
port capacities, not signs for eta-lambda or a gap-monotonicity theorem.

This elementary statement is a port-labelled formulation of four-turn-run
geometry. It is not promoted as a new replacement for the stronger retained
short-return density results. In particular the already signed
`periodic_classification_new/all_cap_period_bounds.md` binds the no-four-
unit-returns, four/eight, and four/eight/twelve first-return theorems. Those
remain available with their exact arbitrary-input scopes.

## 3. Why the proposed count pump fails immediately

One supplied lower complete-history interface has T0..10 headings

    S, W, S, EEWE, SSNS, EEWE, NNNSS, EEEWW,
    NNSNSSSS, WWWEWW, SNSSSN.

Levels -3,-2,-1 are empty, and all levels above10 are UNKNOWN. In full(3,1)
geometry, the next T11 cell Q=(-8,1) has an exact four-step return:

    Q --S--> (-8,0)[T8 rank5]
      --E--> (-7,0)[T7 rank1]
      --N--> (-7,1)[T10 rank1]
      --W--> Q.

All three named helper reads are L. It matches the third S departure of Q
to its second W arrival, so those endpoint ranks are consecutive. The bound
(1) forces lambda>=1 in every completion, at arbitrary multiplicity.

The count-only12-level pump begins from(w,n,s,K)=(5,4,5,2) and chooses
lambda=eta=0 for its first transfer. Therefore it cannot extend THIS supplied
interface. The two other retained T10 interfaces in that count coset have
the same kind of return, with different ordinal details, but no exhaustive
coverage of all possible prefixes is needed or claimed here. The proposed
pump is not rescued by its matching flow counts and stream counter.

## 4. A projected debt count disappears without deleting its chains

Extend the displayed interface by the two COMPLETE histories

    T11 = WEEEEEEWWEEEWEWE,
    T12 = SSNNNSNSSSSSSSSSSS.

The resulting named-history graph has79 events and18 open chains. All exact
internal physical port ordinals and full voltages match. The supplied graph
checker finds no skipped rank, forbidden closed component or positive rank-
clock cycle. This is only a necessary OPEN interface, not an actual finite
factor, phase-complete clock model, controller or proof of extendibility.

The visible same-cell obligations at the next named cell have durations

    before T11: [4];     before T12: [8,4];     before T13: [].

At the final cut the18 chains are instead

    four T13-source -> T14-target chains,
    seven T15-source -> T13-target chains,
    seven T15-source -> T14-target chains.

Their outside-read distances sum to97=79+18, as required by the signed chain
mass identity. One chain has distance36. Every chain, ordinal endpoint and
voltage is retained in the certificate. Thus a scalar count of currently
visible same-cell returns cannot be called a monotone debt on these necessary
interfaces: they can become pending cross-cell obligations. No actual
WHITE growth8 trajectory violating a stronger monotonicity is exhibited.

A separate positive-model probe at period parameter10002, using the installed
solver and the full residue/distinct-phase constraints, returned UNKNOWN by
its30-second timeout. It was not an exhaustion and supplies no positive or
negative conclusion. The OPEN graph statement above does not depend on it.

## 5. Genuine finite controls and the unbounded clock span

A sharp five-read physical factor starts at(0,0), incoming E, with exactly
three initial BLACK cells(0,-1),(1,-1),(1,0). Its word is RLLLL. It follows
the same S->W four-step return and reads its endpoint L with incoming W.
There is one return and exactly one charged L/W occurrence. After all five
reads the ENTIRE field is WHITE and the head is at(0,-1), incoming S. This
is a prepared finite factor, not a complete WHITE front or repeatable module.

There is also an explicit family of prepared finite first returns with an
unchanged central port/rank interface and arbitrarily long clock span. For
any n>=2, start incoming N at the origin and follow the move word

    (E,N)^n (E,S)^n (W,S)^n (W,N)^n.

It has8n moves, returns first to the origin, and restores heading N. Its
read positions before that return are all distinct. To verify this for all
n, the intermediate positions of the four sides are respectively

    (i+1,i), (i+1,i+1);
    (n+i+1,n-i), (n+i+1,n-i-1);
    (2n-i-1,-i), (2n-i-1,-i-1);
    (n-i-1,-n+i), (n-i-1,-n+i+1),

for0<=i<n, retaining shared side-endpoints only once in chronological order.
The four staircase interiors are disjoint for n>=2; the only repeated
position is the final origin. Consecutive move axes alternate, so every turn
is R or L. Set precisely the4n-2 cells whose required first turn is L BLACK,
and all other cells WHITE. This finite initial field exactly realizes the
path. The origin is read R first and L at the returned endpoint. Reading that
endpoint gives an8n+1 factor with complete final BLACK support of size4n+1.

For every n, the central complete FACTOR history is N,N with turns R,L,
departures E then W and one same-cell first return. Its span8n is unbounded.
The executable supplies full initial/final fields for n2,3,5,20. The analytic
formula supplies the entire family. These factors consume growing prepared
input and have many additional odd-read cells. They are not finite-seed
infinite controllers and do not refute a theorem that uses the fixed WHITE
growth8 full inventory. They only prevent bounding return clock spans from
the central port/rank pair alone.

## Remaining proof obligation

No strict growth of a full weighted return debt across arbitrary even gaps
has been proved. A useful next invariant must retain enough cross-cell chain
pairing to account for the36-step obligation above and use complete WHITE
ownership to exclude or charge prepared-like long excursions. Returning only
to scalar flow, stream height or a currently visible short-return count would
forget precisely the information these controls isolate.
