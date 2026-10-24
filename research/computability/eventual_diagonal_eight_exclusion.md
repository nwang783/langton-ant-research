# No finite-seed eventual affine diagonal eightfold inflation

Status: independently analytically audited on 2026-10-22 at23:09 UTC, including the local proof and all affine/rotation phases. The complete local8+8 inventory independently motivated the proof but is not needed as a trusted solver dependency.

## Theorem

For a classical ant with finite initial black support, there are no integers c,N, vector b, and

    a in {2+2i, 2-2i, -2+2i, -2-2i}

such that

    p(8n+c)=a*p(n)+b for all n>=N.

No heading relation, finite controller, substitution, pure root, or alignment at time zero is assumed. This is a scoped self-similarity exclusion, not the highway conjecture.

## 1. A local pristine-row lemma

Start at(2,-2) with any heading, with every cell in y>=0 white and arbitrary colors below it. It is impossible to execute eight moves to(0,0), followed by eight moves to(2,2).

The first eight moves, with displacement(-2,2), necessarily have three north moves, three west moves, one south move, and one east move. This follows because axes alternate, so exactly four moves use each axis.

Consider their first hit of row0. If the unique south move had not yet occurred, this hit uses the second north move. The next two reads are at previously untouched row0 cells and force R,R, hence an east move and the unique south move. Since that east move exhausts the east budget, the remaining horizontal moves are west; the remaining vertical move is north. Depending on the initial movement axis, the entire eight-direction sequence is then exactly one of

    W N W N E S W N,
    N W N E S W N W.

The first sequence reads(0,-1) twice with R; the second reads(1,-1) twice with R. Both violate read alternation. Therefore the unique south move must occur BEFORE the first hit of row0.

That first hit then uses the third and last north move. It is either the final move, or the penultimate move followed by one horizontal move. In the latter case, the fresh row0 read forces R/east. Thus the junction(0,0) is still white and its incoming heading is either north or east. No row>=1 has been touched; in the north case no row0 cell has been read, and in the east case only(-1,0) has been read R.

The following eight moves, with displacement(2,2), again have three north moves and only one south move. This is impossible:

- If the junction heading is north, the fresh row0 read and its fresh eastern neighbor force one south bounce before row1 is first reached. First reaching row1 from below forces another R,R south bounce before row2 can be reached.
- If the junction heading is east, its fresh R immediately moves south. First reaching the untouched row1 again forces a second south bounce before reaching row2.

Both cases require at least two south moves. This proves the lemma on an arbitrary lower-half-plane background.

The discovery control `probe_diagonal_record_pairs.py/json` exhausts all internally alternating eight-letter images and all four headings. It independently finds zero legal predecessor/next pairs with displacements(-2,2),(2,2). The nine surviving first halves have precisely the junction types described above.

## 2. Fine-frame pristine band at a diagonal coarse record

Allow independent quarter-turn coordinate frames for the coarse and fine copies of the actual trajectory. Choose the coarse frame so x+y is unbounded above. Such a frame exists by finite-domain escape: if all four signed diagonal projections were bounded above, the physical trajectory would be bounded.

Choose the fine frame so the effective multiplier is2+2i. This is possible for each a in the theorem, because they differ by quarter rotations and complex multiplication commutes with the chosen coarse rotation. Both frames preserve the classical turn/color rule. Their headings need not agree; the local lemma allows all four fine headings.

In these frames write the affine identity as

    p_f(8n+c)=(2+2i)*p_c(n)+b_f.

If the coarse cell has level x+y=j, the corresponding fine center has height2j+beta, where beta is the vertical component of b_f.

Let t be the first coarse hit of a sufficiently large level Y. Before its predecessor n=t-1:

- Any earlier center at level Y-1 has a nonincreasing coarse step, or it would have hit Y earlier. Its fine macro therefore has vertical displacement-2 and only one north move, so its read heights are at most2Y+beta-1.
- Any center at level at most Y-2 has a fine macro with at most three north moves, so its read heights are again at most2Y+beta-1.

Choose Y beyond the initial black support in the fine frame and the finite uncontrolled fine prefix before8N+c. Consequently the fine half-plane y>=2Y+beta is wholly untouched and white before the predecessor macro begins.

## 3. Sector parity forces the forbidden record type

At a first level-Y record, the incoming coarse heading is north or east. The fixed pose sector is

    sigma = x+y+h modulo2,

where north has h=0 and east has h=1. Every sufficiently large integer Y is first reached because a move changes x+y by exactly1. For infinitely many of those Y, namely Y congruent to sigma modulo2, the incoming heading is therefore NORTH.

Take such a Y also beyond the initial coarse black support. Its cell is a first visit and initially white, so its next turn is R and its next move is east. The fine predecessor macro and following macro thus have displacements

    (2+2i)*north=(-2,2),
    (2+2i)*east=(2,2).

Translate their junction to(0,0). The predecessor starts at(2,-2), and Section2 makes y>=0 pristine before it. These are the two consecutive eight-move blocks forbidden by Section1. Contradiction.

No shifted full trajectory is claimed to obey a pure-root relation. Only the given affine identities at the predecessor, record, and successor are used; b cancels between their endpoints. The arbitrarily late record clears the finite uncontrolled prefix. QED.

## Scope relative to earlier finite searches

The existing positive-real-part diagonal pure-root512-turn theorem applies to ANY initial coloring, but only aligned a=2±2i. The present proof uses FINITE support and therefore covers the broader eventual affine/time-shifted scope and all four diagonal signs.

A newly found512-turn model for the negative-real-part diagonal pure scale(-2,-2) has207 first-L cells. It is a finite arbitrary-background control, not a contradiction to this theorem: it cannot continue indefinitely from finite support while preserving the inflation identity.


## 4. General diagonal-multiplier cone (independently audited extension)

The same record argument extends to arbitrary integer m>=1 and

    a in {m+mi,m-mi,-m+mi,-m-mi}.

Write k for the temporal dilation. Every k-step image has horizontal and vertical displacement of magnitude m. Alternating movement axes force k even, exactly k/2 movements on each axis, and k/2 congruent to m modulo2. Therefore

    k=2m+4r, r>=0.

Each outward fine macro has m+r north moves and r south moves. Each inward fine macro has only r north moves. At the first coarse diagonal record Y, all earlier macros before its predecessor have read heights at most

    mY-m+r+beta.

Indeed a levelY-1 center must move inward and contributes at most r north moves; a center at level<=Y-2 contributes at most m+r north moves. These give the same bound. Choose Y sufficiently large to clear the finite exceptional prefix and initial support as before.

For one of the infinitely many NORTH-entered coarse records, its predecessor and following fresh R/east step yield TWO outward fine macros. Together they have exactly2r south moves and end at height mY+m+beta. Their untouched fresh line starts at

    f=mY-m+r+beta+1.

If L=2m-r-1 is positive, the two-macro path must first hit f and then make L consecutive first-hit crossings from one new row to the next. Each interval begins at its FIRST hit of the lower row, with incoming heading north; the row and every higher row were unvisited before that first hit. Each crossing requires at least one south move. Moreover two adjacent crossings cannot both use only one south move: the audited one-south normal form is RRRRLR, and two consecutive copies force a same-turn reread at their seam. This is Section6 of fresh_band_inflation_obstruction.md. Therefore

    2r >= L+floor(L/2),  L=max(0,2m-r-1).             (2)

This is a necessary condition for every finite-support eventual affine relation in the stated diagonal-multiplier family. No finite control, prescribed heading, or root alignment is used.

For positive L, algebra rewrites(2) as

    7r >= 6m-4+(r modulo2),

or equivalently

    7k >= 38m-16+4(r modulo2).                         (3)

When L=0, r>=2m-1. Then 7r-(6m-4+(r modulo2))>=8m-4>0 for m>=1, so these latter bounds hold automatically. Thus(3) is a necessary condition without a separate case. The complete extension was independently audited on2026-10-22 at23:12 UTC. It excludes an infinite low-retreat cone. The special m2,k8 case has r1 and violates(2): two available south moves cannot pay for two adjacent fresh-row crossings, which require at least three. The explicit local proof above remains a self-contained small-case proof.

For example the least k not excluded by this necessary test is6,12,14,20,26,32 for m1,2,3,4,5,6, respectively. These are NOT asserted realizable. The inequalities do not prove existence or highway capture in any remaining case.

Further independently audited strengthening,23:26 UTC: `pristine_climb_cost.md` defines a total elementary-computable superadditive minimum c(H), with c1=1,c2=3,c3=7. Replace the earlier H+floor(H/2) fresh-row budget by c(H)>=7floor(H/3)+[0,1,3][H mod3]. The earlier inequalities remain valid, but are no longer the strongest recorded cone.
