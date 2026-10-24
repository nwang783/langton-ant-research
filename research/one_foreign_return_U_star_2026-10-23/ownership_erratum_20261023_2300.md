# Returned U/UC physical-read ownership correction

23 October 2026, 23:00 UTC.

The main note's statement "U/UC: phase 25, inside its own RAW" is incorrect. In ALL queried U/UC returned-star gates, the original tag aligns with upper input slot (-1,4). Its actual first read is returned phase 29 L.

- Plain U RAW has length 28. It absorbs the original tag into its exit core; the FOLLOWING word's RAW phase 1 owns the first physical read.
- UC RAW has length 43. It owns that phase-29 read itself, namely its actual C-tail phase 1.

Thus all three plain bases D/V/U have the same ownership pattern: first old-star read at RAW length plus one, physically owned by the following word; DC/VC/UC own the corresponding read inside their own C tail.

The frozen checker and JSON already reconstruct all these phases and ownership fields correctly. Across all 24 U/UC rows, every phase is 29, with twelve plain-U following-word reads and twelve UC RAW reads. The original frozen files and earlier arithmetic erratum are preserved unchanged. The 37/35 ancestry partition and all necessary clock bounds are unchanged, but any prose description of a plain U RAW retirement must be read as exit-core absorption instead.
