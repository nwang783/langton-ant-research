# Two early exits exclude the same-Gamma row-5 return at K=1

23 October 2026, 18:02 UTC. New actual-cursor obstruction, submitted for
independent review. This is a local incompatibility, not a K=1 exclusion.
It does not use a graph-excess upper bound or discard lower sheet nodes.

## 1. Exact configuration and scope

Use a complete WHITE cap-four translating front with actual full P,d,
canonical first-L circle Gamma, and K=1. Suppose the conditional
same-Gamma row-5 return from the signed local theorem occurs:

    main RIGHT row-4 face F, lower-left (0,0);
    return RIGHT row-5 face H, lower-left (-2,0);
    Z=(0,0): W,W,W,E; Y=(0,1): N,N,N,S;
    O=(-1,1): E,E,E,W; E=(-1,0): S,N,S,S.

All four are complete RLRL histories. The return's selected exit is
B'=(-2,0); the main entry is A_main=(1,0). Both return selected contacts
have LEFT L3, as forced by the signed local classification. No further
LEFT-branch-free or leftmost assumption is needed for THIS obstruction.
Optional L3 elsewhere, arbitrary detours and both side currents remain.

Let v_j=B' in the lifted selected-contact order. Put t=T2(O). The signed
actual row-5 corridor gives consecutive reads

    O.R2 at t -> E.R2 at t+1 -> v_j.L3 at t+2.

Thus same-cell return spacing implies

    T2(v_j) <= t-2.                                    (1)

The exact K=1 crossing pipeline gives

    T0(v_j) < T0(v_(j+1)) < T2(v_j).                    (2)

These are physical actual times, not quotient representatives. Long
return spans and nonprimitive full periods have not been reduced.

## 2. The bounded physical ear and its complete crossing list

Join H's and F's C centers by the short horizontal LEFT chord chi at
y=1/2. Its interior lies LEFT of Gamma and meets only the physical
vertical edges O-E and Z-Y. The signed row-5 chronology places H before
F in the positive physical Gamma order. That finite Gamma arc, followed
by chi from F to H, is a simple closed curve bounding a bounded LEFT
Jordan disk Omega. This is the same physical ear as in the signed ear
separator proof; its existence does not use uniqueness of a middle node.
The local downward orientation at H and upward orientation at F fix the
interior as the region below chi and LEFT of the forward Gamma arc.

The selected contacts on this boundary form one consecutive lifted
interval starting at v_j. It includes v_(j+1): H and F differ by(2,0),
so they are NOT C-contact neighbors (whose displacement is (+/-1,+/-1)).
Even the shortest possible H-to-F arc therefore has at least two
selected contacts. No short-quotient identification changes that
physical displacement fact.

The COMPLETE actual crossing list is:

- at a selected contact in this interval, R0 exits Omega from LEFT to
  RIGHT and R2 enters it from RIGHT to LEFT; L1 and optional L3 stay on
  their own side;
- on chi, O.R0, O.R2 and O.L3 go S through O-E and ENTER Omega;
- on chi, Z.R0, Z.R2 and Z.L3 go N through Z-Y and EXIT Omega.

There are no other crossings. Gamma runs through C-face interiors and
selected primal vertices, not through other physical edges; chi has
only the two displayed primal-edge intersections. The finite-transverse
front and nonzero drift put the cursor outside this bounded physical
disk for all sufficiently negative and sufficiently positive times.

## 3. Two exits before any second entry

The K=1 pipeline orders R2_k increasingly with k. Hence the earliest
possible Gamma entry into this ear is R2_j. By (1)-(2), the two Gamma
exits R0_j and R0_(j+1) both occur BEFORE that first Gamma entry, and both
occur BEFORE t=T2(O).

But among the three chord entries, only O.R0 can occur before t. O.R2
is at t itself, and O.L3 is later still. Therefore, by the time of the
second exit R0_(j+1), there have been at least TWO exits and at most ONE
entry into Omega. Extra chord exits from Z only worsen this imbalance.

A single continuous cursor, initially outside a bounded disk, has
alternating entry and exit events. It cannot have more exits than
entries in any time prefix. This is the contradiction.

Consequently the stated same-Gamma row-5 supply configuration is
IMPOSSIBLE for K=1. The argument retains the actual preceding R reads
of O,E and the actual return L3 at B'; replacing those reads by prepared
black singleton L inputs removes precisely the chronology used in(1).

## 4. Consequences and limits

This rules out this particular local old-L3 renewal, rather than paying
for it with a handle or an essential lower-sheet pair. The earlier
nonbridge and additive cycle-rank conclusions remain valid conditional
statements, but their common exact return configuration cannot occur
under the stronger actual-cursor test above.

In the signed leftmost branch-free case, the finite three-packet theorem
would force exactly such a return from (R,L)^3. Therefore that six-face
word is impossible there. If s is the number of straight faces and ell
the total number of Gamma faces, the same all-length symbolic count
improves to

    s >= ceil(ell/17).

Indeed let m=#R=#L, q=m-#RL<=2s and a<=s+q be the number of maximal
RL-pair runs, as proved in the signed density note. Every such run now
has length at most TWO, so #RL<=2a. Thus

    m<=q+2a<=3q+2s<=8s, ell=2m+s<=17s.

Every counted straight face still has its genuine actual rank3-to-rank1
gate, not a fresh input or permanent bud. LEFT maximum branches, other
strict straight-gate detours, other old-stock suppliers and general
K>=2 behavior are not excluded. There is no global capture, K>=2 or
finite-seed fuel theorem here.

Sources retained unchanged:
K1_secondary_return_strand_row5.md, SHA
a46d61d8a2b88f9f8ba8525bf8c1d4d58a1a122c04e443be3e7c968721909e46;
K1_row5_return_ear_forces_nonbridge.md, SHA
25aca7954d9658cceecd179393dee27226801c6bac4b1aea6711fc3538b60cd9;
K1_three_packet_return_and_straight_density.md, SHA
24dc6f859cc6df9095465757eab2f9eadf5321492ffca88f924785c1554de838;
K1_leftmost_branch_free_middle_collar_v2.md, SHA
313509cb42cf3cb2ceb8a395896665aaddc58032de65b0af6a392ca963c3e466;
rank_two_plateau_2026-10-23/cursor_stream_height_and_K1_pipeline.md,
SHA 2e9400915fcc0a571b4effd209f04a8dfd4a0043b7f4c1a80e9f6e2ae5216c35.
