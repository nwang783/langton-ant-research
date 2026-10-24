# A mod-four winding law from a 24-state turn-position cocycle

24 October 2026. Author proof, submitted for independent review. This yields
an all-parameter restriction on the live middle-short family, not its exclusion.
No claim of novelty relative to the literature is made.

## 1. Exact kinematic identity

Use T=3y-x and choose the physical sector in which incoming headings are
vertical for even T and horizontal for odd T. Put

w(T) = ceil(T/3) + 2*1[T=2 modulo6] modulo4.

Equivalently, for T modulo12 from0 through11 its values are

0,1,3,1,2,2,2,3,1,3,0,0.

There is a potential psi(T modulo12,incoming heading) on the24 allowed states.
Its values, listing N,S on even T and E,W on odd T, are

T0:(0,0); T1:(2,0); T2:(3,1); T3:(2,0);
T4:(0,0); T5:(2,2); T6:(0,0); T7:(0,2);
T8:(3,1); T9:(0,2); T10:(0,0); T11:(0,0).

For EACH right or left turn at EACH allowed state, direct substitution gives

psi(after)-psi(before) = w(T)*sigma - delta_y modulo4,

where sigma=+1 for R and-1 for L, and delta_y is the ensuing physical move.
The new normal coordinate is T+3*delta_y-delta_x and the new incoming heading
is the move direction. The certificate checks all48 transitions. This small
finite table is a complete proof of the kinematic identity, not a period scan.

Summing any turn word gives

sum w(T_read)*sigma = displacement_y + psi(end)-psi(start) modulo4.

In particular, if heading is restored and 3*displacement_y-displacement_x is
0 modulo12, the potential term vanishes. No board legality or WHITE assumption
was required for this kinematic statement.

## 2. Consequence for complete WHITE translating fronts

For a complete WHITE front, every full-drift class alternates R,L beginning R.
Its total R-minus-L count is exactly1 for an odd-read class and0 for an even
class. If full drift d=(a,b) satisfies 3b-a=0 modulo12, w(T) is constant on each
full-drift class. Therefore its FULL odd inventory O necessarily obeys

                         sum_(v in O) w(T_v) = b modulo4.

In particular, for actual full d=(3,1), the right side is1. This uses the
actual full drift, not a primitive divisor, and has no period, support-width
or multiplicity cap. The relevant incoming-axis sector must be respected;
one can translate the coordinate origin to this sector before applying it.

BLACK-first odd classes contribute-1 instead of+1 to the kinematic sum. They
must not be silently treated as WHITE outputs. The certificate includes a
literal prepared six-read factor RLRRLL, drift(3,1), with three initial BLACK
cells and its full final board. Its signed sum satisfies the identity; replacing
its BLACK-first signs by WHITE ones does not. Repeating it requires prelaid
BLACK classes indefinitely, so it is not a finite-seed controller.

## 3. The live middle-short family now forces c odd

The independently signed full-ownership reduction52f05a4c gives, specifically
for T6=NNNSS,T7=EEEWW atg8,

O={0,1,2,6,7,6c+1,6a+2,6a+4}, with2<=c<=a.

The five base weights sum to9. The three variable weights sum to
(2c+1)+(2a+3)+(2a+2). Thus

sum w(T) = 15+2c+4a = 3+2c modulo4.

The required value1 forces c ODD. Hence the remaining parameter range is

                         3 <= c <= a, with c odd.

This excludes every even-c member at once, including the independently rejected
O16 example a=c=2. Both upper geometries c=a and c<a remain open for allowed
odd c. No incompatibility between their orders has been presumed.

## 4. Relation to the weighted transfer, and controls

The identity was found by extending the exact four-port transfer to odd cells
and retaining K modulo4. The proof above is independent of that derivation:
only48 local state transitions and complete WHITE class alternation are needed.
Thus it does not depend on the3,109 open lower interfaces, a bounded enumeration
or an inferred bound on the voltage counter.

The retained general wake screen contains signed-residue, winding-mod-two and
quadratic-sign obstructions. The supplied O16 passes those but fails this law,
so those checks alone did not account for this particular obstruction. The
older all-multiplicity modulo-eight theorem concerns actual read multiplicities;
it is not silently substituted for this odd-inventory statement.

Literal controls include every turn word of lengths6,10,14, with respectively
2,30,420 heading-restoring paths of full displacement(3,1), as well as all48
local transitions. Geometric words need not be legal board histories and are
used only to test the kinematic identity.

A positive finite-support control is THREE standard104 periods, translated by
(1,0) to select the stated sector. Its actual full drift is(-6,-6), so
3b-a=-12; its36 complete WHITE odd classes have weighted sum2=-6 modulo4.
This is a repeated standard controller, not a new primitive one and not a
(3,1) front. Its full stable histories are checked independently of phase order.

## Artifacts and remaining scope

`certify_drift31_mod4_winding_cocycle.py` reconstructs the48-state proof table,
all literal controls, the prepared factor's full fields, and parameter controls.
`drift31_mod4_winding_cocycle_certificate.json` retains those exact data.
The all-parameter family conclusion follows from the displayed formula, not
sampling, including huge-parameter controls.

The other two short modes, all odd-c cases above, fronts without an actual
single-used F circle, and the finite-seed highway conjecture remain open.
