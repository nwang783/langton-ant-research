# RIGHT-L3 transport at a bend and odd sources for LEFT-L3 renewal

23 October 2026, 18:58 UTC. New occurrence-level conservation corollary,
submitted for independent review. The output charge is newly written
BLACK wake, not consumption of original fuel or a permanent root.

## 1. Two-sided rank-three state

At a selected first-L contact of a complete WHITE cap-four front, the
history is R,L,R, with either no final L3 or one final L3 on LEFT or RIGHT.
Use a three-state symbol 0,L,R for these alternatives. The previously
signed bit s=1 for L and s=0 for 0/R is retained, not silently identified
with total L3 absence.

Consider a RIGHT face, in the exact normalization

    entry A=(1,0), prefix N,N,S;
    exit B=(1,1), prefix E,E,W.

A RIGHT L3 has incoming S, while B RIGHT L3 has incoming W. Let rho_A,
rho_B indicate those RIGHT L3s. The physical edge B->A points S. The
COMPLETE output/input port counts are

    number of S outputs from B=1+rho_B;
    number of S inputs at A=1+rho_A.

The first S output/input are B.R0 and A.R2. Thus rho_A=rho_B, and when
they equal one, their SECOND physical occurrences are consecutive:

    B.RIGHT-L3 -> A.RIGHT-L3, T3(A)=T3(B)+1.           (1)

This is backward transport in selected Gamma order and actual forward
transport in time on the RIGHT side. It is not a same-full-pose splice.
The identity is independent of the other LEFT neighbors being strict
or equal-M, and its local port proof does not need K=1.

For comparison, the signed LEFT-bend fact transports LEFT L3 forward:
A.LEFT-L3 -> B.LEFT-L3. Hence at EITHER bend a direct L-to-R or R-to-L
state change is impossible: LEFT bends preserve presence of L, RIGHT
bends preserve presence of R. State0 is distinct and cannot be discarded.
Straight faces require their own signed inventories and may behave
differently; no all-geometry side-switch rule is asserted.

## 2. A LEFT-L3 rise has a genuinely final R2 source

Now use K=1 and the signed state-gate theorem: every rise s=0 to s=1
occurs at RIGHT with at least one equal-M LEFT neighbor. In that face
B has LEFT L3, so rho_B=0. Equation(1)'s port count gives rho_A=0.
The entry A has s_A=0 as well, so it has NO L3 on either side. Its
complete history is exactly R,L,R, and its actual final R2 writes BLACK.

Thus each LEFT-L3 renewal has a distinct selected entry cell with odd
complete history and final black output. Different rises have different
physical classes in the actual full-drift quotient, because Gamma is
an embedded full-winding-one circle.

Let n_up count rises and N_odd count all odd complete physical histories.
For complete WHITE cap-four cells, R-L=1 at R or RLR, and zero at RL or
RLRL. Therefore

    R_total-L_total=N_odd >= n_up.                    (2)

This is a reservation of DISTINCT final black output cells. It is NOT
an original-seed budget, does not say those final cells are later fuel,
and does not assign a new ancestry root to each renewal. The front can
produce black wake each period, so(2) alone is no exclusion.

In particular an exactly zero-black-production WHITE cap-four K1 front
would have no rises. Cyclic equality of rises/falls would then make the
selected LEFT-L3 bit constant. Constant-zero and constant-one branchful
modes both remain open; the required LEFT maximum branch need not be a
rise site.

## 3. Canonical turn bookkeeping, without double counting

The signed canonical turn identity gives

    N_odd=4*(number of clockwise contractible canonical cycles
             - number of counterclockwise contractible cycles).

Together with(2), this requires clockwise excess at least
ceil(n_up/4). This is the SAME black-output reservation expressed in
the sheet register, not an additive second payment. It is not asserted
that distinct renewals need distinct clockwise cycles.

A RIGHT-bend FALL L->0 similarly has B with exactly RLR: rho_A=0 from
its LEFT L3, so rho_B=0 and B has no L3. But a fall followed immediately
by a rise may reserve the SAME selected cell. No one-odd-cell-per-change
claim is made. A fall at a strict straight face may retain a RIGHT L3,
so this bend-only fall corollary must not be imported there.

## 4. Saved local table cross-check, not a rerun

The previously frozen right_turn_equal_branch_ports.json has exactly
four local 0->1 profiles:

    Z strict, Y equal: Z=WW,   Y=NSSS;
    Z equal,  Y strict: Z=WWEE,Y=NSN;
    Z equal,  Y equal: Z=WWE,  Y=NSSS;
    Z equal,  Y equal: Z=EWW,  Y=SSNS.

In all four A is exactly NNS and B is EEWE. This agrees with the direct
port proof; no new enumeration, external connector or period scan was
performed. These are necessary local inventories, not realized fronts.

Saved table SHA
5af4aa1ba8c6a087bedc80078ff3c46231815db2821cb24fc741140b0f665fff.
Signed state-gate theorem SHA
ac025ac64acb980d7ace6b757f5c6d9902b4084529ff2d38e449f5f6a771130f.
Signed canonical turn-identity note SHA
afbc4e56fd5b3513d51f8dae596f5aad133b7607b5b0b2181224385a923aa24c.
