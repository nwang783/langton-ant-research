# Zero-output early R ancestry fails at the lower physical square

23 October 2026. Complete WHITE cap-four translating history, actual full
period and drift. This is a finite physical port obstruction. Its local
statement uses no K1 order, no essential-cycle placement, no saturation
of the canonical flag graph and no iterated ancestry.

## 1. Exact retained early interface

Use the signed surviving early source-L3 ancestor inventory
`K1_surviving_cleanup_Q1_two_ancestor_profiles.md` (a7f57d46).
At zero odd output all complete cell histories have even length. Its
STRAIGHT ancestor mode contains the singleton R cell j=W and is therefore
excluded. The RIGHT mode has the following physical histories and maxima:

    P0=(-2,0), Q1=(-3,1), Q2=(-4,0), all at height M;
    j=(-3,1): EEWE;  k=(-3,2): NNNS;
    x=(-2,0): EWWW;  r=(-1,-1): WEWW.

The source inventory has 72 necessary rows. Filtering only for even
length at EVERY displayed physical cell leaves exactly two rows; both
have precisely these x,r,j histories. No choice of the exterior board or
of an off-Gamma event interleaving is made here. In particular r is at
(-1,-1), whereas the additional lower square corner below is at (-2,-1).
They are distinct physical cells.

The local obstruction below only needs the three complete histories
j,x,r, the maximum heights of P0,Q2, and the usual complete WHITE
maximum-face birth theorem. Thus any configuration with this exact local
interface is excluded at zero odd output, whether or not it arose from
the earlier K1 construction.

## 2. The missing lower face and its upper corner

Let F=(-3,-1) be the C face diagonally opposite P0 across x. The two R
headings of x=EWWW are opposite, so its two incident C heights agree.
Consequently h(F)=M.

The NW corner of F is d=(-3,0), whose opposite C face is Q2 at M. It is
therefore a flat maximum contact, with its R headings N and S in either
order. The physical edge from j down to d carries exactly one S arrival
at d: j=EEWE has exactly one S departure. The physical edge from d right
to x carries exactly one E departure at d: x=EWWW has exactly one E
arrival. The unique S arrival is one of d's two opposite R reads; all its
L arrivals are N. Zero odd output then gives exactly

    d=NNSN or d=SNNN.

This deduction keeps all four reads, including L3. It does not discard a
same-face supplier or impose a desired order on the two R reads.

## 3. Complete even canonical completion of F

Write the corners of F in physical coordinates:

    SW a=(-3,-1), NW d=(-3,0), NE x=(-2,0), SE t=(-2,-1).

Every global maximum C face has a genuine canonical first-boundary
minimum at a negative flat L1 contact. The complete signed canonical
one-face inventory contains 110 necessary profiles. Exactly 24 have
even length at all four corners. Test all four rotations of all 24;
match the COMPLETE NW history d and NE history x=EWWW. This retains
exactly the following two possibilities:

    SW a    NW d   NE x   SE t
    EEWE    NNSN   EWWW   SSNS
    EEWE    NNSN   EWWW   NSSS.

There is no completion with d=SNNN. Both displayed completions have the
canonical birth at a. This is an exhaustive necessary completion, not a
claim that either row has an exterior realization. Incoming canonical
flag-zero profiles are included in the 24 even profiles; no global
flag-one assumption has been used.

Finally, t=SSNS and t=NSSS each emit exactly THREE E departures. These
are physical traversals of the same edge from t=(-2,-1) to
r=(-1,-1). But the complete history r=WEWW has exactly ONE E arrival.
Physical edge incidence counts must agree over the complete history.
The required equality 3=1 is impossible.

## 4. Scope and check

The displayed local early R interface cannot occur when Nodd=0.
Together with the signed early zero-L3 supplier exclusions and the
signed two-ancestor classification, the surviving EARLY branch family
has no zero-output realization. This is not an exclusion of every main
K1 branch: identifying all other supplier cases with the exact late D4
route would require its own proof. No new original-fuel charge or
per-branch output injection follows.

Control `zero_output_early_R_ancestor_cross_port_obstruction.py/json`
uses the complete signed canonical inventory, all rotations, and the
signed 72-row ancestor inventory. Counts: 24 even canonical profiles;
72 prior rows, two all-even; two NNSN completions, zero SNNN completions,
zero physical-port survivors. It performs no period, drift, radius or
multiplicity scan.
