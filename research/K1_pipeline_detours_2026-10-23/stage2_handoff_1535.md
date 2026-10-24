# K=1 structural continuation: handoff, 23 October 2026

## Useful results first

Independently approved:

1. Every SIX parent faces of a K=1 first-L curve include a BEND. Thus a
   globally straight K=1 curve is impossible even with equal-M branches.
   Bend classes >= ceil(ell/6), actual full quotient retained.
   Source: K1_branches_force_bends.md, SHA
   57c354298337f3aa7e3b98ac44a0887729e473dc8c42264d737019ad5a631611.

2. The selected LEFT-L3 bit can rise only at a RIGHT turn with a LEFT
   max branch. If there is no such branch anywhere, every selected L3
   is LEFT and a genuine rank3-to-rank1 gate must occur; uninterrupted
   actual L3 corridors cannot cover a full period while omitting ranks0-2.
   Sources: K1_left_L3_state_gates.md, SHA
   ac025ac64acb980d7ace6b757f5c6d9902b4084529ff2d38e449f5f6a771130f;
   K1_branch_or_rank3_gate.md, SHA
   b85bbad1c675f2604d355db955ddbc08e16771f7c077b1ede1cbb07202e8afe4.

3. A zero-state LEFT/RIGHT bend pair needs a specific early outward M
   launch and a further outward M birth supplier. The flat N,S,S[,N]
   escape is retained. The two E outputs there target the older selected
   contact C's R0/L1; they are not q's own R0/L1.
   Source: K1_zero_state_left_right_launch.md, SHA
   8fb5af1921bdad6dcb20b618d17e0c5e0d088a2a54c565684781477f9371feeb.

4. A strict straight/right gate after a LEFT turn can use real old stock:
   Z.L1 -> q.L3 -> C.L3 -> A.L3 -> Z.R2 is literal consecutive LLLL.
   It is not a new max branch, permanent fuel charge or removable splice.
   Source: K1_left_turn_four_L_cleanup.md, SHA
   bb166fa7646904ba293dffb6e6b1023bea8c61b039f3f8c7d32b70dde121a5a1.

## Latest positive control and pending structural closure

The prescribed word LRRRRLLLLRLLLLRLRRRR realizes the locked bent gate
architecture with full P=20,d=(0,2), physical stream c_left=-1,
c_right=0,max_C=1,K=1. Four main cells are WHITE RLRL; two LEFT single-L
fuel cells transfer to two RIGHT single-R outputs. Exact finite seeds
with 2n+3 blacks run 20n reads, checked through n=100. It is NOT a white
front. Source: bent_pipeline_W20_prepared_control.md, SHA
f64cf7e47a128721a00efeb18b95f9e3eeaa54a05576349de7abb28c8407cb81.

Two later analytic notes await review, behind the parent's 1564 audit:

- bent_secondary_rail_height_obligation.md, SHA
  f8a56ac667b3475e3328b86a6420d411c5fe4f03e735d0db02d5615e308185ce.
  Arbitrary WHITE deeper detours preserving the four main locked
  histories must raise at least one secondary C face above M-2. The
  proof couples the two possible R suppliers across unique W entries
  and unique E exits, not a bounded factor table or black-mass loss.

- one_sided_height_barrier_and_bent_rail.md, SHA
  db13fb03af538df1bbe86dc0df2026f0dece08d9d81138b61b703dac95751216.
  Behind a low C row at c_left, a one-sided maximum at c_right cannot
  exist: white first-R propagation removes equal L zero pockets, then
  a local first-L birth curve would require negative right homology
  while its stream jump is zero. Combined with the secondary obligation,
  a white locked-bent completion needs a DISTINCT global-M component
  farther LEFT. Its leftmost maximum component cannot be this exact
  architecture. This does not exclude other K=1 components.

## Review artifacts and exact status

The independent auditor analytically approved results 1-4 and earlier
strict-straight/five-face/right-turn tables. Independent executables are
in audits/check_strict_K1_deep_ports_independent.py/json,
audits/check_K1_local_bends_independent.py/json and
audits/check_K1_zero_launch_independent.py/json. Later analytic approvals
may be entered in the shared audit ledger after its higher priority job.
The pending notes above are NOT represented as independently signed.

## The next concrete open step

For a branch-free K=1 curve, all selected LEFT-L3 bits are 1 and every
intermediate LEFT other-C neighbor is forced to the common baseline M-2.
The next plausible extension is an ordered SECONDARY port map through
arbitrary bends and rank3 gates. The locked alternating-bend map above
is an exact test case. A gate or max branch must not be assigned a paid
budget: literal LLLL old-stock cleanup and N,S,S launches are known
countercontrols. All arbitrary branch suppliers and further max
components remain retained.

No original proof edits, cap6 replay,
period/drift/radius front scan or general K>=2 theorem occurred.
