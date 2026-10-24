# A current residual edge is a causal center-path barrier

23 October 2026, 18:22 UTC. This is a local-to-path physical lemma, not a
historical-component connectivity invariant.

Use the signed even-dual active-center representation. A physical cell is
one diagonal edge, and every actual atomic cut has all four edges incident
to its corrected center in the transported K5 core. Therefore no CURRENT
residual edge is incident to that center.

## Exact local gates

Normalize an atomic entry to head (0,0), heading N and sector zero. Its
corrected-center chord starts at (-1/2,-1/2). Enumerating every physical
edge meeting the OPEN chord gives exactly:

* D or C: the edge at cell (0,0), which is before-core, overlaps the chord.
* V: the edge at cell (0,1), which is before-white, crosses the chord at its
  midpoint. V installs a fresh output at that cell after the passage.
* U: exactly four edges meet the chord, all at its midpoint vertex
  (-1/2,3/2). Three are the true inputs a=(-1,1), q=(-1,2), c=(0,2).
  The fourth is the before-white cell (0,1).

There are no other interior contacts. The enumeration box is not guessed:
in doubled coordinates, an edge midpoint lies within one coordinate unit
of any point of that edge. Thus only the chord rectangle expanded by one
doubled unit can contain an intersecting edge midpoint. Direct literal
raw+M11 reconstruction verifies each listed core/input/white role, including
standalone C's empty residual input mask.

Endpoint contacts are controlled separately. Every edge incident to an
actual atomic endpoint center is a core edge at that cut, so an identity
which remains residual cannot be incident there. Indeed, the D input and
both V inputs meet their exit center; U's remaining inputs b=(-1,4) and
d=(0,3) meet its exit center. Such inputs are retired by the consuming base.

## Causal consequence and its precise timing

Let e be the physical edge of an ordered residual identity current at an
actual atomic cut. Trace any later actual atomic-center subarc, inside the
same complete-eight factor, up to but not through the base that retires e.
Then e is disjoint from that entire subarc. At intermediate atomic vertices
it cannot be residual and core simultaneously. Inside D/C chords it would
be core; inside V it would be before-white; inside U it would have to be a
true input and hence retire at that base. These exhaust the possibilities.

At the retiring base contact IS permitted: a U input can first meet the
center chord at its midpoint or endpoint, while a D/V input can first meet
it at the endpoint. The raw physical L deletion need not coincide with that
geometric chord contact. Ordered residual retirement is the relevant event.
If U recycles a consumed cell as a fresh output, the replacement is a NEW
identity; the old edge-barrier lifetime has ended and the fresh lifetime
starts after that installation. No claim identifies those two identities.

The argument uses actual atomic cuts and the literal D/V/U/C masks inherited
inside a complete recurrent-eight factor. It is not an arbitrary-word
extension of the retained language and does not extend beyond a finite
factor's terminal actual marker.

## Remaining topological gap

A CURRENT connected live archive is a genuine geometric obstacle until one
of its identities retires. But a historical incidence component need not
have a connected current archive. Connecting its pieces by a ghost wire,
or by all core edges, is not justified by this lemma. In particular it does
not prove that a U must merge two incidence components. The signed
disconnected-archive and artificial-coloring controls remain applicable.

Reproduction: check_current_residual_edge_barrier.py, which binds the
literal geometry and signed active-center coordinate bundle and records
every candidate cell and exact rational contact.
