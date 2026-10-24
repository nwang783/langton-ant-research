# Three all-cap first-N return rules remove61 further growth-eight interfaces

24 October 2026. Author analytic proof with explicit physical-path
certificates, submitted for independent review. This reduces the signed
coarse diagonal boundary family; it does not classify all fronts or force
finite width. No SMT result or visit-count enumeration is a premise.

## 1. Local port identities, independent of the first color

At a physical cell with vertical incoming axis, outgoing W is produced
exactly by S/R or N/L. Let w_i be the complete read rank of W-departure
ordinal i, and n_i that of N-arrival ordinal i, with ordinals starting at
zero. Suppose a literal path leaves this cell and first returns to this
SAME physical cell with those port ordinals. If its source is w_i and its
target n_j, they are consecutive reads: n_j=w_i+1. Return duration and
full-drift lifts must be supplied to justify this identity; quotient-only
return to another translated physical cell is insufficient.

The following elementary rules apply to every alternating history, whether
its first color is WHITE or BLACK. They retain all middle reads.

### First-N identity

If n_0=w_a+1, then n_0 must be L. Otherwise it is R and w_a is L; an L
turn departing W must itself arrive N, before the purported first N.
Since n_0 is L, it also departs W. Being the very next read after w_a,
it is the next W departure, hence

    n_0 = w_(a+1), and this event is N/L.               (F)

### Rule A: the known W count has no room for this next departure

Let J be the TOTAL number of W departures in the complete history.
If J<=a+1, (F) demands a W departure beyond that total. Contradiction.

### Rule B: the next return skips an N ordinal

If another physical first return gives n_b=w_(a+1)+1 with b!=1, then(F)
makes the very next read after first N be N ordinal b. Such a read would
necessarily be the SECOND N, ordinal1. Contradiction. In the application
below b is2 or3.

### Rule C: two consecutive N/L events cannot be consecutive on both ports

Suppose J=a+3 and a second return gives

    n_2 = w_(a+2)+1.

Here w_(a+2) is the LAST W departure. Its next N read n_2 cannot be L,
which would depart W once more. It is R, so the preceding w_(a+2) is L
and arrives N. It is the second N arrival, hence n_1=w_(a+2), an N/L event.
Together with(F), the two events n_0=w_(a+1) and n_1=w_(a+2) are consecutive
N arrivals AND consecutive W departures, and both turn L.

Alternation puts at least one R read strictly between two L reads. At this
cell every R read is either N/R, adding an intermediate N arrival, or S/R,
adding an intermediate W departure. Either violates the asserted two
consecutiveness conditions. Contradiction.

These are exact ordinal obstructions, not estimates of elapsed time or
black mass. No arbitrary multiplicity cap, global WHITE count, period or
support bound was imposed in proving them.

## 2. Complete application to the signed diagonal lower cover

Start with the227 open interfaces from the independently signed
DIAGONAL_READ_MINIMUM_COMPLETE_INTERFACE.md77fde6d4, report9d8ef1d3.
Each fixes the COMPLETE histories at t=-1,0,1, including any empty class,
for full d=(2,-2). Its two immediate upper Q classes at t=2 remain unknown.

For each Q class, its TOTAL outgoing W count J is exactly the number of
incoming W occurrences at the relevant named lower neighbor. Its N input
count is likewise retained. Pair every internal physical edge by its
complete occurrence ordinal. Trace every internal chain from an upper
port back to an upper port, with actual full-drift spatial lifts.

Only a chain whose source and target are the SAME physical upper cell
is used as a first return. All its named intermediate reads have t<=1,
so none hits that upper cell at t=2. Therefore its port ordinals give the
consecutive-rank identity used in Section1. No proposed upper history,
port erasure, same-class/different-copy shortcut, or chosen time phase is
inserted.

The certificate retains all actual return paths and one exact Rule A/B/C
witness for each rejected interface. It finds68 such interfaces:

    Rule A:26; Rule B:32; Rule C:10.

The rejected ordered lower families, in the original certificate IDs, are

    case4 (SSN,SSN):7;
    case5 (SSN,SSNS):13;
    case8 (SSNS,SSN):13;
    case9 (SSNS,SSNS):35.

Thus159 of the227 remain after these rules. This is a complete application
of the three stated tests to the supplied finite cover, not a claim that
these are the only possible all-cap return obstructions. No next-row
multiplicity enumeration or paired-row product was required.

## 3. Combining only previously signed exclusions

The separately signed four-step skipped-middle theorem fb198c97,
independent report11beb4ad, removes two one-singleton cases. Neither is
among these68, so157 necessary interfaces remain at arbitrary growth.

At g=8 the signed cyclic-E theorem8981c7ff WITH mandatory read-footprint
addendum b24cf42a removes all nine original case4 interfaces. Seven were
already removed by the present rules, so only two additional removals
are counted here. The exact growth-eight diagonal remainder is therefore

    227 - 68 - 2 - 2 = 155.

The certificate explicitly stores all nine prior cyclic-E case IDs, both
prior skipped-middle IDs, the seven-element intersection with the new68,
the EMPTY intersection with the skipped-middle pair, all61 newly removed
IDs relative to the prior216, and all155 final IDs. The set differences
are checked directly, not inferred from marginal counts.

Equivalently,61 new interfaces are removed from the previously signed216.
The155 break down as4 one-singleton cases,12 mixed N-first/S-first cases,
30 one-quadruple S-first-circle cases, and109 two-quadruple S-first-circle
cases. Each remains only a necessary open interface, not a physical
completion or alternative highway.

## 4. Evidence and limits

certify_first_N_return_rules.py produces
first_N_return_rules_certificate.json, binding the exact signed227-case
input. Every one of68 rejected cases includes full named histories,
upper port counts, complete physical first-return paths and its rule tag.
The displayed proofs plus those finite witnesses establish the rejection;
no opaque solver status is used.

The separate24-event prefix obstruction383f0205 motivated these rules but
is not an input to the227-case cover. Its two-return contradiction and the
positive OPEN cap4 model are compatible: local named-state consistency
does not supply a complete upper history.

All higher support and periods remain unrestricted in the theorem. The
other growth-eight drift types and the full finite-seed capture conjecture
remain open. This is not an assertion that a visit cap or standard104
footprint has been forced. No literature novelty claim is made.
