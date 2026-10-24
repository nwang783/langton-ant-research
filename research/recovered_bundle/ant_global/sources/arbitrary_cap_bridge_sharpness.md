# A sharp family for the old-color bridge terms

21 October 2026. This is an explicit actual-trajectory family for the
arbitrary-color cap theorem. It does not concern eventual highway capture.

## Construction

For each integer k>=1, start the ant at (0,-4), facing west. Let the only
initial black cells be

    B_1=(1,-3),
    B_(k+1)=(k+1,-k-3),
    A_r=(r,-1-r),  r=2,...,k+1.

There are exactly k+2 black cells. Every unspecified cell is white. The
entire trajectory through time 8+2k is the simple path

    (0,-4), C_0, B_1, A_1,
    T_2, A_2, T_3, A_3, ..., T_(k+1), A_(k+1),
    T_(k+2), A_(k+2), B_(k+1), C_(k+1), (k,-k-4).

Its turn word is

    RRLR (RL)^k RRLR.

The first and last four letters each change the heading by two quarter
turns. Every RL pair restores its heading. Thus the final heading is west.
The path stays at x+y<=0; its endpoints both have x+y=-4.

## Why the path holds for every k

The first four updates go north, east, north, east. They read, in order,
a white start cell, white C_0, black B_1, and white A_1. Each subsequent
RL pair reads a white T cell, then its prescribed black A bridge, and
moves south then east. The final four updates read white T_(k+2), white
A_(k+2), black B_(k+1), and white C_(k+1). Their directions are south,
west, south, west.

Every listed cell is distinct for k>=1. The two B endpoints are distinct.
Thus no previous write can change one of these prescribed read colors.
This is a direct proof for the whole integer family, not an extrapolation
from sampled k values.

## Exact statistics

There is one positive roof with k bridges. There are no black lower A
events and no white B upper corners. Therefore

    M=k+1,  H=k,  J_+=1,  rho=k-1,
    J_0=0,  E_B=0,  D_0=0,  D=k-1,
    Q=0,  K_C=0,  Z_0=0.

The row counts and signed black changes are

    N_A=k+2,  Delta_A=2-k,
    N_B=2,    Delta_B=-2,
    N_C=2,    Delta_C=2.

The leading expression in the new third-row identity equals

    12M-8Delta_A+4Delta_B-Delta_C = 20k-14.

The exact stronger bound subtracts

    4H+16rho = 4k+16(k-1) = 20k-16,

leaving N_C=2. Equality holds for every k>=1.

## Sharpness claim and its limit

With all other displayed coefficients fixed, the coefficient 4 on H
cannot be increased: k=1 has rho=D_0=Z_0=0 and equality. With that
coefficient fixed, the coefficient 16 on rho cannot be increased: k=2
has rho=1 and equality. These are coordinatewise sharpness statements
for the two new corrections. They do not assert uniqueness of every
possible weighted inequality or optimize other coefficients jointly.

`check_arbitrary_cap_bridge_sharpness.py` replays k=1 through 64 using
the independent coordinate-set implementation, checks the exact word,
endpoint and all stated counts, and retains the k=1 and k=2 event lists.
