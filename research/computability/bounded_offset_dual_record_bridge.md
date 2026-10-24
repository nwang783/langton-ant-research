# Finite-state aligned offsets and dual-record certificates

2026-10-23 01:20 UTC. Independently signed as audit GV.
It genuinely permits nonconstant aligned offsets. It remains a sufficient
obstruction for a specified representation, not a finite-seed decision method.

## 1. An offset-transition abstraction

Suppose an actual finite-support ant has an eventual identity

    p(kn+c)=A p(n)+beta(s_n),

where k>=2, A is a nonsingular integer matrix, the states s_n range over a
finite set S, and beta:S->Z^2. The state sequence need not be automatic,
computable independently, or produced by a finite controller. Supply any
finite directed graph whose edges (s,t,e) include every late actual
transition s_n=s,s_(n+1)=t,p(n+1)-p(n)=e.

Choose the primitive integer covector ell and positive integer m satisfying
ell A=m*(0,1), as in dual_record_finite_support_bridge.md. For an edge
(s,t,e), let W(s,t,e) contain ALL length-k axis-alternating geometric words
with endpoint A e+beta(t)-beta(s), including both feasible initial axes.
Empty domains can be discarded because those edges cannot actually occur.
Let M(s,t,e) be the maximum ell-height of a proper prefix, including prefix0,
and set

    C=max_edges [ell beta(s)+M(s,t,e)].

Assume the following strict inequality for each state that could occur at a
sufficiently high north record:

    C < m+ell beta(s).                                      (R)

It is sufficient, but not necessary, to check this for every state. These
maxima are exactly computable by the signed-axis slot formula in the cited
note; no exponential enumeration is needed for the geometric bound.

## 2. The finite local test

At the first coarse arrival at a sufficiently high row Y, all earlier coarse
block starts have height at most Y-1. Every earlier proper fine read has
ell-height at most m(Y-1)+C, strictly less than the current aligned position
A p(n)+beta(s_n), whose ell-height is mY+ell beta(s_n). The finite initial
black support and exceptional early fine history are also below this plane.

After translation of the fine aligned endpoint to0, the half-plane ell x>=0
is therefore pristine white. The incoming fine heading is among final
directions of words on north edges ending at s_n. Coarse freshness forces
east and then south. Thus one necessary local continuation consists of

    incoming word on a north edge (u,s,N),
    an east-edge word from W(s,t,E),
    a south-edge word from W(t,v,S),

where the first item supplies only the possible incoming heading. Test the
last two words chronologically with their shared board, initial white
half-plane ell x>=0 and arbitrary colors below. If every compatible chain
fails, no arbitrarily high north records are possible in this class.

The test includes repeated-read alternation and actual turn directions.
Passing it does not establish a model. Omitting an actual edge invalidates
the obstruction; adding extra edges or lower-half-plane colors is safe.

## 3. Producing records in a mixing-matrix class

If A's lower-left entry is nonzero, the coarse vertical coordinate is
unbounded in absolute value under the bounded-offset identity. Indeed,
bounded y(n), bounded y(kn+c), and bounded beta_y would bound x(n) using
the second row of the identity. That would confine the whole ant to a
finite set, contradicting finite-domain escape.

This supplies high records in at least one of the north and south signs.
To get an unconditional exclusion one must check both the given class and
its global half-turn transform (beta becomes -beta and edge directions
become -e), or prove the class is invariant under that transform. The
inequality (R) is NOT automatically invariant for an arbitrary offset set.
For triangular or diagonal matrices, record existence needs a separate
argument; bounded offsets can invalidate the fixed-offset expansiveness
proof. No unsupported record assumption is hidden here.

## 4. Concrete exclusion beyond fixed offsets

Let A=[[3,2],[2,5]], k=9, and E=(1,0). No finite-support ant can satisfy

    p(9n+c)=A p(n)+d+2 h_n A E

eventually, where d is constant, h_n is ANY bounded integer sequence, and
h_(n+1)=h_n whenever the coarse movement is vertical. No fixed image words,
heading preservation, automatic state sequence, or controller is assumed.

Absorb d by translating the fine copy. The offset is tangent to the dual
plane: ell=(-2,3), ell A E=0, and m=11. Vertical coarse movements have
fine displacement +/-A N. For a horizontal coarse movement e=epsilon E,
the fine displacement is (epsilon+2(h_(n+1)-h_n)) A E. A nine-step
quarter-turn path has at most five horizontal moves, so its x displacement
has absolute value at most5. Since (A E)_x=3 and the multiplier is odd,
that multiplier must be +/-1. Hence every horizontal fine macro has
displacement +/-A E, even when the offset changes.

The complete geometric domains are consequently the same four endpoint
domains as the fixed-offset mixing example. Their proper-prefix dual maxima
are10,7,0,7 for N,E,S,W. Since every offset has dual height0, C=10<11,
and the pristine half-plane argument applies. Every north macro has five
north moves and no south moves, hence ends heading north.

At a coarse north record, the next fine macro may now have displacement
EITHER +A E OR -A E. The following south macro still has displacement A S.
There are20*4+20*4=160 raw pairs. The independently replayable complete
certificate check_bounded_offset_oblique.py/json/records.json rejects all
160, latest conflict at zero-based read15. In the extra negative-east
branch all80 pairs already conflict by read9.

The class is invariant under a global half-turn, with d and h negated, so
Section3 supplies the needed sign of records. The stated finite certificate and the analytic argument have both passed
independent audit.

The vertical-stationarity condition on h is essential to this proof. If
h changes during a north move, a nine-step macro can instead have endpoint
(-4,1), whose raw proper-prefix dual ceiling is14, above the scale11. We
do NOT exclude general bounded tangent offsets, arbitrary state-dependent
offsets, or the accepted standard104 finite-state matrix control.
