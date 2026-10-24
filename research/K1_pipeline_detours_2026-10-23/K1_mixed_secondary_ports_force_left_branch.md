# Mixed secondary-port chronology forces a LEFT maximum branch at K=1

23 October 2026, 18:40 UTC. New all-period conditional exclusion,
submitted for independent review. It concerns the canonical curve in
the leftmost maximum component, not general K1 fronts with branches.

## 1. Reduced branch-free geometry already signed

Suppose for contradiction that the canonical first-L Gamma in the
LEFTMOST maximum C component of a complete WHITE cap-four K=1 front
has no LEFT maximum branch. Put b=M-2.

The signed supplier arguments imply:

- every strict-LEFT C face has height <=b;
- Gamma's cyclic word consists of S tokens and R,L pairs;
- every RIGHT face is strict row4, every selected contact has LEFT L3;
- after rotation, outgoing face steps are NW for S and L, NE for R,
  so Gamma has exactly ONE physical C face at each of its consecutive
  vertical face coordinates and is globally monotone in that coordinate;
- S runs are nonempty somewhere, and the numbers of R and L are also
  nonzero. The all-S and all-RL cases were already excluded; alternatively
  use the signed five-S and no-(RL)^3 local exclusions in lifted windows.

Every nonempty S run is therefore preceded by an R,L pair. Thus some
consecutive faces have types R,L,S. We prove this is impossible using
the actual supplier of one secondary first R0; no bounded period scan
or count of original roots enters the argument.

## 2. The finite R,L,S normalization

Normalize these faces to

    F_R lower-left(0,0), F_L lower-left(1,1),
    F_S lower-left(0,2).

Write the selected contacts

    A=(1,0), B=(1,1), C=(1,2), D=(0,3).

The first face's strict row4 histories are

    Z=(0,0): W,W,W,E;
    Y=(0,1): N,N,N,S;
    A: N,N,S,N; B: E,E,W,E.

The straight face has entry C, exit D, and first helper

    Z_s=(0,2): W,W,W,E.

All these displayed histories are complete RLRL. Define secondary cells

    O=(-1,1), e=(-1,2), z=(-1,3),
    S_time=T1(Y)+1, F_time=T3(Z_s)-1.

O has exactly ONE W input, at S_time, from Y.L1. Cell e has exactly
ONE E output, at F_time, feeding Z_s.L3. The common incident C face of
O and e has lower-left(-1,1) and height b, forced by main row4.
Their other C faces have lower-left(-2,0) and(-2,2), respectively.

Both other faces are strictly LEFT and have height <=b. To spell out
the folded/seam point: they connect to the known LEFT b face through
O or e, neither of which can be a selected flat max/max contact unless
that known b face were maximum. Hence the contact path cannot cross
Gamma. They are not Gamma faces because their vertical coordinates
already have the distinct main maximum faces F_R or F_S, and Gamma is
monotone. The collar bound therefore applies.

The main chronology gives the strict future-output inequality

    S_time+1 < F_time.                                  (1)

Indeed Y.L1 precedes Y.R2 then B.L1; the LEFT face next sends B.L1 to
C.R0, well before C.L1 and the straight helper's final L3. No primitive
period or chosen quotient time is substituted for these physical times.

## 3. O forces an early N input at e

At O the NE C height is b and the SW height is <=b. Its unique W input
must be an R read:

- for SW<b every R selects NE and arrives W, making this unique W R0;
- for equality, opposite R headings are required, so the unique W input
  is R0 or R2 and every L arrives E.

In either case O has a first N output no later than S_time. Its first
arrival at e, with heading N, is therefore no later than S_time+1,
strictly before F_time by(1).

If e's NW C height were <b, every R at e would arrive N and the FIRST
N input would already emit its unique E output too early. Therefore
that NW C height is b. With both incident C heights b, its R headings
are opposite N/S. All L reads arrive N, because an L(S) would emit an
additional E output. The early first N arrival cannot be R0; hence the
complete e history is

    S,N,N[,N], with R0(S), L1(N), R2(N),

and its unique future E output is at R2(N). In particular its first
S input has the exact early deadline

    T0(e) < first_N_arrival(e) <= S_time+1.             (2)

This retains the real first R0 supplier; it is not an omitted initial
black read or a chosen secondary seed color.

## 4. The only supplier is a future strict-helper L1

The ONLY source of an incoming S at e=(-1,2) is its north neighbor
z=(-1,3). This z is the first LEFT corner of Gamma's next face after
the STRAIGHT F_S, whose lower-left is(-1,3) and whose entry is D=(0,3).
That next face cannot be LEFT by the signed S-to-LEFT exclusion. It is
S or RIGHT; in the reduced grammar RIGHT is row4. Both alternatives
therefore give the SAME complete first-helper history

    z: W,W,W,E.

Its only S output is L1, supplied by the entry contact D.R2. Thus

    T0(e)=T1(z)+1=T2(D)+2.                              (3)

But D is a later selected contact than C and B. Its R2 is later than
the main packet time S_time by the signed K1 chronology. In particular

    T2(D)+2 > S_time+1,

contradicting(2)-(3). A periodic secondary rail was not assumed; only
this finite R,L,S segment and its actual next first helper are used.

Consequently R,L,S is impossible under the branch-free hypotheses.

## 5. Conclusion and exact open case

Every nonempty S run in the reduced cyclic word has an R,L pair before
it, but no R,L,S can occur. The all-RL and all-S alternatives were
already excluded. This contradiction proves:

    The canonical first-L Gamma in the LEFTMOST maximum C component
    of a complete WHITE cap-four K=1 front has a LEFT maximum branch.

It does NOT prove that K1 is impossible. The branch is a real extra
maximum face in the SAME max component, not automatically a second
maximum component or a paid original-root resource. Its actual birth
parent, R0 suppliers and possible return to the canonical cycle remain
the next target. The later-R2 backbone and clock results stay valid as
conditional consequences of the now-excluded branch-free architecture;
no new general A/B/C existence statement is inferred for branched fronts.

Dependencies retained unchanged:
K1_straight_cannot_precede_left.md, SHA
ec007322c863fb61411511b006607196ddb52ad0dd9719f474287ebd909269dc;
K1_leftmost_branch_free_middle_collar_v2.md, SHA
313509cb42cf3cb2ceb8a395896665aaddc58032de65b0af6a392ca963c3e466;
K1_later_R2_essential_backbone_v2.md, SHA
2f4a3775bf747c6936ee532de1532ac2ae7ae26a722e65310529d8791654e61f;
K1_row5_ear_two_early_exits_obstruction.md, SHA
a95c476e7979ac0123c74474bc4228eea32650edc893a1ef6d15b37b21a12228;
K1_five_face_escape_density.md, SHA
4536aaf13af84af77f42cc046f02d4fd28bf9c180d112fee309fc29f0ff3a690.
