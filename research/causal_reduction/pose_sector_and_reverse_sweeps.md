# Pose sector and exact time reversal

Status: elementary exact proof, independently audited, 22 October 2026. This is a necessary interface
constraint, not an obstruction to every shifted or modified recycling device.
Use headings N,E,S,W = 0,1,2,3 and e_h their unit displacement vectors.

## Invariant

For every ordinary ant trajectory,

    sigma(B,p,h) = x(p)+y(p)+h  (mod 2)

is constant. Each update changes heading by an odd amount and then moves one
unit, changing position parity by an odd amount too. Colors play no role.
Thus any proposed endcap must connect two poses with equal sigma, regardless
of its length or the finite board chosen to realize it.

## Exact reversing involution

Let F be the standard ant map on a full board/pose state. Define

    J(B,p,h) = (B,p-e_h,h+2).

Then J^2=id and J F J=F^{-1}. To check the second identity, set q=p-e_h and
let c be the current color at q. Applying J, then F, then J flips q and ends
at q with heading h+s(c), where s(white)=+1 and s(black)=-1. The predecessor
of (B,p,h) also flips q and has heading h-s(1-c)=h+s(c), exactly the same.

Crucially, sigma(J state)=sigma(state)+1. Hence an actual ant orbit can never
contain a state and its exact J-reversal, even with an arbitrarily long
intervening endcap. The ant map is reversible but the reversing involution
exchanges its two invariant pose sectors.

## Application to the proposed rail sweep

The first-principles analysis's exact sweep word

    A = RRLRRRRL

repeated n times, from (0,0,N) with black cells (2k+1,-1), 0<=k<n, ends at
(2n,0,N). Its output adds upper cells (x,0), 0<=x<2n, and lower cells
(x,-2), 1<=x<=2n, taking black mass n to 5n.

The reverse sweep word

    D = RLLLLRLL

repeated n times from (2n,-1,S) restores the seed while ending at (0,-1,S).
These are the J-transforms of the A endpoint and entry. The proposed direct
connection from A's endpoint to D's entry has sigma 0 to sigma 1. Therefore
NO ant endcap can connect those exact interfaces, even on a different board.
This is not just a failed finite search or a bound on endcap length.

Translating the reverse interface by a vector of odd coordinate sum repairs
the sector mismatch, but translates all of its required rail colors too.
It is necessary to recompute that bulk overlap rather than assume the same
reversible sweep can then be run. A phase shift or other modified sweep is
not excluded by the present observation.
