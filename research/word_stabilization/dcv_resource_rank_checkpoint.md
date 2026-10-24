# D/C/V resource-rank checkpoint

2026-10-22 23:22 UTC. No D/C/V infinite-tail exclusion is proved.

The exact residual-core ledger is independently audited. Exhaustive marked feasible-prefix trees at entry mass 6 through 20 all terminate, the largest with 3,433,815 nodes and maximum 27 raw macros. These are finite controls only. Their maximum consecutive zero-initial-token-use streak is five. The complete mass-20 tree exhibits six RAW producer/consumer types, listed as EDGE records in `dcv_resource_transfers_fuel20.log`; completeness beyond that finite tree is not known.

A separate packet-conditioned enumeration starts at a non-C macro and exhausts 1,799,523 marked prefixes at mass at most 20. It records 23 transfer types including four from the exceptional initial DCCC, hence 19 between recurrent packet types D,DC,V,VC,VCC. The source packet includes its completed C suffix. This distinction matters: the same RAW D output has different future usability depending on whether its packet is D or DC.

Single-token linear ranks fail in the coarse pose-pair abstraction. A max-plus bounding-box rank also fails for the six observed RAW transfer types. However the 19 observed recurrent PACKET transfer types admit an exact integer max-plus potential. `check_dcv_conditional_confinement.py` directly checks the arithmetic. This is a conditional reduction only: many unproved transfer exclusions are needed. A finite, explicitly listed bad-transfer family in `dcv_conditional_confinement.json` is sufficient for that particular potential; none of those exclusions is asserted merely because it was absent from bounded search.

The protected-token relation is a new chronology-aware refinement rather than increased lookahead. Its first two-cell closure narrows the possible transfer poses but does not yet establish the needed exclusions. A radius-two color-patch test of one suspect surviving C output hit its 1.5-million-state cap without a result and is not being enlarged blindly.

Next productive targets are an analytic surviving-output crossing obstruction, a coupled-source bound, or a smaller exact conditional bad-transfer set. All existing zero-fuel V controls remain mandatory negative controls.
