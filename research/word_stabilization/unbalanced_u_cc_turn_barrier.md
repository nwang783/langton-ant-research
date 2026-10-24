# The U V^k CC V^(k+1) terminal C cannot continue

Status: independently audited analytic argument with literal finite ingredients.

For every integer k >= 0 and every macro A in C,U,V,Q,B,

    U V^k C C V^(k+1) C A

is infeasible. If the prefix through the last C is feasible, that C reuses its
phase-1 input. This is the second, unbalanced family appearing in the bounded
classification of reused first-C inputs.

Normalize the first U to pose (0,0,N). After U V^k CC the pose is
(k-1, 5+3k, S). After the returning k+1 V blocks it is (-2,2,S), and after
the final C it is (-2,1,E).

All reads between the first U and the final C, except possibly those in
the last returning V, have height at least 3:
- The outgoing V blocks start at height at least 4 and have minimum local
  read height -1.
- The first middle C starts at height 4+3k and has minimum read height -1.
  The west-facing second C starts one unit higher and has minimum physical
  height equal to the first C's start height.
- V's maximum local read height is 3. The last returning V starts at
  (-1,5,S); every earlier returning V starts at height at least8 and
  therefore reads only at heights at least5.
- The last returning V does not read (0,1), (0,2), or (-1,2): these would
  require its local cells (-1,4), (-1,3), or (0,3), all absent from V.

The final C has local x range [-1,2]. From its south-facing entry (-2,2),
it cannot read either (0,1) or (0,2), because those would require local
x=-2. The first U last reads (0,1) as R at phase19 and (0,2) as L at phase20.

If A is C or V, its phase12 reads physical (0,1) as R, without an earlier
read of that cell inside A: a consecutive R/R conflict.
If A is U,Q,B, its phase13 reads physical (0,2) as L, without an earlier
read of that cell inside A: a consecutive L/L conflict.
These finite footprint facts exhaust all five A choices.

Finally the last C's phase1 input is physical (-1,2). The first U last
reads it as R at phase21. The height bounds and the last-V exclusions
above rule out every intervening read, and final C phase1 reads it as L. Thus this is genuine terminal reuse.

This does not prove that all reused first-C inputs have this form or the
balanced pure-V form. That unbounded classification remains open.
