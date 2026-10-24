# Root-free valley K1 in actual forward L3/R2/L1 chronology

24 October 2026, 02:05 UTC. Complete WHITE cap-four K1 front, actual full
P,d. Positive required odd output is retained. Pending independent
review. This does NOT assume a globally WHITE time reversal.

Let Q be a locally minimal L plateau at m=M-3 with NO odd-output incident
corner. It may be the shared valley plateau between ceiling bands; the
signed ceiling-band theorem excludes this root-free case only INSIDE
a ceiling band, not in such a valley. By the signed prepared reverse
plateau theorem ab9fad0a, Q has an essential reverse selected birth
curve, with reverse retreat

    K_Q=c_left-m=(M-2)-(M-3)=1.

All cells incident to Q have even original histories, so are WHITE at
reverse first read. Odd outputs elsewhere become BLACK reverse input
and remain part of all physical currents. No global reverse-WHITE
argument or zero-output whole-front theorem is imported.

## 1. Reindex the reverse cut in the actual forward direction

Let Lambda be the reverse parent-to-child curve, oriented in reverse
drift -d. Reverse time at a forward read t means reverse event time -t,
using the postflip board and heading opposite the forward OUTGOING
heading, as in signed0353c796. Reorient Lambda to forward drift +d,
and index its selected contacts v_j accordingly. If its quotient has
ell contacts, v_(j+ell)=v_j+d and T_r(j+ell)=T_r(j)+P.

Every selected reverse contact has at least three reads. Its original
history is even, so has exactly FOUR reads. The reverse rank map is

    reverse R0 -> original L3,
    reverse L1 -> original R2,
    reverse R2 -> original L1,
    reverse L3 -> original R0.

Reverse K1's exact pipeline, after reversing time and the contact index,
becomes the actual forward inequalities

    T2(j-1)<T1(j)<T3(j-1)<T2(j)<T1(j+1)<T3(j).

Thus the forward selected order is

    ... R2_(j-1), L1_j, L3_(j-1), R2_j, L1_(j+1), L3_j, ... .

Both L1 and L3 are actual supplied black reads. They are not replaced
by an earlier R or dropped as old stock.

## 2. Only two complete forward heading types

At a reverse birth, reverse R0/L1 have equal headings and reverse R2
has the opposite heading. In forward coordinates this says

    incoming L1=incoming R2=H,
    incoming L3=-H,
    incoming R0 is H or -H.

Normalize H=N. Exactly two complete forward words remain:

    TOP:  N N N S;   C heights m+3=M and m+1=M-2;
    FLAT: S N N S;   both C heights m+2=M-1.

Both L sectors are at m. Rotations and H=S give the other representatives.
TOP is a strict same-R triple-use internal cell, and the reverse selected
LEFT-L3 flag is1. FLAT has all four port flows equal2, and that reverse
flag is0. These are NECESSARY local rows, not realized connectors.

In the H=N normalization the forward-oriented L cut joins SW to NE.
TOP's C=M sector is SE, on geometric RIGHT of this cut. Therefore a
TOP selected reverse birth touches a global maximum C face only on its
forward RIGHT side. FLAT contacts have no C=M face. This one-sided
selection does not say that the whole Q plateau cannot touch maximum
components on both valley boundaries through OTHER contacts.

## 3. Exact forward crossing inventory

For the forward-oriented cut Lambda, the four actual reads have:

    L1: RIGHT -> LEFT;
    R2: stays RIGHT;
    L3: LEFT -> RIGHT;
    R0: stays RIGHT in TOP, stays LEFT in FLAT.

Hence the RIGHT excursion from L3_(j-1) to L1_(j+1) contains R2_j.
The intervening LEFT excursion is L1_j to L3_(j-1). Every original R0
precedes its own L1, but it may lie in a MUCH EARLIER same-side excursion;
no immediate-excursion assignment for R0 is being assumed.

The reverse cursor and both of its physical side currents remain valid
with prepared BLACK cells off Q. The forward crossing statement does
not identify them with the previously constructed C-cut side currents
or add overlapping current budgets.

## 4. A true local maximum/minimum clock coupling

At a TOP contact, let F be its adjacent C=M face on RIGHT. Its actual
forward R0 traverses an F boundary edge. The canonical max-face birth
cannot be that R event, so

    B_C(F)<=T0(j)-1<=T2(j)-9.

The second inequality uses the two actual same-cell return gaps, each
at least4. Thus the forward maximum-face birth lies at least nine reads
before the event which is the reverse minimum-face birth. This is one
exact clock comparison, not a closed ancestry cycle or additive cost.

## 5. Why an old zero-output strict-pit argument cannot simply be imported

The original global zero-output K1 machinery sometimes reaches a strict
opposite pit at lambda-5. Here reverse lambda=-m=3-M, so that would be
-M-2, below the genuine global reverse L lower bound -M. Such a pit
would be impossible. But the old derivation also used helpers OFF the
selected maximum plateau. Those cells may start BLACK in reverse;
they are actual original odd-output defects and are NOT excluded by
Q's root-free collar.

The live problem is therefore to reconstruct that route with every
BLACK off-Q supplier retained, obtaining either the impossible height
or a precise positive-output defect interface. No global even-front
result is being repackaged as a new exclusion. In particular one must
not assume the reverse flag is constant or that all reverse helper
histories start R without an exact incident-Q justification.

Control `root_free_L_plateau_forward_reverse_K1_controls.py/json` checks
all sixteen original four-read N/S histories, the exact read-event
reversal, all four surviving rotated rows, their face levels and every
forward side crossing. The bi-infinite pipeline follows from the signed
selected-contact reverse K1 theorem, not a finite scan.
