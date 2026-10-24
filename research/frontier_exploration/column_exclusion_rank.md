# Exact one-column exclusion dynamics

Status: analytic derivation, with a separate literal local checker. No macro language, bounded retreat, or symbolic lift is assumed.

Fix the usual heading/checkerboard sector and a physical column x. Its rows alternate between H cells (entered horizontally) and V cells (entered vertically). Every horizontal entry into the column is followed by exactly one vertical step within the column, then one horizontal exit, unless the vertical step leaves the proposed strip. Thus an internal column visit reads an adjacent H,V pair and flips both bits.

On rows y=0,...,H-1, let c_y be the black bit. Define an exclusion occupancy by eta_y=c_y at H rows and eta_y=1-c_y at V rows. Let N=sum eta_y and J=sum y*eta_y.

## 1. Exact reflection lemma

A column visit returning to the same side from which it entered has the following effect:

- Entry from the left and exit to the left moves exactly one occupancy particle upward by one row.
- Entry from the right and exit to the right moves exactly one particle downward by one row.

All other occupancies are unchanged. In particular N is conserved, while J changes by +1 or -1 respectively.

Proof for left entry (heading E): if the H cell is white, the ant moves down. To return left from the lower V cell it must read white there too. The pair of physical bits 00 becomes 11; after complementing the V bit this moves its particle from the lower V row to the upper H row. If the H cell is black, the ant moves up. To return left it must read black at the upper V cell. The physical pair 11 becomes 00, moving the particle from H to the upper V row. The right-entry cases are the reflected calculation. These exhaust the four reflection cases.

A transmission to the other side instead creates or destroys two adjacent occupancy particles. It is not a conservative hop. Therefore the reflection rank must not be summed through transmissions without accounting for these sources and sinks.

## 2. Uniform one-sided reflection budget

For a column of height H with N particles, J ranges between N(N-1)/2 and N(2H-N-1)/2. Consequently at most

    N(H-N) <= floor(H^2/4)

left reflections can occur in an interval containing no right entry and no transmission. The same bound holds for right reflections. External excursions may be arbitrary and may choose arbitrary allowed entry rows: they do not change the column's colors, so the rank still telescopes. If the interval begins with the head already inside the column, discard its one incomplete initial visit before applying the bound.

This is an arbitrary-time local theorem, not a periodic trace theorem. Its limitation is equally important: alternating-side reflections can replenish the rank, and transmissions can change N. The full highway conjecture requires control of those interactions.

## 3. A pristine barrier in strips of height at most three

No finite-support square-ant tail can remain in at most three consecutive physical rows.

For height three, take a column whose middle row is V and whose two boundary rows are H. Suppose all three cells are initially white and no entry from the right has yet occurred. A first entry from the left at the lower H row exits the strip immediately. An entry at the upper H row reads RR, reflects to the left through the middle row, and leaves the upper and middle cells black. Thereafter either possible left entry exits the strip: upper black turns out upward; lower white turns out downward. Hence this column cannot first be crossed from left to right while staying in the strip. The analogous right-entry argument exchanges upper and lower. Such bottleneck columns occur at every other x.

For height two, each pristine column has one boundary H row and one V row. Its first possible safe entry from a side is RR and reflects; the next entry from the same side turns outward at the now-black H row. Thus it too cannot be first crossed. Height one is immediate.

At any alleged start of a finite-support strip-confined tail, choose pristine barrier columns on both sides beyond the head and all finitely many black cells. The ant cannot cross either without first leaving the strip. If it never leaves the strip it stays in a finite rectangle, contradicting the standard finite-domain escape theorem. This proves the claim. The barrier argument allows arbitrary finite black cells elsewhere, because they cannot be read before the first strip exit.

## 4. Why the most tempting height monotonicity fails

For a four-row column with H rows 1 and 3, initially all white, arbitrary left-side entries at rows 1,3,1,1 are locally legal until the final transmission. The first two visits create black pairs {0,1} and {2,3}; the third annihilates {1,2}; the fourth transmits right at row 0. Thus first transmission need not raise the entry height, even on a pristine column. This is a local transducer witness, not a claim that an arbitrary exterior ant history realizes the chosen entry sequence. It shows exactly where a global frontier proof must retain exterior chronology.

## 5. Exact finite pristine-block certificates

A finite block [0,W-1] x [0,H-1] starts entirely white. Fix the sector in which x+y odd cells are H. Its allowed left entries are (0,y,E) with y odd. The abstract controller may select ANY such row after every left exit. Vertical exits terminate that branch; a right exit is the forbidden event.

`certify_blank_strip_barrier.py` constructs a finite set S of block color masks containing zero and checks that every allowed entry from every mask in S either exits vertically or returns left with a mask again in S, never right. The generator uses exact two-read column transitions. A separate literal one-update implementation replays every certificate transition and compares the complete result. The saved hexadecimal mask set is the inductive invariant, not a sample of ant runs.

This abstraction safely contains any actual history before the first right crossing: the exterior cannot change a block cell without entering the block, all safe entries before that crossing are from the left, and every safe left exit is allowed to choose any later compatible left entry. Possible external memory is therefore retained by nondeterministic overapproximation rather than discarded.

To exclude an axis-aligned strip, place one such initially pristine block far to the right of the finite field and the head. Place a 180-degree rotated copy far to their left. Choose the horizontal parity independently for the two copies so each realizes the certified sector. Rotation preserves the ant rule; an ordinary reflection would not be a valid substitute. If the ant never leaves the horizontal strip, neither barrier can be crossed, hence it remains in a finite rectangle and contradicts finite-domain escape. A height-H certificate automatically handles every smaller height by embedding its strip in H rows.

The exact discovery closures are (height,width,state count): (4,3,8), (5,3,14), (6,5,77), (7,6,184), (8,8,9438), (9,11,275057). The height-nine manifest and complete mask certificate have now passed fresh generation and complete replay by two independent transition implementations: 275,057 masks, 1,100,228 entries, 686,294 left returns, 413,934 vertical exits, no right exits, and maximum internal excursion length 171 updates. The certificate SHA256 is 04ec386f8d519687306a073b3ead9cb859109f133c62ae2ff34f132a3c4058c4. This one certificate suffices for all strip heights at most nine. Existence of such a pristine barrier at EVERY height is an open candidate, not a proved generalization. A state-cap exhaustion at larger heights is not evidence of a barrier.

These are physical horizontal/vertical strips, not the diagonal strips occupied by the standard highway. No eventual-periodicity assumption is used.


## 6. Self-contained finite-domain escape from the same rank

The independent auditor observed that the reflection rank also proves the finite-domain escape fact needed above, with no external dynamical theorem. Suppose an infinite orbit were confined to a finite rectangle. Let x be the rightmost column visited infinitely often. After finitely many steps no cell to its right is ever visited again. Every subsequent complete visit to column x is therefore a reflection from the left, and there can be no right entry or right transmission. Since each entry lasts only two physical reads, infinitely many visits would require infinitely many left reflections. Section 2 permits at most floor(H^2/4), a contradiction. The possible incomplete initial visit is discarded. This argument works for arbitrary initial colors in the rectangle.

## 7. Scope, comparison, and handoff

The certified conclusion is unconditional but narrow: every finite-support ant orbit eventually leaves every proposed horizontal or vertical strip of at most nine consecutive physical rows or columns; equivalently no tail is contained in such a strip. It does NOT exclude diagonal strip confinement, which the standard highway exhibits. It does not establish physical transience, eventual periodicity, or the standard104 classification.

The original column formulas and the blank-block overapproximation were independently derived in this exploration. Novelty of the theorem has not yet been established. The primary MFCS finite-domain confinement theorem bounds escape from finite connected domains, so its stated result alone does not imply escape from an infinite fixed-width strip. Jillhewar's diagonal transverse-width theorems assume a periodic translating tail and use different coordinates. A separate primary-source comparison was requested from the former literature analysis, who is not currently active. A comprehensive priority check remains open.

There are no pending owned computations at this checkpoint. The finite height-nine invariant is complete, and the independent auditor has the stable manifest. A larger exploratory run was deliberately stopped after reaching the 3,000,000-state cap in several cases; those cap hits are inconclusive, not barriers. In particular height10,width13 hit the cap; height12 transmitted through widths up to16, and height13,width17 hit the cap. The stopped exploratory run did not write its final combined JSON. Do not mistake an absent file for a completed proof.

Exact next targets:

1. Seek an analytic pristine-halfstrip penetration bound for all heights, or a driven safe transmission construction that refutes such a bound. The controller is allowed arbitrary sector-compatible left reentries, so this all-height statement is stronger than the finite-seed strip conjecture and might fail independently of it.
2. Derive a recursive description of the finite closed mask sets rather than merely extending exhaustive widths. The one-column occupancy rank supplies a local order; transmissions create/destroy two particles and are the precise obstruction to summing it globally.
3. If continuing computation, use the complete-mask invariant format and a separately implemented literal verifier; a state cap or long unobserved transmission is not a proof.
4. Test whether real exterior chronology is needed at larger heights. The arbitrary-reentry abstraction intentionally forgets it, whereas any eventual obstruction to that abstraction may be spurious for an autonomous finite-seed ant.
