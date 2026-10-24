# Near-core retained-ray analytic coupling review

Status at 13:33 UTC: the m=0..10 analytic derivation and all fifteen exact
parent/branch/cycle instances have passed independent review and fresh replay.
The fixed m=11..14 replays remain active, so the combined all-ray result is
not yet marked passed.

Fix m in {0,...,14}; n tends to infinity along a hypothetical recurrent
mass-five subsequence. The retained cell s_m=(-23-2m,31+2m) has u=-54-4m,
outside the blank parent's complete u interval[-34,48]. Hence the existing
blank first-contact reduction applies, forcing q_n. Before the one-bit
parent reaches s_m, the escaping partner a has u tending to minus infinity,
c has u tending to plus infinity, and the relevant extra d is excluded by
its diagonal coordinates. This uses the old complete one-bit parent guards,
not a finite simulation. For each fixed m, s_m is encountered at finite
northwest tail depth before any escaping a.

For each of the nine NE two-bit parents (m=0,2,3,4,5,7,8,9,10), every remote
cell in either four-edge strand has |u| tending to infinity. The finite
prefix and entire NE tail have fixed u bounds, so all are missed. In a
four-cycle, a and c are likewise missed. Only d may interrupt the NE tail.
Its required parity is(even,odd), opposite the certified exceptional
phase72 parity(odd,even). An ordinary impact's complete future is in
z>=z(d)-58. The stationary archive has bounded z above; the two axial gaps
z(d)-z(a)=r-l and z(d)-z(c)=t-b tend to infinity. This is sufficient for
ordinary permanent capture even with the complete archived field retained.

For m=1, the two-bit NW parent has lower/upper u and upper z bounds. The
first strand orientation's a has bounded y and z tending to minus infinity,
so cannot meet its fixed-z NW strip; c and d are excluded by upper u or z.
In the transposed strand, only a can be read. An ordinary a impact misses
the archive by its lower-u bound and d by x(d)-x(a) tending to infinity.
The exceptional a=(-33-2n,2n-21) is forced. The three-bit SE parent has upper
u and z bounds. The transposed strand's c has bounded x and z tending to
minus infinity, while d has z tending to plus infinity, so both miss it.
For a cycle, only c can interrupt; an ordinary impact misses the archive
by upper u and d by y(d)-y(c) tending to infinity. Its exceptional coordinate
is c=(2n-100,-14-2n), fixing d too. The complete five-cell cycle certificate
then applies. None of these arguments substitutes a reflected R/L dynamics.

For m=6, the two-bit SE parent exchanges the order of c and a. In the
transposed strand, c has bounded x and z tending to minus infinity; a has
u tending to minus infinity and d has z tending to plus infinity, so all
are missed. In the first orientation, ordinary c escapes above the archive
in u and above d by y(d)-y(c). Exceptional c=(2n+12,-14-2n) is forced. The
three-bit NW parent excludes the first-orientation a and d by fixed-z,
lower-u and upper-z bounds. In a cycle, only a remains as an interruption;
ordinary a misses the archive and d by x(d)-x(a). Exceptional a=(-33-2n,
2n+93) forces the complete certified cycle. Again both orientations are
checked in the actual, non-reflected dynamics.

For m=11..14, the original two-/three-bit interface formulas and D82 bounds
remain unchanged after exact specialization. The same already-reviewed
Section12 coupling therefore applies. The final NW exceptional ray has even
x, while any remaining a shares q_n's odd x column. The ordinary-impact
half-plane bound handles that last possible interruption.

All archive bounds must include the clean canonical core in addition to the
actual finite field. The new interface checkers do this explicitly; bound
endpoints are taken over every ray before XOR cancellation, which is safe.
An affine capture pose is translated from its n=200 canonical instance with
its exact slope, not assumed constant.

Conclusion conditional only on the fresh replays: these instances plus the
already-audited m>=15 cone eliminate the entire half-ray m>=0 as a retained
mass-five local core. They do not eliminate the rest of D82 or mass five.
