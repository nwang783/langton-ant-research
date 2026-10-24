# RRLL flow-two departure circles force disconnected actual events

24 October 2026. Complete WHITE cap-four translating front, actual full
period P and nonzero drift d. The map b chooses the neighbor reached by
FIRST R departure. Physical flow is TOTAL edge use, not a threshold-sheet
copy. Author proof, pending independent audit.

THEOREM. A b-cycle whose every edge has physical multiplicity two cannot
have cyclic geometric turn word (RRLL)^a. No global-maximum C assumption
is needed beyond the signed constant-selected-C rule for an actual
b-cycle. This excludes one whole segment geometry, not every multiply
used departure cycle or every complete cap-four front.

The obstruction is a complete partition of ACTUAL read events, not a
repaired-sheet genus bound. All L1/L3 suppliers and every exterior port
are retained. Finite RRLL segments can still communicate around their
endpoints and are not excluded by this theorem.

## 1. Exact lifted strip and complete alphabet

Rotate and translate the lift so its physical b path is

    Z_k -> A_k -> B_(k-1) -> Y_(k-1) -> Z_(k-1),

where

    Z_k=(0,2k), A_k=(1,2k), B_k=(1,2k+1), Y_k=(0,2k+1).

The turns at Z,A,B,Y are LEFT, RIGHT, RIGHT, LEFT. The signed first-R
rule makes the selected clockwise C height constant on an actual
b-cycle. Thus LEFT corners have opposite R0/R2 headings. Together with
complete WHITE histories of at most four reads and cycle-port flow two,
the full local alphabets are

    Z: NSS, NNSS, NSSN;   A: EEWW, EWWE;
    B: SNNS, SSNN;       Y: EWW, EEWW, EWWE.

Odd three-read LEFT modes are included at this stage. A heading word
lists chronological incoming headings; even ranks are R, odd ranks L.
The actual b arrival at a LEFT corner need not be its R0 arrival.

A full RRLL b-cycle with 4a classes has lifted displacement (0,-2a).
The signed first-departure winding is -1, so the ACTUAL full drift is

    d=(0,2a), a>=1.

Consequently the entire two-column strip x=0,1 consists of the listed
physical cells, with the complete histories repeated under this full
drift. This is not an induction based merely on westward spatial order.

## 2. The physical C-square forces both LEFT profiles

Let F_k be the physical unit square with corners

    Z_k, A_k, B_(k-1), Y_(k-1).

Its directed boundary is E,S,W,N. Use the FIRST physical occurrence of
each boundary edge and match its outgoing/incoming ordinal exactly.
This is a closed clock telescoping identity, not an uninterrupted ant
factor or an assumed b subcycle. At Z,A,B the matched incoming/outgoing
rank is the same. At Y it is

    incoming L1 -> outgoing R2  for EWW or EWWE,
    incoming R2 -> outgoing L1  for EEWW.

Hence the exact physical-time identity is respectively

    0 = 4 + (T2(Y)-T1(Y)),
    0 = 4 - (T2(Y)-T1(Y)).

Only Y=EEWW survives, with T2(Y)-T1(Y)=4. It emits N at ranks1,2, so
the recipient Z has two N arrivals and is four-read. If Z=NSSN those
arrivals are ranks0,3, forcing T3(Z)-T0(Z)=4, contrary to the minimum
three same-cell return gaps, each at least four. Therefore

    Y=EEWW, Z=NNSS, T1(Z)-T0(Z)=4.

This argument is pointwise in k. It does not assume that A/B modes were
already homogeneous and makes no global height or period cutoff.

## 3. The physical L-square forces both RIGHT profiles

Let Q_k have corners Z_k,A_k,B_k,Y_k, directed E,N,W,S. Match the SECOND
physical occurrence of every edge. The now-forced Z/Y profiles have no
rank switch at that ordinal. A=EEWW contributes +Delta12(A), A=EWWE
contributes zero; B=SNNS contributes -Delta12(B), B=SSNN contributes
zero. Thus

    0 = 4 + 1{A=EEWW} Delta12(A) - 1{B=SNNS} Delta12(B).

It follows that B=SNNS. If A=EEWW, its two N departures at ranks1,2 feed
B's N arrivals at ranks1,2, forcing Delta12(A)=Delta12(B). The displayed
identity would then say 0=4. Therefore A=EWWE, and all roles are forced:

    Z=NNSS, A=EWWE, B=SNNS, Y=EEWW.

Also Delta12(B)=Delta23(A)=4. The executable local control rebuilds all
20 port-compatible F-square rows and four Q-square rows directly from
complete histories. It does not claim that the remaining necessary
four-profile strip has an exterior completion.

## 4. Every actual event preserves a two-sided label

Label complete ranks0,1,2,3 as follows:

    Z: WEST,WEST,WEST,EAST;
    A: WEST,EAST,EAST,EAST;
    B: WEST,EAST,EAST,EAST;
    Y: WEST,WEST,WEST,EAST.

Every physical ordinal edge whose endpoints are in the strip preserves
this label. The full list, with k unrestricted, is

    Z_k.0 -> A_k.0,       Z_k.3 -> A_k.3;
    A_k.0 -> B_(k-1).0,   A_k.1 -> B_(k-1).3;
    A_k.2 -> B_k.1,       A_k.3 -> B_k.2;
    B_k.0 -> Y_k.2,       B_k.1 -> Y_k.3;
    Y_k.0 -> Z_k.2,       Y_k.3 -> Z_k.3;
    Y_k.1 -> Z_(k+1).0,   Y_k.2 -> Z_(k+1).1.

These are actual consecutive read events across the respective edges,
not repaired-sheet connections. This accounts for every internal use.
All remaining ports are precisely

    WEST ingress: Y incoming E at ranks0,1;
    WEST egress:  Z outgoing W at ranks1,2;
    EAST ingress: A incoming W at ranks1,2;
    EAST egress:  B outgoing E at ranks2,3.

Assign every event at x<=-1 to WEST and every event at x>=2 to EAST.
The displayed open ports preserve those labels too. Thus unknown
exterior histories, arbitrary repeated visits, passive tracks and other
contours cannot transport the actual cursor between the labels: any
physical path from one halfplane to the other must meet a strip cell,
and every one of its complete read events has already been accounted
for. There are no unused strip ranks through which to cross.

For an additional literal check, the four complete ingress-to-egress
channels have lengths3,7 on each side. With k fixed they are

    WEST: Y_k.0 -> Z_k.2;
    WEST: Y_k.1 -> Z_(k+1).0 -> A_(k+1).0 -> B_k.0
          -> Y_k.2 -> Z_(k+1).1;
    EAST: A_k.1 -> B_(k-1).3;
    EAST: A_k.2 -> B_k.1 -> Y_k.3 -> Z_k.3 -> A_k.3 -> B_k.2.

Lengths include the exterior ingress and egress physical steps. These
channels confirm that even the late L3 supply stays on its own side.

## 5. Full-quotient contradiction and precise scope

The full vertical drift d preserves WEST/EAST, including the rank labels
on the strip. Therefore both labels descend to well-defined nonempty
sets of the ACTUAL P-event quotient. Each set is closed under the actual
next-event permutation sigma. But sigma is one P-cycle for a complete
translating front, so it has no such partition. Contradiction.

This reasoning handles a=1 and all short quotients by keeping physical
lifts until the last step. Distinct roles cannot alias under vertical
translation by (0,2a), and all edges have their exact physical ordinal
matching. There is no primitivity shortcut, unsupported no-crossing
assumption, genus upper bound, or physical deletion/splice.

The theorem does not exclude mixed staircase/RRLL geometries, flow-two
pieces joined through multiplicity changes, odd source/sink stock paths,
or finite segments whose exterior can go around an end. General
single-use behavior of cap-four first-departure cycles remains open.
