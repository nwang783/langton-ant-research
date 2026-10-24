# A forced open-case helper and simultaneous live resources before a V1 branch

23 October 2026 10:49 UTC. Author all-word balance proof and exact masks pass;
independent review requested. This is a CONDITIONAL V1-origin branch, not allV1.

## Scope and coordinates

Normalize a DC producer to(0,0,N), with old outputz=(3,1). Suppose that exact old
identity feeds input(0,3) of a later V at relative pose(0,1,E), with source-
included/consumer-excluded C-age exactly3. All strict intermediate packets are
from D,DC,V,VC,VCC,U,UC,UCC. The V's other input may have ANY legal origin.

Use physical height L(X,Y)=X+Y in this source frame. Let H be the V consumer's
head height (H=1 after this normalization). The goal inputs have heightsH+3
(the protected sourcez) andH+1 (the selected other input). This is the original
phase1 record-height convention after target normalization, not a new direction.

## Complete two-C height balance, with unbounded D runs allowed

Source DC contributes1C, leaving exactly2 strict Cs. Its raw exit heading is W,
and the consumer heading is E. The two C center steps have height changes0,-2,
using the signed core-center correction(-1/2,-1/2) and C-center step(1,1).
The exit head height isH+2, so these C steps supply the entire required drop2.
All zero-C BASES therefore have total height changezero.

Before the first C (headingW), D,V,U bases change height by0,-2,-4.
Between Cs (headingS), they change it by-2,-4,-4.
After the last C (headingE), they change it by0,+2,+4.
Let their respective D,V,U counts be(a,b,c),(d,e,f),(g,h,i), INCLUDING bases
attached to C tails. Exact height balance gives

h+2i=b+2c+d+2e+2f.

The right side is POSITIVE. If one packet supplies both Cs, it is VCC or UCC
(DCC is not retained), so it has a pre-C V/U base. If two packets supply one C
each, the second has a middle-S D/V/U base. Consequently a V or U occurs AFTER
the last C, in the SAME heading E/global phase1 as the goal. This argument uses
no upper bound on D runs, transverse excursions, total packet count, or C-free
cancellations.

Choose the LAST such V/U helper. Every later strict packet is D at headingE.
The helper is exactly V or U, not a positive-C tail. Its start height isH-2 forV
orH-4 forU, since the following Ds have zero height change.

## Three simultaneous identities before this helper

A phase1 V atH-2 consumes input(0,3) atH+1; a phase1 U atH-4 consumes upper
input(-1,4) atH+1. Their output heights are all at mostH-1. Subsequent E-oriented
Ds output only atH-2. Hence neither the helper nor any later strict packet can
create either goal input atH+1 orH+3. Both goal identities already exist before
the helper. Its ownH+1 input is a DIFFERENT identity: it is retired there and
there is no later output at that height to regenerate the future goal identity.

Thus, immediately before the helper, the exact residual ledger contains:
- TWO distinct identities at heightH+1;
- the protected sourceDC identity at heightH+3.

No Cs occur from this helper through the goal, so age obligations synchronize:
- V-helper branch: theH+1 identities require ages>=2 and>=3;
- U-helper branch: theH+1 identities require ages>=5 and>=3;
- theH+3 protected source identity has age exactly3.
Entry identities are exempt from produced minima, or assigned formal infinite
age. In the U-helper branch its critical upper input therefore predates the
sourceDC by at least two C increments if produced; it need not be initial.

For the fixed original record candidate, phase1 created peaks are26 forV and30
forU. With goal scoreS=2H+26, this helper has score EXACTLY S-4 in either case.
This is a forced earlier OPEN-caseV1/U1 helper near the record, not funding atS
and not a contradiction. In particular it does not prove allV1 cases have this
DC-origin branch or that the helper itself is an unfunded record.

## Sharp actual V-helper control

The signed nine-cell word DC,VCC,V,V realizes the V-helper demand exactly:
just before its strict V at rawtime73, cells(2,0) and(0,2) are residual atheight2
with C-ages3 and2, while sourcez=(3,1) is atheight4 with age3. The goal head has
H=1. All actual turns and the final marker are checked from the explicit seed;
there is no freely transported core or helper-root assumption.

Files: check_v1_dc_age3_last_helper.py and
chronology_dcuv/v1_dc_age3_last_helper.json. This supplies a compact conditional
simultaneous count/history obligation beyond marginal input ages. It does not
bound global resources, totalC, or either remaining funding-record case.
