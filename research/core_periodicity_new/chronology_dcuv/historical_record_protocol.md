# Historical-record residual chronology

Status: analytic reduction approved by the independent auditor; prototype finite models remain under independent review. The DCUV exclusion and global highway conjecture remain open.

## Fixed numerical data

Use the hash-bound recurrent-eight profile, the literal ordered residual ledger, and a fixed potential file. In the first pilot the direction is L(x,y)=x+3y. Write A_h=L(R_h(-1,1))+c_h for the core offset. For packet a at heading h, define its created peak

T(a,h)=max(2L(R_h endpoint_a)+A_(h+turn_a), max_j(2L(R_h output_aj)+w_ajh)).

The full peak includes its entering core: max(A_h,T(a,h)). Every output is recorded immediately, even if that identity is later retired. Saturating output weights to T(a,h)-2L(R_h output_aj) preserves the created peak and can only improve transfer inequalities. This normalization is optional for soundness.

All dangerous target types must have a residual input. An empty-input target would require a direct T<=A check and could not be handled by earliest-producer anchoring. Every current recurrent-eight type has inputs.

## Historical maximum and activations

Give each initial residual identity fixed intrinsic weight I at its physical cell, but activate/record its value only when it is first consumed. Choose I at least max(T(b,h)-2L(R_h input_bi)) over all packet inputs and headings. Record the entering core initially, every later core and every newly installed output value, and every initial activation. Let M be the maximum of all recorded values, not merely values of currently active identities.

A packet containing an initial identity cannot make an unfunded strict record: that activation's value already meets its created peak. Every activation increases M by at most

K=max(I+2L(R_h input_bi)-A_h),

because the entering core is already recorded. There are at most m-5 distinct initial residual identities for an entry board of mass m. For the first frozen candidate, exact arithmetic gives I=110 and K=130; these constants are discovery arithmetic until independently rechecked.

## Anchoring an unfunded strict record

Suppose a target creates peak S strictly above every earlier core/output/activation value, and no consumed input is initial. Choose the earliest last producer among its consumed identities as the outer source. Choose one such identity as protected q. All target input identities were produced at or after that source. Every complete intermediate context avoids q by the signed residual lemma. Source and every strict intermediate packet have both entering core and created peak strictly below S.

Normalize the source pose to (0,0,N) but retain its actual global heading phase r. The target threshold is 2L(R_r target_position)+T(target,r+relative_heading). Every explicit intermediate pose (p,h) is allowed only when

2L(R_r p)+max(A_(r+h),T(packet,r+h)) < S.

Equality is excluded, since this is a strict historical record. Source must pass the same strict inequality. A target with T<=A cannot make a record and is removed algebraically. Four source phases cover all actual headings and permit the rotated directional bounds needed for confinement.

## Finite patch abstraction

Start from the separately signed anchored guarded-XOR color abstraction with protected q and signed ordinary/protected subpair guards. Retain all physical target input cells in the color patch. Give each target input cell two fused bits: 0=white, 1=black of unknown origin, 3=black with a producer at or after the outer source. Source outputs initialize as known. A complete context touch retires the previous identity; only after retirement install each fresh RAW output as known, including recycled black-to-black cells. Untouched watched cells retain their identity bits. Nonwatched cells need only their color.

Only the outer goal tests that every residual input has a known producer. There is no unproved intermediate event rejection, no candidate H, and no least-gap mutual induction. Strict near transitions additionally satisfy the geometric record bound. OUT preserves watched cells because every hidden context misses the patch; omitting the geometric restriction during OUT enlarges the model and is conservative.

Thus a no-hit invariant excludes that specific record-conditioned source/target/phase event, not the corresponding unrestricted transfer. All admitted earliest-producer alignments and phases must be covered before concluding that unfunded records never occur.

## Current finite inventory and pilot

`record_peak_inventory01.json/.tsv` has 4,129 admitted record-conditioned alignments after signed protected exclusions, nonrecord target elimination, and the source peak cut. `record_peak_pilot/summary.json` covers source D to D and U: 9 no-hit invariant closures and 9 abstract witnesses. All no-hit invariants pass the existing local reset-BDD checker; independent model and invariant review is pending. No full record family is closed.

If every required event were excluded, the bounded initial-activation jumps would bound M in each of four rotated directions. This would confine marked heads and packet reads to a finite box. The existing positive C/U/V mass accounting and straight-D displacement argument would then rule out an infinite DCUV tail. This conclusion is conditional, not yet proved.
