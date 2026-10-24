# Four/eight-step first-return chronology and visit-density bounds

23 October 2026, 09:18 UTC. Analytic candidate; independent review pending.
This is an arbitrary-input local chronology obstruction, not another
multiplicity/drift inventory. No external novelty claim is made.

## Exact local theorem

On ANY initial board, five consecutive FIRST physical returns to the SAME
cell cannot all have lengths in{4,8}. If four consecutive first returns do
all have lengths4 or8, their total length is at least20.

The incoming heading at the common cell can be normalized to N by a genuine
quarter rotation. Every even return restores its heading parity, so only
N/S incoming headings need be retained thereafter. At a return of length4
or8, enumerate all2^4 or2^8 quarter-turn words. Keep precisely those whose
first return to the origin is at the end and whose consecutive same-cell
reads alternate turns. These conditions are necessary and sufficient for
some initial assignment of colors on the finitely many read cells.

For each incoming heading there are4 legal length-four programs and8
legal length-eight programs. Their read cells over both incoming headings
occupy21 physical positions. Each program is a partial initial-color guard
and a complete XOR mask on these positions. Composition is exact: with
current XOR X and a program guard(G,B), its required original black bits
are B xor(X and G). An intersection disagreement with an earlier guard
is a literal same-cell alternating-color contradiction; otherwise extend
the guard and XOR the update.

`certify_four_eight_unit_returns.py` writes the finite, explicit certificate
`four_eight_unit_returns.certificate.json`. Starting with incoming N,
there are12,42,48,16 compatible program prefixes of depths1,2,3,4, and NONE
of depth5. Every one of the16 depth-four prefixes has an explicit conflict
cell for each of its12 possible next programs (192 witnesses). The minimum
costs at depths0..4 are0,4,8,12,20. Positive depth-four programs are retained;
thus four short returns are NOT excluded. No initial-color assumption is
used and no unbounded period is enumerated.

## A uniform all-multiplicity consequence

Let a complete translating ant trajectory, on any prescribed input profile,
have actual full drift d, D=norm-infinity(d)>=2, period P and n occurrences
of one FULL-drift cell class. Its cyclic phase gaps have displacements
k_i*d, integers k_i with sum1. Zero-displacement gaps are consecutive FIRST
physical returns to their common physical cell. Their lengths are multiples
of four. Nonzero gaps have length at least2D*abs(k_i), by axis alternation.

Call a gap short only when its physical displacement is zero and its length
is4 or8. Every maximal short run has length q<=4, with costs at least

    F(0),...,F(4) = 0,4,8,12,20.

Every other gap is either a physical zero-return of length>=12 or a nonzero
winding gap. Since there is a nonzero winding, the cyclic list splits into
blocks consisting of a short run and one nonshort gap. This decomposition
preserves actual chronology; it does not merge returns at translated cells.

Put c=min(6,3+D/2). For every q in{0,...,4}, F(q)-c*q>=12-3c.
A nonzero winding gap has cost>=2D, and

    (12-3c)+2D-c >= 0.

A long zero-return has cost>=12, and

    (12-3c)+12-c =24-4c >=0.

Summing the blocks proves the ALL-MULTIPLICITY inequality

    P >= min(6,3+D/2)*n.                              (1)

When D>=6, choose one nonzero winding block. Its nonshort gap costs at
least2D instead of the generic12, yielding the stronger

    P >= 6n+2D-12,       D>=6.                        (2)

These are necessary constraints, not capture or all-cap no-front claims.
They strengthen the earlier5-per-visit asymptotic density at D>=5. For
small n, the separately signed white bounds can be stronger.

## An axis-four all-cap period consequence

The signed KR cap-five exclusion supplies some class with n>=6 at actual
full horizontal drift four (and genuine rotations). If n>=7, the signed
LC bound P>=4n+8 already givesP>=36. It remains n=6.

Let r be the number of nonzero class gaps. Their absolute winding sum S is
an odd integer at least r, because their signed sum is1.

- r=1: the other5 gaps form a single run of physical first returns. They
  cannot all be4/8, so at least one costs>=12; the others cost>=4. Their
  total is at least28. The winding gap costs>=8, soP>=36.
- r=2: S>=3, winding cost>=24; four zero gaps cost>=16, soP>=40.
- r=3: S>=3, winding cost>=24; three zero gaps cost>=12, soP>=36.
- r>=4: S>=r, soP>=8r+4(6-r)=24+4r>=40.

Therefore every full axis-four complete WHITE front would satisfy

    P >=36,                                          (3)

with NO period, multiplicity or strip-width cutoff. This improves32, but
does not exclude higher-period fronts or settle the finite-seed conjecture.
