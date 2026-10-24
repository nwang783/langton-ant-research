# Parallel standard legs consume disjoint eleven-level bulk slabs

23 October2026. Analytic proposed architecture restriction; independent review
requested. Not an unrestricted defect budget or a bound on arbitrary endpoint
cap expansion.

## 1. Exact standard profile facts

Normalize d=(-2,-2), transverse coordinate t=x-y, and keep FULL drift cell
orbits (t,x modulo2). The pinned standard104 period has exactly22 touched
full-drift orbits: BOTH longitudinal parity classes at each of11 consecutive
integer t levels. Its stable complete first read on each orbit is R.
Its settled output has12 black orbit classes, including black classes at
BOTH EXTREME t levels of that11-level interval. There is one interior white
level, so it would be incorrect to claim black at every level. These are finite exact properties of the one
pinned literal104 word, unchanged by phase shift, translation or half-turn.
For -d the interval is again11 consecutive levels, with the same properties.

## 2. A physical bulk-packing lemma

Consider several completed genuine standard104 flight legs, all parallel
to +/-d. Assume they cross one common longitudinal bulk band

    Q = {L<=x+y<=U},       U-L>=3,

in which EVERY touched cell has its complete standard local history during
each leg: no initial/final phase fringe cuts a history in Q. Equivalently,
each leg reads every cell of each of its22 orbit classes lying in Q, with
the full stable history. Four consecutive x+y levels ensure every full-drift
cell orbit at a given transverse level has a representative in Q. Assume all
reads between those legs, other than the standard legs themselves, miss Q. Thus endpoint collisions may change their complete caps, but they do
not edit the interior wake that an earlier leg left there.

Then the11-level transverse read intervals of all those legs are pairwise
DISJOINT.

Proof by induction. The first completed leg leaves a black full-drift orbit
at BOTH EXTREME levels of its11-level interval throughout the settled common
bulk. If the next11-level interval overlapped it, their equal lengths imply
that the next interval contains at least one extreme of the old interval.
At that extreme the next leg touches BOTH parity orbits, so it touches an
old occupied orbit. In the common bulk the earlier leg has completed its entire history
there, and all intervening intervals are disjoint by induction, while the
endpoint edits miss the bulk. The cell is therefore still black when this
new leg first reads it. But its stable first read in the genuine canonical
standard trace is R, requiring white. This contradiction excludes the
overlap. The same argument works for either longitudinal direction.

No globally fresh initial-cell assumption is made: the contradiction uses
one actual settled black output identity of an earlier completed flight.
The common-bulk and no-interior-edit premises are essential. Nonstandard
bulk rewriting, short fringes, transverse flights, or edits carried through
the bulk are outside the claim.

## 3. Spatial resource consequence

If all such read intervals lie in a transverse band [a,b] of W=b-a+1 levels,
the number J of legs satisfies

    11J <= W,       J <= floor(W/11).                  (1)

In a supplied itinerary family with arbitrarily long separation between its
endpoint caps, the fixed finite phase fringes can be excluded by taking the
separation large enough for each finite number of legs. Thus no unbounded
number of purely standard parallel bounces can fit in ONE fixed transverse
band while all intervening changes remain endpoint-local.

There is a sector-sensitive sharpening. In ONE actual ant sector, the lower
endpoints of all these11-level intervals have the SAME parity. The canonical
+d lower endpoint is-28; the half-turned -d lower endpoint is18, both even.
A sector-preserving translation has even x-y, and switching the physical
sector shifts every endpoint parity together. Thus disjoint intervals must
have lower endpoints separated by at least12. Consequently

    12J-1 <= W,       J <= floor((W+1)/12).             (1a)

More generally, if the accessible band after J legs has width W_J and a
separate PHYSICAL cap theorem supplies

    W_J <= W_0 + alpha J + C,       alpha<12,

then

    J <= (W_0+C+1)/(12-alpha).                          (2)

For each ADDITIONAL two-leg round trip, the sector-sensitive marginal
width-growth threshold is24 levels. This is not the minimum width for the
first pair: J=2 needs only23 levels by(1a). The parity-free marginal threshold
and its first-pair minimum are both22.
This is a genuine spatial credit, not initial black count or elapsed time.
It does not establish the required cap expansion inequality for arbitrary
ants. A bound on one initial cap's first reaction cannot be iterated on a
changed cap without a separate closure theorem.

## 4. Relation to the exceptional singleton return

The signed first exceptional return has two disjoint11-level slabs (24 black
orbit classes total). The proposed three universal endpoint back-reflections
each add an outgoing and a returning disjoint slab, giving four slabs and48
black classes in the long common bulk. Author-side exact controls in
probe_backreflection_profiles.py/json verify this and retain the finite
collision updates. One recovery enlarges the initial endcap's t-range from
[-82,56] to[-90,56]; the other two remain within[-82,56]. These are just three
first-reaction facts. No bound on every later changed cap, no repeatability,
and no global rank follows from those finite data alone.
