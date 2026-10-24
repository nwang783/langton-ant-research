# An ordered boundary of actual W-deletion ports

## Statement and exact scope

Use the three C3 return interfaces with the old C1 of actual DC normalized to (0,0,N). W has full-source entry clock 1, S clock 2 and E clock 3. All stages have arbitrary finite length. Work only BEFORE the first foreign starts.

For every actual full W packet, retain its entry head and the three local cells

    (-1,0), (-1,-1), (0,-1).

Their final physical reads in EVERY full packet type are L at zero-based ticks 1,2,3. They lie outside that full packet's entire output O and its FULL exit core K. If that W packet is DC, also retain local cells (0,0),(1,0), whose final reads are own C1 L at context ticks 12,13. There are no other full-packet last-L sites with local y<=0 outside both O and exit K.

NO actual external residual input of any plain E D/V/U packet can equal any retained deletion site. This is an actual current-identity ancestry constraint, not a claim that the physical site remains WHITE, that a center path cannot pass it, or that a guard cannot be influenced through the active core. Every port stays in the representation; its list length is unbounded.

The lemma is not extended to the first foreign's own inputs or to a returned packet. It does not iterate across a second foreign.

## 1. Exact deletion and full-output ownership

The checker reconstructs all twenty-six source-type/deletion roles: three for each of the eight full packets, with two additional DC roles. Each deletion is a real last L in that packet's RAW, and all actual own C tails are included. Its cell is absent from both the complete O mask and the FULL exit K mask. Thus the cell is physically WHITE when that full packet finishes, rather than merely being absent from an artificial atomic ledger.

The three common deletions are own-base tick 1/read 2, tick 2/read 3 and tick 3/read 4. The two DC deletions are its own C1 tick 2/read 3 and tick 3/read 4. The canonical formatter supplies every owner label. No marker is executed as an extra word.

The checker also verifies all sixty-eight full-output roles have genuine final RAW R births. This includes outputs physically installed during a real C tail. A current residual exported from a core is therefore included in a genuine completed full producer's O; it is not an untracked source category.

## 2. Later W output births cannot reach the ports

Write a W head as H=(-A,1+B). The three common ports are

    H+(0,-1)=(-A,B),
    H+(1,-1)=(1-A,B),
    H+(1,0)=(1-A,1+B).

The additional DC ports are H and H+(0,1). Every retained port is on or to the RIGHT of its producer head in physical x.

Every later W head has strictly smaller physical x. The possible preceding zero-C steps are D=(-1,1), V=(-3,1), U=(-4,0). A positive C tail ends that W stage, so a full packet carrying a tail has no later W packet in this same stage.

Every one of the eight complete output masks has nonnegative source-local y, INCLUDING all its own C-tail outputs. Rotation to W sends an output to physical x at most its producer head x. Consequently every output born by a later W full producer is strictly LEFT of every recorded earlier deletion port. No such output can supply a new current identity at that port.

This is not a bound on the number of W packets or their longitudinal span. The entire ordered sequence of actual producer heads and deletion ports is retained.

## 3. Exhaustive current-identity proof at an E input

Suppose an actual E external residual input were at a recorded site g. Its current black identity cannot be an unchanged factor-entry or older W-entry residual: the recorded real L destroyed any such identity. Its original deleting packet leaves no O or active exit K at g. It cannot be an older W producer's identity either, for the same deletion reason.

Choose the actual last completed full producer of the current input identity.

1. It cannot be the deleting full packet, which was checked absent from O and exit K.
2. It cannot be a later W full producer, by the strict x cone.
3. Any later core-to-residual export is itself in a genuine later O. It is not an exception to this source selection. Full packets do not overlap, so a producer started before the deleting packet cannot somehow finish after it.
4. Only actual S/E source entries at clocks 2/3 remain. At an E consumer entry clock 3, these have FULL-source-entry ages 1/0.

The signed completed-source young-input theorem excludes ALL actual external input roles at full-source age zero or one. The checker independently reconstructs its whole 3,128-role interface, not only distinguished inputs. Cases whose full source has not finished are marked incomplete rather than being assigned a fictitious younger birth clock. Every remaining sector-valid completed case is an exact signed COUNT5 exclusion.

This exhausts every actual current input identity and proves the contradiction. The argument does not apply COUNT5 to the foreign or any returned consumer.

A physical cell may in principle be toggled or carried through the active core after its recorded deletion. Such a transient or dormant young birth is NOT being declared impossible. What is impossible is presenting that later identity as the external residual input of an E old-eight packet under the exact producer-clock constraints above.

## 4. An explicit ordered forbidden-head interface

For each actual retained port g and each external input q of E plain D/V/U, the corresponding E head

    g - rot_E(q)

is forbidden. All 208 source-type/port/input offset roles are stored, 120 sector-active and 88 already sector-inactive. This records ALL D/V/U inputs, not only the selected genealogy slot. In particular it does not identify U's upper d with a lower input.

The representation is an unbounded ordered causal boundary, not a finite-state quotient. It can supplement the pure-V rail's exact affine deletion proof when mixed V/U outputs change the reverse geometry. It does not by itself prove a complete matching, unique reset, path barrier, at-most-one spending rule or decreasing global resource. The withdrawn seal 6ea48d5 is not used.
