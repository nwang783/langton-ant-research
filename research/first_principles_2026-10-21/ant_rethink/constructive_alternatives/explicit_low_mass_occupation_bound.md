# An explicit uniform bound on the frequency of low black mass

## Statement

Let M_t be the total number of black cells in an arbitrary finite-support
Langton-ant trajectory. For an integer K>=0 define

    D_0=1,
    D_K=2K*D_(K-1)+1  for K>=1,
    C_K=2(K+1)*9^K.

Then, for every starting time s and every integer N>=1,

    #{t in [s,s+N): M_t<=K}
      <= min(N, C_K*N^(1-1/D_K)).

The bound is uniform over all finite input fields, their diameters, their
initial black counts, their positions, and their headings. The first few
D_K are 1,3,13,79,633,6331. Equivalently,

    D_K=2^K*K!*sum_(j=0)^K 1/(2^j*j!).

Thus the frequency of every fixed bound on black mass tends to zero with
an explicit power-law upper bound. This is a bound on frequency, not a
proof that M_t tends to infinity at every time.

## Dependencies and proof status

The proof uses the classical unboundedness theorem and the exact two-endpoint
signed-cut bound derived from Jillhewar's local potentials in
`signed_cut_and_explicit_mass_bound.md`. It also uses the elementary invariant
heading minus black mass modulo four.

The remaining proof below is a finite counting argument. No simulation,
unbounded search, invariant-probability existence theorem, or assumed
highway classification enters it. It was derived in this investigation;
external review and novelty have not been established.

## 1. A complete centered finite state never recurs

A centered state consists of the entire finite black set translated so that
the ant is at the origin, together with its heading. Suppose such a state
occurred twice, at times u<v. Let P=v-u and d=p_v-p_u.

Determinism and translation covariance give the same centered state every
P updates thereafter. In particular, black mass at the period boundaries
is constant, and the ant positions there are p_u+n*d.

The two-endpoint cut bound is

    ||p_t-p_s||_infinity <= (M_s+M_t)/2+1.

Applied to the period boundaries, it forces d=0. The complete uncentered
state then repeats, making the future bounded and periodic, contrary to
the unboundedness theorem. This proves the claim.

Consequently a fixed finite collection of complete centered states can be
visited only finitely many times, with at most one visit per state.

## 2. Definition of the maximal occupation count

Let A_K(N) be the largest possible number of states with mass at most K
among N consecutive state observations on any finite-support trajectory.
The maximum is well-defined as an integer in {0,...,N}; allowing a supremum
would give the same value.

For K=0 there is at most one observation. A zero-black centered state has
the heading fixed by the conserved value of heading minus black mass, so
all zero-black occurrences on one orbit would be the same centered state.
Section 1 excludes a second occurrence. Thus

    A_0(N)<=1.

## 3. A finite-radius decomposition

Fix integers K>=1 and R>=1. Call a state of mass at most K central if its
entire black set lies in the square of L-infinity radius R about its ant.

The square contains L=(2R+1)^2 cells. On one orbit the heading is fixed by
the black count and the conserved heading-minus-mass residue. Hence there
are at most

    S_K(R)=sum_(j=0)^K binomial(L,j)

possible complete central centered states on that orbit. By Section 1, the
number of their occurrences in the entire orbit is at most S_K(R).

Now consider any noncentral observation at time a with mass at most K.
Some black cell q is farther than R from the current ant. Delete that one
cell from the time-a state. This is a legal finite-support initial state
with at most K-1 black cells.

The original and modified trajectories agree on all positions, headings,
and all other cell colors for their next R updates. A unit-speed path cannot
read q during those updates. Throughout the next R state observations their
black masses therefore differ by exactly one. Every original observation
with mass at most K is a modified observation with mass at most K-1.
There are at most A_(K-1)(R) such observations in that block.

### Greedy block coverage

Examine an interval of N observations. Start an R-long block at its first
noncentral low-mass observation. Start the next block at the first such
observation not already covered, and continue. These blocks do not overlap;
the last may extend past the interval, which only enlarges an upper bound.
Their start times are at least R apart, so there are at most ceil(N/R)
blocks.

Every noncentral low-mass observation is covered. Every remaining low-mass
observation is central, and there are at most S_K(R) of these in the entire
orbit. Therefore

    A_K(N)<=S_K(R)+ceil(N/R)*A_(K-1)(R).                 (1)

No distant black cell is erased from the actual trajectory. A single cell
is removed only in a comparison trajectory, on a time interval where it
is proved not to be read.

## 4. Quantitative induction

For R>=1, (2R+1)^2<=9R^2. Hence

    S_K(R)<=(K+1)*9^K*R^(2K).                         (2)

Assume A_(K-1)(n)<=C_(K-1)*n^(1-1/D) for all n>=1,
where D=D_(K-1). Put D'=2KD+1=D_K and choose

    R=floor(N^(D/D')).

This is at least one, at most N, and at least half of N^(D/D'). Substituting
(2) and the inductive hypothesis in (1) gives

    A_K(N)
      <= (K+1)*9^K*N^(2KD/D')
         + 2*C_(K-1)*N*R^(-1/D)
      <= [(K+1)*9^K+4*C_(K-1)]*N^(1-1/D').

Here ceil(N/R)<=2N/R, and rounding R costs at most 2^(1/D)<=2.
Since C_(K-1)=2K*9^(K-1),

    (K+1)*9^K+4*C_(K-1)
      = [K+1+8K/9]*9^K
      <= 2(K+1)*9^K=C_K.

The induction starts from A_0(N)<=1<=C_0. This proves the displayed theorem.

## 5. Uniform divergence of mean black mass

Every observation not counted by A_K(N) has at least K+1 black cells. Thus

    (1/N)*sum_(t=s)^(s+N-1) M_t
      >= (K+1)*(1-C_K*N^(-1/D_K)).

In particular, when

    N >= [4(K+1)*9^K]^(D_K),

the mean black mass in every such interval is at least (K+1)/2. This supplies
an explicit uniform rate for the conclusion that mean black mass tends to
infinity. The constants and exponents are conservative.

## Limits

Low-mass visits may still occur infinitely often, provided their density
decays. The argument does not bound nonstandard turn events, the width of
the visited region, or the amount of old information later reused. It does
not prove eventual periodicity or the standard-highway conjecture.
