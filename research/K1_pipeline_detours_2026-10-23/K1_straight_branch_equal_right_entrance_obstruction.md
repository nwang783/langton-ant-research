# The equal-max RIGHT entrance to a straight branch is impossible

23 October 2026, 19:36 UTC. New actual-cursor branchful obstruction,
submitted for independent review. No leftmostness or globally absent
branches are assumed. The strict entrance alternatives are retained.

## 1. Exact retained geometry and clocks

Use the complete WHITE cap-four K1 front and the physical lift of the
signed straight-branch predecessor and successor notes. The current
STRAIGHT face F=(0,0) has LEFT max J=(-1,-1), helper z=(0,0), entry
U=(1,0), exit A=(0,1), z=WWEE and U,A=NNS or NNSS. The RIGHT successor
has first helper w=(-1,1) and lower corner e=(-1,0), with

    e=NSS or NSSN.

Assume the preceding face P=(1,-1) is RIGHT and its second unused LEFT
C neighbor K=(0,-2) is M. The signed exact entrance table then gives

    r=(1,-1): WEE or WEEW,
    q=(0,-1): NSS, NNSS or NSSN,
    T0(q)=T1(U)-2.

Put u=(-1,-1), whose incident C faces are J(NE) and Q=(-2,-2)(SW).
Q is not assumed maximum or strict. Let delta=T1(U), beta=T1(z).
Complete physical edge matching gives

    T0(z)=delta+1, T0(A)=delta+2,
    beta=T2(U)+1.

Match all occurrences on q--W-->u--N-->e--E-->z--S-->q.
The first E output at e is R0 and arrives z.R2; its optional second
N input is e.L3, which must be strictly later than

    T2(e)=T1(A)+2=T3(z)+3.                          (1)

## 2. The complete corner closure is q=NNSS, u=EWW or EWWE

First suppose q=NSS or NSSN. Its FIRST W output is q.R2, supplied by
z.R2 one step earlier. Hence u's first W input is T2(z)+2. But u's
FIRST N departure must feed e.R0 and z.R2, and therefore occurs at
T2(z)-2, BEFORE that first W input. A strict u starts R0(W) and cannot
do this. A flat u starting W cannot either. A flat u starting E can
emit N before its first W input only at L1(E). The exact counts then
leave u=EEW (one W input) or EEWW (two); EEWE would emit three N into
e's at-most-two N inputs. In either retained case its R2(W) is the first
W input and supplies e.L3 at T2(z)+3. This contradicts (1), because
T3(z)>T2(z). Thus neither NSS nor NSSN is possible at q.

Consequently q=NNSS. Its W outputs are L1,R2 and its S inputs are R2,L3.
If u begins R0(W), the actual first-port chain is

    q.L1 -> u.R0 -> e.R0 -> z.R2 -> q.L3.

This is a four-step return from q rank1 to rank3, with its R2 strictly
between, impossible since T3(q)-T1(q)>=8. If u begins R0(E) but L1(E),
its two W inputs force u=EEWW. Its R2 supplies e.L3, yet

    T2(u)<=T3(u)-4=T2(q)-3=beta-2,

so e.L3 occurs before beta, contradicting (1) and T3(z)>beta.
The only remaining whole histories are therefore

    q=NNSS, u=EWW or EWWE,
    e=NSS for EWW, e=NSSN for EWWE,
    T2(z)=beta+4.                                  (2)

No absent earlier R0 or optional e/u L3 has been silently deleted.
The exact local composite control below independently retains precisely
these two corner profiles. It is not a literal exterior realization.

## 3. J has no possible selected outgoing edge, so its square is LEFT

All four corners of the maximum face J are q,u,e,z. A selected outgoing
first-L edge of J would require R0 choosing J and L1 having that SAME
incoming heading, to enter the child max face.

- q.R0 chooses K, not J;
- u.R0 chooses Q, not J;
- z.R0 chooses F, not J;
- e.R0 chooses J, but e.L1 has the OPPOSITE incoming heading.

Thus J has NO selected outgoing child contact and cannot belong to the
chosen first-L cycle Gamma (indeed it is a leaf in the canonical birth
forest, not a claim about a canonical TOP sheet node).
At q and z the selected negative transitions ENTER J, which is off the
cycle; u/e are not selected contacts at all. Hence none of J's four
corners is crossed by Gamma. A diagonal C-contact curve intersects a
physical square's boundary only at its primal corners. The whole closed
J square is therefore disjoint from Gamma and, by its known local
STRAIGHT-F LEFT sector, is strictly LEFT. This remains true under folded
curves or short full quotients and requires no global halfplane claim.

## 4. q.L1 is forced inside a RIGHT excursion

From q.R0=delta-2 and same-cell spacing,

    T1(q)>=delta+2=T0(A).

From q.R2=T1(z)+1=T2(U)+2,

    T1(q)<=T2(U)-2<T2(U).

The K1 RIGHT excursion starts at A.R0 and ends at U.R2. Equality
T1(q)=T0(A) is impossible, since q and A are distinct physical cells.
Thus q.L1 must occur strictly DURING that RIGHT excursion. Section 3
places q strictly LEFT. This contradicts the actual continuous cursor.
The equal-K RIGHT entrance is impossible at every period.

## 5. Safe resulting branchful alternatives

Together with the signed predecessor theorem, EVERY straight equal-M
LEFT branch must enter through a STRICT state fall: a strict STRAIGHT
predecessor, or the strict second-helper RIGHT row. LEFT and equal-K
RIGHT entrances are both excluded. Therefore the signed strict-fall
stock closure and its output reservation apply to ALL straight max
branches of the chosen Gamma.

In particular a constant-zero LEFT-L3 mode has NO straight faces: its
strict straight faces were already impossible by the input-state rule,
and an equal-M straight would now require a preceding strict state fall.
Constant-one already excludes equal-M straight branches by their state0
ports. All-bend branchful modes remain open. This is not a general K1
exclusion or an original-fuel bound.

If n_SB counts straight max-branch faces and n_up counts selected
LEFT-L3 rises, the signed distinct nonflat output reservation becomes

    N_odd>=n_up+n_SB.

This remains final-black OUTPUT, not initial black fuel, and is the same
canonical-turn reservation rather than an additive second sheet payment.

## Sources and finite necessary control

K1_straight_branch_predecessor_alternative.md SHA
a1f32674b55569559888acafd854403fa7e70b91e1da75ae9a196bc27228740b;
K1_straight_branch_double_max_successor.md SHA
fdb4444ddd0593fdb361cc0e734fb408038339a1b40ddb9e986ff6362e60d8eb;
K1_strict_fall_branch_stock_loops.md SHA
730d9bb19a41dfbdd490b835f3c67679c5d54bc842739c7b62ca9eb2522a6536.

straight_branch_equal_right_entry_closure.py/json combines the complete
signed entrance/successor rows, keeps every strict/equal complete u
history, and matches all physical ordinal edges and finite clock
inequalities. It leaves80 necessary rows, with exactly the two corner
profiles (2). No period, drift, radius, or exterior-connector search
is performed. The analytic LEFT/RIGHT contradiction, not a bounded
row count, excludes those remaining local profiles globally.
