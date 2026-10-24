# A fixed sector still rules out uniformly local energy ranks

Status: new proof submitted for independent audit. This strengthens the earlier two-sector reversal obstruction. It does not exclude a genuinely nonlocal, oriented rank, or a separately chosen function on each conserved-charge orbit.

Let rho be a natural-valued rank defined on every finite state of one invariant sector and strictly decreasing on every nonterminal adjacent-K renewal. There cannot be a decomposition

    rho(B,p,h) = E(B) + c(B,p,h)

with constants L,C such that changing a single board bit changes E by at most L in absolute value, and |c| <= C uniformly. No spatial symmetry of E is assumed. In particular, this excludes an energy given by a fixed weighted sum of finitely many finite-range pattern counts, together with any bounded local head correction. It also excludes a natural rank that depends only on a bounded translated neighborhood of the head.

## An all-n pair of rail traversals in the same sector

Use headings N,E,S,W = 0,1,2,3 and sector (h-x-y) mod2. Fix n>=1 and padding M>=12. Let

    B0 = {(0,y): -M<=y<0} union {(0,2n)}
         union {(1,y): 0<=y<2n or 2n<y<=2n+M}.

The state X=(B0,(0,0),N) executes (RLLR)^n. Each four-step block moves north by2 and transfers the two black cells of column1 to column0. Its endpoint is Y=(B1,(0,2n),N), where

    B1 = {(0,y): -M<=y<=2n}
         union {(1,y): 2n<y<=2n+M}.

Starting instead at Z=(B1,(0,2n),S), the word (LRRL)^n is feasible. Each four-step block moves south by2 and transfers the two black cells of column0 to column1. Its endpoint U=(B2,(0,0),S) has

    B2 = {(0,y): -M<=y<=0}
         union {(1,y): 0<y<=2n+M}.

All four states are in sector0. Every step on both paths is an immediate K renewal. For the first ten reads, the supplied padding gives the true inverse histories of the same periodic rails. Subsequently the histories are inside the displayed path. Every cyclic ten-factor of RLLR and LRRL is outside the84 standard ten-factors. This is checked literally against the canonical standard word, not inferred from an arbitrary external history.

The two endpoint boards differ at exactly four cells:

    B0 symmetric_difference B2 = {(0,0),(1,0),(0,2n),(1,2n)}.

Natural-valued strict descent gives

    rho(X)-rho(Y) >= 4n,
    rho(Z)-rho(U) >= 4n.

The intermediate boards of Y and Z agree. Adding these inequalities under the proposed decomposition therefore gives

    8n <= E(B0)-E(B2) + c(X)-c(Y)+c(Z)-c(U)
        <= 4L+4C,

which is impossible for arbitrarily large n. A unit spatial translation gives the same obstruction in sector1.

The construction uses two distinct physical paths, not one recurrent orbit. It is therefore not a counterexample to eventual capture. Their conserved-charge arrays need not agree. The precise conclusion concerns one rank formula required to work throughout a sector.

## Why this excludes finite-range pattern energies

A finite-range translation-invariant additive energy has the form

    E(B) = sum_z [f(B restricted to z+S)-f(empty)]

for a fixed finite shape S and a real function f on its finitely many binary patterns, or a finite sum of such expressions. The sum is finite on finite boards. Flipping one cell changes at most |S| summands and hence changes E by a uniformly bounded amount. A head correction depending on a fixed finite translated neighborhood and heading has finite range and is uniformly bounded. Thus the theorem applies whenever the resulting rank is natural-valued and strictly decreases on each renewal.

No analogous conclusion is claimed for arbitrary real-valued ranks with shrinking decrements. Position-weighted or genuinely long-range board energies can have unbounded one-bit increments and are not excluded.

Reproduction: check_single_sector_local_rank.py and its JSON output. The script reconstructs each inverse history and checks both entire paths for several n, including1000; the explicit formulas above establish all n.
