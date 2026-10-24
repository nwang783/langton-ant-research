# Quantitative homogeneous-block bounds on the limiting ray

Status: independently analytically audited extension of the exponent-one/exponent-two exclusions, including the entry-cut and final-read conventions. Counts are in permanent-spine syllables, NOT physical ant time.

Write k_i in {1,2} for the successive permanent-spine increments. Let m_i be the number of black cells immediately before permanent entry i, after any optional completed B at that root. Fix an initial cut i=0 with finite m_0=m.

## 1. Every syllable changes mass by at most six

Let epsilon=+1 for an R parent and -1 for an L parent. A G packet of sign a has turn imbalance either0 or4 epsilon_a. A B packet of either sign has imbalance in {-4,0,4}. These identities follow directly from the G/B word grammar; finger depth affects only which parity case occurs.

For k_i=1, the stage is a [optional B_b], so its mass increment has magnitude at most5.

For k_i=2, the stage is a [optional G_b] a [optional B_b]. The core plus optional G contributes 2 epsilon or -2 epsilon. Adding the optional B changes this by at most4. Thus

    |m_(i+1)-m_i| <= 6,

uniformly in every packet length.

## 2. A block of exponent-one syllables has length at most2m_entry+4

Take a consecutive block of L exponent-one syllables. Except possibly its final two root neighborhoods, the argument in `alternating_boundary_exclusion.md` forces every optional B to be the depth-zero one-finger packet. If the first sign is R, look only at its first L-1 core reads; all optional packets before these reads have that forced form.

Every L-root point x_k in this truncated staircase must either have been black at the entry cut, or have been made black by the preceding B_L(0). The latter packet requires the distinct off-diagonal point u_(k-1) to have been black at the entry cut. No other earlier depth-zero packet creates black at x_k: B_R at the same stage restores x_k and itself requires it black, while all earlier unrelated footprints miss it.

Any preparation by a B_L completed before the entry cut is already part of the initial board and its black mass; it is not an additional in-block source. The initial x_k and u_(k-1) charges are pairwise distinct and lie on disjoint diagonals. Hence the number of these L-root reads is at most m_entry. In the R-start case this gives floor((L-1)/2)<=m_entry, so L<=2m_entry+2.

If the block starts with L, omit its first stage. For L>=3 its following optional B_R is forced depth-zero and has mass imbalance0, so the mass at the resulting R entry is m_entry-1. The same bound applies. The short cases are immediate. We retain the convenient conservative universal bound

    L <= 2m_entry+4.                                      (2)

The tail proof was not merely a contradiction at infinity: it supplies a finite entry-mass bound on every homogeneous exponent-one block.

## 3. A block of exponent-two syllables has length at most2m_entry+13

First suppose the initial sign is R and use the two-row coordinates of `doubled_boundary_exclusion.md`. For EACH R stage k in the block, make the following charge:

- if a north finger occurs at stage k, charge its initially black q_k=(2k+1,1);
- if no north finger occurs at stage k, charge the lower L-root l_k=(2k+1,-1), which must have been initially black.

The second assertion uses exactly the odd-column argument from that note, now stage-by-stage rather than after the last north stage. North fingers at other indices miss its column pair. East far endpoints can only create11 at the odd column, and without a same-stage north finger the upper black bit cannot be repaired before its R read. Thus such an endpoint cannot supply the lower black bit. No south finger reaches l_k before its first own-stage read.

At the first R stage, any B_R already completed before the entry cut is absorbed into the initial field and is not counted as an in-block north finger. Charge l_0 unless a north finger actually occurs after the cut. If the block ends on an R stage, its lower L-root read may be immediately outside the counted block; the infinite spine still forces that next read, with no intervening event capable of repairing its color.

All q_k/l_k charges are distinct initial black cells. There are therefore at most m_entry R stages, giving L<=2m_entry for an R-start block.

If a block starts with L, omit its first stage. By Section1 the mass at the next R entry is at most m_entry+6. Hence

    L <= 2m_entry+13.                                     (3)

This argument needs no depth bound or restriction to one-finger B packets.

## 4. The number of exponent-two syllables is at least square-root order

Let M(N) count exponent-two syllables among k_0,...,k_(N-1). The core contribution to m_N-m is at most1+M(N): the baseline alternating single turns have imbalance at most1, and each exponent2 contributes one extra signed turn. Optional G packets occur only at exponent2 stages and contribute at most4M(N) in absolute value.

An optional B at root i has zero imbalance whenever k_i=k_(i+1)=1, by the forced depth-zero lemma. Among B roots i=1,...,N, at most2M(N)+2 can fail that condition: each exponent2 inside the prefix affects at most two B roots, and the two boundary positions beyond the prefix add at most two more. Each B contributes at most4. Consequently

    m_N <= m+13M(N)+9.                                   (4)

The same bound holds at every earlier cut with its own M, and hence with M(N). The first N syllables contain at most M(N)+1 exponent-one blocks. Combining (2) and (4),

    N <= M(N)+(M(N)+1)(2m+26M(N)+22).                    (5)

In particular M(N)=Omega(sqrt(N)) as N tends to infinity, with the initial-cut dependence only in the lower-order constants. No positive linear density is claimed.

## 5. The number of exponent-one syllables is at least logarithmic order

Let J(N) count exponent-one syllables. Partition the prefix into J blocks of the form 2*1 and one final block2*. If a 2-block starts with mass m_i, (3) bounds its length by2m_i+13. By Section1 its end mass is at most13m_i+78; the following exponent1 stage adds at most5. With z_i=m_i+7, each full 2*1 block therefore satisfies

    z_(i+1) <= 13 z_i,
    block length <= 2 z_i.

The final 2* block has length less than2z_i. Summing the geometric bound yields

    N <= (m+7)(13^(J(N)+1)-1)/6,                         (6)

or equivalently

    J(N) >= log_base13(1+6N/(m+7))-1.

Thus J(N)=Omega(log N). The constants are deliberately loose.

## Limits

Individual syllables can still have arbitrarily long completed fingers, but the later note `physical_time_boundary_mixing.md` supplies an aggregate bound: finger depth is at most its entry mass and stage mass grows at most linearly in syllable count. Therefore the first N stages take at most36N²+(12m+150)N physical updates. This transfers the present counting estimates to exponent-two count Omega(t^(1/4)) and exponent-one count Omega(log t), after a fixed permanent cut. Neither note implies bounded run lengths independent of time, positive densities, a finite-state frontier, periodicity, or standard104 attraction.
