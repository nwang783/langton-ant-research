# A two-parameter exceptional rectangle with a retained local core

22 October 2026. Exact computer-assisted result; the new two-variable arithmetic
and its use are submitted for independent review. This is a specified family,
not the general mass-five recurrence exclusion or the finite-seed conjecture.

## 1. The theorem

Use white/right, black/left, flip, then move; north is positive y and headings
N,E,S,W are0,1,2,3. For integers m>=100 and n>=m+100, define

    s_m=(-23-2m, 31+2m),
    q_n=(-33-2n,-14-2n),   a_n=(-33-2n,41+2n),
    c_n=(  8+2n,-14-2n),   d_n=(  8+2n,41+2n).

Start at(0,0),N with exactly these five black cells. Then at

    T(n,m)=416n+312m+197704

the ant is at(-2m-28,2m+68),N and follows a fixed cyclic phase of the standard
104-letter highway word forever, with drift(-2,2). The initially black cells
a_n and d_n are never read, so either or both may instead be omitted.
The exact first input reads are

    q_n: 104n+10881,
    s_m: 208n+104m+70810,
    c_n: 312n+208m+142996.

Every read in the entire finite prefix and infinite tail belongs to

    D82 = { (x,y): |x+y|<=82 or |x-y|<=82 },

uniformly in both parameters. The final tail lies in the narrower strip
|x+y|<=45. The capture time is sufficient, not asserted earliest.

For each fixed m, the local limit as n tends to infinity is the singleton
{s_m}. The entire blank orbit has -34<=x-y<=48, checked against its exact
permanent tail. Since x(s_m)-y(s_m)=-54-4m, the singleton is untouched by the
blank parent. It is first encountered only after the remote exceptional
q_n collision has returned and launched the northwest highway. Thus this
is a genuine retained-core interference family, not a perturbation discarded
because it was never read.

## 2. Relation to the existing rectangle and the useful mechanism

The old rectangle has three successive exceptional contacts q_n,a_n,c_n.
Here s_m is on the same northwest exceptional phase-72 ray as a_n, but occurs
strictly earlier. It substitutes for that northwest contact. After the return
from s_m, the southeast parent rejoins the same fixed pose(40,-50),S as the old
rectangle. The next contact is still c_n. The final return resolves to the
northwest, on a track which misses the unused a_n and d_n.

The old rectangle's fixed recovery words survive unchanged. Their highway
flight counts separate into independent southwestern and northwestern lengths.
This is the reusable feature: a bounded retained bit can replace an expanding
corner without reusing a history-free scattering rule or deleting any old
marks. The exact complete-field certificate supplies the required interaction
closure for this whole two-parameter geometry.

The result eliminates this family with remote rectangular partners along the
far phase-72 retained-core ray. It does not eliminate all remote incidence
shapes for these singleton cores, arbitrary singleton cores on D82, or arbitrary
archives of a one-black parent.

## 3. Witness word and discovery/proof separation

`discover.py` recorded finite runs, and `extract.py` compared n=200,201 with
m=100 to propose the fixed words in `template.json`. That extraction is not the
proof. The bivariate checker verifies every proposed color independently for
all allowed m,n. The witness pieces are:

    fixed9977; W0^(n+8); fixed51118; W0^(n+7); fixed8078;
    W99^m; fixed51123; W0^(m+2); fixed22936;
    W100^(n-20); fixed51122; W0^(n+m+10); fixed2622.

Here W_r denotes the stored standard phase in that stage's actual heading;
all period words are explicitly tested as cyclic phases of canonical W.
The fixed suffix determines the final phase, which is separately tested as
standard before its infinite validation. The template SHA-256 is
05c5fca0529ffb365a499a92ece844fd6cb4520cc8465f4d2027c049b66f222f.

## 4. Exact two-variable arithmetic

`bivariate.py` uses independent nonnegative integers

    u=m-100, v=n-m-100.

A scalar(a,b,c) means a*u+b*v+c. Thus there is no hidden upper bound or sampled
range. A point consists of two such scalars. The complete color field is the
XOR of finite affine point terms and finite diagonal-ray terms, just as in the
previously audited one-variable engine. All old writes are retained.

The changes needed for two variables are explicit:

- An affine scalar is nonnegative throughout the orthant if all three
  coefficients are nonnegative. A strictly negative guard requires both
  variable coefficients nonpositive and the constant strictly negative.
  The checker rejects any ordering not proved by those sufficient guards.
- For a*u+b*v+c=0, existence of a nonnegative integer solution is checked
  exactly. Zero coefficients reduce to divisibility. Opposite-sign nonzero
  coefficients admit such a solution exactly when gcd(a,b) divides -c.
  For same-sign coefficients, normalize to positive a,b and target t=-c;
  t<0 is impossible. Otherwise solve a*u=t mod b for the least nonnegative
  residue u0, after dividing by the gcd. A solution exists exactly when
  a*u0<=t, since all other nonnegative solutions for u are u0+k*b/gcd.
- Two affine coordinates vanish together either at the unique rational
  solution of a2x2system, tested for integrality/nonnegativity, or on a
  dependent equation handled by the preceding exact test. Inconsistency
  excludes the intersection. Possible parameter incidences are rejected,
  not silently tested at the base point.
- Ray intersections reduce to the same affine line equations and diagonal
  determinants. Affine quotient coefficients must be integral uniformly;
  any unhandled residue-class dependency is rejected.

Every fixed-word read is checked against the complete field. For a repeated
period, old points/rays and earlier copies of the same period give exact
intervals of epochs. Their XOR parity boundaries must cancel identically.
The final tail uses the same construction over all epochs k>=0, with finite
intervals and half-lines. Cancellation proves every future read simultaneously,
for every m,n in the domain.

The current successful run records21,118 fixed read requirements,292 periodic
read requirements,19,637 affine guards, and83,662,133 point-incidence exclusions.
These are proof-work counts, not parameter samples. The exact chronology and
never-read claims are separately checked against all read points and rays.

`test_bivariate.py` is a supplementary implementation control:4,961 small
scalar equations and10,000 point-pair equations agree with literal finite
enumeration, and distant isolated incidences at10^6 and10^60 are rejected.
The all-parameter argument is the integer arithmetic above, not those tests.

## 5. Independent geometry interface

`check_geometry.py` reconstructs every finite and periodic read symbolically
without using color fields. For each finite point, one diagonal normal has
zero coefficients of both u and v. For each periodic read ray, the same normal
also annihilates the period drift. Its constant absolute value is at most82.
The infinite tail is handled identically. This checks197,704 read identities.
The geometry is valid independently of parameter size; its use as actual
trajectory geometry depends on the separate complete-field color certificate.

## 6. Reproduction and files

    python certify.py
    python certify_bivariate.py
    python check_geometry.py
    python test_bivariate.py

The first command is the independently reusable old one-variable engine with
m fixed at100; it checks every n>=200. The second proves the full bivariate
statement, producing `bivariate_certificate.json`. The latter two commands
produce `geometry.json` and the arithmetic control output. The literal words
and discovery runs are retained, but need not be regenerated to verify the
certificate. All dependencies point to the recovered exact engine, not to an
unavailable external dataset.

## 7. New complete-history prefix interfaces

The extended checker also removes the proved-unread a_n,c_n,d_n at the end of
stage8 and verifies the complete infinite future of the two-bit parent
{q_n,s_m}. It reaches(40,-50),S at

    T2(n,m)=208n+208m+145000,

then follows phase100 forever with drift(2,-2). Both its complete field at T2
and every earlier read obey

    -4m-130 <= x-y <= 98,   x+y <= 71.

The entire future tail has -15<=x+y<=-5 and increasing x-y, so its whole future
has x+y<=71. Its prefix and tail are both in D82. The corresponding canonical
phase100 core has88<=x-y<=98, so its XOR archive also has upper bound98.

For the three-bit parent{q_n,s_m,c_n}, the complete field at final tail entry
and all finite prefix reads obey

    x-y >= -4m-130,   x+y <= 75.

The final tail has35<=x+y<=45. Its placed phase100 standard core obeys
x-y>=-4m-104, so the XOR residual between the real field and that canonical
core still obeys x-y>=-4m-130. These support bounds are conservative: they
bound every affine point and ray endpoint before using cancellations.

The independent `interface_geometry.py` binds these interfaces to canonical
finite standard cores and gives the final phase72fresh-cell ray exactly:

    (-2m-36,2m+72) + j*(-2,2), j>=0.

Every cell on it has even x. In contrast q_n's x-coordinate -33-2n is odd.
Thus a cell sharing q_n's column cannot make a phase72exceptional first hit
on this final northwest tail. This parity mismatch is a promising analytic
closure condition for more general remote partners, but this note does not
silently promote it into a general mass-five theorem. It still requires the
separate exposure and complete-history ordinary-channel arguments.


## 8. Expanded depth domain and fixed boundary cases

The separate `certify_threshold15.py` replays the identical complete-field
argument, including all prefix interfaces, with independent variables
u=m-15 and v=n-m-100. It passes for every m>=15, n>=m+100.
`check_threshold15_geometry.py` gives the same D82 confinement. This
enlargement awaits the same independent audit; the original m>=100
artifacts are unchanged.

Attempts to replace15 by11 or12 in the conservative bivariate engine are
not proofs: the engine correctly refuses point coincidences occurring on
the parameter boundary. This is not a detected color mismatch. Fixed-m
instances can instead normalize those coincident terms identically.
`certify_boundary_fixed.py` checks m in{11,12,13,14} separately, with
N=(0,1,200) and M=(0,0,m), so all n>=200 are covered. Completed outputs
are `boundary_m*_certificate.json`; an absent output is not a result.
The output retains the full two-bit and three-bit archive/read interfaces
and the exact infinite future.
