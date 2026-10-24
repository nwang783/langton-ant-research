# Mandatory lifetime-metadata clarification

24 October 2026. This qualifies the frozen EXACT_ACTIVE_COMPONENT_FLIGHT.md
SHA47b81e90, without changing its physical field or first-import theorem.

The code exports complete physical edge sets, exact detachment phases, and
period indices. It does NOT export an explicit original R-birth timestamp for
every emitted edge. Section5's phrase "birth/detachment phase" must therefore
not be read as claiming that such a birth-metadata API is implemented.

Before the first import every archived edge retains the same current black
lifetime: no intervening physical read, erasure, or rebirth occurs. That precise
edge-identity and no-read statement, plus the time of detachment, is what the
full-field output preserves directly. Original-birth labels could be recovered
from the literal history but are not part of the current returned data.

No infinite or synthetic trajectory is added by this clarification.
