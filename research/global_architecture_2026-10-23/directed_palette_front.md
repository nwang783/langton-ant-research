# Focused executable colored-front controls

23 October2026. Author implementation, independent implementation audit pending.
The analytic theorem is independently accepted at proof SHA71628c306bf... .

`directed_palette_front.py` accepts a SUPPLIED finite list of nonempty literal
R/L words. Every word must restore one common heading and have exactly one
common nonzero displacement. `FrontArchitecture` builds full-drift orbits,
exact front intervals and literal phase rows; it does not generate a palette.
`PeriodicFront` receives one binary periodic-input row per orbit, with a common
known positive period.

- `edges((phase,bits))` executes every supplied literal word against the actual
  stored-front and fresh-top colors. Returned edges are exact, including all
  multiple visits within a block. Retired debris remains on the physical board.
- `decide(cap=None)` decides unknown finite XOR-cap existence by cycle search,
  returning a literal cycle and at-most-front-size color-flip cap on success.
  Here `None` means SOME finite cap, not the empty cap.
- `decide(cap=[])` checks the unmodified supplied background. A nonempty list
  gives a SPECIFIED finite set of initial XOR flips. This may whiten prepared-
  black cells; black-additions-only existential reachability is not implemented.
- Specified finite caps are processed through their last exceptional fresh-top
  input at time k-U_a. All later effects are retained in the exact front, so
  there is no need to simulate through the later last potential read k-L_a.
- Exact cycle search uses iterative DFS. A separately completed DAG gives an
  exact maximum remaining block count. The phase clock is part of every vertex.
- State-count or finite-prefix budget exhaustion returns an explicit UNKNOWN.
  No incomplete graph, truncated prefix or missing edge is treated as a
  mathematical negative. Caller budgets do not alter literal transition logic.

This code does not implement the separate controlled-input black-addition
criterion, a symbolic compiler for10^104 palettes, generic standard producer
construction, cap synthesis or unrestricted ant reachability.

## Executed author controls

`check_directed_palette_front.py` compares25,744 transitions with a separate
physical-coordinate board replay on four small supplied palettes, all headings,
and every binary prepared profile of periods1/2. It compares1,744 tiny graph
cycle decisions with a transitive-closure oracle and replays64 returned cycles.
Remote supplied caps force failures after37/50 legal blocks; retired off-strip
caps are harmless; prefix/state budget controls return UNKNOWN. The retained
standard104 white-input seed is accepted through its nontrivial18-bit front.
These are implementation controls, not an independent audit or a new ant search.
