# Single isolated solid-rail shift probe

Status: small unreviewed exploratory inventory, not an all-length theorem.

Question: must every mass-neutral west-translating front that replaces one entire solid black row by one solid black row shift the row by -1 modulo4? S gives shift-1 and W20 gives shift+3. The crossed-column charge only proves the shift is odd. No stronger invariant has been established.

`probe_single_rail_shifts.cpp` enumerates internally alternating literal turn words, entry north, displacement(-2,0), equal R/L counts. Every read is grouped by (x modulo2,y) and sorted by increasing x, then phase, which is the exact all-epoch chronological order for west drift(-2,0). Each class must alternate. Exactly two first-L classes must occupy one row, and exactly two final-black classes must occupy one row. No output debris is permitted in this specific probe.

Every nontrivial quarter-turn period has a north-entry cyclic phase, so fixing entry north does not discard a westward front merely because its supplied literal starts east. The inventory is period-bound and fixes full drift(-2,0), not all possible westward drifts.

Complete bounds:
- length<=24:95631 prefix nodes,1252 endpoint candidates; shifts only-1 and+3.
- length<=36:20248758 prefix nodes,264400 endpoint candidates; shifts only-1 and+3.
- length<=44:20-second timeout before completion; UNKNOWN, no count or exclusion.

The stored example words are LLRR (length4) and RRRLRRRRLLLLRLLLLRLR (length20), cyclic phases of the known shifters. No new bulk gadget emerged. The probe does not test caps, initial finite support, arbitrary wake, drift(-4,0), or all-length realizability. No process remains running.
