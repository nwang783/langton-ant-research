# A diameter-free cubic duration bound for D/C/V packet factors

Status: analytic strengthening submitted for independent audit. The underlying no-infinite-D/C/V-tail theorem and198-clause family are already signed. This bound does not import a global freshness assumption.

Consider a physically feasible factor of recurrent packets D, DC, V, VC, VCC with an actual M11 at every packet boundary. Let m be the number of black cells at its initial cut, so m>=5, and let p0 be its initial head. Distant unread initial debris is permitted. The diameter of that debris will not enter the bound.

## Deferred activation of initial residual tokens

Use the signed residual representation and the already certified tilted weights. For each rotated functional L_r(z)=L(R_r z), L(x,y)=x+3y, keep a max potential over the core and all currently present PRODUCED residual tokens. Do not include initial residual tokens until a packet first consumes them. The core's value at (p,h) is 2L_r(p)+a_(h+r), with a=(2,52,54,-8). A produced token q has value2L_r(q)+w_(producer,slot,heading+r).

Before a packet consuming an initial token, temporarily insert that token with weight I=60. This dominates every input requirement. A local input has coordinate q=p+R_h z. Its inserted value minus the current core value is

2L(R_(h+r)z)+60-a_(h+r).

The maximum of this expression, over every input of every recurrent packet and every heading, is exactly76, attained by z=(0,3) at effective heading0. Therefore one activation raises each potential by at most76. If two initial tokens are consumed at one packet, charging76 for each is conservative. The exact residual ledger removes their initial identities permanently; there are at most m-5 such activations in the entire factor.

After those insertions, every consumed token has the required lower-bound weight. The signed transfer relations and148 local inequalities imply that the packet cannot increase the potential. Thus, throughout the factor,

P_r <= 2L_r(p0)+54+76(m-5).

This is an upper bound, not an assertion that all produced tokens are fresh or all initial cells are nearby.

## A mass-controlled active box

Every output weight is at least-60. Hence every currently produced residual black cell satisfies

L_r(q-p0)<=57+38(m-5)=:B.

Exact literal prefix arithmetic gives max_(packet,heading,prefix)[2L(R_h prefix)-a_h]=36, so all intermediate head positions satisfy the sharper bound45+38(m-5). Core black cells satisfy34+38(m-5). Applying all four rotations supplies both signs of x+3y and-3x+y. Inverting these two forms yields

|x-p0_x|, |y-p0_y| <= 2B/5.

Set R=ceil(2B/5) and A=(2R+1)^2. Every visited cell, every produced black cell and every core cell lies in the square of integer radiusR aboutp0. Initial black cells outside it are never visited and remain unchanged; there are at mostm of them. Consequently the total black count at every macro cut is at mostm+A, although the full support need not be confined nearp0.

D changes black mass by0, C by3, and V by4. Let t=floor(A/3). At mostt macros of typeC orV can occur. Between them, D has fixed heading and displacement a quarter-rotation of(1,1), so a D-run has at most2R macros within the active square. There are at mostt+1 such runs. Therefore the factor has at most

2R(t+1)+t macros,
20R(t+1)+18t fine steps.

The second formula uses |D|=10, |C|=15, |V|=18. Since R is linear in m, this is an explicit O(m^3) duration bound independent of initial support diameter. It currently applies to context-complete recurrent packet factors; extending it to arbitrary finite D/C/V factors requires separately stated finite boundary trims.

Exact constants are generated in `derive_dcv_mass_only_bound.py/json`. The activation idea was supplied by the global chronology collaborator; the present proof explicitly accounts for untracked far debris and bounds total mass bym+A rather than incorrectly claiming that the entire initial support lies in the active square.
