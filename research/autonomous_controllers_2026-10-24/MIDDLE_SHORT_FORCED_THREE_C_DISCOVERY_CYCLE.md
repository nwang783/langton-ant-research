# The middle-short core forces a three-face C-discovery cycle

24 October 2026. Author proof, independent audit requested. This strengthens
Section4 of10b4b262: its C5 upper alternative is impossible by one additional
physical port-order argument. The earlier weak alternatives remain true.

## Exact hypotheses

Use the complete WHITE full-drift(3,1) middle-short lower histories
T0..7=S,W,S,EEWE,SSNS,EEWE,NNNSS,EEEWW. No higher visit bound, period bound,
full-wake parameter restriction, or growth budget is used in the proof below.
Thus the result applies to all four still-open winding>=5 boundary types.

Normalize the physical faces
C1=(-7,-2), C3=(-6,-1), C5=(-8,-1), with d=(3,1).
Complete active-C visit counts are6,8,10, respectively. For C5, this follows
from the3 S arrivals at T4, the single W arrival at T5, the3 E arrivals at T7,
and EXACTLY3 N arrivals at T8. The latter count is forced by the complete
N-departure port of T5; it does not cap T8's S arrivals or its total history.

## The ordinal distinction that eliminates the upper entry

At physical T5=(-8,-1), its N-departure port consists of complete ranks1,2,3,
in that order. Therefore these supply the FIRST, SECOND and THIRD N arrivals
at physical T8=(-8,0), respectively.

The already fixed three-read channel is

T7.R0 at(-7,0) -> T4.R0 at(-7,-1) -> T5.R2 at(-8,-1).

Its next read at T8 is consequently the SECOND N arrival, not the first.
There is no T8 read in the three preceding updates. Its FIRST N arrival must
therefore precede the whole three-R channel, and already activates C5.

Every other C5 read is either a later N arrival at T8, or one of the named
T4/T5/T7 active-sector reads. The earliest of the latter is the displayed
T7.R0. Hence the FIRST C5 activation is exactly the FIRST N arrival at T8.
Its immediate predecessor is T5.L1 at(-8,-1), active on C3-d=(-9,-2).

In particular, a putative first entry through T8.S/L1 from C9 cannot be first:
it would land at the already later T7.R0. No assumption about T8's initial
heading, total multiplicity, or optional R laps is needed.

## Actual cycle, exact clocks, and what remains free

The lower named histories already give first entries
C5 -> C1 through T4.L1, and C1 -> C3 through T3.L1.
The argument above gives C3 -> C5+d through T5.L1. Thus these are an ACTUAL
three-face WHITE C-discovery cycle, with forward full winding+1 (or backward
parent winding-1), not a projected lifetime circuit.

Let s be the time of T7.R2 at(-7,0), the start of the forced17-read channel.
Then

A(C1)=s+2, A(C3)=s+7, A(C5+d)=s+17.

The first-activation intervals have exact lengths5,10,P-15. Their fixed first
two literal words are RRRRL and RRRRLLLLRL. The entire remaining interval
C5 -> C1 has length P-15 and remains unrestricted outside its named reads.
The three complete active-face visit counts6,8,10 do NOT bound that interval's
external excursions, T8's other-sector multiplicity, or the global period.

The selected first-entry owner cells are the complete quadruples T4,T3,T5.
Their first L reads retain their genuine R0 owners. Nothing here says the
whole C face remains active during its first-activation interval, that the
three intervals are removable modules, or that C7 has a prescribed first
parent. The two alternatives for C7 in10b4b262 remain open.

No one of the four middle-short boundary types is excluded. The new finite
obligation is the actual three-face discovery cycle with its exact third
interval and all exterior ports still open.

## Reproduction

certify_middle_short_three_C_cycle.py
middle_short_three_C_cycle_certificate.json

The checker independently reconstructs all physical port ranks and all25 named
successor events, inventories every incident C-face sector, and records the
three exact coordinates and full lifts. The proof uses chronological ordinals,
not an arbitrary clock model, exhaustive upper-row scan, or a finite-state claim.
