# Genuine U-entry controls and withdrawal of a pending plain-source cut

Pending full-output-seal manifest 6ea48d5 is NOT PASSED. Its two plain-source
endpoint arguments omit the possible zero-C S run after C2 and before the
putative E consumer. The claim that a plain V/U source must itself own those
two C tails is false. No at-most-one full-output spending or stronger seal
conclusion from that artifact may be used. Frozen sources are preserved so
the rejected inference remains inspectable.

The independently passed ordered matching bf616fdc, older-input transport
bottleneck ef645520, and coordinate-role erratum f2ff1b4d are unaffected.

## A 16-black genuine U-entry control for plain V

Take actual fullpacket sequence U,V,VCC,V,V, followed by actual M11. All
unlisted cells are white. The complete finite initial black board is

(-1,-1),(-1,0),(-1,1),(-1,2),(-1,4),(-1,6),
(0,-1),(0,0),(0,2),(0,3),(0,7),(0,9),
(1,0),(1,6),(1,10),(2,9).

The fullpacket entries are U(0,0,N) at tick0, first V(0,4,N) at tick28,
VCC(1,7,N) at tick46, S-facing V(1,11,S) at tick94, and final V(0,8,S)
at tick112. The first V's genuine fresh A at physical (0,5) is produced by
R39 and remains unread until L131. The final V enters at source-relative
(0,4,S), exactly two source-entry Cs later, and takes A into its actual
input (0,3). That input is marker-only: final V RAW ends at tick130, while
its actual physical L is next-word RAW phase2, here M11 phase2 at tick131.

This is a genuine U-entry complete-eight factor, not merely a prepared
source-free V suffix. Normalized to the first V source, the omitted S V runs
from (1,7,S) to (0,4,S). It is exactly the missing displacement in the false
endpoint argument.

## A 14-black genuine U-entry control for plain U

Take U,VCC,V,V followed by actual M11, from the 14-black complete board in
the JSON. The original U's recycled q=(-1,2) is first consumed at U L13,
genuinely reborn at U R21, and later physically retired at L113. The final
V starts at (-1,5,S), at source-entry C age two, and takes q into (0,3).
Its RAW ends at tick112; the physical retirement again belongs to the next
actual word's RAW phase2. This directly refutes the second plain-source
ownership cut as well.

## What the controls do and do not settle

These exact complete-board replays establish that actual age-two parallel
return transport from a plain source is possible, with genuine source birth
IDs and correct physical marker ownership. They do not include a foreign
word or attain one of the three old-C returned-C geometric residues. A claim
excluding them inside that narrower endpoint problem would need an additional
endpoint-aware argument with all N/W/S stages retained. No larger-prefix scan
or automatic promotion of a repaired seal follows.

Run check_ordered_W_seal_withdrawal_controls.py to replay every physical read,
the full boards, packet clocks, source tag histories and actual M11 reads.
