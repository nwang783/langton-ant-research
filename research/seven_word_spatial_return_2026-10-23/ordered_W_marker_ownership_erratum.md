# Marker-only physical-owner erratum for the ordered W matching

Frozen bf616fdc has correct exact input coordinates and zero-based first-read
ticks but incorrectly labels two marker-only physical owners as next-word
RAW phase1. The correct owners are next-word RAW PHASE2:

- Plain D has RAW length10; input(0,1) is first L at context tick11.
- Plain U has RAW length28; input(-1,4) is first L at context tick29.

The first following RAW read is context tick equal to the preceding RAW
length. Therefore tick11 after length10, and tick29 after length28, are
the SECOND following reads. This agrees with V input(0,3), used in the
portal note: V RAW length18, first L tick19, also following RAW phase2.

In DC and UC/UCC these reads belong instead to their own first C-tail RAW
phase2; VCC's chosen(0,3) read at tick19 belongs to its first C-tail RAW
phase2. V/VC's chosen(1,2) is inside base RAW at tick13.

The original common-output physical R8, all chosen sites, C clocks,
residual I/O order, matching displacements, literal query rows and proved
conclusions are unchanged. No physical L-before-R claim was used.
Read the phase1 owner strings in bf616fdc note/JSON as phase2. Frozen
sources remain preserved. The companion role-name erratum f2ff1b4d still
applies independently; neither erratum creates a new port or theorem.
