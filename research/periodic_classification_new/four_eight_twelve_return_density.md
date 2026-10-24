# Twelve-step local return extension and seven-per-visit density

23 October 2026, 09:21 UTC. Analytic candidate; independent review pending.
This extends the finite guarded-XOR local proof in four_eight_return_density.md.
No front period, drift, width or multiplicity bound is being searched.

On ANY input board, eleven successive FIRST returns to one physical cell
cannot all have lengths in{4,8,12}. For k=0,...,10 successive such returns,
the minimum total lengths among ALL color-consistent words are

    F(k)=0,4,8,12,20,32,36,44,60,68,80.

All positive cases are retained, including eight ten-return words; eleven
are excluded, NOT ten. This also gives the useful unconditional factor:
ANY five consecutive physical first returns cost at least32. Indeed if
one return has length>=16 the other four cost>=4, already32; otherwise
all five belong to{4,8,12} and the displayed minimum is32.

## Complete finite certificate

Producer certify_four_eight_twelve_unit_returns.py enumerates all2^L turn
words at L=4,8,12 for incoming N/S. There are4,8,24 legal first-return
programs per heading, supported on37 cells. A program's complete guard and
XOR are derived by literal replay. Composing these guarded programs exactly
as in the four/eight proof gives compatible prefix counts

    1,36,268,540,524,468,280,184,84,32,8,0.

For each of the eight depth-ten prefixes, all36 possible next programs
have an explicit conflicting physical input-color bit. The288 witnesses,
all earlier prefixes, complete traces and guards are in
four_eight_twelve_unit_returns.certificate.json. Rotation normalizes the
initial incoming heading to N; return parity then permits only N/S.
This is a complete local-factor enumeration, not finite-horizon inference
about an infinite front.

## Uniform consequence at unrestricted multiplicity

Retain the full-drift notation of four_eight_return_density.md. A gap is
now short iff its displacement is zero and its length is4,8 or12. Every
short run has length q<=10 and cost>=F(q). The remaining gap is either a
physical zero-return costing>=16 or a nonzero gap costing>=2D*abs(k_i).
There is at least one nonzero gap, so cyclic gaps split into blocks ending
at such a nonshort gap.

For c in[4,7], direct evaluation of the eleven displayed integers gives

    F(q)-c*q >=12-3c        for every q=0,...,10.

Taking c=min(7,3+D/2), D>=2, a winding block has nonnegative cost surplus:
12-3c+2D-c>=0. A zero-return nonshort block likewise has surplus at least
12-3c+16-c=28-4c>=0. Summing proves

    P >= min(7,3+D/2)*n,                 D>=2.       (1)

If D>=8, choose a winding gap and retain its extra cost2D-16 over the
baseline16. Then

    P >=7n+2D-16,                       D>=8.       (2)

These inequalities hold on arbitrary input profiles. They do not imply
capture, bounded multiplicity or any all-cap no-front theorem. At D<=6
(1) agrees with the four/eight extension; at D7 it gives6.5 per visit,
and at D>=8 seven per visit instead of six. The separately signed WHITE
small-n packing bounds can remain stronger. The axis-four P>=36 argument
in the four/eight note is unchanged, because three minimal winding gaps
are still a possible relaxation.
