# Guard avoidance does not uniformly bound transverse permanent-output span

24 October 2026. AUTHOR all-parameter finite-seed countercontrol, frozen for independent audit. This uses the actual retained twenty-cell circuit, not a supplied infinite wake or an edited mid-run field. Every member captures.

## 1. Two exact permanently unread cells in one fixed column

Use the same full twenty-cell input X_n, with even n=2k>=210. During the marked R60 lifetime, before its next read at e=624n-1516, the actual orbit creates both cells

    u_n = (-200, 2n+203),
    v   = (-200, -199).

Both lifetimes are permanently unread in the FULL actual future. Their exact births are

    b(u_n) = 104n+10325,
    b(v)   = 624n-11915 = e-10399.

Thus actual permanent output produced during this return has transverse span at least 2n+402, even on the SINGLE fixed column x=-200. This column lies in the fixed crossing band

    J = {x=-300,-299,...,-151},      width w=150.

The entire current relevant stock remains <=132 at ALL times, by the independently signed `TWENTY_CELL_RELEVANT_STOCK_AND_OUTPUT.md`. The R60 excursion crosses this same band outbound and back: its birth cell and post-birth head have x=0, while it reaches the third port with x=-5n+5<-300.

## 2. Exact all-parameter birth and never-read proof

In the four-cell reference, let U be its actual period after the 182-read prefix A, and Q_i its physical read position at phase i. Direct reconstruction gives

    Q_20=(5,1), U_20=R;
    Q_15=(8,1), U_15=R.

For the first cell, the complete ray equations Q_i+m(2,2)=(5,1), m>=0, have only solutions (m,i)=(0,0),(0,20). For the second, the only solution is (0,15). Hence the indicated R at phase20 or15 is the last-ever read of that cell in its standalone reference. Translation by j(2,2) proves the same final-read property for that phase in EVERY period j>=0. These are finite exact integer ray tests, not a finite-horizon assumption about permanence.

Stage1 starts at (n-1,n), heading N. Rotating (5,1)+j(2,2) counterclockwise and translating gives

    (n-2-2j, n+5+2j).

Choose j=k+99. Since k>=105,

    0 <= k+99 <= (2k-5)-1,

so this is one of its complete actual periods. The cell is u_n and its absolute birth is (52n-173)+202+104(k+99)=104n+10325.

Stage4 starts at (-3n,-3n+8), heading E. Its permanent phase15 cell in period j is

    (-3n+8+2j, -3n+9+2j).

Choose j=3k-104. Then 0<=j<(3k-4), so it is an actual complete period, and the cell is v. Its absolute birth is (468n-1296)+197+104(3k-104)=624n-11915.

The retained all-parameter pairwise separation of the COMPLETE five stage read sets excludes any other stage reading either born cell. Neither cell is ever reread later in its own stage, by the exact reference ray test. After cut e the ENTIRE true read trace stays in the protected region x>=-16 and -14<=x+y<=12. Both witnesses have x=-200, so the protected recovery and infinite tail never read them either. This completes the actual full-future permanence proof. No old residue is removed.

## 3. Guard avoidance is genuine, but must be precisely scoped

The signed retained family has exact earliest canonical104 word onset e+774. The strict lower bound follows from the literal mismatch at e+773 against the backward extension of the certified tail; it is not merely a sufficient entry time.

Consequently, for every cut t<=e, the actual state cannot satisfy ANY sound guard that guarantees canonical104 word onset within at most 773 further updates. Otherwise its onset would be at most t+773<=e+773, a contradiction. In particular it avoids all translated/rotated versions of the currently certified immediate outward-record guards, the conditional 262-step separator, and the eleven-cell 278-step terminal trap throughout these five stages.

This does not mean “every conceivable finite capture guard.” A guard can include a longer finite transient or be tailored to a whole capturing seed. The claim applies to the specified guarded classes, or more generally to any class with the stated uniform delay bound. Where a guard requires a current pristine half-plane, that premise remains part of the guard; globally unvisited head records are not substituted for it.

Thus avoidance of these actual sufficient guards, initial cardinality20, and a sustained relevant-stock cap132 do NOT yield a UNIFORM transverse-span bound in a fixed repeated crossing band across all finite seeds. The spacing of the original twenty input ports remains an unbounded parameter.

## 4. Span is not packing capacity

The countercontrol does NOT show unbounded permanent-cell COUNT in this fixed band. In fact the complete five-stage word decomposition gives a simple uniform read-count bound there.

Each stage has 182 prefix reads. For a fixed period phase, its x-coordinate advances by +2 or -2 from one copy to the next. Thus at most 75 copies of that phase can fall in the 150-column band. There are 104 phases in each of five stages. The terminal partial periods have lengths 61,71,61,71,14. Therefore the total number of actual reads on this band before e is at most

    5*182 + 5*104*75 + 61+71+61+71+14 = 40188.            (1)

The number of permanent R births there is at most this bound. Their transverse POSITIONS can spread arbitrarily far apart while their cardinality remains bounded. This is why the family defeats a uniform WIDTH closure but does not refute a more careful permanent-CAPACITY packing argument.

For example, combining (1) with the signed packing inequality and M=132, w=150 bounds the number of selected R lifetimes born and consumed within these five stages, each crossing all these fixed lines outbound and back, by

    N <= 132*40188/[4*(150-132)] = 73678.

This is a crude family-only count, not a global lifetime or time bound. No claim that its sampled23 returns are exhaustive for every parameter is made.

## 5. Exact controls and scope

`check_fixed_band_wide_output.py` regenerates the two phase/ray witnesses and directly replays the complete n=210 and n=400 inputs through their full recovery. It checks the exact births, retained final identities, full-field infinite tail parity, exact earliest onset mismatch, and all actual five-stage band reads. The observed band-read counts are 15284 and15600, below (1). Full terminal fields are retained during verification and their complete cell/lifetime hashes are recorded.

The universal result comes from the affine period indices, the retained guarded execution and protected full-future theorem, not from these two controls. This family does not refute an eventual orbit-dependent width or age bound, nor does it exhibit infinitely many deep returns in one orbit. Moving modules and permanent output in distinct distant strips remain separate from the fixed-band repeated-capacity obstruction. The global finite-seed standard104 conjecture remains UNSOLVED.
