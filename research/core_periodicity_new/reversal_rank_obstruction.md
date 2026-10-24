# A K-renewal rank must retain time orientation

Status: exact finite construction, independently reviewed by the proof auditor on 2026-10-22 at 19:34 UTC. This is a restriction on candidate ranks, not an obstruction to the existence of an oriented rank and not a counterexample to capture.

Let F be the forward ant map, and let D_h be the unit vector in incoming heading h. Define the incoming-edge reversal involution

    I(B,p,h) = (B,p-D_h,h+2 mod 4).

It preserves the black field and reverses the directed incoming edge. Directly checking the two colors gives

    I^2 = identity,             F I F = I.

Thus if Y=F(X), then F(I(Y))=I(X), and the latter transition reads the complementary turn at the same physical cell.

Let K be the adjacent-bad-ten predicate with TRUE inverse history at each checkpoint, as in the audited total renewal map R_K. There are finite states X,Y with

    R_K(X)=Y,                  R_K(I(Y))=I(X).

An explicit witness uses the S=RLLR rail. Start with the 40 black cells (1,y), 0<=y<40, ant at (0,0), heading north. After 40 updates, X has position (0,20), heading north, and black field

    {(0,y): 0<=y<20} union {(1,y):20<=y<40}.

The next turn is R at (0,20). Hence Y has that cell added, position (1,20), heading east. Its reversal I(Y) is at (0,20), heading west. Its next turn is L, resulting in I(X), at (0,19), heading south, with the black field of X.

The eleven-turn windows ending at these two reads are, respectively,

    X:     LRRLLRRLLRR
    I(Y):  RRLLRRLLRRL.

Both ten-subwindows of each are outside the 84 standard cyclic ten-factors. All four cyclic ten-factors of the periodic S word are absent from that set. The finite rail has ample material on both sides to realize the needed eleven-step histories, and the supplied checker reconstructs them by the actual inverse ant map rather than assuming an external history. Consequently both first future K events occur immediately, proving the displayed renewal equalities.

Suppose a rank rho strictly decreases on every nonterminal R_K transition and is invariant under I. The two equalities force

    rho(Y) < rho(X),
    rho(I(X)) < rho(I(Y)),

which contradict I-invariance. Therefore no such rank exists. In particular, no function of the black board alone can be a strict K-renewal rank, no matter how nonlinear or nonlocal that function is.

The conclusion also applies to any proposed quotient that identifies X with I(X) for every state. A viable rank may still depend on the full oriented state. The conjecturally total remaining-K count is exactly such a directed quantity and is not contradicted.

Reproduction: check_reversal_rank_obstruction.py and its exact JSON output. This is a finite witness plus an elementary universal rank obstruction; it does not rely on bounded failure to find a rank.


## Unbounded reversal asymmetry is necessary for a natural-valued rank

This strengthening was independently reviewed at20:00 UTC.

Define A(X)=rho(X)-rho(I(X)), where rho is a proposed natural-valued strict K-renewal rank. Arbitrarily long finite S rails contain an arbitrarily long interior interval X,F(X),...,F^n(X)=Y whose every forward step and every I-reversed step is an immediate K renewal. Leave at least eleven rail reads of padding at each end, so all true inverse-history windows are internal. The four cyclic ten-factors of S are bad, as already checked above.

Since natural-valued strict descent costs at least one per transition,

    rho(X)-rho(Y) >= n,
    rho(I(Y))-rho(I(X)) >= n.

Adding gives

    A(X)-A(Y) >= 2n.

In particular at least one endpoint has |A|>=n. Thus the reversal asymmetry of any natural-valued strict rank is necessarily unbounded over finite states. A uniform bound |A|<=C would force n<=C for arbitrarily large n, a contradiction.

Consequences include the impossibility of any rank of the form an arbitrary board-only function plus a uniformly bounded head/local correction. More generally, any correction with uniformly bounded change under I is excluded. An ordinary affine head-position term also has bounded I-change, so adding it to a board-only energy does not repair the obstruction. A heading-dependent correction coupled to unbounded board geometry is not excluded.

The integer-step estimate is essential. No corresponding uniform-C obstruction is asserted for arbitrary strictly decreasing real-valued ranks, whose decrements may shrink.

## Even one fixed sector has no universal board-only rank

The original reversal argument compares the two invariant sectors. A separate finite two-board witness removes that qualification for board-only ranks.

Use B0=X.black and p=(0,20), and set B1=B0 xor{p}. In addition to X=(B0,p,N), take Z=(B1,p,N). The true eleven-turn history at Z is LRRLLRRLLRL, whose two ten-subwindows are both bad. Hence both X and Z have an immediate K renewal. The first toggles B0 to B1 and the second toggles B1 to B0. Both entry states, and both of their successors, belong to the same invariant sector.

A single function rho of the board alone, asserted to decrease at every renewal in this sector, would therefore require both rho(B1)<rho(B0) and rho(B0)<rho(B1). The checker now includes Z and its successor. The auditor independently replayed this strengthening at20:27 UTC. A unit spatial translation transfers the construction to the other sector.

Precise remaining limitation: this does not exclude a seed-dependent board rank asserted only in one fixed conserved-charge orbit. The signed row/column cut charges, together with a board and the sector, recover the full ant pose. Thus on such a restricted invariant class, writing a function as board-only may hide the entire oriented pose. The unbounded reversal-asymmetry result above still concerns a rank defined over both sectors.
