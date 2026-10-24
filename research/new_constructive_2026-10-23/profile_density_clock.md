# A normalized strict clock orders ALL complete parallel bulk-profile conversions

23 October2026. Author analytic corollary of the independently signed oblique
scalar clock/cylinder theorem, exact rational controls; independent review
requested. This is NOT a new global ant rank or finite-seed capture proof.

## 1. Hypotheses: complete profiles, one axis, one sector and one anchor

Fix the NE/SW axis, t=x-y in FIXED physical coordinates, an integer center c,
and one conserved pose sector bit epsilon=x+y+h mod2. Write sigma=(-1)^epsilon.
A complete mature profile S is a binary periodic function S(t,x mod n), for
some finite positive longitudinal period n, with black support in finitely
many actual normal levels t. It includes ALL passive black bands, not only
what the next word reads. Put

    rho_S(t) = (number of black residues x modn at normal t)/n.

A complete profile conversion I -> O means an actual periodic translating
ant interface whose heading-restoring turn word has length P>0 and FULL
nonzero displacement(s,s). Its chronological histories on every read orbit
start with I and end with O; every unread orbit retains its complete input.
The initial interface can have an arbitrary finite head/cap correction and
finite transient. These do not alter its mature I/O profiles.

We do NOT call two full finite ant boards 'profiles' by taking a far-infinity
limit: every finite board would give the zero profile. This theorem concerns
specified infinite prepared BULK INTERFACES and their valid complete input/
output contracts. Transferring it to a proposed finite-family construction
requires proving that interface separately. A sequence of abstract interfaces
is not automatically one finite-seed orbit.

## 2. A potential independent of profile-period representation

Set

    f_c(t)=6(4^(t-c)+4^(c-t))-2 >0,
    Phi_c(S)=sigma sum_t (-1)^t f_c(t) rho_S(t).           (1)

This is a finite rational sum. Refining the longitudinal period from n to kn
does not change rho or Phi. The normal center and sector stay FIXED through
every comparison; recentring a new endpoint for free invalidates telescoping.

### Theorem

Every conversion in Section1 satisfies

    Phi_c(O)-Phi_c(I) >= 2P/|s| >=4.                    (2)

This holds for arbitrary new words, periods, strides, read widths and visit
counts. Positive or negative ordinary black-mass charge is permitted.

## 3. Derivation from the retained exact scalar clock

Use computability/oblique_strip_clock_obstruction.md and the signed
causal_reduction/unit_scale/oblique_cylinder_capfree_bound.md. A fixed90-degree
rotation changes the world normal t to the rotated coordinate sum, reverses
the sector sign, and preserves checker parity. Taking a=b=4 gives

    delta=1/3, M=6,

and r chosen for the fixed center gives the weight f_c above. Every actual
fine update increases the corresponding full clock by AT LEAST2. The field
coefficient in unrotated NE/SW coordinates is +sigma*(-1)^t f_c(t), which
explains the sign in(1). The head correction depends only on normal position
and heading, so it is invariant under every displacement(s,s).

First suppose I/O are periodic with the full stride |s|. Sum the exact local
clock increments over one period modulo Z(s,s). All head terms cancel.
At each orbit R count minus L count is exactly O-I by its COMPLETE alternating
history. Hence

    2P <= sigma sum_(orbit q) (-1)^(q_x+q_y) f_c(t(q))
                              [O(q)-I(q)]
        = |s| [Phi_c(O)-Phi_c(I)].                      (3)

No divergent clock sum on an infinite background has been assigned a value:
this is a finite sum over the finite read-orbit set. Adding unread support
orbits contributes zero, precisely because complete O equals I there.

For arbitrary finite periods n_I,n_O, choose a common multiple L of them
AND |s|. Lift the supplied word to k=L/|s| repeats. The same proof gives

    2kP <= L [Phi_c(O)-Phi_c(I)].

Cancel k and L to obtain the first inequality in(2). The ant makes P unit
moves with net Manhattan displacement2|s|, so P>=2|s|, proving the second.
Each transition may use its OWN common-period lift; no finite common period
for an entire infinite sequence is needed, because Phi already uses densities.

A finite cap/transient affects only finitely many cells. It cannot change the
mature orbit counts used in(3). Conversely, distributed output or helper bands
cannot be omitted as 'cap': their contribution must stay in the profiles.

## 4. Consequences for renewal and changing-period architectures

### No exact reverse bulk replenisher at the same alignment

If I->O occurs in a fixed sector, then ANY complete conversion O->I in that
same sector/normal frame would have NEGATIVE Phi change, contrary to(2).
It need not use the exact time-reverse word: no alternative longer word,
wider read set, different stride, new finite cap or physical phase can help.
An output matching only the old READ-support input, with new passives retained,
is a DIFFERENT complete profile and is not excluded by this reset statement.

The same prohibits a nonempty finite cycle of complete profiles, or even of
their normal-density vectors rho. Longitudinal translations leave rho
unchanged. Normal translations need not leave Phi unchanged and cannot be
silently factored out.

### A finite phase budget in one fixed normal support interval

Suppose every complete profile in a sequence has black support within ONE
actual interval a<=t<=b. At each t, 0<=rho(t)<=1. Therefore the entire possible
range of Phi is

    Phi_max-Phi_min = sum_(t=a)^b f_c(t).

Every complete phase increases Phi by at least4. The number J of such phases
thus satisfies

    J <= floor((Phi_max-Phi_initial)/4)
      <= floor(sum_(t=a)^b f_c(t)/4).                    (4)

The periods, words, read widths, charges and finite caps may vary arbitrarily
from phase to phase. Reads may go outside[a,b]; unchanged white0->0 orbits
there contribute zero and do not weaken the bound. This is a complete-BULK-
phase bound, not a bound on an arbitrary finite endpoint transient or hidden
interior work.

Thus repeated full-field replenishment in a fixed oblique corridor cannot be
rescued merely by changing its periodic word. A genuine infinite construction
must escape these hypotheses: unbounded normal widening/moving coordinate
support, changing directions, nonperiodic bulk evolution, or new complete
passive profiles outside the proposed corridor. Those remain open.

## 5. Direct application to the known15324 output and exact controls

For the signed15324 source, I is the COMPLETE964 period26 input (lifted to2892
classes mod78), and O is the COMPLETE3300 period78 actual output including BOTH
exterior helpers. The original ant has sector bit0. The actual15324 word has
s=-78, P=15324, so (2) gives

    Phi_c(O)-Phi_c(I) >=5108/13 >0.

Consequently NO same-sector parallel periodic consumer can restore EXACTLY
that complete old4352-output profile I from O at the same normal alignment.
This is stronger than the exact-inverse15324 sector test: it covers EVERY
replacement word and any period/width, but also requires COMPLETE restoration.
A new eraser that leaves a different growing archive is not excluded.

profile_density_clock.py/json reconstruct both complete profiles from the
literal15324 parity mask, evaluate(1) as EXACT Fractions at three fixed centers,
and check the forward lower bound. The same-sector reset has the exactly
negative change. As an essential nonvacuous reversal control, reversing the
SECTOR changes the sign and admits the positive exact-reverse budget. The
checker also validates common-period lift invariance and the exact range
formula on a small fully enumerated density box. Numerical controls supplement
the inherited universal local-clock algebra, not replace it.

## Scope and inherited sources

- computability/oblique_strip_clock_obstruction.md: signed strict scalar clock.
- causal_reduction/unit_scale/oblique_cylinder_capfree_bound.md: signed finite
  quotient summation and prescribed-input front framework.
- prepared15324_return_normal_form.json and literal15324 wave: complete source
  and output, all passive helper bands retained.

No global original-mass budget, arbitrary-ant monotone natural-valued rank,
bounded initial-diameter theorem or universal finite-seed capture is claimed.
The fixed normal anchor, physical sector and complete-field requirements are
essential. Axial transport, arbitrary changes of direction, widening endpoints
and nonperiodic supply are not covered by this corollary.
