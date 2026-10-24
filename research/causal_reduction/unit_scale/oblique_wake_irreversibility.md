# A strict order on parallel oblique bulk interfaces

Independently signed as an LK addendum, 2026-10-23 09:58 UTC.
Independent literal104 profile control: audits/check_oblique_profile_order_independent.py/json.
This is a direct application of the signed scalar clock and LK's finite-orbit
telescoping identity, not a new global clock or an arbitrary-return exclusion.

## Exact periodic statement, with no width bound

Fix an oblique lattice vector D with even coordinate sum and one physical
pose sector. A transverse profile is a D-periodic coloring with only finitely
many black cell orbits modulo ZD. Choose a signed strict scalar clock whose
oblique normal is perpendicular to D, as in
`computability/oblique_strip_clock_obstruction.md`. Its field functional per
longitudinal period is the finite sum

    Phi(B) = -sigma sum_(q modulo ZD) chi(q) f(q) B(q).

The value is independent of the representatives, because f and chi are
D-periodic. Every heading-restoring periodic front that changes complete
bulk profile I to complete bulk profile O satisfies

    Phi(O)-Phi(I) >= 2P > 0,

by summing the literal clock over its event orbits, with head terms cancelling.
The front's finite word has finitely many read orbits, but their transverse
width is NOT fixed in this statement. Spectator black orbits cancel.

If the front drift is mD or -mD, use representatives modulo Z(mD); the profile
functional scales by m. For several parallel commensurate drifts, choose a
common longitudinal period and repeat each front word the necessary number
of times. Every change still strictly increases the same functional.

Consequently there is NO finite cycle of such same-sector parallel front
interfaces whose COMPLETE final bulk profile is its initial profile. Each
front may have a different finite period, different transverse read width,
and either sign of longitudinal drift. Exact complete profile restoration
is essential; a changed rail, extra spectator output, a transverse shift,
an oblique direction change, or a sector change is outside this assertion.

## The standard104 wake cannot be completely erased in its producer sector

The standard NE104 front takes the white profile to its mature12-black-orbit
wake W and has D=(2,2). Hence Phi(W)>Phi(white)=0 in the producer's sector.
A proposed return transducer with drift -mD that takes W back to white,
leaving every other bulk cell white, would have change -m Phi(W)<0. This
contradicts the positive clock increment.

Thus NO periodic return word, of ANY period or finite transverse width,
can completely erase that wake in the same pose sector. This is stronger
than the narrow shifted exact-reversal calculation. It does NOT forbid
another return that leaves a nonwhite residual profile with higher Phi,
or a return that interacts with another wake direction.

The opposite-sector literal time reverse is not a counterexample: sigma
changes sign, reversing the field functional. That sector is not reachable
by an actual continuation of the original ant.

## Finite-length, bounded-end-repair version

Let B_N be the COMPLETE board after N periods of an actual finite-seed
oblique producer, with each checkpoint pose differing only by translation
along D and with the same heading. The scalar head term is constant, so

    Phi_finite(B_N) >= Phi_finite(B_0) + 2NP,

where Phi_finite is the ordinary finite-board field term of the same clock.
Allow uniformly bounded additional initial changes, and final black fields
of uniformly bounded cardinality, provided all these extra/final cells and
the starting/final head poses have normal coordinate in one fixed bounded
interval. Their clock contributions are uniformly bounded, even if the
cells move arbitrarily far along D.

For all sufficiently large N, no actual continuation from that prepared
state can reach such a final field/pose: it would decrease Theta. The
continuation need not be periodic, need not remain in any strip while it
runs, and may take arbitrarily long. Only the COMPLETE endpoint field and
pose hypotheses enter the estimate.

This rules out an all-length finite-wake eraser whose only residue/repairs
are uniformly bounded end gadgets in the same bounded-normal region. It
does not rule out unbounded residual black output, off-strip endpoint
writes with growing clock weight, or a changed head/controller geometry.
It is also a consequence of the existing oblique bounded-write clock
framework, not an assertion that every possible return is impossible.
