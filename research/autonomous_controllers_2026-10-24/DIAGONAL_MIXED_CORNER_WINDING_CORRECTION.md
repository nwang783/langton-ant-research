# Mandatory winding correction for the mixed-corner cover

24 October2026,05:53UTC. Apply together with
DIAGONAL_TWO_SINGLETONS_FORCE_FIRST_CIRCLE.md SHA3efd718e.

The prose there says the24 closed event components have winding+1.
The frozen JSON and executable witnesses correctly give winding MINUS ONE
for every one of them. Each has four events and at least44 other named
events. The source assertion of a proper component remains correct.

This typo does not affect the rejection or domain coverage. In fact the
four edge-clock equations alone give4=-P for these winding-minus-one
components, already impossible for P>0, even without invoking their
properness. The4,668 skipped-rank witnesses, all4,692-case coverage,
12 removed interface IDs and the143-case g8 remainder are unchanged.

No original frozen artifact is overwritten. This correction is mandatory
when citing or reviewing the proof note; the original JSON is accurate.
