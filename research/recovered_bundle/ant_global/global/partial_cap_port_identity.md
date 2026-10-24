# Exact endpoint terms for a capped prefix

## Scope

This is an exact algebraic companion to `../boundary/arbitrary_cap_third_row.md`. It applies to a finite prefix starting at height x+y<=-4. No processed event exits above T, the row x+y=0. The endpoint is the current, unprocessed ant pose. All initial colors are arbitrary. The heading sector is horizontal arrivals at T and B, vertical arrivals at A and C.

Use the same M, H, Q, E_B, K_C, Delta_X, D and Z as the boundary note, with all counts restricted to processed events:

`D=E_B-M+2H`, `Z=K_C+2D+H-Q`.

For the endpoint let t=x+y. Define

- u=1{t=0};
- a=1{t=-1 and heading S};
- v=1{t=-1};
- b=1{t=-2 and heading W};
- w=1{t=-2};
- c=1{t=-3 and heading S}.

Then the following identities are exact:

`Q=2M+u-a-Delta_A-3H`,

`N_A=4M+2u-2a-Delta_A-4H`,

`N_B=8M-4Delta_A+Delta_B-8H-4D+6u-8a+2v-2b`,

`N_C=12M-8Delta_A+4Delta_B-Delta_C-8D-4Z+epsilon`,

where

`epsilon=14u-20a+6v-8b+2w-2c`.

## Endpoint table

| Endpoint | Incoming heading | epsilon |
|---|---|---:|
| T | E | 14 |
| A | N | 6 |
| A | S | -14 |
| B | E | 2 |
| B | W | -6 |
| C | N | 0 |
| C | S | -2 |
| below C | either allowed heading | 0 |

This table is an identity, not by itself an inequality: D and Z can be negative when the prefix ends inside a roof or an upper excursion.

## Proof

Write U_j and V_j for upward and downward crossings of the cut between levels j and j+1. The finite path starts below all three cuts of interest, so

`U_j-V_j=1{t>j}`.

Each processed top event descends to A. The endpoint can be one extra unprocessed top arrival. Thus A has `2M+u-a` processed upper ports. The subtraction a is essential: an endpoint at A arriving S is not a processed A event. At A each white event uses one upper port and each H event uses two. This proves Q and N_A.

The number of A-to-B crossings is `N_A-M-u`. The number of B-to-A crossings differs from it by `u+v`. One must subtract b from their sum to remove an unprocessed B upper arrival. Thus B has

`2N_A-2M-u+v-b`

processed upper ports. A black B event uses one, a white upper corner uses two, and a white lower corner uses zero. This gives

`N_B=4N_A-4M-2u+2v-2b-4E_B+Delta_B`.

Substitution gives the displayed N_B identity.

In the same manner C has

`2(N_B-N_A+M)+u-v+w-c`

processed upper ports. A white C event uses one and a black upper C corner uses two. Therefore

`N_C=4(N_B-N_A+M)+2u-2v+2w-2c-4K_C-Delta_C`.

Substitution of N_A, N_B, Q and the definition of Z gives epsilon. This proof is independent of the charging argument in the boundary note.

## Exact numerical audit and proved bounds

`partial_caps.py` simulates 40,000 arbitrary-color starts and checks this identity at every capped prefix before its first exit above T. It checks 5,870,233 endpoint states. Every check passes. The test uses a fixed random seed and retains the extremal examples in `partial_caps.json`.

Observed endpoint maxima of

`F=N_C-(12M-8Delta_A+4Delta_B-Delta_C)`

are 14 at T,E; 6 at A,N; 2 at A,S; 2 at B,E; 10 at B,W; 0 at C,N; 2 at C,S; and 0 below C. These values agree with the open-roof charge proof now written in `../boundary/capped_prefix_charge_bound.md`. The simulation is only an audit; that separate mathematical argument proves the inequalities.

In particular the proved universal capped-prefix inequality is

`N_C <= 12M-8Delta_A+4Delta_B-Delta_C+14`.

The endpoint T before the first black top read has D,Z>=0 by the completed-roof/unmarked-event argument, giving this bound directly from epsilon=14. This is the endpoint needed at a new record.

## Why this is not global capture

The theorem applies to nested prefixes at successive fresh even records. It removes the assumption that a trajectory must return below C before the next record. However, each larger cap changes the physical rows counted by Delta_A, Delta_B and Delta_C. A term on the old T becomes a term on the new B. The formulas are not a single telescoping sum on fixed rows.

The local increasing expression is `12 b_T-8 b_A+4 b_B-b_C`. Under a cap shift by two its coefficients on the former top two rows change from `(12,-8)` to `(4,-1)`. The ratios are 3 and 8, so a uniform scalar rescaling does not preserve this two-row expression. The later argument in `fresh_a_cap_shift_inequality.md` supplies a nontrivial comparison for completed caps with A initially white. One must still establish the corresponding comparison for an unfinished record tail and control the old-row terms over successive cap shifts.

The old black sponsor is restored by a record-creation diamond, as shown in `record_birth.md`. Thus the endpoint allowance and the old-row terms cannot be paid from a decreasing count of initially black sponsors.

## A sharp fresh-record witness for the constant 14

Start at `(0,-4)`, heading W, with exactly the two black cells

`{(1,-3),(0,-2)}`.

After twelve updates the ant is at `(2,-2)`, heading E, on a black top cell. This is the unprocessed second top visit immediately before the first exit above T. The entire prefix stays at or below T, and T and A were both initially white.

Its counts are

`M=1`, `(N_A,N_B,N_C)=(4,4,2)`,

`(Delta_A,Delta_B,Delta_C)=(2,-2,0)`,

`H=D=Z=0`, `Q=K_C=1`.

Thus

`N_C=2=12-16-8+14`.

The constant 14 cannot be decreased with the other displayed coefficients fixed, even for a fresh-record prefix with two initially black cells. The exact twelve events are retained in `partial_cap_sharp_witness.json`.
