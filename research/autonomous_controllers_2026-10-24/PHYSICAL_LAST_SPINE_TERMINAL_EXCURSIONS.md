# Every last spine partitions the whole period, not its own basin

24 October 2026. Author proof and literal controls; independent review pending.
This is an all-cap chronological decomposition and a scope countercontrol, not an output lower bound or a new controller.

## Hypotheses and exact decomposition

Use a genuine complete translating turn path with full period P and drift d. Retain every stable physical read class modulo the FULL lattice Zd. Let lambda(v) be its actual final read time in a chosen representative. A physical last-departure edge v -> u+nu*d has

    Delta(v) = lambda(u)+nu*P-lambda(v) >= 1.

Its actual arrival at u is one step after the source's last read, but need not be u's last read. The independently signed primitive-spine theorem states that each selected quotient cycle is embedded and has winding +1. Consequently its positive Delta values sum to P.

Choose one cycle and an actual lift of one of its final reads. Follow its selected edges and lift all following final times consistently. These times strictly increase and end at the first time plus P, at the first physical cell plus d. Thus the half-open intervals between successive selected final reads partition EXACTLY ONE ENTIRE PERIOD of actual time.

For each selected edge, separate the initial actual departure at v from the remaining Delta(v)-1 reads. The remainder starts at the actual arrival at u and ends immediately before its last read. It is a closed-POSITION excursion at that SAME physical u. Its length is a nonnegative multiple of four, but its incoming and terminal headings may differ by a half-turn. It can contain earlier returns to u; splitting at all such visits gives actual consecutive same-cell first returns. No word or multiplicity cap has been imposed.

Let T_spine be the sum of the ACTUAL R/L signs at the selected last reads, and Q_e the actual R-L excess of these terminal excursions. Then the exact identity is

    GLOBAL g = T_spine + sum_e Q_e.

The effective geometric spine turning is zero, but T_spine need not be zero: the selected incoming edge at a vertex can arrive at an earlier read with the opposite heading. Replacing T_spine by effective turning would lose the retained heading mismatch.

Most importantly, this construction partitions the WHOLE event word for EACH spine, not just that spine's last-departure basin. The excursions may visit every other basin. Different spines' partitions therefore cannot be added as disjoint debts or used to assign each global output to its own spine.

## Actual WHITE standard countercontrol

For normalized standard104, its 4-output physical exit basin has a four-edge spine. Three of its terminal excursion lengths are 0,0,4, and the fourth is 96. The latter contains all 86 actual events of the OTHER, 8-output basin and 10 events of its own basin. It is not an isolated four-output controller.

That 96-read terminal excursion is based at full class (0,1). Its consecutive same-physical-cell first-return factors, in order, have

    lengths: 8,76,8,4,
    R-L:    -2, 8,0,4.

The first word is LRLLLLRR. It is a genuine negative-growth elementary return based on the actual last-exit spine. The later length-eight word is LLRRRRLL and is materially neutral. The whole 96-read aggregate has excess +10; no sign theorem for that aggregate is being asserted.

A fresh empty-board simulation places the negative factor at times10320..10327, based at(-24,2), incoming S and returning incoming N at10328. Its full BLACK field changes from758 to756 cells. Its L inputs have exact owners

    L10320 <- R10316,
    L10322 <- R10242,
    L10323 <- R10295,
    L10324 <- R10296,
    L10325 <- R10321.

All are actual earlier producers in the same empty-seed trajectory, and the entire front is the certified infinite standard tail. Four of those lifetimes are already BLACK at the factor cut; the last is produced inside the factor. Internal historical production does not turn those four imported lifetimes into WHITE inputs of the factor. Seven of the eight updates belong to the other physical exit basin.

This is stronger than a transient or prepared-only warning for ELEMENTARY spine returns: it occurs inside an actual complete WHITE translator. It does not refute positivity for some differently specified larger aggregate, a four-output minimum per basin, or any asserted two-spine theorem. None of those statements follows from this decomposition.

## Controls and retained fields

The certificate reconstructs the complete partition for standard104 and the supplied prepared10,80,1564,4352 controls, plus all20 proper-rotation cases. The prepared backgrounds remain exactly those already retained in the signed component certificate, including passive strands and finite XOR caps; they are not treated as autonomous WHITE realizations. Both long prepared waves also have negative WHOLE terminal excursions. Those prepared examples alone say nothing about a WHITE aggregate sign.

The fresh standard replay retains all96 actual reads and their R owners, complete fields at every intermediate root return, and the dependency on the signed all-future standard parity certificate. Artifacts: `certify_physical_last_spine_excursions.py` and `physical_last_spine_excursions_certificate.json`.
