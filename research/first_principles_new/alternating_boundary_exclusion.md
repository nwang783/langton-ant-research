# Finite square seeds exclude an eventually all-exponent-one boundary ray

Status: independently analytically audited proof, with exact local packet-table replay. This is a restriction on a possible limiting ray, not the highway theorem.

## Statement

For a square ant started with finitely many black cells, the limiting reduced ray in C4*C4 cannot have an eventual tail in which every syllable has exponent1. Equivalently, exponent2 must occur infinitely often in that boundary ray.

The finite-prefix board remains finitely supported, so it suffices to exclude an infinite all-exponent-one tail beginning at a nonreturning module entry. By skipping one syllable if necessary and rotating the physical frame, take its successive permanent-entry roots to be

    R roots w_k=(k,k), heading north;
    L roots x_k=(k+1,k), heading east,       k>=0.

Here "permanent entry" means the final, nonreturning entry into that module. There may be a completed B call at the same root immediately before it. The only core updates are R at w_k and L at x_k.

## 1. Every optional B has exactly one depth-zero G child

The all-exponent-one hypothesis means that every permanent call chooses child1 as its nonreturning child. The general stage grammar therefore permits only an optional B at the selected child, never a G before advancement to child2.

Consider any optional B_a, where b is the opposite letter. In the return ledger, a two-finger B_a leaves its child1 root with color a. A one-finger B_a leaves it with color b. After B_a returns, the immediately repeated permanent a-call must select that same child1 and read b there. Hence a two-finger B is impossible.

Write the remaining packet as a G_b(n) a^3. Let q be the first point reached after the entry read of its G_b child. This is also the next-next permanent spine root. In G_b(n), q has initial color b. If n=0 it is an endpoint and is flipped once, leaving color a. If n>=1 it is an interior rail point and is read twice, leaving color b. The rest of the parent B packet does not read q.

The permanent spine needs q to have color a. An optional B_b at the intervening child1 root cannot repair a wrong color at q: its mandatory G_a child starts by reading q as a. Without that optional B, the permanent b read also goes directly to q and requires a. Thus n>=1 is impossible, and every optional packet is exactly

    B_a(0)=a b^4 a^3.

This argument uses the next two permanent spine entries. There is no bound on packet depth being assumed beforehand.

## 2. The two remaining packet types

Let u_k=(k,k+1), the upper-left off-diagonal point adjacent to w_k and x_k.

A packet B_R(0) at w_k has word RLLLLRRR. Its initial black read points are

    x_k, w_(k+1), u_k,

and its initial white read points are

    w_k, (k+1,k-1), (k,k-1).

It reads w_k and x_k twice, restoring them, and flips its four other read points. In particular it requires u_k black and leaves it white.

A packet B_L(0) at x_k has word LRRRRLLL. Its initial black read points are

    x_k, u_k, w_k,

and its initial white read points are

    w_(k+1), x_(k+1), (k+2,k).

It reads x_k and w_(k+1) twice, restoring them, and flips its four other read points. Again it requires u_k black and leaves it white.

These two finite read tables can be checked directly; the companion script does so with exact coordinates and no simulation cutoff.

## 3. A fresh finite-support charge

The permanent core roots lie on x-y=0 or1. Every u_k lies on x-y=-1. Inspecting the two packet footprints shows that among ALL core updates and optional packets in the infinite tail, u_k is read only by the two candidate packets B_R(0) at w_k and B_L(0) at x_k.

Consequently its first possible read in the tail is L, and either candidate packet turns it white. Both cannot occur. Every optional packet therefore consumes a distinct point u_k that was black in the board at the start of the tail.

That board has finite black support, so only finitely many optional packets occur. After the last one, the tail is the bare staircase RLRL... . Its distinct L-root points x_k eventually lie outside both the finite initial support and the finitely many packet footprints. They have never been read before and are white, contradicting their required L reads.

Therefore no such infinite tail exists. In particular the limiting ray must contain infinitely many exponent2 syllables.

## Scope

The result does not supply a positive lower density of exponent2 syllables, bound intervening blocks uniformly over time, exclude an all-exponent-two tail, or select the standard104 boundary word. The fresh charge works here because the all-exponent-one geometry forces every decoration to the single depth-zero type and confines all possible visits to u_k to its own stage pair. General rays lack this special separation.
