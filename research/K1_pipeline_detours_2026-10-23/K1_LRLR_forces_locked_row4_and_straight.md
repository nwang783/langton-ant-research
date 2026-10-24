# A branchful LRLR block locks row 4; a leftmost K1 curve needs a straight face

23 October 2026, 20:00 UTC. New exact branchful overlap theorem, submitted
for independent review. Complete WHITE cap-four front, actual full P,d,
canonical max-face first-L Gamma, K=1. Branches are not assumed absent.

## 1. Any LEFT/RIGHT pair has lower q with R0 incoming N

Normalize a LEFT followed by RIGHT with selected contacts

    C=(1,-1): EEW[,E or W],
    A=(1,0): NNS[,N or S],
    B=(1,1): EEW[,E or W].

The RIGHT helpers are Z=(0,0), Y=(0,1); q=(0,-1) is the lower supplier.
Its other LEFT C faces are G=(-1,-1), H=(-1,1), each initially at most M.
Let s_A,s_B be the selected LEFT-L3 bits. LEFT transport gives s_C=s_A.

If s_A=0, the signed launch theorem and canonical EEWW gate leave

    Z=EWW, Y=SSN or SSNS, q=NSS or NSSN;
    Z=EWWE, Y=SSNN,       q=NSS or NSSN.

Hence q.R0 arrives N and Y.R0 arrives S in every state-zero case.

Now suppose s_A=1. Then C=EEWE and A=NNSN. A has THREE W outputs
into Z; C has THREE E inputs from q.

### 1a. G cannot be maximum in this state

If G=M, Z is flat with three W inputs, so exactly Z=WWEW or EWWW.
Both have THREE S outputs into q. Since q is flat between G and the
preceding max face, three S inputs and three E outputs force q=NSSS
or SSNS.

For Z=WWEW its first S output is L1, supplied by A.R2, so q's first S
input is T2(A)+2. Either permitted q profile emits its second E no
earlier than this. But that output must supply C.L1 one step later,
while T1(C)<T1(A)<T2(A). Contradiction.

For Z=EWWW, its second S output is L1, supplied by A.L1. If q=SSNS,
q.L1 is its second S input at T1(A)+2 and its first E output, placing
C.R0 after T1(A), impossible. If q=NSSS, q.L3 is its third S input,
supplied by Z.L3 one step earlier; Z.L3 is itself supplied by A.L3.
The third E output then feeds C.L3, which feeds A.L3 along the LEFT
one-edge arc. This would give the impossible actual-time cycle

    A.L3 -> Z.L3 -> q.L3 -> C.L3 -> A.L3.

Thus G is strict, without discarding either possible equal-height source.

### 1b. The strict cleanup reduces the remaining whole histories

The signed strict gate after LEFT theorem applies, retaining either
height at H. It gives

    q=NNNS, Z=WWW or WWWE, G=M-2,
    T3(A)=T2(A)+4, T2(Z)=T2(A)+5.                 (1)

Combining complete counts at Y with the K1 order leaves precisely

    s_A s_B   Z       Y       q        G,H
      1   0   WWW     NNSS    NNNS     M-2,M
      1   0   WWWE    NNN     NNNS     M-2,M-2
      1   1   WWWE    NNNS    NNNS     M-2,M-2.

For clarity, the other strict-G right-turn candidates NSN, NSNN and
NSSN at Y are not silently omitted. Their first N input comes from
Z.R0 at T1(A)+1, so Y.R0=T1(A)+2, B.R0=T1(A)+3 and
T2(A)=T1(A)+4. Equation (1) then puts the next N input from Z.R2 at
T1(A)+10. For Y=NSN or NSNN that is Y.R2 and its third E departure,
feeding B.L3. But B.L1 is no earlier than T1(A)+7, so its rank1-to-rank3
gap would be at most4 instead of at least8. For Y=NSSN it is Y.L3,
only8 after Y.R0 instead of at least12. Each is impossible.

In particular q.R0 arrives N in EVERY LEFT/RIGHT pair, for either input
state and either output state, with all optional RIGHT L3 retained.

## 2. Two consecutive LR pairs force the first RIGHT to locked row 4

Suppose four consecutive faces are LEFT,RIGHT,LEFT,RIGHT. Their five
contacts can be taken as C,A,B,D=(1,2),E=(1,3). The first pair's upper
helper is Y=(0,1). The second pair's lower supplier is EXACTLY that same
physical cell q'=(0,1).

Section 1 says q' must be NSS, NSSN or NNNS. If the first input state
were0, its Y.R0 would arrive S, contradicting q'.R0 arriving N.
Thus the first input is1. Its only Y alternatives are NNSS, NNN, NNNS
from the displayed strict table. Their intersection with the q' list is
ONLY NNNS. Consequently the first RIGHT face is exactly locked row4:

    A=NNSN, Z=WWWE, Y=NNNS, B=EEWE,
    both unused LEFT other C heights M-2.

This also forces the first output state, and therefore D's input state,
to1. The theorem is an exact literal-history overlap, not a phase-only
identification. No leftmost or no-branch premise was used.

## 3. Every all-bend K1 curve is the strict locked rail

The signed all-K no-LL theorem forbids adjacent LEFT turns. A simple
essential diagonal contact-lattice circle has zero total signed turn.
If every face bends, LEFT and RIGHT counts are equal, so no LL forces
exact cyclic alternation. Every RIGHT then occurs in a lifted LRLR
window, including small full quotients. Section 2 locks every RIGHT to
row4 and all selected bits to1.

After rotation the contacts are (1,k), and the complete main histories
are the old strict locked rail

    Z_k=(0,2k): WWWE, Y_k=(0,2k+1): NNNS,
    A_k=(1,2k): NNSN, B_k=(1,2k+1): EEWE.

Both unused LEFT C neighbors at every RIGHT face have height M-2.
These give the whole unused LEFT collar: a LEFT face contributes no
additional unused LEFT corner. Thus an all-bend Gamma has no LEFT max
branch, even though branches were initially allowed throughout.

For Gamma chosen in the LEFTMOST max component, the independently signed
branch-free exclusion b3eb2630 now applies. Therefore such a Gamma
CANNOT BE ALL-BEND: it must contain a STRAIGHT face.

Combined with the signed necessity of a LEFT max branch, the leftmost
K1 Gamma must contain BOTH a straight face AND a LEFT max branch, not
merely one or the other. They need not be at the same face; the straight
may be strict, and no original-root or fuel payment follows. This is
not a general K1, all-cap front or finite-seed exclusion.

## Dependencies and exact finite control

max_face_birth_curve_no_two_LEFT_turns.md SHA
a93dabfc34aecede83ef23fb81cb7899e3b2c774fbdb489a018bab5768fef20d;
max_face_first_corner_EEWW_birth_gate.md SHA
34d2f54cf194ba866fb00fe4e4769366b96e4a345914ddc03d6354186294994f;
K1_zero_state_left_right_launch.md SHA
8fb5af1921bdad6dcb20b618d17e0c5e0d088a2a54c565684781477f9371feeb;
K1_zero_left_right_two_max_launches.md SHA
8cfac7cf84007c000812736c7d5fe554b10fef28430869fa4730d710521e9162;
K1_left_turn_four_L_cleanup.md SHA
bb166fa7646904ba293dffb6e6b1023bea8c61b039f3f8c7d32b70dde121a5a1;
K1_mixed_secondary_ports_force_left_branch.md SHA
b3eb263017c903b1adfa6e0e3c988438e6669aa1ee25952de48c831e9b3bd1c9.

LR_pair_all_states_complete_ports.py/json closes the complete C/q ports
around the existing necessary RIGHT inventories, retains ALL three
selected L3 states and either strict/equal outside face, and uses only
actual ordinal edges, local return gaps, K1 order and canonical boundary
minimum. It retains23 necessary rows (20 state-zero and the three
state-one rows above). No period, drift, radius or exterior front scan.
The analytic common-physical-cell overlap proves the unbounded theorem.
