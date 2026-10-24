# An exact computability boundary for the directed architecture

23 October2026. Consequence of the independently accepted finite-front
reduction, not a hardness classification of Langton's ant.

## Decidable supplied instances

The following fully supplied finite-input problem is decidable:

- explicitly given finite literal palette, common restored heading and common
  nonzero displacement;
- explicitly given periodic background on its full-drift orbits;
- explicitly given finite cap, or the request for some finite arbitrary-flip
  cap, or for some finite black-additions-only cap;
- question: does an infinite legal palette decomposition exist?

The finite-front graph and the correct reachability/cycle tests decide it.
The palette, period and cap can vary with the instance. There is no uniform
small bound needed: each encoded instance has an effectively finite graph.
Explicit code resource limits are implementation UNKNOWNs, not mathematical
undecidability.

Therefore no total effective reduction can map the general halting question
into this precise supplied survival problem (or its complement). Composing
such a map with the finite-front algorithm would decide halting. Any proposed
universal-computation construction inside this architecture must break at
least one hypothesis: for example unbounded relative memory, changing drift,
nonperiodic supplied input, or an unsupplied eventual-entry certificate.
This does not refute universality constructions in other ant models or on
more general prepared backgrounds.

## The quantifier that has not been removed

For a finite-seed orbit, the statement

    exists an eventual directed finite-palette decomposition

is equivalent to eventual nonzero translating periodicity, by
`directed_palette_determinism_corollary.md`. The finite-front decision takes
the palette and entry board as SUPPLIED inputs. It does not decide this
existential eventual-representation statement on an arbitrary seed.

Searching all finite entry times and palettes can semidecide a successful
representation; failure of every supplied architecture test does not produce
a finite negative certificate. A countable existential union of decidable
instance classes need not itself be decidable. No undecidability or
unrecognizability of this actual ant problem has been established here.

Thus this route supplies a rigorous, non-speculative distinction relevant to
halting-based ideas: the explicit directed local architecture is decidable;
the unsolved global quantifier is whether a trajectory eventually enters any
such architecture, followed by classification of the resulting translator.
Replacing that quantifier by a macro-language slogan would assume the very
eventual-translation premise still missing.
