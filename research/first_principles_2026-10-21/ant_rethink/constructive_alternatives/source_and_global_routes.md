# Constructive routes and source check

21 October 2026. This note records the outcome of a further search for a full
finite-support proof or a finite counterexample. Neither was obtained.

## Primary source status

The current primary repositories were read directly through the GitHub tool.

- Atharva Jillhewar's `langtons-ant-highway` README still explicitly says that
  its results neither prove nor disprove the highway conjecture. Its periodic
  constraints leave both an entrance problem and a classification problem.
  https://github.com/Atharva12456/langtons-ant-highway
- Hao Ke's `langtons-ant-core` README lists seven projects. Its final research
  section explicitly says that their combination is not an all-input
  convergence theorem. The README blob read was
  `f916bf23c517936910cf1fedca5c72e6a94f1c93`.
  https://github.com/kehao95/langtons-ant-core
- Gajardo, Moreira and Goles, *Complexity of Langton's ant*, distinguish
  finite-support circuit evaluation from their universality construction.
  The latter requires an infinite, finitely described initial field. Its
  undecidability result therefore does not settle this finite-seed problem.
  https://doi.org/10.1016/S0166-218X(00)00334-6
  https://arxiv.org/abs/nlin/0306022
- A later primary-source check by the parent analysis found the arbitrary
  two-initial-black theorem in the 5 October 2026 revision 5 of
  `imfinn/langton-two-black/paper/TWO_BLACK_CELLS_REVISED.md`. Its scope is
  translating P104 for every two-black input, not the general conjecture.
  The parent handled the independent source review; the constructive branch
  did not count that review as its own replay.
  https://github.com/imfinn/langton-two-black

 A failed
proof search is neither. An independence statement also requires a specified
formal theory and a proof of independence. None is supplied here.

## Self-renewing scattering

Ke's current return-scattering construction includes a genuine return to a
black cell created by the ant on an earlier approach. It allows any finite
number of prescribed packets, with all old writes retained. Each packet uses
three black markers installed at input time. The source separately proves
that its two-marker version converges in a different outgoing direction.

Thus removing the third marker does not give a free reset. The source's
composition proof is a useful interface contract, but it is not a self-renewing
finite controller.

The third marker is q3=(177,-260), with s=x+y=-83 and r=x-y=437.
The inherited history permitted by the interface lies in s<-160, so it
cannot supply q3. In the composable family, the next primary has displacement
Delta(m)=(2m+208,2m-242), with m>=100. Its s coordinate is 4m-34>=366;
the next reset marker is therefore at relative s>=283. The current packet's
entire read envelope has s<=59. Thus earlier packets cannot manufacture
that next marker while retaining the proved guards. A self-generated
replacement would have to change the guard conditions and analyze the
newly exposed history explicitly.

Source read:
https://github.com/kehao95/langtons-ant-core/blob/main/four_cell_port/proof/return-scattering-closure.md
Blob: `a2818eff029aef45e12ffd2c843fbab560cd3b46` is the note's stated historical
base, not the current content hash. No historical base was treated as a replay
certificate in this investigation.

The separate defect-dynamics branch tested a different two-reversal mechanism.
Its two phase-72 reversals return to the old lane. The constructive branch did
not duplicate that computation or assert that the first old-lane contact resets
the original reflector. Its results and evidence belong to that branch.

## Bounded defect locations and the axis-cross gap

The current primary factor-language proof shows that if all late forbidden
ten-turn windows occur in a fixed finite set K, the trajectory lies in a fixed
horizontal/vertical cross. Its universal padding is 44. It does not prove that
this axis-cross behavior is impossible.

Source read:
https://github.com/kehao95/langtons-ant-core/blob/main/factor_language/proof/silent-axis-return.md
Blob SHA: `129e83f0792c021b5e33ef95061624aca842d6ba`.

The non-axis-strip proof in `oblique_strip_pumping.md` cannot be applied here.
At an ordinary axis boundary there is only one outward neighbor. The two
adjacent-neighbor visit assignment needs two. This is a mathematical difference
in the hypotheses, not a missing choice of coordinate labels.

A proposed mass argument also remains incomplete. A physically feasible
ten-legal word of length L has net black change at least (3L-322)/26, by the
primary mass-defect theorem. Hence a long silent excursion creates black cells.
But short excursions near K can erase cells that those long excursions create.
The number of such episodes has not been bounded. Summing the word inequality
does not give a monotone resource on the old exterior field.

The source's explicit silent fold shows why an endpoint-only bound is false:
the endpoints can be fixed while the excursion length and depth increase.
The size of its prepared initial ribbon increases too. Its later autonomous
continuation is certified to reach the standard highway. It provides neither
an infinite controller nor an unconditional exterior resource bound.

## What the new conditional theorem implies globally

The complete crossing-history criterion proves that any directionally escaping
nonperiodic path must fail at least one of these uniform bounds:

1. the number of crossings of a far vertical cut;
2. the vertical diameter of that cut's complete crossing history.

More geometrically, no nonperiodic path can have a tail in a finite union of
fixed-width non-axis strips. This permits unbounded transverse deviation in
one limiting direction. An asymptotic direction alone is insufficient. For
example, the geometric curve (n,n+floor(sqrt(n))) has one limiting direction
but no fixed-width diagonal strip. This is a geometric warning, not a claimed
Langton-ant trajectory.

No argument here forces infinitely many distinct event directions. No argument
turns first-read whiteness into the required uniform crossing-history bounds.
The currently established finite-support condition prevents initially prepared
infinite fuel, but newly written black cells can later be consumed. A valid
global proof must control that production and reuse rather than omit it.

## Further global results proved in this investigation

The signed-cut audit and the later occupation-count argument give complete
global consequences for all finite inputs:

- `signed_cut_and_explicit_mass_bound.md` derives the two-endpoint bound
  `||p_t-p_s||_infinity <= (|B_s|+|B_t|)/2+1`, an explicit exponential time
  bound for exceeding any black-mass ceiling, and the precise limitations
  of those endpoint charges.
- `explicit_low_mass_occupation_bound.md` proves uniform power-law decay
  of the frequency of every fixed black-mass ceiling. It supplies explicit
  constants and a uniform rate of divergence of mean black mass.
- `bounded_directional_retreat.md` proves eventual translation-periodicity
  if two independent linear coordinates have bounded retreat. It includes
  an explicit proof that the discarded black cells are never read again.

These are distinct from the completed oblique-strip/crossing-history criterion.
None proves the needed geometric premise or classifies every possible
periodic highway. The full finite-support conjecture remains unresolved by
this branch.
