# Narrow terminology clarification

24 October 2026. In `RADIAL_SQUARE_WHITE_START_ORDERED_PORT_MODEL.md`, the phrase "64-state local transition table" means a table of64 transitions:16 patch color states times4 possible incoming ports. There are16 color states, not64. The actual checker and explicit96-entry construction use this correct16-state/64-transition automaton. No mathematical claim, data, protocol, or scope is changed.
