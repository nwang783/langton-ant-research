# A same-sector mass-neutral solid-rail rewrite

22 October 2026. Exact primitive, not a finite-white-front highway or a reusable endcap.

The literal word

    W20 = LLRLRRRRLRRRRLLLLRLL

starts at (1,0), heading east, in pose sector x+y+h = 0 modulo2, with N,E,S,W indexed0,1,2,3. It returns to the same heading at (-1,0), so its translation is (-2,0).

For an all-epoch westbound sweep, group its literal reads by (x modulo2,y). At a fixed translated physical cell, the order of reads is increasing 10*x_i+i, where i is the phase and x_i its literal coordinate. For BOTH x parities the exact ordered read words are:

- row0: L, hence black to white;
- row1: RLRL, hence white to white;
- row2: RLRL, hence white to white;
- row3: R, hence white to black.

No other row is read. Thus this front moves a solid black row from y=0 to y=3 while restoring the intervening two white rows. Other rows are spectators. It preserves bulk black mass and stays in sector0. This supplies a concrete negative control against treating same-sector rail motion as necessarily consuming bulk fuel.

The statement specifies the exact periodic bulk chronology. A finite sweep additionally needs its finite boundary phase conditions; no clean cap, renewal mechanism, sparse-rail recovery, or infinite evolution from a finite seed is claimed. The primitive was observed inside a continuation of the earlier finite rail-expansion construction, but that observation is not needed for the all-epoch identity.

Executable certificate: `check_w20_rail_profile.py`; exact output: `check_w20_rail_profile.json`. The certificate derives the physical path from the literal word and asserts every row-class string above.
