# Radius-parametrized compactness and actual helper routes

24 October 2026. A direct refinement of `FINITE_SOURCE_OLD_REMOTE_HELP.md`
(a858ddf0), not a quantitative conjecture or a termination argument.

## 1. Every fixed source radius has a finite first-read maximum

For an integer R>=0, let G(R) be the maximum finite first-read time of a
marked initially black cell over ALL full boards supported in [-R,R]^2,
all four headings, with initial head0; include0 in the maximum. There are
exactly4N*2^(N-1) such states, N=(2R+1)^2, so G(R)<infinity. The same
effectiveness qualification as for F applies: this definition is not a
computable cutoff. In particular F(M)=G(4M) in that note.

In a completed marked episode (e,d,c) with supplied cap M, let R>=4M.
If no old-cohort lifetime outside p_d+[-R,R]^2 is consumed through c,
delete those old outside cells ONCE. All are unread, so execution and
the FIRST marked read are identical. The marked component was already
inside4M, hence retained. Thus c-d<=G(R). Contrapositively:

    c-d>G(R) => an actual old helper is consumed at a cell y
               with L=||y-p_d||_infinity>R, at an update d<=j<c.

This uses the ORIGINAL supplied M and R throughout; it recomputes neither
parameter from the reduced field.

## 2. Exact route inequalities for that particular helper

If the helper lifetime f was R-born at update b, then the physical head
read y at b, is at p_d at cut d, and reads y again at its consuming update
j. Unit-speed motion along these ACTUAL three points gives

    j-b >= ||p_d-y||_infinity + ||y-p_d||_infinity = 2L.

This birth-age bound needs no cap assumption before d. It does not treat
unread cycle support as a causal input and does not charge a rebirth to an
earlier lifetime at the same coordinate.

For the waiting-time statements, assume additionally that f has a previous
active-to-dormant departure cut s, the last such cut at or before d, and
that cap M holds also at s-1. Let a be its first active cut after s.
Because it is dormant at d, s<d<a<=j. The departure metric gives
||p_s-y||_infinity<=M+1. The cap at its actual reimport gives
||p_a-y||_infinity<=M. Therefore

    d-s >= L-M-1,
    a-d >= L-M,
    a-s >= 2L-2M-1,
    j-s >= 2L-M-1.

Here a-s is the length of a genuine COMPLETED frozen dormant interval,
not just a last-import age or a presumed uninterrupted wait. The helper
may undergo further reattachments after a. Its first reimport cannot be
assumed to be its final productive one. If s lies before a sustained-cap
tail, the metric premise at s-1 must be checked separately.

## 3. Sequence consequence and exact remaining gap

Along any sequence of completed episodes with a COMMON fixed cap M and
unbounded lags c-d, choose increasing radii R>=4M and episodes whose lags
exceed G(R). The selected helpers then have unbounded actual distance L
from the corresponding departure head. They must include distinct
consuming events: a fixed event j has L<=j-d<=j. On one fixed finite-seed
trajectory, only finitely many lifetimes are born in any finite prefix,
and each is consumed at most once. Excluding those finitely many events
leaves arbitrarily late-born selected helpers. Their actual consumed ages
are unbounded by j-b>=2L.

If a sustained M-cap covers their departure cuts s-1 as well, their own
completed dormant intervals are unbounded by the displayed route bound.
Early-departing lifetimes form only a finite prefix cohort and can be
excluded when selecting infinitely many distinct helper events.

This is an existence-of-far-actual-input statement, not a rate: no linear,
polynomial or other effective relation between lag and radius is supplied.
It does not say that the helper chosen at the fixed radius4M must be the
far helper chosen at a larger radius. An arbitrarily long parent may have
many differently placed helper events.

The chronological relation is still s<d<=j<c, with sharing between parents.
It permits indefinitely replenished forward families of earlier helper
episodes. The route lower bounds do not decrease any whole-archive
resource and do not prove eventual translation or finite-seed capture.
