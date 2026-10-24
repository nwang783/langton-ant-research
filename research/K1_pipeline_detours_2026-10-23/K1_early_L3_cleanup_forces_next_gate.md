# A literal source-L3 cleanup forces the next gate and its own main birth wait

23 October 2026. Submitted for independent review. Complete WHITE cap-four
K1, actual full P,d. Use precisely the source-L3 early-LEFT-parent mode
in K1_early_LEFT_parent_L3_exact_cleanup.md. This constrains the NEXT
main face, not just a local overlapping return span.

## 1. The actual 12-edge cursor interface excludes an interior next birth

Retain current branched RIGHT F=(0,0), birth alpha, entry A=(1,0),
exit B=(1,1), next main face G=(1,1), birth beta=T1(B)=alpha+15.
The earlier exact source-L3 cleanup gives T3(B)=T2(B)+12 and the literal
consecutive route

    B.R2 -> v.L1 -> a.L1 -> Y.R2 -> u.R2 -> t.L1
    -> f.L3 -> g.L3 -> u.L3 -> t.R2 -> a.R2 -> Y.L3 -> B.L3.

Positions are B=(1,1),v=(1,2),a=(0,2),Y=(0,1),u=(-1,1),
t=(-1,2),f=(-2,2),g=(-2,1). Every event from T2(B) through T3(B)
is occupied by exactly this actual cursor. The next selected contact D
is (2,2) when G is STRAIGHT, and (2,1) when G is RIGHT. Neither physical
D lies anywhere on this route. The K1 pipeline puts D.L1 after B.R2.
It follows, for BOTH successor geometries, that

    T1(D)>T3(B).                                    (1)

No global timestamp-distinctness is imported from minimum-clock tables.
This is the literal continuous-cursor exclusion in the fixed physical
lift, including small quotient/seam cases.

## 2. Next STRAIGHT: retain every output side, birth wait at least18

A strict S successor has v=NNN or NNNS. Its E outputs feed the complete
E inputs of D=EEW,EEWW or EEWE as permitted by the output state. Its
second E output is R2, supplied by B.L3, so exactly

    T1(D)=T2(v)+1=T3(B)+2=T2(B)+14.

Thus all optional selected L3 sides remain, and

    B(next after G)-B(G)>=18,

using T2(B)-T1(B)>=4. This interval is G's own consecutive main birth
interval, not the preceding F interval or an extra payment for the12-span.

## 3. Next RIGHT: three relaxed families are impossible

For R, helpers are v=(1,2),w=(2,2), selected D=(2,1). The complete
signed first-strict RIGHT inventory with input bit1 has six profiles:

    v       w       D
    NNN     EWE     SSNS
    NNNS    EEEW    SSNS
    NNNS    EWEE    SSNS
    NNN     EEWW    SSN
    NNN     EWWE    SSN
    NNNS    EEE     SSN.

All next output states and strict/equal SECOND other heights were
initially retained. First other is strict by the signed branch theorem.
Input B has no RIGHT L3; the signed RIGHT-side L3 transport excludes an
unlisted RIGHT-L3 at D, rather than dropping it by choice.

In vNNN,wEWE and vNNNS,wEWEE, the exact final S output w.R2 feeds
D.L3 and is supplied by v.R2, hence

    T3(D)=T3(B)+3.

Then T1(D)<=T3(D)-8=T3(B)-5, contradicting(1). In vNNN,wEWWE, w.L3
receives v.R2 at T3(B)+2, while w.L1 feeds D.L1. Their rank1-to-rank3
spacing gives the same T1(D)<=T3(B)-5 contradiction. These are actual
occurrence deadlines, not a phase or period scan.

Only the following necessary families survive:

    NNNS,EEEW,SSNS : strict locked row4, bits1->1;
    NNNS,EEE, SSN  : explicit strict rank-lowering fall1->0;
    NNN, EEWW,SSN  : explicit second-max rank-lowering fall1->0.

Thus a constant-one Gamma must choose locked row4 here. A variable-state
Gamma retains BOTH falls, not an unproved renewal or exclusion.

## 4. Each retained next RIGHT has a long own birth interval

For NNNS/EEEW or NNNS/EEE, v.L3 is at least4 after v.R2=T3(B)+1.
Its E output feeds w.R2, whose S output feeds D.L1. Therefore

    T1(D)>=T3(B)+7=T2(B)+19,
    B(next after G)-B(G)>=23.                        (2)

For NNN/EEWW, w.L1 is supplied by v.R2 at T3(B)+2; w.L3's S output
feeds D.L1 and lies at least8 later. Thus

    T1(D)>=T3(B)+11=T2(B)+23,
    B(next after G)-B(G)>=27.                        (3)

These are necessary literal minimum waits, not realized exterior
connectors. The fall's equal-M supplier remains in the EEWW family.

## 5. Safe additive refinement, without overlapping main intervals

Each source-L3 branch F has its current main gap exactly15. Its successor
G is one of the retained S/strict-R/fall-R types above, NEVER itself a
bit-11 maximum-branched RIGHT: S is not RIGHT, locked row4 has no max
LEFT branch, and both other R families are1->0. Hence G's own main birth
interval is disjoint from every bit-11-branch interval already counted
in the signed early-parent/long-wait clock. Distinct marked F classes
have distinct successor G classes in the actual full cyclic face list.

Let m_S count marked successors S, m_R count NNNS/EEEW or NNNS/EEE,
and m_F count NNN/EEWW. With the earlier bit-11 classes n_A,n_L,n_T,
the main intervals alone therefore give

    P>=5ell+10n_A+22n_L+26n_T+13m_S+18m_R+22m_F.

No12-span, parent wait, A/B/C physical flow or original fuel is added on
top. No positive density of these marked modes has been proved, and
no general K1/front exclusion follows.

## 6. Complete local check and scope

bit11_early_L3_cleanup_next_gate_ports.py/json appends complete f histories
and the proven actual deadline(1) to all54 source-L3 early-parent rows.
It checks162 local cases and retains36 necessary rows. Only f=EEEW
survives; next S minimum own wait18 and next R minima23/27 agree with
the analytic ports. The deadline is explicitly derived from the actual
12-edge cursor route, not inferred from disconnected minimum clocks.
These rows are not continuous exterior traces or white-front positives.

Dependencies: early parent six profiles8592d1c4, source-L3 literal cleanup
48494491 (submitted separately), signed outward/upper-branch tables and
RIGHT-side L3 transport6c107bd7, signed early/long clock39b74908.
