# A branch-free K=1 right/left pair forces the row-4 gate

23 October 2026, 15:55 UTC. Analytic local chronology extension, pending
independent review. No paid bend resource or general exclusion is claimed.

## 1. Hypotheses and exact local geometry

Use a complete WHITE cap-four K=1 first-L curve Gamma. Assume it has no
LEFT max branch at any face: every unused LEFT C-contact neighbor is
strictly below M. The signed branch-or-rank3 theorem then gives a LEFT
L3 at every selected contact.

Suppose a RIGHT face is immediately followed by a LEFT face. Normalize
these consecutive C faces and selected contacts as follows:

    F0 lower-left (0,0), RIGHT;
    F1 lower-left (1,1), LEFT;
    F2 lower-left (0,2), type initially arbitrary;

    A=(1,0), prefix N,N,S and LEFT L3(N);
    B=(1,1), prefix E,E,W and LEFT L3(E);
    C=(1,2), prefix N,N,S and LEFT L3(N).

Here A is F0's entry, B its exit and F1's entry, and C is F1's exit and
F2's entry. Put Z=(0,0), Y=(0,1), and U=(0,2). U lies immediately north
of Y and immediately west of C. The selected L1 order gives

    T1(A)<T1(B)<T1(C).

The LEFT turn F1 gives the actual one-edge passages B.L1 -> C.R0 and
B.L3 -> C.L3. Arbitrary intervening side excursions are otherwise kept.

## 2. U has no read early enough to supply Y's proposed early S arrival

For any of the three possible types of F2,

    T0(U)=T1(C)+1, and U.R0 arrives W.

- If F2 is LEFT, U is its next selected contact. The literal LEFT
  one-edge passage C.L1 -> U.R0 gives the assertion directly.
- If F2 is STRAIGHT or RIGHT, U is its first LEFT helper. Its other C
  face is strict by the no-LEFT-branch hypothesis. Therefore every R at
  U arrives W and chooses F2. The first W output of C is its L1; all
  later W outputs are R2 and LEFT L3. Hence U's first W input is its
  R0, supplied exactly by C.L1.

In particular U cannot emit S, or anything else, before T1(C)+1.

## 3. Rows 2 and 5 are chronologically impossible here

The independently signed strict-right table has only rows 2, 4 and 5
when both entry and exit have LEFT L3. Rows 2 and 5 give

    Y: RLR or RLRL, incoming N,S,N[,N].

Its three E outputs target B.R0, B.L1 and B.L3 in exact order. Therefore
Y's L1(S) would have to depart E at T1(B)-1. That S arrival must be
supplied from U by an S departure at T1(B)-2.

But Section 2 puts U's very first read at T1(C)+1>T1(B). This is a
strict actual-time contradiction, not a port-count overapproximation.
Rows 2 and 5 are therefore impossible for this RIGHT/LEFT pair.

Only row 4 remains:

    Z: RLRL, incoming W,W,W,E;
    Y: RLRL, incoming N,N,N,S;
    A: RLRL, incoming N,N,S,N;
    B: RLRL, incoming E,E,W,E.

Thus every such pair is a genuine rank3-to-rank1 gate, not one of the
uninterrupted row-2/row-5 L3 corridors. Its actual consecutive fragments
are exactly

    A.L3 -> Z.R2 -> Y.L1,
    Z.L3 -> Y.R2 -> B.L1,
    Y.L3 -> B.L3 -> C.L3.

The outgoing Y.L1 and incoming Z.L3 are the exterior LEFT packet ports;
their suppliers and arbitrary deep detours remain unclassified.

## 4. The next face cannot also be LEFT

Row 4 gives Y exactly ONE S arrival, namely L3. Therefore U has exactly
ONE S departure in its complete history.

If F2 were LEFT, U would be its selected exit contact with complete
incoming history W,W,E,W: the final W is its forced LEFT L3. Its outputs
would be N,S,S,S, giving THREE S departures into Y. This contradicts
Y's exact one-S input count. Hence

    RIGHT, LEFT, LEFT cannot occur consecutively

under the stated no-LEFT-max-branch hypothesis. F2 must be STRAIGHT or
RIGHT. Its first LEFT helper U is then strict. The signed four-L cleanup
theorem applies to the middle LEFT face and in particular forces U's
complete one-S-output history W,W,W,E:

    U.L1 -> Y.L3 -> B.L3 -> C.L3 -> U.R2

are four actual consecutive L turns. This is old stock, not a fresh
branch or permanent fuel payment.

## 5. Scope

The result narrows actual branch-free K=1 itineraries through a RIGHT/
LEFT pair and retains the explicit deep packet. It does not forbid
consecutive LEFT turns preceded by some other geometry, imply that all
bends alternate, or construct or exclude a white connector for row 4.
It uses neither a finite factor scan nor a primitive-period shortcut.

Sources: strict_left_K1_right_turn_table.md, SHA
63c41e1359c39e52f2f864d9ec8d66c9f52172af9c4969a5a350134a8a87c511;
K1_branch_or_rank3_gate.md, SHA
b85bbad1c675f2604d355db955ddbc08e16771f7c077b1ede1cbb07202e8afe4;
K1_left_turn_four_L_cleanup.md, SHA
bb166fa7646904ba293dffb6e6b1023bea8c61b039f3f8c7d32b70dde121a5a1.
